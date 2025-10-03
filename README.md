# FlaskPractise

This repository contains a small FastAPI application under the `app/` package
and a simple Flask example at the repository root (`SimpleCalculator.py`).

## Python virtual environment

Create a reproducible Python environment and install dependencies before you run the app. Two helper scripts are provided under `scripts/` to create a venv and install `requirements.txt`.

PowerShell (Windows - recommended for this workspace):

```powershell
# Create the venv (creates `.venv` in the project root) and install requirements
.
scripts\setup_venv.ps1
```

Or run the steps manually in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

POSIX (macOS / Linux):

```bash
./scripts/setup_venv.sh
```

Notes:

- The virtual environment folder is `.venv/` and is ignored by `.gitignore`.
- `requirements.txt` is used to install dependencies. If you add packages, update that file.

## Running the project

FastAPI app (main API):

After creating the venv and installing dependencies, start the FastAPI app using uvicorn from the project root:

PowerShell (after activating the venv):

```powershell
.
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Flask example (`SimpleCalculator.py`):

Run directly with the project venv's Python:

```powershell
.venv\Scripts\python.exe SimpleCalculator.py
```

If you need anything else (add pre-commit, pin deps, or create a pyproject), tell me which you'd prefer and I can add it.
