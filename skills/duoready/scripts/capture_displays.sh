#!/usr/bin/env bash
set -euo pipefail

if ! command -v xcrun >/dev/null 2>&1; then
  echo "UNVERIFIED: xcrun is not available." >&2
  exit 2
fi

device_id="${1:-}"
output_dir="${2:-./duoready-captures}"
if [[ -z "$device_id" ]]; then
  echo "Usage: $0 DEVICE_UDID [OUTPUT_DIR]" >&2
  exit 64
fi
mkdir -p "$output_dir"
xcrun simctl io "$device_id" screenshot "$output_dir/display.png"
echo "Captured one simulator screenshot at $output_dir/display.png"
echo "If the runtime exposes multiple displays, verify which display was captured before interpreting it."
