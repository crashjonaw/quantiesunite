"""Subtraction on a Number Line — Check questions."""

CHECKS = [
    {
        "q": 'Use a number line. Start at 8, jump back 3. Where do you land?',
        "hint": "Start at 8. Jump back 1 (land on 7), jump back 1 more (land on 6), jump back 1 more (land on 5). You've jumped back 3 times.",
        "options": [
            {"text": '5', "correct": True},
            {"text": '4', "correct": False},
            {"text": '15', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": '6 − 2 = ?  (Use a number line if you need to.)',
        "hint": 'Start at 6, count back 2: 5, 4. Land on 4.',
        "options": [
            {"text": '4', "correct": True},
            {"text": '8', "correct": False},
            {"text": '6', "correct": False},
            {"text": '14', "correct": False},
        ]
    },
    {
        "q": 'Use a number line. Start at 9, jump back 5. Where do you land?',
        "hint": 'Count back from 9: 8, 7, 6, 5, 4. Five jumps backward.',
        "options": [
            {"text": '4', "correct": True},
            {"text": '14', "correct": False},
            {"text": '8', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": 'On a number line, if you start at 10 and jump back 1, what number do you land on?',
        "hint": 'One jump back from 10 brings you to 9.',
        "options": [
            {"text": '8', "correct": False},
            {"text": '11', "correct": False},
            {"text": '19', "correct": False},
            {"text": '9', "correct": True},
        ]
    },
]
