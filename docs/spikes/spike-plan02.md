# Spike SP-02 — Does the hosted application complete one protected workflow?

- **Unknown:** Can Render start this repository and access Atlas with valid protected sessions?
- **Feeds:** ADR 0001, ADR 0002, ADR 0003
- **Requirements at risk:** FR-AUTH-02, FR-EVT-02, FR-HEALTH-01, NFR-PORT-01
- **Time box:** 2 hours
- **Run on:** Pending; needs configured Render and Atlas accounts

## The question

Can a clean Render deployment return `/health` 200 and complete registration, login, unit creation, event creation, attendance response, and logout replay rejection within 120 minutes?

## The smallest thing that answers it

- Use only synthetic records and a disposable Atlas database. Select Free plans explicitly and review the current quota settings.
- Configure the service root as `implementation`, using the existing requirements and start command; verify which path Render uses to locate the nested Blueprint.
- Set secrets in service settings and permit only the necessary Render outbound addresses in Atlas. Do not publish credentials in results.
- Deploy, save the build identifier and runtime version, query health, and execute the six named actions. Capture status codes and record persistence after one application restart.
- Replay a pre-logout cookie and require denial. Record Secure/HttpOnly/SameSite settings from the browser.

## Success criterion

Health returns 200; all six actions succeed; replay is denied; one acknowledged attendance response survives the restart; total time is at most 120 minutes.

## Failure criterion

Any action fails, acknowledged data disappears, replay succeeds, a paid plan is required above CON-02, or the time box expires.

## Plan B if it fails

Use a supervised local demonstration and keep NFR-PORT-01 pending. Allocate a narrower 90-minute follow-up to the first failed seam. Do not call local success hosted acceptance.

## Result

Not run. No account-level connectivity, deployment, or persistence result has been established.

## Decision

Keep hosting/database ADRs Proposed until this experiment passes. Preserve this failed-or-pending path in the Week 6 plan.
