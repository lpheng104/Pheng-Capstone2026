# Week 7 build plan — Accountabilibuddy

Date: 2026-10-11. Owner: Liam Pheng. Status: **Working Draft.**

## Work breakdown and estimate inputs

**E = (O + 4M + P) / 6; calibrated E = E × (85.83 / 103.30)**. O/M/P below are imported unchanged from my supplied table. Single-number inputs produce an exact E; finite ranges produce an E range; a trailing + produces a lower bound with no stated maximum. The ≥ symbol denotes that lower bound, not a complete point estimate. Displayed results are rounded to two decimals; use unrounded values for totals. These calculations do not turn open-ended pessimistic estimates into finite estimates.

| Task | Package / task | Requirement trace or enabling justification | O | M | P | E from supplied inputs | Calibrated E from supplied inputs | Draft planning E | Draft calibrated planning E | Done when | Dependencies |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T-1.1 | WP-1 Baseline: reconcile requirement IDs | NFR-MAINT-02 | 1 | 2 | 3 | 2.00 | 1.66 | 2.00 | 1.66 | Legacy matrix matches approved 0.4 IDs and checker passes | — |
| T-1.2 | WP-1: inspect current code against target contracts | Enabling: avoid re-estimating completed implementation | 2 | 3 | 4 | 3.00 | 2.49 | 3.00 | 2.49 | Each contract is marked evidenced or a named gap with task ID | T-1.1 |
| T-1.3 | WP-1: approve estimates, capacity, scope and design | Enabling: Week 8 review | 2 | 3 | 4 | 3.00 | 2.49 | 3.00 | 2.49 | Liam Pheng's inputs complete; review decision and baseline commit recorded | T-1.2 |
| T-2.1 | WP-2 Data: verify migration and indexes | NFR-PRIV-01, NFR-REL-02 | 2-3 | 4 | 5-6 | 3.83–4.17 | 3.19–3.46 | 4.17 | 3.46 | Disposable real database has specified validators/indexes and migration ledger | T-1.3 |
| T-2.2 | WP-2: verify atomic unit/owner creation | FR-UNIT-01, NFR-REL-02 | 3 | 4 | 5 | 4.00 | 3.32 | 4.00 | 3.32 | Injected owner-write failure leaves no orphan unit in real replica set | T-2.1 |
| T-2.3 | WP-2: configure hosted workflow spike | NFR-PORT-01, FR-HEALTH-01 | 3 | 5 | 6-7 | 4.83–5.00 | 4.02–4.15 | 5.00 | 4.15 | SP-02 executed with build/runtime evidence and explicit pass/fail | T-2.1, T-3.2 |
| T-2.4 | WP-2: exercise backup, restore and outage | NFR-REL-02 | 3-4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | 5.00 | 4.15 | SP-03 comparisons saved and separate outage/recovery threshold measured | T-2.1, T-2.2 |
| T-3.1 | WP-3 Identity: verify registration and admin token | FR-AUTH-01, FR-AUTH-03 | 1 | 2 | 2+ | ≥ 1.83 | ≥ 1.52 | 1.83 | 1.52 | Unique normalization, password bounds/hash and setup-token cases pass | T-1.3 |
| T-3.2 | WP-3: verify sessions and logout replay | FR-AUTH-02 | 1 | 2 | 3 | 2.00 | 1.66 | 2.00 | 1.66 | Expired and revoked tokens cannot access protected views | T-3.1 |
| T-3.3 | WP-3: complete CSRF and login throttle cases | NFR-SEC-02, FR-AUTH-02 | 2 | 3 | 4+ | ≥ 3.00 | ≥ 2.49 | 3.00 | 2.49 | Every POST rejects missing/tampered CSRF without mutation; throttle edge cases pass | T-3.2 |
| T-3.4 | WP-3: audit role and cross-unit access | FR-ACCESS-01, NFR-SEC-01 | 2-3 | 4 | 5+ | ≥ 3.83 | ≥ 3.19 | 4.00 | 3.32 | Route-by-role matrix denies all forbidden reads/writes with zero mutations | T-3.3, T-4.2, T-5.3 |
| T-4.1 | WP-4 Membership: verify add-member workflow | FR-UNIT-02 | 1 | 2 | 3 | 2.00 | 1.66 | 2.00 | 1.66 | Registered user gains access; duplicate add cannot downgrade owner | T-2.2, T-3.2 |
| T-4.2 | WP-4: verify roles and rank labels | FR-UNIT-03 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | 2.00 | 1.66 | Only owner can edit non-owner role/rank; owner invariant preserved | T-4.1 |
| T-4.3 | WP-4: verify latest-message list | FR-MSG-01 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | 2.00 | 1.66 | Seeded list returns latest 100 with stable chronological display | T-4.1 |
| T-4.4 | WP-4: verify message input and escaping | FR-MSG-02, NFR-SEC-04 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | 2.00 | 1.66 | Length boundaries and authorization pass; all displayed text fields escape markup | T-4.3 |
| T-5.1 | WP-5 Events: verify creation/time validation | FR-EVT-01 | 2 | 3 | 4 | 3.00 | 2.49 | 3.00 | 2.49 | Role and offset-aware timestamp tests pass without invalid writes | T-4.2 |
| T-5.2 | WP-5: verify attendance upsert | FR-EVT-02 | 2 | 3 | 4 | 3.00 | 2.49 | 3.00 | 2.49 | Repeated/concurrent responses leave one latest record; cross-unit event rejected | T-5.1 |
| T-5.3 | WP-5: verify accountability roster | FR-EVT-03 | 1 | 2 | 3 | 2.00 | 1.66 | 2.00 | 1.66 | Leaders see responses and pending current members, including later additions | T-5.2 |
| T-6.1 | WP-6 Quality: check corrective validation messages | NFR-USE-02 | 1 | 2 | 3+ | ≥ 2.00 | ≥ 1.66 | 2.00 | 1.66 | All eight specified invalid-input cases give corrective information | T-4.4, T-5.3 |
| T-6.2 | WP-6: audit desktop/mobile accessibility | NFR-A11Y-01, NFR-A11Y-02 | 3-4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | 5.00 | 4.15 | Dated axe results meet threshold and all five keyboard workflows pass | T-6.1 |
| T-6.3 | WP-6: measure hosted latency and response size | NFR-PERF-01, NFR-PERF-02 | 1-2 | 3 | 4+ | ≥ 2.83 | ≥ 2.35 | 3.00 | 2.49 | Specified seeded dataset and raw deployed measurements meet thresholds | T-2.3, T-5.3 |
| T-6.4 | WP-6: run representative-user exercise | NFR-USE-01 | 3-4 | 5 | 6 | 4.83–5.00 | 4.02–4.15 | 5.00 | 4.15 | Consent/fictional-data conditions cleared; five anonymized task-result records meet target | T-6.2 |
| T-6.5 | WP-6: repeat clean regression and platform smoke | NFR-REL-01, NFR-MAINT-01, NFR-PORT-01 | 3 | 4 | 5+ | ≥ 4.00 | ≥ 3.32 | 4.00 | 3.32 | Ten clean suite runs plus Windows/Render smoke results saved against stated thresholds | T-3.4, T-6.3 |
| T-7.1 | WP-7 Operations: complete health/failure handling | FR-HEALTH-01, NFR-REL-02 | 1-2 | 3 | 4 | 2.83–3.00 | 2.35–2.49 | 3.00 | 2.49 | Health and request deadline failures return specified responses without secret leakage | T-2.3 |
| T-7.2 | WP-7: scan secrets, hashes and dependencies | NFR-SEC-03 | 2 | 3 | 4 | 3.00 | 2.49 | 3.00 | 2.49 | Tracked-file and user-record checks clean; high/critical dependency findings resolved | T-6.5 |
| T-7.3 | WP-7: validate inventory and deletion procedure | NFR-PRIV-01, NFR-PRIV-02 | 3-4 | 5 | 6+ | ≥ 4.83 | ≥ 4.02 | 5.00 | 4.15 | Document keys match inventory; verified deletion exercise and provider limitations recorded | T-2.4, T-5.3 |
| T-7.4 | WP-7: rehearse isolated local fallback | Enabling: R-01/R-02 response | 1-2 | 3 | 4-5 | 2.83–3.17 | 2.35–2.63 | 3.17 | 2.63 | Synthetic local replica-set workflow and fallback recording reproducible without Atlas | T-2.4, T-5.3 |
| T-8.1-W9 | WP-8: Week 9 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 9 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W10 | WP-8: Week 10 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 10 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W11 | WP-8: Week 11 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 11 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W12 | WP-8: Week 12 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 12 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W13 | WP-8: Week 13 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 13 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W14 | WP-8: Week 14 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 14 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.1-W15 | WP-8: Week 15 progress report | Enabling: required milestone reporting | 1 | 1 | 2 | 1.17 | 0.97 | 1.17 | 0.97 | Week 15 report links completed tasks, actual hours and risk updates | T-1.3 |
| T-8.2 | WP-8: named defects when identified (contingent; not an estimated task) | Enabling: bounded defect closure against retained requirements | Not yet known | Not yet known | Not yet known | Not yet known | Not yet known | Contingent; excluded | Contingent; excluded | Named failed checks rerun successfully; no duplicate implementation charging | T-6.2, T-6.5, T-7.3 |
| T-8.3 | WP-8: reproduce release and demo | NFR-MAINT-01, NFR-MAINT-02 | 3 | 4 | 5 | 4.00 | 3.32 | 4.00 | 3.32 | Clean checkout builds; traceability and acceptance evidence complete; demo rehearsed | T-7.2, T-7.4, T-8.2 |
| T-8.4 | WP-8: retrospective and submission | Enabling: Week 16 final package | 4 | 5 | 6 | 5.00 | 4.15 | 5.00 | 4.15 | Estimate/actual analysis compares signed baseline with history; final artifact and commit link ready | T-8.1-W9, T-8.1-W10, T-8.1-W11, T-8.1-W12, T-8.1-W13, T-8.1-W14, T-8.1-W15, T-8.3 |

