# UI/API contract proposal (v0.1, not implemented)

The backend owns the versioned OpenAPI document. The public UI must build and demo with synthetic fixtures; access to the private backend repository is not required. When an API is implemented, publish its reviewed contract into this repository or a versioned contract artifact; generate the Angular client from that artifact. No cross-repo private source dependency.

## Shared scope and semantics

- Query base: /api/v1/projects/{projectId}. Authenticated OIDC bearer token, with server-side project membership authorization.
- Filters: applicationId, environment, release, from and to (UTC ISO-8601; [from,to)), traceId, search. Retain these in router/query state when drilling down.
- Time values: durationMs; telemetry timestamps in UTC, presentation timezone explicit. Percentage fields carry clear units (0–100 percent); comparison deltas distinguish percent from percentage points.
- Cursor pagination: items, nextCursor, hasMore. Stable ordering uses timestamp and a stable identifier. Heavy queries have bounded ranges, page sizes and deadlines.
- Analytics responses identify sample coverage and comparison windows. Counts from sampled traces are labeled estimates; request metrics do not silently use sampled span counts.
- Structured errors use Problem Details with stable error code and request/trace correlation identifier. Handle 401, 403, 404, 409, 429 and unavailable telemetry explicitly.

| Proposed resource | Purpose |
|---|---|
| GET /overview | Overview counters, health and trends |
| GET /applications | Application/runtime/release and heartbeat state |
| POST /applications | Register an application/environment |
| GET /requests/operations | Aggregated operation metrics |
| GET /traces | Filtered trace summaries |
| GET /traces/{traceId} | Span tree and execution context |
| GET /logs | Structured logs, optionally trace-scoped |
| GET /errors/groups | Defect grouping and occurrence counts |
| GET /metrics | Bounded metric series, units and aggregation |
| GET /jobs | Operation/execution analytics |
| GET /releases | Release summaries and comparable baselines |
| GET,POST /alerts/rules | Rule configuration and status |
| GET,POST /ingestion-keys | Key metadata / scoped key creation |
| POST /ingestion-keys/{keyId}/revoke | Explicit audited revocation |

Resource paths above are relative to the project query base. Module-specific endpoints are separate additions. MCP is read-only and uses the same authorized query services; it is not an arbitrary SQL endpoint.

## Ingestion is a separate boundary

OTLP ingestion uses write-only application/environment credentials. It is not the user's query API. Gateway resolves organization scope from credentials and overwrites untrusted scope attributes. Full keys are returned only on creation, then represented as metadata. Never include live keys in public examples or fixtures.

## Client authentication

Use OIDC authorization code with PKCE for the browser client. The provider/client details are runtime environment configuration, with no client secret embedded in the SPA. UI capability checks improve UX; authorization always belongs to the server. Browser token persistence policy is reviewed during implementation.

## Next validation

Replace this proposal with validated OpenAPI endpoints during the first vertical slice. Contract checks must cover filters, pagination, authorization failures, error envelopes and schema compatibility. A newly mocked resource must remain visibly a demo until implemented.
