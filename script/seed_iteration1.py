"""AI-assisted 2026-11-01; docs/ai-usage.md. Reset only the dedicated synthetic demo unit/users."""
import json
import os
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv  # noqa: E402
from werkzeug.security import generate_password_hash  # noqa: E402
from src.persistence import connect  # noqa: E402


def seed_demo(db, password):
    if not (db.name.endswith('_skeleton') or db.name.startswith('test_')):
        raise ValueError('Demo seed requires a dedicated *_skeleton or test_* database.')
    data = json.loads((ROOT/'seed/iteration-1.json').read_text())
    for item in data['users']:
        db.users.update_one({'username': item['username']}, {'$set': {
            'name': item['name'], 'password_hash': generate_password_hash(password)}}, upsert=True)
        user = db.users.find_one({'username': item['username']})
        db.sessions.delete_many({'user_id': user['_id']})
        db.login_attempts.delete_many({'_id': item['username']})
    leader = db.users.find_one({'username': 'iteration_leader'})
    db.units.update_one({'name': data['unit']['name']}, {'$set': {
        **data['unit'], 'created_by': leader['_id']}}, upsert=True)
    unit = db.units.find_one({'name': data['unit']['name']})
    for item in data['users']:
        user = db.users.find_one({'username': item['username']})
        key = {'unit_id': unit['_id'], 'user_id': user['_id']}
        if item['role']:
            db.memberships.update_one(key, {'$set': {'role': item['role'], 'rank': 'DEMO'}}, upsert=True)
        else:
            db.memberships.delete_many(key)
    # Reset only this exact synthetic unit, leaving the Week 9 seed intact.
    for old in db.events.find({'unit_id': unit['_id']}):
        db.responses.delete_many({'event_id': old['_id']})
    db.events.delete_many({'unit_id': unit['_id']})
    db.messages.delete_many({'unit_id': unit['_id']})
    for item in data['events']:
        db.events.insert_one({**item, 'starts_at': datetime.fromisoformat(item['starts_at']),
            'unit_id': unit['_id'], 'created_by': leader['_id'], 'uniform': '', 'details': ''})
    return str(unit['_id'])


if __name__ == '__main__':
    load_dotenv(ROOT/'.env')
    client, db = connect(os.environ['MONGODB_URI'], os.environ['MONGODB_DATABASE'])
    try:
        unit = seed_demo(db, os.environ['SKELETON_PASSWORD'])
        print('DEMO SEEDED: /units/'+unit+'; use SKELETON_PASSWORD from your ignored .env.')
    finally:
        client.close()
