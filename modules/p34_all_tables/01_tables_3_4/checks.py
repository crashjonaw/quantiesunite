CHECKS = [
    {
        "q": 'What is 3 × 7?',
        "hint": 'Count: 3, 6, 9, 12, 15, 18, 21. Or use the digit pattern: 2 + 1 = 3, so 21 is divisible by 3.',
        "options": [
            {"text": '21', "correct": True},
            {"text": '42', "correct": False},
            {"text": '28', "correct": False},
            {"text": '24', "correct": False},
        ]
    },
    {
        "q": 'If you know 2 × 5 = 10, what is 4 × 5?',
        "hint": 'Remember, 4 is just 2 doubled! So 4 × 5 = (2 × 5) + (2 × 5) = 10 + 10 = 20',
        "options": [
            {"text": '20', "correct": True},
            {"text": '10', "correct": False},
            {"text": '40', "correct": False},
            {"text": '25', "correct": False},
        ]
    },
    {
        "q": 'Which times table fact is wrong: 3 × 6 = 18 or 3 × 8 = 25?',
        "hint": "Use the digit sum trick: if digits don't add to 3, 6, or 9, it's not a 3 times table fact.",
        "options": [
            {"text": '3 × 8 = 25 is wrong. 3 × 8 = 24, and the digit sum is 2 + 4 = 6 (divisible by 3).', "correct": True},
            {"text": '3 × 6 = 18 is wrong. 3 × 6 = 20.', "correct": False},
            {"text": 'Both facts are correct.', "correct": False},
            {"text": 'Both facts are wrong.', "correct": False},
        ]
    },
    {
        "q": 'What is 4 × 9?',
        "hint": 'Think: 2 × 9 = 18, so 4 × 9 = 18 × 2 = 36',
        "options": [
            {"text": '36', "correct": True},
            {"text": '32', "correct": False},
            {"text": '40', "correct": False},
            {"text": '45', "correct": False},
        ]
    },
    {
        "q": 'How are the 2, 4, and 8 times tables related?',
        "hint": '2 × 5 = 10, 4 × 5 = 20, 8 × 5 = 40. See the pattern?',
        "options": [
            {"text": '4 is 2 doubled, and 8 is 4 doubled. Each table is double the previous one.', "correct": True},
            {"text": 'They all end with the same digit.', "correct": False},
            {"text": 'They add up to the 14 times table.', "correct": False},
            {"text": 'They decrease by 2 each time.', "correct": False},
        ]
    },
]
