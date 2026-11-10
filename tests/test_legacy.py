"""Characterization tests: they pin today's behavior so fixes don't break it."""
import sqlite3

import pytest

from tdd_lab.accounts import add_user, check_login, find_user, init_db
from tdd_lab.prompt_guard import SYSTEM_PROMPT, build_prompt


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    init_db(connection)
    yield connection
    connection.close()


def test_login_succeeds_with_correct_password(conn):
    add_user(conn, "ada", "s3cret!")
    assert check_login(conn, "ada", "s3cret!") is True


def test_login_fails_with_wrong_password(conn):
    add_user(conn, "ada", "s3cret!")
    assert check_login(conn, "ada", "nope") is False


def test_find_user_returns_none_for_unknown_name(conn):
    assert find_user(conn, "ghost") is None


def test_prompt_contains_system_prompt_and_question():
    prompt = build_prompt("When does registration open?")
    assert SYSTEM_PROMPT in prompt
    assert "When does registration open?" in prompt
def test_find_user_rejects_sql_injection(conn):
    # Create a legitimate user first.
    add_user(conn, "ada", "s3cret!")

    # An SQL injection attempt should not match that user.
    malicious_name = "x' OR '1'='1"

    assert find_user(conn, malicious_name) is None