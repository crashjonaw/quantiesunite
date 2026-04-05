CHECKS = [
    {
        "q": 'What is 7⁰?',
        "hint": 'Any non-zero number to the power 0 equals 1.',
        "options": [
            {"text": '1', "correct": True},
            {"text": '0', "correct": False},
            {"text": '7', "correct": False},
            {"text": 'undefined', "correct": False},
        ]
    },
    {
        "q": 'Express 2⁻³ as a fraction',
        "hint": 'A negative index means take the reciprocal: 2⁻³ = 1/2³ = 1/8',
        "options": [
            {"text": '1/8', "correct": True},
            {"text": '-1/8', "correct": False},
            {"text": '1/2', "correct": False},
            {"text": '-8', "correct": False},
        ]
    },
    {
        "q": 'Simplify: a⁻² × a⁵',
        "hint": 'Use the multiplication law: a⁻² × a⁵ = a⁻²⁺⁵ = a³',
        "options": [
            {"text": 'a³', "correct": True},
            {"text": 'a⁷', "correct": False},
            {"text": 'a⁻¹⁰', "correct": False},
            {"text": '1/a³', "correct": False},
        ]
    },
    {
        "q": 'Simplify: x⁴ ÷ x⁹ and write as a fraction',
        "hint": 'Use division law: x⁴ ÷ x⁹ = x⁻⁵. Then convert: x⁻⁵ = 1/x⁵',
        "options": [
            {"text": '1/x⁵', "correct": True},
            {"text": 'x⁵', "correct": False},
            {"text": '1/x⁹', "correct": False},
            {"text": 'x⁻⁹', "correct": False},
        ]
    },
    {
        "q": 'Simplify: (3⁻²)³',
        "hint": 'Power of power: (3⁻²)³ = 3⁻⁶ = 1/3⁶ = 1/729',
        "options": [
            {"text": '1/729', "correct": True},
            {"text": '-1/729', "correct": False},
            {"text": '1/9', "correct": False},
            {"text": '-729', "correct": False},
        ]
    },
]
