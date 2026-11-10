"""Security tests for the report exporter."""

from unittest.mock import patch

from tdd_lab.exporter import archive_report


def test_exporter_uses_safe_argument_list():
    filename = "report.txt; echo unsafe"

    with patch(
        "tdd_lab.exporter.subprocess.call",
        return_value=0,
    ) as mocked_call:
        result = archive_report(filename)

    args, kwargs = mocked_call.call_args

    assert args[0] == [
        "zip",
        "-q",
        "archive.zip",
        "--",
        filename,
    ]
    assert kwargs.get("shell", False) is False
    assert result == 0
