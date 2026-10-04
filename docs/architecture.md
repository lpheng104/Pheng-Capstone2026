# Technical Specification — Accountabilibuddy

Version: v0.1 · Date: 2026-10-04 · Author: lpheng104 (repository owner) · Status: Draft for owner review

Requirements baseline this design satisfies: [requirements.md](requirements.md), version 0.4. This is the target design for the remaining implementation work, not a declaration that the current prototype meets every contract. The owner must read and approve it before changing its status to Baselined. The existing Flask/MongoDB constraint is retained; decisions refine [ADRs 0001–0004](adr/0001-session-revocation.md).

## 1. Purpose and Scope

Accountabilibuddy provides fictional military-style units with authenticated group communication, event scheduling, attendance intentions, and a leader roster. The system distinguishes identity, unit membership, and permission roles. Rank is a display label and never grants authority. Server-rendered forms are the only application client. The design serves a course prototype with one small unit as the performance baseline.

In scope:

- Registration, login, logout, administrator bootstrap: FR-AUTH-01, FR-AUTH-02, FR-AUTH-03.
- Unit creation, adding registered members, owner-controlled roles/ranks: FR-UNIT-01, FR-UNIT-02, FR-UNIT-03.
- Latest messages and posting: FR-MSG-01, FR-MSG-02.
- Events, attendance intentions and leader rosters: FR-EVT-01, FR-EVT-02, FR-EVT-03.
- Cross-unit isolation and health: FR-ACCESS-01, FR-HEALTH-01.
- All NFRs in baseline 0.4, with verification responsibilities in §10; constrained administrative deletion supports NFR-PRIV-02.

Out of scope:

- Official readiness, verified physical presence, emergency notification, or sensitive real-world personnel information: the course prototype has no authority or delivery guarantee.
- Direct messages, uploads, live push chat, external calendars and parent/child unit permissions: not required by baseline 0.4.
- Password reset, MFA, federation, self-service account deletion and event edit/delete UI: deferred; administrative deletion remains an operator procedure.
- AI inference, a separate frontend framework, custom domain and payments: no baseline requirement justifies these dependencies.

### Baseline reconciliation and implementation delta

The older `docs/traceability.csv` contains FR-ACCT identifiers and a different meaning for FR-UNIT-03 (member removal). It is not the baseline for this specification. Do not silently equate those identifiers. Q1 in §11 assigns reconciliation to the owner; this specification's §10 maps the actual 0.4 requirements. The older checker only validates CSV structure, so its previous success did not establish cross-file agreement.

Target work beyond the prototype: extract components; unified errors and strict form parsing; bounded database deadlines; request-level query batching; durable migration ledger/validators; atomic unit creation with owner membership; deterministic message ordering; explicit duplicate-submit behavior; administrative deletion tooling and deployment/recovery measurements. The prototype currently mixes flashed 200 responses with default HTML errors, creates indexes in the app factory, and reads members/events in loops. These are implementation tasks, not unresolved design choices.

Correction to Week 5 evidence: `create_app()` already creates both the sessions token unique index and sessions expiration TTL index near its return. The earlier claim that the TTL index was missing was wrong. TTL cleanup is asynchronous; authorization must still check expiration. No actual TTL timing measurement has been performed [V2].

## 2. System Context (Level 1)

Source: [context.json](diagrams/context.json). Render: [context.png](diagrams/context.png).

![System context](diagrams/context.png)

| External actor / system | What it does with us | Protocol | If it is unavailable |
|---|---|---|---|
| Member | Register, read/post messages, set attendance | HTTPS HTML/forms/cookie | Tasks wait; there is no offline write queue. |
| Owner/leader/administrator | Perform authorized unit operations and read roster | HTTPS HTML/forms/cookie | Members retain their existing permissions; no automatic privilege transfer. |
| Operator/reviewer | Deploy, inspect health, run verification and migration | HTTPS health; local CLI; MongoDB TLS | Leave last successful deployment in place; postpone changes. |
| MongoDB Atlas | Store application records and server sessions | PyMongo MongoDB wire protocol over TLS | Return bounded 503; do not authenticate from the cookie alone. |

## 3. Containers (Level 2)

Source: [containers.json](diagrams/containers.json). Render: [containers.png](diagrams/containers.png).

![Containers and trust boundaries](diagrams/containers.png)

| Container | Responsibility (one sentence) | Technology | Runs where | Holds secrets? |
|---|---|---|---|---|
| Browser | Display HTML and submit forms. | HTML/CSS browser | User device | Signed session cookie/CSRF token; never database credentials. |
| Web application | Authorize and execute unit workflows. | Python, Flask, Jinja, Gunicorn | Render Linux; local Flask server for development | SECRET_KEY, MONGODB_URI, ADMIN_SETUP_TOKEN from environment. |
| Data store | Persist typed application records. | MongoDB | Atlas; local MongoDB for isolated demo | Password hashes, session tokens, database credentials managed by operator. |
| Maintenance CLI | Apply migrations and perform controlled maintenance. | Python/PyMongo | Operator workstation, one process at a time | Separate database credentials in environment; never command arguments/logs. |

Trust boundary: browser input is untrusted; Render terminates HTTPS before the application; MongoDB credentials cross only the server/provider boundary using TLS. No browser may connect directly to MongoDB. Production cookies are Secure, HttpOnly, SameSite=Lax; local HTTP uses Secure=false only in the isolated development profile [V3]. Set COOKIE_SECURE=true and a random SECRET_KEY in hosting settings. Require ADMIN_USERNAME and ADMIN_SETUP_TOKEN at bootstrap; do not print them. Treat proxy headers as untrusted unless the deployed proxy arrangement has been verified. The application does not use client IP for authorization.

Target deployment sets the service root to `implementation`, starts the existing app factory with Gunicorn, and explicitly selects the free compute plan; use `rootDir` when the Blueprint is located above the app [V9]. Run migration separately before web startup, using a migration credential. Web startup verifies migration 0001's checksum and fails readiness if absent/mismatched; it does not modify schema. Connection pools are per worker; start with one worker and measure before increasing it. Credentials and hosting account configuration remain operator inputs, not hard-coded defaults.

## 4. Components (Level 3 — Web application)

Source: [components.json](diagrams/components.json). Render: [components.png](diagrams/components.png).

![Component dependency graph](diagrams/components.png)

