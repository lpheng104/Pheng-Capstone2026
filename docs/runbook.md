# Accountabilibuddy operations runbook

Owner: Liam Pheng. Instructor: Dr. Litman. Draft reviewed against source on 2026-11-22 by Codex; **last personally verified date/name: pending Liam Pheng**. Existing hosted verification is dated 2026-11-02, not a new claim.

## Where it runs and expected readings

The public Flask/Gunicorn app runs on Render at https://accountabilibuddy-demo.onrender.com; MongoDB Atlas stores its data. They do not require the developer laptop to stay on. Local development binds loopback only on port 5000 by default. Earlier 5010 overrides are not required. MongoDB local default is 27017. Normal state: public HTTPS sign-in page, `/health` HTTP 200 with JSON `{"status":"ok"}`, protected unit pages require authentication, and cookie flags Secure/HttpOnly/SameSite=Lax on the hosted service.

## Start, stop and restart

Follow README install/configure first. Local start: ` .\.venv\Scripts\python.exe script/start ` from the checkout. Expected: listening URL on loopback and a terminal that remains open. Ctrl+C stops only that app process; restart with the same command and confirm the stored unit remains. Stopping MongoDB is a separate action; identify the server before stopping it. Do not kill every Python or MongoDB process.

For the README's disposable Docker server only: `docker stop accountabilibuddy-m13` expects the container name and stops it without erasing its data. `docker start accountabilibuddy-m13` expects the name and makes it available again. Human command verification is pending; do not run these against an unrelated container.

For Render, open the service dashboard and inspect the deployment's source commit, status and logs. Manual Deploy → Deploy latest commit publishes the linked branch. Wait for Live, then check health and login. The blueprint requests deployment after checks pass; do not assume the live manually created service inherited every blueprint setting. Verify its actual Auto-Deploy setting. Roll back only to a known application/schema-compatible revision; redeploying old code does not roll back Atlas writes.

## Health and degraded state

In PowerShell: `Invoke-RestMethod http://127.0.0.1:5000/health` should yield a `status` property of `ok`. For hosted checks substitute the public HTTPS URL. An unhealthy database returns HTTP 503 and the page text `Database unavailable. Please try again shortly.`; PowerShell normally raises a non-success HTTP error instead of returning JSON. A failed startup can produce a provider error before Flask is available. Neither case proves that stored data was lost. Record the time, source commit and exception class without copying URIs or credentials.

The Milestone 12 tag adds a retry header and expanded recovery checks; those are not silently assumed present on current main. No automatic database failover, backup restore or blanket retry of writes is implemented.

## Routine operations and boundaries

Check health and a fictional user's authenticated unit page after a deploy. Keep dependency pins, README and schema changes reviewed together. Use Render's private environment settings for secrets; generation/rotation of SECRET_KEY invalidates session cookies. ADMIN_SETUP_TOKEN authorizes bootstrap of the one configured admin username; it neither reveals nor changes an existing account password. Passwords are hashes. Use the application's authenticated password-change flow when current credentials are known.

There is no fully verified Atlas backup/restore procedure here. Before migrations, arrange a provider-supported backup/export and independently prove restore in a separate database. Do not claim free-tier snapshots exist without checking the account's actual service. Escalate before modifying schema, removing members through raw queries or running a privacy deletion request.

## Failure catalogue from recorded defects

| Evidence | Symptom and diagnosis | Safe response / workaround | Escalation |
|---|---|---|---|
| DEF-M11-01 | Duplicate username rejected; older revisions show inconsistent wording | Choose a unique fictional username; confirm count remains one | Maintainer if multiple records appear |
| DEF-M11-02 | Weak password rejected; wording differs by revision | Use 8–128 characters, upper/lowercase and one of !@#$%; do not bypass validation | Maintainer if valid input fails |
| DEF-M11-03 | Blank unit name cancels creation | Enter a nonblank unit name and retry once; inspect for duplicates first if a request outcome is unknown | Maintainer for orphaned membership |
| DEF-M11-04 | Unknown username cannot be added | Register the user first and recheck the spelling; no direct database grant | Unit owner, then maintainer |
| DEF-M11-05 (S2, open) | No supported member-removal workflow | Do not onboard real or sensitive units; there is no safe in-app revocation workaround | Stop sensitive use and escalate to Liam Pheng |
| DEF-M11-06 (S2, open) | Only unit-wide chat; no private subgroup | Treat all unit members as readers; do not post subgroup-private data | Maintainer before expanding audience |
| DEF-M11-07 (open) | No separate add-calendar control | Use existing unit events; do not assume the distinct calendar lifecycle is delivered | Requirements owner |
| DEF-M11-09 (open) | Rank is free text, not a military rank selector | Use a consistent fictional label; it never grants permission | Requirements owner for a rank catalog |
| DEF-I1-01 / issue #49 | Interruption between event deletion and response cleanup may leave orphan responses | Do not claim transactionally complete deletion; inspect in an isolated copy before remediation | Maintainer before any cleanup write |

## Destructive commands: do not run in production

`db.dropDatabase()` destroys a MongoDB database; **do not run it against Atlas or any shared dataset**. It is named here as a prohibition, not an execution step. Likewise do not use `docker rm -v` as a restart procedure: removing storage can erase data. `script/seed_iteration1.py` resets named demo passwords/sessions and replaces synthetic unit events/messages; never run it on live or real-user data just to repair login. `script/iteration1_http.py` invokes that same reset as part of a test. Database-name suffix guards do not make real content disposable.

## Escalation and evidence

Contact Liam Pheng through repository issues for technical triage; Dr. Litman for course acceptance/scope questions. Provide commit, timestamp, affected fictional workflow, status code and sanitized exception class. Put secrets only in provider private settings, never in issue screenshots. For suspected exposure, revoke/rotate at the provider first and preserve incident evidence privately; changing Git history alone does not revoke a credential. Do not assert an untested recovery succeeded.
