# Milestone 12 performance evidence

Owner: Liam Pheng. Measured November 15, 2026 Central. Baseline `dc9ea326e0b5f1b22952408a0663ef3660582fc7`; candidate batches member and attendance reads (DEF-M12-01).

Both runs used a fresh standalone Flask HTTP process on the Windows development machine with Python 3.12.14 and disposable MongoDB 8.0.17. Each run applied the real schema and inserted 50 members, 100 messages, 25 events and 625 responses. The client signed in as the fictional owner, discarded one warm-up, then made 20 sequential authenticated GETs. Elapsed time is client-observed full response time; p95 is the 19th ordered observation. HTML bytes exclude CSS. The demo on Render/Atlas was not modified or seeded. The local environment is a controlled comparison, not the deployed environment required by the SRS.

| Target | Run | Sample | p50 | p95 | Verdict and action |
|---|---|---:|---:|---:|---|
| NFR-PERF-01: ≤1,500 ms | Baseline, fresh local HTTP | 20 | 102.410 ms | 127.199 ms | Local threshold passed; repeated per-member and per-event queries motivated batching. |
| NFR-PERF-01 | Candidate, same local method | 20 | 45.577 ms | 57.713 ms | Local threshold passed; p95 improved 54.6%. Deployed verdict pending a same-volume hosted candidate run. |
| NFR-PERF-02: ≤512,000 bytes | Baseline, fresh local HTTP | 20 | 113,550 B | 113,550 B | Every measured body was below the threshold. |
| NFR-PERF-02 | Candidate, same local method | 20 | 113,550 B | 113,550 B | No body-size regression; deployed verdict pending. |

The final candidate with the three patched pins was remeasured using the same fresh process and fixture: n=20, p50 **38.833 ms**, p95 **47.340 ms**. Body p50/p95 **113,550 B**. Both local thresholds passed. [All raw samples](evidence/m12-performance.json).

Reproduce: `python code/measure_http.py --mongo-port 27020 --requests 20` with the locked Python environment and a disposable MongoDB bound to loopback. `--source PATH` selects a checkout for the running server; use the same fixture script for both revisions. The program cleans up only its uniquely named database and subprocess.

## Other Week 4 non-functional targets

Security, recovery, accessibility, usability and process targets are not latency distributions. Their required observations and missing evidence are tracked in the criterion matrix and the RC evidence. No p50/p95 or participant results are invented for those targets. The RC does not claim that every Week 4 NFR has been independently reverified.
