CHECKS = [
    {
        "q": 'If P(event) = 0.3, what is P(NOT event)?',
        "hint": 'Use the complement rule: P(NOT event) = 1 - P(event) = 1 - 0.3 = 0.7',
        "options": [
            {"text": '1.2', "correct": False},
            {"text": '0.19999999999999996', "correct": False},
            {"text": '1', "correct": False},
            {"text": '0.7', "correct": True},
        ]
    },
    {
        "q": 'A spinach has 4 equal sections: red, blue, green, yellow. What is P(red OR yellow)?',
        "hint": 'Red and yellow are 2 out of 4 sections. P(R or Y) = 2/4 = 1/2',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": '2/4 = 1/2 (or 0.5 or 50%)', "correct": True},
        ]
    },
    {
        "q": "A weather forecast says there's a 35% chance of rain. What is P(no rain)?",
        "hint": 'No rain is the complement of rain. P(no rain) = 1 - 0.35 = 0.65',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": '0.65 or 65%', "correct": True},
            {"text": 'None of the above', "correct": False},
        ]
    },
    {
        "q": 'Is a probability of 0.05 more likely or unlikely?',
        "hint": '0.05 is much closer to 0 (impossible) than to 1 (certain)',
        "options": [
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'Unlikely (very unlikely, actually - only 5%)', "correct": True},
            {"text": 'All of the above', "correct": False},
        ]
    },
    {
        "q": 'If P(passing a test) = 7/10, what is P(failing)?',
        "hint": 'Failing is the complement of passing. 1 - 7/10 = 3/10',
        "options": [
            {"text": '4/10', "correct": False},
            {"text": '1/10', "correct": False},
            {"text": '2/10', "correct": False},
            {"text": '3/10', "correct": True},
        ]
    },
]
