# Iteration 1 demo — Liam Pheng

Audience: Dr. Litman. Target: five minutes. Record the running application, not slides.
Prepared 2026-11-01 before implementing this increment.

Prerequisites: local MongoDB running; `python script/setup`, then `.venv/Scripts/python script/seed_iteration1.py` (Windows) or `.venv/bin/python script/seed_iteration1.py` (Linux). Start with `python script/start`. Read the generated demo password from the ignored `.env`; never show that file or credentials on camera. Use only fictional seed data.

| Time | Action and narration |
|---|---|
| 0:00–0:35 | Introduce Accountabilibuddy, Liam Pheng, and FR-ACCT-03 password change, FR-CHAT-04 send message, FR-CLNDR-03 delete event. Sign in as iteration_leader. |
| 0:35–1:35 | Open Change password. Submit a weak new password to show “Password does not meet the secure requirements”. Submit a secure new password with the current password. Sign in with the new password; explain that old sessions are revoked. Do not narrate or reveal the password. |
| 1:35–2:35 | Open Iteration One Squad. Send “Meet at Demo Field at 0600.” Show the persisted message, username and UTC timestamp. Refresh to prove persistence. The automated suite also bypasses browser validation to test whitespace-only input. |
| 2:35–3:35 | Select Delete event for “Practice briefing”. Show the confirmation page, cancel once, then confirm. The event disappears; “Keep this formation” remains. Explain that members cannot delete events. |
| 3:35–4:15 | Show the test summary and green CI link from docs/iteration-1-evidence.md. Show the three requirement rows and acceptance evidence. |
| 4:15–5:00 | State remaining work: calendar creation and unit/group membership flows Week 11; accessibility and measured performance Week 12; user trials Week 13; security/hosting hardening Week 14. Say the self-review and recording status honestly. End before five minutes. |

Rehearse once, reset only the dedicated demo database using the seed command, then record. Upload the actual screen recording to a Canvas-supported location and submit its accessible link. A script or automated test is not a recording. Recording/link pending until an actual capture is produced.
