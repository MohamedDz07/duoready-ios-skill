#!/usr/bin/env bash
set -euo pipefail

if ! command -v xcrun >/dev/null 2>&1; then
  echo "UNVERIFIED: xcrun is not available; Swift samples were not type-checked." >&2
  exit 2
fi
swiftc_path="$(xcrun --find swiftc 2>/dev/null || true)"
sdkroot="$(xcrun --sdk iphonesimulator --show-sdk-path 2>/dev/null || true)"
if [[ -z "$swiftc_path" || -z "$sdkroot" ]]; then
  echo "UNVERIFIED: Swift compiler or iPhoneSimulator SDK unavailable." >&2
  exit 2
fi
echo "SDK: $sdkroot"
echo "Type-checking is intentionally opt-in for a named target; no app project is included."
