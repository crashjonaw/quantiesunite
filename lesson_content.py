"""
QuantiesUnite — Lesson Content & Quiz Data
Loads authored content from modules/<topic_id>/ subfolders.
Quiz questions are served from the SQLite question bank with random sampling.
Falls back to legacy quiz.py for modules not yet migrated.
"""

import database as db
from modules import LESSONS

# Default quiz size per attempt
QUIZ_SIZE = 10


# ── Generic lesson fallback ──────────────────────────────────────────────────

def _generic_lesson(tid, t):
    return {
      "type": "flat",
      "sections": [
        {"title": f"Introduction to {t['name']}",
         "body": f"""<p class='intro-text'>{t['tagline']}</p>
         <p>This module covers <strong>{t['name']}</strong>, part of the <em>{t['level']}</em> level in QuantiesUnite.</p>
         <p>Estimated study time: <strong>{t['hours']} hours</strong>.</p>
         <div class='coming-soon-box'>📚 Detailed lesson content is being authored for this topic.
         The quiz below tests the core concepts you should master.</div>""",
         "check": None},
      ],
      "concepts": [],
      "quiz": [
        {"question": f"What level is '{t['name']}' part of?", "answer": t["level"].lower(),
         "explanation": f"'{t['name']}' belongs to the {t['level']} level."},
        {"question": f"What is the tagline for '{t['name']}'?", "answer": t["tagline"].lower(),
         "explanation": f"Tagline: {t['tagline']}"},
      ]
    }


def get_lesson_content(tid):
    from curriculum_data import TOPICS
    if tid in LESSONS:
        return LESSONS[tid]
    t = TOPICS.get(tid)
    if t:
        return _generic_lesson(tid, t)
    return None


def get_quiz(tid, n=QUIZ_SIZE, must_include_ids=None):
    """Get quiz questions for a topic. Samples from DB question bank.
    must_include_ids: question IDs to always include (e.g. previously wrong).
    Falls back to legacy quiz.py if no DB questions exist."""
    # Try DB first
    q_count = db.get_question_count(tid)
    if q_count > 0:
        return db.sample_quiz(tid, n=n, must_include_ids=must_include_ids)

    # Fallback to legacy in-memory quiz
    content = get_lesson_content(tid)
    if content:
        legacy = content.get("quiz", [])
        out = []
        for i, q in enumerate(legacy):
            entry = {"id": -(i+1), **q}
            # MCQ with "options" + "correct" (index) → derive "answer" text
            if "options" in entry and "correct" in entry and "answer" not in entry:
                entry["answer"] = entry["options"][entry["correct"]]
            out.append(entry)
        return out
    return []


def get_concept(tid, concept_id):
    """Return a single concept dict from a concept-structured module."""
    content = get_lesson_content(tid)
    if not content or content.get("type") != "concepts":
        return None
    for c in content.get("concepts", []):
        if c["id"] == concept_id:
            return c
    return None
