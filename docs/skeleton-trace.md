# Milestone 9 — Walking skeleton trace

Owner: Liam Pheng. Instructor: Dr. Litman. Date: 2026-10-25. Status: local integration verified; remote acceptance is recorded below as it occurs.

## Source and baseline reconciliation

The actual GitHub main branch is authoritative for coursework and requirement IDs. Its history differs from the earlier local prototype checkout. This integration preserves the existing requirements, architecture, planning, interviews, licenses, hours sessions and legacy workflows; it adds the verified skeleton in root src/ and tests/. No force-push of the independent local history is used.

Earlier local FR-AUTH/FR-MSG/FR-EVT identifiers are not treated as remote baseline IDs. The trace below uses actual FR-ACCT, FR-CHAT, FR-CLNDR and NFR identifiers. Existing requirements not exercised by the thin skeleton remain planned; no claim is made that the skeleton completes the product. The separate course skeleton-trace template was not supplied, so this file implements the required hop/trace/acceptance structure.

## Real slice and hop table

After real HTTP sign-in, the browser follows the dashboard unit link and requests GET /units/<id>. Returned HTML contains the seeded message, formation and attendance intention. MongoDB is the real external integration; there is no additional external API or AI service in the specified product.

| Hop/component | Source | Behavior | Mocked or stubbed on live path? |
|---|---|---|---|
| Client/browser | src/templates/auth.html, dashboard.html, unit.html | Forms, session cookie and rendered HTML | No; smoke uses real HTTP; browser inspection claims are separate |
| C1 web adapter | src/app.py; src/web | Dispatch, CSRF and Jinja rendering | No |
| C2 identity | src/identity | Resolve live unexpired/revocable database session and user | No |
| C3 unit access | src/unit_access | Authorize current membership and join roster users | No |
| C4 messaging | src/messaging | Authorize and retrieve stable latest-100 messages | No |
| C5 scheduling | src/scheduling | Authorize and assemble events/responses/current-member accountability | No |
| C6 persistence/data store | src/persistence; MongoDB 8.0.17 | Bounded real PyMongo operations and migration-version check | No |
| Return/render | src/web; src/templates/unit.html | Escaped HTML with real persisted rows | No |
| C7 maintenance | script/manage.py; migrations; src/maintenance | Real schema/index migration and synthetic seed before requests | Separate operator process, not an HTTP hop |

The remaining prototype mutation routes still contain business logic in app.py; full service extraction is not claimed. Deletion/backup/restore maintenance beyond the initial migration and seed is not implemented by this skeleton. Unit tests explicitly use mongomock, while live smoke uses neither mocks nor Flask's test client. A production Render/Atlas run is not presumed from local MongoDB or Linux CI.

## Requirement traceability

| Remote requirement | Slice responsibility | Test/evidence | Acceptance scope |
|---|---|---|---|
| FR-ACCT-04 | Real HTTP login and database-session identity | script/smoke.py; tests/test_app.py | Thin login path; broader requirement acceptance remains separate |
| FR-ACCT-05 | Revoke session on logout | test_accounts_csrf_and_revoked_logout | Regression evidence |
| FR-CHAT-05 | Persisted message history | stable-window regression; live database mutation proof | Latest-message slice |
| FR-CLNDR-02 | Seed/read a real event through scheduling | real seeded event plus event regression | No complete calendar UI claimed |
| NFR-SEC-01 | Unit isolation | outsider-denial and service-authorization tests | Tested paths only |
| NFR-REL-02 | Failure handling | /health and stopped-database negative smoke | No backup/recovery acceptance inferred |
| NFR-MAINT-01 | Reproducible CI/regression/build | script verbs and CI workflow | Observed local and remote results recorded separately |
| NFR-PORT-01 | Pinned bootstrap | Python pin, hash lock, Windows setup and Linux CI | Render acceptance remains pending |
| NFR-SEC-03 | Credential isolation/audit | root .env.example; Gitleaks; rotation plan | Scanner evidence, not a universal no-secret guarantee |

