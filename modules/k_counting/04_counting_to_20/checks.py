"""Counting to 20 — Concept checks."""

CHECKS = [
    {
        "q": 'What is the counting sequence from 11 to 20?',
        "hint": "Remember the 'teen' numbers and the pattern.",
        "options": [
            {"text": '11, 12, 13, 14, 15, 16, 17, 18, 19, 20', "correct": True},
            {"text": '11, 12, 13, 14, 15, 16, 17, 18, 20, 21', "correct": False},
            {"text": '10, 11, 12, 13, 14, 15, 16, 17, 18, 19', "correct": False},
            {"text": '20, 19, 18, 17, 16, 15, 14, 13, 12, 11', "correct": False},
        ]
    },
    {
        "q": 'If you have a group of 10 and 7 more, what is the total?',
        "hint": 'Count on from 10: 10... 11, 12, 13, 14, 15, 16, 17',
        "options": [
            {"text": '15', "correct": False},
            {"text": '17', "correct": True},
            {"text": '34', "correct": False},
            {"text": '19', "correct": False},
        ]
    },
    {
        "q": 'What comes before 18 in the counting sequence?',
        "hint": 'Think about the sequence: 16, 17, 18...',
        "options": [
            {"text": '19', "correct": False},
            {"text": '15', "correct": False},
            {"text": '34', "correct": False},
            {"text": '17', "correct": True},
        ]
    },
]
