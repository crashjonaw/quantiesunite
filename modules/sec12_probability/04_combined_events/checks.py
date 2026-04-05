CHECKS = [
    {
        "q": 'Two fair dice are rolled. What is P(both show a 4)?',
        "hint": 'P(first die is 4) = 1/6. P(second die is 4) = 1/6. P(both) = 1/6 × 1/6 = 1/36',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": '1/36 (or approximately 0.028 or 2.8%)', "correct": True},
            {"text": 'None of the above', "correct": False},
            {"text": 'All of the above', "correct": False},
        ]
    },
    {
        "q": 'What is P(rolling a 2 OR a 5 on a single die)?',
        "hint": 'These are mutually exclusive. P(2 or 5) = P(2) + P(5) = 1/6 + 1/6 = 2/6 = 1/3',
        "options": [
            {"text": 'Something that cannot be measured or described', "correct": False},
            {"text": '2/6 = 1/3 (or approximately 0.33 or 33%)', "correct": True},
            {"text": 'A type of number that only exists in math textbooks', "correct": False},
            {"text": 'A concept with no real-world application', "correct": False},
        ]
    },
    {
        "q": 'A coin is flipped and a spinner with 3 equal sections is spun. How many total outcomes are in the sample space?',
        "hint": 'Coin: 2 outcomes. Spinner: 3 outcomes. Combined: 2 × 3 = 6 total outcomes.',
        "options": [
            {"text": '6 (or 2 × 3 = 6)', "correct": True},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'All of the above', "correct": False},
        ]
    },
    {
        "q": 'A bag has 4 red and 6 blue balls. Pick one, put it back, pick again. What is P(red, then blue)?',
        "hint": 'P(red) = 4/10. P(blue) = 6/10. P(red, then blue) = 4/10 × 6/10',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": '4/10 × 6/10 = 24/100 = 0.24 (or 24%)', "correct": True},
        ]
    },
    {
        "q": 'A die is rolled twice. What is P(first die is even AND second die is even)?',
        "hint": 'P(even) = 3/6 = 1/2 for each die. P(both even) = 1/2 × 1/2 = 1/4',
        "options": [
            {"text": '3/6 × 3/6 = 9/36 = 1/4 (or 0.25 or 25%)', "correct": True},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'All of the above', "correct": False},
        ]
    },
]
