"""
User CRUD — create, read, update, delete users and auth.
"""

import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from db.core import get_db


def create_user(username, email, password):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?,?,?)",
            (username.strip(), email.strip().lower(),
             generate_password_hash(password))
        )
        db.commit()
        count = db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
        if count == 1:
            db.execute("UPDATE users SET is_admin=1 WHERE email=?",
                       (email.strip().lower(),))
            db.commit()
        uid = db.execute("SELECT id FROM users WHERE email=?",
                         (email.strip().lower(),)).fetchone()["id"]
        return uid, None
    except sqlite3.IntegrityError as e:
        db.rollback()
        msg = str(e).lower()
        if "username" in msg:
            return None, "Username already taken."
        if "email" in msg:
            return None, "Email is already registered."
        return None, "Registration failed — please try again."
    finally:
        db.close()


def get_user_by_email(email):
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE email=?",
                     (email.strip().lower(),)).fetchone()
    db.close()
    return dict(row) if row else None


def get_user_by_id(uid):
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    db.close()
    return dict(row) if row else None


def get_user_by_username(username):
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE username=?",
                     (username.strip(),)).fetchone()
    db.close()
    return dict(row) if row else None


def verify_credentials(email_or_username, password):
    user = get_user_by_email(email_or_username)
    if not user:
        user = get_user_by_username(email_or_username)
    if user and check_password_hash(user["password_hash"], password):
        return user
    return None


def update_target_level(uid, level):
    db = get_db()
    db.execute("UPDATE users SET target_level=? WHERE id=?", (level, uid))
    db.commit()
    db.close()


def update_username(uid, new_username):
    db = get_db()
    try:
        db.execute("UPDATE users SET username=? WHERE id=?",
                   (new_username.strip(), uid))
        db.commit()
        return None
    except sqlite3.IntegrityError:
        db.rollback()
        return "Username already taken."
    finally:
        db.close()


def update_password(uid, new_password):
    db = get_db()
    db.execute("UPDATE users SET password_hash=? WHERE id=?",
               (generate_password_hash(new_password), uid))
    db.commit()
    db.close()


def all_users():
    db = get_db()
    rows = db.execute("""
        SELECT u.*,
               COUNT(p.id) AS topics_started,
               SUM(CASE WHEN p.complete=1 THEN 1 ELSE 0 END) AS topics_done
        FROM users u
        LEFT JOIN user_progress p ON p.user_id = u.id
        GROUP BY u.id ORDER BY u.created_at DESC
    """).fetchall()
    db.close()
    return [dict(r) for r in rows]


def toggle_admin(uid):
    db = get_db()
    db.execute("UPDATE users SET is_admin = 1 - is_admin WHERE id=?", (uid,))
    db.commit()
    db.close()


def delete_user(uid):
    db = get_db()
    db.execute("DELETE FROM users WHERE id=?", (uid,))
    db.commit()
    db.close()


def site_stats():
    db = get_db()
    stats = {}
    stats["total_users"] = db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
    stats["admin_users"] = db.execute("SELECT COUNT(*) AS c FROM users WHERE is_admin=1").fetchone()["c"]
    stats["total_completions"] = db.execute(
        "SELECT COUNT(*) AS c FROM user_progress WHERE complete=1").fetchone()["c"]
    stats["most_active"] = db.execute("""
        SELECT u.username, COUNT(p.id) AS cnt
        FROM users u LEFT JOIN user_progress p ON p.user_id=u.id AND p.complete=1
        GROUP BY u.id ORDER BY cnt DESC LIMIT 5
    """).fetchall()
    db.close()
    return stats


def ensure_default_admin():
    existing = get_user_by_username("admin")
    if existing:
        if not existing["is_admin"]:
            db = get_db()
            db.execute("UPDATE users SET is_admin=1 WHERE username='admin'")
            db.commit()
            db.close()
        return
    db = get_db()
    try:
        db.execute(
            "INSERT INTO users (username, email, password_hash, is_admin, target_level) "
            "VALUES (?,?,?,1,'Deep Learning Advanced')",
            ("admin", "admin@quantiesunite.local",
             generate_password_hash("123456")))
        db.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        db.close()
