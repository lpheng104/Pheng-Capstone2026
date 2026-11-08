# Milestone 11 manual and measurement cases

Candidate procedures, not executed this run. Use synthetic data only. Each case maps to the corresponding NFR metric criterion, AC1.

### NFR-PERF-01-AC1

1. Seed an isolated deployed fixture with 50 members, 100 messages and 25 events.
2. Authenticate, warm the unit page once, then time 20 sequential GET requests. Record environment, status codes and durations.
3. **Pass:** all requests succeed; after sorting durations, the 19th is at most 1.5 s.

### NFR-REL-01-AC1

1. Use a clean pinned environment and disposable loopback MongoDB.
2. Run the full suite ten consecutive times and record each exit code, skip and expected failure.
3. **Pass:** ten zero exit codes and all integration cases run. Disclose expected failures separately.

### NFR-REL-02-AC1

1. Create an event via HTTP on an isolated disposable server; record its ID and fields.
2. Stop only that fixture MongoDB, confirm health fails, restart with the same data directory, and time recovery.
3. **Pass:** HTTP 200 within five minutes and the original event remains unchanged.

### NFR-SEC-01-AC1

1. Build a grid of all unit-scoped routes and methods against anonymous, outsider, member, leader and owner roles.
2. Exercise each cell with its permitted or prohibited action; include foreign unit and event IDs and compare stored data before and after.
3. **Pass:** every prohibited request is 302, 403 or 404 and makes no write. Record the whole grid.

### NFR-SEC-03-AC1

1. Scan Git-tracked files for secret patterns using the repository scanner.
2. Register a fictional account and inspect stored fields for no plaintext credential. Audit pinned runtime dependencies using pip-audit; reconcile the outdated SRS file path before final acceptance.
3. **Pass:** zero credentials or plaintext passwords and zero unresolved high/critical dependency vulnerabilities.

### NFR-SEC-04-AC1

1. Submit the hostile markup fixture to every displayed user-controlled name and message field.
2. Open each affected view in a real browser; inspect rendered text, DOM and alert behavior.
3. **Pass:** markup is escaped and there are zero injected elements or script executions. Record every field/view pair.

### NFR-PRIV-01-AC1

1. Run synthetic registration, member and leadership flows.
2. Enumerate field names from the affected MongoDB collections and compare with the approved inventory.
3. **Pass:** zero undocumented collected fields. Document and obtain approval for any mismatch before merge.

### NFR-ACCSS-01-AC1

1. Open register, login, dashboard and populated unit pages in a browser.
2. Run axe on each page at desktop width and 390 px; save eight dated results.
3. **Pass:** zero critical or serious findings across all eight results.

### NFR-ACCSS-02-AC1

1. Start at Chrome’s address bar at 100% zoom. Use only keyboard input.
2. Register, sign in, post a message, respond to an event and sign out. Record focus order and visibility at each step.
3. **Pass:** 5/5 tasks complete, with logical order and visible focus.

### NFR-USE-02-AC1

1. Prepare weak password, duplicate username, bad admin token, unknown member, missing field, overlong field, naive time and invalid attendance cases.
2. Execute all eight on a synthetic fixture; inspect the response and relevant stored records after each.
3. **Pass:** 8/8 reject the write with corrective feedback or the documented HTTP error.

### NFR-MAINT-01-AC1

1. Install pinned dependencies in a fresh environment on the course Windows laptop.
2. Run and time the full test command with real disposable MongoDB. Record exit status, duration, pass, failure and skip counts.
3. **Pass:** 100% of cases pass and elapsed time is at most 60 s. Expected failures do not establish 100% pass.
