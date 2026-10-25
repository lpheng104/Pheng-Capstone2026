"""Bounded HTTP readiness wait; never treats a redirect as database health."""
import time
import urllib.error
import urllib.request

for attempt in range(30):
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/health',timeout=2) as response:
            if response.status == 200:
                print('READY: HTTP health returned 200')
                break
    except (urllib.error.URLError,TimeoutError):
        time.sleep(1)
else:
    raise SystemExit('READINESS FAILED: health never returned 200')
