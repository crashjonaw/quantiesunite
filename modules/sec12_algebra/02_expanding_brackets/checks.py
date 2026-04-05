"""Expanding Brackets — Mid-lesson checks."""

CHECKS = [
    {
        "q": 'Expand: 3(x + 4)',
        "hint": 'Multiply 3 by each term: 3 times x, and 3 times 4',
        "options": [
            {"text": '3x + 12', "correct": True},
            {"text": '3x + 4', "correct": False},
            {"text": '3x + 3', "correct": False},
            {"text": 'x + 12', "correct": False},
        ]
    },
    {
        "q": 'Expand: 2(3x - 5)',
        "hint": '2 times 3x = 6x, and 2 times -5 = -10',
        "options": [
            {"text": '6x - 10', "correct": True},
            {"text": '6x - 5', "correct": False},
            {"text": '5x - 10', "correct": False},
            {"text": '6x + 10', "correct": False},
        ]
    },
    {
        "q": 'Expand: (x + 2)(x + 4)',
        "hint": 'Use the area model: x*x, x*4, 2*x, 2*4. Then collect like terms.',
        "options": [
            {"text": 'x^2 + 6x + 8', "correct": True},
            {"text": 'x^2 + 8x + 8', "correct": False},
            {"text": 'x^2 + 4x + 8', "correct": False},
            {"text": 'x^2 + 6x + 6', "correct": False},
        ]
    },
    {
        "q": 'Expand: (x - 1)(x + 5)',
        "hint": 'x*x, x*5, -1*x, -1*5. Then simplify 5x - x = 4x',
        "options": [
            {"text": 'x^2 + 4x - 5', "correct": True},
            {"text": 'x^2 + 5x - 5', "correct": False},
            {"text": 'x^2 - 1x - 5', "correct": False},
            {"text": 'x^2 + 6x - 5', "correct": False},
        ]
    },
]
