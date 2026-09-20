# Definition of Done

- [ ] The change has a stable requirement ID in docs/requirements.md, and that ID has exactly one nonblank row in docs/traceability.csv.
- [ ] The implemented behavior satisfies the requirement's stated acceptance or measurement method, with dated evidence recorded in the test output or docs/measurements.md.
- [ ] Automated tests cover the expected behavior, an invalid/boundary case, and a denied role when authorization is involved; the entire suite exits zero.
- [ ] python code/check-traceability.py exits zero with no blank, duplicate, orphaned, or unknown requirement rows.
- [ ] No secret, credential, plaintext password, sensitive real-world data, or unapproved dependency is present in tracked files.
- [ ] Every state-changing route rejects a missing/invalid CSRF token, and every data-scoped route enforces authentication and unit role/membership server-side.
- [ ] The changed workflow is operable by keyboard, has visible focus, has programmatically associated labels, and has zero critical/serious axe findings.
- [ ] User-facing errors reject invalid input without exposing stack traces or secrets and tell the user how to correct recoverable input.
- [ ] Setup/run/test documentation, data inventory, obligations, and traceability are updated when behavior, data, dependencies, or configuration changed.
- [ ] A fresh checkout can install the pinned dependencies and complete the documented smoke test on a supported environment without undocumented manual changes.
