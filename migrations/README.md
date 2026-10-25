# Initial MongoDB schema

`0001_initial.json` is the immutable manifest after application. It defines eight application collections, typed required fields, validators and indexes; `run.py` also creates the migration ledger. See architecture §6 for cross-collection invariants and deletion lifecycle.

From the repository root, `.\.venv\Scripts\python.exe migrations\run.py --plan` prints the canonical JSON checksum without reading credentials or contacting MongoDB.

Only use `--apply` after stopping application writes and setting MONGODB_URI and MONGODB_DATABASE in the operator environment. Use a disposable empty database first. The runner rejects non-empty unversioned collections and unexpected collections; it never deletes or transforms application data. Use only one migration process. A failed initial attempt may be rerun while its collections remain empty. Once its ledger row exists, the same checksum is a no-op and a changed checksum is an error.

The canonical hash ignores JSON whitespace and object-key ordering, so Git line-ending conversion does not change it. Preserve array order. Do not edit an applied manifest. Future migration numbers require an extension of the runner; this deliverable implements 0001 only. Real MongoDB execution remains pending; mock tests are not database validation evidence.
