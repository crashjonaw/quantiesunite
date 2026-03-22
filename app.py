"""
QuantiesUnite — Main Flask + Waitress Server (with Account System)
BloomBurrow-style: single app.py entry point, served via waitress.
Run: python app.py  (or double-click run.bat on Windows)
"""

import json
import os
from functools import wraps

from flask import (Flask, render_template, jsonify, request,
                   session, redirect, url_for, flash)

from curriculum_data import (TOPICS, LEVELS_ORDER, LEVEL_DESCRIPTIONS,
                             get_graph_data, get_topic, get_unlocked_by)
from lesson_content import get_lesson_content, get_quiz
import database as db

app = Flask(__name__)
app.secret_key = "quantiesunite-secret-2024-change-in-production"

# Make Python builtins available in Jinja2 templates
app.jinja_env.globals.update(enumerate=enumerate, len=len, int=int, round=round)

# Initialise database and default admin on startup
db.init_db()
db.ensure_default_admin()


# ── Auth helpers ──────────────────────────────────────────────────────────────

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
            return redirect(url_for("login", next=request.path))
        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = current_user()
        if not user or not user["is_admin"]:
            flash("Admin access required.", "danger")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated


# ── Level access helpers ──────────────────────────────────────────────────────

def get_enabled_levels(target_level):
    """All levels enabled when target_level is selected (cascade downward)."""
    if target_level not in LEVELS_ORDER:
        return set(LEVELS_ORDER)
    idx = LEVELS_ORDER.index(target_level)
    return set(LEVELS_ORDER[: idx + 1])


def topic_level_accessible(user, topic):
    """True if this topic's level is within the user's enabled levels. Admins see all."""
    if not user:
        return False
    if user.get("is_admin"):
        return True
    enabled = get_enabled_levels(user.get("target_level", "Deep Learning Advanced"))
    return topic["level"] in enabled


# ── Progress helpers (now DB-backed per user) ─────────────────────────────────

def user_progress():
    uid = session.get("user_id")
    if uid:
        return db.get_progress(uid)
    return {}


def is_unlocked(tid, progress=None):
    t = TOPICS.get(tid)
    if not t:
        return False
    if not t["prereqs"]:
        return True
    if progress is None:
        progress = user_progress()
    return all(progress.get(p, {}).get("complete") for p in t["prereqs"])


# ── Inject current_user into all templates ────────────────────────────────────

@app.context_processor
def inject_user():
    return {"current_user": current_user(), "LEVELS_ORDER": LEVELS_ORDER}


# ════════════════════════════════════════════════════════════════════
# AUTH ROUTES
# ════════════════════════════════════════════════════════════════════

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("index"))
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
                session["user_id"] = uid
                flash(f"Welcome to QuantiesUnite, {username}! 🎉", "success")
                return redirect(url_for("account"))
    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("index"))
    error = None
    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password   = request.form.get("password", "")
        user = db.verify_credentials(identifier, password)
        if user:
            session["user_id"] = user["id"]
            next_url = request.args.get("next") or url_for("index")
            flash(f"Welcome back, {user['username']}! 👋", "success")
            return redirect(next_url)
        else:
            error = "Invalid email/username or password."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    flash("You've been logged out.", "info")
    return redirect(url_for("login"))


# ════════════════════════════════════════════════════════════════════
# ACCOUNT & LEVEL SELECTOR
# ════════════════════════════════════════════════════════════════════

@app.route("/account", methods=["GET"])
@login_required
def account():
    user = current_user()
    progress = user_progress()
    total  = len(TOPICS)
    done   = sum(1 for v in progress.values() if v.get("complete"))
    enabled = get_enabled_levels(user["target_level"])
    return render_template("account.html",
                           user=user,
                           progress=progress,
                           total=total,
                           done=done,
                           enabled_levels=enabled,
                           levels_order=LEVELS_ORDER,
                           level_descriptions=LEVEL_DESCRIPTIONS)