| Component | Responsibility (verb first) | Owns (state) | Depends on | Serves (req IDs) |
|---|---|---|---|---|
| C1 Web adapter | Parse requests, enforce CSRF and render accessible responses. | Request-local form/error/view models; no durable business state | C2, C3, C4, C5, C6 | FR-ACCESS-01, NFR-SEC-02, NFR-SEC-04, NFR-A11Y-01, NFR-A11Y-02, NFR-USE-02 |
| C2 Identity | Register identities, verify credentials and revoke sessions. | users, sessions, login_attempts | C6 | FR-AUTH-01, FR-AUTH-02, FR-AUTH-03, NFR-SEC-03 |
| C3 Unit access | Create units and resolve current memberships and permissions. | units, memberships | C6 | FR-UNIT-01, FR-UNIT-02, FR-UNIT-03, FR-ACCESS-01, NFR-SEC-01 |
| C4 Messaging | Store and retrieve unit messages in stable order. | messages | C3, C6 | FR-MSG-01, FR-MSG-02 |
| C5 Scheduling | Create events, upsert intentions and assemble leader rosters. | events, responses | C3, C6 | FR-EVT-01, FR-EVT-02, FR-EVT-03, NFR-PERF-01 |
| C6 Persistence | Execute bounded database operations and enforce schema versions. | schema_migrations; connections (process-local) | None | FR-HEALTH-01, NFR-REL-01, NFR-REL-02, NFR-MAINT-01, NFR-PORT-01 |
| C7 Maintenance | Coordinate verified deletion and recovery while writes are stopped. | No additional stored user data | C2, C3, C4, C5, C6 | NFR-PRIV-01, NFR-PRIV-02, NFR-MAINT-02, CON-01 |

Dependency graph is acyclic: C1/C7 call services; C4/C5 call C3; C2/C3 call C6; C1 also calls C6 for health. C6 never calls a service or web adapter. Identity is resolved before service dispatch and passed as an immutable user ID, not obtained through a callback. Service return values are plain data; only C1 knows Flask request/response objects. Every durable collection has exactly one owner. C6 provides mechanical access but does not own business rules; C7 requests changes through collection owners rather than becoming a second owner. C7 imports the same service modules into the maintenance process: its diagram arrows are code dependencies, not RPC to a running web worker.

## 5. Interface Contracts

These are project-defined contracts, not vendor endpoint claims. Route names retain the prototype's paths. All lengths are Unicode code points after trimming, except passwords: preserve password bytes as submitted, encode UTF-8 for hashing, and never trim them. Normalize usernames by trim then lowercase. Reject duplicate form keys, unknown fields, and non-form POST bodies with 400 invalid_input. Decode UTF-8 strictly. All POSTs require a scalar `csrf` string (1–128 characters) matching the signed browser session. Missing/incorrect CSRF is 400 invalid_csrf before any mutation. Resource IDs are 24 hexadecimal characters; malformed or missing resources are 404. Templates escape all user text. Browser input never chooses a MongoDB operator or collection name.

Common limits: MAX_CONTENT_LENGTH=65,536 bytes; larger payload is 413. POST content type is application/x-www-form-urlencoded, with no file upload. Reads have no mutation except issuance of a CSRF cookie. Protected requests without a valid unexpired database session receive 302 to `/login`; a valid session without the required role receives 403. All dynamic responses use Cache-Control: no-store. All contracts inherit common 400/413/503/500 failures; unsupported methods return 405. No general API is exposed. A JSON Accept header selects only the error rendering, not an alternate successful data API.

Error envelope used system-wide: `{ "error": { "code": "invalid_input", "message": "Enter a title of 1–100 characters.", "fields": {"title": "Required."}, "request_id": "32-lowercase-hex" } }`. `fields` is always an object, empty when no field is implicated; request_id is newly generated per request, not stored with a user. Browser errors render exactly those four values in `error.html` with an alert, field links, and a safe back/reload link. Never echo passwords/tokens, raw exceptions, query bodies or connection strings. JSON errors use application/json; HTML uses text/html; both retain the same HTTP status. The examples below specify status, Location/body, and observable content, not byte-identical HTML formatting.

Status-code policy: 200 successful page/health; 302 same-origin GET redirect after mutation or for missing authentication; 400 validation/CSRF; 403 authorization; 404 missing/malformed resource; 405 method; 409 duplicate username or unique-index conflict; 413 body limit; 429 sign-in throttle; 500 unexpected internal error; 503 database/deadline failure. A timeout on a mutation means outcome unknown, not guaranteed rollback. Give the user a refresh-and-check instruction before resubmission. For HTML failures, preserve non-secret form fields in the view, not server logs. Generic 500 message: “Something went wrong. Contact the operator with this request ID.”

### I1 — GET/POST /register (serves FR-AUTH-01, FR-AUTH-03)

**Purpose:** Create a unique user identity.

**Auth:** Public; configured admin username additionally requires setup_token.

**Request:** GET none. POST username:string required [a-z0-9_]{3,32} after normalization; name:string required 1–80; password:string required 8–128 with at least one ASCII upper, lower and one of !@#$%; setup_token:string optional 1–256, required for admin username; csrf as common policy.

**Success:** GET 200 auth.html with registration fields and CSRF. POST 302 Location: /login with a safe confirmation; e.g. username=member01 creates one user.

**Errors:** 400 invalid_input for field/password rules; 403 invalid_setup_token; 409 username_taken, including races; common failures apply.

**Idempotency:** Repeat normalized username yields 409, never another user.

**Side effects:** Insert users document with password_hash only; no auto-login.

**Limits:** Common 64 KiB cap; no new rate rule beyond platform resources; registration remains synthetic/invite-supervised.

### I2 — GET/POST /login (serves FR-AUTH-02)

**Purpose:** Authenticate credentials and issue a revocable session.

**Auth:** Public, valid CSRF on POST; wrong credentials return identical 403 invalid_credentials.

**Request:** GET none. POST username:string required normalized [a-z0-9_]{3,32}; password:string required 1–128, untrimmed; csrf required.

**Success:** GET 200 auth.html. POST 302 Location: /; Set-Cookie for new session. Example member01 signs in and sees only their units.

**Errors:** 400 field/CSRF; 403 invalid_credentials; 429 login_throttled with Retry-After remaining seconds; common failures.

