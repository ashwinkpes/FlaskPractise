<#
Creates a Python virtual environment in `.venv`, activates it for the current
PowerShell session, upgrades pip, and installs packages from requirements.txt.

Usage (PowerShell):
  .\scripts\setup_venv.ps1
#>

param()

Write-Host "Creating virtual environment in .venv..."
python -m venv .venv

Write-Host "Activating .venv for this session..."
& .\.venv\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing requirements..."
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host "Virtual environment ready. To activate later run: . \\.venv\\Scripts\\Activate.ps1"
