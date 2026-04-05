CHECKS = [
    {
        "q": 'What is the value of the digit 3 in the number 35,678?',
        "hint": 'The digit 3 is in the ten thousands place. It represents 3 groups of 10,000, which is 30,000.',
        "options": [
            {"text": '30,000 (three ten-thousands)', "correct": True},
            {"text": '3,000 (three thousands)', "correct": False},
            {"text": '300 (three hundreds)', "correct": False},
            {"text": '3 (just three ones)', "correct": False},
        ]
    },
    {
        "q": 'Write the number forty-two thousand, seven hundred nineteen in digits.',
        "hint": 'Forty-two thousand = 42,000. Seven hundred nineteen = 719. Put them together: 42,719',
        "options": [
            {"text": '42,719', "correct": True},
            {"text": '42,179', "correct": False},
            {"text": '24,719', "correct": False},
            {"text": '42,791', "correct": False},
        ]
    },
    {
        "q": 'Break down 56,234 into expanded form.',
        "hint": '5 in ten thousands = 50,000. 6 in thousands = 6,000. 2 in hundreds = 200. 3 in tens = 30. 4 in ones = 4.',
        "options": [
            {"text": '50,000 + 6,000 + 200 + 30 + 4', "correct": True},
            {"text": '50,000 + 6,000 + 200 + 3 + 4', "correct": False},
            {"text": '5 + 6 + 2 + 3 + 4', "correct": False},
            {"text": '50,000 + 6,000 + 20 + 30 + 4', "correct": False},
        ]
    },
    {
        "q": 'Skip count by ten thousands. Write the sequence: 20,000, _____, 40,000, _____',
        "hint": 'Each step adds 10,000. From 20,000 add 10,000 to get 30,000. From 40,000 add 10,000 to get 50,000.',
        "options": [
            {"text": '20,000, 30,000, 40,000, 50,000', "correct": True},
            {"text": '20,000, 25,000, 40,000, 45,000', "correct": False},
            {"text": '20,000, 40,000, 60,000, 80,000', "correct": False},
            {"text": '20,000, 30,000, 40,000, 60,000', "correct": False},
        ]
    },
    {
        "q": 'Which is larger: 49,999 or 50,000?',
        "hint": '49,999 has 4 in the ten thousands place. 50,000 has 5 in the ten thousands place. Since 5 > 4, 50,000 is larger.',
        "options": [
            {"text": '50,000', "correct": True},
            {"text": '49,999', "correct": False},
            {"text": 'They are equal.', "correct": False},
            {"text": '49,999 is larger by 1.', "correct": False},
        ]
    },
]
