"""Check the real HTTP health contract without database credentials."""
import argparse
import json
import time
from urllib.error import HTTPError
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['up', 'down', 'recover'])
    parser.add_argument('--url', default='http://127.0.0.1:5000/health')
    args = parser.parse_args()
    started = time.monotonic()
    while True:
        try:
            with urlopen(args.url, timeout=8) as response:
                assert response.status == 200 and json.load(response) == {'status': 'ok'}
                assert args.mode != 'down', 'Healthy response while database is stopped'
                break
        except HTTPError as error:
            assert error.code == 503, error.code
            if args.mode == 'down':
                body = error.read()
                assert error.headers['Retry-After'] == '5'
                assert b'Database unavailable. Please try again shortly.' in body
                assert b'Traceback' not in body and b'mongodb://' not in body
                break
            if args.mode != 'recover' or time.monotonic()-started >= 290:
                raise
            time.sleep(2)
    elapsed = time.monotonic()-started
    assert elapsed <= (300 if args.mode == 'recover' else 8)
    print(f'RC health {args.mode}: PASS; {elapsed:.3f} seconds')


if __name__ == '__main__':
    main()
