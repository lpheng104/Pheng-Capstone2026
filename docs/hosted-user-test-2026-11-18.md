# Hosted user check — November 18, 2026

Recorded on 2026-11-22 from Liam Pheng's report. Instructor: Dr. Litman.

## Run header

- Session: Wednesday, 2026-11-18, 08:30–09:00 (30-minute session window; time zone not supplied).
- Tester: Nikita Adamov, with Liam Pheng operating the administrator account.
- Additional environment: Liam Pheng reported opening the hosted demo on an alternate PC. Exact OS/browser versions were not supplied.
- Target: https://accountabilibuddy-demo.onrender.com, backed by Atlas.
- Deployed commit: not recorded; the current source revision must not be substituted retrospectively.
- Method: user-reported hosted functional/usability check, not an instrumented installation test. No per-action timings, command transcript, screenshots or contemporaneous recording were supplied.

## Reported actions and results

| Action | Liam Pheng's reported result |
|---|---|
| Open the Render demo from another device | Hosted demo loaded. |
| Register Nikita's account | Account was created successfully. |
| Add Nikita to a unit using Liam Pheng's admin account | Nikita could participate in the unit. |
| Sign in and sign out | Both worked. |
| Send messages | Messages could be sent; seeing updates required refreshing the page. |
| Submit a present/attendance response for a demo event | Response was submitted successfully. The report uses “present”; exact UI option text was not recorded. |

These results are the owner's report of what happened, not an independently reconstructed server log. The 30-minute session window is not a measured acceptance-action completion time.

## Friction HUT-01 — messages require refresh

Liam Pheng relayed Nikita's feedback: “the only thing that wasn't super great was the text feature didn't have automatic updates and required refreshing the page.” This is an indirect report, not a verbatim transcript certified by Nikita.

- Observed impact: participants must refresh to see new messages; the interaction does not feel live.
- Existing behavior: the unit page describes refresh-based updates. Automatic polling/push has not been implemented or proven by this session.
- Current workaround: refresh the unit page to retrieve new messages.
- Disposition: record as usability feedback and a proposed enhancement for Liam Pheng to triage. Do not label the enhancement fixed, silently change requirements or claim a second run.
- Follow-up: if approved, specify an update interval and transport, preserve membership/session enforcement on every read, and test visibility from two separate sessions.

## Relationship to Milestone 13

This is real reported human use of the hosted application and useful evidence for the demo. It does **not** establish that an uncoached tester cloned, installed, configured and ran the repository in a clean environment. Liam Pheng's admin participation also means it was not the required silent repository-only protocol. No documentation fixes or post-fix rerun were reported. The separate clean-machine record remains incomplete.
