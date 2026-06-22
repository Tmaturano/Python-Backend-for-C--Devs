# Lesson 6 - Virtual Environments, Packages, pip and Project Structure

## Overview

This lesson is critical because the Python ecosystem works very differently from .NET.

When .NET developers start Python, they usually struggle with:

- Virtual environments
- Package management
- Project structure
- Dependency isolation

After this lesson, you'll understand how professional Python projects are organized.

---

## The Problem: Version Conflicts

Imagine:
- **Project A** needs FastAPI 0.120
- **Project B** needs FastAPI 0.115

If everything is installed globally using `pip install FastAPI`, you'll quickly have version conflicts.

**Virtual environments** solve this by isolating dependencies per project.
- Equivalent to the `packages/` folder in .NET
- Very similar to `bin/` and `obj/` folders in .NET

## Creating a Virtual Environment

Inside your project folder:

```bash
python -m venv .venv
```

This creates the following structure:

```
project/
├── .venv/
├── src/
└── tests/
```

## Activating a Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\activate
```

You should see `(.venv)` at the beginning of your terminal prompt.

## Installing Packages

Once your virtual environment is activated:

```bash
pip install requests
```

This is equivalent to in .NET:

```bash
dotnet add package
```

## Checking Installed Packages

```bash
pip list
```

Example output:
```
requests
urllib3
certifi
```

## Dependency File: requirements.txt

Traditional Python projects use `requirements.txt` to track dependencies.

**Generate a requirements.txt file:**

```bash
pip freeze > requirements.txt
```

**Example requirements.txt:**

```text
fastapi==0.120.0
sqlalchemy==2.0.45
pytest==8.4.0
```

## Restoring Dependencies

```bash
pip install -r requirements.txt
```

Equivalent to in .NET:

```bash
dotnet restore
```

## Modern Python Packaging: uv

Many teams are moving away from `requirements.txt` and adopting **uv**, a fast Python package installer and project manager developed by Astral.

### Why uv?

- **Much faster** than pip
- **Handles virtual environments** automatically
- **Handles dependency resolution** efficiently
- **Becoming the default recommendation** in the Python community

### Install uv

**Windows:**

```powershell
winget install astral-sh.uv
```

**Verify installation:**

```bash
uv --version
```

## Creating a New Project with uv

```bash
uv init football-api
```

Creates the following structure:

```
football-api/
├── pyproject.toml
├── .python-version
└── main.py
```

## Understanding pyproject.toml

Think of `pyproject.toml` as a combination of:
- `.csproj` files
- `Directory.Build.props`
- NuGet package references

**Example pyproject.toml (TOML format):**

```toml
[project]
name = "football-api"
version = "0.1.0"

dependencies = [
  "fastapi",
  "sqlalchemy"
]
```

## Recommendation

**For Learning:**
- Use `python -m venv .venv`
- Use `pip` for package management

**Once Comfortable:**
- Transition to `uv` for better performance and tooling

## Project Structure Examples

### Small Projects

```
project/
├── main.py
├── requirements.txt
└── .venv/
```

### Professional API Structure

This is what we'll use in more advanced modules:

```
football-api/
├── src/
│   ├── api/
│   ├── application/
│   └── domain/
├── tests/
├── pyproject.toml
├── .python-version
└── .venv/
```
