"""C3: enforce unit membership before returning protected data."""
from bson import ObjectId


class UnitNotFound(Exception):
    pass


class AccessDenied(Exception):
    pass


def authorized_unit(store, unit_id, user_id):
    if not ObjectId.is_valid(unit_id):
        raise UnitNotFound()
    unit = store.one('units', {'_id': ObjectId(unit_id)})
    if not unit:
        raise UnitNotFound()
    member = store.one('memberships', {'unit_id': unit['_id'], 'user_id': user_id})
    if not member:
        raise AccessDenied()
    return unit, member


def roster(store, unit_id, user_id):
    unit, member = authorized_unit(store, unit_id, user_id)
    members = store.many('memberships', {'unit_id': unit['_id']})
    for row in members:
        row['user'] = store.one('users', {'_id': row['user_id']})
    return unit, member, members
