
"""Account helpers with secure password hashing and SQL queries."""

import hashlib
import hmac
import os
import sqlite3

SECRET_KEY = os.environ.get("APP_SECRET_KEY", "")


def hash_password(password: str) -> str:
    """Hash a password with a random salt using PBKDF2-HMAC-SHA256."""
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600_000,
    )
    return salt.hex() + "$" + digest.hex()


def verify_password(password: str, stored: str) -> bool:
    """Verify a password against its stored salted hash."""
    try:
        salt_hex, digest_hex = stored.split("$")
        salt = bytes.fromhex(salt_hex)
        expected_digest = bytes.fromhex(digest_hex)
    except (ValueError, AttributeError):
        return False

    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600_000,
    )

    return hmac.compare_digest(digest, expected_digest)


def init_db(conn: sqlite3.Connection) -> None:
    """Initialize the user database."""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT, pw_hash TEXT)"
    )
    conn.commit()


def add_user(
    conn: sqlite3.Connection,
    name: str,
    password: str,
) -> None:
    """Add a user with a salted password hash."""
    conn.execute(
        "INSERT INTO users (name, pw_hash) VALUES (?, ?)",
        (name, hash_password(password)),
    )
    conn.commit()


def find_user(conn: sqlite3.Connection, name: str):
    """Find a user safely using a parameterized SQL query."""
    return conn.execute(
        "SELECT name, pw_hash FROM users WHERE name = ?",
        (name,),
    ).fetchone()


def check_login(
    conn: sqlite3.Connection,
    name: str,
    password: str,
) -> bool:
    """Verify credentials against a stored password hash."""
    row = find_user(conn, name)
    return row is not None and verify_password(password, row[1])