**Idempotency:** Not idempotent: each successful login revokes the current browser token and creates a new token; other devices remain signed in.

**Side effects:** Update login_attempts; read user hash; replace browser session token; clear successful attempt row.

**Limits:** At most 10 attempts per normalized username in 15 minutes; 11th denied; password hashing budget verified through NFR tests.

### I3 — POST /logout (serves FR-AUTH-02)

**Purpose:** Revoke current session and clear browser authentication.

**Auth:** Authenticated user with CSRF; no valid session redirects to /login without a mutation.

**Request:** csrf only.

**Success:** 302 Location: /login and expired/cleared signed cookie; captured prior auth_token subsequently denied.

**Errors:** 400 invalid_csrf; 503 outcome_unknown if revocation cannot be acknowledged; common failures.

**Idempotency:** Deleting an already deleted token is safe; repeat browser request without auth redirects to login.

**Side effects:** Delete current sessions row, clear signed session only after acknowledgement.

**Limits:** Common cap; one token deletion; no all-devices logout.

### I4 — GET / (serves FR-AUTH-02, FR-ACCESS-01)

**Purpose:** Display the signed-in user's accessible units.

**Auth:** Any authenticated user; otherwise 302 /login.

**Request:** No fields/query parameters.

**Success:** 200 dashboard.html with unit names/links; an empty set shows “No units assigned.” Example member01 sees Alpha only.

**Errors:** Common read errors; unknown query keys 400.

**Idempotency:** Read-only apart from CSRF issuance.

**Side effects:** Read memberships and matching units; no record mutation.

**Limits:** Fetch unit records in one batched query; no arbitrary server-side role based on rank.

### I5 — POST /units (serves FR-UNIT-01)

**Purpose:** Create a unit and its owner membership atomically.

**Auth:** Configured administrator identity only; all other authenticated users 403.

**Request:** name:string required 1–80; echelon:string required 1–30; csrf.

**Success:** 302 Location: /units/{new_id}; e.g. Alpha / Squad yields a unit and its owner membership together.

**Errors:** 400 fields; 403 forbidden; 503 transaction failure or uncertain commit; common errors.

**Idempotency:** Not idempotent; repeat submission intentionally creates a new unit even with the same name. Refresh after ambiguous result before retry.

**Side effects:** C3 transaction inserts units and memberships(role=owner, rank=''); acknowledge after commit.

**Limits:** Common cap; no uniqueness constraint on unit name; no automatic transaction replay.

### I6 — GET /units/{unit_id} (serves FR-MSG-01, FR-EVT-03, FR-ACCESS-01)

**Purpose:** Render authorized unit content and leader accountability.

**Auth:** Current unit member; outsider 403; anonymous 302. Owner/leader sees roster, member sees only own intention.

**Request:** unit_id:ObjectId path; no query fields.

**Success:** 200 unit.html with escaped unit/members, latest 100 messages and events; leader sees one row per current member per event, derived pending if no response.

**Errors:** 404 malformed/missing unit; 403 outsider; common read errors.

**Idempotency:** Read-only.

**Side effects:** Read unit/members/users/messages/events/responses; no caches of permission decisions.

**Limits:** Messages sort created_at descending then _id descending, limit 100, reverse for display. Events sort starts_at then _id ascending. No event pagination in v0.1; scale target 25 events, 50 members. Batch users/responses with $in; avoid one DB call per member/event.

### I7 — POST /units/{unit_id}/members (serves FR-UNIT-02)

**Purpose:** Add an existing registered user to the unit.

**Auth:** Owner or leader of that unit; other member/outsider 403.

**Request:** unit_id path; username:string required normalized 3–32; csrf.

**Success:** 302 Location: /units/{unit_id}; user becomes member with empty rank. Existing membership succeeds unchanged.

**Errors:** 404 unit; 400 unknown_user with “Ask this user to register first.”; 403 forbidden; common errors.

**Idempotency:** Idempotent by unit_id/user_id; preserve any existing owner/leader role and rank.

**Side effects:** Upsert memberships using insert-only role/rank defaults.

**Limits:** Common cap; membership uniqueness enforced; no silent creation of user accounts.

### I8 — POST /units/{unit_id}/members/{user_id} (serves FR-UNIT-03)

**Purpose:** Change a non-owner's role and display rank.

**Auth:** Only the unit owner; target owner is never editable; failures 403.

**Request:** unit_id/user_id:ObjectId paths; role:string required enum member/leader; rank:string optional 0–30 defaults ''; csrf.

**Success:** 302 Location: /units/{unit_id}; e.g. role=leader and rank=SGT updates only the target membership.

**Errors:** 404 missing unit/user membership; 403 actor or protected owner; 400 invalid role/rank; common errors.

**Idempotency:** Setting the same role/rank is a no-op; concurrent requests use last acknowledged update.

**Side effects:** Update one membership with filter excluding role=owner; rank never authorizes access.

**Limits:** Common cap; this interface does not remove membership or transfer ownership.

### I9 — POST /units/{unit_id}/messages (serves FR-MSG-02, FR-ACCESS-01)

**Purpose:** Append a plain-text unit message.

**Auth:** Current member; otherwise common authentication/authorization behavior.

**Request:** unit_id path; body:string required 1–2000; csrf.

**Success:** 302 Location: /units/{unit_id}; example body=Meet at 0600 appears as escaped text with author and UTC time.

**Errors:** 404 unit; 403 outsider; 400 empty/overlong body; common errors.

**Idempotency:** Not idempotent: repeated successful submits produce separate messages. Disable repeated UI submission until response; do not auto-retry.

**Side effects:** Insert message with server-derived author_id, author snapshot, created_at and unit_id.

**Limits:** Common cap; display only latest 100, older records retained until deletion policy; no polling or live delivery guarantee.

### I10 — POST /units/{unit_id}/events (serves FR-EVT-01)

**Purpose:** Schedule an offset-aware unit event.

**Auth:** Owner/leader of unit only.

**Request:** unit_id path; title:string required 1–100; starts_at:string required 1–40 ISO-8601 with explicit UTC offset or Z; location:string required 1–200; uniform:string optional 0–100 default ''; details:string optional 0–2000 default ''; csrf.

**Success:** 302 Location: /units/{unit_id}; 2026-10-05T06:00-05:00 stores 2026-10-05T11:00:00Z.

**Errors:** 400 invalid_time or fields; 403 member/outsider; 404 unit; common errors.

