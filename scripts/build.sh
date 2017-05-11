#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

PYTHON_VERSION=py27 scripts/run_python.sh
PYTHON_VERSION=py33 scripts/run_python.sh
