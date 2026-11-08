# Milestone 11 test results

Owner: Liam Pheng. Instructor: Dr. Litman. Run date: 2026-11-08 (Central).

## Committed CI run

[GitHub Actions run 42529825389](https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/42529825389)
passed on November 8, 2026 against commit `4c992b060d7987c2292eb1140eed6fa13073616d`.
Runner: Ubuntu 24.04, Python 3.12.14, disposable MongoDB 8.0.17.
Command: `.venv/bin/python -m pytest -q -rx --junitxml=<runner-temp>/milestone11-junit.xml`
with `M11_MONGO_PORT=27017`.

The uploaded JUnit report records **70 passed, 4 strict expected failures,
0 unexpected failures, 0 other skips**, including all three real MongoDB tests.
Suite duration: **31.80 s**. CI also passed fixture
reproduction, matrix audit, lint, credential scan, build and the live HTTP gates.
This evidence update changes documentation only; it does not change the tested code.

## Local full run and baseline reproduction

The full local run tested a review candidate derived from commit `c5b89372a9f77579e01c75f73d155e8824918450`.
The candidate was uncommitted at run time. SHA-256 of the tested source/fixture file manifest:
`7b3b7fd785f69249325a9bce85cafcd7b423c683d4e0f3b4909e488c28723e55`. The observed cases and timings are in
[milestone-11-run.json](milestone-11-run.json); the committed CI observation is recorded above.

Environment: Windows course laptop, Python 3.12.14; MongoDB 8.0.17 loopback:27019. No connection to Atlas or Render was used.

```powershell
$env:M11_MONGO_PORT='27019'
python -m pytest -q -rx --junitxml=../m11-candidate.xml
```

| Result | Observed |
|---|---:|
| Collected | 74 |
| Passed | 70 |
| Unexpected failures | 0 |
| Strict expected failures (known open defects) | 4 |
| Skips excluding expected failures | 0 |
| Real MongoDB integration tests passed | 3 |
| Elapsed (JUnit) | 110.99 s |

The exact baseline source was archived from Git, then run with the same ten regression
assertions using `pytest --runxfail` and a case-ID filter. All ten failed (exit 1) in
14.69 s. Six of those criterion cases now pass
after five feedback fixes. Four still reproduce open gaps. This is before/after
evidence, not an artificial failure or a fixed-defect count based on green alone.

## Verified requirement coverage

Run `python code/coverage_report.py`. A requirement is verified only if every
criterion passed. Partial, failed, not-run and gap rows never count as verified.
These are candidate technical results pending Liam Pheng’s assertion approval.

| Measure | Result |
|---|---:|
| Total requirements | 43 |
| Verified requirements | 8 |
| Verified-requirement coverage | 8/43 (18.6%) |
| Verified-Must coverage | 6/28 (21.4%) |

Verified IDs: FR-ACCT-01, FR-ACCT-02, FR-ACCT-03, FR-ACCT-04, FR-ACCT-05, FR-ACCT-06, FR-CLNDR-03, NFR-SEC-02.
The matrix contains 136 criteria; status counts are
failed: 4, gap: 84, not-run: 11, partial: 12, passed: 25.
All 28 Must requirements are mapped to at least one executable case or numbered manual procedure.
Manual cases were not run, and the controlled HTTP client does not constitute browser evidence.

## Exit gate check

| Gate | Result |
|---|---|
| 0 unexpected failures | Met locally |
| At least 3 real integration tests, no skips | Met: 3 passed |
| All 43 requirements represented; every Must mapped | Met: 43/43 and 28/28 |
| At least 8 reproduced defects | Met: 9, including 5 fixed in draft |
| 100% verified Must and no open S1/S2 | **Not met**: 6/28 Must verified; 2 new S2 defects open |
| 100% suite pass within 60 s (NFR-MAINT-01) | **Not met in this run**: 4 expected failures; 110.99 s |

Pytest exited zero for the regression gate, which permits only specifically identified,
strict expected failures. It does not mean the release gate passed. Existing
mongomock datetime deprecation warnings remain; no warnings were hidden to change results.
