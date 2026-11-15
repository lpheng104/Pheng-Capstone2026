# Changelog

| Date | Request | Disposition | Destination |
|---|---|---|---|
| 2026-11-15 | [CR-001: native mobile](docs/change-requests/CR-001-native-mobile.md) | REJECT — Liam Pheng | Existing native mobile exclusions |
| 2026-11-15 | [CR-002: event tracker](docs/change-requests/CR-002-event-accountability.md) | DEFER — Liam Pheng | [B-12-01](docs/backlog.md#b-12-01--dedicated-event-accountability-tracker) |

Notable changes follow the Keep a Changelog structure.

## [Unreleased]

## [0.9.0-rc.1] — 2026-11-15

### Added
- Clean-checkout integration gates and outage/recovery checks (NFR-REL-02, NFR-MAINT-01).
- Reproducible full-volume loopback performance measurements (NFR-PERF-01, NFR-PERF-02).

### Fixed
- Batch roster/user and attendance reads without changing unit authorization or rendered data (DEF-M12-01, NFR-PERF-01).
- Add a retry hint to the existing sanitized HTTP 503 response when MongoDB is unavailable (DEF-M12-02, NFR-REL-02).

### Security
- Update dnspython, PyMongo and Werkzeug pins for the advisories documented in the security review (DEF-M12-03, NFR-SEC-03).

### Known issues
- DEF-M11-05 (S2): no unit member removal workflow. Do not onboard real members or use sensitive units; there is no supported in-app revocation workaround.
- DEF-M11-06 (S2): no isolated subgroup chat. Use fictional data only in the unit-wide demo channel.
- DEF-M11-07 (S3): no separate calendar creation. Use the existing unit events area.
- DEF-M11-09 (S3): rank input is free text. Use a consistent fictional rank convention; it is not a validated rank catalog.
- DEF-I1-01 / #49: interrupted event cleanup may leave orphan responses. Avoid relying on event deletion as transactionally complete.
