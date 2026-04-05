CHECKS = [
    {
        "q": 'Plot the point (2, 3). In which quadrant does it appear?',
        "hint": 'Starting from the origin, move 2 units right and 3 units up. Both coordinates are positive, so it is in Quadrant I.',
        "options": [
            {"text": 'Quadrant I', "correct": True},
            {"text": 'Quadrant II', "correct": False},
            {"text": 'Quadrant III', "correct": False},
            {"text": 'Quadrant IV', "correct": False},
        ]
    },
    {
        "q": 'What are the coordinates of the point 1 unit left and 2 units down from the origin?',
        "hint": 'Left means negative x-value (-1). Down means negative y-value (-2). The point is (-1, -2).',
        "options": [
            {"text": '(-1, -2)', "correct": True},
            {"text": '(-1, 2)', "correct": False},
            {"text": '(1, -2)', "correct": False},
            {"text": '(-2, -1)', "correct": False},
        ]
    },
    {
        "q": 'If you see a point at the location 3 right and 4 up from the origin, what are its coordinates?',
        "hint": 'Right means positive x (3). Up means positive y (4). The coordinates are (3, 4).',
        "options": [
            {"text": '(3, 4)', "correct": True},
            {"text": '(4, 3)', "correct": False},
            {"text": '(3, -4)', "correct": False},
            {"text": '(-3, 4)', "correct": False},
        ]
    },
    {
        "q": 'Is the point (2, 3) the same as the point (3, 2)?',
        "hint": '(2, 3) is 2 right and 3 up. (3, 2) is 3 right and 2 up. The order matters!',
        "options": [
            {"text": 'No, they are different points', "correct": True},
            {"text": 'Yes, they are the same', "correct": False},
            {"text": 'Yes, the order does not matter', "correct": False},
            {"text": 'Yes, both have a sum of 5', "correct": False},
        ]
    },
]
