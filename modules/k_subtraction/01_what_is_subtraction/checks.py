"""What is Subtraction? — Check questions."""

CHECKS = [
    {
        "q": 'If you start with 8 toys and give away 3, how many do you have left?',
        "hint": '8 − 3. Start at 8 and count back 3 steps: 7, 6, 5.',
        "options": [
            {"text": '4', "correct": False},
            {"text": '6', "correct": False},
            {"text": '15', "correct": False},
            {"text": '5', "correct": True},
        ]
    },
    {
        "q": 'What does the − symbol mean?',
        "hint": 'The minus sign shows we are removing or taking away.',
        "options": [
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
            {"text": 'take away', "correct": True},
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'It tells you the starting point of counting', "correct": False},
        ]
    },
    {
        "q": 'You have 9 crayons. You break 2. How many are still good?',
        "hint": '9 − 2 = 7. Start at 9, count back 2.',
        "options": [
            {"text": '7', "correct": True},
            {"text": '8', "correct": False},
            {"text": '14', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": 'In the problem 6 − 1 = 5, what do we call the 6?',
        "hint": 'The minuend is the number we start with (the bigger number).',
        "options": [
            {"text": 'the subtrahend', "correct": False},
            {"text": 'the difference', "correct": False},
            {"text": 'the answer', "correct": False},
            {"text": 'minuend', "correct": True},
        ]
    },
]
