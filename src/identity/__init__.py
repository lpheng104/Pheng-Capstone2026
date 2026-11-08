"""C2: resolve identity from a revocable, unexpired database session."""
from datetime import datetime, timezone
import re


def password_valid(password):
    """Registration and password-change policy; AI-assisted 2026-11-08."""
    return (8 <= len(password) <= 128 and re.search('[a-z]', password)
            and re.search('[A-Z]', password) and re.search('[!@#$%]', password))


def resolve_user(store, token):
    if not token:
        return None
    auth = store.one('sessions', {'token': token,
                                 'expires_at': {'$gt': datetime.now(timezone.utc)}})
    return store.one('users', {'_id': auth['user_id']}) if auth else None
