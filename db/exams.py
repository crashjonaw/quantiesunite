"""
Exam database operations — question bank, sampling, attempts, pass tracking.
Uses a separate exam_questions table so students never see exam questions
during regular quizzes or practice.
"""

import json
from db.core import get_db


def insert_exam_questions(topic_id, questions):
    """Bulk insert exam questions for a topic."""
    db = get_db()
    for q in questions:
        diff = q.get("difficulty", 2)
        if isinstance(diff, list):
            diff = diff[0] if diff else 2
        diff = int(diff) if isinstance(diff, (int, float, str)) else 2
        explanation = q.get("explanation", "")
        if isinstance(explanation, list):
            explanation = " ".join(str(x) for x in explanation) if explanation else ""
        concept = q.get("concept", "")
        if isinstance(concept, list):
            concept = ", ".join(str(x) for x in concept)
        db.execute(
            """INSERT INTO exam_questions
               (topic_id, question, answer, options, explanation, difficulty, concept, tags)
               VALUES (?,?,?,?,?,?,?,?)""",
            (topic_id, q["question"], q["answer"],
             json.dumps(q.get("options") or []),
             explanation, diff, concept,
             json.dumps(q.get("tags") or [])))
    db.commit()
    db.close()


def get_exam_question_count(topic_id):
    """Return number of exam questions for a topic."""
    db = get_db()
    row = db.execute(
        "SELECT COUNT(*) AS c FROM exam_questions WHERE topic_id=?",
        (topic_id,)).fetchone()
    db.close()
    return row["c"] if row else 0


