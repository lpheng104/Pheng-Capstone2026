# Week 7 build plan — Accountabilibuddy

Date: 2026-10-11. Owner: Liam Pheng. Status: **Working draft**

## Work breakdown and estimate inputs

For the final baseline: **E = (O + 4M + P) / 6; calibrated E = E × k**. For this M-only draft, the last numeric column is **calibrated M = M × k**. It is a provisional scheduling value, not a computed three-point expected value.

| Task | Package / task | Requirement trace or enabling justification | O | M | P | E | Calibrated E | Done when | Dependencies |
|---|---|---|---|---|---|---|---|---|---|
| T-1.1 | WP-1 Baseline: reconcile requirement IDs | NFR-MAINT-02 | Pending | 2 | Pending | Pending | Pending | Legacy matrix matches approved 0.4 IDs and checker passes | — |
| T-1.2 | WP-1: inspect current code against target contracts | Enabling: avoid re-estimating completed implementation | 2 | 3 | 4 | 3.00 | 2.49 | Each contract is marked evidenced or a named gap with task ID | T-1.1 |
| T-1.3 | WP-1: approve estimates, capacity, scope and design | Enabling: Week 8 review | 2 | 3 | 4 | 3.00 | 2.49 | Liam Pheng's inputs complete; review decision and baseline commit recorded | T-1.2 |
| T-2.1 | WP-2 Data: verify migration and indexes | NFR-PRIV-01, NFR-REL-02 | 2–3 | 4 | 5–6 | 3.83–4.17 | 3.19–3.46 | Disposable real database has specified validators/indexes and migration ledger | T-1.3 |
| T-2.2 | WP-2: verify atomic unit/owner creation | FR-UNIT-01, NFR-REL-02 | 3 | 4 | 5 | 4.00 | 3.32 | Injected owner-write failure leaves no orphan unit in real replica set | T-2.1 |
| T-2.3 | WP-2: configure hosted workflow spike | NFR-PORT-01, FR-HEALTH-01 | 3 | 5 | 6–7 | 4.83–5.00 | 4.02–4.15 | SP-02 executed with build/runtime evidence and explicit pass/fail | T-2.1, T-3.2 |
| T-2.4 | WP-2: exercise backup, restore and outage | NFR-REL-02 | 3–4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | SP-03 comparisons saved and separate outage/recovery threshold measured | T-2.1, T-2.2 |
| T-3.1 | WP-3 Identity: verify registration and admin token | FR-AUTH-01, FR-AUTH-03 | 1 | 2 | 2+ | ≥ 1.83 | ≥ 1.52 | Unique normalization, password bounds/hash and setup-token cases pass | T-1.3 |
| T-3.2 | WP-3: verify sessions and logout replay | FR-AUTH-02 | 1 | 2 | 3 | 2.00 | 1.66 | Expired and revoked tokens cannot access protected views | T-3.1 |
| T-3.3 | WP-3: complete CSRF and login throttle cases | NFR-SEC-02, FR-AUTH-02 | 2 | 3 | 4+ | ≥ 3.00 | ≥ 2.49 | Every POST rejects missing/tampered CSRF without mutation; throttle edge cases pass | T-3.2 |
| T-3.4 | WP-3: audit role and cross-unit access | FR-ACCESS-01, NFR-SEC-01 | 2–3 | 4 | 5+ | ≥ 3.83 | ≥ 3.19 | Route-by-role matrix denies all forbidden reads/writes with zero mutations | T-3.3, T-4.2, T-5.3 |
| T-4.1 | WP-4 Membership: verify add-member workflow | FR-UNIT-02 | 1 | 2 | 3 | 2.00 | 1.66 | Registered user gains access; duplicate add cannot downgrade owner | T-2.2, T-3.2 |
| T-4.2 | WP-4: verify roles and rank labels | FR-UNIT-03 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | Only owner can edit non-owner role/rank; owner invariant preserved | T-4.1 |
| T-4.3 | WP-4: verify latest-message list | FR-MSG-01 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | Seeded list returns latest 100 with stable chronological display | T-4.1 |
| T-4.4 | WP-4: verify message input and escaping | FR-MSG-02, NFR-SEC-04 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | Length boundaries and authorization pass; all displayed text fields escape markup | T-4.3 |
| T-5.1 | WP-5 Events: verify creation/time validation | FR-EVT-01 | 2 | 3 | 4 | 3.00 | 2.49 | Role and offset-aware timestamp tests pass without invalid writes | T-4.2 |
| T-5.2 | WP-5: verify attendance upsert | FR-EVT-02 | 2 | 3 | 4 | 3.00 | 2.49 | Repeated/concurrent responses leave one latest record; cross-unit event rejected | T-5.1 |
| T-5.3 | WP-5: verify accountability roster | FR-EVT-03 | 1 | 2 | 3 | 2.00 | 1.66 | Leaders see responses and pending current members, including later additions | T-5.2 |
| T-6.1 | WP-6 Quality: check corrective validation messages | NFR-USE-02 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | All eight specified invalid-input cases give corrective information | T-4.4, T-5.3 |
| T-6.2 | WP-6: audit desktop/mobile accessibility | NFR-A11Y-01, NFR-A11Y-02 | 3–4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | Dated axe results meet threshold and all five keyboard workflows pass | T-6.1 |
| T-6.3 | WP-6: measure hosted latency and response size | NFR-PERF-01, NFR-PERF-02 | 1–2 | 3 | 4+ | ≥ 2.83 | ≥ 2.35 | Specified seeded dataset and raw deployed measurements meet thresholds | T-2.3, T-5.3 |
| T-6.4 | WP-6: run representative-user exercise | NFR-USE-01 | 3–4 | 5 | 6 | 4.83–5.00 | 4.02–4.15 | Consent/fictional-data conditions cleared; five anonymized task-result records meet target | T-6.2 |
| T-6.5 | WP-6: repeat clean regression and platform smoke | NFR-REL-01, NFR-MAINT-01, NFR-PORT-01 | 3 | 4 | 5+ | ≥ 4.00 | ≥ 3.32 | Ten clean suite runs plus Windows/Render smoke results saved against stated thresholds | T-3.4, T-6.3 |
| T-7.1 | WP-7 Operations: complete health/failure handling | FR-HEALTH-01, NFR-REL-02 | 1–2 | 3 | 4 | 2.83–3.00 | 2.35–2.49 | Health and request deadline failures return specified responses without secret leakage | T-2.3 |
| T-7.2 | WP-7: scan secrets, hashes and dependencies | NFR-SEC-03 | 2 | 3 | 4 | 3.00 | 2.49 | Tracked-file and user-record checks clean; high/critical dependency findings resolved | T-6.5 |
| T-7.3 | WP-7: validate inventory and deletion procedure | NFR-PRIV-01, NFR-PRIV-02 | 3–4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | Document keys match inventory; verified deletion exercise and provider limitations recorded | T-2.4, T-5.3 |
| T-7.4 | WP-7: rehearse isolated local fallback | Enabling: R-01/R-02 response | 1–2 | 3 | 4–5 | 2.83–3.17 | 2.35–2.63 | Synthetic local replica-set workflow and fallback recording reproducible without Atlas | T-2.4, T-5.3 |
| T-8.1-W9 | WP-8: Week 9 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 9 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W10 | WP-8: Week 10 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 10 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W11 | WP-8: Week 11 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 11 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W12 | WP-8: Week 12 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 12 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W13 | WP-8: Week 13 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 13 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W14 | WP-8: Week 14 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 14 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W15 | WP-8: Week 15 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | Week 15 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.2 | WP-8: named defects when identified (contingent; not an estimated task) | Enabling: bounded defect closure against retained requirements | Not yet known | Not yet known | Not yet known | Not yet known | Not yet known | Named failed checks rerun successfully; no duplicate implementation charging | T-6.2, T-6.5, T-7.3 |
| T-8.3 | WP-8: reproduce release and demo | NFR-MAINT-01, NFR-MAINT-02 | 3 | 4 | 5 | 4.00 | 3.32 | Clean checkout builds; traceability and acceptance evidence complete; demo rehearsed | T-7.2, T-7.4, T-8.2 |
| T-8.4 | WP-8: retrospective and submission | Enabling: Week 16 final package | 4 | 5 | 6 | 5.00 | 4.15 | Estimate/actual analysis compares signed baseline with history; final artifact and commit link ready | T-8.1-W9, T-8.1-W10, T-8.1-W11, T-8.1-W12, T-8.1-W13, T-8.1-W14, T-8.1-W15, T-8.3 |

