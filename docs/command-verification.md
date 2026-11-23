# Documentation command verification ledger

Prepared 2026-11-22. **Personal execution not yet recorded.** Expected signals in README/runbook are instructions to verify, not invented human outputs. Do not mark them done from an assistant or CI check.

| Group | Commands / UI steps | Existing source of expected signal | Liam Pheng actual output/date | Status |
|---|---|---|---|---|
| Prerequisites | Git/Python/MongoDB versions, TCP check, optional Docker version/run | Version pin, migration requirements; Git drafting-machine check only | pending | pending personal verification |
| Checkout | clone, change directory, optional review-branch selection | Git semantics; exact target must be recorded by tester | pending | pending |
| Install | python script/setup | Source in script/manage.py; prior Linux CI, not human evidence | pending | pending |
| Run / restart | local script/start, Ctrl+C and same start command | Source defaults and prior development runs | pending | pending |
| Tests | M11_MONGO_PORT setting and full pytest command | November 8 CI recorded 70 pass / 4 xfail; current head must be rerun | pending | pending |
| Smoke | script/smoke --mutation-proof on disposable data | Existing CI real HTTP mutation check | pending | pending |
| Operations | local health request, optional Docker stop/start, Render manual deploy UI | App health handler and historical deployment record | pending | pending |

## Drafting corrections discovered from repository inspection

- Original README still described Week 9, linked deleted week9-submission.md, and mixed default port 5000 with an old 5010 override. Replaced with one canonical default and historical context.
- runbook.md and clean-machine-test.md contained only “week 13.” Replaced with a runbook and an explicitly uncompleted protocol, not a fabricated result.
- Legacy ADR filenames are “ADR 0001” through “ADR 0004,” not the .md filenames referenced by older design links. The new index points at actual files.
- The standalone Milestone 12 tag has not been merged into main. Do not claim its batching, patched pins or retry-header behavior as current main.

Correction rate: **not calculable until Liam Pheng executes the proposed command sequence**. There is no asserted 0% error rate. Record proposed executable-command count and corrected-command count using the same counting rule after the actual run.
