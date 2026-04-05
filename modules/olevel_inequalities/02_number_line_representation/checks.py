CHECKS = [
    {
        "q": 'When graphing \\(x \\geq 5\\), should you use an open or closed circle at 5?',
        "hint": "The \\(\\geq\\) symbol means 'greater than or EQUAL to', so 5 is included.",
        "options": [
            {"text": 'Open circle (for strict > symbol)', "correct": False},
            {"text": 'Closed circle (the endpoint IS included in the solution)', "correct": True},
            {"text": 'Half-filled circle', "correct": False},
            {"text": 'No symbol needed', "correct": False},
        ]
    },
    {
        "q": 'Convert \\(2 < x \\leq 7\\) to interval notation',
        "hint": 'Open at 2 (strict inequality), closed at 7 (equal allowed). So ( on left, ] on right.',
        "options": [
            {"text": '[2, 7] (both closed)', "correct": False},
            {"text": '(2, 7) (both open)', "correct": False},
            {"text": '[2, 7) (wrong brackets)', "correct": False},
            {"text": '\\((2, 7]\\)', "correct": True},
        ]
    },
    {
        "q": 'Express in interval notation: \\(x < -1\\) OR \\(x \\geq 3\\)',
        "hint": 'Two separate regions, so use the union symbol ∪. Left side is open (strict <), right side is closed (≥).',
        "options": [
            {"text": '[-1, 3] (single interval)', "correct": False},
            {"text": '(-1, 3) (wrong region)', "correct": False},
            {"text": '[3, ∞) (only right side)', "correct": False},
            {"text": '\\((-\\infty, -1) \\cup [3, \\infty)\\)', "correct": True},
        ]
    },
    {
        "q": 'A number line shows a closed circle at 0 and a closed circle at 5, with shading between. Write the inequality',
        "hint": 'Both circles are closed, so both endpoints are included. Use ≤ on both sides.',
        "options": [
            {"text": '\\(0 < x < 5\\) (open circles)', "correct": False},
            {"text": '\\(0 \\leq x < 5\\) (right open)', "correct": False},
            {"text": '\\(0 < x \\leq 5\\) (left open)', "correct": False},
            {"text": '\\(0 \\leq x \\leq 5\\) or in interval notation \\([0, 5]\\)', "correct": True},
        ]
    },
]
