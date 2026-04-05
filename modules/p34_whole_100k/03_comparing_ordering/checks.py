CHECKS = [
    {
        "q": 'Compare these numbers: 42,567 and 42,576. Which is larger?',
        "hint": 'The ten thousands and thousands places are the same (4 and 2). Look at the hundreds place: both have 5. Look at the tens place: 42,567 has 6, but 42,576 has 7. Since 7 > 6, the second number is larger.',
        "options": [
            {"text": '42,576 is larger', "correct": True},
            {"text": '42,567 is larger', "correct": False},
            {"text": 'They are equal.', "correct": False},
            {"text": '42,567 is larger by 9.', "correct": False},
        ]
    },
    {
        "q": 'Order these numbers from least to greatest: 8,234 | 8,342 | 8,243 | 8,324',
        "hint": 'All start with 8, so look at the hundreds place: 2, 3, 2, 3. Those with 2 hundreds (8,234 and 8,243) come first. Compare their tens: 34 vs 43, so 8,234 < 8,243. For the 3-hundreds numbers: 8,324 < 8,342.',
        "options": [
            {"text": '8,234 < 8,243 < 8,324 < 8,342', "correct": True},
            {"text": '8,234 < 8,324 < 8,243 < 8,342', "correct": False},
            {"text": '8,342 < 8,324 < 8,243 < 8,234', "correct": False},
            {"text": 'All four numbers are equal.', "correct": False},
        ]
    },
    {
        "q": 'Which number is larger: 35,999 or 36,001?',
        "hint": 'The ten thousands place is the same (3). Look at the thousands place: 35,999 has 5, but 36,001 has 6. Since 6 > 5, 36,001 is larger.',
        "options": [
            {"text": '36,001 is larger', "correct": True},
            {"text": '35,999 is larger', "correct": False},
            {"text": 'They are equal.', "correct": False},
            {"text": '35,999 is larger by 2.', "correct": False},
        ]
    },
    {
        "q": 'Order from greatest to least: 50,432 | 45,023 | 54,302 | 45,320',
        "hint": 'Look at ten thousands: 5 and 4. The 50,000s and 54,302 come first. Between 54,302 and 50,432, the thousands place: 4 > 0. Among the 45,000s: 45,320 > 45,023 (look at hundreds: 3 > 0).',
        "options": [
            {"text": '54,302 > 50,432 > 45,320 > 45,023', "correct": True},
            {"text": '54,302 > 45,320 > 50,432 > 45,023', "correct": False},
            {"text": '50,432 > 54,302 > 45,320 > 45,023', "correct": False},
            {"text": '45,023 > 45,320 > 50,432 > 54,302', "correct": False},
        ]
    },
    {
        "q": 'Which is smaller: 9,999 or 10,000?',
        "hint": '9,999 has 4 digits, but 10,000 has 5 digits. Any 4-digit number is always smaller than any 5-digit number.',
        "options": [
            {"text": '9,999 is smaller', "correct": True},
            {"text": '10,000 is smaller', "correct": False},
            {"text": 'They are equal.', "correct": False},
            {"text": '10,000 is smaller by 1.', "correct": False},
        ]
    },
]
