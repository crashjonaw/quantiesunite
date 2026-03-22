"""
QuantiesUnite — Per-topic module loader.

Each topic has its own subfolder under modules/ containing:
  - lesson.py  : SECTIONS list (title + body HTML)
  - checks.py  : CHECKS list  (mid-lesson check questions, one per section)
  - quiz.py    : QUIZ list    (final quiz questions)

This __init__.py auto-discovers every subfolder, imports the three files,
and assembles them into a single LESSONS dict that the rest of the app uses.
"""

import os
import importlib

_DIR = os.path.dirname(__file__)

def _load_lessons():
    """Scan every subfolder and combine lesson + checks + quiz into LESSONS."""
    lessons = {}
    for entry in sorted(os.listdir(_DIR)):
        folder = os.path.join(_DIR, entry)
        if not os.path.isdir(folder):
            continue
        lesson_file = os.path.join(folder, "lesson.py")
        if not os.path.isfile(lesson_file):
            continue  # skip folders without content yet

        tid = entry  # folder name IS the topic ID

        # Dynamically import sub-modules
        lesson_mod = importlib.import_module(f".{tid}.lesson", package="modules")
        sections   = getattr(lesson_mod, "SECTIONS", [])

        checks_mod = None
        try:
            checks_mod = importlib.import_module(f".{tid}.checks", package="modules")
        except (ModuleNotFoundError, ImportError):
            pass
        checks = getattr(checks_mod, "CHECKS", []) if checks_mod else []

        quiz_mod = None
        try:
            quiz_mod = importlib.import_module(f".{tid}.quiz", package="modules")
        except (ModuleNotFoundError, ImportError):
            pass
        quiz = getattr(quiz_mod, "QUIZ", []) if quiz_mod else []

        # Combine: embed check questions back into their corresponding sections
        result_sections = []
        for i, sec in enumerate(sections):
            s = dict(sec)
            if i < len(checks) and checks[i]:
                s["check"] = checks[i]
            else:
                s["check"] = None
            result_sections.append(s)

        lessons[tid] = {
            "sections": result_sections,
            "quiz": quiz,
        }
    return lessons


LESSONS = _load_lessons()