T-8.1 is split into seven individually scheduled weekly reports, each with the suggested M = 1 hour. T-8.2 is a contingent defect register, not an invented duration or a zero-hour task. Identify and estimate specific defects when checks fail; use available task slack or an explicitly allocated buffer response and record the change. There are 36 estimated task rows plus the contingent defect placeholder.

### Draft calculation convention and remaining inputs

The supplied O/M/P values and their exact/ranged/lower-bound E results are preserved. To make the schedule and burn-down numerical, the separate **Draft planning E** column uses these explicit calculation conventions:

- Finite ranges use their upper endpoint, such as O = 3 for 2–3 and P = 7 for 6–7.
- A value ending in + uses its stated threshold only, such as P = 6 for 6+. This is a provisional floor scenario, not an estimate of the worst case and not a bound on overruns.
- T-1.1 now uses the supplied O = 1, M = 2 and P = 3, giving E = 2.00 hours and calibrated E = 1.66 hours. No missing-input substitution is needed.
- T-8.2 remains a contingent defect register. Defects receive separate estimates and allocations when identified; they are excluded from this scenario rather than asserted to require zero time.


Calculated from this supplied version: **19 exact E values, 5 finite E ranges and 12 E lower bounds** across 36 planning tasks. All O/M/P fields for those tasks are now populated; T-8.2 remains contingent. Schedule and burn-down use the separate numerical planning scenario and unrounded calculations. A complete bounded expected-effort forecast still needs single-number choices for range/+ inputs.

