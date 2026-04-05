CHECKS = [
    {
        "q": 'A circle has radius 8 cm. What is its diameter?',
        "hint": 'Diameter = 2 × radius',
        "options": [
            {"text": '24 cm (added extra 8)', "correct": False},
            {"text": '16 cm', "correct": True},
            {"text": '4 cm (halved instead)', "correct": False},
            {"text": '8 cm (forgot to double)', "correct": False},
        ]
    },
    {
        "q": 'A circle has circumference 44 cm. Estimate the radius (use π ≈ 22/7)',
        "hint": 'C = 2πr, so r = C/(2π). Rearrange and solve.',
        "options": [
            {"text": '7 cm', "correct": True},
            {"text": '22 cm (used C/2)', "correct": False},
            {"text": '14 cm (used C/π)', "correct": False},
            {"text": '3.5 cm (halved)', "correct": False},
        ]
    },
    {
        "q": 'What is the area of a circle with radius 5 cm?',
        "hint": 'Use A = πr²',
        "options": [
            {"text": 'Something that cannot be measured or described', "correct": False},
            {"text": 'A concept with no real-world application', "correct": False},
            {"text": '25π cm² or approximately 78.5 cm²', "correct": True},
            {"text": 'A type of number that only exists in math textbooks', "correct": False},
        ]
    },
    {
        "q": 'A chord divides a circle into two arcs. If one arc is 95°, what is the other?',
        "hint": 'The two arcs must sum to 360°',
        "options": [
            {"text": '95° (same as first)', "correct": False},
            {"text": '180° (complementary confusion)', "correct": False},
            {"text": '265°', "correct": True},
            {"text": '85° (180° - 95°)', "correct": False},
        ]
    },
    {
        "q": 'In a circle with radius 10 cm, what is the maximum length of a chord?',
        "hint": 'The diameter is the longest possible chord',
        "options": [
            {"text": '20 cm (the diameter)', "correct": True},
            {"text": '10 cm (just the radius)', "correct": False},
            {"text": '31.4 cm (circumference confusion)', "correct": False},
            {"text": '314 cm (area confusion)', "correct": False},
        ]
    },
]
