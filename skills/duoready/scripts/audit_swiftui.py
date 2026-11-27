#!/usr/bin/env python3
"""Heuristic audit for layout assumptions in Swift/SwiftUI/UIKit sources."""
from __future__ import annotations
import argparse
import pathlib
import re
import sys

RULES = (
    ("fixed-frame", re.compile(r"\.frame\s*\([^\n]*(?:width:|height:)"), "Review fixed frame."),
    ("screen-bounds", re.compile(r"UIScreen\.main\.bounds|UIScreen\.main\.nativeBounds"), "Avoid screen bounds for window layout."),
    ("hard-coded-offset", re.compile(r"\.offset\s*\([^\n]*(?:x:|y:)|\.position\s*\("), "Review manual positioning across size classes."),
    ("manual-safe-area", re.compile(r"safeAreaInsets|additionalSafeAreaInsets"), "Confirm this is not duplicating system safe-area handling."),
    ("magic-spacing", re.compile(r"\.padding\s*\(\s*\d{2,}|\.spacing\s*:\s*\d{2,}"), "Review large fixed spacing."),
)

def scan(root: pathlib.Path):
    for path in sorted(root.rglob("*")):
        if path.suffix not in {".swift", ".m", ".mm"} or any(part in {".git", "Pods", "DerivedData"} for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            for rule, pattern, advice in RULES:
                if pattern.search(line):
                    yield {"rule": rule, "path": str(path), "line": number, "advice": advice}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path)
    args = parser.parse_args()
    if not args.root.exists():
        parser.error(f"not found: {args.root}")
    findings = list(scan(args.root))
    for item in findings:
        print(f"{item['path']}:{item['line']} [{item['rule']}] {item['advice']}")
    print(f"Findings: {len(findings)} (heuristic; review in context)", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
