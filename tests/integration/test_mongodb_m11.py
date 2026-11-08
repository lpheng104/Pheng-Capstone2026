"""Real MongoDB 8 integration, explicitly isolated from Atlas."""
from datetime import datetime, timezone
import os
from uuid import uuid4

from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, WriteError
import pytest

from migrations.run import apply, load_manifest
from src.persistence import Store, verify_schema


@pytest.fixture
def live_db():
    port = os.getenv('M11_MONGO_PORT')
    if not port:
        pytest.skip('Set M11_MONGO_PORT to a disposable loopback MongoDB port')
    assert port.isdecimal() and 1 <= int(port) <= 65535
    with MongoClient('127.0.0.1', int(port), serverSelectionTimeoutMS=3000,
                     directConnection=True, tz_aware=True) as client:
        name = 'test_m11_' + uuid4().hex
        db = client[name]
        try:
            assert apply(db, *load_manifest()) == 'APPLIED 0001'
            yield db
        finally:
            client.drop_database(name)


def test_real_migration_ledger_and_validator(live_db):
    assert apply(live_db, *load_manifest()) == 'ALREADY APPLIED 0001'
    verify_schema(live_db)
    with pytest.raises(WriteError) as failure:
        live_db.users.insert_one({'username': 'fictional_incomplete'})
    assert failure.value.code == 121


def test_real_unique_username_survives_duplicate_write(live_db):
    user = {'username':'fictional_unique', 'name':'Synthetic', 'password_hash':uuid4().hex}
    live_db.users.insert_one(user.copy())
    with pytest.raises(DuplicateKeyError):
        live_db.users.insert_one(user.copy())
    assert live_db.users.count_documents({'username': user['username']}) == 1


def test_real_message_read_through_store(live_db, fictional_data):
    unit = ObjectId()
    body = fictional_data['happy']['message']
    live_db.messages.insert_one({'unit_id':unit, 'author_id':ObjectId(),
                                 'author':'fictional', 'body':body,
                                 'created_at':datetime.now(timezone.utc)})
    assert Store(live_db).many('messages', {'unit_id':unit})[0]['body'] == body
    assert Store(live_db).many('messages', {'unit_id':ObjectId()}) == []