**Idempotency:** Not idempotent: repeat creates separate event; verify after ambiguous timeout before resubmitting.

**Side effects:** Insert events; convert to UTC; created_by from current identity.

**Limits:** Common cap; past times are allowed and clearly displayed; no inferred local timezone.

### I11 — POST /units/{unit_id}/events/{event_id}/respond (serves FR-EVT-02, FR-ACCESS-01)

**Purpose:** Set one current attendance intention.

**Auth:** Current member of URL unit; event must belong to that unit.

**Request:** unit_id/event_id:ObjectId paths; status:string required enum attending/not attending; csrf.

**Success:** 302 Location: /units/{unit_id}; response for this user/event equals submitted status.

**Errors:** 404 event missing/cross-unit; 403 outsider; 400 invalid status; 409 conflicting upsert not resolved by one reread; common errors.

**Idempotency:** Idempotent for identical status; last acknowledged update wins for differing values; pending is never persisted.

**Side effects:** Upsert responses keyed on event_id/user_id; never accept user_id from form.

**Limits:** Common cap; one response per pair; no claim of verified physical presence.

### I12 — GET /health (serves FR-HEALTH-01, NFR-REL-02)

**Purpose:** Expose bounded database readiness without user data.

**Auth:** Public operator probe; bypass cookie authentication resolution.

**Request:** None.

**Success:** 200 application/json exactly {"status":"ok"} after database ping and known schema readiness.

**Errors:** 503 dependency_unavailable or schema_not_ready in common JSON envelope; no database name or exception text.

**Idempotency:** Read-only.

**Side effects:** Database ping; check cached startup schema readiness flag, no schema mutation.

**Limits:** 2-second total DB timeout; no automatic retries.

### I13 — Migration CLI (serves CON-01, NFR-MAINT-01, NFR-REL-01)

**Purpose:** Apply the explicit initial schema in a reproducible step.

**Auth:** Operator with migration database credentials; no web route.

**Request:** python migrations/run.py [--plan|--apply]; URI/database only from environment; manifest path fixed to 0001_initial.json.

**Success:** Exit 0; stdout “PLAN 0001: 8 collections” in offline plan mode, or “APPLIED 0001”/“ALREADY APPLIED 0001” after apply.

**Errors:** Exit 1 generic connection/schema/checksum/non-empty-database failure; exit 2 invalid arguments. CLI errors carry no secrets; common HTTP envelope does not apply to process exit.

**Idempotency:** Same checksum ledger gives ALREADY APPLIED; interrupted empty-schema creation can resume with no ledger.

**Side effects:** Apply validators/indexes then ledger; no user records written.

**Limits:** 60-second DB deadline; single operator process with web writes stopped.

### I14 — Administrative deletion procedure (serves NFR-PRIV-01, NFR-PRIV-02)

**Purpose:** Remove verified subject records through maintenance services.

**Auth:** Operator only, verified request and service stopped; never a public endpoint.

**Request:** Verified user_id:ObjectId; deletion scope user or explicitly approved unit; proof handled outside app; no proof documents stored in database.

**Success:** Completion record: {status: complete, completed_on: UTC-date, remaining_references: 0}; report to requester without subject details in logs.

**Errors:** Owner deletion blocked pending unit-deletion authorization; partial database failure yields incomplete status and preserved procedure position; no false success.

**Idempotency:** Repeat query sequence is safe; only matching records removed.

**Side effects:** Deletes dependent records in §6 order and verifies zero matches; subject-bearing synthetic backups removed within 7 days.

**Limits:** 7-day end-to-end SLA; 15-minute attempt time box; no background automatic destructive job. This contract is to be implemented, not a delivered deletion CLI.

### I15 — Verification CLI and manual test protocol (serves NFR-REL-01, NFR-MAINT-01, NFR-A11Y-01, NFR-A11Y-02, NFR-USE-02)

**Purpose:** Measure repeatability, security, accessibility and usability gates.

**Auth:** Developer/reviewer on synthetic data; no production credentials in test suite.

**Request:** Run pytest from implementation directory with pinned dev dependencies; run spec-check with spec and baseline paths; use required NFR dataset and documented manual browser steps.

**Success:** Exit 0 for automated checks; retain count/runtime; 10/10 sequential pytest runs required for NFR-REL-01; manual results record per-page/task pass/fail.

**Errors:** Nonzero exit or threshold violation means unaccepted requirement; incomplete manual measurement remains pending.

**Idempotency:** Read-only production behavior; isolated fixtures are recreated for each run.

**Side effects:** Creates only temporary synthetic fixtures/reports; no new real-user data.

**Limits:** Regression run <=60 seconds; warm p95 <=1.5 s at defined dataset; 0 serious/critical accessibility findings; 5/5 keyboard tasks. These are targets, not new measured outcomes.

## 6. Data Model

MongoDB BSON documents use `_id` as primary key. All fields below are required and non-null, unless an explicit empty-string rule is given; omit nothing and store no nulls. ObjectId references are application-enforced, not foreign keys. Dates are BSON UTC instants; form offsets convert to UTC before storage. Strings are plain text, never HTML. The schema and database indexes are executable in [migration 0001](../migrations/0001_initial.json); cross-collection invariants are service obligations. No money fields exist. Current counts have not been queried; each “now” value below is a fresh synthetic fixture, not a claim about an account's contents.

### Entity: users (serves FR-AUTH-01)

Purpose: One registered person identity. Owner: C2.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| username | string | Required, non-null; length 3–32; pattern `^[a-z0-9_]{3,32}$`;  |
| name | string | Required, non-null; length 1–80;  |
| password_hash | string | Required, non-null; length 1–512;  |

Invariants: Normalized username unique; no plaintext password; display name is not an authorization key.

Relationships: 1 user to many memberships, messages, sessions and responses.

Volume (fresh fixture now / Week 16 estimate): 0 / 50. These are planning estimates, not quotas.

Lifecycle: Register creates; operator deletion removes dependent records first.

### Entity: units (serves FR-UNIT-01)

Purpose: One independent communication group. Owner: C3.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| name | string | Required, non-null; length 1–80;  |
| echelon | string | Required, non-null; length 1–30;  |
| created_by | objectId | Required, non-null;  |

Invariants: Exactly one owner membership, created in the same transaction as the unit; creator must exist.

