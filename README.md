# DuoReady iOS Skill

An AI-agent skill and lightweight static audit toolkit for making iOS interfaces adaptive across compact, regular, and wide layouts.

> **Scope note:** This project focuses on resilient adaptive UI patterns for current SwiftUI and UIKit projects. It does not assume unreleased foldable-iPhone hardware, hinge APIs, or unannounced Apple SDK capabilities.

## What it helps with

- Review SwiftUI and UIKit layouts for hard-coded sizing and positioning.
- Identify layout patterns that may break when available space changes.
- Recommend adaptive composition, readable content widths, and robust navigation.
- Check safe-area, keyboard, Dynamic Type, and accessibility considerations.
- Run a fast, dependency-free source scan to highlight patterns worth reviewing.

## Quick start

Run the static heuristic scanner with Python 3.9+:

```bash
python3 skills/duoready/scripts/audit_swiftui.py /path/to/YourApp
```

The scanner reports candidate issues with file paths and line numbers. It is a review aid, **not** a Swift compiler, UI test, or proof that a layout is broken.

## Repository map

- `skills/duoready/SKILL.md` — instructions for an AI coding agent.
- `skills/duoready/references/adaptive-layout.md` — adaptive layout guidance and examples.
- `skills/duoready/scripts/audit_swiftui.py` — standard-library source scanner.
- `docs/validation-checklist.md` — manual and simulator validation checklist.
- `examples/AdaptiveLayoutExample.swift` — small SwiftUI example.

## Suggested workflow

1. Inspect the app's deployment target, supported devices, navigation model, and design system.
2. Run the scanner and review each finding in context.
3. Refactor fixed assumptions into adaptive layout decisions.
4. Validate compact, regular, and wide available sizes, including short-height and accessibility cases.
5. Record device/simulator configuration and any remaining limitations.

## Compatibility

The guidance uses established SwiftUI and UIKit concepts. Confirm API availability against your app's deployment target and the current Apple documentation before adopting an API.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
