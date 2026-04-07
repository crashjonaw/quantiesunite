"""Exam routes — exam listing, taking exams, submitting, results."""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from curriculum_data import TOPICS, LEVELS_ORDER
from exam_config import EXAMS, EXAM_ORDER, get_review_modules, get_exam_params
import database as db
from routes.helpers import current_user, login_required, get_enabled_levels

exam_bp = Blueprint("exam", __name__)


@exam_bp.route("/exams")
@login_required
def exam_list():
    user = current_user()
    progress = db.get_progress(user["id"])
    exam_status = db.get_all_exam_status(user["id"])
    enabled = get_enabled_levels(user["target_level"])
    is_admin = bool(user.get("is_admin"))

    exams = []
    for eid in EXAM_ORDER:
        exam = EXAMS[eid]
        status = exam_status.get(eid, {})
        passed = status.get("passed", False)

        # Check if all modules in the grade are completed
        grade_complete = all(
            progress.get(tid, {}).get("complete")
            for tid in exam["grade_modules"]
        )

        # Exam is accessible if all grade modules are done (or admin)
        accessible = is_admin or grade_complete
        # Level must also be enabled
        level_ok = is_admin or exam["from_level"] in enabled

        exams.append({
            "id": eid,
            **exam,
            "passed": passed,
            "attempts": status.get("attempts", 0),
            "best_score": status.get("best_score"),
            "best_total": status.get("total"),
            "accessible": accessible and level_ok,
            "grade_complete": grade_complete,
            "grade_done": sum(1 for tid in exam["grade_modules"]
                             if progress.get(tid, {}).get("complete")),
            "grade_total": len(exam["grade_modules"]),
        })

    return render_template("pages/exams.html", exams=exams, user=user)


@exam_bp.route("/exam/<exam_id>")
@login_required
def take_exam(exam_id):
    user = current_user()
    if exam_id not in EXAMS:
        return render_template("404.html"), 404

    exam = EXAMS[exam_id]
    is_admin = bool(user.get("is_admin"))
    progress = db.get_progress(user["id"])
    enabled = get_enabled_levels(user["target_level"])

    # Check access
    if not is_admin:
        grade_complete = all(
            progress.get(tid, {}).get("complete")
            for tid in exam["grade_modules"]
        )
        if not grade_complete:
            flash("Complete all modules in this grade before taking the exam.", "warning")
            return redirect(url_for("exam.exam_list"))
        if exam["from_level"] not in enabled:
            flash("Enable this level in your account settings first.", "warning")
            return redirect(url_for("exam.exam_list"))

    # Determine timed or untimed mode
    timed = request.args.get("mode", "timed") == "timed"
    total_q, grade_q, review_q, time_limit = get_exam_params(exam_id, timed=timed)

    # Admin gets no review questions — grade only
    if is_admin:
        grade_q = total_q
        review_q = 0

    # Get wrong/seen questions for smart sampling
    wrong_ids = db.get_exam_wrong_question_ids(user["id"], exam_id)
    seen_ids = db.get_exam_seen_question_ids(user["id"], exam_id)

    # Sample questions — prioritizes wrong, then unseen, then recycles
    review_modules = get_review_modules(exam_id) if review_q > 0 else []
    questions = db.sample_exam_questions(
        exam["grade_modules"], grade_q,
        review_modules, review_q,
        must_include_ids=wrong_ids if wrong_ids else None,
        seen_ids=seen_ids if seen_ids else None,
    )

    if len(questions) < total_q // 2:
        flash("Not enough exam questions available yet. Please try again later.", "info")
        return redirect(url_for("exam.exam_list"))

    return render_template("pages/exam_take.html",
                           exam_id=exam_id, exam=exam, quiz=questions,
                           timed=timed, time_limit_min=time_limit,
                           total_expected=total_q)


