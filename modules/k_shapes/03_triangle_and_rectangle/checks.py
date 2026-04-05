"""Triangle and Rectangle — Mid-lesson checks."""

CHECKS = [
    {
        "q": 'How many sides does a triangle have?',
        "hint": "Triangle = 'tri' (three) + 'angle'. Count the sides carefully!",
        "options": [
            {"text": '3', "correct": True},
            {"text": '13', "correct": False},
            {"text": '1', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": 'How many corners does a triangle have?',
        "hint": 'Count the points where sides meet.',
        "options": [
            {"text": '1', "correct": False},
            {"text": '6', "correct": False},
            {"text": '3', "correct": True},
            {"text": '13', "correct": False},
        ]
    },
    {
        "q": 'How many sides does a rectangle have?',
        "hint": 'A rectangle has 4 straight edges, just like a square.',
        "options": [
            {"text": '6', "correct": False},
            {"text": '8', "correct": False},
            {"text": '14', "correct": False},
            {"text": '4', "correct": True},
        ]
    },
    {
        "q": 'In a rectangle, are all sides the same length?',
        "hint": 'A rectangle has 2 long sides and 2 short sides. The opposite sides are equal, but not all four.',
        "options": [
            {"text": 'no', "correct": True},
            {"text": 'Yes, it is the same thing', "correct": False},
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
            {"text": 'It depends on how fast you count', "correct": False},
        ]
    },
    {
        "q": 'How many corners does a rectangle have?',
        "hint": 'A rectangle has 4 corners, all at right angles.',
        "options": [
            {"text": '6', "correct": False},
            {"text": '14', "correct": False},
            {"text": '8', "correct": False},
            {"text": '4', "correct": True},
        ]
    },
    {
        "q": 'What shape is a pizza slice?',
        "hint": 'When you slice a pizza, you cut it into pointed pieces!',
        "options": [
            {"text": 'a circle', "correct": False},
            {"text": 'a rectangle', "correct": False},
            {"text": 'triangle', "correct": True},
            {"text": 'a square', "correct": False},
        ]
    },
]