Relationships: 1 unit to many memberships, messages and events; created_by references one user.

Volume (fresh fixture now / Week 16 estimate): 0 / 1. These are planning estimates, not quotas.

Lifecycle: Admin creates; approved operator deletion removes dependent records before unit.

### Entity: memberships (serves FR-UNIT-02, FR-UNIT-03)

Purpose: One user's permission and rank within one unit. Owner: C3.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| unit_id | objectId | Required, non-null;  |
| user_id | objectId | Required, non-null;  |
| role | string | Required, non-null; length 1–10; enum owner, leader, member;  |
| rank | string | Required, non-null; length 0–30;  |

Invariants: Pair unit/user unique; at most one owner via partial unique index; service ensures at least one. Empty rank means unspecified, never NULL.

Relationships: Many memberships to one unit and one user.

Volume (fresh fixture now / Week 16 estimate): 0 / 50. These are planning estimates, not quotas.

Lifecycle: Create with unit or add-member; owner cannot be edited through I8; hard-delete during approved user/unit cleanup.

### Entity: messages (serves FR-MSG-01, FR-MSG-02)

Purpose: One submitted unit message. Owner: C4.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| unit_id | objectId | Required, non-null;  |
| author_id | objectId | Required, non-null;  |
| author | string | Required, non-null; length 1–80;  |
| body | string | Required, non-null; length 1–2000;  |
| created_at | date | Required, non-null; UTC instant |

Invariants: Author and unit are authorized at creation; author string is historical display snapshot; same text may appear twice.

Relationships: Many messages to one unit and author user.

Volume (fresh fixture now / Week 16 estimate): 0 / 1000 stored, latest 100 shown. These are planning estimates, not quotas.

Lifecycle: Create on I9; retain for prototype duration; hard-delete on approved author/unit cleanup.

### Entity: events (serves FR-EVT-01)

Purpose: One scheduled unit gathering. Owner: C5.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| unit_id | objectId | Required, non-null;  |
| title | string | Required, non-null; length 1–100;  |
| starts_at | date | Required, non-null; UTC instant |
| location | string | Required, non-null; length 1–200;  |
| uniform | string | Required, non-null; length 0–100;  |
| details | string | Required, non-null; length 0–2000;  |
| created_by | objectId | Required, non-null;  |

Invariants: starts_at is UTC derived from explicit offset; empty uniform/details mean not supplied; created_by exists.

Relationships: Many events to one unit; 1 event to many responses.

Volume (fresh fixture now / Week 16 estimate): 0 / 25. These are planning estimates, not quotas.

Lifecycle: Authorized leader creates; approved unit/event maintenance removes responses before event.

### Entity: responses (serves FR-EVT-02, FR-EVT-03)

Purpose: One member's current intention for one event. Owner: C5.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| event_id | objectId | Required, non-null;  |
| user_id | objectId | Required, non-null;  |
| status | string | Required, non-null; length 1–20; enum attending, not attending;  |

Invariants: Pair unique; user must be a current member at write; absence derives pending, never stored as status.

Relationships: Many responses to one event and user.

Volume (fresh fixture now / Week 16 estimate): 0 / 1250 maximum at baseline scale. These are planning estimates, not quotas.

Lifecycle: Upsert on I11; replace status; hard-delete on user/event/unit cleanup.

### Entity: sessions (serves FR-AUTH-02)

Purpose: One revocable browser login. Owner: C2.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | objectId | Required, non-null; primary key;  |
| token | string | Required, non-null; length 43–43; pattern `^[A-Za-z0-9_-]{43}$`;  |
| user_id | objectId | Required, non-null;  |
| expires_at | date | Required, non-null; UTC instant |

Invariants: Token unique and generated with 32 random bytes encoded URL-safe; absolute expiry 8 hours; validate on every protected request regardless of TTL deletion.

Relationships: Many sessions to one user.

Volume (fresh fixture now / Week 16 estimate): 0 / 100 active estimate. These are planning estimates, not quotas.

Lifecycle: Insert on login, delete on logout/re-login of same browser/user deletion; TTL eventually removes expired rows.

### Entity: login_attempts (serves FR-AUTH-02)

Purpose: One normalized username's login-attempt window. Owner: C2.

| Field | BSON type | Nullability / constraint |
|---|---|---|
| _id | string | Required, non-null; primary key; length 3–32; pattern `^[a-z0-9_]{3,32}$`;  |
| count | int or long | Required, non-null; minimum 1;  |
| expires_at | date | Required, non-null; UTC instant |

Invariants: count includes all validly formed login attempts in window; 11th denied; atomic reset after 15 minutes; success deletes row.

Relationships: Zero or one window per username; unknown usernames may also have a window.

Volume (fresh fixture now / Week 16 estimate): 0 / 100 active estimate. These are planning estimates, not quotas.

Lifecycle: Atomic upsert on login; delete on successful login/admin cleanup; TTL removes expired rows.

### Entity: schema_migrations (serves CON-01, NFR-MAINT-01)

Purpose: one applied manifest. Owner C6. Required non-null fields: _id:string four digits (primary key), sha256:string 64 lowercase hex, applied_at:BSON UTC date. At most one row per migration; recorded hashes never change. No user relationship. Fresh fixture: 0; Week 16 estimate: 1–5. Created only after successful migration; never deleted during normal operation. This is operational metadata, not a new user-data field.


### Migrations

Mechanism: numbered JSON manifests with strict MongoDB `$jsonSchema` validators and explicit indexes, applied by [migrations/run.py](../migrations/run.py). Ledger `_id='0001'` stores manifest SHA-256 and UTC application time. Direction: forward-only; never edit an applied manifest. Later schema changes require 0002 onward. This runner implements only 0001 and must be extended for additional migrations.

Migration 0001 targets an empty application database. It refuses non-empty unversioned collections; preserve existing data and design an explicit adoption/backfill migration instead of deleting it. Stop web writes and run one maintenance process. Creation/validation/index operations are not globally atomic: after interruption, rerun against the still-empty collections; ledger is written last. If the recorded hash differs, exit 1 without changing the database. CLI `--plan` is the default and performs no network access. `--apply` requires environment variables MONGODB_URI and MONGODB_DATABASE; no default target and no system database allowed. Migration errors exit 1, arguments exit 2, success exits 0. No downgrade or data deletion is provided.

From repository root:

