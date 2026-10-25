"""C7: idempotently seed one synthetic workflow in a dedicated demo database."""
from datetime import datetime, timezone

from werkzeug.security import generate_password_hash


def seed(database, password):
    # Refuse to seed an arbitrary application database by accident.
    if not (database.name.endswith('_skeleton') or database.name.startswith('test_')):
        raise ValueError('Seeding requires a *_skeleton or test_* database.')
    username = 'skeleton_member'
    database.users.update_one({'username': username}, {'$setOnInsert': {
        'username': username, 'name': 'Synthetic Member',
        'password_hash': generate_password_hash(password)}}, upsert=True)
    user = database.users.find_one({'username': username})
    database.units.update_one({'name': 'Skeleton Demo Unit'}, {'$setOnInsert': {
        'name': 'Skeleton Demo Unit', 'echelon': 'Squad', 'created_by': user['_id']}}, upsert=True)
    unit = database.units.find_one({'name': 'Skeleton Demo Unit'})
    database.memberships.update_one({'unit_id': unit['_id'], 'user_id': user['_id']},
        {'$setOnInsert': {'role': 'owner', 'rank': 'DEMO'}}, upsert=True)
    now = datetime.now(timezone.utc)
    database.messages.update_one({'unit_id': unit['_id'], 'body': 'Skeleton database row'},
        {'$setOnInsert': {'author_id': user['_id'], 'author': user['name'],
                          'created_at': now}}, upsert=True)
    database.events.update_one({'unit_id': unit['_id'], 'title': 'Synthetic Formation'},
        {'$setOnInsert': {'starts_at': datetime(2030, 1, 1, tzinfo=timezone.utc),
                          'location': 'Demo Field', 'uniform': '', 'details': '',
                          'created_by': user['_id']}}, upsert=True)
    event = database.events.find_one({'unit_id': unit['_id'], 'title': 'Synthetic Formation'})
    database.responses.update_one({'event_id': event['_id'], 'user_id': user['_id']},
                                   {'$setOnInsert': {'status': 'attending'}}, upsert=True)
    return str(unit['_id'])