## Environment and secrets

Python is pinned to 3.12.14 and MongoDB to 8.0.17. requirements.lock pins all transitive packages and SHA-256 hashes; setup installs with --require-hashes. Setup generates local credentials in ignored .env and refuses to migrate/seed a database outside *_skeleton or test_ names. The example lists the six app variables plus the synthetic fixture password. CI uses an isolated loopback MongoDB service and generated fixture credentials, so no Atlas credential is embedded in YAML. Deployment credentials, if introduced, belong in GitHub/hosting secret stores. Four-line rotation plan: secret-rotation.md.

## Acceptance record

| Check | Evidence/result |
|---|---|
| Independent local prototype | 21 tests/eight subtests, lint, build, fresh-environment and local-tag clone passed; that count included course-tool regressions outside this integration |
| Integrated root src/tests suite | 5 passed in 6.72 s; lint and build also passed; mock-based unit fixtures explicitly labeled |
| Real datastore change | Original local path passed a direct MongoDB message update reflected in HTTP HTML, then restored the row |
| Database unavailable | Original local smoke exited 1 while the project datastore was stopped; after restart positive smoke passed |
| Integrated live smoke | Passed real HTTP login, service/data-store path and direct-database mutation/restoration on isolated port 5003 |
| Render/Atlas | Not executed by this milestone record |
| Browser visual inspection | Local login page inspected; no authenticated-page screenshot claimed |
| Annotated release | Final remote-integrated commit/tag will be recorded after CI |

## GitHub CI, issues and submission

The workflow runs install → lint → test → build → live smoke on every push and PR into main. The smoke stage also stops the isolated MongoDB and requires a nonzero smoke result. A deliberately failing test will prove the actual CI red path; its removal will be the explicit fix commit. Run URLs and the exact observed failure line will be added after execution. No successful run is asserted in advance.

Eight issue definitions using remote requirement IDs are in week9-issues.md. The existing project board is https://github.com/users/lpheng104/projects/1 (2026CapstoneProjectBoard). Published issue links/board membership are recorded after verification. All final submission links go in week9-submission.md.

## Hours and provenance

The remote detailed hours-log.csv is preserved; earlier aggregate reports of 14 Week 8 hours and 15.4 Week 9 hours are not appended again. Some sessions and aggregate reports differ and require Liam Pheng's reconciliation; no session hours, timestamps or task estimates are silently changed. AI-assisted skeleton rows are flagged and the historic calibration column is computed only for eligible pre-Week-7 sessions. Substantive AI use and the separate-history integration are documented in ai-usage.md.

## Secret audit output

Full remote-history and current-source audit output will be pasted after running the integrated command. The clean audit of the independent local prototype is not misrepresented as an audit of this remote repository history.

Verified local audit of all fetched/local refs and integrated source before publication:

```text
289 commits scanned
scanned ~829169 bytes (829.17 KB)
no leaks found
scanned ~408735 bytes (408.73 KB) of tracked/unignored source
no leaks found
SECRET AUDIT PASS: complete Git history and tracked/unignored source; no findings.
```

Eight requirement-linked issues #37–#44 have been published and verified on the existing board with status This Week. Remote CI run links remain pending execution.

## Observed deliberate red CI evidence

Run: https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/40232422421
Commit: c18c91cf682bfcfacf0fd4d3ec2475135df23b43
Observed conclusion: failure at Test after successful install, lint and full-history/source secret audit.

```text
AssertionError: DELIBERATE FAILURE: Week 9 pipeline regression proof
FAILED tests/test_ci_failure_proof.py::test_pipeline_rejects_deliberate_regression
1 failed, 5 passed, 191 warnings in 1.20s
```

The next separate fix commit removes only the intentionally failing test and records this evidence. A green result is not presumed until the subsequent remote run completes.
