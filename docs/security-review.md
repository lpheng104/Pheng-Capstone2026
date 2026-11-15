# Milestone 12 security review — evidence for owner review

Owner: Liam Pheng. Evidence collected 2026-11-15 Central. Advisory IDs below link directly to GitHub Advisory Database records. Reachability notes are draft source/configuration inferences for Liam Pheng to verify; no personal finding or risk acceptance is attributed to Liam Pheng.

| Area | Evidence | Finding and disposition |
|---|---|---|
| Secrets | `script/audit.py` scans Git history and tracked/unignored source; `.env.example` contains placeholders. Hosted secrets provided via Render environment. | No rotation claimed. Scanner outcome is recorded in candidate CI; it does not establish that credentials were never exposed elsewhere. |
| Input validation | `tests/acceptance/test_m11_criteria.py` exercises malformed dates, message lengths and escaped hostile markup; MongoDB validator rejects incomplete documents. | These checks cover tested fields, not every field/view. Full NFR-SEC-04 browser coverage remains open. |
| Authentication | `tests/test_iteration1.py` and live `script/iteration1_http.py` check password replacement, session revocation and invalid login; `src/identity` checks expiry. | No complete abuse-resistance claim. Login rate limiting per username can temporarily lock the targeted account; owner review pending. |
| Authorization | Outsider and standard-member deny cases, including direct requests and foreign event IDs, are recorded in Milestone 11 tests and live smoke. | DEF-M11-05 and DEF-M11-06 remain open. No real users or sensitive unit content approved. Full role/route grid pending. |
| Transport | `render.yaml` enables secure cookies; earlier hosted checks observed HTTPS and secure cookie attributes. Local CI uses isolated HTTP. | Candidate has no live Render TLS assessment. Preserve certificate verification and scoped Atlas access. |
| Dependencies | `pip-audit --no-deps --disable-pip -r requirements.lock` against exact pins. Seven baseline findings identified; see advisory table. | Candidate updates dnspython, PyMongo and Werkzeug; clean setup required; rescan found 0 known advisories in 21 pinned packages (baseline: 7 in 21). See [scan summary](evidence/m12-dependency-audit.json). |
| Logging | `src/app.py::database_error` logs exception class; `script/rc_health.py down` asserts sanitized 503, retry hint and no traceback or database URI in response. | Startup errors from Gunicorn are a separate path; output review is still required. Never enable Flask debug on public hosting. |

## Baseline advisory findings and candidate remediation

| Advisory | Baseline and patch | Reachability in this project (draft judgment) |
|---|---|---|
| [GHSA-45c3-73f7-pv4m](https://github.com/advisories/GHSA-45c3-73f7-pv4m) | dnspython 2.8.0 → 2.9.2 | The Atlas SRV URI invokes DNS parsing, so untrusted DNS replies are relevant. An HTTP field does not determine the SRV hostname. Upgrade. |
| [GHSA-vvf4-9x63-8xvv](https://github.com/advisories/GHSA-vvf4-9x63-8xvv) | dnspython 2.8.0 → 2.9.2 | No application path parses attacker-provided zone files; this is distinct from ordinary SRV lookups. Upgrade with the same dependency. |
| [GHSA-qx36-8mw2-4r3x](https://github.com/advisories/GHSA-qx36-8mw2-4r3x) | PyMongo 4.18.1 → 4.18.3 | No client-side field-level encryption, Queryable Encryption or KMS key-vault path configured. Upgrade. |
| [GHSA-vp6j-j7w5-5xjj](https://github.com/advisories/GHSA-vp6j-j7w5-5xjj) | PyMongo 4.18.1 → 4.18.3 | Atlas URI supplied by environment, not derived from request input; hostile URI host interpolation not observed. Upgrade. |
| [GHSA-v4x9-3549-crwv](https://github.com/advisories/GHSA-v4x9-3549-crwv) | PyMongo 4.18.1 → 4.18.3 | BSON encoding is used, but request bodies and stored fields are limited far below the unusually large single-document condition. Upgrade. |
| [GHSA-98qm-wvgf-w4cf](https://github.com/advisories/GHSA-98qm-wvgf-w4cf) | PyMongo 4.18.1 → 4.18.3 | App does not decode raw BSON uploads or mmap/array BSON buffers. Upgrade. |
| [GHSA-g6x2-hccm-hh4m](https://github.com/advisories/GHSA-g6x2-hccm-hh4m) | Werkzeug 3.1.8 → 3.1.9 | Windows/NTFS file-serving concern; Render is Linux, but the project also runs locally on Windows. No malicious static request was attempted. Upgrade. |

These are findings against the exact baseline pins. The scan is not coverage of MongoDB server, OS, the Render platform, or every project risk. Review the primary links and disposition each remaining risk before signing.
