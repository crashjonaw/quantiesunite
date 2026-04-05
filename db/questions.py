"""
Quiz question bank — CRUD, sampling, practice, attempt tracking.
"""

import json
from db.core import get_db


def insert_questions(topic_id, questions):
    db = get_db()
    for q in questions:
        db.execute(
            """INSERT INTO quiz_questions
               (topic_id, question, answer, options, explanation, difficulty, concept, tags)
               VALUES (?,?,?,?,?,?,?,?)""",
            (topic_id, q["question"], q["answer"],
             json.dumps(q.get("options") or []),
             q.get("explanation", ""), q.get("difficulty", 1),
             q.get("concept", ""), json.dumps(q.get("tags") or [])))
    db.commit()
    db.close()


def get_question_count(topic_id):
    db = get_db()
    count = db.execute(
        "SELECT COUNT(*) AS c FROM quiz_questions WHERE topic_id=?",
        (topic_id,)).fetchone()["c"]
    db.close()
    return count


def sample_quiz(topic_id, n=10, difficulty_weights=None, must_include_ids=None):
    db = get_db()
    forced, forced_ids = [], set()
    if must_include_ids:
        ph = ",".join("?" * len(must_include_ids))
        forced = db.execute(
            f"SELECT * FROM quiz_questions WHERE topic_id=? AND id IN ({ph})",
            (topic_id, *must_include_ids)).fetchall()
        forced_ids = {r["id"] for r in forced}

    remaining_slots = n - len(forced)
    if remaining_slots <= 0:
        import random
        forced = list(forced)
        random.shuffle(forced)
        questions = forced[:n]
    elif difficulty_weights:
        questions = list(forced)
        exclude_ids = set(forced_ids)
        for diff, count in sorted(difficulty_weights.items()):
            if exclude_ids:
                ph = ",".join("?" * len(exclude_ids))
                rows = db.execute(
                    f"SELECT * FROM quiz_questions WHERE topic_id=? AND difficulty=? AND id NOT IN ({ph}) ORDER BY RANDOM() LIMIT ?",
                    (topic_id, diff, *exclude_ids, count)).fetchall()
            else:
                rows = db.execute(
                    "SELECT * FROM quiz_questions WHERE topic_id=? AND difficulty=? ORDER BY RANDOM() LIMIT ?",
                    (topic_id, diff, count)).fetchall()
            questions.extend(rows)
            exclude_ids.update(r["id"] for r in rows)
        if len(questions) < n:
            ph = ",".join("?" * len(exclude_ids)) if exclude_ids else "0"
            extra = db.execute(
                f"SELECT * FROM quiz_questions WHERE topic_id=? AND id NOT IN ({ph}) ORDER BY RANDOM() LIMIT ?",
                (topic_id, *exclude_ids, n - len(questions))).fetchall()
            questions.extend(extra)
    else:
        if forced_ids:
            ph = ",".join("?" * len(forced_ids))
            random_qs = db.execute(
                f"SELECT * FROM quiz_questions WHERE topic_id=? AND id NOT IN ({ph}) ORDER BY RANDOM() LIMIT ?",
                (topic_id, *forced_ids, remaining_slots)).fetchall()
        else:
            random_qs = db.execute(
                "SELECT * FROM quiz_questions WHERE topic_id=? ORDER BY RANDOM() LIMIT ?",
                (topic_id, remaining_slots)).fetchall()
        questions = list(forced) + list(random_qs)

    db.close()
    return [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "options": json.loads(r["options"]) if r["options"] else [],
             "explanation": r["explanation"] or "", "difficulty": r["difficulty"],
             "concept": r["concept"] or ""} for r in questions]


def get_all_questions(topic_id):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM quiz_questions WHERE topic_id=? ORDER BY difficulty, id",
        (topic_id,)).fetchall()
    db.close()
    return [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "options": json.loads(r["options"]) if r["options"] else [],
             "explanation": r["explanation"] or "", "difficulty": r["difficulty"],
             "concept": r["concept"] or "",
             "tags": json.loads(r["tags"]) if r["tags"] else []} for r in rows]


# ── Attempt tracking ─────────────────────────────────────────────────────────

def save_quiz_attempt(user_id, topic_id, question_ids, answers, score, total, passed):
    db = get_db()
    db.execute(
        """INSERT INTO quiz_attempts
           (user_id, topic_id, question_ids, answers, score, total, passed)
           VALUES (?,?,?,?,?,?,?)""",
        (user_id, topic_id, json.dumps(question_ids),
         json.dumps(answers), score, total, int(passed)))
    db.commit()
    db.close()