E = (O + 4M + P) / 6. Calibrated E = E × (85.83 / 103.30).
All values are hours, rounded to two decimals. Ranges remain ranges.
The ≥ symbol indicates a lower bound where an input uses +; it is not a final point estimate.

## Calibration from recorded history

| Completed task | Sessions | Estimated hours | Actual hours | Actual / estimate |
|---|---:|---:|---:|---:|
| Create repo + scaffold docs/ tree | 1 | 3.00 | 3.00 | 1.000000 |
| Create board + README.md | 1 | 3.00 | 1.75 | 0.583333 |
| Idea portfolio & scoping | 8 | 22.30 | 17.87 | 0.801345 |
| Software requirement specification | 13 | 39.00 | 32.05 | 0.821795 |
| Technology Evaluation & architecture decision records | 7 | 21.00 | 15.55 | 0.740476 |
| Technical Specification | 5 | 15.00 | 15.61 | 1.040667 |
| **Total** | **35** | **103.30** | **85.83** | **0.830881** |

**Calibration factor k = 85.83 / 103.30 = 0.8308809293**, displayed as 0.830881. Apply the unrounded factor once to every remaining task: **calibrated E = ((O + 4M + P) / 6) × (85.83 / 103.30)**. Round only displayed outputs. This is a ratio of totals, not a simple average of row ratios. It represents documented planning/design experience, not demonstrated implementation throughput; broad session estimates should not be mistaken for precise forecasts of unfamiliar engineering work.

