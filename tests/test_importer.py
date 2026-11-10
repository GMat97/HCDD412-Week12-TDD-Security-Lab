
"""Security tests for data import and expression handling."""

import pytest

from tdd_lab.importer import compute_discount, load_session


def test_load_session_accepts_json():
    # Session data should use JSON instead of pickle.
    blob = b'{"user": "ada", "active": true}'

    result = load_session(blob)

    assert result == {"user": "ada", "active": True}


def test_compute_discount_rejects_expressions():
    # Arithmetic expressions should not be evaluated as Python code.
    with pytest.raises((ValueError, SyntaxError)):
        compute_discount("1 + 1")


def test_compute_discount_accepts_number():
    # Simple numeric literals should still work.
    assert compute_discount("15") == 15
