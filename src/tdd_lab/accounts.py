"""Legacy account helpers -- INTENTIONALLY INSECURE. Your job: scan, triage, fix.

Every weakness below is something a real static-analysis tool will flag.
"""
import hashlib
import sqlite3

SECRET_KEY = "campus-secret-123"  # hard-coded credential


def hash_password(password: str) -> str:
    # Weak, fast hash -- unsuitable for passwords.
    return hashlib.md5(password.encode()).hexdigest()


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pw_hash TEXT)")
    conn.commit()


def add_user(conn: sqlite3.Connection, name: str, password: str) -> None:
    conn.execute(
        "INSERT INTO users (name, pw_hash) VALUES (?, ?)",
        (name, hash_password(password)),
    )
    conn.commit()


def find_user(conn: sqlite3.Connection, name: str):
    # String-built SQL: attacker-controlled input becomes part of the query.
    query = "SELECT name, pw_hash FROM users WHERE name = '%s'" % name
    return conn.execute(query).fetchone()


def check_login(conn: sqlite3.Connection, name: str, password: str) -> bool:
    row = find_user(conn, name)
    return row is not None and row[1] == hash_password(password)