## Capacity and separate buffer

Other-class overhead and personal/ROTC losses are already excluded from this stated availability, so they receive no additional deduction. The table does not claim those commitments consume no time; it avoids subtracting them twice. Project-specific milestone reporting is included in T-8.1 and consumes the planned-task budget.

| Week | Net availability supplied by Liam Pheng | Course overhead treatment | Known losses and reason | Project capacity baseline | Minimum buffer | Planned-task budget |
|---|---:|---|---|---:|---:|---:|
| 8 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 9 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 10 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 11 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 12 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 13 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 14 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 15 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| 16 | 15–16 h | Other classes already excluded | Personal/ROTC commitments already excluded | 15 h | 1 h | 14 h |
| **Total** | **135–144 h** | **Already excluded** | **Already excluded** | **135 h** | **9 h** | **126 h** |

**Declared minimum project buffer: 1 hour per week × 9 weeks = 9 hours**,. This is **6.67% of the 135-hour baseline project capacity** (9 / 135 × 100). The baseline scheduled-task budget is **135 − 9 = 126 hours**, or **14 hours per week**. If all 16 available hours are realized in every week, capacity is 144 hours and the same minimum buffer leaves 135 task hours; the buffer is then 6.25% of capacity. The baseline relies on 126 task hours rather than this optional upper bound.

## Proposed sequencing and weekly gates

