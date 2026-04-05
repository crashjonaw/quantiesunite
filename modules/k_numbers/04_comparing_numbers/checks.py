"""04. Comparing Numbers — Check questions."""

CHECKS = [
    {
        "q": 'Which is bigger: 12 or 9? Write the symbol too (< or >).',
        "hint": '12 is bigger than 9. The > symbol opens toward the bigger number (12).',
        "options": [
            {"text": '9', "correct": False},
            {"text": '12, 12 > 9', "correct": True},
            {"text": "can't tell from the numbers", "correct": False},
            {"text": 'they are the same', "correct": False},
        ]
    },
    {
        "q": 'Write the correct symbol for: 5 __ 5',
        "hint": 'When two numbers are the same, use the equals sign.',
        "options": [
            {"text": 'they are the same', "correct": False},
            {"text": '9', "correct": False},
            {"text": '=', "correct": True},
            {"text": "can't tell from the numbers", "correct": False},
        ]
    },
    {
        "q": 'Is 3 < 10 true or false?',
        "hint": "3 is less than 10, so yes, it's true.",
        "options": [
            {"text": 'true', "correct": True},
            {"text": 'they are the same', "correct": False},
            {"text": "can't tell from the numbers", "correct": False},
            {"text": '9', "correct": False},
        ]
    },
]
