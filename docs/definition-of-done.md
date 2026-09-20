# Definition of Done

**Adopted:** 2026-09-20

A change is done only when every applicable statement below can be answered **yes** by a reviewer who did not implement it. “Not applicable” must include a written reason in the pull request or commit notes.

- [ ] The change has a stable requirement ID in `docs/requirements.md`, and that ID has exactly one nonblank row in `docs/traceability.csv`.
- [ ] The implemented behavior satisfies the requirement's stated acceptance or measurement method, with dated evidence recorded in the test output or `docs/measurements.md`.
- [ ] Automated tests cover the expected behavior, an invalid/boundary case, and a denied role when authorization is involved; the entire suite exits zero.
- [ ] `python code/check-traceability.py` exits zero with no blank, duplicate, orphaned, or unknown requirement rows.
- [ ] No secret, credential, plaintext password, sensitive real-world data, or unapproved dependency is present in tracked files.
- [ ] Every state-changing route rejects a missing/invalid CSRF token, and every data-scoped route enforces authentication and unit role/membership server-side.
- [ ] The changed workflow is operable by keyboard, has visible focus, has programmatically associated labels, and has zero critical/serious axe findings.
- [ ] User-facing errors reject invalid input without exposing stack traces or secrets and tell the user how to correct recoverable input.
- [ ] Setup/run/test documentation, data inventory, obligations, and traceability are updated when behavior, data, dependencies, or configuration changed.
- [ ] A fresh checkout can install the pinned dependencies and complete the documented smoke test on a supported environment without undocumented manual changes.

## Items cut from the course template

- Formal code-review approval was cut because this is currently a one-student repository; the independent course reviewer and reproducible evidence replace a second developer approval.
- Production deployment and 24/7 monitoring were cut from each change because the product is a student prototype; deployment evidence is required only for release/demo milestones.
- A fixed code-coverage percentage was cut because it can reward low-value assertions; requirement, boundary, and authorization coverage is required instead.
- Product-owner sign-off per change was cut because stakeholder access is periodic; unresolved stakeholder decisions remain dated assumptions/open questions.
