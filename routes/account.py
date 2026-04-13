"""Account routes — settings, profile, avatar, password, level."""

import os
import uuid
from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from curriculum_data import LEVELS_ORDER, LEVEL_DESCRIPTIONS, TOPICS
import database as db
from routes.helpers import current_user, login_required, get_enabled_levels

account_bp = Blueprint("account", __name__)

AVATAR_UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                 "static", "uploads", "avatars")
AVATAR_MAX_SIZE_MB = 5
AVATAR_OUTPUT_PX   = 256
AVATAR_QUALITY     = 75
ALLOWED_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


@account_bp.route("/account", methods=["GET"])
@login_required
def account():
    user = current_user()
    progress = db.get_progress(user["id"])
    total  = len(TOPICS)
    done   = sum(1 for v in progress.values() if v.get("complete"))
    enabled = get_enabled_levels(user["target_level"])
    active_plan = db.get_active_plan(user["id"])
    return render_template("pages/account.html",
                           user=user, progress=progress, total=total, done=done,
                           enabled_levels=enabled, levels_order=LEVELS_ORDER,
                           level_descriptions=LEVEL_DESCRIPTIONS,
                           active_plan=active_plan)


@account_bp.route("/account/level", methods=["POST"])
@login_required
def update_level():
    user = current_user()
    level = request.form.get("target_level") or request.form.get("new_grade")

    # If grade already set, check 30-day cooldown
    if user.get("current_level"):
        from datetime import datetime, timedelta
        changed_at = user.get("current_level_changed_at")
        if changed_at:
            last_change = datetime.fromisoformat(changed_at)
            days_since = (datetime.now() - last_change).days
            if days_since < 30:
                remaining = 30 - days_since
                flash(f"You can change your grade again in {remaining} days.", "warning")
                return redirect(url_for("account.account"))

    if level in LEVELS_ORDER:
        db.set_current_level(session["user_id"], level)
        db.update_target_level(session["user_id"], "Deep Learning Advanced")
        # Mark lower levels as complete
        grade_idx = LEVELS_ORDER.index(level)
        for tid, t in TOPICS.items():
            topic_level = t["level"]
            if topic_level in LEVELS_ORDER:
                if LEVELS_ORDER.index(topic_level) < grade_idx:
                    db.mark_topic_complete(user["id"], tid)
        flash(f"Grade set to: {level}. All lower levels marked as complete.", "success")
    return redirect(url_for("account.account"))


@account_bp.route("/account/setup", methods=["POST"])
@login_required
def account_setup():
    """One-time setup for Google sign-up users — set username and grade."""
    user = current_user()
    username = request.form.get("username", "").strip()
    grade = request.form.get("grade", "").strip()

    # Validate username
    if len(username) < 3:
        flash("Username must be at least 3 characters.", "warning")
        return redirect(url_for("account.account"))
    existing = db.get_user_by_username(username)
    if existing and existing["id"] != user["id"]:
        flash("That username is already taken.", "warning")
        return redirect(url_for("account.account"))

    # Update username
    db.update_username(user["id"], username)

    # Set grade (one-time)
    if grade and grade in LEVELS_ORDER and not user.get("current_level"):
        db.set_current_level(user["id"], grade)
        db.update_target_level(user["id"], "Deep Learning Advanced")
        grade_idx = LEVELS_ORDER.index(grade)
        for tid, t in TOPICS.items():
            topic_level = t["level"]
            if topic_level in LEVELS_ORDER:
                if LEVELS_ORDER.index(topic_level) < grade_idx:
                    db.mark_topic_complete(user["id"], tid)

    session.pop("needs_setup", None)
    flash(f"Welcome to QuantiesUnite, {username}!", "success")
    return redirect(url_for("learning.index"))


@account_bp.route("/account/username", methods=["POST"])
@login_required
def update_username():
    new_name = request.form.get("username", "").strip()
    if len(new_name) < 3:
        flash("Username must be at least 3 characters.", "danger")
    elif new_name == current_user()["username"]:
        flash("That's already your username.", "info")
    else:
        existing = db.get_user_by_username(new_name)
        if existing and existing["id"] != session["user_id"]:
            flash(f"Username \"{new_name}\" is already taken. Please choose another.", "danger")
        else:
            err = db.update_username(session["user_id"], new_name)
            if err:
                flash(err, "danger")
            else:
                flash("Username updated!", "success")
    return redirect(url_for("account.account"))