@exam_bp.route("/api/exam/submit", methods=["POST"])
@login_required
def submit_exam():
    user = current_user()
    data = request.get_json()
    exam_id = data.get("exam_id")
    answers = data.get("answers", {})
    quiz_qs = data.get("questions", [])

    if exam_id not in EXAMS or not quiz_qs:
        return jsonify({"error": "Invalid exam submission"}), 400

    exam = EXAMS[exam_id]

    # Fetch correct answers from exam_questions table
    q_ids = [q["id"] for q in quiz_qs]
    db_questions = {}
    if q_ids:
        all_eq = db.get_all_exam_questions_by_ids(q_ids)
        db_questions = {q["id"]: q for q in all_eq}

    score, results, attempt_answers = 0, [], []
    module_stats = {}  # topic_id -> {correct, total, name, emoji}

    for q in quiz_qs:
        qid = q["id"]
        user_ans = answers.get(str(qid), "").strip().lower()
        ref = db_questions.get(qid, q)
        correct = str(ref["answer"]).strip().lower()
        ok = (user_ans == correct)
        if ok:
            score += 1

        topic_id = ref.get("topic_id", q.get("topic_id", "unknown"))
        results.append({
            "question_id": qid, "question": ref["question"],
            "user": answers.get(str(qid), ""),
            "correct_answer": ref["answer"], "correct": ok,
            "explanation": ref.get("explanation", ""),
            "topic_id": topic_id,
        })
        attempt_answers.append({"qid": qid, "user": answers.get(str(qid), ""), "correct": ok})

        # Build module stats
        if topic_id not in module_stats:
            t = TOPICS.get(topic_id, {})
            module_stats[topic_id] = {
                "correct": 0, "total": 0,
                "name": t.get("name", topic_id),
                "emoji": t.get("emoji", ""),
                "level": t.get("level", ""),
            }
        module_stats[topic_id]["total"] += 1
        if ok:
            module_stats[topic_id]["correct"] += 1

    total = len(quiz_qs)
    passed = score >= total * (exam["pass_percent"] / 100)

    db.save_exam_attempt(user["id"], exam_id, q_ids, attempt_answers, score, total, passed)

    db.log_activity(user["id"], "exam_attempt", detail=f"{exam['name']}: {score}/{total}", points=5)
    if passed:
        db.log_activity(user["id"], "exam_pass", detail=f"{exam['name']}: {score}/{total}", points=20)

    attempt_num = db.get_exam_attempt_count(user["id"], exam_id)
    show_answers = attempt_num >= 3
    if not show_answers:
        for r in results:
            r.pop("correct_answer", None)
            r.pop("explanation", None)

    # Build module breakdown sorted by accuracy (weakest first)
    module_breakdown = []
    for tid, ms in module_stats.items():
        pct = round(ms["correct"] / ms["total"] * 100) if ms["total"] > 0 else 0
        module_breakdown.append({
            "topic_id": tid, "name": ms["name"], "emoji": ms["emoji"],
            "level": ms["level"],
            "correct": ms["correct"], "total": ms["total"], "pct": pct,
        })
    module_breakdown.sort(key=lambda x: x["pct"])

    strong = [m for m in module_breakdown if m["pct"] >= 80]
    weak = [m for m in module_breakdown if m["pct"] < 50]

    return jsonify({
        "score": score, "total": total, "results": results,
        "passed": passed, "attempt": attempt_num,
        "show_answers": show_answers,
        "pass_percent": exam["pass_percent"],
        "exam_name": exam["name"],
        "module_breakdown": module_breakdown,
        "strong_modules": strong,
        "weak_modules": weak,
    })


@exam_bp.route("/exam/<exam_id>/bank")
@login_required
def exam_bank(exam_id):
    """Admin-only: view all questions in an exam's question bank."""
    user = current_user()
    if not user.get("is_admin"):
        flash("Admin access required.", "warning")
        return redirect(url_for("exam.exam_list"))
    if exam_id not in EXAMS:
        return render_template("404.html"), 404

    exam = EXAMS[exam_id]
    # Get all questions for grade modules
    questions = []
    for tid in exam["grade_modules"]:
        qs = db.get_all_exam_questions(tid)
        t = TOPICS.get(tid, {})
        for q in qs:
            questions.append({
                "id": q["id"],
                "question": q["question"],
                "answer": q["answer"],
                "options": q.get("options"),
                "explanation": q.get("explanation", ""),
                "difficulty": q.get("difficulty", ""),
                "topic_id": tid,
                "topic_name": t.get("name", tid),
                "topic_emoji": t.get("emoji", ""),
            })

    return render_template("pages/exam_bank.html",
                           exam=exam, exam_id=exam_id,
                           questions=questions, total=len(questions))
