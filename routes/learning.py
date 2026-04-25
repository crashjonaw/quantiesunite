"""Learning routes — index, curriculum, graph, topic, concept, quiz, practice,
mindmap, progress, trophies, search, feedback, API endpoints."""

import csv
import os
import re
from datetime import datetime
from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from curriculum_data import (TOPICS, LEVELS_ORDER, LEVEL_DESCRIPTIONS,
                             LEVEL_TROPHY_NAMES, get_graph_data, get_topic, get_unlocked_by)
from lesson_content import get_lesson_content, get_quiz, get_concept
import database as db
from routes.helpers import (current_user, login_required, get_enabled_levels,
                            get_accessible_levels, is_unlocked, user_progress)

learning_bp = Blueprint("learning", __name__)


# ════════════════════════════════════════════════════════════════════
# MAIN PAGES
# ════════════════════════════════════════════════════════════════════

@learning_bp.route("/")
def index():
    user = current_user()
    if user:
        progress = db.get_progress(user["id"])
        total = len(TOPICS)
        done  = sum(1 for v in progress.values() if v.get("complete"))
        enabled = get_accessible_levels(user)
        accessible = sum(1 for t in TOPICS.values() if t["level"] in enabled)
    else:
        done = total = accessible = 0
    return render_template("pages/index.html",
                           total=len(TOPICS), done=done,
                           percent=round(done / len(TOPICS) * 100) if done else 0,
                           user=user, accessible=accessible)


TRIAL_TOPICS = ["k_numbers", "p12_whole_1000", "sec12_algebra", "alevel_functions"]


@learning_bp.route("/about")
def about_page():
    return render_template("pages/about.html")


@learning_bp.route("/trial")
def trial_page():
    trials = []
    for tid in TRIAL_TOPICS:
        t = TOPICS.get(tid)
        if t:
            trials.append({"id": tid, **t})
    return render_template("pages/trial.html", trials=trials)


@learning_bp.route("/plans")
def plans_page():
    from datetime import datetime
    promo_active = datetime.now().year <= 2026
    return render_template("pages/plans.html", promo_active=promo_active)


@learning_bp.route("/payment/success")
def payment_success():
    # HitPay may use "status" or "payment_status", "reference" or "reference_number"
    status = request.args.get("status", "") or request.args.get("payment_status", "")
    reference = (request.args.get("reference", "") or
                 request.args.get("reference_number", ""))

    # Fallback activation: if webhook missed, activate from redirect params
    user = current_user()
    if user and reference:
        parts = reference.split("|")
        if len(parts) == 3:
            try:
                uid, tier, duration = int(parts[0]), parts[1], parts[2]
                if uid == user["id"]:
                    existing = db.get_active_plan(uid)
                    if not existing or existing["plan_tier"] != tier:
                        from routes.payments import PLAN_PRICES
                        amount = PLAN_PRICES.get(tier, {}).get(duration, 0)
                        db.activate_plan(uid, tier, duration, amount,
                                         payment_ref="redirect_fallback",
                                         activated_by="redirect_check")
                        status = "completed"
            except (ValueError, KeyError):
                pass

    # Second fallback: always check HitPay API for recent completed payments
    if user and status != "completed":
        try:
            from routes.payments import _check_recent_completed_payment
            import logging
            logging.warning(f"Running API fallback for user {user['id']}")
            activated = _check_recent_completed_payment(user["id"])
            logging.warning(f"API fallback result: {activated}")
            if activated:
                status = "completed"
        except Exception as e:
            import logging
            logging.error(f"API fallback FAILED: {e}", exc_info=True)

    return render_template("pages/payment_success.html",
                           payment_status=status, reference=reference)


@learning_bp.route("/graph")
def graph_page():
    return render_template("pages/graph.html")


