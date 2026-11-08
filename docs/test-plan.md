# Milestone 11 test plan

## 1. Scope
Accountabilibuddy at baseline `c5b8937` (full SHA in results). Verify account, unit, chat, event and permission flows and map every written SRS criterion. 

## 2. Out of scope
No mutation of Render, Atlas, or real accounts. Hosted performance and accessibility, participant usability, provider interruption, privacy deletion and complete portability need separate environments or people; keep their criteria visible as gaps. No changes to the hours log.

## 3. Levels
Unit: validation and equivalence partitions. Integration: real MongoDB schema, uniqueness and persistence. Acceptance: Flask request client exercises routing, forms, sessions, HTML and persistence in a controlled environment; browser and human-only requirements have manual procedures/gaps. Existing live HTTP smoke separately exercises actual sockets.

## 4. Environment
Python from `.python-version`, dependencies from `requirements.lock`, MongoDB 8.0.17 on loopback, independent disposable database. No `.env` or Atlas connection is used by the new tests. Deterministic fictional fixture families use seed 1108.

## 5. Entry criteria
Baseline and requirement document identified; fixture regeneration reproducible; dependency pins available; disposable loopback MongoDB reachable for the full run.

## 6. Exit criteria
Zero unexpected test failures, at least three real integration tests executed without skips, all 43 requirements represented, every Must has at least one case, and at least eight reproducible defects logged. Release gate: 100% verified Must requirements and zero open severity S1/S2 defects. A green regression suite does not clear that gate if known defects or unverified criteria remain.

## 7. Testing risks
Mock fidelity: check indexes and persistence against real MongoDB. Shared-data contamination: require loopback and use uniquely named disposable databases. Timing noise: report actual elapsed time and avoid claiming a hosted performance threshold from a local run. Expected failures must be strict so a surprise pass requires triage.

## 8. Schedule
November 8, 2026: prepare plan, derive and execute cases, capture results and triage, then present the changes to Liam Pheng. Only after review/signoff: commit and push with the assignment’s exact message and confirm CI.

## 9. Signature
Liam Pheng 08NOV2026
