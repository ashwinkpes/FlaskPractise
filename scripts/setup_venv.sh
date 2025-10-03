#!/usr/bin/env bash
# Creates a Python virtual environment in .venv, activates it, upgrades pip,
# and installs packages from requirements.txt.

set -euo pipefail

echo "Creating virtual environment in .venv..."
python3 -m venv .venv

echo "Activating .venv for this shell..."
source .venv/bin/activate

echo "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Virtual environment ready. Activate it with: source .venv/bin/activate"
