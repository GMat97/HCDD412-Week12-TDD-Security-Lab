# HCDD 412 - Week 12 Starter: TDD + Security Scan Lab

Python 3.10+ . pytest . flake8 . Bandit . (optional) CodeQL. Runs fully local.

## Setup
```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                            # expect 1 RED test (promo) + 4 green
```

## What is in here
| Path | Purpose |
|---|---|
| `src/tdd_lab/promo.py` | Stub for the feature you build with Red-Green-Refactor (rules in the docstring) |
| `tests/test_promo.py` | Your TDD workspace - starts with one deliberately failing test |
| `tests/test_legacy.py` | Characterization tests that protect legacy behavior while you fix it |
| `src/tdd_lab/accounts.py`, `exporter.py`, `importer.py` | Intentionally insecure legacy code to scan and remediate |
| `src/tdd_lab/prompt_guard.py` | Naive LLM prompt builder to test for prompt injection |
| `.github/workflows/ci.yml` | `test` job (lint + coverage) and `security` job (Bandit, fails on High) |
| `.github/workflows/codeql.yml` | Optional CodeQL (public repos only) |

## Commands
```
pytest --cov --cov-report=term-missing   # tests + coverage
flake8 src tests                          # lint
bandit -r src                  # full scan (all severities)
bandit -r src --severity-level high   # the CI gate
```

## Rules of the lab
1. The `security` CI job is **expected to be red** at first. Your goal is no unaddressed High/Critical findings by the deadline.
2. Never "fix" a finding by deleting its test or adding `# nosec` without a written justification.
3. Disclose all AI use (prompts + what you changed) in your submission.
