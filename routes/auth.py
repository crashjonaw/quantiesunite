"""Auth routes — register, login, logout, Google OAuth."""

import os
import json
import subprocess
import secrets
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from curriculum_data import TOPICS, LEVELS_ORDER
import database as db

auth_bp = Blueprint("auth", __name__)

# ── Google OAuth config ────────────────────────────────────────────────────────
_google_creds_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "google_api_secret.json")
_google_creds = {}
if os.path.exists(_google_creds_path):
    with open(_google_creds_path) as f:
        _google_creds = json.load(f).get("web", {})

GOOGLE_CLIENT_ID = _google_creds.get("client_id", "")
GOOGLE_CLIENT_SECRET = _google_creds.get("client_secret", "")
GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URI = "https://www.googleapis.com/oauth2/v2/userinfo"


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
                    db.update_target_level(uid, "Deep Learning Advanced")
                    db.set_current_level(uid, grade)
                    grade_idx = LEVELS_ORDER.index(grade)
                    for tid, t in TOPICS.items():
                        topic_level = t["level"]
                        if topic_level in LEVELS_ORDER:
                            if LEVELS_ORDER.index(topic_level) < grade_idx:
                                db.mark_topic_complete(uid, tid)
                session.permanent = True
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
            session.permanent = True
            session["user_id"] = user["id"]
            session["sid"] = secrets.token_urlsafe(16)
            device = request.headers.get("User-Agent", "")[:100]
            db.register_session(user["id"], session["sid"], device)
            db.log_activity(user["id"], "login", points=1)
            db.grant_achievement(user["id"], "first_login")
            db.check_and_grant_achievements(user["id"])
            next_url = request.args.get("next") or url_for("learning.index")
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(next_url)
        else:
            error = "Invalid email/username or password."
            # Track failed login attempts for brute-force detection
            ip = request.remote_addr or ""
            _track_failed_login(ip, identifier)
    return render_template("auth/login.html", error=error)


_FAILED_LOGINS = {}  # ip -> list of timestamps

def _track_failed_login(ip, identifier):
    """Detect brute-force login attempts: 5+ failures from same IP in 5 minutes."""
    import time
    now = time.time()
    window = 300  # 5 minutes
    if ip not in _FAILED_LOGINS:
        _FAILED_LOGINS[ip] = []
    _FAILED_LOGINS[ip] = [t for t in _FAILED_LOGINS[ip] if now - t < window]
    _FAILED_LOGINS[ip].append(now)
    count = len(_FAILED_LOGINS[ip])
    if count >= 5:
        # Try to find the user to attach violation to their account
        user = db.get_user_by_email(identifier) or db.get_user_by_username(identifier)
        uid = user["id"] if user else None
        db.log_violation(uid, "brute_login", ip_address=ip,
                         detail=f"{count} failed login attempts in {window}s for '{identifier}'",
                         endpoint="auth.login", severity="critical")
        _FAILED_LOGINS[ip] = []  # reset after logging


@auth_bp.route("/logout")
def logout():
    sid = session.get("sid")
    if sid:
        db.remove_session(sid)
    session.clear()
    flash("You've been logged out.", "info")
    return redirect(url_for("auth.login"))


# ── Google OAuth ───────────────────────────────────────────────────────────────

@auth_bp.route("/auth/google")
def google_login():
    """Redirect user to Google's OAuth consent screen."""
    if not GOOGLE_CLIENT_ID:
        flash("Google Sign-In is not configured.", "warning")
        return redirect(url_for("auth.login"))

    # Generate state token to prevent CSRF
    state = secrets.token_urlsafe(32)
    session["oauth_state"] = state

    # Determine redirect URI based on request host
    if "localhost" in request.host or "127.0.0.1" in request.host:
        redirect_uri = "http://localhost:5001/auth/google/callback"
    else:
        redirect_uri = "https://quantiesunite.sg/auth/google/callback"

    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "offline",
        "prompt": "select_account",
    }
    auth_url = GOOGLE_AUTH_URI + "?" + "&".join(f"{k}={v}" for k, v in params.items())
    return redirect(auth_url)


