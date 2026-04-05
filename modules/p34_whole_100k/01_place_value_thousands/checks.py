CHECKS = [
    {
        "q": 'What is the value of the digit 7 in the number 7,234?',
        "hint": 'The digit 7 is in the thousands place. The thousands place means groups of 1,000, so 7 in the thousands place = 7 × 1,000 = 7,000.',
        "options": [
            {"text": '7,000 (seven thousands)', "correct": True},
            {"text": '700 (seven hundreds)', "correct": False},
            {"text": '7 (just seven ones)', "correct": False},
            {"text": '70 (seven tens)', "correct": False},
        ]
    },
    {
        "q": 'Write the number five thousand, three hundred twenty-one in digits.',
        "hint": 'Five thousand = 5,000. Three hundred twenty-one = 321. Put them together: 5,321',
        "options": [
            {"text": '5,321', "correct": True},
            {"text": '5,312', "correct": False},
            {"text": '3,215', "correct": False},
            {"text": '5,123', "correct": False},
        ]
    },
    {
        "q": 'Skip count by thousands. What is the 6th number? (Start: 0, 1,000, 2,000...)',
        "hint": 'Count: 0 (1st), 1,000 (2nd), 2,000 (3rd), 3,000 (4th), 4,000 (5th), 5,000 (6th)',
        "options": [
            {"text": '5,000', "correct": True},
            {"text": '6,000', "correct": False},
            {"text": '4,000', "correct": False},
            {"text": '2,000', "correct": False},
        ]
    },
    {
        "q": 'Break down 4,562 into expanded form.',
        "hint": '4 is in the thousands place = 4,000. 5 is in the hundreds place = 500. 6 is in the tens place = 60. 2 is in the ones place = 2.',
        "options": [
            {"text": '4,000 + 500 + 60 + 2', "correct": True},
            {"text": '4 + 5 + 6 + 2', "correct": False},
            {"text": '4,000 + 50 + 6 + 2', "correct": False},
            {"text": '4,000 + 500 + 6 + 20', "correct": False},
        ]
    },
    {
        "q": 'Which is larger: 3,999 or 4,000?',
        "hint": '3,999 has a 3 in the thousands place, but 4,000 has a 4 in the thousands place. Since 4 > 3, 4,000 is larger.',
        "options": [
            {"text": '4,000', "correct": True},
            {"text": '3,999', "correct": False},
            {"text": 'They are equal.', "correct": False},
            {"text": '3,999 is larger by 1.', "correct": False},
        ]
    },
]
