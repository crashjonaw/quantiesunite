"""
QuantiesUnite — Mindmap data loader.

Each module can have a mindmap.py file in its modules/<tid>/ folder:

    modules/<tid>/mindmap.py:
        MINDMAP = {
            "concepts": [
                {"title": "Concept Name", "points": ["point 1", "point 2", ...]},
                ...
            ],
            "formulas": [
                {"label": "Formula Name", "expr": "\\(E = mc^2\\)"},
                ...
            ],
            "tips": [
                "Key takeaway 1",
                "Key takeaway 2",
                ...
            ],
        }
"""

import os
import importlib

_MINDMAPS = {}


def _load_mindmaps():
    """Scan modules/ for mindmap.py files and load them."""
    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    for entry in sorted(os.listdir(modules_dir)):
        folder = os.path.join(modules_dir, entry)
        if not os.path.isdir(folder) or entry.startswith("__"):
            continue
        mindmap_file = os.path.join(folder, "mindmap.py")
        if os.path.isfile(mindmap_file):
            try:
                mod = importlib.import_module(f"modules.{entry}.mindmap")
                data = getattr(mod, "MINDMAP", None)
                if data:
                    _MINDMAPS[entry] = data
            except (ModuleNotFoundError, ImportError, SyntaxError) as e:
                print(f"  [WARN] Could not load mindmap for {entry}: {e}")


_load_mindmaps()


def get_mindmap(tid):
    """Return the mindmap data for a topic, or None if not available."""
    return _MINDMAPS.get(tid)