## Calibration from recorded history

Use the recorded `hours` and `estimate_hours` values, not reconstructed elapsed times. Some start/end intervals differ from the recorded hours; those discrepancies require Liam Pheng's review rather than automatic correction. The October 11 entry has end 00:00 and hours 0.00 and is treated as open, not as a completed zero-hour task.

Calibration uses completed historical work before Week 7 (through 2026-10-04): **35 sessions grouped into six finished tasks** by trimmed task name. Repeated estimates are treated as estimates for the corresponding work sessions and summed within each task. I confirmed on 2026-10-11 that each estimate is separate for its work session; the calibration denominator is therefore supported by that confirmation. The completed deliverables and final notes support grouping the first six task names as finished; the Week 7 planning task remains in progress and is excluded.

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

The `calibration` column contains each eligible historical session's actual/estimate ratio; it is blank for ongoing Week 7 work. Past hours are sunk effort, excluded from remaining task effort and future capacity. The imported history calibrates remaining work; future O/P values come from my own supplied task table, with ranges and open-ended values preserved. Historic 3-hour session estimates were not copied into future task rows.

### Week 7 actual work

Recorded actual hours: **12.50**, comprising October 5 (4.00), October 6 (4.50), and October 8 (4.00). This matches my earlier self-report and replaces that aggregate entry rather than adding to it. 

