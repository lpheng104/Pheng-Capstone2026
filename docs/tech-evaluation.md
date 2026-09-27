# Accountabilibuddy — Week 5 technology evaluation

Date: 2026-09-27. Author of record: repository owner `Liam Pheng`. Status: proposed architecture review for student confirmation. The student reports prior Flask and MongoDB use and 14 hours of Week 5 work. Personal deployment experience has not been established.

## 1. Architectural drivers

| Driver | Requirement / constraint | Architectural consequence |
|---|---|---|
| Logout must revoke access | FR-AUTH-02 | A captured cookie must fail after logout. |
| Unit data stays within membership boundaries | FR-ACCESS-01, NFR-SEC-01 | Check current membership for each protected operation. |
| Small unit page remains responsive | NFR-PERF-01, ASM-04 | Measure warm p95 at 50 members, 100 messages, 25 events; target 1.5 s. |
| Acknowledged writes survive an interruption | NFR-REL-02 | Database persistence and restore need real-service evidence. |
| Reviewer can reproduce and access the app | CON-01, NFR-PORT-01 | Maintain documented local commands and verify hosted startup. |
| Student spending stays bounded | CON-02 | Target zero added subscriptions; maximum $10/month without further approval. |
| Existing stack limits rewrite scope | CON-05 | Retain Python/Flask/MongoDB; evaluate operational seams rather than invent a prior language comparison. |
| Synthetic data only | CON-04, NFR-PRIV-01 | Use fictional accounts and units in spikes and demonstrations. |

## 2. Weighted evaluation

The [CSV](tech-evaluation.csv) contains 24 evidenced rows: three decisions, two options each, four criteria per decision. Distinct criterion weights total 1.00 for each decision. [Method](weights-method.md) and blank scores were committed as `e0b0eac` before scores were entered. This establishes ordering for this review only; the application and original stack predate it. No history has been backdated.

Scores use the 0–5 anchors in the method. They are evidence-informed judgments, not vendor ratings or performance measurements. References V1–V5 resolve in section 7. Source inspection, design estimates, and executed results are labeled separately. Security requirements are gates, not tradeable points. The student must confirm that the alternatives reflect options they genuinely considered; assistant comparison is not evidence of that personal judgment.

| Decision | Option | Weighted score | Recommendation and cost |
|---|---|---:|---|
| Session storage | Database token | 4.55 | Keep; SP-01 rejects captured cookies, but each authenticated request depends on the database. |
| Session storage | Signed cookie only | 2.25 | Reject as specified: replay violates FR-AUTH-02. Adding revocation state changes this option. |
| Database operation | Atlas Free | 3.60 | Proposed primary; hosted connectivity and manual restore remain unproven. |
| Database operation | Local MongoDB | 3.20 | Genuine local-demo fallback; student operates backups and availability. |
| Hosting | Render Free | 4.15 | Proposed primary; idle startup and account quotas constrain demonstrations. |
| Hosting | Local Linux demonstration | 3.25 | Supervised fallback; using it as primary requires revising NFR-PORT-01. |

None of the leading options is within 0.25 of the runner-up. Sensitivity matters most for the database: moving 0.10 weight from remote fit to recovery yields a 3.40/3.40 tie. Thus Atlas is preferred for reviewer reachability, not because it has proven recovery. A local database is reachable through a local app; exposing a laptop database directly to Render is not the fallback design.

The four records are [session storage](adr/0001-session-revocation.md), [database operation](adr/0002-database-operation.md), [hosting](adr/0003-hosting.md), and [project licensing](adr/0004-project-license.md). The license comparison is qualitative; numeric scoring of legal obligations would imply false precision.

## 3. Seam inventory and risk register

High means an unverified seam can defeat a Must requirement or prevent the hosted demo; Medium means a bounded fallback exists; Low means locally supported with a limited remaining question. This table also serves as the Week 5 risk register.

| ID | Seam | Requirement | Risk | Evidence / spike / next action |
|---|---|---|---|---|
| S1 | Browser cookie → session collection → logout | FR-AUTH-02 | Low locally | SP-01 passed 10/10 replay denials; hosted behavior remains S2. |
| S2 | Render TLS/browser → session cookie | FR-AUTH-02, NFR-PORT-01 | High | SP-02: verify cookie flags and hosted logout replay. |
| S3 | Render outbound network → Atlas access rules | FR-HEALTH-01 | High | SP-02: health, credentials, and network path. |
| S4 | Repository subdirectory → build/start command | CON-01, NFR-PORT-01 | High | SP-02: service root must be implementation; nested Blueprint discovery unverified. |
| S5 | Unit membership → role-gated routes | FR-ACCESS-01 | Medium | Existing permission tests; full route/role matrix still needed. |
| S6 | PyMongo behavior → mongomock tests | NFR-REL-02 | High | SP-02 and SP-03 add real-service evidence; mocks do not prove recovery or index behavior. |
| S7 | Database → export → separate restore | NFR-REL-02 | High | SP-03 remains pending; no managed Atlas Free backup. |
| S8 | Free host sleep → reviewer page load | NFR-PERF-01 | Medium | Warm up before timing; keep a local demo and recording fallback. |

