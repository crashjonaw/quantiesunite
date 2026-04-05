CHECKS = [
    {
        "q": 'Find the gradient of the line through (1, 2) and (3, 6)',
        "hint": '\\(m = \\frac{6-2}{3-1} = \\frac{4}{2} = 2\\)',
        "options": [
            {"text": '2', "correct": True},
            {"text": '4', "correct": False},
            {"text": '1', "correct": False},
            {"text": '3', "correct": False},
        ]
    },
    {
        "q": 'What is the gradient of a horizontal line?',
        "hint": 'A horizontal line has no vertical change, so rise = 0, making the gradient 0.',
        "options": [
            {"text": '0', "correct": True},
            {"text": '1', "correct": False},
            {"text": 'undefined', "correct": False},
            {"text": '-1', "correct": False},
        ]
    },
    {
        "q": 'If line A has gradient 3, what is the gradient of a line perpendicular to A?',
        "hint": 'For perpendicular lines, \\(m_1 \\times m_2 = -1\\). So \\(3 \\times m_2 = -1\\) gives \\(m_2 = -1/3\\)',
        "options": [
            {"text": '-1/3', "correct": True},
            {"text": '-3', "correct": False},
            {"text": '1/3', "correct": False},
            {"text": '3', "correct": False},
        ]
    },
    {
        "q": 'Are lines with gradients 2 and 2 parallel?',
        "hint": 'Parallel lines have the same gradient. Both have gradient 2, so they are parallel.',
        "options": [
            {"text": 'Yes', "correct": True},
            {"text": 'No', "correct": False},
            {"text": 'Only if they do not intersect', "correct": False},
            {"text": 'Only if the y-intercepts are the same', "correct": False},
        ]
    },
]
