# Architecture decision index

Inventory checked against actual files on 2026-11-22. Owner: Liam Pheng. Source statuses are preserved; “implemented” observations do not retroactively turn a Proposed record into signed acceptance.

| Number / record | Decision | Current status | Consequence a successor notices |
|---|---|---|---|
| [0001](<ADR 0001>) | Server-side session revocation | Proposed in original record; database-token behavior implemented | Old cookies fail after server-side logout; query expiry still matters before TTL cleanup. |
| [0002](<ADR 0002>) | Operate MongoDB with Atlas for hosting | Proposed in original record; later Atlas deployment evidenced | Laptop shutdown does not stop the hosted data store; backups and network access require provider operations. |
| [0003](<ADR 0003>) | Render application hosting | Proposed in original record; later deployment evidenced | Public Gunicorn service differs from local Flask; free-tier wake time and deployment SHA must be checked. |
| [0004](<ADR 0004>) | Retain MIT source license | Proposed record; LICENSE currently MIT | Preserve copyright/license notices; cloud service terms remain separate. |
| [0005](0005-admin-bootstrap-boundary.md) | Separate global admin bootstrap from unit roles | Retrospective documentation; implemented behavior, reviewed by Liam Pheng on 2026-11-22 | One configured global admin; setup token is not a password or multi-admin grant. |

The extensionless legacy filenames are intentional existing files. Older prose that names nonexistent 0001-session-revocation.md-style files should use this index. Keep superseded records; add a new dated record when reversing a decision. Do not rewrite the original approval history.
