# Accountabilibuddy

Owner: Liam Pheng · Instructor: Dr. Litman · Documentation draft: 2026-11-22.

## 1. What it is, audience and non-goals

A Flask/MongoDB web demo for fictional military-style unit communication, events and attendance intentions. Intended for course evaluation and successor development, not operational military use or sensitive personnel data. Accounts, a unit-wide chat, events, attendance responses and unit roles exist. Native mobile apps, offline use, real-time push, isolated subgroup chat and a supported member-removal workflow are not delivered. The last recorded Milestone 11 suite had 70 passes and four strict expected failures; this is not full requirement acceptance. Read the [defect log](docs/defect-log.md) before adopting it.

## 2. Demo

[Public demo](https://accountabilibuddy-demo.onrender.com) · [recorded iteration-one demo](https://github.com/lpheng104/Pheng-Capstone2026/releases/download/iteration-1/iteration-1-demo.webm).

Use fictional data. A new registrant initially has no units; a unit leader must add the username. Administrator registration requires the configured username and a private setup token. Neither the setup token nor an Atlas login is an application password. See the [hosted deployment record](docs/render-demo-verification.md), dated November 2; it is not a fresh availability check. The free hosting instance can need time to wake up.

## 3. Prerequisites and checks

Canonical local instructions below use **Windows PowerShell**, a new checkout, and MongoDB listening only on loopback. Linux CI is separate engineering evidence. Do not use an Atlas URI for these local seeded steps.

| Prerequisite | Check command | Expected signal | If it differs |
|---|---|---|---|
| Git; drafting machine reports 2.56.0.windows.4 | `git --version` | `git version 2...`; record your exact version | Install Git from its official distribution; restart the terminal if not found. |
| Python exactly 3.12.14 | `python --version` | `Python 3.12.14` | Select the pinned interpreter; setup rejects a different patch. Do not edit the pin merely to bypass that check. |
| MongoDB server 8.0.17 | `mongod --version` | First version line `db version v8.0.17` | Install the pinned official server or use the Docker alternative below. A Python MongoDB driver is not a running server. |
| Disposable loopback MongoDB | `Test-NetConnection 127.0.0.1 -Port 27017 -InformationLevel Quiet` | `True` | Start the isolated server first; `False` means setup cannot connect. |

MongoDB must already be running before install/setup. If using Docker instead of native MongoDB, check `docker version` first: both Client and Server sections must appear. Then:

```powershell
docker run --name accountabilibuddy-m13 --publish 127.0.0.1:27017:27017 --detach mongo:8.0.17
```

Expected: a generated container ID, not a fixed string. A port conflict means another server already uses 27017; do not stop it without identifying its owner. A Docker daemon error means Docker is not running. This Docker path has **not** been run by the human tester for this milestone; actual versions/output belong in the [command record](docs/command-verification.md).

## 4. Install

```powershell
git clone https://github.com/lpheng104/Pheng-Capstone2026.git
Set-Location Pheng-Capstone2026
```

Expected: Git completes the clone without error; PowerShell changes to the cloned directory. A clone of `main` will not contain unmerged documentation changes. For the pre-merge documentation trial only, after cloning use:

```powershell
git switch --track origin/codex/milestone-13-review
```

Expected: the review branch is selected. This command will no longer apply if the remote review branch has been deleted; use the final reviewed commit instead. The tester must discover this instruction from the repository, not receive a verbal branch hint.

```powershell
python script/setup
```

Expected success signals: dependencies install from `requirements.lock` with hash checking, `APPLIED 0001` (or `ALREADY APPLIED 0001` on repeat), then `SEEDED`, `START with script/start` and a generated `UNIT /units/...` URL. Exact IDs are variable. Exit must be zero. Setup creates `.venv` and ignored `.env`, migrates and seeds; it is not just a package install. Do not proceed after `COMMAND FAILED: ...`.

## 5. Configure

Open the newly generated `.env` privately. Do not publish it, paste it into an issue, or show it in a recording.

| Variable | Local meaning |
|---|---|
| SECRET_KEY | Generated signing secret; stable across app restarts; changing it invalidates cookies. |
| MONGODB_URI | Default local MongoDB URI; contains credentials when using Atlas. |
| MONGODB_DATABASE | Default `accountabilibuddy_skeleton`; setup permits only dedicated `*_skeleton` or `test_*` names. |
| ADMIN_USERNAME | Default `skeleton_admin`; the one global admin username, not a pre-created account. |
| ADMIN_SETUP_TOKEN | Generated private code for initial admin registration; not a login password. |
| COOKIE_SECURE | `false` for local HTTP; `true` for Render HTTPS. |
| SKELETON_PASSWORD | Generated password for synthetic fixture accounts; setup does not print it. |

For hosted configuration use [Render operations](docs/render-demo.md). Provider environment values override `.env`. Never copy the hosted URI into the local clean-machine run. Stopping your laptop does not stop Render or Atlas.

## 6. Run and acceptance action

```powershell
.\.venv\Scripts\python.exe script/start
```

Expected: Flask serves `http://127.0.0.1:5000` with debug off; the terminal stays occupied. Local port 5010 used in earlier sessions was an explicit override, not the default. Open the displayed loopback URL in the browser on this machine.

**Acceptance action defined before the human run:** sign in as `skeleton_member` using the generated `SKELETON_PASSWORD`; open Skeleton Demo Unit; confirm Skeleton database row and Synthetic Formation; change the attendance response, save, refresh and confirm it persists; sign out and confirm the unit cannot be opened without signing in. This tests local setup and persistent behavior, not all requirements. Never put the actual password in the tester's transcript.

Stop with Ctrl+C in the server terminal. Restart by running the same start command; expected result is the same URL with stored records intact. Do not run the development server as the public host; Render uses Gunicorn.

## 7. Test

In a second PowerShell terminal, in the checkout:

```powershell
$env:M11_MONGO_PORT='27017'
.\.venv\Scripts\python.exe -m pytest -q -rx
```

Expected baseline signal: `70 passed, 4 xfailed`, exit zero, and all three real integration tests executed. Durations and warnings vary. An `xfail` is an open known defect, not a passed requirement. Missing M11_MONGO_PORT skips the three integration tests and is not a valid full run. The tests create and drop only uniquely named `test_m11_*` databases on the specified loopback port.

With the local server still running:

```powershell
.\.venv\Scripts\python.exe script/smoke --mutation-proof
```

Expected: `SMOKE PASS: direct MongoDB update appeared in rendered HTML; original row restored.` followed by the real HTTP/MongoDB path success message; exit zero. This temporarily changes and restores a synthetic message. Never target the public demo or real data with it.

The [CI workflow](.github/workflows/ci.yml) runs pinned setup, lint, secret scanning, tests, fixture/matrix checks, build and real HTTP smoke. CI is not the human clean-machine test. [Test results](docs/test-results.md) identify their own tested commit. Milestone 12's `v0.9.0-rc.1` is a separate tagged candidate; it has not been silently merged into this branch.

## 8. Project layout

| Path | Responsibility |
|---|---|
| `src/app.py` | Flask factory, form POSTs, CSRF, global admin and unit permissions |
| `src/web`, `identity`, `unit_access`, `messaging`, `scheduling`, `persistence` | Authorized reads, session lookup, MongoDB gateway and rendering |
| `src/maintenance`, `migrations`, `seed` | Synthetic data and schema ledger |
| `tests/unit`, `integration`, `acceptance`, `data` | Deterministic candidate assertions and real MongoDB checks |
| `script` and `.github/workflows` | Cross-platform commands and CI |
| `docs` and `docs/adr` | Requirements, evidence, operations and decision history |

## 9. Troubleshooting

| Symptom | Next action |
|---|---|
| `COMMAND FAILED: ServerSelectionTimeoutError` | Check MongoDB availability and target configuration before retrying. |
| `OperationFailure` against Atlas | Check database-user credentials and scoped Network Access, not the Atlas website login. |
| Existing administrator username | Sign in with its chosen password; setup token does not reset that password. |
| No unit assigned | Ask an authorized leader to add the registered username; do not change the database directly. |
| Tests show four xfails | Read DEF-M11-05/06/07/09; do not delete the expected failures to make results look complete. |

See [runbook](docs/runbook.md) for the defect-based failure catalogue and recovery limits. Record new friction verbatim in the [human test form](docs/clean-machine-test.md).

## 10. License

[MIT](LICENSE), copyright 2026 Accountabilibuddy contributors. The license applies to project source, not ownership of hosted provider services or user data. Keep third-party license notices when redistributing dependencies.

## 11. Contact and further reading

Maintainer: Liam Pheng, via [repository issues](https://github.com/lpheng104/Pheng-Capstone2026/issues); course reviewer: Dr. Litman. Never post credentials or sensitive unit information. Start with [architecture §0](docs/architecture.md#0--overview-as-built), [onboarding](docs/onboarding.md), [ADR index](docs/adr/README.md), [requirements](docs/requirements.md) and [AI disclosure](docs/ai-usage.md).

**Evidence boundary:** these are AI-assisted documentation instructions with historical engineering evidence. Liam Pheng and the real tester must execute and record them independently. The [command ledger](docs/command-verification.md) distinguishes observed history from uncompleted human verification. A successful assistant or CI run cannot fill the human test form.
