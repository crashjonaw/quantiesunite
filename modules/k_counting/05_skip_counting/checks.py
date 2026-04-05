"""Skip Counting — Concept checks."""

CHECKS = [
    {
        "q": 'What is skip counting?',
        "hint": 'Think about counting by 2s or 5s instead of 1, 2, 3, 4, 5...',
        "options": [
            {"text": 'missing numbers when you count', "correct": False},
            {"text": 'counting slowly', "correct": False},
            {"text": 'counting by ones', "correct": False},
            {"text": 'counting by a certain number over and over, or counting by groups instead of by ones', "correct": True},
        ]
    },
    {
        "q": 'Complete the sequence: 2, 4, 6, 8, __, __, 14',
        "hint": 'When counting by 2s, add 2 each time.',
        "options": [
            {"text": '10, 12', "correct": True},
            {"text": '8, 10', "correct": False},
            {"text": '12, 14', "correct": False},
            {"text": '10, 14', "correct": False},
        ]
    },
    {
        "q": 'If you skip count by 5s, what is the sequence? Give at least 4 numbers.',
        "hint": 'Start at 5 and add 5 each time.',
        "options": [
            {"text": '10, 14', "correct": False},
            {"text": '12, 14', "correct": False},
            {"text": '8, 10', "correct": False},
            {"text": '5, 10, 15, 20', "correct": True},
        ]
    },
]
