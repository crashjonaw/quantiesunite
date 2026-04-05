"""Counting to 10 — Concept checks."""

CHECKS = [
    {
        "q": 'What is the sequence of numbers from 1 to 10 in order?',
        "hint": 'Say it slowly and carefully.',
        "options": [
            {"text": '1, 2, 3, 4, 5, 6, 7, 8, 9, 10', "correct": True},
            {"text": '1, 2, 3, 4, 5, 6, 7, 8, 9, 11', "correct": False},
            {"text": '10, 9, 8, 7, 6, 5, 4, 3, 2, 1', "correct": False},
            {"text": '1, 2, 3, 4, 5, 6, 7, 8, 10, 11', "correct": False},
        ]
    },
    {
        "q": 'If the sequence is 4, 5, 6, 7, what number comes next?',
        "hint": 'What comes after 7 in the counting sequence?',
        "options": [
            {"text": '6', "correct": False},
            {"text": '18', "correct": False},
            {"text": '7', "correct": False},
            {"text": '8', "correct": True},
        ]
    },
    {
        "q": 'Count these objects and tell how many: 🍎🍎🍎🍎🍎',
        "hint": 'Point to each apple and count: 1, 2, 3...',
        "options": [
            {"text": '6', "correct": False},
            {"text": '5', "correct": True},
            {"text": '15', "correct": False},
            {"text": '4', "correct": False},
        ]
    },
]
