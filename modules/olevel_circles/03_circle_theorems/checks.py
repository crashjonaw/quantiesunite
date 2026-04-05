CHECKS = [
    {
        "q": 'The angle at the center of a circle is 120°. What is the angle at the circumference subtending the same arc?',
        "hint": 'Angle at circumference = (1/2) × angle at center',
        "options": [
            {"text": '240° (reflex angle)', "correct": False},
            {"text": '30° (quarter)', "correct": False},
            {"text": '60°', "correct": True},
            {"text": '120° (same as center)', "correct": False},
        ]
    },
    {
        "q": 'A point P lies on a circle, and AB is a diameter. What is angle ∠APB?',
        "hint": 'Angle in a semicircle is always 90°',
        "options": [
            {"text": '45° (quarter right angle)', "correct": False},
            {"text": '180° (straight line)', "correct": False},
            {"text": '60° (equilateral confusion)', "correct": False},
            {"text": '90°', "correct": True},
        ]
    },
    {
        "q": 'ABCD is a cyclic quadrilateral. If ∠B = 100°, what is ∠D?',
        "hint": 'Opposite angles in a cyclic quadrilateral sum to 180°',
        "options": [
            {"text": '80°', "correct": True},
            {"text": '100° (same as B)', "correct": False},
            {"text": '50° (half of B)', "correct": False},
            {"text": '180° (sum confusion)', "correct": False},
        ]
    },
    {
        "q": 'Two angles ∠APB and ∠AQB are inscribed in a circle and subtend the same arc AB. How do they compare?',
        "hint": 'Angles subtended by the same arc at the circumference are equal',
        "options": [
            {"text": 'They are perpendicular', "correct": False},
            {"text": 'They are equal', "correct": True},
            {"text": 'They differ by 90°', "correct": False},
            {"text": 'One is twice the other', "correct": False},
        ]
    },
    {
        "q": 'A tangent to a circle at point T makes an angle of 50° with a chord TA. What is the angle in the alternate segment?',
        "hint": 'By the alternate segment theorem, the tangent-chord angle equals the inscribed angle in the alternate segment',
        "options": [
            {"text": '25° (half angle)', "correct": False},
            {"text": '40° (complementary)', "correct": False},
            {"text": '130° (supplementary)', "correct": False},
            {"text": '50°', "correct": True},
        ]
    },
]