```powershell
.\.venv\Scripts\python.exe migrations\run.py --plan
# Set MONGODB_URI and MONGODB_DATABASE securely before explicitly applying:
.\.venv\Scripts\python.exe migrations\run.py --apply
```

The migration role needs collection/index/validator privileges. Published MongoDB validation support is verified [V6]; exact Atlas account permissions and a real server execution remain pending. Contract tests of the runner are not proof of database validator enforcement. The prototype's startup index creation must be removed when the migration-based deployment is implemented.

Deletion lifecycle: stop application writes; verify requester control outside the app; C7 deletes the user's sessions and attempts, their responses, authored messages and memberships. It also deletes events created_by that user after deleting all responses to those events, then deletes the user document. Reject deletion of a unit owner until an authorized unit deletion is approved; there is no owner-transfer UI. For a unit deletion, delete responses for its event IDs, then events/messages/memberships, then the unit. Run the same query sequence again to verify zero remaining references; resume after failure from the beginning. This is an idempotent maintenance procedure, not a pretend cross-collection cascade. Delete synthetic backups containing the subject within the same 7-day request window; provider-side retention limitations stay in Q3. C7 creates no new PII collection. Store only aggregate completion/date in the maintenance record.

## 7. Sequence Flows

### F1 — Attendance intention and accountability roster

1. Browser GETs I6 with signed cookie; C1 asks C2 to resolve an unexpired session and C3 to authorize membership.
2. C5 loads unit events and the member's current response; C1 renders a CSRF-protected form.
3. Browser POSTs I11 with status and token; C1 validates; C3 checks membership; C5 verifies the event belongs to the URL unit.
4. C5 upserts one response keyed by event_id/user_id through C6; unique index prevents a second document. Return 302 only after acknowledgement.
5. Browser follows GET; leaders see every current member with latest intention or derived pending; members see only their own response alongside event details.

| Step | What can go wrong | System behavior | User sees |
|---|---|---|---|
| 1 | Session absent/expired; outsider | 302 login or 403, no unit data | Login or access-denied page. |
| 2 | Database unavailable | Stop at shared deadline; 503 | Reload later; no stale roster represented as current. |
| 3 | Tampered CSRF/status/event ID | 400, 403 or 404; no mutation | Corrective error; authentication first. |
| 4 | Concurrent identical upsert; timeout | Unique conflict: reread once within deadline; if desired state exists treat as success, otherwise 409; ambiguous timeout 503 | Refresh before resubmitting; no claim of saved state on timeout. |
| 5 | Another tab changed intention | Render latest acknowledged state | Most recent value; no duplicate row. |

### F2 — Login across the database boundary

1. Browser GETs I2; C1 issues CSRF token and login form without a credential lookup.
2. Browser POSTs I2; C1 validates fields/CSRF and creates a request ID.
3. C2 atomically increments the username attempt window in MongoDB; reject count over 10 within a 15-minute window. A single update pipeline resets an expired window and increments a live one; do not do a racy read-then-reset sequence.
4. C2 reads the user, checks the hash, removes the previous browser token if any, and inserts a new random session with an 8-hour absolute expiration. Delete successful login's attempt row.
5. C1 clears prior cookie state, sets the new signed cookie and redirects to I4; C2 verifies the token on that GET. No redirect is sent until session insertion is acknowledged.

| Step | What can go wrong | System behavior | User sees |
|---|---|---|---|
| 1 | Cookie disabled | Form may render; POST cannot satisfy session-bound CSRF | Enable cookies and reload. |
| 2 | Missing/overlong password | 400 without database mutation | Field-specific validation, no password echo. |
| 3 | Throttled or database unavailable | 429 with Retry-After seconds to window end, or bounded 503 | Wait time or service-unavailable page. |
| 4 | Bad credentials / write ambiguity | 403 invalid_credentials for bad password; 503 for DB errors | Same credential message for unknown and known usernames. |
| 5 | Lost redirect / lost cookie | Old token remains revoked; a newly inserted unreceived session expires later | Login again; no role cached in browser. |

### F3 — Login with MongoDB unreachable

1. Browser submits valid login form; C1 establishes one 5-second database-operation deadline for the entire request.
2. C2 asks C6 to update the attempt window; DNS/network/server selection cannot complete.
3. C6 raises a typed dependency failure; C1 returns 503 with the common envelope and request ID. No automatic application retry occurs.
4. Operator inspects health using I12, restores connectivity, then confirms health returns 200 within the NFR-REL-02 5-minute recovery window. User deliberately retries login.

| Step | What can go wrong | System behavior | User sees |
|---|---|---|---|
| 1 | Previously loaded form is stale | Invalid CSRF returns 400 before DB work | Reload the form. |
| 2 | Connection unavailable | Single request deadline; no offline authentication | Waiting bounded by DB budget plus rendering. |
| 3 | Response lost; update may have committed | No success acknowledgement; log event type/request ID only | Reopen page; an attempt may count against throttle. |
| 4 | Provider outage continues | Remain fail-closed; operator uses separate synthetic local-demo profile | 503 remains on hosted app; local demo clearly labeled as separate data. |

## 8. Error Handling and Edge Cases

| Category | Policy |
|---|---|
| Invalid input | 400 + stable code/field corrections; no write after failed validation. |
| Not authorized | Missing session 302 login; authenticated outsider/role failure 403; check permissions on every operation. |
| Not found | 404 for malformed/nonexistent IDs or event outside authorized unit; never reveal another unit's event. |
| Conflict | 409 duplicate username/unique conflict; idempotent membership add preserves current role. |
| Dependency failure | 503 by request deadline; fail closed and distinguish unknown mutation outcome. |
| Exhaustion | 413 body cap; 429 login window; 503 provider quota exhaustion; no automatic paid upgrade. |

For every call that leaves the web/maintenance process:

