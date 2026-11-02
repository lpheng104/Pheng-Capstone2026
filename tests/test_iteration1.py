"""AI-assisted 2026-11-01; docs/ai-usage.md. Tests map to verbatim SRS criteria."""
from datetime import datetime, timezone

from bson import ObjectId
import mongomock
import pytest
from werkzeug.security import check_password_hash

from src.app import create_app


@pytest.fixture
def world():
    db = mongomock.MongoClient(tz_aware=True).test_iteration1
    app = create_app({'TESTING': True, 'SECRET_KEY': 'fixture-only',
                      'ADMIN_USERNAME': 'leader', 'ADMIN_SETUP_TOKEN': 'fixture-only'}, db)
    clients = {}
    for username in ['leader', 'member', 'outsider']:
        c = app.test_client()
        post(c, '/register', {'username': username, 'name': 'Fictional '+username,
                             'password': 'Original!Pass1', 'setup_token': 'fixture-only'})
        post(c, '/login', {'username': username, 'password': 'Original!Pass1'})
        clients[username] = c
    post(clients['leader'], '/units', {'name': 'Iteration Squad', 'echelon': 'Squad'})
    unit = db.units.find_one()
    base = '/units/'+str(unit['_id'])
    post(clients['leader'], base+'/members', {'username': 'member'})
    return app, db, clients, base


def post(client, path, data=None, follow=False):
    client.get('/login')
    with client.session_transaction() as s:
        csrf = s['csrf']
    return client.post(path, data={**(data or {}), 'csrf': csrf}, follow_redirects=follow)


def test_password_change_ac1_persists_hash_revokes_all_sessions_and_reauthenticates(world):
    app, db, clients, _ = world
    c = clients['member']
    second = app.test_client()
    post(second, '/login', {'username': 'member', 'password': 'Original!Pass1'})
    assert b'New password' in c.get('/account/password').data
    r = post(c, '/account/password', {'current_password': 'Original!Pass1',
                                    'new_password': 'Replacement!Pass2'}, True)
    assert b'Password changed. Please sign in again.' in r.data
    user = db.users.find_one({'username': 'member'})
    assert check_password_hash(user['password_hash'], 'Replacement!Pass2')
    assert not check_password_hash(user['password_hash'], 'Original!Pass1')
    assert db.sessions.count_documents({'user_id': user['_id']}) == 0
    assert second.get('/').status_code == 302
    assert b'Invalid username or password.' in post(c, '/login', {'username': 'member', 'password': 'Original!Pass1'}, True).data
    post(c, '/login', {'username': 'member', 'password': 'Replacement!Pass2'})
    assert c.get('/').status_code == 200


@pytest.mark.parametrize('password', ['weak', 'NOLOWER!', 'noupper!', 'NoSpecial1', 'A!a', 'Aa!'+'x'*126])
def test_password_change_ac2_invalid_password_never_overwrites(world, password):
    _, db, clients, _ = world
    old = db.users.find_one({'username': 'member'})['password_hash']
    r = post(clients['member'], '/account/password',
             {'current_password': 'Original!Pass1', 'new_password': password}, True)
    assert b'Password does not meet the secure requirements' in r.data
    assert db.users.find_one({'username': 'member'})['password_hash'] == old


def test_password_change_denies_anonymous_wrong_current_and_csrf(world):
    app, db, clients, _ = world
    assert app.test_client().get('/account/password').status_code == 302
    c = clients['member']
    assert c.post('/account/password', data={}).status_code == 400
    old = db.users.find_one({'username': 'member'})['password_hash']
    assert b'Current password is incorrect.' in post(c, '/account/password',
        {'current_password': 'wrong', 'new_password': 'Replacement!Pass2'}, True).data
    assert db.users.find_one({'username': 'member'})['password_hash'] == old


