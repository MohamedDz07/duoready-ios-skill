#!/usr/bin/env bash
set -euo pipefail

if ! command -v xcrun >/dev/null 2>&1; then
  echo "UNVERIFIED: xcrun is not available; no Apple SDK inspection performed." >&2
  exit 2
fi
sdkroot="$(xcrun --sdk iphoneos --show-sdk-path 2>/dev/null || true)"
if [[ -z "$sdkroot" || ! -d "$sdkroot" ]]; then
  echo "UNVERIFIED: iPhoneOS SDK not available." >&2
  exit 2
fi
echo "SDK: $sdkroot"
for symbol in ArrangementView ReservedRegion UIArrangementViewController ToolbarOverflowMenu; do
  if rg -l --hidden --glob '*.swiftinterface' --glob '*.h' "$symbol" "$sdkroot" >/dev/null 2>&1; then
    echo "FOUND $symbol"
  else
    echo "NOT_FOUND $symbol"
  fi
done