| Call | Timeout (s) | Retries + backoff | Fallback | User is told? |
|---|---:|---|---|---|
| PyMongo business reads/writes, including auth and index-version check | 5 total per HTTP request, using one `pymongo.timeout(5)` context | Application 0; set retryReads=false and retryWrites=false for explicit bounded behavior; no backoff | 503; preserve persisted state; separate local synthetic demo only | Yes; mutation result may be unknown. |
| Health ping | 2 total | 0 | JSON 503 envelope | Yes; no credentials disclosed. |
| MongoDB connection/TLS/DNS | serverSelectionTimeoutMS=2000, connectTimeoutMS=2000; outer 5 s deadline | Driver topology discovery may probe; outer deadline bounds operations | Fail closed | Yes via 503. |
| Migration collection/validator/index commands | 60 total for migration | 0 automatic; manual rerun after inspecting error | Keep web stopped; preserve prior records | CLI generic failure and exit 1. |
| Administrative deletion/backup/restore | 900 total maintenance time box; 5 s per application data operation | No automatic retry; operator resumes documented idempotent deletion or restores into separate DB | Stop writes, retain source/backup, report incomplete maintenance | Operator and requester get completion status only. |

The app makes no outbound HTTP calls, sends no mail, and loads no third-party browser resources. Browser navigation timeout is not under server control. Vendor deployment/build operations happen outside this process and are operator tasks. Use connection maxPoolSize=10 per worker; no nested timeout blocks that reset the request budget. Client-side database timeout semantics are verified in V1; chosen numeric budgets are project decisions. Create the client once at worker startup, outside request handling: SRV DNS resolution during client construction may block and is not covered by a later timeout context [V7]. The 60-second migration budget similarly covers database operations after client creation, not OS DNS initialization; an operator must interrupt startup if resolution stalls beyond 30 seconds. Explicit health handling bypasses normal session resolution so a stale cookie cannot turn a health probe into an extra database query.

Edge-case register (each row is a future acceptance test):

| # | Edge case | Expected behavior |
|---|---|---|
| E01 | Username differs only by case/whitespace | Normalize, reject duplicate 409. |
| E02 | Two concurrent registrations for same username | Exactly one user; other receives 409. |
| E03 | Empty password or 129 characters | 400, no hash/session created. |
| E04 | Admin username with missing/wrong setup token | 403; no user. |
| E05 | Cookie replay after acknowledged logout | 302 login, no protected content. |
| E06 | Session expires before TTL removes document | Deny by expires_at, independently of cleanup. |
| E07 | POST omits or tampers with CSRF | 400; zero mutation. |
| E08 | Logged-in outsider knows unit ID | 403 for read and all writes. |
| E09 | Member submits role=owner | 403 if caller lacks owner permission; owner with invalid role gets 400. |
| E10 | Owner targeted by role edit | 403; owner remains owner. |
| E11 | 101 messages or identical timestamps | Display latest 100, stable created_at/_id order. |
| E12 | Script markup in name/message | Escaped text; no executable markup. |
| E13 | Event time lacks offset | 400 with offset-aware example. |
| E14 | Event ID belongs to other unit | 404 after authorization of URL unit. |
| E15 | Repeat identical attendance POST | One response document, same desired value. |
| E16 | Concurrent opposite attendance POSTs | Last successful database update wins; one row. |
| E17 | Database timeout after a write was sent | 503 outcome unknown; refresh/check before retry. |
| E18 | Request over 65,536 bytes | 413 before handler mutation. |
| E19 | Member added after event creation | Leader roster includes member as pending. |
| E20 | Duplicate membership add for owner | No-op; never downgrade to member. |
| E21 | 11th login attempt in live window | 429 with remaining seconds, even if password is correct. |
| E22 | Expired login-attempt row remains | Atomically reset window; allow fresh first attempt. |
| E23 | Unit insert succeeds but owner insert fails | Abort transaction; no visible orphan unit. |
| E24 | Migration interrupted before ledger | Keep app stopped; rerun only against empty initial collections. |
| E25 | Malformed UTF-8 / duplicate form field | 400; never silently choose one duplicate. |
| E26 | Keyboard-only form use at 390 px | Visible focus, labeled inputs/errors, no horizontal task obstruction. |

## 9. External and Nondeterministic Dependencies

There is no AI component. MongoDB Atlas is the riskiest third-party dependency. Contract: an environment-supplied MongoDB URI and database select the persistence service; the application sends BSON queries/updates for only the collections in §6, over verified TLS. Use a restricted application credential and a separate migration credential. The provider receives synthetic identity labels, hashed passwords, text, event/response metadata and session tokens; never send official personnel data. No password, URI, form content, cookie or raw database exception enters application logs. Log only request_id, route template (not actual IDs), status, duration and exception class; application-created local diagnostic captures expire after 7 days. Provider retention is independently unresolved in Q3.

Set majority write concern for the hosted replica-set profile; acknowledge mutation success only after the configured concern succeeds [V7]. Unit + owner membership use one explicit transaction; no automatic transaction retries. A transient transaction or commit ambiguity becomes 503, then operator reconciliation. Plain standalone local MongoDB is adequate only for read-only synthetic demonstrations; to exercise unit creation, use a local single-node replica set. Single-document response updates are atomic but cross-collection invariants are not automatic [V4].

Budget: $0/month planned for explicitly selected free tiers; aggregate spending cap $10/month from CON-02. Do not enable paid upgrades automatically. Project warning thresholds: 80% displayed storage/transfer allowance, 80% monthly host hours, or 2 missed demos. These are operator checks, not invented provider hard limits. At quota exhaustion fail closed and fall back to the isolated local profile. The local profile uses separate secrets, local MongoDB and synthetic fixtures, and has no Atlas dependency; it does not synchronize or accept writes on behalf of the unavailable hosted database. Actual local replica-set recovery and hosted acceptance remain verification tasks.

| Fact | Value | Source URL | Date checked |
|---|---|---|---|
| V1 PyMongo timeout | timeout() bounds operations inside its context; timeoutMS bounds individual operations | https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/csot/ | 2026-10-04 |
| V2 MongoDB TTL | Cleanup is asynchronous; expiry index is not an authorization guarantee | https://www.mongodb.com/docs/manual/core/index-ttl/ | 2026-10-04 |
| V3 Flask configuration | MAX_CONTENT_LENGTH and cookie Secure/HttpOnly/SameSite settings are supported | https://flask.palletsprojects.com/en/stable/config/ | 2026-10-04 |
| V4 Atomicity | Single-document writes atomic; multi-document changes require transaction semantics | https://www.mongodb.com/docs/manual/core/write-operations-atomicity/ | 2026-10-04 |
| V5 Free providers | Render free service sleeps after 15 idle minutes and has ephemeral disk; Atlas Free lacks managed backups | https://render.com/docs/free ; https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/ | 2026-10-04 |
| V6 Schema validation | MongoDB supports BSON-aware $jsonSchema validation | https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/ | 2026-10-04 |
| V7 Driver options | MongoClient accepts documented timeouts/pooling/read-write retry and concern options | https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html | 2026-10-04 |
| V8 Password hashing | generate_password_hash/check_password_hash provide hash generation/verification | https://werkzeug.palletsprojects.com/en/stable/utils/ | 2026-10-04 |
| V9 Hosting root | Blueprint rootDir locates a service below repository root | https://render.com/docs/blueprint-spec | 2026-10-04 |

