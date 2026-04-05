CHECKS = [
    {
        "q": 'Find the mean of: 12, 15, 18, 21, 24',
        "hint": 'Sum: 12 + 15 + 18 + 21 + 24 = 90. Count: 5 values. Mean = 90 ÷ 5 = 18',
        "options": [
            {"text": '19', "correct": False},
            {"text": '17', "correct": False},
            {"text": '18', "correct": True},
            {"text": '36', "correct": False},
        ]
    },
    {
        "q": 'Find the median of: 5, 8, 3, 9, 2, 7, 4',
        "hint": 'Arrange in order: 2, 3, 4, 5, 7, 8, 9. There are 7 values (odd), so median is the 4th value = 5',
        "options": [
            {"text": '5', "correct": True},
            {"text": '4', "correct": False},
            {"text": '6', "correct": False},
            {"text": '15', "correct": False},
        ]
    },
    {
        "q": 'Find the mode of: 2, 2, 2, 3, 4, 4, 5, 6',
        "hint": 'Count frequencies: 2 appears 3 times, 4 appears 2 times, others once. Mode = 2 (highest frequency)',
        "options": [
            {"text": '2', "correct": True},
            {"text": '1', "correct": False},
            {"text": '0', "correct": False},
            {"text": '12', "correct": False},
        ]
    },
    {
        "q": 'A dataset has values 10, 11, 12, 13, 200. Which measure is most affected by the outlier 200?',
        "hint": 'Mean = (10+11+12+13+200)÷5 = 49.2 (pulled up). Median = 12 (unaffected). Mode = no mode.',
        "options": [
            {"text": 'The mean', "correct": True},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'All of the above', "correct": False},
        ]
    },
]