@account_bp.route("/account/edit")
@login_required
def edit_profile():
    user = current_user()
    profile = db.get_profile(user["id"])
    return render_template("pages/edit_profile.html", user=user, profile=profile)


@account_bp.route("/account/profile", methods=["POST"])
@login_required
def update_profile():
    uid = session["user_id"]
    db.update_profile(uid,
                      display_name=request.form.get("display_name", "").strip(),
                      bio=request.form.get("bio", "").strip(),
                      school=request.form.get("school", "").strip(),
                      grade=request.form.get("grade", "").strip())
    flash("Profile updated!", "success")
    return redirect(url_for("account.edit_profile"))


@account_bp.route("/account/avatar", methods=["POST"])
@login_required
def upload_avatar():
    uid = session["user_id"]
    file = request.files.get("avatar")
    if not file or not file.filename:
        flash("No file selected.", "warning")
        return redirect(url_for("dashboard.dashboard"))

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_IMAGE_EXTS:
        flash("Invalid file type. Use JPG, PNG, GIF, or WebP.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    file_data = file.read()
    if len(file_data) > AVATAR_MAX_SIZE_MB * 1024 * 1024:
        flash(f"File too large. Maximum {AVATAR_MAX_SIZE_MB} MB.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    from PIL import Image
    import io
    try:
        img = Image.open(io.BytesIO(file_data))
    except Exception:
        flash("Could not read image file.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    w, h = img.size
    if w != h:
        side = min(w, h)
        left, top = (w - side) // 2, (h - side) // 2
        img = img.crop((left, top, left + side, top + side))
    img = img.resize((AVATAR_OUTPUT_PX, AVATAR_OUTPUT_PX), Image.LANCZOS)

    old_profile = db.get_profile(uid)
    old_file = old_profile.get("avatar_url", "")
    if old_file:
        old_path = os.path.join(AVATAR_UPLOAD_DIR, old_file)
        if os.path.exists(old_path):
            os.remove(old_path)

    filename = f"{uid}_{uuid.uuid4().hex[:8]}.jpg"
    img.save(os.path.join(AVATAR_UPLOAD_DIR, filename), "JPEG",
             quality=AVATAR_QUALITY, optimize=True)
    db.update_profile(uid, avatar_url=filename)
    flash("Profile picture updated!", "success")
    return redirect(url_for("dashboard.dashboard"))


@account_bp.route("/account/avatar/remove", methods=["POST"])
@login_required
def remove_avatar():
    uid = session["user_id"]
    profile = db.get_profile(uid)
    old_file = profile.get("avatar_url", "")
    if old_file:
        old_path = os.path.join(AVATAR_UPLOAD_DIR, old_file)
        if os.path.exists(old_path):
            os.remove(old_path)
    db.update_profile(uid, avatar_url="")
    flash("Profile picture removed.", "info")
    return redirect(url_for("dashboard.dashboard"))


@account_bp.route("/account/password", methods=["POST"])
@login_required
def update_password():
    current_pw = request.form.get("current_password", "")
    new_pw     = request.form.get("new_password", "")
    confirm    = request.form.get("confirm_password", "")
    user = current_user()
    if not check_password_hash(user["password_hash"], current_pw):
        flash("Current password is incorrect.", "danger")
    elif len(new_pw) < 6:
        flash("New password must be at least 6 characters.", "danger")
    elif new_pw != confirm:
        flash("Passwords do not match.", "danger")
    else:
        db.update_password(session["user_id"], new_pw)
        flash("Password updated!", "success")
    return redirect(url_for("account.account"))


@account_bp.route("/api/preferences", methods=["POST"])
@login_required
def save_preferences():
    """Save user theme/pastel preferences to profile."""
    uid = session["user_id"]
    data = request.get_json()
    profile = db.get_profile(uid)
    prefs = profile.get("preferences", {}) or {}

    if "pastel" in data:
        prefs["pastel"] = data["pastel"]
    if "theme" in data:
        prefs["theme"] = data["theme"]

    db.update_profile(uid, preferences=prefs)
    return jsonify({"ok": True})
