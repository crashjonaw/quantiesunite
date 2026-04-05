CHECKS = [
    {
        "q": 'Find the vertex of y = x² - 6x + 8',
        "hint": 'Use x = -b/(2a) to find x-coordinate, then substitute',
        "options": [
            {"text": '(3, -1)', "correct": True},
            {"text": '(6, 0) (wrong calculation)', "correct": False},
            {"text": '(-3, -1) (wrong sign)', "correct": False},
            {"text": '(3, 1) (wrong y)', "correct": False},
        ]
    },
    {
        "q": 'Find the roots of y = x² - 5x + 6',
        "hint": 'Factor or use the quadratic formula',
        "options": [
            {"text": 'x = 1 and x = 6', "correct": False},
            {"text": 'x = 2 and x = -3', "correct": False},
            {"text": 'x = 2 and x = 3', "correct": True},
            {"text": 'x = -2 and x = -3', "correct": False},
        ]
    },
    {
        "q": 'Find the discriminant of 2x² - 4x + 3 = 0',
        "hint": 'Δ = b² - 4ac',
        "options": [
            {"text": '2', "correct": False},
            {"text": '-8', "correct": True},
            {"text": '28 (wrong formula)', "correct": False},
            {"text": '0 (perfect square)', "correct": False},
        ]
    },
    {
        "q": 'Write y = (x - 2)² + 3 in the form y = ax² + bx + c',
        "hint": 'Expand the brackets: (x-2)² = x² - 4x + 4',
        "options": [
            {"text": 'y = x² - 4x + 3 (missing the +3)', "correct": False},
            {"text": 'y = x² - 4x + 7', "correct": True},
            {"text": 'y = x² - 2x + 3 (incomplete expansion)', "correct": False},
            {"text": 'y = x² - 4x + 4', "correct": False},
        ]
    },
]
