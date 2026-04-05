"""Sides and Corners — Mid-lesson checks."""

CHECKS = [
    {
        "q": 'What is a side?',
        "hint": 'A side is one straight line that makes up part of a shape.',
        "options": [
            {"text": 'a number', "correct": False},
            {"text": 'something invisible', "correct": False},
            {"text": 'not used in real life', "correct": False},
            {"text": 'a straight edge of a shape', "correct": True},
        ]
    },
    {
        "q": 'What is a corner?',
        "hint": "A corner is a pointy or sharp part where two edges meet. It's also called a vertex.",
        "options": [
            {"text": 'a number', "correct": False},
            {"text": 'a point where two sides meet', "correct": True},
            {"text": 'something invisible', "correct": False},
            {"text": 'not used in real life', "correct": False},
        ]
    },
    {
        "q": 'In a shape, the number of sides equals the number of ___.',
        "hint": 'Each side connects to other sides at corners!',
        "options": [
            {"text": 'sides', "correct": False},
            {"text": 'corners', "correct": True},
            {"text": 'shapes', "correct": False},
            {"text": 'lines', "correct": False},
        ]
    },
    {
        "q": 'How many right angles does a square have?',
        "hint": 'A right angle is 90 degrees. All 4 corners of a square are right angles.',
        "options": [
            {"text": '14', "correct": False},
            {"text": '4', "correct": True},
            {"text": '8', "correct": False},
            {"text": '6', "correct": False},
        ]
    },
    {
        "q": 'How many right angles does a rectangle have?',
        "hint": 'Rectangles always have 4 right angle corners, just like squares.',
        "options": [
            {"text": '4', "correct": True},
            {"text": '6', "correct": False},
            {"text": '14', "correct": False},
            {"text": '8', "correct": False},
        ]
    },
    {
        "q": 'Does a circle have any corners?',
        "hint": 'A circle is smooth and curved. It has no corners at all!',
        "options": [
            {"text": 'Yes, it is the same thing', "correct": False},
            {"text": 'no', "correct": True},
            {"text": 'It depends on how fast you count', "correct": False},
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
        ]
    },
]
