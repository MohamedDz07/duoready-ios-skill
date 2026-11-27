# Vertical controls

On a wide-and-short display, system toolbars, tab bars, and navigation controls may move to a vertical edge. Prefer standard navigation and toolbar containers so the system can adapt placement and overflow.

- Give actions both a user-facing title and a symbol where the API supports both.
- Group related actions with system groups rather than manual spacer views.
- Prioritize frequent actions and preserve the same functionality in every pose.
- Keep custom controls aware of asymmetric safe areas and the current toolbar edge.
- Avoid assuming a toolbar is horizontal or that a fixed number of items is visible.

Verify the exact vertical-bar APIs and their deployment availability locally; this guide intentionally avoids treating names from another SDK as guaranteed.