Vendor facts were checked by the assistant. Student verification/signature remains pending. Existing dependency versions are pinned in requirements files; no claim of “latest” or cross-platform compatibility is made. Use explicit Werkzeug method `scrypt:32768:8:1` and salt_length=16 as the design choice, verified as accepted syntax in V8; performance must be measured on the selected host. Pin updates require regression/security review. If a provider retires a tier or changes supported runtime, update the dependency pin/configuration only after a clean rebuild and revisit the relevant ADR if cost/architecture changes. Numeric request, retention and field limits elsewhere are project contracts, not provider promises.

## 10. Traceability

Every Must requirement in version 0.4 maps to a component, an interface and a flow. NFR rows identify where acceptance tests apply; none of these mappings assert tests already passed. F1 covers member/leader interaction, F2 identity, F3 dependency failure; I13–I15 cover operator and verification contracts.

| Requirement | Priority | Component(s) | Interface(s) | Flow |
|---|---|---|---|---|
| FR-AUTH-01 | Must | C1, C2 | I1 | F2 |
| FR-AUTH-02 | Must | C1, C2 | I2, I3, I4 | F2, F3 |
| FR-AUTH-03 | Must | C2 | I1 | F2 |
| FR-UNIT-01 | Must | C3 | I5 | F1 |
| FR-UNIT-02 | Must | C3 | I7 | F1 |
| FR-UNIT-03 | Must | C3 | I8 | F1 |
| FR-MSG-01 | Must | C4 | I6 | F1 |
| FR-MSG-02 | Must | C4 | I9 | F1 |
| FR-EVT-01 | Must | C5 | I10 | F1 |
| FR-EVT-02 | Must | C5 | I11 | F1 |
| FR-EVT-03 | Must | C5 | I6 | F1 |
| FR-ACCESS-01 | Must | C1, C3 | I4, I5, I6, I7, I8, I9, I10, I11 | F1 |
| FR-HEALTH-01 | Should | C6 | I12 | F3 |
| NFR-PERF-01 | Must | C1, C5, C6 | I6, I15 | F1 |
| NFR-PERF-02 | Should | C1 | I6, I15 | F1 |
| NFR-REL-01 | Must | C6 | I15 | F1, F2, F3 |
| NFR-REL-02 | Must | C6, C7 | I12, I15 | F3 |
| NFR-SEC-01 | Must | C1, C3 | I5, I6, I7, I8, I9, I10, I11, I15 | F1 |
| NFR-SEC-02 | Must | C1 | I1, I2, I3, I5, I7, I8, I9, I10, I11, I15 | F1, F2 |
| NFR-SEC-03 | Must | C2, C6 | I1, I2, I13, I15 | F2 |
| NFR-SEC-04 | Must | C1 | I6, I9, I15 | F1 |
| NFR-PRIV-01 | Must | C2, C3, C4, C5, C7 | I1, I6, I14, I15 | F1, F2 |
| NFR-PRIV-02 | Should | C7 | I14 | F3 |
| NFR-A11Y-01 | Must | C1 | I1, I2, I4, I6, I15 | F1, F2 |
| NFR-A11Y-02 | Must | C1 | I1, I2, I3, I9, I11, I15 | F1, F2 |
| NFR-USE-01 | Should | C1 | I15 | F1, F2 |
| NFR-USE-02 | Must | C1 | I1, I2, I7, I9, I10, I11, I15 | F1, F2 |
| NFR-MAINT-01 | Must | C6 | I13, I15 | F3 |
| NFR-MAINT-02 | Should | C7 | I15 | F1, F2, F3 |
| NFR-PORT-01 | Should | C6 | I12, I13, I15 | F3 |

## 11. Open Questions and Design Risks

All core design choices above are concrete. These questions concern baseline ownership, external configuration or evidence; none is permission to guess a different contract during implementation.

| # | Open question | What it blocks | Owner | Decide by |
|---|---|---|---|---|
| Q1 | Does the owner approve baseline 0.4 rather than the conflicting older CSV? | Final baseline signature and legacy traceability reconciliation; use 0.4 meanwhile | lpheng104 | 2026-10-06 |
| Q2 | Can SP-02 complete against the actual Render/Atlas accounts, including transaction and migration permissions? | Hosted acceptance and NFR-PORT-01; design stays fixed | lpheng104 | 2026-10-08 |
| Q3 | What provider retention/deletion settings apply, and does the instructor accept the administrative deletion path? | NFR-PRIV-02 acceptance and any real-user trial | lpheng104 / instructor | 2026-10-08 |
| Q4 | Does SP-03 restore the stated records and indexes in 15 minutes? | Recovery acceptance; no backed-up-data promise before measurement | lpheng104 | 2026-10-09 |
| Q5 | Are ASM-04 unit size and synthetic-only demonstration approved? | Baseline scale and user testing; maintain conservative fictional-data scope | lpheng104 / sponsor | 2026-10-06 |
| Q6 | Has the owner read vendor facts, contracts and diagram relationships? | Changing Draft to Baselined and signing submission | lpheng104 | 2026-10-04 |

## 12. Change Log for This Document

| Version | Date | Change | Why |
|---|---|---|---|
| v0.1 | 2026-10-04 | Establish target contracts, component/state boundaries, schema migration, three flows, error policy and traceability. | Milestone 6 blueprint for implementation and review. |

Reproduce static checks from repository root with `.\.venv\Scripts\python.exe code\spec-check.py docs\architecture.md docs\requirements.md`. The checker was authored locally because no course-provided `spec-check.py` was present or attached. It checks structure, reference coverage, contracts, state ownership, dependency cycles and required artifacts; it cannot establish semantic correctness, accessibility, security or provider behavior. Validation output is recorded in the Week 6 hours/verification entry. Local-only commits follow the owner's prior instruction; no remote push is performed.
