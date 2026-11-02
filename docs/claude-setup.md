# Claude Code setup

This is a repository-specific Angular / TypeScript setup. It installs instructions and on-demand workflows, not the Claude CLI, account credentials or a running application.

## Sources and tailoring

- User baseline: [ai-engineering-setups](https://github.com/vpetukhov-wbss/ai-engineering-setups), revision f5c3583f91383240edf3710fc7f1168b7b11dfa7.
- Modular foundation: the user's build-claude-engineering-standards skill, with an explicit stack selection because this repository has no application manifests yet.
- Selected upstream rules/skills/knowledge are listed in .claude/manifest.json. Imported text retains MIT attribution in .claude/UPSTREAM-LICENSE.txt; the repository license is unchanged.
- Root CLAUDE.md is tailored to actual RuntimeLens facts and directs product-specific work to the existing documentation and Figma links.
- Framework rules use planned paths, including modern src/**/*.ts component filenames, templates and e2e tests.

## Scope

Core observability leads; EF/Dapper, dependency inventory and profiling are additions. The backend is a modular monolith with a separate telemetry pipeline. The UI is a separate public repository using reviewed API artifacts and synthetic fixtures.

No speculative generic repositories, mediator/mapping framework, message broker, event sourcing, extra services or frontend state library is introduced. No MAUI, Blazor, React or Ionic instructions are installed. Irrelevant legacy/domain/frontend procedures were removed from the selected template. Optional specialist-agent profiles, shell hooks, blanket permission grants and MCP credentials were not added.

Nebular remains the proposed UI library and Aquila remains an alternative. Select the library and compatible versions during bootstrap; the setup does not silently finalize that product choice.

## Use

From an updated local checkout, run claude. Review its loaded project memory with /memory, then invoke an installed workflow, for example /runtime-lens-screen or /angular-feature. Startup alone is not an instruction to create the application.

## Validation

Run: python3 scripts/validate-claude-setup.py

The standard-library validator checks skill metadata, names, local references, Markdown fences, representative path globs and upstream attribution. It is deliberately independent of application frameworks. In a Git checkout also run git diff --check.

No solution/csproj or package/Angular manifests exist, so application build/test/lint commands are unavailable. Live Claude CLI memory/rule loading must be checked in a local session; structural validation is not evidence of runtime loading, working API integration or deployment. When application scaffolding is introduced, update CLAUDE.md with its exact verified commands and run the real framework checks.
