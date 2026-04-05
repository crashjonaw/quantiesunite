"""
Admin analytics — site-wide stats, user growth, top users/topics.
"""

from datetime import date, timedelta
from db.core import get_db
from db.violations import get_flagged_users, get_violations, VIOLATION_TYPES, admin_violation_timeline


def admin_site_overview():
    db = get_db()
    today = date.today().isoformat()
    week_ago = (date.today() - timedelta(days=7)).isoformat()
    month_ago = (date.today() - timedelta(days=30)).isoformat()
    stats = {}
    stats["total_users"] = db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
    stats["users_today"] = db.execute("SELECT COUNT(*) AS c FROM users WHERE DATE(created_at) = ?", (today,)).fetchone()["c"]
    stats["users_this_week"] = db.execute("SELECT COUNT(*) AS c FROM users WHERE DATE(created_at) >= ?", (week_ago,)).fetchone()["c"]
    stats["users_this_month"] = db.execute("SELECT COUNT(*) AS c FROM users WHERE DATE(created_at) >= ?", (month_ago,)).fetchone()["c"]
    stats["dau"] = db.execute("SELECT COUNT(DISTINCT user_id) AS c FROM user_activity WHERE activity_date = ?", (today,)).fetchone()["c"]
    stats["wau"] = db.execute("SELECT COUNT(DISTINCT user_id) AS c FROM user_activity WHERE activity_date >= ?", (week_ago,)).fetchone()["c"]
    stats["mau"] = db.execute("SELECT COUNT(DISTINCT user_id) AS c FROM user_activity WHERE activity_date >= ?", (month_ago,)).fetchone()["c"]
    stats["total_completions"] = db.execute("SELECT COUNT(*) AS c FROM user_progress WHERE complete=1").fetchone()["c"]
    stats["total_quiz_attempts"] = db.execute("SELECT COUNT(*) AS c FROM quiz_attempts").fetchone()["c"]
    stats["total_questions"] = db.execute("SELECT COUNT(*) AS c FROM quiz_questions").fetchone()["c"]
    stats["open_violations"] = db.execute("SELECT COUNT(*) AS c FROM policy_violations WHERE resolved=0").fetchone()["c"]
    stats["critical_violations"] = db.execute("SELECT COUNT(*) AS c FROM policy_violations WHERE resolved=0 AND severity='critical'").fetchone()["c"]
    db.close()
    return stats


def admin_user_growth(days=90):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        "SELECT DATE(created_at) AS reg_date, COUNT(*) AS count FROM users WHERE DATE(created_at) >= ? GROUP BY reg_date ORDER BY reg_date",
        (cutoff,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def admin_daily_active_users(days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        "SELECT activity_date, COUNT(DISTINCT user_id) AS dau FROM user_activity WHERE activity_date >= ? GROUP BY activity_date ORDER BY activity_date",
        (cutoff,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def admin_top_users(limit=10):
    db = get_db()
    rows = db.execute(
        """SELECT a.user_id, u.username, u.email,
                  SUM(a.points) AS total_points, COUNT(*) AS total_events,
                  COUNT(DISTINCT a.activity_date) AS active_days,
                  MAX(a.activity_date) AS last_active
           FROM user_activity a LEFT JOIN users u ON u.id = a.user_id
           GROUP BY a.user_id ORDER BY total_points DESC LIMIT ?""",
        (limit,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def admin_top_topics(limit=15):
    db = get_db()
    rows = db.execute(
        """SELECT p.topic_id,
               SUM(CASE WHEN p.complete=1 THEN 1 ELSE 0 END) AS completions,
               COUNT(DISTINCT p.user_id) AS unique_users,
               (SELECT COUNT(*) FROM quiz_attempts qa WHERE qa.topic_id = p.topic_id) AS quiz_attempts,
               (SELECT ROUND(AVG(qa.score * 100.0 / qa.total), 1) FROM quiz_attempts qa WHERE qa.topic_id = p.topic_id AND qa.total > 0) AS avg_score
           FROM user_progress p GROUP BY p.topic_id ORDER BY completions DESC LIMIT ?""",
        (limit,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def admin_get_full_dashboard():
    return {
        "overview": admin_site_overview(),
        "user_growth": admin_user_growth(),
        "dau_chart": admin_daily_active_users(),
        "top_users": admin_top_users(),
        "top_topics": admin_top_topics(),
        "flagged_users": get_flagged_users(),
        "recent_violations": get_violations(limit=20, unresolved_only=True),
        "violation_timeline": admin_violation_timeline(),
        "violation_types": VIOLATION_TYPES,
    }
