"""Milestone 11 disposable test fixtures; never load application database settings."""
from pathlib import Path
import json
import secrets
from uuid import uuid4

import mongomock
import pytest
from werkzeug.security import generate_password_hash

from src.app import create_app


@pytest.fixture(scope='session')
def fictional_data():
    folder = Path(__file__).parent / 'data'
    return {name: json.loads((folder / f'{name}.json').read_text(encoding='utf-8'))
            for name in ('happy', 'boundary', 'hostile')}


@pytest.fixture
def qa(fictional_data, monkeypatch):
    monkeypatch.setattr('src.app.load_dotenv', lambda: None)
    db = mongomock.MongoClient(tz_aware=True).test_m11
    password = 'Qa!' + secrets.token_urlsafe(12)
    setup_token = secrets.token_urlsafe(16)
    app = create_app({'TESTING': True, 'SECRET_KEY': uuid4().hex,
                      'ADMIN_USERNAME': 'qa_owner', 'ADMIN_SETUP_TOKEN': setup_token}, db)
    people = {}
    clients = {}
    # One hash per fixture avoids repeated expensive fixture setup while exercising real login checks.
    password_hash = generate_password_hash(password)
    for role in ('owner', 'member', 'outsider'):
        username = 'qa_' + role
        people[role] = db.users.insert_one({'username': username, 'name': 'Fictional '+role,
                                            'password_hash': password_hash}).inserted_id
        clients[role] = app.test_client()
    unit = db.units.insert_one({'name': fictional_data['happy']['unit'], 'echelon': 'Squad',
                                'created_by': people['owner']}).inserted_id
    for role in ('owner', 'member'):
        db.memberships.insert_one({'unit_id': unit, 'user_id': people[role], 'role': role, 'rank': ''})
    for role, client in clients.items():
        assert submit(client, '/login', username='qa_'+role, password=password).status_code == 302
    return app, db, clients, people, unit, password


def submit(client, path, **values):
    client.get('/login')
    with client.session_transaction() as session:
        csrf = session['csrf']
    return client.post(path, data={'csrf': csrf, **values}, follow_redirects=False)
