#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 PROJECT_OR_SOURCE_DIRECTORY" >&2
  exit 64
fi

script_dir="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$script_dir/audit_swiftui.py" "$1"