def test_chat_ac1_ac2_ac5_persists_username_time_and_is_visible_to_members(world):
    _, db, clients, base = world
    before = datetime.now(timezone.utc)
    post(clients['member'], base+'/messages', {'body': 'Meet at Demo Field at 0600.'})
    row = db.messages.find_one()
    assert row['body'] == 'Meet at Demo Field at 0600.'
    assert row['author'] == 'member'  # Username, not the display name.
    assert before <= row['created_at'] <= datetime.now(timezone.utc)
    for role in ['member', 'leader']:
        page = clients[role].get(base).data
        assert b'Meet at Demo Field at 0600.' in page
        assert b'<strong>member</strong>' in page
        assert row['created_at'].strftime('%b %d, %H:%M UTC').encode() in page


@pytest.mark.parametrize('body', ['', '   ', '\n\t'])
def test_chat_ac3_exact_empty_message_error_no_write(world, body):
    _, db, clients, base = world
    r = post(clients['member'], base+'/messages', {'body': body}, True)
    assert b'Message cannot be empty.' in r.data
    assert db.messages.count_documents({}) == 0


def test_chat_ac4_authorization_csrf_boundary_and_escaping(world):
    app, db, clients, base = world
    assert post(clients['outsider'], base+'/messages', {'body': 'denied'}).status_code == 403
    assert post(app.test_client(), base+'/messages', {'body': 'denied'}).status_code == 302
    assert clients['member'].post(base+'/messages', data={'body': 'denied'}).status_code == 400
    post(clients['member'], base+'/messages', {'body': 'x'*2001})
    assert db.messages.count_documents({}) == 0
    post(clients['member'], base+'/messages', {'body': 'x'*2000})
    assert len(db.messages.find_one()['body']) == 2000
    post(clients['member'], base+'/messages', {'body': '<script>alert(1)</script>'})
    assert b'&lt;script&gt;alert(1)&lt;/script&gt;' in clients['leader'].get(base).data


def event(world):
    _, db, clients, base = world
    post(clients['leader'], base+'/events', {'title': 'Practice briefing',
        'starts_at': '2030-01-01T06:00-06:00', 'location': 'Demo Field'})
    return db.events.find_one()


def test_delete_event_ac1_ac2_selection_confirmation_and_persistence(world):
    _, db, clients, base = world
    row = event(world)
    path = base+'/events/'+str(row['_id'])+'/delete'
    db.responses.insert_one({'event_id': row['_id'], 'user_id': ObjectId(), 'status': 'attending'})
    assert b'Delete event: Practice briefing' in clients['leader'].get(base).data
    assert b'Confirm delete event' in clients['leader'].get(path).data
    assert db.events.count_documents({}) == 1  # GET/cancel cannot delete.
    r = post(clients['leader'], path, follow=True)
    assert b'Calendar event deleted.' in r.data
    assert b'Practice briefing' not in r.data
    assert db.events.count_documents({}) == db.responses.count_documents({}) == 0


@pytest.mark.parametrize('identifier', ['not-an-id', str(ObjectId())])
def test_delete_event_ac3_exact_invalid_event_error(world, identifier):
    _, _, clients, base = world
    r = post(clients['leader'], base+'/events/'+identifier+'/delete', follow=True)
    assert b'Invalid event, delete calendar event request cancelled.' in r.data


def test_delete_event_ac4_ac5_cross_unit_member_and_csrf_denied(world):
    _, db, clients, base = world
    row = event(world)
    path = base+'/events/'+str(row['_id'])+'/delete'
    for role in ['member', 'outsider']:
        assert clients[role].get(path).status_code == 403
        assert post(clients[role], path).status_code == 403
    assert clients['leader'].post(path, data={}).status_code == 400
    other = db.units.insert_one({'name': 'Other', 'echelon': 'Squad'}).inserted_id
    leader = db.users.find_one({'username': 'leader'})
    db.memberships.insert_one({'unit_id': other, 'user_id': leader['_id'], 'role': 'leader', 'rank': ''})
    r = post(clients['leader'], '/units/'+str(other)+'/events/'+str(row['_id'])+'/delete', follow=True)
    assert b'Invalid event, delete calendar event request cancelled.' in r.data
    assert db.events.count_documents({}) == 1
