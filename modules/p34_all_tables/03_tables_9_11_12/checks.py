CHECKS = [
    {
        "q": 'What is 9 × 8?',
        "hint": 'Check using the 9-pattern: 7 + 2 = 9. Use the finger trick: put down finger 8, count 7 left and 2 right = 72.',
        "options": [
            {"text": '72', "correct": True},
            {"text": '63', "correct": False},
            {"text": '81', "correct": False},
            {"text": '80', "correct": False},
        ]
    },
    {
        "q": 'What is 11 × 6?',
        "hint": 'With the 11 times table, the digit repeats for single digits. 11 × 6 means 6 repeated = 66',
        "options": [
            {"text": '66', "correct": True},
            {"text": '60', "correct": False},
            {"text": '72', "correct": False},
            {"text": '77', "correct": False},
        ]
    },
    {
        "q": 'If 10 × 5 = 50 and 2 × 5 = 10, what is 12 × 5?',
        "hint": '12 × 5 = (10 × 5) + (2 × 5) = 50 + 10 = 60',
        "options": [
            {"text": '60', "correct": True},
            {"text": '50', "correct": False},
            {"text": '70', "correct": False},
            {"text": '62', "correct": False},
        ]
    },
    {
        "q": 'Which digit sum test would work for 9 × 3 = 27?',
        "hint": "That's the special 9-pattern! The digits always add to 9.",
        "options": [
            {"text": '2 + 7 = 9 (all 9 times table answers have digits that sum to 9)', "correct": True},
            {"text": '2 + 7 = 9 only works for 9 × 3.', "correct": False},
            {"text": 'All 9 times table answers end in 9.', "correct": False},
            {"text": '9 × 3 = 27 is wrong; it should be 25.', "correct": False},
        ]
    },
    {
        "q": 'What is 12 × 8?',
        "hint": 'Use 12 = 10 + 2: (10 × 8) + (2 × 8) = 80 + 16 = 96',
        "options": [
            {"text": '96', "correct": True},
            {"text": '80', "correct": False},
            {"text": '88', "correct": False},
            {"text": '104', "correct": False},
        ]
    },
]
