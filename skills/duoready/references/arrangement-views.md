# Arrangement views

Use an arrangement for two related content views whose relationship changes with available space. A split arrangement is appropriate for peer panes; an overlay arrangement is appropriate for foreground controls over background content.

Keep navigation containers outside the arrangement. Do not place an arrangement inside a scrolling container or use it as a replacement for a navigation split view.

Before implementing, answer:

- What is the single-pane fallback when the secondary content cannot fit?
- What is the minimum readable width of each pane?
- Can both minimums fit in the smallest expected usable region?
- Does the content remain understandable when the device changes pose live?

The API names and modifier placement must be confirmed by `api-reference.md` and the installed SDK. This repository makes no claim that an arrangement sample compiles here.
