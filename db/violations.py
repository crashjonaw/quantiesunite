"""
Policy violations — rate-limit tracking, suspicious activity, admin moderation.
"""

from datetime import datetime, timedelta, date
from db.core import get_db


VIOLATION_TYPES = {
    "rate_limit":       {"name": "Rate Limit Hit",       "icon": "🚨", "severity": "warning"},
    "rapid_browsing":   {"name": "Rapid Page Browsing",  "icon": "⚡", "severity": "warning"},
    "repeated_scrape":  {"name": "Repeated Scraping",    "icon": "🕷️", "severity": "critical"},
    "brute_login":      {"name": "Brute-Force Login",    "icon": "🔓", "severity": "critical"},
    "suspicious_agent": {"name": "Suspicious User-Agent","icon": "🤖", "severity": "warning"},
    "manual_flag":      {"name": "Manually Flagged",     "icon": "🚩", "severity": "info"},
}


def log_violation(user_id, violation_type, ip_address="", detail="",
                  endpoint="", severity=None):
    if severity is None:
        severity = VIOLATION_TYPES.get(violation_type, {}).get("severity", "warning")
    db = get_db()
    db.execute(
        """INSERT INTO policy_violations
           (user_id, ip_address, violation_type, severity, detail, endpoint)
           VALUES (?,?,?,?,?,?)""",
        (user_id, ip_address, violation_type, severity, detail, endpoint))
    db.commit()
    db.close()


def get_violations(limit=50, unresolved_only=False, user_id=None):
    db = get_db()
    clauses, params = [], []
    if unresolved_only:
        clauses.append("v.resolved = 0")
    if user_id is not None:
        clauses.append("v.user_id = ?")
        params.append(user_id)
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    rows = db.execute(
        f"""SELECT v.*, u.username FROM policy_violations v
            LEFT JOIN users u ON u.id = v.user_id {where}
            ORDER BY v.created_at DESC LIMIT ?""",
        (*params, limit)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_violation_count(user_id, violation_type=None, days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    if violation_type:
        row = db.execute(
            "SELECT COUNT(*) AS c FROM policy_violations WHERE user_id=? AND violation_type=? AND created_at >= ?",
            (user_id, violation_type, cutoff)).fetchone()
    else:
        row = db.execute(
            "SELECT COUNT(*) AS c FROM policy_violations WHERE user_id=? AND created_at >= ?",
            (user_id, cutoff)).fetchone()
    db.close()
    return row["c"] if row else 0


def resolve_violation(violation_id, resolved_by="admin"):
    db = get_db()
    db.execute(
        "UPDATE policy_violations SET resolved=1, resolved_by=?, resolved_at=? WHERE id=?",
        (resolved_by, datetime.now().isoformat(), violation_id))
    db.commit()
    db.close()


def resolve_all_user_violations(user_id, resolved_by="admin"):
    db = get_db()
    db.execute(
        "UPDATE policy_violations SET resolved=1, resolved_by=?, resolved_at=? WHERE user_id=? AND resolved=0",
        (resolved_by, datetime.now().isoformat(), user_id))
    db.commit()
    db.close()


def admin_violation_timeline(days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        """SELECT DATE(created_at) AS vdate, COUNT(*) AS count,
                  SUM(CASE WHEN severity='critical' THEN 1 ELSE 0 END) AS critical
           FROM policy_violations WHERE DATE(created_at) >= ?
           GROUP BY vdate ORDER BY vdate""",
        (cutoff,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_flagged_users(days=30):
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    db = get_db()
    rows = db.execute(
        """SELECT v.user_id, u.username, u.email, u.created_at AS joined,
                  COUNT(*) AS total_violations,
                  SUM(CASE WHEN v.severity='critical' THEN 1 ELSE 0 END) AS critical_count,
                  SUM(CASE WHEN v.severity='warning' THEN 1 ELSE 0 END) AS warning_count,
                  MAX(v.created_at) AS last_violation,
                  GROUP_CONCAT(DISTINCT v.violation_type) AS violation_types
           FROM policy_violations v LEFT JOIN users u ON u.id = v.user_id
           WHERE v.resolved=0 AND v.created_at >= ?
           GROUP BY v.user_id
           ORDER BY critical_count DESC, total_violations DESC""",
        (cutoff,)).fetchall()
    db.close()
    return [dict(r) for r in rows]
