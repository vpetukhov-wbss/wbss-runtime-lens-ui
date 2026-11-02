---
name: runtime-lens-screen
description: Implement or review a RuntimeLens Figma screen while preserving shared filters, typed API boundaries, accessibility and synthetic demo support.
---

# RuntimeLens screen

1. Read CLAUDE.md, docs/design.md, docs/api-contract.md, the issue and its exact Figma frame. Inspect installed Angular/UI/chart versions; resolve component-library choice during bootstrap.
2. Define route/project/application/environment/release/time state and loading/empty/partial/error/denied/rate-limit/unavailable behavior.
3. Reuse approved tokens/components. Keep meaningful TS, HTML and styles separate; keep view state out of generated DTOs and transport code.
4. Where no backend exists, use clearly marked synthetic fixtures. Integrate through a reviewed versioned API with cancellation, paging/virtualization and bounded charts.
5. Preserve operation → trace → logs/error context and explicit units/timezone/coverage. Optional insights cannot replace the core overview or imply exact CPU/memory attribution.
6. Run actual installed build/type/behavior checks and inspect keyboard/focus/contrast and the relevant viewport. Report unavailable checks; a static mock does not prove responsive/light-mode or backend integration.