@app.route("/account/level", methods=["POST"])
@login_required
def update_level():
    level = request.form.get("target_level")
    if level in LEVELS_ORDER:
        db.update_target_level(session["user_id"], level)
        flash(f"Level access updated to: {level} (and all prerequisites). ✅", "success")
    return redirect(url_for("account"))


@app.route("/account/username", methods=["POST"])
@login_required
def update_username():
    new_name = request.form.get("username", "").strip()
    if len(new_name) < 3:
        flash("Username must be at least 3 characters.", "danger")
    else:
        err = db.update_username(session["user_id"], new_name)
        if err:
            flash(err, "danger")
        else:
            flash("Username updated! ✅", "success")
    return redirect(url_for("account"))


@app.route("/account/password", methods=["POST"])
@login_required
def update_password():
    current  = request.form.get("current_password", "")
    new_pw   = request.form.get("new_password", "")
    confirm  = request.form.get("confirm_password", "")
    user = current_user()
    from werkzeug.security import check_password_hash
    if not check_password_hash(user["password_hash"], current):
        flash("Current password is incorrect.", "danger")
    elif len(new_pw) < 6:
        flash("New password must be at least 6 characters.", "danger")
    elif new_pw != confirm:
        flash("Passwords do not match.", "danger")
    else:
        db.update_password(session["user_id"], new_pw)
        flash("Password updated! ✅", "success")
    return redirect(url_for("account"))


# ════════════════════════════════════════════════════════════════════
# ADMIN PANEL
# ════════════════════════════════════════════════════════════════════

@app.route("/admin")
@login_required
@admin_required
def admin_panel():
    users = db.all_users()
    stats = db.site_stats()
    return render_template("admin.html",
                           users=users,
                           stats=stats,
                           total_topics=len(TOPICS),
                           levels_order=LEVELS_ORDER)


@app.route("/admin/toggle-admin/<int:uid>", methods=["POST"])
@login_required
@admin_required
def admin_toggle(uid):
    if uid == session["user_id"]:
        flash("You cannot remove your own admin rights.", "warning")
    else:
        db.toggle_admin(uid)
        flash("Admin status toggled.", "success")
    return redirect(url_for("admin_panel"))


@app.route("/admin/delete-user/<int:uid>", methods=["POST"])
@login_required
@admin_required
def admin_delete_user(uid):
    if uid == session["user_id"]:
        flash("You cannot delete your own account here.", "warning")
    else:
        db.delete_user(uid)
        flash("User deleted.", "success")
    return redirect(url_for("admin_panel"))


@app.route("/admin/user/<int:uid>")
@login_required
@admin_required
def admin_user_detail(uid):
    """Comprehensive per-user progress view."""
    user = db.get_user_by_id(uid)
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("admin_panel"))

    progress_rows = db.get_user_full_progress(uid)
    progress = {r["topic_id"]: r for r in progress_rows}

    # Build level-by-level breakdown
    level_breakdown = {}
    for level in LEVELS_ORDER:
        topics_in_level = {k: v for k, v in TOPICS.items() if v["level"] == level}
        level_topics = []
        for tid, t in topics_in_level.items():
            p = progress.get(tid, {})
            level_topics.append({
                "id":        tid,
                "name":      t["name"],
                "emoji":     t["emoji"],
                "complete":  bool(p.get("complete")),
                "quiz_score": p.get("quiz_score"),
                "quiz_total": p.get("quiz_total"),
                "completed_at": p.get("completed_at"),
            })
        done  = sum(1 for t in level_topics if t["complete"])
        total = len(level_topics)
        level_breakdown[level] = {
            "topics": level_topics,
            "done":   done,
            "total":  total,
            "pct":    round(done / total * 100) if total else 0,
        }

    total_done  = sum(1 for r in progress_rows if r["complete"])
    total_all   = len(TOPICS)
    enabled     = get_enabled_levels(user["target_level"])

    return render_template("admin_user.html",
                           u=user,
                           level_breakdown=level_breakdown,
                           levels_order=LEVELS_ORDER,
                           total_done=total_done,
                           total_all=total_all,
                           enabled_levels=enabled)


