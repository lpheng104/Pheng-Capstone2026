# Ten-minute successor orientation

Owner: Liam Pheng. Draft date: 2026-11-22. Audience: an engineer new to this repository.

**Minutes 0–2:** read README §1 and the known defects. A running demo is not a complete requirements implementation. Distinguish main from the unmerged Milestone 12 tag before choosing what to run.

**Minutes 2–4:** read architecture §0 and the ADR index. User identifies a registered account; membership links it to a unit; role grants unit actions. Rank is display text, not an authorization grant. Attendance is an intention, not verified physical presence. Global admin is the one configured username; unit owners/leaders are different.

**Minutes 4–7:** inspect the feature map. Do the human setup run separately; ten minutes of orientation is not a promise that the dependencies install in ten minutes.

| Feature | Entry / implementation | Evidence |
|---|---|---|
| Register, sign in, password change | `src/app.py`, `src/identity/__init__.py`, `src/templates/auth.html`, `password.html` | `tests/test_app.py`, `tests/test_iteration1.py` |
| Unit membership and role checks | `src/app.py`, `src/unit_access/__init__.py` | `tests/acceptance/test_m11_criteria.py` |
| Unit chat | `src/messaging/__init__.py`, POST routes in `src/app.py`, `unit.html` | Message boundary and escaping cases |
| Events and attendance | `src/scheduling/__init__.py`, POST routes in `src/app.py` | Event date, denial and deletion cases |
| Setup, schema and seed | `script/manage.py`, `migrations/run.py`, `src/maintenance/__init__.py` | Real MongoDB tests and live HTTP CI |

**Minutes 7–10:** read the first task below, the defect log, and work policy. Ask for clarification before changing a requirement or a credential.

## First task — DOC-13-01 ([unassigned issue #54](https://github.com/lpheng104/Pheng-Capstone2026/issues/54))

**Title:** explain a missing virtual environment in script launchers. **Status:** open and unassigned when created on 2026-11-22; check the issue before claiming it.

The launchers assume the checkout's `.venv` Python executable exists. If setup has not completed, `script/test` and `script/smoke` can raise an unhelpful missing-executable traceback. This wrapper pattern exists in source; an earlier smoke invocation exposed WinError 2. Reproduce it on a disposable checkout before writing the fix. No Atlas connection or real user account is needed.

Acceptance: missing `.venv` produces a concise nonzero error directing the reader to `python script/setup`, with no traceback; an existing environment still launches the command and propagates its exit status; subprocess tests cover both cases on supported platforms; update troubleshooting with the actual observed symptom. Proposed size: 1–2 hours, subject to re-estimate after reproduction. Do not install automatically or silently connect to a configured hosted database. Claim the issue before starting.

## How work moves

Use a branch from current main and a draft PR. Map changes to the existing requirement/criterion ID. Write a red regression first for a confirmed defect, keep inputs fictional, run the documented tests, record AI contributions and actual hours yourself. Never put passwords, Atlas URIs or personal data in commits. Explain strict xfails in the PR; do not remove them to inflate pass counts. Liam Pheng reviews assertions and scope changes before merge. Main, a release tag and the active Render deployment can differ; verify the actual commit before announcing a release.

Decisions live in `docs/adr/`, requirements in `docs/requirements.md`, test status in `docs/traceability.csv`, and open defects in `docs/defect-log.md`. Read historical ADR statuses literally; an implementation observation is not a retroactive signature.
