#!/usr/bin/env python3
"""Validate the shape of DuoReady evaluation cases without grading model quality."""
import json
import pathlib
import sys

required = {"id", "prompt", "checks"}
path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).with_name("evals.json"))
cases = json.loads(path.read_text(encoding="utf-8"))
if not isinstance(cases, list) or not cases:
    raise SystemExit("evaluation file must contain a non-empty list")
for case in cases:
    missing = required - set(case)
    if missing or not isinstance(case["checks"], list) or not case["checks"]:
        raise SystemExit(f"invalid case: {case.get('id', '<unknown>')} missing={sorted(missing)}")
print(f"Validated {len(cases)} evaluation cases; no model score was produced.")
