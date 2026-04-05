"""05. Number Line — Check questions."""

CHECKS = [
    {
        "q": 'On the number line, which is bigger: 15 or 10?',
        "hint": '15 is to the right of 10 on the number line, so 15 is bigger.',
        "options": [
            {"text": '14', "correct": False},
            {"text": '13', "correct": False},
            {"text": '25', "correct": False},
            {"text": '15', "correct": True},
        ]
    },
    {
        "q": 'What number comes right after 19?',
        "hint": 'Look at the number line and find the next mark to the right of 19.',
        "options": [
            {"text": '20', "correct": True},
            {"text": '22', "correct": False},
            {"text": '19', "correct": False},
            {"text": '40', "correct": False},
        ]
    },
    {
        "q": 'If you start at 7 and jump right 3 times, what number do you land on?',
        "hint": '7 + 3 = 10. Jump right once (8), twice (9), three times (10).',
        "options": [
            {"text": '8', "correct": False},
            {"text": '10', "correct": True},
            {"text": '12', "correct": False},
            {"text": '11', "correct": False},
        ]
    },
]
