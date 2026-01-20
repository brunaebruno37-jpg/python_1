# Copilot / AI agent instructions for this repo

## ⚡ Quick context
- This repository is a set of Python lesson/exercise scripts (files named `aula*.py`) and small example modules under `dados/` and `aula99_package/`.
- Primary language is **Portuguese** (variable names, strings and user-facing text are in Portuguese).

## 🔧 How to run / debug
- Run individual lessons manually: `python aula36.py` (Windows PowerShell or terminal).
- Many files are interactive (use `input()`); do not break interactive behavior unless you provide a non-interactive variant or guard via `if __name__ == "__main__"`.
- Debug by running a single file and using `print()`s, or import functions into a small local test script to exercise behavior without interaction.

## 🗂 Project layout & patterns to follow
- `aulaNN.py` — independent lesson scripts; often self-contained and executable.
- `dados/` — small data modules; `dados/__init__.py` exports `produtos` from `dados/produtos_modulo.py`. Prefer `from dados import produtos` when referencing dataset.
- `aula99_package/` — example package skeleton (currently `modulo.py` is empty).
- Naming conventions: **snake_case** for variables and functions, file names keep `aula` + number pattern, and texts are in Portuguese (preserve this).
- Typical libs: standard library only (examples show using `itertools.groupby`). Avoid adding heavy new dependencies without approval.

## ✅ Safe edit rules for AI agents
- Preserve original interactive behavior of lessons. If you refactor to enable testing, add a non-interactive wrapper or parameterized function and keep the original script behavior.
- Add `if __name__ == "__main__"` guards for runnable examples so they are safe to import from tests.
- When adding tests, create a `tests/` dir and use `pytest` (recommended) with files named `test_*.py`.
  - For code that calls `input()`, either refactor to accept parameters or use `monkeypatch` to mock `input()` in tests.
- Keep all user-facing messages and comments in Portuguese to match repo tone.

## ⚠️ Repository quirks & known issues
- There is a file named `aula5..py` (double dot) — avoid creating similarly malformed filenames.
- `aula99_package/modulo.py` is empty — review before using as a package example.
- There is no test framework or CI configured; adding tests or CI should be discussed in PRs.

## ✍️ Examples (reference in repo)
- Data import: `from dados import produtos  # produtos is defined in dados/produtos_modulo.py`
- Typical guard pattern to add when making functions importable:

```python
# in aula36.py
def zipper(lista1, lista2):
    ...

if __name__ == "__main__":
    print(zipper([...], [...]))
```

## What to ask the maintainer in PRs
- Preferred test framework (pytest vs unittest).
- Whether we should convert interactive lessons to parameterized functions or leave them as-is.

---
If anything here is incomplete or you want different conventions (e.g., English messages or a testing policy), please tell me and I will update this file.