# ════════════════════════════════════════════════════════════════════
# MAIN LEARNING ROUTES
# ════════════════════════════════════════════════════════════════════

@app.route("/")
def index():
    user = current_user()
    if user:
        progress = db.get_progress(user["id"])
        total = len(TOPICS)
        done  = sum(1 for v in progress.values() if v.get("complete"))
        enabled = get_enabled_levels(user["target_level"])
        accessible = sum(1 for t in TOPICS.values() if t["level"] in enabled)
    else:
        done = total = accessible = 0
    return render_template("index.html",
                           total=len(TOPICS),
                           done=done,
                           percent=round(done / len(TOPICS) * 100) if done else 0,
                           user=user,
                           accessible=accessible)


@app.route("/graph")
@login_required
def graph_page():
    return render_template("graph.html")


@app.route("/api/graph")
@login_required
def api_graph():
    user = current_user()
    progress  = db.get_progress(user["id"]) if user else {}
    is_admin  = bool(user and user.get("is_admin"))
    enabled   = set(LEVELS_ORDER) if is_admin else (
                get_enabled_levels(user["target_level"]) if user else set(LEVELS_ORDER))
    data = get_graph_data()
    for node in data["nodes"]:
        tid = node["id"]
        t   = TOPICS.get(tid, {})
        node["complete"]    = bool(progress.get(tid, {}).get("complete"))
        node["unlocked"]    = is_admin or is_unlocked(tid, progress)
        node["accessible"]  = is_admin or (t.get("level", "") in enabled)
        node["quiz_score"]  = progress.get(tid, {}).get("quiz_score")
        node["quiz_total"]  = progress.get(tid, {}).get("quiz_total")
    return jsonify(data)


@app.route("/curriculum")
@login_required
def curriculum():
    user = current_user()
    progress = db.get_progress(user["id"]) if user else {}
    enabled  = get_enabled_levels(user["target_level"]) if user else set(LEVELS_ORDER)
    levels = {}
    for level in LEVELS_ORDER:
        topics_in_level = {k: v for k, v in TOPICS.items() if v["level"] == level}
        levels[level] = {
            "desc":       LEVEL_DESCRIPTIONS.get(level, ""),
            "topics":     topics_in_level,
            "total":      len(topics_in_level),
            "done":       sum(1 for k in topics_in_level if progress.get(k, {}).get("complete")),
            "accessible": level in enabled,
        }
    return render_template("curriculum.html",
                           levels=levels,
                           levels_order=LEVELS_ORDER,
                           progress=progress,
                           enabled_levels=enabled)


@app.route("/topic/<tid>")
@login_required
def topic(tid):
    user = current_user()
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404

    is_admin         = bool(user and user.get("is_admin"))
    enabled          = set(LEVELS_ORDER) if is_admin else (
                       get_enabled_levels(user["target_level"]) if user else set(LEVELS_ORDER))
    level_accessible = is_admin or (t["level"] in enabled)

    progress         = db.get_progress(user["id"]) if user else {}
    unlocked         = is_admin or is_unlocked(tid, progress)
    prereq_topics   = {p: TOPICS[p] for p in t["prereqs"] if p in TOPICS}
    unlocks_topics  = {u: TOPICS[u] for u in get_unlocked_by(tid) if u in TOPICS}
    content         = get_lesson_content(tid)
    complete        = bool(progress.get(tid, {}).get("complete"))
    quiz_score      = progress.get(tid, {}).get("quiz_score")
    quiz_total      = progress.get(tid, {}).get("quiz_total")

    return render_template("topic.html",
                           tid=tid, t=t,
                           content=content,
                           unlocked=unlocked,
                           level_accessible=level_accessible,
                           prereq_topics=prereq_topics,
                           unlocks_topics=unlocks_topics,
                           complete=complete,
                           quiz_score=quiz_score,
                           quiz_total=quiz_total)


