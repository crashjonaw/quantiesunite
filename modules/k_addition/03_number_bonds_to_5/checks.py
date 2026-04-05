"""Concept 3: Number Bonds to 5 — Checks."""

CHECKS = [
    {
        "q": 'If 5 = 3 + ?, what is the missing number?',
        "hint": 'Count on from 3: 4, 5. You counted 2 more.',
        "options": [
            {"text": '2', "correct": True},
            {"text": '1', "correct": False},
            {"text": '0', "correct": False},
            {"text": '12', "correct": False},
        ]
    },
    {
        "q": '2 + 3 = ? and 3 + 2 = ? Are they the same?',
        "hint": "Order doesn't matter in addition. Both equal 5.",
        "options": [
            {"text": 'It depends on the situation', "correct": False},
            {"text": 'No, they are completely different', "correct": False},
            {"text": 'yes', "correct": True},
            {"text": 'Only sometimes', "correct": False},
        ]
    },
    {
        "q": 'How many different ways can you make 5 by adding two numbers?',
        "hint": 'Count them: 0+5, 1+4, 2+3, 3+2, 4+1, 5+0.',
        "options": [
            {"text": '12', "correct": False},
            {"text": '6', "correct": True},
            {"text": '8', "correct": False},
            {"text": '7', "correct": False},
        ]
    },
]
