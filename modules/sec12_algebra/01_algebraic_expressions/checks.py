"""Algebraic Expressions — Mid-lesson checks."""

CHECKS = [
    {
        "q": 'Simplify: 4x + 3x',
        "hint": 'Add the coefficients: 4 + 3 = 7',
        "options": [
            {"text": '7x', "correct": True},
            {"text": '7', "correct": False},
            {"text": '4x + 3', "correct": False},
            {"text": '12x', "correct": False},
        ]
    },
    {
        "q": 'Simplify: 5y + 2 - 3y - 1',
        "hint": 'Collect like terms: (5y - 3y) + (2 - 1)',
        "options": [
            {"text": '2y + 1', "correct": True},
            {"text": '2y - 1', "correct": False},
            {"text": '8y + 1', "correct": False},
            {"text": '2y', "correct": False},
        ]
    },
    {
        "q": 'Find the value of 2x + 1 when x = 3',
        "hint": 'Replace x with 3: 2(3) + 1 = ? + 1',
        "options": [
            {"text": '7', "correct": True},
            {"text": '6', "correct": False},
            {"text": '8', "correct": False},
            {"text": '14', "correct": False},
        ]
    },
    {
        "q": 'Simplify: 6a + 4b - 2a + b',
        "hint": 'Group the a terms and the b terms separately',
        "options": [
            {"text": '4a + 5b', "correct": True},
            {"text": '4a + 3b', "correct": False},
            {"text": '8a + 5b', "correct": False},
            {"text": '4a + 5', "correct": False},
        ]
    },
]
