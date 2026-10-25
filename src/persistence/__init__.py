"""C6: real, bounded MongoDB access for the walking-skeleton path."""
from pymongo import MongoClient, timeout


class Store:
    def __init__(self, database):
        self.database = database

    def one(self, collection, query):
        with timeout(5):
            return self.database[collection].find_one(query)

    def many(self, collection, query, sort=None, limit=0):
        with timeout(5):
            cursor = self.database[collection].find(query)
            if sort:
                cursor = cursor.sort(sort)
            if limit:
                cursor = cursor.limit(limit)
            return list(cursor)

    def ping(self):
        with timeout(2):
            return self.database.command('ping')


def connect(uri, name):
    client = MongoClient(uri, serverSelectionTimeoutMS=2000,
                         connectTimeoutMS=2000, timeoutMS=5000,
                         retryReads=False, retryWrites=False, tz_aware=True)
    return client, client[name]


def verify_schema(database):
    from migrations.run import load_manifest
    manifest, digest = load_manifest()
    with timeout(5):
        row = database.schema_migrations.find_one({'_id': manifest['version']})
    if not row or row.get('sha256') != digest:
        raise RuntimeError('Database schema is not ready. Run script/setup before starting.')