@learning_bp.route("/api/graph")
def api_graph():
    user = current_user()
    progress = db.get_progress(user["id"]) if user else {}
    is_admin = bool(user and user.get("is_admin"))
    enabled = set(LEVELS_ORDER) if is_admin else (
              get_accessible_levels(user) if user else set(db.PLAN_LEVELS["free"]))
    targets = db.get_targets(user["id"]) if user else []
    data = get_graph_data()
    for node in data["nodes"]:
        tid = node["id"]
        t = TOPICS.get(tid, {})
        node["complete"]   = is_admin or bool(progress.get(tid, {}).get("complete"))
        node["unlocked"]   = is_admin or is_unlocked(tid, progress)
        node["accessible"] = is_admin or (t.get("level", "") in enabled)
        node["quiz_score"] = progress.get(tid, {}).get("quiz_score")
        node["quiz_total"] = progress.get(tid, {}).get("quiz_total")
    data["targets"] = targets
    return jsonify(data)


@learning_bp.route("/curriculum")
@login_required
def curriculum():
    user = current_user()
    progress = db.get_progress(user["id"]) if user else {}
    enabled = get_accessible_levels(user) if user else set(db.PLAN_LEVELS["free"])
    levels = {}
    for level in LEVELS_ORDER:
        topics_in_level = {k: v for k, v in TOPICS.items() if v["level"] == level}
        levels[level] = {
            "desc": LEVEL_DESCRIPTIONS.get(level, ""),
            "topics": topics_in_level,
            "total": len(topics_in_level),
            "done": sum(1 for k in topics_in_level if progress.get(k, {}).get("complete")),
            "accessible": level in enabled,
        }
    return render_template("pages/curriculum.html", levels=levels,
                           levels_order=LEVELS_ORDER, progress=progress,
                           enabled_levels=enabled)


@learning_bp.route("/search")
@login_required
def search():
    user = current_user()
    q = request.args.get("q", "").lower()
    enabled = get_accessible_levels(user) if user else set(db.PLAN_LEVELS["free"])
    results = []
    if q:
        for tid, t in TOPICS.items():
            if q in t["name"].lower() or q in t["level"].lower() or q in t["tagline"].lower():
                results.append({"id": tid, **t, "accessible": t["level"] in enabled})
    return render_template("pages/search.html", query=q, results=results)


# ════════════════════════════════════════════════════════════════════
# TOPIC / CONCEPT / QUIZ / PRACTICE / MINDMAP
# ════════════════════════════════════════════════════════════════════

@learning_bp.route("/topic/<tid>")
@login_required
def topic(tid):
    user = current_user()
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    enabled = get_accessible_levels(user)
    level_accessible = is_admin or (t["level"] in enabled)
    progress = db.get_progress(user["id"]) if user else {}
    unlocked = is_admin or is_unlocked(tid, progress)
    prereq_topics  = {p: TOPICS[p] for p in t["prereqs"] if p in TOPICS}
    unlocks_topics = {u: TOPICS[u] for u in get_unlocked_by(tid) if u in TOPICS}
    content = get_lesson_content(tid)
    complete = bool(progress.get(tid, {}).get("complete"))
    quiz_score = progress.get(tid, {}).get("quiz_score")
    quiz_total = progress.get(tid, {}).get("quiz_total")
    targets = db.get_targets(user["id"]) if user else []
    is_target = tid in targets
    if content and content.get("type") == "concepts" and content.get("concepts") and unlocked and level_accessible:
        return redirect(url_for("learning.concept_page", tid=tid, concept_id=content["concepts"][0]["id"]))
    return render_template("topic.html", tid=tid, t=t, content=content,
                           unlocked=unlocked, level_accessible=level_accessible,
                           prereq_topics=prereq_topics, unlocks_topics=unlocks_topics,
                           complete=complete, quiz_score=quiz_score, quiz_total=quiz_total,
                           is_target=is_target, progress=progress)


