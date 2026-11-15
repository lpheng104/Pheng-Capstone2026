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
