"""Dashboard routes — user dashboard, study session API."""

from flask import Blueprint, render_template, request, jsonify
from curriculum_data import TOPICS, LEVELS_ORDER
import database as db
from routes.helpers import current_user, login_required, get_accessible_levels

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    user = current_user()
    data = db.get_dashboard_data(user["id"])
    enabled = get_accessible_levels(user)

    for lst_name in ("best_topics", "worst_topics"):
        enriched = []
        for tid, score, total in data[lst_name]:
            t = TOPICS.get(tid)
            if t:
                enriched.append({"tid": tid, "name": t["name"], "emoji": t["emoji"],
                                 "score": score, "total": total,
                                 "pct": round(score / total * 100) if total else 0})
        data[lst_name] = enriched

    for act in data["recent_activity"]:
        t = TOPICS.get(act.get("topic_id", ""))
        act["topic_name"] = t["name"] if t else act.get("topic_id", "")
        act["topic_emoji"] = t["emoji"] if t else ""

    for s in data["study_by_topic"]:
        t = TOPICS.get(s["topic_id"])
        s["name"] = t["name"] if t else s["topic_id"]
        s["emoji"] = t["emoji"] if t else ""

    total_s = data["study_total_s"]
    data["study_hours"] = total_s // 3600
    data["study_minutes"] = (total_s % 3600) // 60

    new_achievements = db.check_and_grant_achievements(user["id"])
    if new_achievements:
        data["achievements"] = db.get_user_achievements(user["id"])

    # Exam progress
    from exam_config import EXAMS, EXAM_ORDER
    exam_status = db.get_all_exam_status(user["id"])
    exams_passed = sum(1 for eid in EXAM_ORDER if exam_status.get(eid, {}).get("passed"))
    exams_total = len(EXAM_ORDER)

    return render_template("pages/dashboard.html",
                           user=user, data=data, topics=TOPICS,
                           total_topics=len(TOPICS), enabled_levels=enabled,
                           levels_order=LEVELS_ORDER,
                           new_achievements=new_achievements,
                           exams_passed=exams_passed, exams_total=exams_total)


@dashboard_bp.route("/api/dashboard/heatmap")
@login_required
def api_heatmap():
    user = current_user()
    return jsonify({"heatmap": db.get_activity_heatmap(user["id"])})


@dashboard_bp.route("/api/study/start", methods=["POST"])
@login_required
def api_start_study():
    user = current_user()
    data = request.get_json()
    tid = data.get("topic_id")
    if not tid:
        return jsonify({"error": "topic_id required"}), 400
    sid = db.start_study_session(user["id"], tid)
    db.log_activity(user["id"], "lesson_view", topic_id=tid)
    return jsonify({"ok": True, "session_id": sid})


@dashboard_bp.route("/api/study/end", methods=["POST"])
@login_required
def api_end_study():
    data = request.get_json()
    sid = data.get("session_id")
    if sid:
        db.end_study_session(sid)
    return jsonify({"ok": True})
