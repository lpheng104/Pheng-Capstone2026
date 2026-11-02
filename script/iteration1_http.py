"""AI-assisted 2026-11-01; real HTTP + MongoDB acceptance smoke for three slices.

Run after setup/seed_iteration1 against a disposable synthetic database.
"""
import argparse
import http.cookiejar
import os
from pathlib import Path
import re
import secrets
import sys
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv  # noqa: E402
from src.persistence import connect  # noqa: E402
from script.seed_iteration1 import seed_demo  # noqa: E402


def run(base):
    load_dotenv(ROOT/'.env')
    client, db = connect(os.environ['MONGODB_URI'], os.environ['MONGODB_DATABASE'])
    password = os.environ['SKELETON_PASSWORD']
    try:
        unit = seed_demo(db, password)
        cookies = http.cookiejar.CookieJar()
        browser = build_opener(HTTPCookieProcessor(cookies))

        def get(path):
            with browser.open(base+path, timeout=15) as r:
                return r.read().decode()

        def post(path, data):
            token = re.search(r'name="csrf" value="([^"]+)"', get('/login')).group(1)
            data = urlencode({**data, 'csrf': token}).encode()
            with browser.open(base+path, data=data, timeout=15) as r:
                return r.read().decode()

        post('/login', {'username': 'iteration_leader', 'password': password})
        assert 'Change password' in get('/')
        assert 'Password does not meet the secure requirements' in post('/account/password',
            {'current_password': password, 'new_password': 'weak'})
        replacement = 'Live!'+secrets.token_urlsafe(24)
        assert 'Password changed. Please sign in again.' in post('/account/password',
            {'current_password': password, 'new_password': replacement})
        assert 'Invalid username or password.' in post('/login',
            {'username': 'iteration_leader', 'password': password})
        post('/login', {'username': 'iteration_leader', 'password': replacement})
        base_unit = '/units/'+unit
        assert 'Message cannot be empty.' in post(base_unit+'/messages', {'body': '   '})
        message = 'HTTP acceptance '+secrets.token_hex(8)
        page = post(base_unit+'/messages', {'body': message})
        assert message in page and '<strong>iteration_leader</strong>' in page
        assert db.messages.find_one({'body': message})['author'] == 'iteration_leader'
        event = db.events.find_one({'unit_id': db.units.find_one({'name': 'Iteration One Squad'})['_id'],
                                    'title': 'Practice briefing'})
        path = base_unit+'/events/'+str(event['_id'])+'/delete'
        assert 'Confirm delete event' in get(path)
        page = post(path, {})
        assert 'Calendar event deleted.' in page and 'Practice briefing' not in page
        assert 'Keep this formation' in page
        assert db.events.find_one({'_id': event['_id']}) is None
        assert 'Invalid event, delete calendar event request cancelled.' in post(path, {})
        post('/logout', {})
        post('/login', {'username': 'iteration_member', 'password': password})
        try:
            post(path, {})
            raise AssertionError('Member delete was permitted')
        except HTTPError as error:
            assert error.code == 403
        print('LIVE ACCEPTANCE PASS: FR-ACCT-03, FR-CHAT-04, FR-CLNDR-03; real HTTP and MongoDB.')
    finally:
        # Repeatable demo state; this only touches the guarded synthetic fixture.
        seed_demo(db, password)
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='http://127.0.0.1:5000')
    args = parser.parse_args()
    run(args.base_url.rstrip('/'))
