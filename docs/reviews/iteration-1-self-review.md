# Iteration 1 four-pass review record

Owner: Liam Pheng. Instructor: Dr. Litman. Date: 2026-11-01.

This is the assistant's recorded four-pass code review and an explicit handoff for Liam Pheng's required self-review. It is not a claim that Liam Pheng personally performed these passes. Personal review: pending.

| Slice | Pass | Finding | Disposition and evidence |
|---|---|---|---|
| FR-ACCT-03 | 1 — correctness | A valid replacement must overwrite the account hash; an invalid replacement must not. | Fixed: shared security predicate, exact SRS error, compare-and-set update; test_password_change_ac1* and test_password_change_ac2*. |
| FR-ACCT-03 | 2 — security | A stolen active session must not silently rotate a password; old sessions must not retain access. | Fixed: require current password and CSRF; delete all account sessions and clear the cookie. Wrong-current, anonymous and revoked-second-session tests pass. |
| FR-ACCT-03 | 3 — maintainability | Duplicating password policy would drift from registration. | Fixed: reuse password_valid. Existing route closures retained to keep this increment narrow; extraction deferred to Week 11 if the routes expand. |
| FR-ACCT-03 | 4 — requirements/evidence | Password recovery without a current password is not delivered by this route. | Accepted limit: the two written ACs cover signed-in replacement; no email reset/recovery claim. Liam Pheng should resolve the broader rationale before Week 11. Both verbatim ACs are mapped in iteration-1-evidence.md. |
| FR-CHAT-04 | 1 — correctness | Existing code stored display name rather than the required username; empty input used a generic 400. | Fixed: store username for new messages; exact empty-message notice; tests assert durable attribution and error text. Historical display-name entries remain historical, not migrated. |
| FR-CHAT-04 | 2 — security | A hidden UI control would not stop a direct outsider POST or script payload. | Fixed/retained: membership before insertion, CSRF, 2000-character cap, autoescaped Jinja rendering. Authorization, escaping and 2000/2001 boundary tests pass. |
| FR-CHAT-04 | 3 — maintainability | Required validation failures should return to a usable chat page. | Fixed: notices with redirect and no write. Shared field helper retained for other flows; changed body validation is deliberately explicit for exact AC messages. |
| FR-CHAT-04 | 4 — requirements/evidence | Persistence and visibility cannot be proved by a mocked test alone. | Fixed: committed real HTTP/MongoDB acceptance smoke, plus member/leader visibility and persisted username/time tests. Message polling/real-time push is not claimed. |
| FR-CLNDR-03 | 1 — correctness | A destructive GET or event-only lookup could delete the wrong unit's event. | Fixed: GET confirmation only; POST delete scoped by both unit and event. Cancel, invalid-ID and cross-unit tests pass. |
| FR-CLNDR-03 | 2 — security | Standard members or outsiders could forge a delete request. | Fixed: server-side owner/leader membership check before lookup; CSRF required. GET/POST denied-role regressions pass. |
| FR-CLNDR-03 | 3 — maintainability | Event responses would become orphaned if cleanup were omitted. | Fixed: delete matching responses after confirmed deletion. Residual risk: these two writes are not a transaction; a database outage between them can leave unreachable response rows. Log as DEF-I1-01, Week 11 cleanup/retry work; no atomicity claim. |
| FR-CLNDR-03 | 4 — requirements/evidence | The user needs to select a concrete event and see the exact invalid-event failure. | Fixed: title-specific selection link, named confirmation and exact SRS cancellation message. Browser recording shows cancel and confirmation; live HTTP smoke checks persisted deletion. |

Cross-cutting findings: the new header link inherited a low-contrast dark color on dark green; fixed with light navigation text and explicit :focus-visible outlines. Initial seed script lint identified import-order exceptions caused by executable root-path setup; narrowly annotated those imports. Neither finding is attributed to Liam Pheng as a personal finding.

## Liam Pheng's remaining self-review

For each slice, inspect the linked route, template and tests. Explain the control flow without the assistant; deliberately exercise one denied/invalid path; rewrite any portion you cannot defend. Record actual findings and fixed/defect/accepted dispositions here. Record the actual date and any additional time in hours-log.csv. Do not check this off simply because CI is green.

| Slice | Personal explanation and break test | Personal changes/disposition | Date |
|---|---|---|---|
| FR-ACCT-03 | Pending Liam Pheng | Pending | |
| FR-CHAT-04 | Pending Liam Pheng | Pending | |
| FR-CLNDR-03 | Pending Liam Pheng | Pending | |

Accessibility check found footer contrast 4.41:1 and timestamp contrast 4.49:1 below the 4.5:1 threshold. Fixed muted text to a darker shade and repeated axe on all three changed flows; exact results are in docs/iteration-1-a11y.json. Demo fixture check also found that regenerated local credentials did not update an existing skeleton seed account. Fixed the guarded seed credential reconciliation and added a repeat-seed regression; this changes only synthetic seed data.