@app.route("/topic/<tid>/quiz")
@login_required
def quiz_page(tid):
    user = current_user()
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404

    is_admin = bool(user and user.get("is_admin"))
    enabled  = set(LEVELS_ORDER) if is_admin else get_enabled_levels(user["target_level"])
    if not is_admin and t["level"] not in enabled:
        flash("Enable this level in your account settings first.", "warning")
        return redirect(url_for("account"))

    progress = db.get_progress(user["id"])
    if not is_admin and not is_unlocked(tid, progress):
        return redirect(url_for("topic", tid=tid))

    quiz = get_quiz(tid)
    return render_template("quiz.html", tid=tid, t=t, quiz=quiz)


@app.route("/api/quiz/submit", methods=["POST"])
@login_required
def submit_quiz():
    user = current_user()
    data    = request.get_json()
    tid     = data.get("tid")
    answers = data.get("answers", {})
    quiz    = get_quiz(tid)
    if not quiz:
        return jsonify({"error": "No quiz found"}), 404

    score   = 0
    results = []
    for i, q in enumerate(quiz):
        key      = str(i)
        user_ans = answers.get(key, "").strip().lower()
        correct  = str(q["answer"]).strip().lower()
        ok       = (user_ans == correct)
        if ok:
            score += 1
        results.append({
            "question":       q["question"],
            "user":           answers.get(key, ""),
            "correct_answer": q["answer"],
            "correct":        ok,
            "explanation":    q.get("explanation", ""),
        })

    total  = len(quiz)
    passed = score >= total * 0.7

    db.save_quiz_score(user["id"], tid, score, total)
    if passed:
        db.mark_topic_complete(user["id"], tid)

    return jsonify({"score": score, "total": total, "results": results, "passed": passed})


@app.route("/api/complete/<tid>", methods=["POST"])
@login_required
def api_complete(tid):
    user = current_user()
    db.mark_topic_complete(user["id"], tid)
    return jsonify({"ok": True})


@app.route("/progress")
@login_required
def progress_page():
    user     = current_user()
    progress = db.get_progress(user["id"])
    total    = len(TOPICS)
    done     = sum(1 for v in progress.values() if v.get("complete"))
    enabled  = get_enabled_levels(user["target_level"])
    level_stats = {}
    for level in LEVELS_ORDER:
        topics_in_level = [k for k, v in TOPICS.items() if v["level"] == level]
        level_stats[level] = {
            "done":       sum(1 for k in topics_in_level if progress.get(k, {}).get("complete")),
            "total":      len(topics_in_level),
            "accessible": level in enabled,
        }
    return render_template("progress.html",
                           progress=progress,
                           topics=TOPICS,
                           total=total,
                           done=done,
                           level_stats=level_stats,
                           levels_order=LEVELS_ORDER)


@app.route("/api/reset", methods=["POST"])
@login_required
def reset_progress():
    user = current_user()
    db.reset_progress(user["id"])
    flash("Progress reset.", "info")
    return jsonify({"ok": True})


@app.route("/search")
@login_required
def search():
    user = current_user()
    q    = request.args.get("q", "").lower()
    enabled = get_enabled_levels(user["target_level"]) if user else set(LEVELS_ORDER)
    results = []
    if q:
        for tid, t in TOPICS.items():
            if (q in t["name"].lower() or
                    q in t["level"].lower() or
                    q in t["tagline"].lower()):
                results.append({"id": tid, **t,
                                 "accessible": t["level"] in enabled})
    return render_template("search.html", query=q, results=results)


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        from waitress import serve
        print("=" * 55)
        print("  QuantiesUnite — Learning Platform")
        print("  Serving on http://localhost:5001")
        print("  Press Ctrl+C to stop")
        print("=" * 55)
        serve(app, host="0.0.0.0", port=5001, threads=4)
    except ImportError:
        print("Waitress not found — using Flask dev server")
        app.run(host="0.0.0.0", port=5001, debug=True)
