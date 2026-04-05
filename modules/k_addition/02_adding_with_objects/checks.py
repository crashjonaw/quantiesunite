"""Concept 2: Adding with Objects — Checks."""

CHECKS = [
    {
        "q": 'Draw circles to show 2 + 3. How many circles do you have altogether?',
        "hint": 'Draw 2 circles, then 3 more circles. Count them all.',
        "options": [
            {"text": '6', "correct": False},
            {"text": '5', "correct": True},
            {"text": '4', "correct": False},
            {"text": '15', "correct": False},
        ]
    },
    {
        "q": 'Use your fingers. Hold up 1 on one hand and 4 on the other. How many fingers?',
        "hint": 'Count all your fingers: 1, 2, 3, 4, 5.',
        "options": [
            {"text": '5', "correct": True},
            {"text": '15', "correct": False},
            {"text": '4', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": '3 + 1 = ?',
        "hint": 'Start at 3 and count on 1 more: 4.',
        "options": [
            {"text": '6', "correct": False},
            {"text": '4', "correct": True},
            {"text": '14', "correct": False},
            {"text": '8', "correct": False},
        ]
    },
]
