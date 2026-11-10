# Week 12 — Bandit Security Triage Log

| Bandit ID | File | Severity | Decision |
|---|---|---|---|
| B324 | accounts.py | High | Fix |
| B602 | exporter.py | High | Fix |
| B608 | accounts.py | Medium | Fix |
| B301 | importer.py | Medium | Fix |
| B307 | importer.py | Medium | Fix |
| B105 | accounts.py | Low | Fix |
| B404 | exporter.py | Low | Review / Justify |
| B403 | importer.py | Low | Review / Justify |

## Triage Notes

For each finding, document:
- Whether untrusted input can reach the vulnerable code.
- The potential security impact.
- The fix or justification.
- The Git commit or test demonstrating the resolution.

## Before and After Results

Before: 2 High, 3 Medium, 3 Low.

After: To be completed following remediation.

## Remaining Low-Severity Findings

### B404 — Subprocess Import
- File: exporter.py
- Reachability: The subprocess module is imported by application code. The import itself does not execute user input.
- Worst case: Unsafe use of subprocess could enable command execution.
- Decision: Accept with justification.
- Justification: The implementation uses a subprocess argument list without shell=True. The import alone does not create a command injection vulnerability.
- Evidence: test_exporter_uses_safe_argument_list; commit 496894b.

### B607 — Partial Executable Path
- File: exporter.py
- Reachability: The application invokes zip using the executable name rather than an absolute path.
- Worst case: An attacker who controls the process PATH could substitute a malicious executable.
- Decision: Accept with justification for this lab.
- Justification: The lab assumes a controlled execution environment with a trusted PATH. A production implementation should resolve and use a trusted executable path.
- Evidence: Bandit after.txt; exporter security tests.

### B603 — Subprocess Execution Without Shell
- File: exporter.py
- Reachability: A user-supplied filename reaches the subprocess argument list.
- Worst case: Unsafe filename or executable handling could cause unintended behavior.
- Decision: Accept with justification for this lab.
- Justification: The implementation uses a list of arguments, does not enable shell=True, and inserts -- before the filename to prevent option interpretation. This reduces command injection risk but does not replace production filename and path validation.
- Evidence: test_exporter_uses_safe_argument_list; commit 496894b.

## Bandit Scan Comparison

| Severity | Before | After |
|---|---:|---:|
| High | 2 | 0 |
| Medium | 3 | 0 |
| Low | 3 | 3 |

All High and Medium findings have been remediated. The remaining Low findings have documented risk assessments and justifications.
