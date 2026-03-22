"""
QuantiesUnite — Lesson Content & Quiz Data
Loads authored content from modules/<topic_id>/ subfolders.
Falls back to a generic placeholder for topics without authored lessons.
"""

from modules import LESSONS


# ── Generic lesson fallback ──────────────────────────────────────────────────

def _generic_lesson(tid, t):
    return {
      "sections": [
        {"title": f"Introduction to {t['name']}",
         "body": f"""<p class='intro-text'>{t['tagline']}</p>
         <p>This module covers <strong>{t['name']}</strong>, part of the <em>{t['level']}</em> level in QuantiesUnite.</p>
         <p>Estimated study time: <strong>{t['hours']} hours</strong>.</p>
         <div class='coming-soon-box'>📚 Detailed lesson content is being authored for this topic.
         The quiz below tests the core concepts you should master.</div>""",
         "check": None},
      ],
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


def get_quiz(tid):
    content = get_lesson_content(tid)
    if content:
        return content.get("quiz", [])
    return []