SP-01 was executed; [SP-02](spikes/SP-02-hosted-path.md) and [SP-03](spikes/SP-03-restore.md) are written plans. Do not report pending experiments as completed.

## 4. Novelty load

Confirmed familiar: Flask and MongoDB, per student response on 2026-09-27. Familiarity does not establish deployment or security competence. Three learning areas remain unconfirmed: (1) Render/Gunicorn deployment, (2) Atlas networking and recovery, (3) session-security verification. Conservatively count these as three new areas until the student corrects the record.

The proposed single innovation budget goes to reliable hosted deployment. Database recovery and session verification are mandatory supporting work, not optional innovations, and remain real learning costs. Defer a new frontend framework, hosted identity provider, live chat, and AI features. Chat refresh and existing server-rendered forms stay in scope. Budget the next work as 2 h SP-02, 1.5 h SP-03, 1 h security review, and 0.5 h runbook review. These are forward estimates, not additional actual hours. If both operational areas cannot be resolved within those 5 h, use the local demonstration and explicitly revise the hosting acceptance plan with the instructor.

## 5. Cost sheet and free-tier watch list

Planning basis: one app, one synthetic unit with the ASM-04 dataset, one free database, no purchased domain, no external AI API. The expected incremental subscription total is $0/month only while free eligibility and quotas hold. Existing hardware, internet, electricity, tax, and personal labor are excluded; no account invoice has been inspected. CON-02 caps spending at $10/month. Paid upgrade prices are not asserted because the retrieved pricing page did not expose a reliable numeric quote.

| Item | Planned incremental monthly cost | Watch / trigger | Fallback |
|---|---:|---|---|
| Render Free web service | $0 conditional [V1] | Sleeps after 15 idle minutes; 750 free instance hours/workspace/month; inspect dashboard weekly and before demos; investigate at 80% quota | Warm up for demo; local supervised app/recording if suspended. |
| Atlas Free database | $0 conditional [V2] | No managed backup; check dashboard storage/traffic weekly; investigate at 80% displayed quota | Verified manual export/restore; local MongoDB if service unavailable. |
| Existing laptop and local Linux environment | $0 added subscription, assumption | Confirm Linux setup before relying on it; check 24 h before demo | Windows development-server demo for a supervised session; Linux portability remains pending. |
| Domain and external APIs | $0 by scope | No custom domain or API dependency budgeted | Use host-provided URL and existing features. |
| Recovery work | 1.5 h planned, not cash | SP-03 failure or restore longer than 15 minutes | Revisit ADR 0002; do not promise recovered user data from a seed. |

Review free-tier eligibility each week through Week 16 and before Week 14 handoff. If projected total exceeds $10/month, stop selecting paid resources and use the local fallback. No service purchase or deployment was performed in this review. Vendor deprecation or a required runtime change triggers a regression run and a new ADR when it changes the architecture. Data handling stays synthetic; provider retention and account deletion settings remain unverified. No AI provider is part of the application, so there are no token charges or AI failure modes to evaluate.

## 6. License inventory

The existing root [LICENSE](../LICENSE) remains MIT. This is a source-only project release decision, not permission to relabel dependency code. Upstream license texts were inspected on 2026-09-27. Exact installed distribution notices must be retained when bundling; moving upstream branches are not immutable release evidence.