## Capacity and separate buffer

I have confirmed that **15–16 hours per week during Weeks 8–16 are available exclusively for project work**, after other classes and personal/ROTC commitments. This is net project capacity: **135–144 hours across nine weeks**. Use the lower bound, **15 hours per week / 135 hours total**, as the planning baseline. The additional possible hour each week is optional capacity, not committed task time.

Other-class overhead and personal/ROTC losses are already excluded from this stated availability, so they receive no additional deduction. The table does not claim those commitments consume no time; it avoids subtracting them twice. Project-specific milestone reporting is included in T-8.1 and consumes the planned-task budget.

| Week | My Personal Net availability | Course overhead treatment | Known losses and reason | Project capacity baseline | Minimum buffer | Planned-task budget |
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

**Declared minimum project buffer: 1 hour per week × 9 weeks = 9 hours**, This is **6.67% of the 135-hour baseline project capacity** (9 / 135 × 100). The baseline scheduled-task budget is **135 − 9 = 126 hours**, or **14 hours per week**. If all 16 available hours are realized in every week, capacity is 144 hours and the same minimum buffer leaves 135 task hours; the buffer is then 6.25% of capacity. The baseline relies on 126 task hours rather than this optional upper bound.

The assignment's approximate 87 hours is context; this plan uses my confirmed availability. Historical logged hours are sunk effort and are not deducted from future Weeks 8–16 capacity.

Buffer is separate from calibrated task estimates and reserved for unexpected problems. Record its use during the weekly review, including the triggering issue, hours consumed and remaining reserve; I may have more than the stated minimum by assigning fewer tasks. Risk exposure is a prioritization measure and is not automatically added to task totals. A response is funded only once its linked task has an estimate and fits the weekly task budget, or a documented decision allocates available buffer. Linked mitigation tasks have provisional planning-E allocations in the schedule; additional defects and contingency decisions need separate estimates and allocations. These are draft allocations, not a personally estimated approved baseline.

## Proposed sequencing and weekly gates

Tasks are allocated using the draft planning-E convention above and calibrated once. Tasks in each row run in dependency order; reports close the week's work. The numerical schedule excludes unidentified defects. Reforecast before dependent work proceeds if an acceptance gate fails. This is a working scenario, not evidence that a gate has passed.

