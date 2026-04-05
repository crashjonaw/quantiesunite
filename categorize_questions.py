#!/usr/bin/env python3
"""
Step 1: Re-categorize existing questions within each module into difficulty 1-3.
Currently all questions in a module share the same difficulty (from curriculum level).
This script spreads them across tiers based on question complexity heuristics.

Heuristics:
  d1 (easy):   recall, definition, "what is", simple identification, MCQ with obvious answers
  d2 (medium): application, single-step calculation, "solve", "find", "calculate"
  d3 (hard):   multi-step, "show that", "prove", "explain why", word problems, complex calc

Run: python3 categorize_questions.py
"""

import re
import database as db

# Complexity scoring patterns
EASY_PATTERNS = [
    (r'\bwhat is\b.*\bcalled\b', -2),
    (r'\bwhat does\b', -2),
    (r'\bwhich of the following\b.*\bNOT\b', 1),  # NOT questions are trickier
    (r'\bwhich of the following\b', -1),
    (r'\bwhat is the (primary|main)\b', -1),
    (r'\bdefin(e|ition)\b', -2),
    (r'\bname\b', -1),
    (r'\bidentif(y|ies)\b', -1),
    (r'\bcount\b', -2),
    (r'\bhow many\b', -1),
    (r'🌟|⭐|🔵|🟢|🍎', -3),  # emoji-based questions are easiest
    (r'\bwhat is the value\b', -1),
    (r'\btrue or false\b', -2),
    (r'\bwhat type\b', -1),
]

MEDIUM_PATTERNS = [
    (r'\bsolve\b', 1),
    (r'\bcalculat(e|ion)\b', 1),
    (r'\bfind\b', 1),
    (r'\bsimplif(y|ied)\b', 1),
    (r'\bexpand\b', 1),
    (r'\bconvert\b', 0),
    (r'\bwhat is \d', 0),  # "what is 5 + 3" type
    (r'\bfactor(ise|ize)\b', 1),
    (r'\bevaluat(e|ion)\b', 1),
]

HARD_PATTERNS = [
    (r'\bshow that\b', 3),
    (r'\bprove\b', 3),
    (r'\bexplain why\b', 2),
    (r'\bderive\b', 3),
    (r'\bgeometrically\b', 2),
    (r'\bword problem\b', 2),
    (r'\bmaximum|minimum\b', 1),
    (r'\bperimeter.*area|area.*perimeter\b', 2),
    (r'\brectangle has\b', 1),  # word problem indicator
    (r'\ba (farmer|tank|car|train|rectangle|box|company)\b', 2),  # word problem
    (r'\bno real roots\b', 2),
    (r'\blimitation\b', 1),
    (r'\barchitecture\b', 1),
    (r'\bcompare\b', 1),
    (r'\badvantage.*disadvantage\b', 2),
    (r'\bhow does.*differ\b', 2),
]


def score_question(q_text):
    """Return a complexity score. Lower = easier."""
    score = 0
    text = q_text.lower()

    for pattern, pts in EASY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            score += pts

    for pattern, pts in MEDIUM_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            score += pts

    for pattern, pts in HARD_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            score += pts

    # Longer questions tend to be harder (word problems)
    if len(text) > 150:
        score += 1
    if len(text) > 250:
        score += 1

    # Questions with multiple math operations
    if len(re.findall(r'[+\-×÷*/^²³]', text)) > 3:
        score += 1

    return score


def recategorize():
    """Spread existing questions across difficulty 1-3 within each module."""
    conn = db.get_db()

    # Get all topic_ids
    topics = conn.execute(
        "SELECT DISTINCT topic_id FROM quiz_questions ORDER BY topic_id"
    ).fetchall()

    total_changed = 0

    for row in topics:
        tid = row["topic_id"]
        questions = conn.execute(
            "SELECT id, question FROM quiz_questions WHERE topic_id=? ORDER BY id",
            (tid,)
        ).fetchall()

        n = len(questions)
        if n == 0:
            continue

        # Score each question
        scored = [(q["id"], q["question"], score_question(q["question"])) for q in questions]
        # Sort by complexity score
        scored.sort(key=lambda x: x[2])

        # Split into thirds: easiest → d1, middle → d2, hardest → d3
        if n <= 3:
            # With 3 or fewer, one per tier
            for i, (qid, _, _) in enumerate(scored):
                diff = i + 1
                conn.execute("UPDATE quiz_questions SET difficulty=? WHERE id=?", (diff, qid))
                total_changed += 1
        else:
            # Split into rough thirds
            third = n / 3
            for i, (qid, qtxt, qscore) in enumerate(scored):
                if i < third:
                    diff = 1
                elif i < 2 * third:
                    diff = 2
                else:
                    diff = 3
                conn.execute("UPDATE quiz_questions SET difficulty=? WHERE id=?", (diff, qid))
                total_changed += 1

        # Verify distribution
        d1 = len([s for i, s in enumerate(scored) if i < n/3])
        d2 = len([s for i, s in enumerate(scored) if n/3 <= i < 2*n/3])
        d3 = len([s for i, s in enumerate(scored) if i >= 2*n/3])
        print(f"  {tid:40s}  {n} questions → d1={d1} d2={d2} d3={d3}")

    conn.commit()
    conn.close()
    print(f"\nRecategorized {total_changed} questions across {len(topics)} modules.")


if __name__ == "__main__":
    recategorize()