def get_wrong_question_ids(user_id, topic_id):
    db = get_db()
    attempts = db.execute(
        "SELECT answers FROM quiz_attempts WHERE user_id=? AND topic_id=? ORDER BY created_at",
        (user_id, topic_id)).fetchall()
    db.close()
    ever_wrong, ever_right = set(), set()
    for att in attempts:
        for a in json.loads(att["answers"]):
            (ever_right if a["correct"] else ever_wrong).add(a["qid"])
    return list(ever_wrong - ever_right)


def get_seen_question_ids(user_id, topic_id):
    db = get_db()
    attempts = db.execute(
        "SELECT question_ids FROM quiz_attempts WHERE user_id=? AND topic_id=?",
        (user_id, topic_id)).fetchall()
    db.close()
    seen = set()
    for att in attempts:
        for qid in json.loads(att["question_ids"]):
            seen.add(qid)
    return seen


def sample_practice_quiz(topic_id, user_id, n=10):
    wrong_ids = get_wrong_question_ids(user_id, topic_id)
    seen_ids = get_seen_question_ids(user_id, topic_id)
    db = get_db()
    all_ids = {r["id"] for r in db.execute(
        "SELECT id FROM quiz_questions WHERE topic_id=?", (topic_id,)).fetchall()}
    unseen_ids = all_ids - seen_ids
    selected = []

    if unseen_ids:
        ph = ",".join("?" * len(unseen_ids))
        selected.extend(db.execute(
            f"SELECT * FROM quiz_questions WHERE id IN ({ph}) ORDER BY RANDOM() LIMIT ?",
            (*unseen_ids, n)).fetchall())
    remaining = n - len(selected)
    if remaining > 0 and wrong_ids:
        already = {r["id"] for r in selected}
        fill = [qid for qid in wrong_ids if qid not in already]
        if fill:
            ph = ",".join("?" * len(fill))
            selected.extend(db.execute(
                f"SELECT * FROM quiz_questions WHERE id IN ({ph}) ORDER BY RANDOM() LIMIT ?",
                (*fill, remaining)).fetchall())
    remaining = n - len(selected)
    if remaining > 0:
        already = {r["id"] for r in selected}
        if already:
            ph = ",".join("?" * len(already))
            selected.extend(db.execute(
                f"SELECT * FROM quiz_questions WHERE topic_id=? AND id NOT IN ({ph}) ORDER BY RANDOM() LIMIT ?",
                (topic_id, *already, remaining)).fetchall())
        else:
            selected.extend(db.execute(
                "SELECT * FROM quiz_questions WHERE topic_id=? ORDER BY RANDOM() LIMIT ?",
                (topic_id, remaining)).fetchall())
    db.close()
    return [{"id": r["id"], "question": r["question"], "answer": r["answer"],
             "options": json.loads(r["options"]) if r["options"] else [],
             "explanation": r["explanation"] or "", "difficulty": r["difficulty"],
             "concept": r["concept"] or ""} for r in selected]


def get_practice_stats(user_id, topic_id):
    total = get_question_count(topic_id)
    if total == 0:
        return None
    seen = len(get_seen_question_ids(user_id, topic_id))
    wrong = len(get_wrong_question_ids(user_id, topic_id))
    return {"total_in_bank": total, "seen": seen, "unseen": total - seen,
            "wrong": wrong, "mastered": seen - wrong}


def get_attempt_count(user_id, topic_id):
    db = get_db()
    count = db.execute(
        "SELECT COUNT(*) AS c FROM quiz_attempts WHERE user_id=? AND topic_id=?",
        (user_id, topic_id)).fetchone()["c"]
    db.close()
    return count


def get_question_stats(topic_id):
    db = get_db()
    attempts = db.execute(
        "SELECT question_ids, answers FROM quiz_attempts WHERE topic_id=?",
        (topic_id,)).fetchall()
    questions = db.execute(
        "SELECT id, question, difficulty FROM quiz_questions WHERE topic_id=?",
        (topic_id,)).fetchall()
    db.close()
    q_map = {r["id"]: {"question": r["question"], "difficulty": r["difficulty"]} for r in questions}
    stats = {}
    for att in attempts:
        for qid, a in zip(json.loads(att["question_ids"]), json.loads(att["answers"])):
            if qid not in stats:
                stats[qid] = {"shown": 0, "correct": 0}
            stats[qid]["shown"] += 1
            if a.get("correct"):
                stats[qid]["correct"] += 1
    result = []
    for qid, s in sorted(stats.items()):
        info = q_map.get(qid, {})
        acc = round(s["correct"] / s["shown"] * 100) if s["shown"] > 0 else 0
        result.append({"question_id": qid, "question": info.get("question", "?"),
                       "difficulty": info.get("difficulty", 1),
                       "times_shown": s["shown"], "times_correct": s["correct"],
                       "accuracy": acc})
    return sorted(result, key=lambda x: x["accuracy"])
