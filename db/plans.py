"""
Plan management — activate, check, and expire user subscription plans.
"""

from datetime import datetime, timedelta
from db.core import get_db


# Plan tier → which levels the user can access
PLAN_LEVELS = {
    "free":      ["Kindergarten"],
    "primary":   ["Kindergarten", "Primary 1–2", "Primary 3–4", "Primary 5–6"],
    "secondary": ["Kindergarten", "Primary 1–2", "Primary 3–4", "Primary 5–6",
                   "Sec 1–2", "Sec 3–4"],
    "jc":        ["Kindergarten", "Primary 1–2", "Primary 3–4", "Primary 5–6",
                   "Sec 1–2", "Sec 3–4", "J1–2"],
    "full":      ["Kindergarten", "Primary 1–2", "Primary 3–4", "Primary 5–6",
                   "Sec 1–2", "Sec 3–4", "J1–2",
                   "Linear Algebra", "Probability & Statistics", "Python",
                   "Deep Learning", "Deep Learning Advanced"],
}

# Duration string → days
PLAN_DURATIONS = {
    "1_month":  30,
    "3_months": 90,
    "1_year":   365,
}


def activate_plan(user_id, plan_tier, plan_duration, amount_paid,
                  payment_ref="", activated_by="admin"):
    """Activate a plan for a user. Deactivates any existing plan of the same tier."""
    days = PLAN_DURATIONS.get(plan_duration, 30)
    now = datetime.now()
    expires = now + timedelta(days=days)

    db = get_db()
    # Deactivate old plans for this user
    db.execute("UPDATE user_plans SET is_active=0 WHERE user_id=? AND is_active=1", (user_id,))
    # Insert new plan
    db.execute(
        """INSERT INTO user_plans
           (user_id, plan_tier, plan_duration, amount_paid, started_at, expires_at,
            payment_ref, activated_by, is_active)
           VALUES (?,?,?,?,?,?,?,?,1)""",
        (user_id, plan_tier, plan_duration, amount_paid,
         now.isoformat(), expires.isoformat(), payment_ref, activated_by))
    # Update user's plan field
    db.execute("UPDATE users SET plan=? WHERE id=?", (plan_tier, user_id))
    db.commit()
    db.close()


def get_active_plan(user_id):
    """Return the user's active plan, or None if free/expired."""
    db = get_db()
    row = db.execute(
        """SELECT * FROM user_plans
           WHERE user_id=? AND is_active=1
           ORDER BY expires_at DESC LIMIT 1""",
        (user_id,)).fetchone()
    db.close()
    if not row:
        return None
    plan = dict(row)
    # Check if expired
    if datetime.fromisoformat(plan["expires_at"]) < datetime.now():
        expire_plan(user_id, plan["id"])
        return None
    # Add days remaining
    remaining = (datetime.fromisoformat(plan["expires_at"]) - datetime.now()).days
    plan["days_remaining"] = max(0, remaining)
    return plan


def expire_plan(user_id, plan_id=None):
    """Mark a plan as expired and revert user to free."""
    db = get_db()
    if plan_id:
        db.execute("UPDATE user_plans SET is_active=0 WHERE id=?", (plan_id,))
    else:
        db.execute("UPDATE user_plans SET is_active=0 WHERE user_id=? AND is_active=1", (user_id,))
    db.execute("UPDATE users SET plan='free' WHERE id=?", (user_id,))
    db.commit()
    db.close()


def get_plan_levels(user_id):
    """Return the set of curriculum levels this user can access based on their plan."""
    plan = get_active_plan(user_id)
    if plan:
        return set(PLAN_LEVELS.get(plan["plan_tier"], PLAN_LEVELS["free"]))
    return set(PLAN_LEVELS["free"])


def get_plan_history(user_id):
    """Return all plans for a user, newest first."""
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_plans WHERE user_id=? ORDER BY started_at DESC",
        (user_id,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_all_active_plans():
    """Admin: return all users with active plans."""
    db = get_db()
    rows = db.execute(
        """SELECT up.*, u.username, u.email
           FROM user_plans up
           JOIN users u ON u.id = up.user_id
           WHERE up.is_active=1
           ORDER BY up.expires_at ASC""").fetchall()
    db.close()
    return [dict(r) for r in rows]
