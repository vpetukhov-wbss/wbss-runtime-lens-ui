# Change workflow

Before editing:

- Read the task, repository instructions, relevant implementation, tests, manifests, and nearby conventions.
- Trace callers, consumers, contracts, persistence, and security implications.
- State unresolved assumptions; ask only when a choice materially changes the result.

While editing:

- Keep the diff focused and preserve unrelated changes.
- Prefer complete vertical behavior over disconnected scaffolding.
- Do not reformat unrelated files or perform opportunistic migrations.
- Add dependencies only after checking whether the platform or existing stack already solves the need.

Before finishing:

- Review the full diff.
- Format/lint, build, and run focused tests; expand verification according to risk.
- Check failure, concurrency, cancellation, authorization, accessibility, and observability paths.
- Report exactly what ran and any remaining risk.
