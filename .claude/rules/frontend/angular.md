---
paths:
  - "src/**/*.ts"
  - "src/**/*.html"
  - "src/**/*.scss"
  - "src/**/*.css"
  - "angular.json"
  - "package.json"
---

# Angular

- Detect the installed Angular version before using version-specific APIs. Do not turn a feature task into a framework migration.
- For compatible modern projects, prefer standalone components, signals for local state, `computed` for derivation, `input`/`output`/`model`, `inject`, native control flow, and lazy feature routes.
- Do not write `standalone: true` where the installed Angular version already makes it the default.
- Follow the installed version's change-detection defaults; do not add `OnPush` mechanically when it is already the default.
- Keep components focused on presentation and coordination. Put reusable domain/data behavior in focused services or feature state.
- Keep templates declarative and simple. Move complex transformations to computed state or pure functions.
- Prefer class/style bindings over `ngClass`/`ngStyle` in compatible modern code.
- Use `NgOptimizedImage` for eligible static images.
- Prefer signal forms when stable and already adopted by the project; otherwise use strictly typed reactive forms for non-trivial forms.
- Use signals for synchronous state and RxJS for asynchronous streams/events where its operators add value. Do not convert back and forth without need.
- Complete subscriptions with framework interop such as `takeUntilDestroyed`; prefer `async` pipe when the template owns the subscription.
- Keep state transformations pure; use `set`/`update`, not in-place mutation.
- Use route guards for navigation UX, never as the sole server authorization control.
- Meet WCAG AA and automated accessibility checks; manage focus for routes, dialogs, and dynamic errors.
- Test observable user behavior and service contracts, not private implementation.
