# Milestone 11 defect log

Owner: Liam Pheng. Reviewer: Dr. Litman. Discovery: 2026-11-08.

Environment for each reproduction: Windows course laptop, pinned Python 3.12.14, isolated Flask test client and synthetic mongomock fixture. No production data or Atlas writes.

Triage order: revoke transferred-member access (#05), then separate subgroup access (#06), then reconcile calendar/rank workflows (#07 and #09). Feedback fixes are small and independent. S2 means a major missing or unsafe workflow; S3 means limited impact with a workaround. P1 precedes P2 due to user risk and sequencing.

Status “fixed in draft” means reproduced red before the patch and green in the candidate; no merge or owner approval is implied.

## DEF-M11-01 — Duplicate registration reports different text

- **Requirement criterion:** FR-ACCT-01-AC2 and FR-ACCT-06-AC2.
- **Reproduction:** Submit registration for the existing fictional qa_member username.
- **Expected:** Reject the duplicate and display “username already is in use”.
- **Actual before patch:** The unique index rejects the duplicate; the form shows “Username already in use.”
- **Severity:** S3 — no duplicate account or data loss; specified feedback differs.
- **Priority:** P2 — update the message in this increment; a user can already choose another name.
- **Status / disposition:** Fixed in draft; verified green after red.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-ACCT-01-AC2]`, `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-ACCT-06-AC2]`.

## DEF-M11-02 — Weak registration password reports different text

- **Requirement criterion:** FR-ACCT-02-AC2.
- **Reproduction:** Submit registration with the synthetic password input weak.
- **Expected:** Do not create an account and display “Password does not meet the secure requirements”.
- **Actual before patch:** No account is created; registration shows a different policy sentence.
- **Severity:** S3 — validation holds; the user sees inconsistent guidance across password forms.
- **Priority:** P2 — fix the clear specification mismatch while retaining the policy guidance.
- **Status / disposition:** Fixed in draft; verified green after red.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-ACCT-02-AC2]`.

## DEF-M11-03 — Blank unit name shows generic field error

- **Requirement criterion:** FR-UNIT-01-AC4.
- **Reproduction:** Sign in as fixture owner and POST unit creation with a blank name and Squad echelon.
- **Expected:** Cancel creation, retain no extra record, and display “No unit name entered creation request cancelled”.
- **Actual before patch:** No extra unit is written, but the response is a generic field error.
- **Severity:** S3 — no orphan unit; the cancellation feedback is incorrect.
- **Priority:** P2 — inexpensive user-facing correction with a precise regression.
- **Status / disposition:** Fixed in draft; verified green after red.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-UNIT-01-AC4]`.

## DEF-M11-04 — Unknown unit member shows different cancellation text

- **Requirement criterion:** FR-UNIT-02-AC3.
- **Reproduction:** As fixture owner, submit the hostile dataset’s unknown username to Add a member.
- **Expected:** Cancel without writing a membership and display “Invalid user, add user request cancelled”.
- **Actual before patch:** No membership is written; the unit page says “That user must register first.”
- **Severity:** S3 — membership remains unchanged; cancellation text differs.
- **Priority:** P2 — align the message while preserving the registration hint.
- **Status / disposition:** Fixed in draft; verified green after red.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-UNIT-02-AC3]`.

## DEF-M11-05 — No workflow to remove a member

- **Requirement criterion:** FR-UNIT-03-AC1.
- **Reproduction:** Sign in as fixture owner. Open the unit roster with a current member; inspect member controls and routes.
- **Expected:** Offer a removal request with username selection so a transferred member can be removed.
- **Actual before patch:** Roster offers add/edit but no removal flow; normal owners cannot revoke membership.
- **Severity:** S2 — transferred users may retain access until membership is corrected outside the UI.
- **Priority:** P1 — implement server-authorized removal first, with replay and nonmember denial tests.
- **Status / disposition:** Open; strict expected failure with reproducible baseline symptom.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-UNIT-03-AC1]`.

## DEF-M11-06 — No separate named group-chat creation

- **Requirement criterion:** FR-CHAT-01-AC1.
- **Reproduction:** Open the fixture unit as its owner and look for a chat creation form and endpoint.
- **Expected:** Offer a named group chat with selection of unit members.
- **Actual before patch:** Only a single unit-wide chat exists; there is no group-chat creation path.
- **Severity:** S2 — core channel separation is unavailable; sensitive subgroup discussion cannot safely use unit-wide chat.
- **Priority:** P1 — after member removal, design group authorization before exposing subgroup content.
- **Status / disposition:** Open; strict expected failure with reproducible baseline symptom.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-CHAT-01-AC1]`.

## DEF-M11-07 — No distinct calendar creation workflow

- **Requirement criterion:** FR-CLNDR-01-AC1.
- **Reproduction:** Open a freshly created fixture unit as owner and inspect the events/calendar controls.
- **Expected:** Offer an add-calendar request for an existing unit that has no calendar.
- **Actual before patch:** The unit has an events area immediately; no calendar creation action or entity is available.
- **Severity:** S3 — scheduling remains usable but the distinct lifecycle in the SRS is absent.
- **Priority:** P2 — reconcile the intended calendar lifecycle with Liam Pheng before implementing or changing the SRS.
- **Status / disposition:** Open; strict expected failure with reproducible baseline symptom.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-CLNDR-01-AC1]`.

## DEF-M11-08 — Missing event information shows generic field error

- **Requirement criterion:** FR-CLNDR-02-AC4.
- **Reproduction:** As owner, submit the happy event with its title blank.
- **Expected:** Reject the write and display “Required event information missing, add calendar event request cancelled.”
- **Actual before patch:** No event is written; the server instead returns the generic title field error.
- **Severity:** S3 — no invalid event persists, but the promised cancellation feedback is absent.
- **Priority:** P2 — align the exact missing-field response in this review candidate.
- **Status / disposition:** Fixed in draft; verified green after red.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-CLNDR-02-AC4]`.

## DEF-M11-09 — Rank assignment does not offer a military rank list

- **Requirement criterion:** FR-RANK-02-AC2.
- **Reproduction:** As owner, open a current non-owner member’s roster edit form.
- **Expected:** Present available military ranks for the selected member.
- **Actual before patch:** A free-text rank input is shown, not the required selection list.
- **Severity:** S3 — inconsistent rank values can be stored; role restrictions still apply.
- **Priority:** P2 — define the approved rank catalog, then validate selections on the server.
- **Status / disposition:** Open; strict expected failure with reproducible baseline symptom.
- **Regression:** `tests/acceptance/test_m11_criteria.py::test_written_criterion[FR-RANK-02-AC2]`.

Existing Week 10 defect [#49](https://github.com/lpheng104/Pheng-Capstone2026/issues/49) remains separately tracked; it was not counted as a newly reproduced defect.
