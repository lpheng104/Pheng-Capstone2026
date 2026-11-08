"""SRS-derived candidate criteria. Known gaps remain visible as strict expected failures."""
from datetime import datetime, timezone

from bson import ObjectId
import pytest
from werkzeug.security import check_password_hash

from conftest import submit


FIXED = {
    'FR-ACCT-01-AC2': 'DEF-M11-01', 'FR-ACCT-06-AC2': 'DEF-M11-01',
    'FR-ACCT-02-AC2': 'DEF-M11-02', 'FR-UNIT-01-AC4': 'DEF-M11-03',
    'FR-UNIT-02-AC3': 'DEF-M11-04', 'FR-CLNDR-02-AC4': 'DEF-M11-08',
}
KNOWN = {
    'FR-UNIT-03-AC1': 'DEF-M11-05',
    'FR-CHAT-01-AC1': 'DEF-M11-06', 'FR-CLNDR-01-AC1': 'DEF-M11-07',
    'FR-RANK-02-AC2': 'DEF-M11-09',
}


class KnownGap(AssertionError):
    """Only the exact recorded baseline symptom is accepted as an expected failure."""


def expected_text(response, wanted, baseline=None):
    if wanted not in response.data and baseline is not None and baseline in response.data:
        raise KnownGap(wanted.decode())
    assert wanted in response.data


def missing_control(app, response, label, possible_endpoints):
    if label not in response.data and not any(
        endpoint in rule.endpoint for rule in app.url_map.iter_rules() for endpoint in possible_endpoints
    ):
        raise KnownGap(label.decode())
    assert label in response.data


CASES = [
    'FR-ACCT-01-AC1', 'FR-ACCT-01-AC2', 'FR-ACCT-02-AC1', 'FR-ACCT-02-AC2',
    'FR-ACCT-04-AC1', 'FR-ACCT-04-AC2', 'FR-ACCT-04-AC3', 'FR-ACCT-04-AC4',
    'FR-ACCT-05-AC1', 'FR-ACCT-05-AC2', 'FR-ACCT-06-AC1', 'FR-ACCT-06-AC2',
    'FR-UNIT-01-AC1', 'FR-UNIT-01-AC4', 'FR-UNIT-02-AC2', 'FR-UNIT-02-AC3',
    'FR-UNIT-03-AC1', 'FR-CHAT-01-AC1', 'FR-CHAT-04-AC3', 'FR-CHAT-04-AC4',
    'FR-CHAT-05-AC1', 'FR-CHAT-05-AC2', 'FR-CHAT-05-AC5',
    'FR-CLNDR-01-AC1', 'FR-CLNDR-02-AC2', 'FR-CLNDR-02-AC4',
    'FR-CLNDR-02-AC5', 'FR-RANK-01-AC3', 'FR-RANK-02-AC2', 'FR-RANK-05-AC3',
]


