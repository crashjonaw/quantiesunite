"""02. The Ten Digits — Check questions."""

CHECKS = [
    {
        "q": 'How many digits are there in our number system?',
        "hint": 'The digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Count them!',
        "options": [
            {"text": '10', "correct": True},
            {"text": '11', "correct": False},
            {"text": '8', "correct": False},
            {"text": '12', "correct": False},
        ]
    },
    {
        "q": 'Why do we use 10 digits?',
        "hint": 'How many fingers do you have on both hands?',
        "options": [
            {"text": 'because 10 is the biggest number', "correct": False},
            {"text": 'because 10 comes after 9', "correct": False},
            {"text": 'because humans have 10 fingers, base-10 system', "correct": True},
            {"text": 'because it is easy to remember', "correct": False},
        ]
    },
    {
        "q": 'How many different digits are in the number 717?',
        "hint": "What are the different symbols? 7 and 1. The 7 appears twice, but it's the same digit.",
        "options": [
            {"text": '12', "correct": False},
            {"text": '0', "correct": False},
            {"text": '1', "correct": False},
            {"text": '2', "correct": True},
        ]
    },
]
