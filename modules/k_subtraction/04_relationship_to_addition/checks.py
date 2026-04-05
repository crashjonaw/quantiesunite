"""Relationship to Addition — Check questions."""

CHECKS = [
    {
        "q": 'If 4 + 3 = 7, what is 7 − 4?',
        "hint": 'Subtraction undoes addition. If 4 + 3 = 7, then 7 − 4 = 3.',
        "options": [
            {"text": '13', "correct": False},
            {"text": '6', "correct": False},
            {"text": '3', "correct": True},
            {"text": '1', "correct": False},
        ]
    },
    {
        "q": 'If 6 − 2 = 4, which addition fact is true?',
        "hint": 'The fact family for 2, 4, and 6 includes: 2 + 4 = 6 and 4 + 2 = 6.',
        "options": [
            {"text": '2 + 4 = 6', "correct": True},
            {"text": '6 + 2 = 8', "correct": False},
            {"text": '4 + 4 = 8', "correct": False},
            {"text": '2 + 2 = 4', "correct": False},
        ]
    },
    {
        "q": 'Write a subtraction fact from the addition fact 3 + 5 = 8.',
        "hint": 'If 3 + 5 = 8, then 8 − 5 = 3 or 8 − 3 = 5. Either answer works!',
        "options": [
            {"text": '8 − 3 = 5', "correct": False},
            {"text": '8 − 2 = 6', "correct": False},
            {"text": '8 − 5 = 3', "correct": True},
            {"text": '3 − 5 = 2', "correct": False},
        ]
    },
    {
        "q": 'Check: Is 9 − 3 = 6? Use addition: 6 + 3 = ?',
        "hint": 'If 6 + 3 = 9, then 9 − 3 = 6 is correct! ✓',
        "options": [
            {"text": '11', "correct": False},
            {"text": '9', "correct": True},
            {"text": '8', "correct": False},
            {"text": '19', "correct": False},
        ]
    },
]
