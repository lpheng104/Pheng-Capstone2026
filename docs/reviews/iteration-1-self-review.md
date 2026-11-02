# Iteration 1 four-pass review record

Owner: Liam Pheng. Instructor: Dr. Litman. Date: 2026-11-01.

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
