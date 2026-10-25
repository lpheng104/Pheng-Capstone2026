"""C4: authorize and return a stable latest-message window."""
from src.unit_access import authorized_unit


def latest_messages(store, unit_id, user_id):
    unit, _ = authorized_unit(store, unit_id, user_id)
    latest = store.many('messages', {'unit_id': unit['_id']},
                        [('created_at', -1), ('_id', -1)], limit=100)
    return latest[::-1]
