"""Concept 4: Number Bonds to 10 — Checks."""

CHECKS = [
    {
        "q": 'What two numbers add to make 10? One is 7, the other is ?',
        "hint": '7 + ? = 10. Count on from 7: 8, 9, 10.',
        "options": [
            {"text": '3', "correct": True},
            {"text": '13', "correct": False},
            {"text": '1', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": 'Is 4 + 6 = 10 the same as 6 + 4 = 10?',
        "hint": "Order doesn't matter in addition.",
        "options": [
            {"text": 'Only sometimes', "correct": False},
            {"text": 'yes', "correct": True},
            {"text": 'No, they are completely different', "correct": False},
            {"text": 'It depends on the situation', "correct": False},
        ]
    },
    {
        "q": 'What is 5 + 5?',
        "hint": 'This is the middle number bond. Both parts are equal.',
        "options": [
            {"text": '12', "correct": False},
            {"text": '8', "correct": False},
            {"text": '11', "correct": False},
            {"text": '10', "correct": True},
        ]
    },
]
