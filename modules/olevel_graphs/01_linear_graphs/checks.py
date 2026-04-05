CHECKS = [
    {
        "q": 'Find the gradient of the line through (2, 5) and (5, 11).',
        "hint": 'Use m = (y₂ - y₁) / (x₂ - x₁)',
        "options": [
            {"text": '2', "correct": True},
            {"text": '0', "correct": False},
            {"text": '12', "correct": False},
            {"text": '1', "correct": False},
        ]
    },
    {
        "q": 'Find the equation of the line with gradient 3 and y-intercept −2.',
        "hint": 'Use y = mx + c where m is gradient, c is y-intercept',
        "options": [
            {"text": 'y = 3x - 2', "correct": True},
            {"text": 'y = -3x - 2 (flipped slope)', "correct": False},
            {"text": 'y = 3x + 2 (wrong sign)', "correct": False},
            {"text": 'y = 2x - 3 (swapped)', "correct": False},
        ]
    },
    {
        "q": 'Find the gradient of a line perpendicular to y = 4x + 1.',
        "hint": 'For perpendicular: m₁ × m₂ = -1',
        "options": [
            {"text": '-4 (negated)', "correct": False},
            {"text": '-1/4 or -0.25', "correct": True},
            {"text": '1/4 (reciprocal without negative)', "correct": False},
            {"text": '4 (same slope)', "correct": False},
        ]
    },
    {
        "q": 'Find the equation of the line through (1, 3) parallel to y = 2x + 5.',
        "hint": 'Parallel lines have the same gradient',
        "options": [
            {"text": 'y = 2x + 3 (wrong y-intercept)', "correct": False},
            {"text": 'y = 2x + 1', "correct": True},
            {"text": 'y = x + 2 (wrong slope)', "correct": False},
            {"text": 'y = -2x + 5 (opposite slope)', "correct": False},
        ]
    },
]
