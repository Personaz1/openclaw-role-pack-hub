#!/usr/bin/env bash
set -euo pipefail
python3 -m rolepackhub.cli --all | tee demo/validate-all.txt
echo "Demo artifact: demo/validate-all.txt"
