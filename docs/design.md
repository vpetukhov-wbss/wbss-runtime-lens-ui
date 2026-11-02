# Product design and handoff

[Figma file](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea) · [Overview](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-1852) · [Trace detail](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2510) · [Onboarding](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3599)

Three pages: Foundations, Observability, Extensions. There are 13 core screens and 3 optional extension previews, all editable Figma layers. Core prototype navigation and investigation actions link within the Observability page. Extension pages are accessed from the Figma page list; cross-page navigation is not claimed as a working prototype flow.

| Screen | Figma | Scope |
|---|---|---|
| Overview | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-1852) | Core |
| Applications | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2042) | Core |
| Requests | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2198) | Core |
| Traces | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2365) | Core |
| Trace Detail | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2510) | Core |
| Logs | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2639) | Core |
| Errors | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2761) | Core |
| Metrics | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-2902) | Core |
| Jobs | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3057) | Core |
| Releases | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3200) | Core |
| Alerts | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3340) | Core |
| Settings | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3477) | Core |
| Onboarding | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=3-3599) | Core |
| Database Lens | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=4-6) | Optional extension |
| Dependencies | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=4-137) | Optional extension |
| Profiling | [Open screen](https://www.figma.com/design/mz9wNAmqfnkcYxusIHWnea?node-id=4-284) | Optional extension |

## Proposed UI foundation

Angular + Nebular + Apache ECharts. Nebular is the working recommendation, not a user-confirmed library choice. The user also proposed Allianz Aquila; confirm the choice before committing to runtime package dependencies. Material was the initial proposal and is superseded as the preferred direction. Nebular's repository declares minimal maintenance; evaluate version compatibility during bootstrap and keep application code independent of theme-specific models.

Open Sans is the UI font; Roboto Mono is used for SQL, trace identifiers and logs. The Figma palette is a custom WBSS theme intended to map to Nebular tokens; it is not an imported or certified Nebular Figma kit. There are no Code Connect files in the initial repositories and no matching Nebular assets in the available team library; local reusable components were created for buttons, navigation and statuses.

The file contains primitive palette values, semantic Dark/Light modes, layout variables, seven text styles and 12 component variants. Current review screens are dark mode; light mode tokens exist but a light-mode screen has not been visually validated. Responsive layouts and full keyboard/accessibility behavior are implementation tasks.

## Design requirements

- Preserve project/application/environment/time context across overview → operation → trace → logs/error.
- Use explicit status labels alongside colors; retain table sorting, selected row and active filter state.
- Separate core navigation from optional modules; hide unavailable modules or explain activation without blocking onboarding.
- Server-side data filtering, pagination and series downsampling. Virtualize large log/result lists.
- Provide loading, empty, no permission, time-window-no-data, API unavailable, rate-limited and partial telemetry states.
- Waterfall and profiling visualizations require purpose-built components. Standard chart/timeline widgets are not complete substitutes.
- All charts, counts, keys and profiles in this design are examples. No real production data or credentials are included.

## Validation completed

Structural evidence recorded editable text/vector layers, reusable instances, no full-UI raster fills and expected font families. All screen content fits the 1600×1080 review viewport after density adjustments. Overview, trace detail, onboarding and profiling received full-size visual review. Remaining views received structural validation; detailed interactive behavior is not implemented.

The Figma file is hosted in the connected 2VDevelopers plan. No public-sharing permission was changed; a public repository link does not grant access to the design file.
