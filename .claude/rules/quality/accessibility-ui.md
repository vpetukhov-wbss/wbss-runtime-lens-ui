---
paths:
  - "**/*.{html,razor,tsx,jsx,css,scss,xaml}"
---

# UI and accessibility

- Use semantic native controls before ARIA or custom widgets.
- Every interactive element must be reachable and operable by keyboard with a visible focus indicator.
- Provide programmatic labels, names, roles, states, instructions, and accessible validation errors.
- Manage focus deliberately for navigation, dialogs, async errors, added/removed content, and restored views.
- Announce important dynamic status without excessive screen-reader noise.
- Meet WCAG AA contrast, target size, zoom/reflow, and text-spacing expectations.
- Respect reduced motion, color-scheme, platform font scaling, safe areas, and device orientation where applicable.
- Do not rely on color, hover, placeholder text, or icons alone to communicate meaning.
- Provide loading, empty, partial, error, offline, retry, and permission-denied states.
- Prevent layout shift and content jumps; reserve space for predictable asynchronous media/content.
- Use responsive constraints and content-driven breakpoints; test long translations and large text.
- Automated accessibility checks are necessary but do not replace keyboard and screen-reader-oriented review.
