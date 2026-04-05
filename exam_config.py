"""
QuantiesUnite — Exam Configuration

Defines grade-level exams that gate progression between curriculum levels.
Each exam draws questions from the grade's modules + review questions
testing first-principle concepts from any earlier grade.
"""

from curriculum_data import TOPICS, LEVELS_ORDER

# ── First-Principle Review Topics ────────────────────────────────────────────
# These are foundational concepts every student should retain regardless of
# their current level. Review questions are sampled from these modules.
FIRST_PRINCIPLE_MODULES = [
    # Kindergarten — number sense
    "k_numbers", "k_counting", "k_addition", "k_subtraction",
    # Primary 1-2 — arithmetic fluency
    "p12_whole_1000", "p12_add_sub", "p12_multiply", "p12_divide",
    "p12_fractions_basic",
    # Primary 3-4 — operational mastery
    "p34_all_tables", "p34_long_mult_div", "p34_fractions", "p34_decimals",
    # Primary 5-6 — proportional reasoning & algebra foundations
    "p56_ratio", "p56_percentage", "p56_algebra_intro", "p56_fractions_adv",
    # Sec 1-2 — algebraic thinking
    "sec12_algebra", "sec12_indices", "sec12_pythagoras",
    # Sec 3-4 — advanced foundations
    "olevel_quadratic", "olevel_trigonometry", "amath_diff_intro", "amath_int_intro",
]


def _modules_for_level(level):
    """Return all topic IDs belonging to a curriculum level."""
    return [tid for tid, t in TOPICS.items() if t["level"] == level]


# ── Exam Definitions ─────────────────────────────────────────────────────────

EXAMS = {
    "exam_p12": {
        "name": "P1–2 Mastery Exam",
        "emoji": "🏫",
        "description": "Demonstrate mastery of whole numbers, operations, fractions, measurement, and time.",
        "from_level": "Primary 1–2",
        "unlocks_level": "Primary 3–4",
        "grade_modules": _modules_for_level("Primary 1–2"),
        "grade_questions": 25,
        "review_questions": 5,
        "total_questions": 30,
        "pass_percent": 70,
        "time_limit_min": 40,       # ~1.3 min/question
        "untimed_multiplier": 1.5,  # untimed = 45 questions
        "color": "#90EE90",
    },
    "exam_p34": {
        "name": "P3–4 Mastery Exam",
        "emoji": "🧱",
        "description": "Show your command of long multiplication, fractions, decimals, geometry, and data.",
        "from_level": "Primary 3–4",
        "unlocks_level": "Primary 5–6",
        "grade_modules": _modules_for_level("Primary 3–4"),
        "grade_questions": 25,
        "review_questions": 5,
        "total_questions": 30,
        "pass_percent": 70,
        "time_limit_min": 45,       # 1.5 min/question
        "untimed_multiplier": 1.5,  # untimed = 45 questions
        "color": "#98FB98",
    },
    "exam_p56": {
        "name": "PSLE Readiness Exam",
        "emoji": "🎓",
        "description": "A comprehensive exam covering ratio, percentage, algebra, volume, and problem solving — PSLE-level difficulty.",
        "from_level": "Primary 5–6",
        "unlocks_level": "Sec 1–2",
        "grade_modules": _modules_for_level("Primary 5–6"),
        "grade_questions": 30,
        "review_questions": 10,
        "total_questions": 40,
        "pass_percent": 70,
        "time_limit_min": 75,       # ~1.9 min/question (PSLE is a big exam)
        "untimed_multiplier": 1.5,  # untimed = 60 questions
        "color": "#3CB371",
    },
    "exam_sec12": {
        "name": "Sec 1–2 Mastery Exam",
        "emoji": "📚",
        "description": "Prove your understanding of algebra, geometry, Pythagoras, statistics, and probability.",
        "from_level": "Sec 1–2",
        "unlocks_level": "Sec 3–4",
        "grade_modules": _modules_for_level("Sec 1–2"),
        "grade_questions": 25,
        "review_questions": 5,
        "total_questions": 30,
        "pass_percent": 70,
        "time_limit_min": 60,       # 2 min/question
        "untimed_multiplier": 1.5,  # untimed = 45 questions
        "color": "#4169E1",
    },
    "exam_sec34": {
        "name": "O-Level Readiness Exam",
        "emoji": "🏅",
        "description": "A rigorous exam spanning E-Math and A-Math — quadratics, trigonometry, calculus, and more.",
        "from_level": "Sec 3–4",
        "unlocks_level": "J1–2",
        "grade_modules": _modules_for_level("Sec 3–4"),
        "grade_questions": 30,
        "review_questions": 10,
        "total_questions": 40,
        "pass_percent": 70,
        "time_limit_min": 90,       # ~2.25 min/question
        "untimed_multiplier": 1.5,  # untimed = 60 questions
        "color": "#1E90FF",
    },
    "exam_jc": {
        "name": "A-Level Readiness Exam",
        "emoji": "🎯",
        "description": "The capstone exam — complex numbers, advanced calculus, vectors, distributions, and hypothesis testing.",
        "from_level": "J1–2",
        "unlocks_level": None,
        "grade_modules": _modules_for_level("J1–2"),
        "grade_questions": 35,
        "review_questions": 15,
        "total_questions": 50,
        "pass_percent": 70,
        "time_limit_min": 120,      # 2.4 min/question (A-Level is demanding)
        "untimed_multiplier": 1.5,  # untimed = 75 questions
        "color": "#9400D3",
    },
}


def get_exam_params(exam_id, timed=True):
    """Return (total_questions, grade_questions, review_questions, time_limit_min)
    based on timed/untimed mode."""
    exam = EXAMS[exam_id]
    if timed:
        return (exam["total_questions"], exam["grade_questions"],
                exam["review_questions"], exam["time_limit_min"])
    else:
        mult = exam.get("untimed_multiplier", 1.5)
        total = round(exam["total_questions"] * mult)
        grade = round(exam["grade_questions"] * mult)
        review = total - grade
        return (total, grade, review, None)

# Ordered list for display
EXAM_ORDER = [
    "exam_p12", "exam_p34", "exam_p56",
    "exam_sec12", "exam_sec34", "exam_jc",
]


def get_review_modules(exam_id):
    """Return first-principle modules available for review questions.
    Excludes modules from the exam's own grade (those are grade_modules)."""
    exam = EXAMS[exam_id]
    grade_set = set(exam["grade_modules"])
    # Only include first-principle modules from levels below the exam's level
    exam_level_idx = LEVELS_ORDER.index(exam["from_level"])
    eligible = []
    for tid in FIRST_PRINCIPLE_MODULES:
        if tid in grade_set:
            continue
        t = TOPICS.get(tid)
        if t and t["level"] in LEVELS_ORDER:
            if LEVELS_ORDER.index(t["level"]) < exam_level_idx:
                eligible.append(tid)
    return eligible


def get_exam_for_level(level):
    """Return the exam_id that gates entry INTO this level, or None."""
    for eid, exam in EXAMS.items():
        if exam["unlocks_level"] == level:
            return eid
    return None


def get_exam_from_level(level):
    """Return the exam_id for completing this level, or None."""
    for eid, exam in EXAMS.items():
        if exam["from_level"] == level:
            return eid
    return None
