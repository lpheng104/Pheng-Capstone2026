# ADR 0005 — Global admin bootstrap and unit roles are separate

- Recorded: 2026-11-22, retrospectively.
- Status: implemented behavior; documentation draft awaiting Liam Pheng review.
- Owner/reviewer: Liam Pheng. The assistant records observable code, not a new decision in the owner's name.
- Evidence: src/app.py registration, is_admin context, create_unit route and membership helper.

## Context

Users repeatedly confused the administrator setup token with a login password. The existing code reserves the ADMIN_USERNAME environment value for one global admin and checks ADMIN_SETUP_TOKEN during that username's registration. It does not maintain a global-admin role list in MongoDB.

## Implemented decision

Global administrator identity is configured separately from unit owner/leader memberships. Registration still requires a user-chosen password, stored only as a hash. The setup token authorizes registration; it is not an account recovery mechanism. Local and Render token values are independently configured.

## Consequences

A successor cannot create multiple global administrators by handing out the same setup token. Changing ADMIN_USERNAME can change which existing username passes global-admin checks; review the security effect first. Resetting a setup token does not change the account password. Unit leaders do not gain global unit-creation permission automatically. Do not reconfigure these settings as a troubleshooting shortcut.

## Alternatives and owner confirmation

A database-backed global role list and an account recovery workflow would be changes, not documentation fixes. No historical comparison or approval is invented here. Liam Pheng should confirm this recorded behavior and decide separately whether it should change; preserve the reason and date of any reversal.
