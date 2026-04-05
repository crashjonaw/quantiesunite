CHECKS = [
    {
        "q": 'For y = 1/x, what are the asymptotes?',
        "hint": 'Asymptotes are where the function is undefined or approaches as x → ±∞',
        "options": [
            {"text": 'x = 0 only', "correct": False},
            {"text": 'x = 1 and y = 1', "correct": False},
            {"text": 'x = 0 (vertical) and y = 0 (horizontal)', "correct": True},
            {"text": 'No asymptotes', "correct": False},
        ]
    },
    {
        "q": 'Sketch y = 2^x. What is the y-intercept?',
        "hint": 'All exponential functions a^x pass through (0, 1) since a^0 = 1',
        "options": [
            {"text": '(0, 1)', "correct": True},
            {"text": '(0, 0)', "correct": False},
            {"text": '(1, 0)', "correct": False},
            {"text": '(0, 2)', "correct": False},
        ]
    },
    {
        "q": 'State the period of y = sin x',
        "hint": 'Period is the horizontal distance for one complete cycle',
        "options": [
            {"text": '1', "correct": False},
            {"text": '2π', "correct": True},
            {"text": 'π', "correct": False},
            {"text": '360', "correct": False},
        ]
    },
    {
        "q": 'Find all roots of y = cos x in [0, 2π]',
        "hint": 'cos x = 0 at these two points in the given interval',
        "options": [
            {"text": 'x = 0 and x = π', "correct": False},
            {"text": 'x = π/2 and x = 3π/2', "correct": True},
            {"text": 'x = π/4 and x = 3π/4', "correct": False},
            {"text": 'x = π/2 only', "correct": False},
        ]
    },
]
