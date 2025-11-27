import sqlite3
import pytest

DB_FILE = "test.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def test_insert_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name,email) VALUES (?,?)", ("Alice","alice@example.com"))
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE name=?", ("Alice",))
    result = cursor.fetchone()
    assert result is not None
    conn.close()

def test_update_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email=? WHERE name=?", ("bob_new@example.com","Bob"))
    conn.commit()
    cursor.execute("SELECT email FROM users WHERE name=?", ("Bob",))
    result = cursor.fetchone()
    assert result[0] == "bob_new@example.com"
    conn.close()

def test_delete_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name=?", ("Alice",))
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE name=?", ("Alice",))
    result = cursor.fetchone()
    assert result is None
    conn.close()
