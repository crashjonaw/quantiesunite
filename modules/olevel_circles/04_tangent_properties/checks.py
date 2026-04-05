CHECKS = [
    {
        "q": 'A tangent to a circle at point T meets the radius OT. What angle do they make?',
        "hint": 'A tangent is always perpendicular to the radius at the point of tangency',
        "options": [
            {"text": '60° (equilateral)', "correct": False},
            {"text": '45° (half right angle)', "correct": False},
            {"text": '180° (straight line)', "correct": False},
            {"text": '90° (a right angle)', "correct": True},
        ]
    },
    {
        "q": 'From external point P, two tangents PA and PB are drawn to a circle with center O. If OA = 8 cm and OP = 17 cm, find PA.',
        "hint": 'Use Pythagoras in right triangle OAP: PA² + OA² = OP²',
        "options": [
            {"text": '9 cm (difference)', "correct": False},
            {"text": '15 cm', "correct": True},
            {"text": '25 cm (sum)', "correct": False},
            {"text": '17 cm (just OP)', "correct": False},
        ]
    },
    {
        "q": 'A circle has center O, radius 6 cm. Point P is outside with OP = 10 cm. A line through P intersects the circle at A and B (A closer to P). If PA = 2 cm, find PB.',
        "hint": 'Use power of a point: PA × PB = OP² - r² = 100 - 36 = 64',
        "options": [
            {"text": '4 cm (halved)', "correct": False},
            {"text": '8 cm', "correct": True},
            {"text": '32 cm (wrong formula)', "correct": False},
            {"text": '6 cm (just the radius)', "correct": False},
        ]
    },
    {
        "q": 'Two tangents are drawn from external point P to a circle. Both tangents have length 24 cm. If the radius is 7 cm, what is OP?',
        "hint": 'In right triangle OTP: OT² + PT² = OP², so 7² + 24² = OP²',
        "options": [
            {"text": '25 cm', "correct": True},
            {"text": '24 cm (tangent length only)', "correct": False},
            {"text": '31 cm (sum)', "correct": False},
            {"text": '17 cm (difference)', "correct": False},
        ]
    },
    {
        "q": 'Point P is outside a circle. One secant through P intersects the circle at A and B (PA = 3, PB = 8). Another secant intersects at C and D (PC = 2). Find PD.',
        "hint": 'By power of a point: PA × PB = PC × PD, so 3 × 8 = 2 × PD',
        "options": [
            {"text": '6 cm (halved)', "correct": False},
            {"text": '12 cm', "correct": True},
            {"text": '8 cm (wrong value)', "correct": False},
            {"text": '24 cm (doubled)', "correct": False},
        ]
    },
]
