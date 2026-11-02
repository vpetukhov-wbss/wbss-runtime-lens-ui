# Contributing

The project is currently in planning/design. Start from an issue and the linked Figma screen; implementation should preserve the core-versus-extensions boundary.

Use synthetic fixtures only. Do not add live telemetry, credentials, private infrastructure or customer data. Keep server authorization separate from UI visibility checks. Generate clients from a reviewed versioned OpenAPI artifact; do not hand-edit generated output.

A feature PR should describe the observable behavior, reference its screen/issue, cover loading/empty/error/permission states and include relevant validation. Runtime bootstrap, accessibility checks and CI commands will be documented when the application exists; no placeholder passing checks are provided.

For large log/trace datasets, use server-side filtering/pagination and bounded visualization. Profiling results must show coverage and uncertainty; do not present sample estimates as exact costs.
