---
name: frontend-component
description: Design and implement an accessible, responsive, testable Blazor, React, Angular, or MAUI Hybrid UI component or flow. Use for non-trivial components, forms, stateful interactions, shared web/hybrid UI, or design-system work.
---

# Frontend component or flow

1. Detect the framework/version, rendering/hosting model, design system, state/data conventions, and target devices.
2. Define user states: initial, loading, content, empty, validation, partial, error, offline, unauthorized, retry, and success.
3. Define semantic structure, keyboard path, focus behavior, labels, announcements, contrast, reduced motion, and responsive behavior.
4. Keep state at one clear owner; derive state rather than synchronizing duplicates.
5. Separate presentation from external I/O and domain operations only where it improves clarity/testability.
6. Handle cancellation, races, stale responses, optimistic rollback, and component disposal.
7. Reuse established tokens/components before creating new variants.
8. Test visible behavior with accessible queries and add platform/browser coverage according to risk.
9. Profile rendering/list/image/interop hot paths only when the component is performance-sensitive.
