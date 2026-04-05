CHECKS = [
    {
        "q": 'A sector has radius 5 cm and central angle 72°. Find the arc length.',
        "hint": 'Use arc length = θπr/180 where θ is in degrees',
        "options": [
            {"text": '2.5π cm (used diameter)', "correct": False},
            {"text": 'π cm (forgot the 2)', "correct": False},
            {"text": '2π cm (or πr × θ/180 = π × 5 × 72/180 = 2π)', "correct": True},
            {"text": '4π cm (doubled)', "correct": False},
        ]
    },
    {
        "q": 'A sector has radius 8 cm and central angle π/6 radians. Find the sector area.',
        "hint": 'Use A = (1/2)r²θ where θ is in radians',
        "options": [
            {"text": '16π/3 cm² (or approximately 16.76 cm²)', "correct": True},
            {"text": '8π/3 cm² (halved)', "correct": False},
            {"text": '32π/3 cm² (doubled)', "correct": False},
            {"text": '16π cm² (forgot division by 3)', "correct": False},
        ]
    },
    {
        "q": 'Compare two sectors: one with radius 10 and angle 30°, another with radius 5 and angle 120°. Which has greater area?',
        "hint": 'Calculate both areas using (θ/360) × πr²',
        "options": [
            {"text": 'The first sector (larger area)', "correct": False},
            {"text": 'The second sector (radius 5, angle 120°) has area 25π/3 ≈ 26.2, while the first has area 25π/3 ≈ 26.2. They have equal area!', "correct": True},
            {"text": 'The second is clearly larger', "correct": False},
            {"text": 'More information is needed', "correct": False},
        ]
    },
    {
        "q": 'A segment is created by a chord in a circle of radius 6 cm. The central angle is π/3 radians. Find the segment area.',
        "hint": 'Segment Area = Sector Area - Triangle Area = (1/2)r²θ - (1/2)r²sinθ',
        "options": [
            {"text": '6π cm² (forgot triangle area)', "correct": False},
            {"text": '9√3 cm² (only triangle)', "correct": False},
            {"text": '12π - 18√3 cm² (doubled)', "correct": False},
            {"text": '6π - 9√3 cm² (or approximately 18.85 - 15.59 = 3.26 cm²)', "correct": True},
        ]
    },
    {
        "q": 'If a full circle has circumference 20π cm, what is the arc length of a 45° sector?',
        "hint": 'First find radius from C = 2πr. Then arc = (45/360) × C',
        "options": [
            {"text": '10π cm (half)', "correct": False},
            {"text": '20π cm (whole circumference)', "correct": False},
            {"text": '5π cm (1/4 of circumference, not 45/360)', "correct": False},
            {"text": '2.5π cm', "correct": True},
        ]
    },
]