def sample_exam_questions(grade_modules, grade_count, review_modules, review_count,
                          must_include_ids=None, seen_ids=None):
    """Sample exam questions from the dedicated exam question bank.
    Enforces difficulty distribution: ~30% easy, ~40% medium, ~30% hard
    for grade questions. Review questions use difficulty 1-2 only.

    must_include_ids: question IDs to force-include (previously wrong).
    seen_ids: question IDs already seen — unseen questions are preferred.
    """
    import random
    db = get_db()
    questions = []
    forced_ids = set()

    all_modules = list(set((grade_modules or []) + (review_modules or [])))
    all_modules_ph = ",".join("?" * len(all_modules)) if all_modules else "''"

    # 1. Force-include wrong questions first
    if must_include_ids:
        ph = ",".join("?" * len(must_include_ids))
        forced = db.execute(
            f"SELECT * FROM exam_questions WHERE id IN ({ph})",
            must_include_ids).fetchall()
        questions.extend(forced)
        forced_ids = {r["id"] for r in forced}

    total_needed = grade_count + review_count
    remaining = total_needed - len(questions)

    # 2. Prefer unseen questions
    if remaining > 0 and seen_ids is not None:
        exclude = forced_ids | seen_ids
        if exclude:
            ph_ex = ",".join("?" * len(exclude))
            unseen = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({all_modules_ph}) AND id NOT IN ({ph_ex})
                    ORDER BY RANDOM() LIMIT ?""",
                (*all_modules, *exclude, remaining)).fetchall()
        else:
            unseen = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({all_modules_ph})
                    ORDER BY RANDOM() LIMIT ?""",
                (*all_modules, remaining)).fetchall()
        questions.extend(unseen)
        forced_ids.update(r["id"] for r in unseen)
        remaining = total_needed - len(questions)

    # 3. Fill remaining with difficulty-stratified sampling (recycled if needed)
    if remaining > 0 and grade_modules:
        placeholders = ",".join("?" * len(grade_modules))
        exclude = forced_ids
        # Split remaining into difficulty buckets
        easy_n = round(remaining * 0.30)
        medium_n = round(remaining * 0.40)
        hard_n = remaining - easy_n - medium_n

        for diff, n in [(1, easy_n), (2, medium_n), (3, hard_n)]:
            if n <= 0:
                continue
            if exclude:
                ph_ex = ",".join("?" * len(exclude))
                rows = db.execute(
                    f"""SELECT * FROM exam_questions
                        WHERE topic_id IN ({placeholders}) AND difficulty = ? AND id NOT IN ({ph_ex})
                        ORDER BY RANDOM() LIMIT ?""",
                    (*grade_modules, diff, *exclude, n)).fetchall()
            else:
                rows = db.execute(
                    f"""SELECT * FROM exam_questions
                        WHERE topic_id IN ({placeholders}) AND difficulty = ?
                        ORDER BY RANDOM() LIMIT ?""",
                    (*grade_modules, diff, n)).fetchall()
            questions.extend(rows)
            exclude = exclude | {r["id"] for r in rows}

    # 4. Fill any final shortfall from review modules
    remaining = total_needed - len(questions)
    if remaining > 0 and review_modules:
        r_ph = ",".join("?" * len(review_modules))
        exclude = {r["id"] for r in questions}
        if exclude:
            ph_ex = ",".join("?" * len(exclude))
            rows = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({r_ph}) AND difficulty <= 2 AND id NOT IN ({ph_ex})
                    ORDER BY RANDOM() LIMIT ?""",
                (*review_modules, *exclude, remaining)).fetchall()
        else:
            rows = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({r_ph}) AND difficulty <= 2
                    ORDER BY RANDOM() LIMIT ?""",
                (*review_modules, remaining)).fetchall()
        questions.extend(rows)

    # 5. Final fallback — recycle any if still short
    remaining = total_needed - len(questions)
    if remaining > 0:
        exclude = {r["id"] for r in questions}
        if exclude:
            ph_ex = ",".join("?" * len(exclude))
            rows = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({all_modules_ph}) AND id NOT IN ({ph_ex})
                    ORDER BY RANDOM() LIMIT ?""",
                (*all_modules, *exclude, remaining)).fetchall()
        else:
            rows = db.execute(
                f"""SELECT * FROM exam_questions
                    WHERE topic_id IN ({all_modules_ph})
                    ORDER BY RANDOM() LIMIT ?""",
                (*all_modules, remaining)).fetchall()
        questions.extend(rows)

    db.close()
    random.shuffle(questions)

    result = []
    for r in questions:
        opts = r["options"]
        if isinstance(opts, str):
            try:
                opts = json.loads(opts)
            except (json.JSONDecodeError, TypeError):
                opts = []
        result.append({
            "id": r["id"],
            "topic_id": r["topic_id"],
            "question": r["question"],
            "answer": r["answer"],
            "options": opts if opts else [],
            "explanation": r["explanation"] or "",
            "difficulty": r["difficulty"],
            "concept": r["concept"] or "",
        })
    return result


def get_all_exam_questions(topic_id):
    """Return all exam questions for a topic (for admin/dedup)."""
    db = get_db()
    rows = db.execute(
        "SELECT * FROM exam_questions WHERE topic_id=? ORDER BY id",
        (topic_id,)).fetchall()
    db.close()
    return [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "options": json.loads(r["options"]) if r["options"] else [],
             "explanation": r["explanation"] or "", "difficulty": r["difficulty"],
             "concept": r["concept"] or ""} for r in rows]


def get_all_exam_questions_by_ids(question_ids):
    """Fetch exam questions by their IDs (for answer verification)."""
    if not question_ids:
        return []
    db = get_db()
    placeholders = ",".join("?" * len(question_ids))
    rows = db.execute(
        f"SELECT * FROM exam_questions WHERE id IN ({placeholders})",
        question_ids).fetchall()
    db.close()
    return [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "options": json.loads(r["options"]) if r["options"] else [],
             "explanation": r["explanation"] or "", "difficulty": r["difficulty"],
             "concept": r["concept"] or ""} for r in rows]


def get_exam_wrong_question_ids(user_id, exam_id):
    """Return exam question IDs the user got wrong and never subsequently got right."""
    db = get_db()
    attempts = db.execute(
        "SELECT answers FROM exam_attempts WHERE user_id=? AND exam_id=? ORDER BY created_at",
        (user_id, exam_id)).fetchall()
    db.close()
    ever_wrong, ever_right = set(), set()
    for att in attempts:
        for a in json.loads(att["answers"]):
            (ever_right if a["correct"] else ever_wrong).add(a["qid"])
    return list(ever_wrong - ever_right)


def get_exam_seen_question_ids(user_id, exam_id):
    """Return all exam question IDs the user has ever been shown."""
    db = get_db()
    attempts = db.execute(
        "SELECT question_ids FROM exam_attempts WHERE user_id=? AND exam_id=?",
        (user_id, exam_id)).fetchall()
    db.close()
    seen = set()
    for att in attempts:
        for qid in json.loads(att["question_ids"]):
            seen.add(qid)
    return seen


def save_exam_attempt(user_id, exam_id, question_ids, answers, score, total, passed):
    db = get_db()
    db.execute(
        """INSERT INTO exam_attempts
           (user_id, exam_id, question_ids, answers, score, total, passed)
           VALUES (?,?,?,?,?,?,?)""",
        (user_id, exam_id, json.dumps(question_ids),
         json.dumps(answers), score, total, int(passed)))
    db.commit()
    db.close()


def has_passed_exam(user_id, exam_id):
    db = get_db()
    row = db.execute(
        "SELECT COUNT(*) AS c FROM exam_attempts WHERE user_id=? AND exam_id=? AND passed=1",
        (user_id, exam_id)).fetchone()
    db.close()
    return row["c"] > 0


def get_exam_attempt_count(user_id, exam_id):
    db = get_db()
    row = db.execute(
        "SELECT COUNT(*) AS c FROM exam_attempts WHERE user_id=? AND exam_id=?",
        (user_id, exam_id)).fetchone()
    db.close()
    return row["c"]


def get_best_exam_score(user_id, exam_id):
    db = get_db()
    row = db.execute(
        """SELECT score, total FROM exam_attempts
           WHERE user_id=? AND exam_id=?
           ORDER BY score DESC LIMIT 1""",
        (user_id, exam_id)).fetchone()
    db.close()
    return (row["score"], row["total"]) if row else (None, None)


def get_all_exam_status(user_id):
    db = get_db()
    rows = db.execute(
        """SELECT exam_id, MAX(passed) AS passed, COUNT(*) AS attempts,
                  MAX(score) AS best_score, MAX(total) AS total
           FROM exam_attempts WHERE user_id=?
           GROUP BY exam_id""",
        (user_id,)).fetchall()
    db.close()
    return {r["exam_id"]: {
        "passed": bool(r["passed"]),
        "attempts": r["attempts"],
        "best_score": r["best_score"],
        "total": r["total"],
    } for r in rows}
