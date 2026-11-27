---
name: duoready
description: Audit and improve adaptive SwiftUI or UIKit interfaces for changing iOS window sizes and iPhone Duo layouts. Use for foldable or folding iPhone work, reserved regions, arrangement views, vertical controls, scene resizing, and adaptive navigation. Verify every Duo-specific API against the installed SDK before using it.
---

# DuoReady iOS

This skill covers the engineering decisions around a changing iOS window: content sizing, navigation, safe areas, reserved regions, arrangements, vertical controls, media, and multiple scenes. It does not assume that a device-specific API exists merely because a product page or another repository mentions it.

## Operating rule

Treat the app's actual deployment target, installed SDK, source tree, and build output as authoritative. Treat device names, future APIs, measurements, and remembered spellings as unverified until checked. Never invent a simulator run or compilation result.

## Workflow

1. Identify platform targets, minimum OS, orientation policy, scene configuration, SwiftUI/UIKit boundary, navigation containers, and existing size-class or geometry logic.
2. Run `scripts/audit_swiftui.py` and inspect every finding in context. A finding is a prompt for review, not proof of a defect.
3. Prefer resizable system containers, size classes, safe areas, layout margins, Dynamic Type, and content-driven sizing over display-specific constants.
4. Keep navigation outside a two-content arrangement. Use `NavigationSplitView` or `UISplitViewController` for hierarchy; use an arrangement only for the content relationship it owns.
5. For Duo-specific work, run `bash scripts/check_sdk.sh` first. If the SDK does not expose an API, mark it unavailable locally and do not write code that assumes it compiles.
6. Validate compact, regular, wide, short-height, accessibility, keyboard, RTL, split-view, and scene-reconnection states. Record exact Xcode, SDK, runtime, and device/simulator configuration.

Read only the reference needed for the task. Use `references/api-reference.md` for spellings and confidence, `references/arrangement-views.md` for two-pane or layered content, `references/reserved-regions.md` for fold/camera avoidance, `references/vertical-controls.md` for bars, `references/split-views.md` for navigation, `references/camera-and-scenes.md` for media and scene identity, `references/device-and-metrics.md` for measurements, `references/audit-checklist.md` for an existing-app review, and `references/verification.md` plus `references/simulator-verification.md` for validation protocol.

## API confidence labels

- **Verified locally**: found by the SDK check or compiled by the app's build.
- **Apple-documented**: linked in the source register, but not confirmed in this workspace's SDK.
- **Unverified**: inferred or secondary; do not present it as an API contract.

## Review priorities

- Fixed frames, offsets, and screen bounds that decide information hierarchy.
- Manual safe-area or keyboard compensation that duplicates system behavior.
- HStacks/VStacks/ZStacks that represent a two-pane or overlay relationship.
- Toolbars and tab bars that assume horizontal placement or a fixed number of items.
- Camera/media code that assumes one display, one scene, or a fixed camera direction.
- State restoration and scene identity when multiple UI instances can exist.

## Output format

Report observed evidence, risk, smallest adaptive change, APIs and confidence labels, validation performed, and unresolved limitations. Keep speculative behavior separate.
