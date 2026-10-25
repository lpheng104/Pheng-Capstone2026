# Project Status: Construction — Week 9
**Owner:** Liam Pheng |
**Project Name:** Accountabilibuddy | **Last Update** 2026-10-25

[![CI](https://github.com/lpheng104/Pheng-Capstone2026/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lpheng104/Pheng-Capstone2026/actions/workflows/ci.yml)

## Run it

Prerequisites: **Python 3.12.14**, Git, and a running **MongoDB 8.0.17** server reachable on `127.0.0.1:27017`. MongoDB is a real service, not a Python dependency or test mock. If Docker is available, start an isolated local instance with:

```sh
docker run --name accountabilibuddy-mongo --publish 127.0.0.1:27017:27017 --detach mongo:8.0.17
```

From a fresh checkout on Windows PowerShell:

```powershell
git clone https://github.com/lpheng104/Pheng-Capstone2026.git
Set-Location Pheng-Capstone2026
py -3.12 script/setup
.\.venv\Scripts\python.exe script/start
```

On Linux/macOS, with the pinned Python selected:

```sh
git clone https://github.com/lpheng104/Pheng-Capstone2026.git
cd Pheng-Capstone2026
python3 script/setup
.venv/bin/python script/start
```

The one-command setup creates `.venv`, installs **only from `requirements.lock` with verified hashes**, generates local secrets in ignored `.env`, applies migration 0001 and seeds fictional records. It refuses to seed a database whose name is neither `*_skeleton` nor `test_*`. For a non-default MongoDB endpoint, copy `.env.example` to `.env` and edit its configuration before setup. Do not use real unit/personnel information.

Open [the local application](http://127.0.0.1:5000). Sign in as **skeleton_member**, using the generated `SKELETON_PASSWORD` in your local `.env`. The dashboard links **Skeleton Demo Unit**. Its page must visibly show **Skeleton database row**, **Synthetic Formation**, and **attending**. Credentials are never printed by setup or committed. The Flask server is local development only; it is not a production deployment.

In a second terminal, verify all stages on Windows:

```powershell
.\.venv\Scripts\python.exe script/lint
.\.venv\Scripts\python.exe script/test
.\.venv\Scripts\python.exe script/build
.\.venv\Scripts\python.exe script/smoke --mutation-proof
.\.venv\Scripts\python.exe script/audit.py
```

On Linux/macOS replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`. Smoke success prints `SMOKE PASS` and exits zero. `--mutation-proof` temporarily changes a seeded message directly in MongoDB, verifies the change in real HTTP HTML, then restores it. Stopping the isolated datastore must make the same smoke command print `SMOKE FAIL` and exit nonzero. Build emits `dist/accountabilibuddy-skeleton.zip`, excluding secrets, dependencies and database binaries. The audit command downloads checksum-verified official Gitleaks if needed.

Repository guide: application components are in `src/{web,identity,unit_access,messaging,scheduling,persistence,maintenance}`; shared templates/static files are alongside them. `migrations/` holds versioned validators/indexes. `script/` holds runnable verbs; `.github/workflows/ci.yml` runs install → lint → test → build → live smoke on every push and PR into main. Unit tests explicitly use mocks; smoke uses real MongoDB. [Skeleton trace and acceptance evidence](docs/skeleton-trace.md), [issue drafts](docs/week9-issues.md), and [credential rotation](docs/secret-rotation.md) record remaining remote evidence. The [verified green main run](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/40233100468) and [deliberately red proof run](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/40232422421) are recorded in the skeleton trace; copyable submission links are in [week9-submission.md](docs/week9-submission.md).


## What's New 
- Architecture.md is now completely filled out
- check-spec.yml is now a workflow that can be ran from Actions 

## Fixes
- None

***
# Table of Contents
1. What has been Added
2. Fixes
3. Introduction
4. How to Navigate
5. What is Missing

### Introduction
This repository was built by Liam Pheng, a Senior at Concordia University-Wisconsin, for his Senior Capstone Project. When completed, this will be the repository of a Military Focused Communication and accountability app, with text chat and calendar event features. 

### How to Navigate
This repository has been organized into several folders which are crucial to later portents of the project. Here is a list of what is where and what their purposes are:

- **.github/workflows** = This is where all GitHub automation will be stored. Week 9 source/automation is implemented; see the Run it section above
- **docs/** = Is the folder containing all documentation and planning regarding this project. The important files to read would be the Project Charter, the Hour-log, and the AI-usage log.
- **src/** = This is reserved for the project's source code. Week 9 source/automation is implemented; see the Run it section above
- **tests/** = This is reserved for project testing material. Application/service regressions are in tests/, and live integration is exercised by script/smoke
- **.gitignore** = Contains specified files that Git will not be able to track. Week 9 source/automation is implemented; see the Run it section above
- **CHANGELOG.md** = This is where all noteable changes to the project will be stored
- **LICENSE** = This is where the project license is held
- **README.md** = This is what you are reading right now! It is a detailed explanation and instruction manual of how to operate the software and navigate the repository. It is also an updated notification log discussing the Project Progress

**Project Board**: 
This can be navigated to by clicking the "Projects" tab on the top of the repository menu. This project board shows what is currently being worked on, what has been completed, and what future features are planned to be added.

### What is Missing
The walking skeleton is implemented and verified through real MongoDB and CI. Full product features, Render/Atlas acceptance, broader non-functional measurements and personal code review remain tracked separately; see docs/skeleton-trace.md.
