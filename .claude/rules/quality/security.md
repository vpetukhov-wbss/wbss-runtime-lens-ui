# Security and privacy

- Treat all external input as untrusted, including headers, claims, filenames, URLs, serialized objects, and data returned by partner systems.
- Validate canonicalized input with allowlists and size/count/depth limits; encode output for its destination context.
- Enforce authorization server-side at resource and action level. Test tenant/user isolation and privilege changes.
- Use parameterized data access. Prevent injection into SQL, commands, templates, LDAP, paths, and dynamic expressions.
- Prevent SSRF with approved destinations, safe URL parsing, DNS/redirect policy, protocol restrictions, timeouts, and response limits.
- Prevent XSS with framework escaping, sanitization for intentional HTML, safe DOM APIs, and a restrictive CSP where feasible.
- Apply CSRF protection to cookie-authenticated state-changing requests and use appropriate SameSite/cookie flags.
- Keep secrets out of source, client bundles, logs, errors, URLs, analytics, and test fixtures. Use the platform secret store.
- Store passwords only through a current adaptive password hasher; prefer established identity/OIDC/OAuth libraries over custom crypto/auth.
- Validate uploads by size, content, type, name, and destination; store outside executable/public paths and scan when risk warrants.
- Use secure defaults for CORS, redirects, headers, TLS, cookies, token lifetime, and key rotation.
- Minimize personal data, define retention, and redact logs/traces. Never log credentials, tokens, session IDs, payment data, or full sensitive payloads.
- Pin and scan dependencies according to repository policy; assess reachability and exploitability before disruptive upgrades.
- Security failures should be observable without revealing sensitive internals to clients.
