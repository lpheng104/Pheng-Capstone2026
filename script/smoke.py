"""Real HTTP + MongoDB smoke test. No Flask test client and no mock database."""
import argparse
import html
import http.cookiejar
import os
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT),str(ROOT)]


def run(base_url, mutation_proof=False, save_html=None):
    from dotenv import load_dotenv
    from src.persistence import connect
    load_dotenv(ROOT/'.env')
    base_url = base_url.rstrip('/')
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def get(path):
        with opener.open(base_url+path, timeout=12) as response:
            assert response.status == 200, 'Unexpected HTTP status'
            return response.read().decode('utf-8')

    assert 'ok' in get('/health'), 'Health did not confirm database connectivity'
    login = get('/login')
    csrf = re.search(r'name="csrf" value="([^"]+)"',login).group(1)
    payload = urllib.parse.urlencode({'username':'skeleton_member',
                                     'password':os.environ['SKELETON_PASSWORD'],
                                     'csrf':html.unescape(csrf)}).encode()
    with opener.open(base_url+'/login',data=payload,timeout=12) as response:
        assert response.geturl().rstrip('/') == base_url, 'Login did not reach dashboard'
        dashboard = response.read().decode()
    client, db = connect(os.environ['MONGODB_URI'],os.environ['MONGODB_DATABASE'])
    try:
        unit = db.units.find_one({'name':'Skeleton Demo Unit'})
        assert unit, 'Seeded unit missing'
        path = '/units/'+str(unit['_id'])
        assert path in dashboard, 'Unit is not linked from rendered dashboard'
        page = get(path)
        message = db.messages.find_one({'unit_id':unit['_id'],'body':'Skeleton database row'})
        assert message, 'Seeded message missing'
        for marker in ('Skeleton Demo Unit','Skeleton database row','Synthetic Formation','attending'):
            assert marker in page, 'A real rendered component is missing'
        if mutation_proof:
            probe = 'Database change proof '+uuid.uuid4().hex[:12]
            original = message['body']
            try:
                db.messages.update_one({'_id':message['_id']},{'$set':{'body':probe}})
                updated = get(path)
                assert probe in updated and original not in updated, 'Database change did not reach HTML'
                print('SMOKE PASS: direct MongoDB update appeared in rendered HTML; original row restored.')
            finally:
                db.messages.update_one({'_id':message['_id']},{'$set':{'body':original}})
        if save_html:
            save_html.parent.mkdir(parents=True,exist_ok=True)
            save_html.write_text(page,encoding='utf-8')
        print('SMOKE PASS: HTTP -> identity -> unit access -> messaging/scheduling -> real MongoDB -> HTML.')
    finally:
        client.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url',default='http://127.0.0.1:5000')
    parser.add_argument('--mutation-proof',action='store_true')
    parser.add_argument('--save-html',type=Path)
    args = parser.parse_args()
    try:
        run(args.url,args.mutation_proof,args.save_html)
    except Exception as error:
        print('SMOKE FAIL: real HTTP/database path unavailable ('+type(error).__name__+').',file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
