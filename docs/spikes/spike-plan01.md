# Spike SP-01 — Does logout reject a replayed session cookie?

- **Unknown:** Does the existing database-token implementation revoke a captured session?
- **Feeds:** ADR 0001
- **Requirements at risk:** FR-AUTH-02, NFR-SEC-01
- **Time box:** 90 minutes
- **Run on:** 2026-09-27

## The question

Does replaying a captured authenticated cookie after logout produce a redirect to login in all 10 independent trials?

## The smallest thing that answers it

Use Flask's test client and an isolated mongomock database. Register and log in, capture the actual cookie, log out with a valid CSRF token, replay the cookie in a fresh client, and request the dashboard. Run a minimal signed-cookie-only Flask control to test the same replay. Keep this diagnostic script for reproducibility; it is not application code.

## Success criterion

Database-token replay is denied in 10/10 trials. Each initial login permits dashboard access and each logout returns a redirect. Record control results separately.

## Failure criterion

Any replay receives protected content, any setup fails, or the 90-minute time box expires.

## Plan B if it fails

Keep ADR 0001 Proposed, investigate revocation, and block acceptance of FR-AUTH-02. Do not replace revocable sessions with a cookie-only design that also fails replay.

## Result

Executed 2026-09-27 at 22:59:56 UTC using `code/spike-session-replay.py`. Execution took 7.765 seconds, within the 90-minute time box. Database-token design denied all 10/10 replay requests with HTTP 302 to login. The signed-cookie-only control allowed all 10/10 replay requests with HTTP 200. Initial authentication and logout assertions passed. The useful finding is that clearing the browser cookie does not invalidate a previously captured signed cookie.

The plan was written before execution. Script retained for reproduction; [captured output](SP-01-result.json). This experiment cannot establish Atlas consistency, TTL behavior, concurrent worker behavior, or hosted cookie security. It is assistant-executed evidence, not a claim of student execution or an additional 90 minutes of student work.

## Decision

Proceed with the database-token recommendation in ADR 0001. Close only the local replay question in seam S1; retain hosted session verification in SP-02. The hours log records the student's reported total separately from the measured execution time.
