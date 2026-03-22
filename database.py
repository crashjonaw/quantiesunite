"""
QuantiesUnite — Database Layer (SQLite)
BloomBurrow-style: single-file SQLite, no external ORM needed.
"""

import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantiesunite.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            username      TEXT     UNIQUE NOT NULL,
            email         TEXT     UNIQUE NOT NULL,
            password_hash TEXT     NOT NULL,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            target_level  TEXT     DEFAULT 'Deep Learning Advanced',
            plan          TEXT     DEFAULT 'free',
            is_admin      INTEGER  DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS user_progress (
            id           INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER  NOT NULL,
            topic_id     TEXT     NOT NULL,
            complete     INTEGER  DEFAULT 0,
            quiz_score   INTEGER,
            quiz_total   INTEGER,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id)
        );
    """)
    db.commit()
    db.close()


# ── User CRUD ────────────────────────────────────────────────────────────────

def create_user(username, email, password):
    """Create a new user. Returns (user_id, None) or (None, error_str)."""
    db = get_db()
    try:
        db.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?,?,?)",
            (username.strip(), email.strip().lower(),
             generate_password_hash(password))
        )
        db.commit()
        # Make the very first user admin automatically
        count = db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
        if count == 1:
            db.execute(
                "UPDATE users SET is_admin=1 WHERE email=?",
                (email.strip().lower(),)
            )
            db.commit()
        uid = db.execute(
            "SELECT id FROM users WHERE email=?",
            (email.strip().lower(),)
        ).fetchone()["id"]
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
    row = db.execute(
        "SELECT * FROM users WHERE email=?", (email.strip().lower(),)
    ).fetchone()
    db.close()
    return dict(row) if row else None


def get_user_by_id(uid):
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    db.close()
    return dict(row) if row else None


def get_user_by_username(username):
    db = get_db()
    row = db.execute(
        "SELECT * FROM users WHERE username=?", (username.strip(),)
    ).fetchone()
    db.close()
    return dict(row) if row else None


def verify_credentials(email_or_username, password):
    """Accept login by email OR username."""
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
        db.execute("UPDATE users SET username=? WHERE id=?", (new_username.strip(), uid))
        db.commit()
        return None
    except sqlite3.IntegrityError:
        db.rollback()
        return "Username already taken."
    finally:
        db.close()


def update_password(uid, new_password):
    db = get_db()
    db.execute(
        "UPDATE users SET password_hash=? WHERE id=?",
        (generate_password_hash(new_password), uid)
    )
    db.commit()
    db.close()


# ── Admin CRUD ───────────────────────────────────────────────────────────────

def all_users():
    db = get_db()
    rows = db.execute("""
        SELECT
            u.*,
            COUNT(p.id)                                      AS topics_started,
            SUM(CASE WHEN p.complete=1 THEN 1 ELSE 0 END)   AS topics_done
        FROM users u
        LEFT JOIN user_progress p ON p.user_id = u.id
        GROUP BY u.id
        ORDER BY u.created_at DESC
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
    stats["total_users"]    = db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
    stats["admin_users"]    = db.execute("SELECT COUNT(*) AS c FROM users WHERE is_admin=1").fetchone()["c"]
    stats["total_completions"] = db.execute(
        "SELECT COUNT(*) AS c FROM user_progress WHERE complete=1"
    ).fetchone()["c"]
    stats["most_active"] = db.execute("""
        SELECT u.username, COUNT(p.id) AS cnt
        FROM users u
        LEFT JOIN user_progress p ON p.user_id=u.id AND p.complete=1
        GROUP BY u.id ORDER BY cnt DESC LIMIT 5
    """).fetchall()
    db.close()
    return stats


# ── Progress CRUD ─────────────────────────────────────────────────────────────

def get_progress(user_id):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_progress WHERE user_id=?", (user_id,)
    ).fetchall()
    db.close()
    result = {}
    for r in rows:
        result[r["topic_id"]] = {
            "complete":   bool(r["complete"]),
            "quiz_score": r["quiz_score"],
            "quiz_total": r["quiz_total"],
        }
    return result


def mark_topic_complete(user_id, topic_id):
    db = get_db()
    now = datetime.now().isoformat()
    db.execute("""
        INSERT INTO user_progress (user_id, topic_id, complete, completed_at)
        VALUES (?,?,1,?)
        ON CONFLICT(user_id, topic_id)
        DO UPDATE SET complete=1, completed_at=excluded.completed_at
    """, (user_id, topic_id, now))
    db.commit()
    db.close()


def save_quiz_score(user_id, topic_id, score, total):
    db = get_db()
    db.execute("""
        INSERT INTO user_progress (user_id, topic_id, quiz_score, quiz_total)
        VALUES (?,?,?,?)
        ON CONFLICT(user_id, topic_id)
        DO UPDATE SET quiz_score=excluded.quiz_score, quiz_total=excluded.quiz_total
    """, (user_id, topic_id, score, total))
    db.commit()
    db.close()


def reset_progress(user_id):
    db = get_db()
    db.execute("DELETE FROM user_progress WHERE user_id=?", (user_id,))
    db.commit()
    db.close()


def ensure_default_admin():
    """Create the default admin account if it doesn't exist yet."""
    existing = get_user_by_username("admin")
    if existing:
        # Make sure the account is admin
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
             generate_password_hash("123456"))
        )
        db.commit()
    except sqlite3.IntegrityError:
        pass  # Already exists
    finally:
        db.close()


def get_user_full_progress(user_id):
    """Return all progress rows for a single user (for admin view)."""
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_progress WHERE user_id=? ORDER BY topic_id",
        (user_id,)
    ).fetchall()
    db.close()
    return [dict(r) for r in rows]
