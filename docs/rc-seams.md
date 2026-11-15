# Release candidate seam map

Owner: Liam Pheng. Date: 2026-11-15 Central. Production-shaped release checks run on Linux CI with real MongoDB 8.0.17, never against the public Atlas fixture.

| Tier 1 seam | Acceptance path | Real test |
|---|---|---|
| Browser-facing HTTP → Flask/HTML (C1) | Sign in, follow authenticated unit route and render persisted results | `script/smoke --mutation-proof`; `script/iteration1_http.py` |
| C2 identity → MongoDB sessions/users (C6) | Real password change, bad password rejection, new session and sign-out | `script/iteration1_http.py` |
| C3 authorization → MongoDB memberships (C6) | Member denial enforced on actual event deletion request | `script/iteration1_http.py` |
| C4 messaging → MongoDB (C6) | Write through HTTP and directly perturb stored message for rendered-read proof | Both live HTTP scripts |
| C5 scheduling → MongoDB (C6) | Confirmed event deletion persists; retained event remains available | `script/iteration1_http.py` |
| C7 bootstrap → schema/storage (C6) | Fresh pinned install, migrate, seed; strict validators and unique index | `script/setup` plus `tests/integration/test_mongodb_m11.py` |
| Flask → MongoDB failure boundary | Healthy → stopped → sanitized 503 and unsuccessful smoke → restart and successful smoke | `script/rc_health.py` plus the CI stop/restart step |

Gunicorn/Render TLS and Atlas cloud routing are environment seams. Existing [Render evidence](render-demo-verification.md) demonstrates those boundaries for the deployed demo, not this undeployed candidate. A candidate Render rerun requires owner approval.

Failure probes: unavailable MongoDB and recovery via real container stop/start; malformed fixture documents via the real schema validator; expired, absent or invalid auth via existing session tests; forged cross-unit identifiers via existing regressions; duplicate write via the real username index; malformed/naive date via acceptance cases; slow behavior with 20 timed full-volume requests. A bounded timeout is configured, but sustained slow-response injection, provider quota enforcement and upstream shape mutation have not been independently exercised.
