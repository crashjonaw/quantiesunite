"""
Progress tracking — topic completion, quiz scores, targets.
"""

from datetime import datetime
from db.core import get_db


def get_progress(user_id):
    db = get_db()
    rows = db.execute("SELECT * FROM user_progress WHERE user_id=?",
                      (user_id,)).fetchall()
    db.close()
    result = {}
    for r in rows:
        result[r["topic_id"]] = {
            "complete": bool(r["complete"]),
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


def add_target(user_id, topic_id):
    db = get_db()
    try:
        db.execute("INSERT INTO user_targets (user_id, topic_id) VALUES (?,?)",
                   (user_id, topic_id))
        db.commit()
    except Exception:
        pass
    finally:
        db.close()


def remove_target(user_id, topic_id):
    db = get_db()
    db.execute("DELETE FROM user_targets WHERE user_id=? AND topic_id=?",
               (user_id, topic_id))
    db.commit()
    db.close()


def get_targets(user_id):
    db = get_db()
    rows = db.execute(
        "SELECT topic_id FROM user_targets WHERE user_id=? ORDER BY added_at",
        (user_id,)).fetchall()
    db.close()
    return [r["topic_id"] for r in rows]


def get_user_full_progress(user_id):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_progress WHERE user_id=? ORDER BY topic_id",
        (user_id,)).fetchall()
    db.close()
    return [dict(r) for r in rows]
