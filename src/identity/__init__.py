"""C2: resolve identity from a revocable, unexpired database session."""
from datetime import datetime, timezone


def resolve_user(store, token):
    if not token:
        return None
    auth = store.one('sessions', {'token': token,
                                 'expires_at': {'$gt': datetime.now(timezone.utc)}})
    return store.one('users', {'_id': auth['user_id']}) if auth else None
