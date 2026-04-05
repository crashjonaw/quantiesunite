CHECKS = [
    {
        "q": 'Solve \\(2x + 5 > 13\\)',
        "hint": 'Subtract 5, then divide by 2. No sign reversal needed (dividing by positive).',
        "options": [
            {"text": '\\(x > 8\\) (forgot to divide)', "correct": False},
            {"text": '\\(x > 4\\) or \\((4, \\infty)\\)', "correct": True},
            {"text": '\\(x < 4\\) (flipped sign)', "correct": False},
            {"text": '\\(x > 3.6\\) (calculation error)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(-3x \\leq 9\\)',
        "hint": 'Divide by -3 and REVERSE the inequality sign.',
        "options": [
            {"text": '\\(x \\leq -3\\) (forgot to flip)', "correct": False},
            {"text": '\\(x \\geq -3\\) or \\([-3, \\infty)\\)', "correct": True},
            {"text": '\\(x \\geq 3\\) (wrong sign)', "correct": False},
            {"text": '\\(x < -3\\) (wrong direction)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(4x - 7 < 2x + 5\\)',
        "hint": 'Move variables left, constants right. 4x - 2x gives 2x.',
        "options": [
            {"text": '\\(x < 12\\) (calc error)', "correct": False},
            {"text": '\\(x > 6\\) (flipped)', "correct": False},
            {"text": '\\(x < 6\\) or \\((-\\infty, 6)\\)', "correct": True},
            {"text": '\\(x < 3\\) (wrong calculation)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(5(x - 2) \\geq 3x - 4\\)',
        "hint": 'Expand 5(x-2) to 5x - 10. Then: 5x - 10 ≥ 3x - 4 becomes 2x ≥ 6.',
        "options": [
            {"text": '\\(x \\geq 3\\) or \\([3, \\infty)\\)', "correct": True},
            {"text": '\\(x \\leq 3\\) (flipped)', "correct": False},
            {"text": '\\(x \\geq 6\\) (calc error)', "correct": False},
            {"text": '\\(x > 3\\) (not equal)', "correct": False},
        ]
    },
]
