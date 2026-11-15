# Milestone 12 release candidate gates

Recorded before candidate evaluation: 2026-11-15 Central. Baseline: `dc9ea326e0b5f1b22952408a0663ef3660582fc7`. Owner: Liam Pheng; instructor: Dr. Litman.

| Gate | Pass threshold |
|---|---|
| Clean checkout | Fresh Linux checkout can install from hash lock, migrate, seed, run the full CI suite and serve HTTP; zero unexpected failures or integration skips. |
| Seam coverage | Every mapped Tier 1 seam has a real-process test; unavailable database produces bounded 503 without leaking raw diagnostics. |
| Performance | 20 authenticated sequential GETs after one warm-up at 50 members, 100 messages and 25 events: p95 ≤1.5 s and every HTML body ≤512,000 bytes. Repeat the same workload after a fix. |
| Security | Seven areas reviewed, no unaddressed high/critical finding, verified advisory sources and Liam Pheng review. |
| Scope control | REJECT and DEFER decisions written by Liam Pheng; any approved deferral preserves criteria and links to the backlog. |
| Product readiness | 28/28 Must requirements verified and no open S1/S2 defects. |
| Candidate publication | Annotated tag on approved commit, pushed; exact tagged checkout passes. |

Results are recorded separately in the candidate evidence; an expected failure does not verify a requirement.

## Evaluation — 2026-11-15 Central

Tested application commit: `2b2356597e57d3159494c3c508f01dfb65faff2c`.
[Clean branch CI, run 43773631970](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/43773631970).

| Gate | Result |
|---|---|
| Clean checkout | **PASS for review commit.** Ubuntu 24.04 runner installed the updated hash lock, migrated and seeded real MongoDB, then passed 70 cases with 4 strict expected failures, no unexpected failures, and no integration skips. |
| Seam coverage | **PASS for CI seams.** Live synthetic HTTP/MongoDB smoke and iteration acceptance passed. Real stop returned sanitized 503 with Retry-After in 2.339 s; health recovered in 0.345 s after restart and smoke passed again. Hosted candidate routing and comprehensive acknowledged-write verification remain untested. |
| Performance | **PASS locally; hosted qualification pending.** 20 warm requests; final candidate p95 47.340 ms and 113,550 B HTML. NFR-PERF-01/02 remain unverified against their deployed condition. |
| Security | **PASS** Seven evidence areas; 21 pinned packages rescanned with zero known matches after fixes. Open authorization defects and incomplete coverage are not accepted. |
| Scope control | **PASS** Proposed REJECT and DEFER are documented; |
| Product readiness | **FAIL.** 6/28 Must criteria sets fully verified; two S2 feature defects remain open. No full product release claim. |
| Candidate publication | **APPROVED**|
