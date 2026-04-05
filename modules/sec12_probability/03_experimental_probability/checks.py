CHECKS = [
    {
        "q": 'In 80 coin flips, heads appeared 42 times. What is the experimental P(heads)?',
        "hint": 'Experimental P = (times it happened) / (total trials) = 42/80',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": '42/80 = 0.525 or 52.5%', "correct": True},
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
        ]
    },
    {
        "q": 'What does the Law of Large Numbers tell us?',
        "hint": 'With more data, random fluctuations average out and patterns emerge.',
        "options": [
            {"text": 'As we do more trials, experimental probability gets closer to theoretical probability', "correct": True},
            {"text": 'It tells you the starting point of counting', "correct": False},
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
        ]
    },
    {
        "q": 'A die is rolled 300 times. Number 3 appears 48 times. Is this close to the theoretical P(3) = 1/6?',
        "hint": 'Calculate experimental: 48/300 ≈ 0.16. Compare to theoretical: 1/6 ≈ 0.167. These are very close!',
        "options": [
            {"text": 'Yes. Experimental P(3) = 48/300 = 0.16, and theoretical is 1/6 ≈ 0.167', "correct": True},
            {"text": 'Only sometimes', "correct": False},
            {"text": 'It depends on the situation', "correct": False},
            {"text": 'No, they are completely different', "correct": False},
        ]
    },
    {
        "q": 'Why would you use experimental probability instead of theoretical?',
        "hint": 'If you suspect a coin, die, or spinner might be weighted, run an experiment to test.',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": "To test if equipment is fair/biased, or when you can't mathematically determine outcomes", "correct": True},
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
        ]
    },
    {
        "q": 'After 50 trials you get P(exp) = 0.3. After 500 trials you get P(exp) = 0.48. Which is more trustworthy?',
        "hint": 'The Law of Large Numbers says more trials give results closer to the true probability.',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'The 500-trial result (more trials = more reliable)', "correct": True},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
        ]
    },
]
