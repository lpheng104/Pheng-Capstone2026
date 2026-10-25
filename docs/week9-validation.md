# Week 9 integrated validation

Owner: Liam Pheng. Instructor: Dr. Litman. Date: 2026-10-25.

The remote-main integration preserves the repository's original history and coursework. Root src/ and tests/ are the publication layout. The separately verified local prototype tag is not confused with the final integrated release.

Integrated local checks: hash-locked bootstrap/migration/seed passed in a separate environment and database; lint passed; five application/service tests passed in 6.72 seconds with 191 mock-library deprecation warnings; build passed; the repository traceability checker reported 43 rows and zero findings. Real HTTP login, the complete protected read path and a direct MongoDB change reflected in HTML passed. Full fetched/local-ref history and tracked/unignored source secret scans reported no findings; output is pasted in skeleton-trace.md.

Eight issues #37–#44 are verified on the existing project board. The next commit deliberately introduces one failing regression test to prove the remote pipeline rejects a failure. Its removal will be a separate fix commit. No green/red run URL or remote release tag is claimed until observed.

Remote completion: PR #45 merged; deliberate red https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/40232422421; fix cbf0213595e247f57803f840548e50e218199c59; fixed push and PR green; main green https://github.com/lpheng104/Pheng-Capstone2026/actions/runs/40233100468. All CI stages including datastore mutation and outage proof passed. Main-branch evidence is actual GitHub output, not inferred from local checks.
