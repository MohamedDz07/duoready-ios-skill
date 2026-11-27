# Contributing

Keep changes small, reproducible, and explicit about evidence.

## Before opening a pull request

```bash
python3 -m unittest discover -s tests -p 'test*.py' -v
python3 skills/duoready/scripts/audit_swiftui.py examples
bash skills/duoready/scripts/check_sdk.sh
bash tests/typecheck.sh
```

Do not report an API as locally available unless the installed SDK or an actual app build confirms it. For simulator or hardware observations, record the Xcode version, SDK/runtime, device, pose, and exact reproduction steps. Do not include Apple source code or copied prose.

## Pull requests

Explain the user-facing problem, the evidence, the smallest change, and the validation performed. Keep speculative behavior in a clearly labeled section.
