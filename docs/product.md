# Product scope

WBSS RuntimeLens is a general-purpose observability platform for .NET applications. The primary experience connects requests, distributed traces, logs, errors, metrics, background jobs, releases and alerts.

Database diagnostics (EF Core/Dapper), dependency inventory and profiling are optional additions. They must not become a prerequisite for basic onboarding or dominate the default overview.

## Core MVP

- Organizations, projects, applications, environments and scoped ingestion keys.
- HTTP request analytics and trace waterfall with log/error correlation.
- Structured logs and grouped error occurrences.
- HTTP/runtime/custom metrics; raw counters/histograms are separate from sampled traces.
- Background operation executions, duration and failure; queue wait/retries only where adapters report them.
- Release metadata and baseline comparisons, threshold alerts with cooldown.
- Read-only MCP using user/project permissions.

## Optional roadmap

1. EF Core/Dapper Database Lens with query fingerprints and N+1 candidates.
2. Direct/transitive dependency inventory tied to releases.
3. Explicit profiling capture/import with sample-to-assembly/package mapping and confidence.
4. Controlled CI performance budgets.

## Product constraints

A slow SQL span is not database-server CPU. Long wall time is not CPU consumption. Package inventory is not package runtime cost. Sampled allocations are not retained heap ownership. Findings carry supporting evidence and uncertainty.

## Delivery status

Planning and editable Figma design only. No backend, SDK package, deployed environment or running dashboard is shipped yet. Demonstration values in Figma are fictional.