@learning_bp.route("/topic/<tid>/overview")
def topic_overview(tid):
    user = current_user()
    is_trial = tid in TRIAL_TOPICS
    if not user and not is_trial:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("auth.login", next=request.path))
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    enabled = get_accessible_levels(user) if user else set()
    level_accessible = is_admin or is_trial or (t["level"] in enabled)
    progress = db.get_progress(user["id"]) if user else {}
    unlocked = is_admin or is_trial or is_unlocked(tid, progress)
    prereq_topics  = {p: TOPICS[p] for p in t["prereqs"] if p in TOPICS}
    unlocks_topics = {u: TOPICS[u] for u in get_unlocked_by(tid) if u in TOPICS}
    content = get_lesson_content(tid)
    complete = bool(progress.get(tid, {}).get("complete"))
    quiz_score = progress.get(tid, {}).get("quiz_score")
    quiz_total = progress.get(tid, {}).get("quiz_total")
    targets = db.get_targets(user["id"]) if user else []
    is_target = tid in targets
    return render_template("topic.html", tid=tid, t=t, content=content,
                           unlocked=unlocked, level_accessible=level_accessible,
                           prereq_topics=prereq_topics, unlocks_topics=unlocks_topics,
                           complete=complete, quiz_score=quiz_score, quiz_total=quiz_total,
                           is_target=is_target, progress=progress)


@learning_bp.route("/topic/<tid>/learn/<concept_id>")
def concept_page(tid, concept_id):
    user = current_user()
    is_trial = tid in TRIAL_TOPICS
    if not user and not is_trial:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("auth.login", next=request.path))
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    enabled = get_accessible_levels(user) if user else set()
    level_accessible = is_admin or is_trial or (t["level"] in enabled)
    progress = db.get_progress(user["id"]) if user else {}
    unlocked = is_admin or is_trial or is_unlocked(tid, progress)
    complete = bool(progress.get(tid, {}).get("complete"))
    quiz_score = progress.get(tid, {}).get("quiz_score")
    quiz_total = progress.get(tid, {}).get("quiz_total")
    if not level_accessible or not unlocked:
        flash("Complete the prerequisite topics first to unlock this lesson.", "warning")
        return redirect(url_for("learning.topic_overview", tid=tid))
    content = get_lesson_content(tid)
    concept = get_concept(tid, concept_id)
    if not concept:
        return redirect(url_for("learning.topic_overview", tid=tid))
    concepts = content.get("concepts", []) if content else []
    concept_ids = [c["id"] for c in concepts]
    cur_idx = concept_ids.index(concept_id) if concept_id in concept_ids else 0
    prev_concept = concepts[cur_idx - 1] if cur_idx > 0 else None
    next_concept = concepts[cur_idx + 1] if cur_idx < len(concepts) - 1 else None
    return render_template("concept.html", tid=tid, t=t, concept=concept,
                           concepts=concepts, cur_idx=cur_idx,
                           prev_concept=prev_concept, next_concept=next_concept,
                           unlocked=unlocked, level_accessible=level_accessible,
                           complete=complete, quiz_score=quiz_score, quiz_total=quiz_total)


@learning_bp.route("/topic/<tid>/mindmap")
@login_required
def mindmap_page(tid):
    user = current_user()
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    enabled = get_accessible_levels(user)
    if not is_admin and t["level"] not in enabled:
        flash("This content requires a paid plan. Upgrade to access it.", "warning")
        return redirect(url_for("learning.plans_page"))
    progress = db.get_progress(user["id"])
    complete = bool(progress.get(tid, {}).get("complete"))
    if not is_admin and not complete:
        flash("Complete this module first to unlock the mindmap.", "warning")
        return redirect(url_for("learning.topic", tid=tid))
    from mindmap_data import get_mindmap
    return render_template("mindmap.html", tid=tid, t=t, mindmap=get_mindmap(tid))


