
"""Safely import session data and parse discount values."""

import ast
import json


def load_session(blob: bytes):
    """Load JSON session data without executing arbitrary code."""
    return json.loads(blob)


def compute_discount(expression: str):
    """Parse literal values without executing Python expressions."""
    return ast.literal_eval(expression)
