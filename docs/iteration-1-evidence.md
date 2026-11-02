# Iteration 1 acceptance evidence

Owner: Liam Pheng. Instructor: Dr. Litman. Evidence date: 2026-11-01.

Three implemented slices. Automated acceptance has passed. Personal review remains a release-acceptance gate; these are not represented as fully Done on the board.

## Verbatim acceptance criteria and implementation map

### FR-ACCT-03

Implementation: [src/app.py::change_password](../src/app.py#L191).

**AC-1 (verbatim):** Given an already existing user wants to change their already existing password, when they click the "change password option" they will be taken to a screen asking for input of new password. The user will then input a newly generated password that meets the security criteria (at least 8 characters, 1 lowercase, 1 uppercase, special character (!,@,#,$,%)) and input it into the system. The new password will then overwrite the already existing password within the MongoDB database assigned to their account. 

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L38); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-2 (verbatim):** Given the user input newly generated password is not secure (does not meet the password criteria), when inputting the newly created password for the account, then the system will spit out "Password does not meet the secure requirements" and then prompt the user to create a new password. The system will not store the invalid password to the account created in MongoDB.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L58); live HTTP/MongoDB smoke and demo script. Result: automated pass.

### FR-CHAT-04

Implementation: [src/app.py::send_message](../src/app.py#L272).

**AC-1 (verbatim):** Given a user is a member of a group chat, when they enter a message and submit it, the system will send the message to the group chat.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L78); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-2 (verbatim):** Given a message is successfully sent, the message will be displayed in the group chat and will be visible to all authorized members of the group chat.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L78); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-3 (verbatim):** Given a user attempts to send an empty message, the system will not send the message and will display "Message cannot be empty."

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L94); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-4 (verbatim):** Given a user is not a member of the group chat, the system will deny the user from sending messages in the group chat.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L101); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-5 (verbatim):** Given a message is sent, the system will associate the message with the username of the user who sent it and the time the message was sent.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L78); live HTTP/MongoDB smoke and demo script. Result: automated pass.

### FR-CLNDR-03

Implementation: [src/app.py::delete_event](../src/app.py#L306).

**AC-1 (verbatim):** Given an existing event is on a unit calendar, when an administrative/leadership user initiates a delete calendar event request, the system will ask which event they want to delete.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L121); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-2 (verbatim):** Given the administrative user selects a valid event from the unit calendar, the system will delete the event from the selected unit's calendar.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L121); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-3 (verbatim):** Given the selected event does not exist on the unit calendar, the delete calendar event request will be cancelled and the system will spit out "Invalid event, delete calendar event request cancelled."

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L136); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-4 (verbatim):** Given an administrative user attempts to delete an event from a unit calendar they are not authorized to manage, the system will deny the request.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L142); live HTTP/MongoDB smoke and demo script. Result: automated pass.

**AC-5 (verbatim):** Given a non-administrative user attempts to delete a calendar event, the system will deny the request.

Evidence: [tests/test_iteration1.py](../tests/test_iteration1.py#L142); live HTTP/MongoDB smoke and demo script. Result: automated pass.

## Verification results

- Full local suite: 23 passed in 50.49 seconds. 1109 warnings originate from mongomock deprecated utcnow use; no failed tests.
- Ruff: all checks passed. Build: passed, with source, migrations, seed and executable scripts included.
- Real HTTP + MongoDB: script/iteration1_http.py passed for all three slices; uses real sockets and persisted records, not Flask test_client or mongomock.
- Original skeleton live smoke and database-outage failure remain required CI gates.
- Browser capture: docs/demo/iteration-1-script.md and script/record_iteration1.cjs. Actual captioned automated recording: [download demo](https://github.com/lpheng104/Pheng-Capstone2026/releases/download/iteration-1/iteration-1-demo.webm); duration/hash in docs/demo/iteration-1-recording.json.
- Accessibility, exact CI URLs and release link are recorded below once verified.

## Known limits and remaining product work

| Work | Scheduled week | Status |
|---|---|---|
| Calendar creation and remaining unit/group membership acceptance; orphan-response cleanup DEF-I1-01 | 11 | Backlog |
| Accessibility across the full product; measured performance and deletion evidence | 12 | Backlog |
| User trials and platform/regression repeat | 13 | Backlog |
| Production hosting/security hardening and backup/restore verification | 14 | Backlog |
| Final release/demo rehearsal | 15 | Planned |

Chat still requires refresh; no real-time push claim. No production deployment, full WCAG audit, human usability observation, personal self-review or complete original planning-task acceptance is implied.

## Process exceptions

All new increment commits are honestly dated November 1. This supplies coherent commits, but cannot satisfy the separate requirement that at least eight commits be spread across the week. Hours source is a user-reported weekly aggregate; session intervals were not invented. Original Week 9 overlapping/reconstructed entries are preserved and flagged in hours report notes.

## Accessibility and clean setup follow-up

Axe-core 4.10.3 checked the password form, unit chat and delete confirmation in Chromium against the real local app. The first run found footer contrast 4.41:1 and timestamp contrast 4.49:1, both below 4.5:1. Darkened muted text and repeated the check: three pages, zero violations, zero critical/serious findings. Tab focus produced an explicit solid outline. Raw result: [iteration-1-a11y.json](iteration-1-a11y.json). This does not certify a full-product WCAG audit or a human usability observation.

A regenerated local .env against an existing demo database exposed a seed credential mismatch. Updated the guarded synthetic skeleton account on seed and added the repeated-seed credential regression; the full suite now has 23 passing tests. The final browser recording captions report the observed 23-test suite; the added twenty-third test covers this setup follow-up.

Initial hosted PR checks passed at 3fc5cbf: CI push run [41368264188](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/41368264188) and PR run [41368269500](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/41368269500). Merged default-branch CI at f81d36d passed: [41368856412](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/41368856412). The final recording/submission metadata commit has a subsequent exact-head CI run, supplied in the submission handoff.

## Verified recording

The captioned automated browser recording is 300.00 seconds, 1440 × 1000 VP8/WebM, with actual password rejection, password rotation, persisted message, cancelled/confirmed deletion and HTTP 403 denial. [Recording](https://github.com/lpheng104/Pheng-Capstone2026/releases/download/iteration-1/iteration-1-demo.webm). [Manifest](demo/iteration-1-recording.json). Frames at the failure, message, confirmation, remaining-event and denied-role points were visually inspected. The final file is a stream-copy five-minute trim of the capture, not a constructed slideshow.

All three selected issues are linked on [the project board](https://github.com/users/lpheng104/projects/1): [#46](https://github.com/lpheng104/Pheng-Capstone2026/issues/46), [#47](https://github.com/lpheng104/Pheng-Capstone2026/issues/47), [#48](https://github.com/lpheng104/Pheng-Capstone2026/issues/48). Personal review remains open. [DEF-I1-01 / #49](https://github.com/lpheng104/Pheng-Capstone2026/issues/49) is in Backlog for Week 11.
