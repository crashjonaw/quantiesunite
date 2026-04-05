CHECKS = [
    {
        "q": 'You roll a standard die. What is the sample space?',
        "hint": 'A standard die has 6 faces. List all possible numbers that can appear.',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": '{1, 2, 3, 4, 5, 6} or any list of all 6 outcomes', "correct": True},
        ]
    },
    {
        "q": 'A die is rolled. What is the probability of getting a number less than 3?',
        "hint": "Numbers less than 3 are: 1 and 2. That's 2 favorable outcomes out of 6 total. P = 2/6 = 1/3",
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": '2/6 = 1/3 (or approximately 0.33 or 33%)', "correct": True},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
        ]
    },
    {
        "q": 'A bag contains 5 red balls, 3 blue balls, and 2 green balls. What is P(picking a red ball)?',
        "hint": 'Total balls: 5 + 3 + 2 = 10. Red balls: 5. P(red) = 5/10 = 1/2',
        "options": [
            {"text": '5/10 = 1/2 (or 0.5 or 50%)', "correct": True},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'All of the above', "correct": False},
        ]
    },
    {
        "q": 'What must be true about the sum of all probabilities in a sample space?',
        "hint": 'Since one outcome must happen, all probabilities together must equal certainty.',
        "options": [
            {"text": 'They must add up to 1 (or 100%)', "correct": True},
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
        ]
    },
    {
        "q": 'A spinner has 4 equal sections: Red, Blue, Green, Yellow. What is P(spinning Red)?',
        "hint": '4 equally likely outcomes, 1 is Red. P(Red) = 1/4',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": '1/4 (or 0.25 or 25%)', "correct": True},
            {"text": 'None of the above', "correct": False},
        ]
    },
]
