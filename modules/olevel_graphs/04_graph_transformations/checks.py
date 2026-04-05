CHECKS = [
    {
        "q": 'Describe the transformation: y = f(x) → y = f(x - 3) + 2',
        "hint": 'f(x - h) shifts right by h; adding k shifts up by k',
        "options": [
            {"text": 'Shift right 3 units, then shift up 2 units', "correct": True},
            {"text": 'Shift right 2 units, then shift up 3 units', "correct": False},
            {"text": 'Shift left 3 units, then shift down 2 units', "correct": False},
            {"text": 'Shift up 3 units, then shift right 2 units', "correct": False},
        ]
    },
    {
        "q": 'If y = x² becomes y = -(x + 1)² + 4, find the vertex',
        "hint": 'Rewrite as y = -(x - (-1))² + 4',
        "options": [
            {"text": '(1, 4)', "correct": False},
            {"text": '(-1, -4) (wrong y)', "correct": False},
            {"text": '(1, 4) (wrong sign)', "correct": False},
            {"text": '(-1, 4)', "correct": True},
        ]
    },
    {
        "q": 'What transformation is y = f(2x)?',
        "hint": 'b > 1 compresses horizontally',
        "options": [
            {"text": 'Shift right by 2', "correct": False},
            {"text": 'Vertical compression by factor 1/2', "correct": False},
            {"text": 'Horizontal stretch by factor 2', "correct": False},
            {"text": 'Horizontal compression (narrower) by factor 1/2', "correct": True},
        ]
    },
    {
        "q": 'Describe: y = 2sin(x) vs y = sin(2x)',
        "hint": 'Vertical transformations are outside; horizontal inside',
        "options": [
            {"text": 'Both are the same transformation', "correct": False},
            {"text": 'First: horizontal stretch; Second: vertical compression', "correct": False},
            {"text": 'First: vertical stretch by 2; Second: horizontal compression by 1/2', "correct": True},
            {"text": 'Opposite transformations', "correct": False},
        ]
    },
]
