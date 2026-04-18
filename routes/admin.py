"""Admin routes — panel, analytics dashboard, user management, violations."""

from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from curriculum_data import TOPICS, LEVELS_ORDER
import database as db
from routes.helpers import current_user, login_required, admin_required, get_enabled_levels

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@login_required
@admin_required
def admin_panel():
    users = db.all_users()
    stats = db.site_stats()
    # Attach plan info to each user
    for u in users:
        u["all_plans"] = db.get_all_active_plans_for_user(u["id"])
        u["current_level"] = u.get("current_level") or "Not set"
    return render_template("admin/admin.html", users=users, stats=stats,
                           total_topics=len(TOPICS), levels_order=LEVELS_ORDER)


@admin_bp.route("/admin/dashboard")
@login_required
@admin_required
def admin_dashboard():
    data = db.admin_get_full_dashboard()
    for t in data["top_topics"]:
        topic = TOPICS.get(t["topic_id"])
        t["name"] = topic["name"] if topic else t["topic_id"]
        t["emoji"] = topic["emoji"] if topic else ""
        t["level"] = topic["level"] if topic else ""
    for fu in data["flagged_users"]:
        types = (fu.get("violation_types") or "").split(",")
        fu["violation_labels"] = [
            db.VIOLATION_TYPES.get(vt.strip(), {}).get("name", vt.strip())
            for vt in types if vt.strip()]
    return render_template("admin/admin_dashboard.html", data=data,
                           total_topics=len(TOPICS),
                           total_users=data["overview"]["total_users"])


@admin_bp.route("/api/admin/violation/<int:vid>/resolve", methods=["POST"])
@login_required
@admin_required
def resolve_violation(vid):
    db.resolve_violation(vid, resolved_by=current_user()["username"])
    return jsonify({"ok": True})


@admin_bp.route("/api/admin/user/<int:uid>/resolve-all", methods=["POST"])
@login_required
@admin_required
def resolve_all_violations(uid):
    db.resolve_all_user_violations(uid, resolved_by=current_user()["username"])
    return jsonify({"ok": True})


@admin_bp.route("/api/admin/user/<int:uid>/flag", methods=["POST"])
@login_required
@admin_required
def flag_user(uid):
    data = request.get_json()
    db.log_violation(uid, "manual_flag",
                     detail=data.get("detail", "Manually flagged by admin"),
                     severity="info")
    return jsonify({"ok": True})


@admin_bp.route("/api/admin/user/<int:uid>/activate-plan", methods=["POST"])
@login_required
@admin_required
def activate_user_plan(uid):
    data = request.get_json()
    tier = data.get("tier", "primary")
    duration = data.get("duration", "1_month")
    amount = data.get("amount", 0)
    payment_ref = data.get("payment_ref", "")
    db.activate_plan(uid, tier, duration, amount,
                     payment_ref=payment_ref,
                     activated_by=current_user()["username"])
    return jsonify({"ok": True})


@admin_bp.route("/admin/toggle-admin/<int:uid>", methods=["POST"])
@login_required
@admin_required
def admin_toggle(uid):
    if uid == session["user_id"]:
        flash("You cannot remove your own admin rights.", "warning")
    else:
        db.toggle_admin(uid)
        flash("Admin status toggled.", "success")
    return redirect(url_for("admin.admin_panel"))


@admin_bp.route("/admin/delete-user/<int:uid>", methods=["POST"])
@login_required
@admin_required
def admin_delete_user(uid):
    if uid == session["user_id"]:
        flash("You cannot delete your own account here.", "warning")
    else:
        db.delete_user(uid)
        flash("User deleted.", "success")
    return redirect(url_for("admin.admin_panel"))


@admin_bp.route("/admin/user/<int:uid>")
@login_required
@admin_required
def admin_user_detail(uid):
    user = db.get_user_by_id(uid)
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("admin.admin_panel"))
    progress_rows = db.get_user_full_progress(uid)
    progress = {r["topic_id"]: r for r in progress_rows}
    level_breakdown = {}
    for level in LEVELS_ORDER:
        topics_in_level = {k: v for k, v in TOPICS.items() if v["level"] == level}
        level_topics = []
        for tid, t in topics_in_level.items():
            p = progress.get(tid, {})
            level_topics.append({"id": tid, "name": t["name"], "emoji": t["emoji"],
                                 "complete": bool(p.get("complete")),
                                 "quiz_score": p.get("quiz_score"),
                                 "quiz_total": p.get("quiz_total"),
                                 "completed_at": p.get("completed_at")})
        done = sum(1 for t in level_topics if t["complete"])
        total = len(level_topics)
        level_breakdown[level] = {"topics": level_topics, "done": done, "total": total,
                                  "pct": round(done / total * 100) if total else 0}
    all_plans = db.get_all_active_plans_for_user(uid)
    return render_template("admin/admin_user.html", u=user,
                           level_breakdown=level_breakdown, levels_order=LEVELS_ORDER,
                           total_done=sum(1 for r in progress_rows if r["complete"]),
                           total_all=len(TOPICS),
                           enabled_levels=get_enabled_levels(user["target_level"]),
                           all_plans=all_plans)


@admin_bp.route("/api/admin/quiz-stats/<tid>")
@login_required
@admin_required
def quiz_stats_api(tid):
    stats = db.get_question_stats(tid)
    total = db.get_question_count(tid)
    return jsonify({"topic_id": tid, "total_questions": total, "stats": stats})
