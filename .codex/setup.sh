#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"
python3 --version
python3 ferramentas/portal.py build
python3 ferramentas/portal.py verify-clean