@learning_bp.route("/topic/<tid>/quiz")
def quiz_page(tid):
    user = current_user()
    is_trial = tid in TRIAL_TOPICS
    if not user and not is_trial:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("auth.login", next=request.path))
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    if user:
        enabled = get_accessible_levels(user)
        if not is_admin and not is_trial and t["level"] not in enabled:
            flash("This content requires a paid plan. Upgrade to access it.", "warning")
            return redirect(url_for("learning.plans_page"))
        progress = db.get_progress(user["id"])
        if not is_admin and not is_trial and not is_unlocked(tid, progress):
            flash("Complete the prerequisite topics first to unlock this quiz.", "warning")
            return redirect(url_for("learning.topic_overview", tid=tid))
        wrong_ids = db.get_wrong_question_ids(user["id"], tid)
        quiz = get_quiz(tid, must_include_ids=wrong_ids if wrong_ids else None)
    else:
        quiz = get_quiz(tid)
    return render_template("quiz.html", tid=tid, t=t, quiz=quiz, is_trial=is_trial)


@learning_bp.route("/topic/<tid>/practice")
@login_required
def practice_page(tid):
    user = current_user()
    t = get_topic(tid)
    if not t:
        return render_template("404.html"), 404
    is_admin = bool(user and user.get("is_admin"))
    enabled = get_accessible_levels(user)
    if not is_admin and t["level"] not in enabled:
        flash("This content requires a paid plan. Upgrade to access it.", "warning")
        return redirect(url_for("learning.plans_page"))
    # Must pass the module quiz first
    progress = db.get_progress(user["id"])
    if not is_admin and not progress.get(tid, {}).get("complete"):
        flash("Pass the module quiz first to unlock More Practice.", "warning")
        return redirect(url_for("learning.quiz_page", tid=tid))
    stats = db.get_practice_stats(user["id"], tid)
    if not stats or stats["total_in_bank"] == 0:
        flash("No questions available for practice in this topic.", "info")
        return redirect(url_for("learning.topic", tid=tid))
    quiz = db.sample_practice_quiz(tid, user["id"], n=10)
    return render_template("quiz.html", tid=tid, t=t, quiz=quiz,
                           is_practice=True, practice_stats=stats)


# ════════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ════════════════════════════════════════════════════════════════════

@learning_bp.route("/api/quiz/submit", methods=["POST"])
def submit_quiz():
    user = current_user()
    data = request.get_json()
    tid = data.get("tid")
    answers = data.get("answers", {})
    quiz_qs = data.get("questions", [])
    is_trial = tid in TRIAL_TOPICS

    if not user and not is_trial:
        return jsonify({"error": "Login required"}), 401
    if not quiz_qs:
        return jsonify({"error": "No questions submitted"}), 400

    q_ids = [q["id"] for q in quiz_qs]
    db_questions = {}
    if q_ids and q_ids[0] > 0:
        db_questions = {q["id"]: q for q in db.get_all_questions(tid)}

    score, results, attempt_answers = 0, [], []
    for q in quiz_qs:
        qid = q["id"]
        user_ans = answers.get(str(qid), "").strip().lower()
        ref = db_questions.get(qid, q)
        correct = str(ref["answer"]).strip().lower()
        ok = (user_ans == correct)
        if ok:
            score += 1
        results.append({"question_id": qid, "question": ref["question"],
                        "user": answers.get(str(qid), ""),
                        "correct_answer": ref["answer"], "correct": ok,
                        "explanation": ref.get("explanation", "")})
        attempt_answers.append({"qid": qid, "user": answers.get(str(qid), ""), "correct": ok})

    total = len(quiz_qs)
    passed = score >= total * 0.7

    # Only record progress for logged-in users
    if user:
        db.save_quiz_score(user["id"], tid, score, total)
        if passed:
            db.mark_topic_complete(user["id"], tid)
        db.save_quiz_attempt(user["id"], tid, q_ids, attempt_answers, score, total, passed)
        db.log_activity(user["id"], "quiz_attempt", topic_id=tid,
                        detail=f"{score}/{total}", points=2)
        if passed:
            db.log_activity(user["id"], "quiz_pass", topic_id=tid,
                            detail=f"{score}/{total}", points=5)
        if score == total:
            db.log_activity(user["id"], "quiz_perfect", topic_id=tid, points=10)
            db.grant_achievement(user["id"], "first_perfect")
        if db.get_attempt_count(user["id"], tid) == 1:
            db.grant_achievement(user["id"], "first_quiz")
        if passed:
            db.grant_achievement(user["id"], "first_pass")
        db.check_and_grant_achievements(user["id"])

    if user:
        attempt_num = db.get_attempt_count(user["id"], tid)
    else:
        attempt_num = 1  # trial users always see attempt 1

    # Trial users always see answers; logged-in users after 3 attempts
    show_answers = (not user) or (attempt_num >= 3)
    if not show_answers:
        for r in results:
            r.pop("correct_answer", None)
            r.pop("explanation", None)

    return jsonify({"score": score, "total": total, "results": results,
                    "passed": passed, "attempt": attempt_num,
                    "show_answers": show_answers})


