"""
QuantiesUnite — Per-topic module loader (v2: sub-concept support).

Each topic folder under modules/ can be structured in one of two ways:

  FLAT (legacy):
    modules/<tid>/
      lesson.py   → SECTIONS list
      checks.py   → CHECKS list  (optional)
      quiz.py     → QUIZ list    (optional)

  CONCEPT (new):
    modules/<tid>/
      <concept_id>/         e.g. 01_what_are_numbers/
        lesson.py  → SECTIONS list
        checks.py  → CHECKS list  (optional)
      <concept_id>/
        ...
      quiz.py               → Final module QUIZ (at module level)

LESSONS dict structure:
  LESSONS[tid] = {
      "type": "flat" | "concepts",
      "sections": [...],          # flat only
      "concepts": [...],          # concept only — list of concept dicts
      "quiz": [...],              # always present
  }

  Each concept dict:
  {
      "id": "01_what_are_numbers",
      "title": "What Are Numbers?",   # from TITLE var in lesson.py, or auto-derived
      "sections": [...],              # list of {title, body, check}
  }
"""

import os
import importlib

_DIR = os.path.dirname(__file__)


def _concept_title_from_id(concept_id):
    """Convert '01_what_are_numbers' → 'What Are Numbers'."""
    parts = concept_id.split("_", 1)
    if len(parts) == 2 and parts[0].isdigit():
        name = parts[1]
    else:
        name = concept_id
    return name.replace("_", " ").title()


def _load_flat(tid, folder):
    """Load a legacy flat module (lesson.py at module root)."""
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

    # Embed check questions into sections
    result_sections = []
    for i, sec in enumerate(sections):
        s = dict(sec)
        s["check"] = checks[i] if i < len(checks) and checks[i] else None
        result_sections.append(s)

    return {
        "type": "flat",
        "sections": result_sections,
        "concepts": [],
        "quiz": quiz,
    }


def _load_concepts(tid, folder, concept_dirs):
    """Load a concept-structured module (sub-folders with lesson.py)."""
    concepts = []
    for concept_id in concept_dirs:
        concept_path = os.path.join(folder, concept_id)
        mod_path = f".{tid}.{concept_id}.lesson"
        try:
            lesson_mod = importlib.import_module(mod_path, package="modules")
        except (ModuleNotFoundError, ImportError, SyntaxError) as e:
            print(f"  [WARN] Could not load {mod_path}: {e}")
            continue

        sections = getattr(lesson_mod, "SECTIONS", [])
        title = getattr(lesson_mod, "TITLE", _concept_title_from_id(concept_id))

        checks_mod = None
        try:
            checks_mod = importlib.import_module(
                f".{tid}.{concept_id}.checks", package="modules")
        except (ModuleNotFoundError, ImportError):
            pass
        checks = getattr(checks_mod, "CHECKS", []) if checks_mod else []

        # Embed checks
        result_sections = []
        for i, sec in enumerate(sections):
            s = dict(sec)
            s["check"] = checks[i] if i < len(checks) and checks[i] else None
            result_sections.append(s)

        concepts.append({
            "id":       concept_id,
            "title":    title,
            "sections": result_sections,
        })

    # Module-level quiz (in <tid>/quiz.py)
    quiz_mod = None
    try:
        quiz_mod = importlib.import_module(f".{tid}.quiz", package="modules")
    except (ModuleNotFoundError, ImportError):
        pass
    quiz = getattr(quiz_mod, "QUIZ", []) if quiz_mod else []

    return {
        "type": "concepts",
        "sections": [],
        "concepts": concepts,
        "quiz": quiz,
    }


def _load_lessons():
    """Scan every subfolder and load lessons (flat or concept-structured)."""
    lessons = {}
    for entry in sorted(os.listdir(_DIR)):
        folder = os.path.join(_DIR, entry)
        if not os.path.isdir(folder):
            continue
        if entry.startswith("__"):
            continue

        # Detect concept sub-folders: direct child dirs that contain lesson.py
        concept_dirs = []
        for sub in sorted(os.listdir(folder)):
            sub_path = os.path.join(folder, sub)
            if (os.path.isdir(sub_path) and
                    not sub.startswith("__") and
                    os.path.isfile(os.path.join(sub_path, "lesson.py"))):
                concept_dirs.append(sub)

        if concept_dirs:
            # New concept structure
            lessons[entry] = _load_concepts(entry, folder, concept_dirs)
        elif os.path.isfile(os.path.join(folder, "lesson.py")):
            # Legacy flat structure
            try:
                lessons[entry] = _load_flat(entry, folder)
            except (ModuleNotFoundError, ImportError, SyntaxError, NameError) as e:
                print(f"  [WARN] Could not load {entry}: {e}")
        # else: folder exists but no lesson content — skip silently

    return lessons


LESSONS = _load_lessons()