@auth_bp.route("/auth/google/callback")
def google_callback():
    """Handle Google OAuth callback — login or register the user."""
    try:
        return _handle_google_callback()
    except Exception as e:
        import traceback
        traceback.print_exc()
        flash(f"Google sign-in error: {str(e)}", "danger")
        return redirect(url_for("auth.login"))


def _handle_google_callback():
    error = request.args.get("error")
    if error:
        flash(f"Google sign-in was cancelled or failed: {error}", "warning")
        return redirect(url_for("auth.login"))

    code = request.args.get("code")
    state = request.args.get("state")

    # Verify state token
    if state != session.pop("oauth_state", None):
        flash("Invalid OAuth state. Please try again.", "danger")
        return redirect(url_for("auth.login"))

    if not code:
        flash("No authorization code received.", "warning")
        return redirect(url_for("auth.login"))

    # Determine redirect URI
    if "localhost" in request.host or "127.0.0.1" in request.host:
        redirect_uri = "http://localhost:5001/auth/google/callback"
    else:
        redirect_uri = "https://quantiesunite.sg/auth/google/callback"

    # Exchange code for access token (using curl to avoid Python SSL crash on macOS)
    try:
        token_result = subprocess.run([
            "curl", "-s", "-X", "POST", GOOGLE_TOKEN_URI,
            "-d", f"code={code}&client_id={GOOGLE_CLIENT_ID}&client_secret={GOOGLE_CLIENT_SECRET}&redirect_uri={redirect_uri}&grant_type=authorization_code",
            "-H", "Content-Type: application/x-www-form-urlencoded",
            "--max-time", "15",
        ], capture_output=True, text=True, timeout=20)
        token_data = json.loads(token_result.stdout)
    except Exception as e:
        flash(f"Failed to authenticate with Google: {e}", "danger")
        return redirect(url_for("auth.login"))

    access_token = token_data.get("access_token")
    if not access_token:
        error_msg = token_data.get("error_description", token_data.get("error", "Unknown error"))
        flash(f"Google authentication failed: {error_msg}", "danger")
        return redirect(url_for("auth.login"))

    # Get user info from Google (using curl)
    try:
        info_result = subprocess.run([
            "curl", "-s", GOOGLE_USERINFO_URI,
            "-H", f"Authorization: Bearer {access_token}",
            "--max-time", "15",
        ], capture_output=True, text=True, timeout=20)
        userinfo = json.loads(info_result.stdout)
    except Exception as e:
        flash(f"Failed to get user info from Google: {e}", "danger")
        return redirect(url_for("auth.login"))
    google_email = userinfo.get("email", "")
    google_name = userinfo.get("name", "")
    google_picture = userinfo.get("picture", "")

    if not google_email:
        flash("Could not retrieve email from Google.", "danger")
        return redirect(url_for("auth.login"))

    # Check if user already exists with this email
    user = db.get_user_by_email(google_email)

    if user:
        # Existing user — log them in
        session.permanent = True
        session["user_id"] = user["id"]
        session["sid"] = secrets.token_urlsafe(16)
        device = request.headers.get("User-Agent", "")[:100]
        db.register_session(user["id"], session["sid"], device)
        db.log_activity(user["id"], "login", points=1)
        db.check_and_grant_achievements(user["id"])
        flash(f"Welcome back, {user['username']}!", "success")
        return redirect(url_for("learning.index"))
    else:
        # New user — create account
        # Generate username from Google name (remove spaces, add random suffix)
        base_username = google_name.replace(" ", "").lower()[:15]
        if len(base_username) < 3:
            base_username = google_email.split("@")[0][:15]
        username = base_username + str(secrets.randbelow(1000))

        # Generate a random password (user won't need it for Google login)
        random_password = secrets.token_urlsafe(16)

        uid, err = db.create_user(username, google_email, random_password)
        if err:
            # Email might already exist with different case, or username collision
            flash(f"Could not create account: {err}", "danger")
            return redirect(url_for("auth.login"))

        session.permanent = True
        session["user_id"] = uid
        session["sid"] = secrets.token_urlsafe(16)
        device = request.headers.get("User-Agent", "")[:100]
        db.register_session(uid, session["sid"], device)
        session["needs_setup"] = True
        return redirect(url_for("account.account"))
