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
    """Activate a plan for a user. Same tier = extend. Different tier = coexist."""
    days = PLAN_DURATIONS.get(plan_duration, 30)
    now = datetime.now()

    db = get_db()

    # Check if user has an active plan of the same tier — extend it
    existing = db.execute(
        "SELECT * FROM user_plans WHERE user_id=? AND plan_tier=? AND is_active=1",
        (user_id, plan_tier)).fetchone()

    if existing:
        # Extend from current expiry (not from now)
        current_expiry = datetime.fromisoformat(existing["expires_at"])
        base = max(current_expiry, now)
        new_expiry = base + timedelta(days=days)
        db.execute("UPDATE user_plans SET expires_at=? WHERE id=?",
                   (new_expiry.isoformat(), existing["id"]))
        # Log the extension as a separate record
        db.execute(
            """INSERT INTO user_plans
               (user_id, plan_tier, plan_duration, amount_paid, started_at, expires_at,
                payment_ref, activated_by, is_active)
               VALUES (?,?,?,?,?,?,?,?,0)""",
            (user_id, plan_tier, plan_duration, amount_paid,
             now.isoformat(), new_expiry.isoformat(), payment_ref,
             activated_by + "_extension"))
    else:
        # Different tier — don't deactivate old plans, let them coexist
        expires = now + timedelta(days=days)
        db.execute(
            """INSERT INTO user_plans
               (user_id, plan_tier, plan_duration, amount_paid, started_at, expires_at,
                payment_ref, activated_by, is_active)
               VALUES (?,?,?,?,?,?,?,?,1)""",
            (user_id, plan_tier, plan_duration, amount_paid,
             now.isoformat(), expires.isoformat(), payment_ref, activated_by))

    # Update user's plan field to the highest active tier
    all_active = db.execute(
        "SELECT plan_tier FROM user_plans WHERE user_id=? AND is_active=1",
        (user_id,)).fetchall()
    best = max([r["plan_tier"] for r in all_active], key=lambda t: TIER_RANK.get(t, 0))
    db.execute("UPDATE users SET plan=? WHERE id=?", (best, user_id))
    db.commit()
    db.close()


TIER_RANK = {"free": 0, "primary": 1, "secondary": 2, "jc": 3, "full": 4}


def get_all_active_plans_for_user(user_id):
    """Return all active (non-expired) plans for a user."""
    db = get_db()
    rows = db.execute(
        "SELECT * FROM user_plans WHERE user_id=? AND is_active=1 ORDER BY expires_at DESC",
        (user_id,)).fetchall()
    db.close()

    now = datetime.now()
    active = []
    for row in rows:
        plan = dict(row)
        if datetime.fromisoformat(plan["expires_at"]) < now:
            # Expired — deactivate
            expire_plan(user_id, plan["id"])
        else:
            plan["days_remaining"] = max(0, (datetime.fromisoformat(plan["expires_at"]) - now).days)
            active.append(plan)
    return active


def get_active_plan(user_id):
    """Return the user's highest-tier active plan, or None if free/expired."""
    plans = get_all_active_plans_for_user(user_id)
    if not plans:
        return None
    # Return the highest tier
    plans.sort(key=lambda p: TIER_RANK.get(p["plan_tier"], 0), reverse=True)
    return plans[0]


def expire_plan(user_id, plan_id=None):
    """Mark a plan (or all plans) as expired."""
    db = get_db()
    if plan_id:
        db.execute("UPDATE user_plans SET is_active=0 WHERE id=?", (plan_id,))
    else:
        db.execute("UPDATE user_plans SET is_active=0 WHERE user_id=? AND is_active=1", (user_id,))
    # Update user's plan field to the highest remaining active plan
    remaining = get_db().execute(
        "SELECT plan_tier FROM user_plans WHERE user_id=? AND is_active=1 ORDER BY id",
        (user_id,)).fetchall()
    if remaining:
        best = max([r["plan_tier"] for r in remaining], key=lambda t: TIER_RANK.get(t, 0))
        db.execute("UPDATE users SET plan=? WHERE id=?", (best, user_id))
    else:
        db.execute("UPDATE users SET plan='free' WHERE id=?", (user_id,))
    db.commit()
    db.close()


def get_plan_levels(user_id):
    """Return the set of curriculum levels this user can access based on ALL active plans."""
    plans = get_all_active_plans_for_user(user_id)
    if not plans:
        return set(PLAN_LEVELS["free"])
    # Combine levels from all active plans
    levels = set(PLAN_LEVELS["free"])
    for plan in plans:
        levels.update(PLAN_LEVELS.get(plan["plan_tier"], []))
    return levels


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
