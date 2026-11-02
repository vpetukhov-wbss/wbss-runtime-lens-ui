# WBSS RuntimeLens UI

Angular dashboard for WBSS RuntimeLens: explore application health, distributed traces, logs, metrics, errors, background jobs, releases, and alerts, with optional database and dependency performance insights.

**Status: product design and documentation. The Angular application has not been scaffolded yet.**

[Open product design in Figma](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea) · [Overview](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-1852) · [Trace detail](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2510)

## Planned stack

Angular, Nebular (proposed), Apache ECharts. The API is maintained separately; this public UI will support a synthetic demo and a versioned generated API client without access to private backend source. Confirm the component library and compatible package versions during bootstrap.

## Documentation

- [Product scope](docs/product.md)
- [Design, screen links and implementation handoff](docs/design.md)
- [UI/API contract proposal](docs/api-contract.md)
- [Delivery backlog](docs/backlog.md)
- [Contribution guide](CONTRIBUTING.md)

Core observability comes first. EF Core/Dapper analysis, dependency inventory and profiling are optional extensions. All current design data is fictional. A public source repository does not imply a public hosted service or public Figma access.

## Claude Code

Repository-specific instructions are in [CLAUDE.md](CLAUDE.md). See the [setup guide](docs/claude-setup.md) for workflows, provenance and validation.
