"""Safely archive reports without invoking a command shell."""

import subprocess


def archive_report(filename: str) -> int:
    """Archive a report using a subprocess argument list."""
    return subprocess.call([
        "zip",
        "-q",
        "archive.zip",
        "--",
        filename,
    ])
