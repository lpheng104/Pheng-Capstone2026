# Definition of Done

Adapted from the existing course-derived checklist in this repository for Iteration 1. Owner: Liam Pheng. Updated 2026-11-01. A green automated check is necessary, but a slice remains In Progress until every applicable gate below passes. Dr. Litman can follow the criterion map in docs/iteration-1-evidence.md.

| Gate | Required evidence | Iteration 1 application |
|---|---|---|
| Stable requirement and verbatim acceptance | Exactly one traceability row; every written AC mapped to implementation and test | FR-ACCT-03, FR-CHAT-04, FR-CLNDR-03 mapped in iteration-1-evidence.md |
| Observable end-to-end behavior | Route, UI, real database persistence and a handled failure | script/iteration1_http.py; committed seed; five-minute browser capture |
| Regression and boundary checks | Entire suite, denied roles, missing CSRF and invalid input pass | 23 pytest cases; exact errors, password boundaries, message limits and cross-unit deletion |
| Traceability | tools/check-traceability.py exits zero | Record result in evidence document |
| Credentials/configuration | Secret audit of history and source passes; every environment variable documented; no real personal/military data | Existing audit stage plus .env.example and README Run it |
| Accessibility | Associated labels, visible keyboard focus, keyboard-operable controls; no serious/critical axe findings on changed flows | Automated browser/a11y evidence recorded separately; no full WCAG conformance claim |
| Recoverable errors | Clear exact required messages, no secret/trace in user-facing error | Invalid password, empty message, invalid event and denied-role paths |
| Reproducible release | Pinned install, setup/seed, build and live smoke pass from CI checkout; default branch green | CI workflow including live iteration-one acceptance; iteration-1 tag |
| Four-pass personal review | Liam Pheng records correctness, security, maintainability and requirements findings with dispositions | Assistant review exists; Liam Pheng personal review pending |
| Disclosure/process | Every surviving AI contribution disclosed; current honest hours; board and burn-down updated | AI entry 2026-11-01; reported 14-hour aggregate explicitly reconstructed; board remains In Progress while personal gates remain |
| Demo | Five-minute seeded demo and accessible fallback recording, including failure path | Script and automated capture provided; Liam Pheng reviews recording before Canvas submission |

Milestone 11 extends traceability to one row per acceptance criterion in `docs/traceability.csv`.
Use `python tools/milestone11_matrix.py --check` for that matrix. The historical
one-row-per-requirement design matrix is preserved as `docs/design-traceability.csv`.

No task moves to Done with a failed or pending applicable gate. Current slice issues remain open/In Progress because personal review has not been supplied. The eight-commits-across-the-week criterion is assessed honestly from timestamps; November 1 commits cannot substitute for daily work earlier in the week.
