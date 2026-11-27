# API reference and confidence

This is a verification index, not a substitute for the installed SDK. Each item must be checked against the app's deployment target and Xcode interfaces.

| Area | Apple-documented names to verify | Local status |
|---|---|---|
| SwiftUI arrangements | `ArrangementView`, arrangement styles, pane sizing modifiers | Apple-documented; not locally verified in this workspace |
| UIKit arrangements | `UIArrangementViewController` and related arrangement types | Apple-documented; not locally verified |
| Reserved regions | SwiftUI `ReservedRegion` queries; UIKit reserved-region equivalents | Apple-documented; not locally verified |
| Navigation | `NavigationSplitView`, `UISplitViewController` | Established APIs; deployment target still matters |
| Vertical controls | SwiftUI toolbar visibility/compression APIs and UIKit bar equivalents | Apple-documented; verify exact spellings locally |
| Scenes | `UIScene`, scene sessions, window-scene geometry | Established APIs; verify app lifecycle integration |

Do not infer an API's module, availability, enum case, or runtime behavior from a symbol name. `check_sdk.sh` is a presence check only; compilation is the stronger test.