@pytest.mark.parametrize('case', [
    pytest.param(case, id=case, marks=pytest.mark.xfail(
        strict=True, raises=KnownGap, reason=KNOWN[case])) if case in KNOWN else pytest.param(case, id=case)
    for case in CASES
])
def test_written_criterion(qa, fictional_data, case):
    app, db, clients, people, unit, password = qa
    owner, member, outsider = (clients[k] for k in ('owner', 'member', 'outsider'))
    base = '/units/' + str(unit)
    event = fictional_data['happy']['event']
    requirement, ac = case.rsplit('-', 1)
    if requirement in ('FR-ACCT-01', 'FR-ACCT-02', 'FR-ACCT-06'):
        visitor = app.test_client()
        assert b'name="username"' in visitor.get('/register').data
        if ac == 'AC1':
            assert submit(visitor, '/register', username='qa_new', name="Fictional O'Example",
                          password=password).status_code == 302
            row = db.users.find_one({'username':'qa_new'})
            assert row and check_password_hash(row['password_hash'], password)
        elif requirement == 'FR-ACCT-02':
            response = submit(visitor, '/register', username='qa_new', name='Fictional', password='weak')
            assert db.users.find_one({'username':'qa_new'}) is None
            expected_text(response, b'Password does not meet the secure requirements', b'Password needs')
        else:
            response = submit(visitor, '/register', username='qa_member', name='Fictional', password=password)
            assert db.users.count_documents({'username':'qa_member'}) == 1
            expected_text(response, b'username already is in use', b'Username already in use.')
    elif requirement == 'FR-ACCT-04':
        visitor = app.test_client()
        username = 'qa_member' if ac in ('AC1', 'AC4') else 'qa_nonexistent'
        response = submit(visitor, '/login', username=username, password=password if ac in ('AC1','AC3') else 'wrong')
        if ac == 'AC1':
            assert response.status_code == 302 and visitor.get(base).status_code == 200
        else:
            assert b'Invalid username or password.' in response.data and visitor.get('/').status_code == 302
    elif requirement == 'FR-ACCT-05':
        with member.session_transaction() as session:
            token = session['auth_token']
        assert submit(member, '/logout').location.endswith('/login')
        if ac == 'AC1':
            assert db.sessions.find_one({'token':token}) is None
        else:
            assert member.get(base).location.endswith('/login')
            assert submit(member, base+'/messages', body='denied').location.endswith('/login')
            assert db.messages.count_documents({}) == 0
    elif requirement == 'FR-UNIT-01':
        response = submit(owner, '/units', name='Second unit' if ac == 'AC1' else '', echelon='Squad')
        if ac == 'AC1':
            assert response.status_code == 302 and db.units.find_one({'name':'Second unit'})
        else:
            assert db.units.count_documents({}) == 1
            expected_text(response, b'No unit name entered creation request cancelled', b'name is required')
    elif requirement == 'FR-UNIT-02':
        if ac == 'AC2':
            assert outsider.get(base).status_code == 403
            assert submit(owner, base+'/members', username='qa_outsider').status_code == 302
            page = outsider.get(base)
            assert page.status_code == 200 and b'Unit chat' in page.data and b'Events' in page.data
        else:
            submit(owner, base+'/members', username=fictional_data['hostile']['unknown_user'])
            assert db.memberships.count_documents({'unit_id':unit}) == 2
            expected_text(owner.get(base), b'Invalid user, add user request cancelled', b'That user must register first.')
    elif requirement == 'FR-UNIT-03':
        missing_control(app, owner.get(base), b'Remove member', ('remove_member', 'remove_user'))
    elif requirement == 'FR-CHAT-01':
        missing_control(app, owner.get(base), b'Create group chat', ('create_chat', 'create_group'))
    elif requirement == 'FR-CLNDR-01':
        missing_control(app, owner.get(base), b'Add calendar', ('add_calendar', 'create_calendar'))
    elif requirement == 'FR-CHAT-04':
        client = member if ac == 'AC3' else outsider
        response = submit(client, base+'/messages', body='  ' if ac == 'AC3' else 'denied')
        assert db.messages.count_documents({}) == 0
        if ac == 'AC3':
            assert b'Message cannot be empty.' in member.get(base).data
        else:
            assert response.status_code == 403
    elif requirement == 'FR-CHAT-05':
        message = fictional_data['happy']['message']
        assert submit(member, base+'/messages', body=message).status_code == 302
        if ac == 'AC1':
            assert message.encode() in owner.get(base).data
        elif ac == 'AC2':
            assert db.messages.find_one({'unit_id':unit, 'body':message})
        else:
            assert outsider.get(base).status_code == 403
    elif requirement == 'FR-CLNDR-02':
        response = submit(owner if ac != 'AC5' else member, base+'/events',
                          **(event if ac != 'AC4' else {**event, 'title':''}))
        if ac == 'AC2':
            row = db.events.find_one({'unit_id':unit})
            assert response.status_code == 302 and row['starts_at'] == datetime(2030,1,2,12,tzinfo=timezone.utc)
            assert event['title'].encode() in member.get(base).data
        elif ac == 'AC4':
            assert db.events.count_documents({}) == 0
            expected_text(response, b'Required event information missing, add calendar event request cancelled.',
                          b'title is required')
        else:
            assert response.status_code == 403 and db.events.count_documents({}) == 0
    elif requirement in ('FR-RANK-01', 'FR-RANK-05'):
        response = submit(owner if ac == 'AC3' and requirement == 'FR-RANK-01' else member,
                          base+'/members/'+str(people['member']), role='leader', rank='SGT')
        if requirement == 'FR-RANK-01':
            assert response.status_code == 302
            assert db.memberships.find_one({'unit_id':unit,'user_id':people['member']})['role'] == 'leader'
        else:
            assert response.status_code == 403
            assert db.memberships.find_one({'unit_id':unit,'user_id':people['member']})['role'] == 'member'
    elif requirement == 'FR-RANK-02':
        page = owner.get(base)
        if b'<input name="rank"' in page.data and b'<select name="rank"' not in page.data:
            raise KnownGap('Rank entry is free text rather than a list of available ranks')
        assert b'<select name="rank"' in page.data
    else:
        raise AssertionError('Unimplemented test case: '+case)


def test_nfr_sec_02_every_post_missing_or_modified_csrf(qa):
    app, db, clients, people, unit, _ = qa
    owner = clients['owner']
    ids = {'<unit_id>':str(unit), '<user_id>':str(people['member']), '<event_id>':str(ObjectId())}
    paths = []
    for rule in app.url_map.iter_rules():
        if 'POST' in rule.methods:
            path = rule.rule
            for key, value in ids.items():
                path = path.replace(key, value)
            paths.append(path)
    assert len(paths) >= 10 and all('<' not in path for path in paths)
    snapshot = {name:list(db[name].find()) for name in db.list_collection_names()}
    for path in paths:
        for payload in ({}, {'csrf':'invalid-token'}):
            assert owner.post(path, data=payload).status_code == 400, path
    assert {name:list(db[name].find()) for name in db.list_collection_names()} == snapshot


@pytest.mark.parametrize('index,valid', [(0, False), (1, True), (2, False), (3, False)])
def test_event_date_boundaries(qa, fictional_data, index, valid):
    _, db, clients, _, unit, _ = qa
    event = {**fictional_data['happy']['event'], 'starts_at':fictional_data['boundary']['dates'][index]}
    response = submit(clients['owner'], f'/units/{unit}/events', **event)
    assert response.status_code == (302 if valid else 400)
    assert db.events.count_documents({}) == int(valid)


def test_chat_message_size_boundaries(qa, fictional_data):
    _, db, clients, _, unit, _ = qa
    member = clients['member']
    path = f'/units/{unit}/messages'
    for size in fictional_data['boundary']['message_lengths']:
        before = db.messages.count_documents({})
        assert submit(member, path, body='x'*size).status_code == 302
        after = db.messages.count_documents({})
        assert after-before == int(1 <= size <= 2000), size


def test_hostile_markup_is_rendered_as_text(qa, fictional_data):
    _, db, clients, _, unit, _ = qa
    markup = fictional_data['hostile']['markup']
    base = f'/units/{unit}'
    assert submit(clients['member'], base+'/messages', body=markup).status_code == 302
    assert db.messages.find_one({'unit_id':unit})['body'] == markup
    page = clients['owner'].get(base)
    assert markup.encode() not in page.data
    assert b'&lt;script&gt;alert(1)&lt;/script&gt;' in page.data