| Week | Tasks in dependency order | Draft calibrated planning E (h) | Unassigned task capacity (h) | Gate |
|---|---|---:|---:|---|
| 8 | T-1.1, T-1.2, T-1.3, T-3.1, T-3.2, T-2.1 | 13.29 | 0.71 | Reconciliation and review decision recorded; identity and migration checks pass |
| 9 | T-2.2, T-2.3, T-2.4, T-8.1-W9 | 12.60 | 1.40 | Atomic unit creation, hosted workflow and restore checks pass; blockers have explicit decisions |
| 10 | T-3.3, T-4.1, T-4.2, T-4.3, T-4.4, T-7.1, T-8.1-W10 | 12.60 | 1.40 | Membership, roles, messages, CSRF/throttling and failure handling pass |
| 11 | T-5.1, T-5.2, T-5.3, T-3.4, T-8.1-W11 | 10.94 | 3.06 | Event, attendance, roster and authorization matrix pass |
| 12 | T-6.1, T-6.2, T-6.3, T-7.3, T-8.1-W12 | 13.43 | 0.57 | Accessibility, performance and deletion evidence pass; trial conditions cleared |
| 13 | T-6.4, T-6.5, T-8.1-W13 | 8.45 | 5.55 | Usability and repeated regression/platform checks pass |
| 14 | T-7.2, T-7.4, T-8.1-W14 | 6.09 | 7.91 | Security audit and local fallback pass; triggered defects individually estimated |
| 15 | T-8.3, T-8.1-W15 | 4.29 | 9.71 | Release and demo pass; all named mandatory defects closed |
| 16 | T-8.4 | 4.15 | 9.85 | Retrospective and package complete; Liam Pheng posts commit URL |
| **Total** | **36 planning tasks; contingent defects excluded** | **85.86** | **40.14** | Range/+ inputs still require finite choices before final approval |

## Burn-down baseline

**Draft planning-E scenario:** raw planning effort = **103.33 hours**; calibrated remaining effort R = **85.86 hours**, calculated with k = 85.83 / 103.30. These totals use the explicitly stated range/plus conventions, not a complete set of personal point estimates. Project capacity is 135 hours, the separate buffer is nine hours, and scheduled-task capacity is 126 hours. The draft leaves **40.14 task hours unassigned**, separate from buffer. Unknown defects and the unstated tails of + estimates are not included.

Ideal remaining after n weeks = R × (9 − n) / 9. Projected remaining subtracts the unrounded calibrated planning effort of tasks scheduled to meet their done-whens by each week end. The same task values drive both the schedule and this table. Actual progress is tracked separately after completion evidence exists.

| Point | Ideal remaining (h) | Projected remaining (h) | Future task capacity (h) | Future capacity including buffer (h) | Over task capacity? |
|---|---:|---:|---:|---:|---|
| Start Week 8 | 85.86 | 85.86 | 126 | 135 | No |
| End Week 8 | 76.32 | 72.56 | 112 | 120 | No |
| End Week 9 | 66.78 | 59.96 | 98 | 105 | No |
| End Week 10 | 57.24 | 47.36 | 84 | 90 | No |
| End Week 11 | 47.70 | 36.42 | 70 | 75 | No |
| End Week 12 | 38.16 | 22.99 | 56 | 60 | No |
| End Week 13 | 28.62 | 14.54 | 42 | 45 | No |
| End Week 14 | 19.08 | 8.45 | 28 | 30 | No |
| End Week 15 | 9.54 | 4.15 | 14 | 15 | No |
| End Week 16 | 0.00 | 0.00 | 0 | 0 | No |

**First projected over-budget week: none under this stated draft scenario.** Every weekly allocation is below 14 task hours and projected remaining fits future task capacity. **No unconditional no-deficit claim is made:** range inputs, open-ended + values and unidentified defects prevent a final bounded forecast. Complete the inputs and rerun before approving the baseline.

Future capacity covers weeks after each row and assumes future buffer is unspent. At weekly gates, log actual time and completed task IDs, remaining reserve, named defects and approved scope/estimate changes. Preserve this version for comparison. Spending time without meeting a done-when does not burn down the task's estimated effort.

## Scope decision and Week 8 change control

I explicitly chose to retain all current requirements on 2026-10-11. Requirements priorities remain unchanged; no Won't changes are appropriate.

| Decision | Requirements affected | Hours recovered | MoSCoW before to after | Reason |
|---|---|---|---|---|
| Retain all current requirements | All version 0.4 FR/NFR IDs | 0 (no scope removed) | Unchanged for every requirement | The stated draft fits capacity, so I retained the current scope; reassess after finite personal estimates and risk responses are finalized. |
