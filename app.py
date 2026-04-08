"""
QuantiesUnite — Main Flask Application Entry Point

Architecture:
  app.py              — this file (app factory, config, middleware)
  routes/             — Flask Blueprints (auth, account, dashboard, admin, learning, exam)
  db/                 — Database layer (core, users, progress, questions, profiles, violations, exams)
  curriculum_data.py  — Topic/curriculum definitions
  lesson_content.py   — Lesson & quiz content loading
  modules/            — Authored lesson content

Run:
  Development:  python app.py
  Production:   gunicorn -c gunicorn.conf.py app:app
"""

import os
import time

from flask import Flask, render_template, request, session

from curriculum_data import LEVELS_ORDER
import database as db
from routes import register_blueprints
from routes.helpers import current_user, get_avatar_url, get_age_group

# ── App creation ─────────────────────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = "quantiesunite-secret-2024-change-in-production"

# Avatar upload config
AVATAR_UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "static", "uploads", "avatars")
os.makedirs(AVATAR_UPLOAD_DIR, exist_ok=True)

# Make Python builtins available in Jinja2 templates
app.jinja_env.globals.update(enumerate=enumerate, len=len, int=int, round=round)
app.jinja_env.globals["get_age_group"] = get_age_group


# ── Initialise database ─────────────────────────────────────────────────────

db.init_db()
db.ensure_default_admin()


# ── Content rate limiter (multi-worker safe via SQLite) ──────────────────────

RATE_LIMIT_WINDOW   = 60
RATE_LIMIT_MAX_HITS = 15
RATE_LIMIT_COOLDOWN = 30

_CONTENT_ENDPOINTS = {"learning.topic", "learning.concept_page",
                      "learning.quiz_page", "learning.mindmap_page",
                      "learning.topic_overview"}


def _init_rate_limit_table():
    conn = db.get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS _rate_limit_hits (
            user_id   INTEGER NOT NULL,
            hit_time  REAL    NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_rl_user ON _rate_limit_hits(user_id);
        CREATE TABLE IF NOT EXISTS _rate_limit_blocks (
            user_id       INTEGER PRIMARY KEY,
            blocked_until REAL NOT NULL,
            strike_count  INTEGER DEFAULT 1
        );
    """)
    conn.commit()
    conn.close()

_init_rate_limit_table()


@app.before_request
def check_content_rate_limit():
    uid = session.get("user_id")
    if not uid:
        return

    endpoint = request.endpoint
    if endpoint not in _CONTENT_ENDPOINTS:
        return

    user = db.get_user_by_id(uid)
    if user and user.get("is_admin"):
        return

    now = time.time()
    conn = db.get_db()

    try:
        block = conn.execute(
            "SELECT blocked_until, strike_count FROM _rate_limit_blocks WHERE user_id=?",
            (uid,)).fetchone()

        if block and block["blocked_until"] > now:
            remaining = block["blocked_until"] - now
            conn.close()
            return render_template("pages/rate_limited.html",
                                   wait_seconds=int(remaining) + 1), 429

        if block and block["blocked_until"] <= now:
            conn.execute("DELETE FROM _rate_limit_blocks WHERE user_id=?", (uid,))

        conn.execute("INSERT INTO _rate_limit_hits (user_id, hit_time) VALUES (?,?)",
                     (uid, now))
        cutoff = now - RATE_LIMIT_WINDOW
        conn.execute("DELETE FROM _rate_limit_hits WHERE user_id=? AND hit_time < ?",
                     (uid, cutoff))

        hit_count = conn.execute(
            "SELECT COUNT(*) AS c FROM _rate_limit_hits WHERE user_id=? AND hit_time >= ?",
            (uid, cutoff)).fetchone()["c"]

        if hit_count > RATE_LIMIT_MAX_HITS:
            vcount = (block["strike_count"] + 1) if block else 1
            cooldown = min(RATE_LIMIT_COOLDOWN * (2 ** (vcount - 1)), 600)
            conn.execute(
                """INSERT INTO _rate_limit_blocks (user_id, blocked_until, strike_count)
                   VALUES (?,?,?) ON CONFLICT(user_id) DO UPDATE
                   SET blocked_until=excluded.blocked_until, strike_count=excluded.strike_count""",
                (uid, now + cooldown, vcount))
            conn.execute("DELETE FROM _rate_limit_hits WHERE user_id=?", (uid,))
            conn.commit()
            conn.close()

            ip = request.remote_addr or ""
            severity = "critical" if vcount >= 3 else "warning"
            vtype = "repeated_scrape" if vcount >= 3 else "rate_limit"
            db.log_violation(uid, vtype, ip_address=ip,
                             detail=f"Strike {vcount}: {RATE_LIMIT_MAX_HITS}+ pages "
                                    f"in {RATE_LIMIT_WINDOW}s (cooldown {int(cooldown)}s)",
                             endpoint=endpoint, severity=severity)
            return render_template("pages/rate_limited.html",
                                   wait_seconds=int(cooldown)), 429
        conn.commit()
    finally:
        try:
            conn.close()
        except Exception:
            pass


# ── Session validation (max 1 device) ────────────────────────────────────────

@app.before_request
def check_session_valid():
    """Kick users whose session was replaced by a newer login."""
    if session.get("user_id") and session.get("sid"):
        if not db.is_session_valid(session["user_id"], session["sid"]):
            session.clear()
            from flask import flash
            flash("You've been logged out because your account was signed in on another device.", "warning")
            return redirect("/login")


# ── Context processors ───────────────────────────────────────────────────────

@app.context_processor
def inject_user():
    user = current_user()
    user_pastel = ""
    user_theme = ""
    if user:
        profile = db.get_profile(user["id"])
        prefs = profile.get("preferences", {}) or {}
        user_pastel = prefs.get("pastel", "")
        user_theme = prefs.get("theme", "")
    return {
        "current_user": user,
        "current_avatar_url": get_avatar_url(user) if user else None,
        "LEVELS_ORDER": LEVELS_ORDER,
        "get_age_group": get_age_group,
        "user_pastel": user_pastel,
        "user_theme": user_theme,
    }


# ── Register all route blueprints ────────────────────────────────────────────

register_blueprints(app)


# ── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        from waitress import serve
        print("=" * 55)
        print("  QuantiesUnite — Learning Platform")
        print("  Serving on http://localhost:5001")
        print("  For production, use: gunicorn -c gunicorn.conf.py app:app")
        print("  Press Ctrl+C to stop")
        print("=" * 55)
        serve(app, host="0.0.0.0", port=5001, threads=4)
    except ImportError:
        print("Waitress not found — using Flask dev server")
        app.run(host="0.0.0.0", port=5001, debug=True)