@learning_bp.route("/api/complete/<tid>", methods=["POST"])
@login_required
def api_complete(tid):
    user = current_user()
    db.mark_topic_complete(user["id"], tid)
    db.log_activity(user["id"], "topic_complete", topic_id=tid, points=10)
    db.check_and_grant_achievements(user["id"])
    return jsonify({"ok": True})


@learning_bp.route("/api/targets", methods=["GET"])
@login_required
def get_targets():
    return jsonify({"targets": db.get_targets(current_user()["id"])})


@learning_bp.route("/api/targets/add", methods=["POST"])
@login_required
def add_target():
    user = current_user()
    data = request.get_json()
    tid = data.get("topic_id")
    if tid not in TOPICS:
        return jsonify({"ok": False, "error": "Invalid topic"}), 400
    db.add_target(user["id"], tid)
    return jsonify({"ok": True})


@learning_bp.route("/api/targets/remove", methods=["POST"])
@login_required
def remove_target():
    user = current_user()
    data = request.get_json()
    db.remove_target(user["id"], data.get("topic_id"))
    return jsonify({"ok": True})


@learning_bp.route("/api/reset", methods=["POST"])
@login_required
def reset_progress():
    db.reset_progress(current_user()["id"])
    flash("Progress reset.", "info")
    return jsonify({"ok": True})


# ════════════════════════════════════════════════════════════════════
# PROGRESS & TROPHIES
# ════════════════════════════════════════════════════════════════════

@learning_bp.route("/progress")
@login_required
def progress_page():
    user = current_user()
    progress = db.get_progress(user["id"])
    total = len(TOPICS)
    done = sum(1 for v in progress.values() if v.get("complete"))
    enabled = get_accessible_levels(user)
    level_stats = {}
    for level in LEVELS_ORDER:
        topics_in_level = [k for k, v in TOPICS.items() if v["level"] == level]
        level_stats[level] = {
            "done": sum(1 for k in topics_in_level if progress.get(k, {}).get("complete")),
            "total": len(topics_in_level), "accessible": level in enabled}
    targets = db.get_targets(user["id"])
    target_data = []
    for target_tid in targets:
        t = TOPICS.get(target_tid)
        if not t:
            continue
        all_prereqs, visited, queue = [], set(), list(t["prereqs"])
        while queue:
            pid = queue.pop(0)
            if pid in visited:
                continue
            visited.add(pid)
            pt = TOPICS.get(pid)
            if pt:
                all_prereqs.append(pid)
                queue.extend(pt["prereqs"])
        all_topics = all_prereqs + [target_tid]
        topic_details = []
        for tid2 in all_topics:
            t2 = TOPICS.get(tid2)
            if t2:
                topic_details.append({"id": tid2, "name": t2["name"], "emoji": t2["emoji"],
                                      "level": t2["level"],
                                      "complete": bool(progress.get(tid2, {}).get("complete")),
                                      "is_target": tid2 == target_tid})
        target_data.append({"tid": target_tid, "name": t["name"], "emoji": t["emoji"],
                            "level": t["level"],
                            "done": sum(1 for tid2 in all_topics if progress.get(tid2, {}).get("complete")),
                            "total": len(all_topics), "topics": topic_details})
    # Exam status for level gates
    from exam_config import EXAMS, EXAM_ORDER, get_exam_from_level
    exam_status = db.get_all_exam_status(user["id"])
    exam_gates = []
    for eid in EXAM_ORDER:
        exam = EXAMS[eid]
        status = exam_status.get(eid, {})
        exam_gates.append({
            "id": eid, "name": exam["name"], "emoji": exam["emoji"],
            "from_level": exam["from_level"],
            "unlocks_level": exam["unlocks_level"],
            "passed": status.get("passed", False),
            "best_score": status.get("best_score"),
            "total": status.get("total"),
            "attempts": status.get("attempts", 0),
            "color": exam["color"],
        })

    return render_template("pages/progress.html", progress=progress, topics=TOPICS,
                           total=total, done=done, level_stats=level_stats,
                           levels_order=LEVELS_ORDER, target_data=target_data,
                           exam_gates=exam_gates)


