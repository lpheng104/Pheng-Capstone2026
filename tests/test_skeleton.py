"""Meaningful service regressions; live integration is verified by script/smoke."""
from datetime import datetime, timezone

import mongomock
import pytest
from bson import ObjectId

from src.identity import resolve_user
from src.messaging import latest_messages
from src.persistence import Store
from src.unit_access import AccessDenied


def test_message_window_is_stable_and_does_not_allow_cross_unit_reads():
    db = mongomock.MongoClient(tz_aware=True).test
    user, unit = ObjectId(), ObjectId()
    db.units.insert_one({'_id':unit})
    db.memberships.insert_one({'unit_id':unit,'user_id':user,'role':'member'})
    timestamp = datetime(2030,1,1,tzinfo=timezone.utc)
    ids = [ObjectId() for _ in range(101)]
    for key in ids:
        db.messages.insert_one({'_id':key,'unit_id':unit,'created_at':timestamp,'body':str(key)})
    rows = latest_messages(Store(db),str(unit),user)
    assert [r['_id'] for r in rows] == sorted(ids)[-100:]
    with pytest.raises(AccessDenied):
        latest_messages(Store(db),str(unit),ObjectId())


def test_expired_session_is_denied_even_before_ttl_cleanup():
    db = mongomock.MongoClient(tz_aware=True).test
    user = ObjectId()
    db.users.insert_one({'_id':user})
    db.sessions.insert_one({'token':'expired','user_id':user,
                            'expires_at':datetime(2000,1,1,tzinfo=timezone.utc)})
    assert resolve_user(Store(db),'expired') is None
    assert db.sessions.count_documents({}) == 1
