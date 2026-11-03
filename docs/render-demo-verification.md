# Render demo verification

Owner: Liam Pheng. Instructor: Dr. Litman. Verified: 2026-11-02.

Public URL: [https://accountabilibuddy-demo.onrender.com](https://accountabilibuddy-demo.onrender.com). Free Python web service in Ohio. Source: main commit 8c51504cf5a63d63c29b862b6789a9241bf35796 (PR #51). The iteration-1 tag remains unchanged.

Render service: srv-dbkk7umi0phs73agshig. Successful deployment: dep-dbkka2t9fdbs73bir28g. Render reported “Deploy succeeded | Live” at November 2, 2026, 8:21 PM Central; deployment duration 52.6 seconds. Gunicorn listens on Render's assigned PORT with the existing Flask factory.

| Check | Observed result |
|---|---|
| Public TLS/health | HTTPS GET /health returned 200 and status ok, including a real Atlas ping |
| Login page | Public browser rendered the real Accountabilibuddy sign-in form |
| Session cookie | Secure, HttpOnly, SameSite=Lax |
| CSRF | POST /login without a token rejected with HTTP 400 |
| Authenticated access | Existing fictional iteration_member signed in and opened Iteration One Squad |
| Persisted data | Hosted unit page displayed Practice briefing and Keep this formation from Atlas |
| Anonymous access | Independent unauthenticated unit request redirected to /login |

The first deployment built successfully but failed its Atlas TLS/server-selection connection. Render showed outbound ranges 74.220.50.0/24 and 74.220.58.0/24. Liam Pheng added those ranges to Atlas Network Access; a redeploy succeeded without disabling TLS or broadening access to all IPs. Secrets were entered privately in Render by Liam Pheng. None appear in source, this record or screenshots. The full local .env was not imported.

Other devices can use the public HTTPS URL without the development computer running. A physical second-device test is left for Liam Pheng; the automated checks used the public service rather than localhost. Existing Atlas accounts work; local-only accounts have not been migrated. New registrations initially have no unit access until an authorized leader adds them. The hosted administrator setup token is the independently generated Render value, not the local token.

Free instances can sleep when idle; Render warns that a cold request can take 50 seconds or more. This remains a fictional-data working demo with the personal review and remaining feature gates documented in the iteration-one evidence. It is not full product acceptance or production-readiness certification.
