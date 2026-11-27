# DuoReady iOS Skill

[![Validate](https://github.com/MohamedDz07/duoready-ios-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/MohamedDz07/duoready-ios-skill/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An original Agent Skills-compatible skill for auditing and adapting iOS interfaces to changing display sizes, including iPhone Duo when the app's SDK and deployment target provide the relevant APIs.

This repository is evidence-led. It separates stable SwiftUI/UIKit practices from iPhone Duo APIs that must be confirmed in the installed Xcode SDK. It does not claim hardware measurements, simulator results, compilation, or API availability unless a local check produced them.

## Use it

Read `skills/duoready/SKILL.md` before asking an agent to audit or modify an iOS interface. Run:

```bash
python3 skills/duoready/scripts/audit_swiftui.py path/to/App
```

or use the portable wrapper:

```bash
bash skills/duoready/scripts/audit.sh path/to/App
```

The audit emits review candidates only; it is not a compiler or UI test.

## Install

For Codex:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/MohamedDz07/duoready-ios-skill.git
ln -s "$PWD/duoready-ios-skill/skills/duoready" ~/.agents/skills/duoready
```

For Claude Code, use `~/.claude/skills/duoready/`. For another Agent Skills client, copy `skills/duoready/` into its skills directory.

Then ask: `Audit this iOS app for adaptive layouts and iPhone Duo readiness.`

## Layout

- `skills/duoready/SKILL.md` — agent workflow and guardrails.
- `skills/duoready/references/` — API evidence and adaptive patterns.
- `skills/duoready/scripts/` — static audit and optional SDK surface check.
- `skills/duoready/assets/` — optional DEBUG layout probe.
- `examples/` — small SwiftUI and UIKit patterns.
- `tests/` — standard-library tests and an SDK-gated type-check entry point.
- `evals/` — evaluation prompts and structural grader.

## Evidence boundary

The iPhone Duo guidance is based on Apple's public documentation and Tech Talks, linked in `references/source-register.md`. API names are not treated as locally available until `check_sdk.sh` or an actual Xcode build confirms them.

## Validation

Run the repository checks with Python 3.9 or newer:

```bash
python3 -m unittest discover -s tests -p 'test*.py' -v
bash skills/duoready/scripts/check_sdk.sh
bash tests/typecheck.sh
```

The SDK check returns status `2` when Xcode or an iPhoneOS SDK is unavailable. That means “not verified”, not “the API is absent”. See `docs/validation-checklist.md` before claiming simulator or device validation.

## Contributing

See `CONTRIBUTING.md`. Keep Apple API claims linked to primary documentation and label anything not verified by the installed SDK or a reproducible build.

## License

MIT — see `LICENSE`.
