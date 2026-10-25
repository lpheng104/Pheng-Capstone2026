# Credential rotation — Liam Pheng

1. Revoke the exposed database credential or token immediately in its provider; stop affected application access.
2. Issue a replacement with minimum permissions and update local environment, hosting settings and any GitHub Actions secret; never paste it into an issue or log.
3. Rotate SECRET_KEY and ADMIN_SETUP_TOKEN when affected, revoke stored sessions, restart the app and verify the protected workflow with the new configuration.
4. Remove the exposed value from files and Git history with a reviewed history-rewrite procedure, coordinate any required force-push, and rerun the full-history audit; deleting only the latest line does not revoke a credential.
