"""
Migrate quiz and exam questions to use LaTeX formatting for mathematical expressions.
Wraps mathematical patterns in \\( ... \\) delimiters for KaTeX rendering.

Usage: python3 generated_questions/latex_migrate.py [--dry-run]
"""

import re
import sys
import os
import json
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.core import get_db

# Skip questions that already have LaTeX
ALREADY_LATEX = re.compile(r'\\[(\[]|\\frac|\\sqrt|\\times|\\div|\$[^$]+\$')

# Patterns to wrap in LaTeX — order matters (more specific first)
MATH_PATTERNS = [
    # Expressions with variables and operators: "3x + 5", "2x² - 7x + 1"
    (r'(?<![\\$a-zA-Z])(\d*[a-zA-Z][²³⁴⁵⁶⁷⁸⁹⁰]*(?:\s*[+\-*/]\s*\d*[a-zA-Z]?[²³⁴⁵⁶⁷⁸⁹⁰]*)+(?:\s*[+\-]\s*\d+)?)', r'\\(\1\\)'),
    # Equations: "x = 5", "y = 2x + 3", "x² + y² = r²"
    (r'(?<![\\$a-zA-Z])([a-zA-Z][²³⁴⁵⁶⁷⁸⁹⁰]?\s*=\s*[^,.\n]{2,30}?)(?=[,.\s?]|$)', r'\\(\1\\)'),
    # Powers with caret: "x^2", "2^10", "(a+b)^n"
    (r'(?<![\\$])(\(?[a-zA-Z0-9+\-]+\)?\^[\{\(]?[a-zA-Z0-9/+\-]+[\}\)]?)', r'\\(\1\\)'),
    # Fractions written as a/b where a,b are numbers or simple expressions
    (r'(?<![\\$a-zA-Z/])(\d+/\d+)(?![a-zA-Z/])', r'\\(\1\\)'),
    # Unicode superscripts: "x²", "5³"
    (r'(?<![\\$])(\w+[²³⁴⁵⁶⁷⁸⁹⁰]+)', r'\\(\1\\)'),
    # Inequality expressions: "x < 5", "n ≥ 10"
    (r'(?<![\\$])([a-zA-Z]\s*[<>≤≥≠]\s*\d+)', r'\\(\1\\)'),
    # Standalone math functions: "sin(x)", "cos(30°)", "log(x)", "ln(e)"
    (r'(?<![\\$a-zA-Z])((?:sin|cos|tan|log|ln|sqrt)\s*\([^)]+\))', r'\\(\1\\)'),
    # dy/dx, d²y/dx²
    (r'(?<![\\$])(d[²]?[a-zA-Z]/d[a-zA-Z][²]?)', r'\\(\1\\)'),
    # Plus/minus symbol
    (r'(?<![\\$])(±)', r'\\(\1\\)'),
    # Pi symbol standalone
    (r'(?<![\\$a-zA-Z])(π)(?![a-zA-Z])', r'\\(\1\\)'),
]


def needs_latex(text):
    """Check if text has math patterns but no existing LaTeX."""
    if not text:
        return False
    if ALREADY_LATEX.search(text):
        return False
    # Check for any math-like patterns
    math_indicators = [
        r'[²³⁴⁵⁶⁷⁸⁹⁰]', r'\^', r'[a-z]\s*[=<>]',
        r'\d+/\d+', r'sqrt', r'sin|cos|tan|log|ln',
        r'dy/dx', r'd/dx', r'[±π]',
    ]
    for pattern in math_indicators:
        if re.search(pattern, text):
            return True
    return False


def apply_latex(text):
    """Apply LaTeX wrapping to mathematical expressions in text."""
    if not text or ALREADY_LATEX.search(text):
        return text

    result = text
    for pattern, replacement in MATH_PATTERNS:
        # Don't re-wrap things already in \( \)
        result = re.sub(pattern, replacement, result)

    # Clean up double-wrapping
    result = result.replace('\\(\\(', '\\(').replace('\\)\\)', '\\)')

    # Convert Unicode superscripts to LaTeX within \( \)
    def fix_unicode_super(match):
        s = match.group(1)
        s = s.replace('²', '^2').replace('³', '^3').replace('⁴', '^4')
        s = s.replace('⁵', '^5').replace('⁶', '^6').replace('⁷', '^7')
        s = s.replace('⁸', '^8').replace('⁹', '^9').replace('⁰', '^0')
        return '\\(' + s + '\\)'

    result = re.sub(r'\\(([^)]*[²³⁴⁵⁶⁷⁸⁹⁰][^)]*)\\)', fix_unicode_super, result)

    return result


def process_options(options_json):
    """Apply LaTeX to MCQ options."""
    if not options_json:
        return options_json
    try:
        opts = json.loads(options_json) if isinstance(options_json, str) else options_json
    except (json.JSONDecodeError, TypeError):
        return options_json

    if not opts:
        return options_json

    changed = False
    new_opts = []
    for opt in opts:
        new_opt = apply_latex(str(opt)) if needs_latex(str(opt)) else str(opt)
        if new_opt != str(opt):
            changed = True
        new_opts.append(new_opt)

    return json.dumps(new_opts) if changed else options_json


def migrate_table(table_name, dry_run=False):
    """Migrate all questions in a table to use LaTeX."""
    db = get_db()
    rows = db.execute(f"SELECT id, question, answer, options, explanation FROM {table_name}").fetchall()

    updated = 0
    skipped = 0

    for row in rows:
        qid = row["id"]
        q = row["question"]
        a = row["answer"]
        opts = row["options"]
        exp = row["explanation"]

        new_q = apply_latex(q) if needs_latex(q) else q
        new_a = apply_latex(a) if needs_latex(a) else a
        new_opts = process_options(opts)
        new_exp = apply_latex(exp) if needs_latex(exp) else exp

        if new_q != q or new_a != a or new_opts != opts or new_exp != exp:
            if not dry_run:
                db.execute(
                    f"UPDATE {table_name} SET question=?, answer=?, options=?, explanation=? WHERE id=?",
                    (new_q, new_a, new_opts if isinstance(new_opts, str) else json.dumps(new_opts), new_exp, qid)
                )
            updated += 1
            if updated <= 5:
                print(f"  [{qid}] {q[:60]}")
                print(f"     → {new_q[:60]}")
                print()
        else:
            skipped += 1

    if not dry_run:
        db.commit()
    db.close()

    return updated, skipped


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN (no changes will be saved) ===\n")

    print("Processing quiz_questions...")
    quiz_updated, quiz_skipped = migrate_table("quiz_questions", dry_run)
    print(f"  Updated: {quiz_updated}, Skipped: {quiz_skipped}\n")

    print("Processing exam_questions...")
    exam_updated, exam_skipped = migrate_table("exam_questions", dry_run)
    print(f"  Updated: {exam_updated}, Skipped: {exam_skipped}\n")

    total = quiz_updated + exam_updated
    print(f"Total questions updated: {total}")
    if dry_run:
        print("(No changes saved — run without --dry-run to apply)")
