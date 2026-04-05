"""Auth routes — register, login, logout."""

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from curriculum_data import TOPICS, LEVELS_ORDER
import database as db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("learning.index"))
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm", "")
        if not username or not email or not password:
            error = "All fields are required."
        elif len(username) < 3:
            error = "Username must be at least 3 characters."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            uid, err = db.create_user(username, email, password)
            if err:
                error = err
            else:
                grade = request.form.get("grade", "").strip()
                if grade and grade in LEVELS_ORDER:
                    grade_idx = LEVELS_ORDER.index(grade)
                    for tid, t in TOPICS.items():
                        topic_level = t["level"]
                        if topic_level in LEVELS_ORDER:
                            if LEVELS_ORDER.index(topic_level) < grade_idx:
                                db.mark_topic_complete(uid, tid)
                session["user_id"] = uid
                flash(f"Welcome to QuantiesUnite, {username}!", "success")
                return redirect(url_for("account.account"))
    return render_template("auth/register.html", error=error)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("learning.index"))
    error = None
    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password   = request.form.get("password", "")
        user = db.verify_credentials(identifier, password)
        if user:
            session["user_id"] = user["id"]
            db.log_activity(user["id"], "login", points=1)
            db.grant_achievement(user["id"], "first_login")
            db.check_and_grant_achievements(user["id"])
            next_url = request.args.get("next") or url_for("learning.index")
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(next_url)
        else:
            error = "Invalid email/username or password."
    return render_template("auth/login.html", error=error)


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You've been logged out.", "info")
    return redirect(url_for("auth.login"))
