"""
User profiles, activity tracking, streaks, achievements, study sessions,
and dashboard aggregation.
"""

import json
import sqlite3
from datetime import datetime, timedelta, date
from db.core import get_db


# ══════════════════════════════════════════════════════════════════
# PROFILES
# ══════════════════════════════════════════════════════════════════

def ensure_profile(user_id):
    db = get_db()
    db.execute("INSERT OR IGNORE INTO user_profiles (user_id) VALUES (?)", (user_id,))
    db.commit()
    db.close()


def get_profile(user_id):
    ensure_profile(user_id)
    db = get_db()
    row = db.execute("SELECT * FROM user_profiles WHERE user_id=?", (user_id,)).fetchone()
    db.close()
    profile = dict(row) if row else {}
    if profile.get("preferences"):
        try:
            profile["preferences"] = json.loads(profile["preferences"])
        except (json.JSONDecodeError, TypeError):
            profile["preferences"] = {}
    return profile


def update_profile(user_id, **fields):
    allowed = {"display_name", "bio", "avatar_url", "school", "grade",
               "birth_year", "timezone", "preferences"}
    updates = {k: v for k, v in fields.items() if k in allowed}
    if not updates:
        return
    if "preferences" in updates and isinstance(updates["preferences"], dict):
        updates["preferences"] = json.dumps(updates["preferences"])
    ensure_profile(user_id)
    db = get_db()
    set_clause = ", ".join(f"{k}=?" for k in updates)
    values = list(updates.values()) + [datetime.now().isoformat(), user_id]
    db.execute(f"UPDATE user_profiles SET {set_clause}, updated_at=? WHERE user_id=?", values)
    db.commit()
    db.close()


# ══════════════════════════════════════════════════════════════════
# ACTIVITY TRACKING
# ══════════════════════════════════════════════════════════════════

def log_activity(user_id, activity_type, topic_id=None, detail="", points=1):
    today = date.today().isoformat()
    db = get_db()
    db.execute(
        """INSERT INTO user_activity (user_id, activity_date, activity_type, topic_id, detail, points)
           VALUES (?,?,?,?,?,?)""",
        (user_id, today, activity_type, topic_id, detail, points))
    db.commit()
    db.close()
    _update_streak(user_id, today)


def get_activity_heatmap(user_id, days=365):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        """SELECT activity_date, COUNT(*) as count, SUM(points) as points
           FROM user_activity WHERE user_id=? AND activity_date >= ?
           GROUP BY activity_date ORDER BY activity_date""",
        (user_id, cutoff)).fetchall()
    db.close()
    return [{"date": r["activity_date"], "count": r["count"], "points": r["points"]} for r in rows]


