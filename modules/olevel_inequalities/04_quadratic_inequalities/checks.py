CHECKS = [
    {
        "q": 'Solve \\(x^2 - 9 < 0\\)',
        "hint": 'Factor as (x-3)(x+3) < 0. Roots at -3 and 3. Middle region is negative (e.g., test x=0 gives -9).',
        "options": [
            {"text": '\\(x < -3\\) or \\(x > 3\\) (outside regions)', "correct": False},
            {"text": '\\(-3 < x < 3\\) or \\((-3, 3)\\)', "correct": True},
            {"text": '\\(-3 \\leq x \\leq 3\\) (wrong brackets)', "correct": False},
            {"text": '\\(x > -3\\) or \\(x < 3\\) (both true always)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(x^2 + 2x - 8 > 0\\)',
        "hint": 'Factor: (x+4)(x-2) > 0. Roots at -4 and 2. Select + regions: left and right of the roots.',
        "options": [
            {"text": '\\(-4 < x < 2\\) (middle region)', "correct": False},
            {"text": '\\(x < -4\\) OR \\(x > 2\\), i.e., \\((-\\infty, -4) \\cup (2, \\infty)\\)', "correct": True},
            {"text": '\\(-4 \\leq x \\leq 2\\) (with equality)', "correct": False},
            {"text": '\\(x > -4\\) and \\(x > 2\\) (wrong logic)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\((x - 5)^2 \\leq 0\\)',
        "hint": 'A square is always ≥ 0. It equals 0 only when x = 5. So the solution is just the single point x = 5.',
        "options": [
            {"text": '\\(x \\leq 5\\) (forgot squared)', "correct": False},
            {"text": '\\(x = 5\\) (only solution)', "correct": True},
            {"text": 'All real numbers (no limit)', "correct": False},
            {"text": 'No solution (empty set)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\((x + 1)(x - 2)(x - 4) \\geq 0\\)',
        "hint": 'Roots at -1, 2, 4. Sign pattern: −, +, −, +. Inequality ≥ 0 selects non-negative regions and the roots themselves.',
        "options": [
            {"text": '\\((-\\infty, -1] \\cup [2, 4]\\) (wrong regions)', "correct": False},
            {"text": '\\([-1, 2] \\cup [4, \\infty)\\)', "correct": True},
            {"text": '\\([-1, 4]\\) (single interval)', "correct": False},
            {"text": '\\((-1, 2) \\cup (4, \\infty)\\) (open brackets)', "correct": False},
        ]
    },
]
