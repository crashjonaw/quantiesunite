#!/usr/bin/env python3
"""
One-time migration: import all quiz.py QUIZ lists into the quiz_questions DB table.

Assigns difficulty based on curriculum level:
  Kindergarten/Primary 1-2       → difficulty 1 (easy)
  Primary 3-6                    → difficulty 1-2
  Secondary / O-Level            → difficulty 2 (medium)
  A-Level / A-Math               → difficulty 2-3
  University / Deep Learning     → difficulty 3 (hard)

Run once:  python3 migrate_quiz.py
"""

import os
import sys
import importlib

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(__file__))

import database as db
from curriculum_data import TOPICS

# Difficulty mapping by level
LEVEL_DIFFICULTY = {
    "Kindergarten": 1,
    "Primary 1–2": 1,
    "Primary 3–4": 1,
    "Primary 5–6": 2,
    "Sec 1–2": 2,
    "Sec 3–4": 2,
    "J1–2": 3,
    "Linear Algebra": 3,
    "Probability & Statistics": 3,
    "Python": 2,
    "Deep Learning": 3,
    "Deep Learning Advanced": 3,
}


def migrate():
    # Ensure tables exist
    db.init_db()

    conn = db.get_db()
    existing = conn.execute("SELECT COUNT(*) AS c FROM quiz_questions").fetchone()["c"]
    conn.close()

    if existing > 0:
        print(f"quiz_questions already has {existing} rows. Skipping migration.")
        print("To re-migrate, run: DELETE FROM quiz_questions;")
        return

    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    total_q = 0
    total_m = 0

    for tid in sorted(os.listdir(modules_dir)):
        quiz_path = os.path.join(modules_dir, tid, "quiz.py")
        if not os.path.isfile(quiz_path):
            continue

        try:
            mod = importlib.import_module(f"modules.{tid}.quiz")
            quiz_list = getattr(mod, "QUIZ", [])
        except Exception as e:
            print(f"  [WARN] Could not load {tid}/quiz.py: {e}")
            continue

        if not quiz_list:
            continue

        topic_info = TOPICS.get(tid, {})
        level = topic_info.get("level", "")
        base_difficulty = LEVEL_DIFFICULTY.get(level, 2)

        questions = []
        for q in quiz_list:
            questions.append({
                "question": q.get("question", ""),
                "answer": str(q.get("answer", "")),
                "options": q.get("options", []),
                "explanation": q.get("explanation", ""),
                "difficulty": base_difficulty,
                "concept": "",
                "tags": [],
            })

        db.insert_questions(tid, questions)
        total_q += len(questions)
        total_m += 1
        print(f"  {tid}: {len(questions)} questions (difficulty={base_difficulty})")

    print(f"\nMigrated {total_q} questions from {total_m} modules.")


if __name__ == "__main__":
    migrate()
