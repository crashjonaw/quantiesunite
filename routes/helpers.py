"""
Shared route helpers — auth decorators, user helpers, level access.
"""

from functools import wraps
from flask import session, redirect, url_for, flash, request
import database as db
from curriculum_data import LEVELS_ORDER, TOPICS


AGE_GROUP_MAP = {
    "Kindergarten": "kindergarten",
    "Primary 1–2": "primary", "Primary 3–4": "primary", "Primary 5–6": "primary",
    "Sec 1–2": "secondary", "Sec 3–4": "secondary",
    "J1–2": "adult", "Linear Algebra": "adult",
    "Probability & Statistics": "adult", "Python": "adult",
    "Deep Learning": "adult", "Deep Learning Advanced": "adult",
}


def get_age_group(level):
    return AGE_GROUP_MAP.get(level, "adult")


def current_user():
    uid = session.get("user_id")
    if uid:
        return db.get_user_by_id(uid)
    return None


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("auth.login", next=request.path))
        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = current_user()
        if not user or not user["is_admin"]:
            flash("Admin access required.", "danger")
            return redirect(url_for("learning.index"))
        return f(*args, **kwargs)
    return decorated


def get_enabled_levels(target_level):
    """Levels enabled by target_level setting (used for display/curriculum scope)."""
    if target_level not in LEVELS_ORDER:
        return set(LEVELS_ORDER)
    idx = LEVELS_ORDER.index(target_level)
    return set(LEVELS_ORDER[: idx + 1])


def get_accessible_levels(user):
    """Levels the user can actually access based on their plan (or admin/free status)."""
    if not user:
        return set(db.PLAN_LEVELS["free"])
    if user.get("is_admin"):
        return set(LEVELS_ORDER)
    plan_levels = db.get_plan_levels(user["id"])
    return plan_levels


def topic_level_accessible(user, topic):
    if not user:
        return False
    if user.get("is_admin"):
        return True
    accessible = get_accessible_levels(user)
    return topic["level"] in accessible


def user_progress():
    uid = session.get("user_id")
    if uid:
        return db.get_progress(uid)
    return {}


def is_unlocked(tid, progress=None):
    """True if all prerequisites for this topic are completed."""
    t = TOPICS.get(tid)
    if not t:
        return False
    if not t["prereqs"]:
        return True  # No prerequisites — always unlocked
    if progress is None:
        return False
    for prereq_id in t["prereqs"]:
        if not progress.get(prereq_id, {}).get("complete"):
            return False
    return True


def get_avatar_url(user_obj):
    if not user_obj:
        return None
    profile = db.get_profile(user_obj["id"])
    avatar_file = profile.get("avatar_url", "")
    if avatar_file:
        return url_for("static", filename=f"uploads/avatars/{avatar_file}")
    return None