def get_recent_activity(user_id, limit=20):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_activity WHERE user_id=? ORDER BY created_at DESC LIMIT ?",
        (user_id, limit)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_activity_summary(user_id, days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    row = db.execute(
        """SELECT COUNT(*) AS total_events, COUNT(DISTINCT activity_date) AS active_days,
               SUM(points) AS total_points,
               SUM(CASE WHEN activity_type='quiz_pass' THEN 1 ELSE 0 END) AS quizzes_passed,
               SUM(CASE WHEN activity_type='quiz_attempt' THEN 1 ELSE 0 END) AS quizzes_taken,
               SUM(CASE WHEN activity_type='topic_complete' THEN 1 ELSE 0 END) AS topics_completed,
               SUM(CASE WHEN activity_type='lesson_view' THEN 1 ELSE 0 END) AS lessons_viewed
           FROM user_activity WHERE user_id=? AND activity_date >= ?""",
        (user_id, cutoff)).fetchone()
    db.close()
    return dict(row) if row else {}


def get_weekly_activity(user_id, weeks=12):
    cutoff = (date.today() - timedelta(weeks=weeks)).isoformat()
    db = get_db()
    rows = db.execute(
        """SELECT strftime('%%Y-W%%W', activity_date) AS week,
               COUNT(*) AS count, SUM(points) AS points,
               COUNT(DISTINCT activity_date) AS active_days
           FROM user_activity WHERE user_id=? AND activity_date >= ?
           GROUP BY week ORDER BY week""",
        (user_id, cutoff)).fetchall()
    db.close()
    return [dict(r) for r in rows]


# ══════════════════════════════════════════════════════════════════
# STREAKS
# ══════════════════════════════════════════════════════════════════

def _update_streak(user_id, today_str):
    today = date.fromisoformat(today_str)
    db = get_db()
    row = db.execute("SELECT * FROM user_streaks WHERE user_id=?", (user_id,)).fetchone()
    if not row:
        db.execute(
            """INSERT INTO user_streaks
               (user_id, current_streak, longest_streak, last_active_date, total_active_days)
               VALUES (?,1,1,?,1)""", (user_id, today_str))
    else:
        last_active = date.fromisoformat(row["last_active_date"]) if row["last_active_date"] else None
        current, longest, total = row["current_streak"] or 0, row["longest_streak"] or 0, row["total_active_days"] or 0
        if last_active == today:
            db.close()
            return
        current = (current + 1) if (last_active and (today - last_active).days == 1) else 1
        longest = max(longest, current)
        total += 1
        db.execute(
            """UPDATE user_streaks SET current_streak=?, longest_streak=?, last_active_date=?, total_active_days=?
               WHERE user_id=?""", (current, longest, today_str, total, user_id))
    db.commit()
    db.close()


def get_streak(user_id):
    db = get_db()
    row = db.execute("SELECT * FROM user_streaks WHERE user_id=?", (user_id,)).fetchone()
    db.close()
    if not row:
        return {"current_streak": 0, "longest_streak": 0, "last_active_date": None, "total_active_days": 0}
    return dict(row)


# ══════════════════════════════════════════════════════════════════
# ACHIEVEMENTS
# ══════════════════════════════════════════════════════════════════

ACHIEVEMENTS = {
    "first_login":        {"name": "Welcome!",           "emoji": "👋", "desc": "Logged in for the first time"},
    "first_quiz":         {"name": "Quiz Taker",         "emoji": "📝", "desc": "Completed your first quiz"},
    "first_pass":         {"name": "Passing Grade",      "emoji": "✅", "desc": "Passed a quiz for the first time"},
    "first_perfect":      {"name": "Perfect Score",      "emoji": "💯", "desc": "Scored 100% on a quiz"},
    "streak_3":           {"name": "3-Day Streak",       "emoji": "🔥", "desc": "Active for 3 consecutive days"},
    "streak_7":           {"name": "Week Warrior",       "emoji": "⚡", "desc": "Active for 7 consecutive days"},
    "streak_30":          {"name": "Monthly Master",     "emoji": "🌟", "desc": "Active for 30 consecutive days"},
    "topics_5":           {"name": "Getting Started",    "emoji": "🚀", "desc": "Completed 5 topics"},
    "topics_10":          {"name": "Dedicated Learner",  "emoji": "📚", "desc": "Completed 10 topics"},
    "topics_25":          {"name": "Knowledge Seeker",   "emoji": "🧠", "desc": "Completed 25 topics"},
    "topics_50":          {"name": "Scholar",            "emoji": "🎓", "desc": "Completed 50 topics"},
    "quizzes_10":         {"name": "Quiz Enthusiast",    "emoji": "🎯", "desc": "Attempted 10 quizzes"},
    "quizzes_50":         {"name": "Quiz Champion",      "emoji": "🏆", "desc": "Attempted 50 quizzes"},
    "study_1h":           {"name": "First Hour",         "emoji": "⏱️", "desc": "Studied for 1 hour total"},
    "study_10h":          {"name": "10-Hour Club",       "emoji": "📖", "desc": "Studied for 10 hours total"},
    "level_complete":     {"name": "Level Cleared",      "emoji": "🏅", "desc": "Completed all topics in a level"},
    "night_owl":          {"name": "Night Owl",          "emoji": "🦉", "desc": "Studied after midnight"},
    "early_bird":         {"name": "Early Bird",         "emoji": "🐦", "desc": "Studied before 7 AM"},
}


def grant_achievement(user_id, achievement_id):
    if achievement_id not in ACHIEVEMENTS:
        return False
    db = get_db()
    try:
        db.execute("INSERT INTO user_achievements (user_id, achievement_id) VALUES (?,?)",
                   (user_id, achievement_id))
        db.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        db.close()


def get_user_achievements(user_id):
    db = get_db()
    rows = db.execute("SELECT * FROM user_achievements WHERE user_id=? ORDER BY earned_at",
                      (user_id,)).fetchall()
    db.close()
    return [{"id": r["achievement_id"],
             **ACHIEVEMENTS.get(r["achievement_id"], {"name": r["achievement_id"], "emoji": "?", "desc": ""}),
             "earned_at": r["earned_at"]} for r in rows]


def check_and_grant_achievements(user_id):
    from db.progress import get_progress
    newly_granted = []
    progress = get_progress(user_id)
    streak = get_streak(user_id)
    summary = get_activity_summary(user_id, days=9999)
    study_time = get_total_study_time(user_id)
    topics_done = sum(1 for v in progress.values() if v.get("complete"))

    for threshold, aid in [(3, "streak_3"), (7, "streak_7"), (30, "streak_30")]:
        if streak.get("current_streak", 0) >= threshold and grant_achievement(user_id, aid):
            newly_granted.append(aid)
    for threshold, aid in [(5, "topics_5"), (10, "topics_10"), (25, "topics_25"), (50, "topics_50")]:
        if topics_done >= threshold and grant_achievement(user_id, aid):
            newly_granted.append(aid)
    quizzes = summary.get("quizzes_taken", 0) or 0
    for threshold, aid in [(10, "quizzes_10"), (50, "quizzes_50")]:
        if quizzes >= threshold and grant_achievement(user_id, aid):
            newly_granted.append(aid)
    for threshold, aid in [(3600, "study_1h"), (36000, "study_10h")]:
        if study_time >= threshold and grant_achievement(user_id, aid):
            newly_granted.append(aid)
    now = datetime.now()
    if now.hour < 7 and grant_achievement(user_id, "early_bird"):
        newly_granted.append("early_bird")
    if 0 <= now.hour < 5 and grant_achievement(user_id, "night_owl"):
        newly_granted.append("night_owl")
    return newly_granted


# ══════════════════════════════════════════════════════════════════
# STUDY SESSIONS
# ══════════════════════════════════════════════════════════════════

def start_study_session(user_id, topic_id):
    db = get_db()
    cur = db.execute(
        "INSERT INTO user_study_sessions (user_id, topic_id, started_at) VALUES (?,?,?)",
        (user_id, topic_id, datetime.now().isoformat()))
    db.commit()
    sid = cur.lastrowid
    db.close()
    return sid


def end_study_session(session_id):
    db = get_db()
    row = db.execute("SELECT started_at FROM user_study_sessions WHERE id=?",
                     (session_id,)).fetchone()
    if row:
        started = datetime.fromisoformat(row["started_at"])
        duration = min(int((datetime.now() - started).total_seconds()), 7200)
        db.execute("UPDATE user_study_sessions SET ended_at=?, duration_s=? WHERE id=?",
                   (datetime.now().isoformat(), duration, session_id))
        db.commit()
    db.close()


def get_total_study_time(user_id):
    db = get_db()
    row = db.execute(
        "SELECT COALESCE(SUM(duration_s), 0) AS total FROM user_study_sessions WHERE user_id=?",
        (user_id,)).fetchone()
    db.close()
    return row["total"] if row else 0


def get_study_time_by_topic(user_id):
    db = get_db()
    rows = db.execute(
        """SELECT topic_id, SUM(duration_s) AS total_seconds, COUNT(*) AS sessions
           FROM user_study_sessions WHERE user_id=?
           GROUP BY topic_id ORDER BY total_seconds DESC""", (user_id,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_study_time_by_day(user_id, days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        """SELECT DATE(started_at) AS study_date, SUM(duration_s) AS total_seconds, COUNT(*) AS sessions
           FROM user_study_sessions WHERE user_id=? AND started_at >= ?
           GROUP BY study_date ORDER BY study_date""", (user_id, cutoff)).fetchall()
    db.close()
    return [dict(r) for r in rows]


# ══════════════════════════════════════════════════════════════════
# DASHBOARD AGGREGATION
# ══════════════════════════════════════════════════════════════════

def get_dashboard_data(user_id):
    from db.progress import get_progress
    progress = get_progress(user_id)
    streak = get_streak(user_id)
    profile = get_profile(user_id)
    achievements = get_user_achievements(user_id)
    heatmap = get_activity_heatmap(user_id)
    recent = get_recent_activity(user_id, limit=15)
    summary_30d = get_activity_summary(user_id, days=30)
    summary_7d = get_activity_summary(user_id, days=7)
    weekly = get_weekly_activity(user_id)
    study_total = get_total_study_time(user_id)
    study_by_topic = get_study_time_by_topic(user_id)
    study_by_day = get_study_time_by_day(user_id)

    topics_done = sum(1 for v in progress.values() if v.get("complete"))
    quiz_scores = [v["quiz_score"] / v["quiz_total"] * 100
                   for v in progress.values()
                   if v.get("quiz_score") is not None and v.get("quiz_total")]
    avg_quiz = round(sum(quiz_scores) / len(quiz_scores), 1) if quiz_scores else 0

    scored = [(tid, v["quiz_score"], v["quiz_total"])
              for tid, v in progress.items()
              if v.get("quiz_score") is not None and v.get("quiz_total")]
    scored.sort(key=lambda x: x[1] / x[2], reverse=True)

    return {
        "profile": profile, "progress": progress, "streak": streak,
        "achievements": achievements, "all_achievements": ACHIEVEMENTS,
        "heatmap": heatmap, "recent_activity": recent,
        "summary_30d": summary_30d, "summary_7d": summary_7d,
        "weekly_activity": weekly, "study_total_s": study_total,
        "study_by_topic": study_by_topic, "study_by_day": study_by_day,
        "topics_done": topics_done, "avg_quiz_score": avg_quiz,
        "best_topics": scored[:5],
        "worst_topics": scored[-5:] if len(scored) > 5 else [],
    }
