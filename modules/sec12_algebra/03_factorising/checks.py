"""Factorising — Mid-lesson checks."""

CHECKS = [
    {
        "q": 'Factorise: 5x + 10',
        "hint": 'What is the HCF of 5x and 10?',
        "options": [
            {"text": '5(x + 2)', "correct": True},
            {"text": '5(x + 5)', "correct": False},
            {"text": '10(x + 1)', "correct": False},
            {"text": '5x(1 + 2)', "correct": False},
        ]
    },
    {
        "q": 'Factorise: 3a + 3b + 2a + 2b',
        "hint": 'Group the first two terms and the last two terms. Then factor each group.',
        "options": [
            {"text": '(a + b)(3 + 2)', "correct": True},
            {"text": '(a + b)(5)', "correct": False},
            {"text": '5(a + b)', "correct": False},
            {"text": '(3a + 2a)(3b + 2b)', "correct": False},
        ]
    },
    {
        "q": 'Factorise: x^2 + 7x + 12',
        "hint": 'Find two numbers that multiply to 12 and add to 7',
        "options": [
            {"text": '(x + 3)(x + 4)', "correct": True},
            {"text": '(x + 2)(x + 6)', "correct": False},
            {"text": '(x + 1)(x + 12)', "correct": False},
            {"text": '(x + 5)(x + 2)', "correct": False},
        ]
    },
    {
        "q": 'Factorise: 2x^2 - 8x',
        "hint": 'What is the HCF of 2x^2 and -8x?',
        "options": [
            {"text": '2x(x - 4)', "correct": True},
            {"text": '2x(x - 8)', "correct": False},
            {"text": '2(x^2 - 4x)', "correct": False},
            {"text": 'x(2x - 8)', "correct": False},
        ]
    },
]
