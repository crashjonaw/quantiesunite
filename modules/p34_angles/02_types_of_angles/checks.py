CHECKS = [
    {
        "q": 'Classify these angles: 45°, 90°, 120°, 200°',
        "hint": 'Acute < 90°, Right = 90°, Obtuse between 90° and 180°, Reflex between 180° and 360°',
        "options": [
            {"text": '45° is acute, 90° is right, 120° is obtuse, 200° is reflex', "correct": True},
            {"text": '45° is right, 90° is acute, 120° is reflex, 200° is obtuse', "correct": False},
            {"text": '45° is obtuse, 90° is reflex, 120° is acute, 200° is right', "correct": False},
            {"text": 'All four angles are the same type.', "correct": False},
        ]
    },
    {
        "q": 'Which type of angle measures exactly 180°?',
        "hint": 'This angle forms a perfectly straight line',
        "options": [
            {"text": 'A straight angle', "correct": True},
            {"text": 'An acute angle', "correct": False},
            {"text": 'A right angle', "correct": False},
            {"text": 'A reflex angle', "correct": False},
        ]
    },
    {
        "q": 'Is an 85° angle acute, right, or obtuse?',
        "hint": "Acute angles are less than 90°. Since 85° < 90°, it's acute",
        "options": [
            {"text": 'Acute (because it is less than 90°)', "correct": True},
            {"text": 'Right (because it is close to 90°)', "correct": False},
            {"text": 'Obtuse (because it is almost 90°)', "correct": False},
            {"text": 'Reflex (because 85 is a big number)', "correct": False},
        ]
    },
    {
        "q": 'An angle measures 230°. Is it a straight angle, a reflex angle, or something else?',
        "hint": 'Reflex angles go the long way around, measuring between 180° and 360°',
        "options": [
            {"text": 'A reflex angle (because it is between 180° and 360°)', "correct": True},
            {"text": 'An obtuse angle (because 230° is a big angle)', "correct": False},
            {"text": 'A straight angle (because 230 is close to 180)', "correct": False},
            {"text": 'An acute angle (because 230 is greater than 180)', "correct": False},
        ]
    },
]
