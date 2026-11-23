# Milestone 13 clean-machine evidence — reported solo fallback

Owner/tester: Liam Pheng. Instructor: Dr. Litman. Recorded 2026-11-22 from the owner's account of a run performed on 2026-11-20. This is a human owner-run check, not an assistant-run test or an independent uncoached tester run.

## Run header

- Session: Friday, November 20, 2026, 19:30–20:00. Time zone was not supplied.
- Environment: Liam Pheng's PC, described by Liam Pheng as a fresh environment/version. He reported downloading the repository and all dependencies. Exact OS, browser and dependency versions were not supplied.
- Database: the existing shared MongoDB Atlas database. Liam Pheng added the machine's IP to the Atlas access list. This was not a fresh database or a new seed-data run.
- Repository/commit used: not recorded. Do not substitute the later Milestone 13 documentation commit.
- Observer and repository-only/silence protocol: not applicable to an owner solo run; not claimed.
- Evidence source: Liam Pheng's account in this conversation, not a command transcript, recording or server log.

## Reported actions and results

All actions below were reported within the 19:30–20:00 session. Individual timestamps, commands and console outputs were not supplied. The 30-minute window is not an instrumented acceptance-action duration.

| Action | Reported observation | Evidence limit |
|---|---|---|
| Download repository | Completed on Liam Pheng's PC | Exact revision and download/clone command not supplied |
| Install dependencies | Liam Pheng reported downloading all dependencies in the fresh environment | Exact install commands, versions and outputs not supplied |
| Configure Atlas access | Added the machine's IP to the access list and connected to the same existing database | No credentials, IP or connection string included in this record |
| Access existing accounts | Worked | Exact account, browser URL and authentication sequence not recorded |
| Access existing chats | Worked because the application used the same Atlas database | No new message, attendance write, fresh-data seed or additional acceptance action inferred |

**Reported outcome:** the repository setup and access check worked without issues according to Liam Pheng. It supports the assignment's labeled solo fallback, subject to the missing execution detail and clean-environment evidence. It is not a full-credit independent tester protocol.

## Friction and fixes

Liam Pheng reported no issue in this November 20 run. No friction quote, corrective commit or post-fix result is fabricated. No documentation change is attributed to a problem observed during this run.

A separate [November 18 hosted check](hosted-user-test-2026-11-18.md) involved Nikita Adamov and administrator-assisted unit membership. Nikita's relayed feedback concerned messages requiring page refresh. That feedback is not retroactively attributed to the November 20 setup run and has not been claimed fixed.

## Rerun

No second repository run has been reported. The owner reported no fix was needed for the November 20 check; there is no fix/rerun cycle to certify. If a later reader finds documentation friction, record the exact quote, commit the correction and capture the actual subsequent run.

## Documentation verification still to supply

The current documentation draft was written after this run. The November 20 report therefore does not establish that its commands were followed in order. Record actual commands and sanitized outputs in [command-verification.md](command-verification.md) when independently executing the revised instructions. Do not infer missing outputs from CI.

For a future independent run, give a non-owner tester only the repository URL in a genuinely clean environment, observe silently and stop at 60 minutes. Record the tested SHA and actual checkpoint times. Proposed acceptance action for that future run: sign in, open the seeded unit, verify the stored message/event, change an attendance response and refresh to verify persistence, then sign out and confirm protected access is denied. This action was proposed on November 22; it was not defined retrospectively as the November 20 acceptance action.
