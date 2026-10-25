"""Forward-only initial MongoDB migration. Default mode is offline --plan."""
import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = Path(__file__).with_name('0001_initial.json')


def load_manifest():
    raw = MANIFEST.read_bytes()
    # Canonical JSON hash survives Git line-ending conversion.
    manifest = json.loads(raw)
    canonical = json.dumps(manifest, sort_keys=True, separators=(',', ':')).encode()
    return manifest, hashlib.sha256(canonical).hexdigest()


def apply(db, manifest, digest):
    version = manifest['version']
    record = db.schema_migrations.find_one({'_id': version})
    if record:
        if record.get('sha256') != digest:
            raise ValueError('Applied manifest checksum differs; create a new migration.')
        return 'ALREADY APPLIED ' + version
    existing = set(db.list_collection_names())
    allowed = {c['name'] for c in manifest['collections']} | {'schema_migrations'}
    if existing - allowed:
        raise ValueError('Unexpected collections; use an explicit adoption migration.')
    for name in existing:
        if db[name].find_one({}) is not None:
            raise ValueError('Initial migration requires empty unversioned collections.')
    # Caller must stop web writes and ensure a single migration process.
    for collection in manifest['collections']:
        name = collection['name']
        options = {'validator': collection['validator'], 'validationLevel': 'strict', 'validationAction': 'error'}
        if name in existing:
            db.command('collMod', name, **options)
        else:
            db.create_collection(name, **options)
        for index in collection['indexes']:
            db[name].create_index([tuple(key) for key in index['keys']],
                                  **{key: value for key, value in index.items() if key != 'keys'})
    ledger_validator = {'$jsonSchema': {'bsonType': 'object', 'additionalProperties': False,
        'required': ['_id', 'sha256', 'applied_at'], 'properties': {
            '_id': {'bsonType': 'string', 'pattern': '^[0-9]{4}$'},
            'sha256': {'bsonType': 'string', 'pattern': '^[a-f0-9]{64}$'},
            'applied_at': {'bsonType': 'date'}}}}
    if 'schema_migrations' in existing:
        db.command('collMod', 'schema_migrations', validator=ledger_validator,
                   validationLevel='strict', validationAction='error')
    else:
        db.create_collection('schema_migrations', validator=ledger_validator,
                             validationLevel='strict', validationAction='error')
    db.schema_migrations.insert_one({'_id': version, 'sha256': digest, 'applied_at': datetime.now(timezone.utc)})
    return 'APPLIED ' + version


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--plan', action='store_true')
    mode.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    manifest, digest = load_manifest()
    if not args.apply:
        print(f"PLAN {manifest['version']}: {len(manifest['collections'])} collections")
        print('No connection made. SHA-256 ' + digest)
        return 0
    uri, name = os.getenv('MONGODB_URI'), os.getenv('MONGODB_DATABASE')
    if not uri or not name or not re.fullmatch(r'[A-Za-z0-9_-]{1,38}', name) or name in {'admin', 'local', 'config'}:
        print('ERROR: set URI and a non-system database name in the environment.')
        return 1
    try:
        from pymongo import MongoClient, timeout
        # Avoid logging exceptions/URI; SRV resolution occurs during construction.
        with MongoClient(uri, serverSelectionTimeoutMS=2000, connectTimeoutMS=2000,
                         timeoutMS=5000, retryReads=False, retryWrites=False, tz_aware=True) as client:
            with timeout(60):
                print(apply(client[name], manifest, digest))
    except Exception as error:
        print('ERROR: migration incomplete (' + type(error).__name__ + '). Inspect target state before retrying.')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
