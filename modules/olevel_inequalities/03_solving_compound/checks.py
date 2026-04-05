CHECKS = [
    {
        "q": 'Does \\(x > 3\\) AND \\(x < 1\\) have any solutions? Explain.',
        "hint": "AND means both conditions must be true. Look for the overlap. If there's no overlap, no solution.",
        "options": [
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
            {"text": 'No solutions (empty set). A number cannot be both greater than 3 and less than 1.', "correct": True},
            {"text": 'It depends on how fast you count', "correct": False},
            {"text": 'Yes, it is the same thing', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(-5 < 3x + 1 \\leq 10\\)',
        "hint": 'Subtract 1 from all parts, then divide by 3. No sign reversal (positive division).',
        "options": [
            {"text": '\\(-5 < x \\leq 10\\) (didn\'t subtract)', "correct": False},
            {"text": '\\(-2 < x \\leq 3\\) or \\((-2, 3]\\)', "correct": True},
            {"text": '\\(-2 < x < 3\\) (forgot equality)', "correct": False},
            {"text": '\\(-6 < x \\leq 9\\) (calc error)', "correct": False},
        ]
    },
    {
        "q": 'Solve \\(|x + 2| > 3\\)',
        "hint": 'Absolute value > leads to OR. Split: (x+2) > 3 gives x > 1, and (x+2) < -3 gives x < -5.',
        "options": [
            {"text": '\\(-5 \\leq x \\leq 1\\) (AND instead of OR)', "correct": False},
            {"text": '\\(x < -5\\) OR \\(x > 1\\), written as \\((-\\infty, -5) \\cup (1, \\infty)\\)', "correct": True},
            {"text": '\\(x > 3\\) or \\(x < -3\\) (wrong calculation)', "correct": False},
            {"text": '\\(-5 < x < 1\\) (wrong type)', "correct": False},
        ]
    },
    {
        "q": 'Find all integer solutions to \\(0 \\leq x < 3.5\\)',
        "hint": 'List all whole numbers from 0 (included) up to 3.5 (excluded). So 0, 1, 2, 3.',
        "options": [
            {"text": '\\(\\{0, 1, 2, 3, 4\\}\\) (included 4)', "correct": False},
            {"text": '\\(\\{0, 1, 2, 3\\}\\)', "correct": True},
            {"text": '\\(\\{1, 2, 3\\}\\) (forgot 0)', "correct": False},
            {"text": '\\(\\{0, 1, 2\\}\\) (forgot 3)', "correct": False},
        ]
    },
]
