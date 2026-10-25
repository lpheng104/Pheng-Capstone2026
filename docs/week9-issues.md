# Week 9 requirement-linked issues

Owner: Liam Pheng. Instructor: Dr. Litman. Requirement IDs below are from the existing remote specification and traceability matrix, not the independent local baseline. Links are recorded after GitHub creation.

## FR-ACCT-04 — Verify real HTTP sign-in for the walking skeleton

- [ ] A seeded fictional member signs in through real HTTP and reaches its unit page.
- [ ] The identity service reads the live database session and user.
- [ ] Wrong credentials do not grant protected-page access.

## FR-ACCT-05 — Prove server-side logout revocation

- [ ] A captured pre-logout cookie cannot read protected content after logout.
- [ ] An expired session is rejected independently of TTL cleanup.
- [ ] The automated account/session regressions pass.

## FR-CHAT-05 — Render persisted history through real component services

- [ ] Setup creates at least one synthetic persisted message.
- [ ] The protected HTML page displays that message through messaging and persistence services.
- [ ] A direct MongoDB row change appears in the next HTTP response and is restored afterward.
- [ ] A 101-message equal-timestamp test returns a stable latest-100 window.

## FR-CLNDR-02 — Exercise event storage in the skeleton workflow

- [ ] Setup creates a synthetic event in real MongoDB.
- [ ] The route calls scheduling and unit-access services and renders the event in HTML.
- [ ] Existing event permission/time-validation regression passes; this thin slice does not claim a complete calendar UI.

## NFR-SEC-01 — Enforce unit membership on the skeleton read path

- [ ] An anonymous request redirects to login.
- [ ] An authenticated outsider receives 403 for another unit.
- [ ] Membership is checked before message/event data is returned.

## NFR-MAINT-01 — Automate install lint test build and live smoke

- [ ] CI runs on every push and every pull request into main.
- [ ] Install, lint, test, build and real-MongoDB smoke each propagate nonzero failure.
- [ ] A deliberate red run, exact failure line and fix commit are recorded.
- [ ] A green run on main is linked from the skeleton trace.

## NFR-PORT-01 — Bootstrap the skeleton from a clean checkout

- [ ] Python version and all transitive package versions/hashes are committed.
- [ ] One setup command installs the hash lock, applies migration 0001 and seeds synthetic records.
- [ ] Windows commands and Linux CI commands are documented exactly.
- [ ] Local/Linux evidence is distinguished from unverified Render deployment.

## NFR-SEC-03 — Audit credentials and keep configuration outside source

- [ ] All application and fixture environment variables are listed in .env.example.
- [ ] History and tracked/unignored-source Gitleaks scans report no findings.
- [ ] The release build excludes .env, downloaded dependencies and database binaries.
- [ ] A four-line credential rotation procedure is documented.

## Verified publication

All eight issues are on [2026CapstoneProjectBoard](https://github.com/users/lpheng104/projects/1), status This Week.

| Requirement | Issue |
|---|---|
| FR-ACCT-04 | [#37](https://github.com/lpheng104/Pheng-Capstone2026/issues/37) |
| FR-ACCT-05 | [#38](https://github.com/lpheng104/Pheng-Capstone2026/issues/38) |
| FR-CHAT-05 | [#39](https://github.com/lpheng104/Pheng-Capstone2026/issues/39) |
| FR-CLNDR-02 | [#40](https://github.com/lpheng104/Pheng-Capstone2026/issues/40) |
| NFR-SEC-01 | [#41](https://github.com/lpheng104/Pheng-Capstone2026/issues/41) |
| NFR-MAINT-01 | [#42](https://github.com/lpheng104/Pheng-Capstone2026/issues/42) |
| NFR-PORT-01 | [#43](https://github.com/lpheng104/Pheng-Capstone2026/issues/43) |
| NFR-SEC-03 | [#44](https://github.com/lpheng104/Pheng-Capstone2026/issues/44) |