| Component | SPDX / terms | Source | Ship call and required action |
|---|---|---|---|
| Accountabilibuddy | MIT | Root LICENSE; V12 | Ship own source with license; confirm ownership before external contributions. |
| Flask | BSD-3-Clause | V6 | Conditional ship: preserve copyright, conditions, disclaimer, non-endorsement. |
| PyMongo | Apache-2.0 | V7 | Conditional ship: retain license and applicable notices. |
| python-dotenv | BSD-3-Clause | V8 | Conditional ship: retain notices. |
| Gunicorn | MIT | V9 | Conditional ship: retain permission/copyright notice. |
| pytest (development) | MIT | V10 | Conditional ship if included: retain notice. |
| mongomock (development) | ISC | V11 | Conditional ship if included: retain notice. |
| MongoDB server fallback | SSPL-1.0 | V13 | Do not bundle server in the project release; separately review server distribution/service obligations. |
| Render / Atlas services | N/A — service terms, not SPDX software licenses | Requirements §13; account review pending | Synthetic prototype only; do not claim account/data-retention approval. |
| Transitive Python packages | SPDX expressions in [installed inventory](dependency-licenses.md) | Publisher-provided distribution metadata and captured license texts, 2026-09-27 | Conditional ship with captured notices; re-inventory the final Linux environment before bundling. |

Installed transitive packages observed: blinker, click, colorama, dnspython, iniconfig, itsdangerous, Jinja2, MarkupSafe, packaging, pluggy, Pygments, pytz, sentinels, Werkzeug. Their publisher-provided notices and the direct-package notices are captured in [dependency-licenses.md](dependency-licenses.md), including Werkzeug's separate icon notice. pip is environment tooling. The source repository contains requirements files rather than redistributed wheels or a virtual environment. A Linux container's OS, runtime, and installed dependency set still require their own final inventory.

## 7. Verification log

All successful source checks below were performed by the assistant on 2026-09-27. The student must read the retained claims at their sources before submitting under the assignment's AI policy. Local installed versions are observations, not proof of upstream availability or supported compatibility.

| ID | Claim checked | Primary source | Checked on / outcome |
|---|---|---|---|
| V1 | Render Free idle sleep, ephemeral files, 750 monthly instance hours | https://render.com/docs/free | 2026-09-27; confirmed published limits, account quota not inspected |
| V2 | Atlas Free exists and lacks managed backups | https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/ | 2026-09-27; confirmed; manual recovery pending |
| V3 | Flask default session uses signed cookies | https://flask.palletsprojects.com/en/stable/api/#sessions | 2026-09-27; confirmed; replay implication tested in SP-01 |
| V4 | PyMongo connection uses MongoClient | https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/mongoclient/ | 2026-09-27; documentation confirmed, hosted path pending |
| V5 | Render documents Flask/Gunicorn and branch-triggered deployment | https://render.com/docs/deploy-flask | 2026-09-27; confirmed, this app not deployed |
| V6 | Flask BSD-3-Clause text | https://github.com/pallets/flask/blob/main/LICENSE.txt | 2026-09-27; upstream text checked |
| V7 | PyMongo Apache-2.0 text | https://github.com/mongodb/mongo-python-driver/blob/main/LICENSE | 2026-09-27; upstream text checked |
| V8 | python-dotenv BSD-3-Clause text | https://github.com/theskumar/python-dotenv/blob/main/LICENSE | 2026-09-27; upstream text checked |
| V9 | Gunicorn MIT text | https://github.com/benoitc/gunicorn/blob/master/LICENSE | 2026-09-27; upstream text checked |
| V10 | pytest MIT text | https://github.com/pytest-dev/pytest/blob/main/LICENSE | 2026-09-27; upstream text checked |
| V11 | mongomock ISC text | https://github.com/mongomock/mongomock/blob/develop/LICENSE | 2026-09-27; upstream text checked |
| V12 | MIT notice requirement; Apache alternative patent/notice terms | https://opensource.org/license/mit ; https://www.apache.org/licenses/LICENSE-2.0 | 2026-09-27; texts checked |
| V13 | MongoDB server license differs from driver license | https://www.mongodb.com/legal/licensing/server-side-public-license | 2026-09-27; SSPL text checked |
| V14 | Paid Render numeric quote | https://render.com/pricing | 2026-09-27; not verified from retrieved page; no price asserted |
| V15 | Gunicorn installation/platform documentation | https://docs.gunicorn.org/en/stable/install.html | 2026-09-27; retrieval failed; no verified native-Windows support claim |

Repository pins were observed in the requirements files and matched the local installed direct packages. They are not newly selected versions in these ADRs. Vendor release-specific validation remains pending before deployment. The existing broad `Python 3.12+` support assertion is not established by testing one local interpreter.

## Submission readiness

Matrix validation, the local session spike, and the installed Python dependency notice inventory are complete. Student reports 14 actual hours. Pending: student review of facts and alternatives, preferred attribution, personal Rep 12 verification, hosted/restore spikes, final Linux release inventory if bundling, and a configured Git remote for push. No remote was configured when inspected. Do not claim a pushed submission or full hosted acceptance from these documents.

