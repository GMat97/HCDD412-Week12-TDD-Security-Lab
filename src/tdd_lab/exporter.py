"""Legacy report exporter -- INTENTIONALLY INSECURE."""
import subprocess


def archive_report(filename: str) -> int:
    """Zip a report file. ``filename`` comes straight from a web form."""
    return subprocess.call("zip -q archive.zip " + filename, shell=True)
