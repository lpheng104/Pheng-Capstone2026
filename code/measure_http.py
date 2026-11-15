"""Measure a fresh local HTTP server and disposable, realistic MongoDB fixture."""
import argparse
from datetime import datetime, timedelta, timezone
from http.cookiejar import CookieJar
import json
from math import ceil
import os
from pathlib import Path
import re
import secrets
import statistics
import subprocess
import sys
import time
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener
from uuid import uuid4

from pymongo import MongoClient
from werkzeug.security import generate_password_hash

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from migrations.run import apply, load_manifest  # noqa: E402


def seed(db, password):
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    hashed = generate_password_hash(password)
    users = db.users.insert_many([
        {'username': f'fixture_{i}', 'name': f'Fictional Member {i}', 'password_hash': hashed}
        for i in range(50)]).inserted_ids
    unit = db.units.insert_one({'name': 'Synthetic QA Unit', 'echelon': 'Squad', 'created_by': users[0]}).inserted_id
    db.memberships.insert_many([{'unit_id': unit, 'user_id': user, 'rank': '',
                                 'role': 'member' if i else 'owner'} for i, user in enumerate(users)])
    db.messages.insert_many([{'unit_id': unit, 'body': f'Synthetic notice {i}: rehearsal at the demo field.',
                              'author': 'fixture_0', 'author_id': users[0],
                              'created_at': now+timedelta(seconds=i)} for i in range(100)])
    events = db.events.insert_many([{'unit_id': unit, 'title': f'Synthetic Event {i}',
                                    'starts_at': now+timedelta(days=i), 'location': 'Demo field',
                                    'uniform': '', 'details': 'Fictional rehearsal.', 'created_by': users[0]}
                                   for i in range(25)]).inserted_ids
    db.responses.insert_many([{'event_id': event, 'user_id': user, 'status': 'attending'}
                              for event in events for user in users[::2]])
    return unit


def run(source, mongo_port, port, requests):
    uri = f'mongodb://127.0.0.1:{mongo_port}/?directConnection=true'
    name = 'test_m12_' + uuid4().hex
    password = 'Qa!' + secrets.token_urlsafe(20)
    base = f'http://127.0.0.1:{port}'
    browser = build_opener(HTTPCookieProcessor(CookieJar()))
    with MongoClient(uri, serverSelectionTimeoutMS=3000, tz_aware=True) as client:
        db = client[name]
        process = None
        try:
            apply(db, *load_manifest())
            unit = seed(db, password)
            env = {**os.environ, 'SECRET_KEY': secrets.token_hex(32), 'COOKIE_SECURE': 'false',
                   'MONGODB_URI': uri, 'MONGODB_DATABASE': name, 'ADMIN_USERNAME': '',
                   'ADMIN_SETUP_TOKEN': ''}
            process = subprocess.Popen([sys.executable, 'script/manage.py', 'start', '--port', str(port)],
                                       cwd=source, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            for _ in range(40):
                if process.poll() is not None:
                    raise RuntimeError('Fresh benchmark server exited')
                try:
                    with browser.open(base+'/health', timeout=1) as response:
                        if json.load(response) == {'status': 'ok'}:
                            break
                except OSError:
                    time.sleep(.25)
            else:
                raise RuntimeError('Benchmark health unavailable')
            with browser.open(base+'/login', timeout=10) as response:
                csrf = re.search(rb'name="csrf" value="([^"]+)"', response.read())[1].decode()
            data = urlencode({'csrf': csrf, 'username': 'fixture_0', 'password': password}).encode()
            with browser.open(base+'/login', data=data, timeout=10) as response:
                assert response.geturl().rstrip('/') == base
            sizes, clocks = [], []
            for i in range(requests+1):
                start = time.perf_counter()
                with browser.open(f'{base}/units/{unit}', timeout=10) as response:
                    page = response.read()
                    assert response.status == 200
                elapsed = (time.perf_counter()-start)*1000
                assert b'Synthetic notice 99' in page and b'Synthetic Event 24' in page
                if i:
                    clocks.append(round(elapsed, 3))
                    sizes.append(len(page))
            return {'samples_ms': clocks, 'p50_ms': statistics.median(clocks),
                    'p95_ms': sorted(clocks)[ceil(.95*requests)-1], 'body_bytes': sizes,
                    'p50_bytes': statistics.median(sizes), 'p95_bytes': sorted(sizes)[ceil(.95*requests)-1],
                    'members': 50, 'messages': 100, 'events': 25, 'attendance_rows': 625}
        finally:
            if process is not None and process.poll() is None:
                process.terminate()
                process.wait(timeout=10)
            client.drop_database(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT)
    parser.add_argument('--mongo-port', type=int, required=True)
    parser.add_argument('--port', type=int, default=5012)
    parser.add_argument('--requests', type=int, default=20, choices=range(1, 101), metavar='1..100')
    args = parser.parse_args()
    print(json.dumps(run(args.source, args.mongo_port, args.port, args.requests), indent=2))
