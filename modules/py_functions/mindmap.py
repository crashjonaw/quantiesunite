MINDMAP = {
    "concepts": [
        {"title": "Defining Functions", "points": [
            "def function_name(params): ... return value",
            "Parameters can have defaults: def greet(name='World')",
            "Functions are first-class objects — can be passed as arguments",
        ]},
        {"title": "Arguments", "points": [
            "Positional: f(1, 2) — order matters",
            "Keyword: f(x=1, y=2) — order doesn't matter",
            "*args: variable positional args (tuple)",
            "**kwargs: variable keyword args (dict)",
        ]},
        {"title": "Scope", "points": [
            "Local variables: defined inside a function",
            "Global variables: defined at module level, use 'global' keyword to modify",
            "LEGB rule: Local → Enclosing → Global → Built-in",
        ]},
        {"title": "Modules & Imports", "points": [
            "import math, from math import sqrt",
            "import module as alias: import numpy as np",
            "Create your own: any .py file is a module",
            "__name__ == '__main__' guard for scripts",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Functions should do one thing well — keep them short and focused",
        "Use docstrings to document: def f(x): '''Doubles x.''' return x*2",
        "Avoid mutable default arguments: def f(lst=[]) is a common bug — use None instead",
    ],
}