| Week | Tasks in dependency order | Draft calibrated task hours | Unassigned task capacity | Gate |
|---|---|---:|---:|---|
| 8 | T-1.1, T-1.2, T-1.3, T-3.1, T-3.2, T-2.1 | 13.29 | 0.71 | Requirement reconciliation and review recorded; identity and real-database migration checks pass |
| 9 | T-2.2, T-2.3, T-2.4, T-8.1-W9 | 12.46 | 1.54 | Atomic unit creation, hosted workflow and restore/outage evidence pass or have recorded decisions |
| 10 | T-3.3, T-4.1, T-4.2, T-4.3, T-4.4, T-7.1, T-8.1-W10 | 12.46 | 1.54 | Membership, roles, messages, CSRF/throttling and health/failure checks pass |
| 11 | T-5.1, T-5.2, T-5.3, T-3.4, T-8.1-W11 | 10.80 | 3.20 | Events, attendance, roster and complete authorization matrix pass |
| 12 | T-6.1, T-6.2, T-6.3, T-7.3, T-8.1-W12 | 13.29 | 0.71 | Input guidance, accessibility, performance and privacy/deletion checks pass; trial conditions cleared |
| 13 | T-6.4, T-6.5, T-8.1-W13 | 8.31 | 5.69 | Usability exercise and repeated regression/platform checks pass |
| 14 | T-7.2, T-7.4, T-8.1-W14 | 5.82 | 8.18 | Security audit and independent local fallback pass; triggered defects individually estimated |
| 15 | T-8.3, T-8.1-W15 | 4.15 | 9.85 | Clean-checkout release and demo pass; all named mandatory defects closed |
| 16 | T-8.4 | 4.15 | 9.85 | Retrospective and final package complete; Liam Pheng posts submission commit URL |
| **Total** | **36 estimated tasks; contingent defects excluded** | **84.75** | **41.25** | Personal estimates and review still required |

## Burn-down baseline

**Provisional M-only baseline:** raw suggested M effort = **102.00 hours**; calibrated remaining effort R_M = 102.00 × (85.83 / 103.30) = **84.75 hours**. The 135-hour capacity includes nine buffer hours, leaving 126 task hours. This draft leaves **41.25 task hours unassigned**, separately from the nine-hour buffer. Unassigned capacity is not a task estimate, a scope cut, or evidence that defects take no time.

The ideal line decreases evenly across nine weeks: R_M × (9 − n) / 9 after n weeks. The projected line subtracts the calibrated M effort of tasks scheduled to meet their done-whens each week. Use unrounded calculations; displayed values are rounded to two decimals. Actual remaining effort is not recorded until task completion is demonstrated.

| Point | Ideal remaining (h) | Projected remaining (h) | Future task capacity (h) | Future capacity including buffer (h) | Over task capacity? |
|---|---:|---:|---:|---:|---|
| Start Week 8 | 84.75 | 84.75 | 126 | 135 | No |
| End Week 8 | 75.33 | 71.46 | 112 | 120 | No |
| End Week 9 | 65.92 | 58.99 | 98 | 105 | No |
| End Week 10 | 56.50 | 46.53 | 84 | 90 | No |
| End Week 11 | 47.08 | 35.73 | 70 | 75 | No |
| End Week 12 | 37.67 | 22.43 | 56 | 60 | No |
| End Week 13 | 28.25 | 14.12 | 42 | 45 | No |
| End Week 14 | 18.83 | 8.31 | 28 | 30 | No |
| End Week 15 | 9.42 | 4.15 | 14 | 15 | No |
| End Week 16 | 0.00 | 0.00 | 0 | 0 | No |

**First projected over-budget week: none in this provisional M-only schedule.** Every weekly allocation fits 14 task hours, and projected remaining effort fits future task capacity at every point. This result excludes unidentified defects and may change when Liam Pheng replaces draft suggestions with personal O/M/P estimates. A complete three-point baseline is not established by this calculation.

Capacity columns cover weeks after the stated point and assume future buffer is still available. In weekly reviews, record completed task IDs, actual effort, named defects, changes to capacity and buffer use. Preserve this draft and the later personally estimated baseline as distinct versions. Spending hours without meeting a done-when does not automatically burn down work.

## Scope decision and Week 8 change control

I explicitly chose to retain all current requirements on 2026-10-11. Requirements priorities remain unchanged; no Won't changes are appropriate.

| Decision | Requirements affected | Hours recovered | MoSCoW before to after | Reason |
|---|---|---|---|---|
| Retain all current requirements | All version 0.4 FR/NFR IDs | 0 (no scope removed) | Unchanged for every requirement | I think that the current requirements are good |
