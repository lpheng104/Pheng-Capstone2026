# AI-generated 2026-09-17; see docs/ai-usage.md.
import mongomock
import pytest
from src.app import create_app

@pytest.fixture
def setup():
    db = mongomock.MongoClient(tz_aware=True).test
    app = create_app({'TESTING': True, 'SECRET_KEY': 'test-only', 'ADMIN_USERNAME': 'admin', 'ADMIN_SETUP_TOKEN': 'test-setup'}, db)
    return app, db

def post(client, path, data=None):
    client.get('/login')
    with client.session_transaction() as s:
        token = s['csrf']
    return client.post(path, data={**(data or {}), 'csrf': token})

def register(client, username):
    return post(client, '/register', {'username': username, 'name': username, 'password': 'Strong!Pass1', 'setup_token': 'test-setup'})

def login(client, username):
    return post(client, '/login', {'username': username, 'password': 'Strong!Pass1', 'setup_token': 'test-setup'})

def test_accounts_csrf_and_revoked_logout(setup):
    app, db = setup
    c = app.test_client()
    assert c.post('/register', data={}).status_code == 400
    post(c, '/register', {'username': 'admin', 'name': 'Admin', 'password': 'Strong!Pass1'})
    assert db.users.count_documents({}) == 0
    register(c, 'admin')
    register(c, 'ADMIN')
    assert db.users.count_documents({}) == 1
    assert 'Strong!Pass1' not in db.users.find_one()['password_hash']
    login(c, 'admin')
    assert c.get('/').status_code == 200
    with c.session_transaction() as s:
        old = dict(s)
    post(c, '/logout')
    with c.session_transaction() as s:
        s.update(old)
    assert c.get('/').status_code == 302

def test_unit_permissions_chat_and_attendance(setup):
    app, db = setup
    owner, member, outsider = [app.test_client() for _ in range(3)]
    for c, name in [(owner, 'admin'), (member, 'soldier'), (outsider, 'outsider')]:
        register(c, name)
        login(c, name)
    assert post(member, '/units', {'name': 'Bad', 'echelon': 'Squad'}).status_code == 403
    post(owner, '/units', {'name': 'Alpha', 'echelon': 'Squad'})
    unit = str(db.units.find_one()['_id'])
    base = '/units/' + unit
    assert outsider.get(base).status_code == 403
    assert post(outsider, base + '/messages', {'body': 'no'}).status_code == 403
    post(owner, base + '/members', {'username': 'soldier'})
    assert member.get(base).status_code == 200
    post(member, base + '/messages', {'body': '<script>alert(1)</script>'})
    assert b'&lt;script&gt;' in member.get(base).data
    data = {'title': 'PT', 'starts_at': '2026-10-01T06:00-05:00', 'location': 'Field', 'uniform': 'PT', 'details': ''}
    assert post(member, base + '/events', data).status_code == 403
    assert post(owner, base + '/events', {**data, 'starts_at': '2026-10-01T06:00'}).status_code == 400
    post(owner, base + '/events', data)
    event = str(db.events.find_one()['_id'])
    path = base + '/events/' + event + '/respond'
    assert post(outsider, path, {'status': 'attending'}).status_code == 403
    post(member, path, {'status': 'attending'})
    post(member, path, {'status': 'not attending'})
    assert db.responses.count_documents({}) == 1
    assert db.responses.find_one()['status'] == 'not attending'
    assert b'not attending' in owner.get(base).data
    soldier = str(db.users.find_one({'username': 'soldier'})['_id'])
    assert post(member, base + '/members/' + soldier, {'role': 'leader', 'rank': 'SGT'}).status_code == 403
    post(owner, base + '/members/' + soldier, {'role': 'leader', 'rank': 'SGT'})
    assert post(member, base + '/events', data).status_code == 302
    assert owner.get('/units/bad-id').status_code == 404

def test_login_throttle_and_weak_password(setup):
    app, db = setup
    c = app.test_client()
    post(c, '/register', {'username': 'weak', 'name': 'Weak', 'password': 'weak'})
    assert db.users.count_documents({}) == 0
    for _ in range(10):
        assert post(c, '/login', {'username': 'nobody', 'password': 'bad'}).status_code == 200
    assert post(c, '/login', {'username': 'nobody', 'password': 'bad'}).status_code == 429