@learning_bp.route("/trophies")
@login_required
def trophies_page():
    user = current_user()
    progress = db.get_progress(user["id"])
    quiz_medals = []
    for tid, t in TOPICS.items():
        p = progress.get(tid, {})
        score, total = p.get("quiz_score"), p.get("quiz_total")
        if score is not None and total and total > 0:
            pct = score / total * 100
            medal = "gold" if pct >= 100 else ("silver" if pct >= 90 else ("bronze" if pct >= 70 else None))
            if medal:
                quiz_medals.append({"tid": tid, "name": t["name"], "emoji": t["emoji"],
                                    "level": t["level"], "score": score, "total": total,
                                    "pct": round(pct), "medal": medal})
    level_trophies = []
    for level in LEVELS_ORDER:
        topics_in_level = [k for k, v in TOPICS.items() if v["level"] == level]
        done = sum(1 for k in topics_in_level if progress.get(k, {}).get("complete"))
        trophy_info = LEVEL_TROPHY_NAMES.get(level, {"name": level, "emoji": "🏆"})
        level_trophies.append({"level": level, "name": trophy_info["name"],
                               "emoji": trophy_info["emoji"], "done": done,
                               "total": len(topics_in_level),
                               "earned": done == len(topics_in_level) and len(topics_in_level) > 0})
    total_topics = len(TOPICS)
    total_done = sum(1 for v in progress.values() if v.get("complete"))
    milestones = [
        {"name": "First Steps", "emoji": "👣", "desc": "Complete your first module", "threshold": 1},
        {"name": "Warm Up", "emoji": "🔥", "desc": "Complete 3 modules", "threshold": 3},
        {"name": "Getting Started", "emoji": "🚀", "desc": "Complete 5 modules", "threshold": 5},
        {"name": "Double Digits", "emoji": "🔟", "desc": "Complete 10 modules", "threshold": 10},
        {"name": "Steady Learner", "emoji": "📖", "desc": "Complete 15 modules", "threshold": 15},
        {"name": "On a Roll", "emoji": "🎯", "desc": "Complete 20 modules", "threshold": 20},
        {"name": "Quarter Way", "emoji": "🌱", "desc": "Complete 25% of all modules", "threshold": total_topics // 4},
        {"name": "Rising Star", "emoji": "💫", "desc": "Complete 30 modules", "threshold": 30},
        {"name": "Knowledge Builder", "emoji": "🧱", "desc": "Complete 40 modules", "threshold": 40},
        {"name": "Halfway Hero", "emoji": "⭐", "desc": "Complete 50% of all modules", "threshold": total_topics // 2},
        {"name": "Momentum", "emoji": "⚡", "desc": "Complete 60 modules", "threshold": 60},
        {"name": "Deep Thinker", "emoji": "🧠", "desc": "Complete 70 modules", "threshold": 70},
        {"name": "Almost There", "emoji": "🏔️", "desc": "Complete 75% of all modules", "threshold": (total_topics * 3) // 4},
        {"name": "Final Stretch", "emoji": "🏃", "desc": "Complete 85 modules", "threshold": 85},
        {"name": "On the Doorstep", "emoji": "🚪", "desc": "Complete 95 modules", "threshold": 95},
        {"name": "QuantiesUnite Master", "emoji": "👑", "desc": "Complete every single module", "threshold": total_topics},
    ]
    for m in milestones:
        m["earned"] = total_done >= m["threshold"]
        m["progress"] = min(total_done, m["threshold"])
    # Exam trophies
    from exam_config import EXAMS, EXAM_ORDER
    exam_status = db.get_all_exam_status(user["id"])
    exam_trophies = []
    for eid in EXAM_ORDER:
        exam = EXAMS[eid]
        status = exam_status.get(eid, {})
        passed = status.get("passed", False)
        best = status.get("best_score")
        total_q = status.get("total")
        pct = round(best / total_q * 100) if best and total_q else 0
        exam_trophies.append({
            "id": eid, "name": exam["name"], "emoji": exam["emoji"],
            "color": exam["color"], "passed": passed,
            "best_score": best, "total": total_q, "pct": pct,
            "attempts": status.get("attempts", 0),
        })
    exams_passed = sum(1 for et in exam_trophies if et["passed"])

    return render_template("pages/trophies.html", quiz_medals=quiz_medals,
                           level_trophies=level_trophies, milestones=milestones,
                           gold_count=sum(1 for m in quiz_medals if m["medal"] == "gold"),
                           silver_count=sum(1 for m in quiz_medals if m["medal"] == "silver"),
                           bronze_count=sum(1 for m in quiz_medals if m["medal"] == "bronze"),
                           levels_earned=sum(1 for lt in level_trophies if lt["earned"]),
                           milestones_earned=sum(1 for m in milestones if m["earned"]),
                           total_done=total_done, total_topics=total_topics,
                           exam_trophies=exam_trophies, exams_passed=exams_passed)


# ════════════════════════════════════════════════════════════════════
# FEEDBACK
# ════════════════════════════════════════════════════════════════════

FEEDBACK_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "update", "feedback.csv")
FEEDBACK_COLUMNS = [
    "#", "user", "page_link", "module", "topic", "title", "description",
    "priority", "category", "theme", "submitted_at", "fix_summary", "fixed?",
    "fixed_at", "fixed_by",
]

def _ensure_feedback_csv():
    os.makedirs(os.path.dirname(FEEDBACK_CSV), exist_ok=True)
    if not os.path.exists(FEEDBACK_CSV):
        with open(FEEDBACK_CSV, "w", newline="") as f:
            csv.writer(f).writerow(FEEDBACK_COLUMNS)

def _next_feedback_id():
    try:
        with open(FEEDBACK_CSV, "r") as f:
            return sum(1 for _ in csv.reader(f))
    except FileNotFoundError:
        return 1

def _extract_module_topic(page_url):
    m = re.match(r"/topic/([^/]+)", page_url)
    if m:
        tid = m.group(1)
        t = TOPICS.get(tid)
        return tid, t["name"] if t else tid
    return "", ""


@learning_bp.route("/api/feedback", methods=["POST"])
@login_required
def submit_feedback():
    user = current_user()
    data = request.get_json()
    description = (data.get("description") or "").strip()
    page_url = (data.get("page_url") or "").strip()
    theme = (data.get("theme") or "").strip()
    category = (data.get("category") or "General").strip()
    if not description:
        return jsonify({"ok": False, "error": "Description is required."}), 400
    title = description[:60] + ("..." if len(description) > 60 else "")
    _ensure_feedback_csv()
    fb_id = _next_feedback_id()
    module_id, topic_name = _extract_module_topic(page_url)
    row = [fb_id, user["username"], page_url, module_id, topic_name, title,
           description, "", category, theme or "",
           datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "", "no", "", ""]
    with open(FEEDBACK_CSV, "a", newline="") as f:
        csv.writer(f).writerow(row)
    return jsonify({"ok": True, "id": fb_id})
