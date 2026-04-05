CHECKS = [
    {
        "q": 'Write 56,000 in standard form',
        "hint": 'Move the decimal point to get a number between 1 and 10. You moved it 4 places left, so the power is +4.',
        "options": [
            {"text": '5.6 × 10⁴', "correct": True},
            {"text": '56 × 10³', "correct": False},
            {"text": '5.6 × 10⁵', "correct": False},
            {"text": '0.56 × 10⁵', "correct": False},
        ]
    },
    {
        "q": 'Write 0.00032 in standard form',
        "hint": 'Move the decimal 4 places to the right to get 3.2. Moving right means negative power: 0.00032 = 3.2 × 10⁻⁴',
        "options": [
            {"text": '3.2 × 10⁻⁴', "correct": True},
            {"text": '3.2 × 10⁴', "correct": False},
            {"text": '32 × 10⁻⁵', "correct": False},
            {"text": '3.2 × 10⁻³', "correct": False},
        ]
    },
    {
        "q": 'Convert 2.5 × 10³ to normal form',
        "hint": 'Positive power: move decimal 3 places right. 2.5 → 2500',
        "options": [
            {"text": '2,500', "correct": True},
            {"text": '250', "correct": False},
            {"text": '25,000', "correct": False},
            {"text": '0.0025', "correct": False},
        ]
    },
    {
        "q": 'Convert 7 × 10⁻² to normal form',
        "hint": 'Negative power: move decimal 2 places left. 7 → 0.07',
        "options": [
            {"text": '0.07', "correct": True},
            {"text": '0.7', "correct": False},
            {"text": '700', "correct": False},
            {"text": '0.007', "correct": False},
        ]
    },
    {
        "q": 'Calculate: (5 × 10³) × (2 × 10⁴) in standard form',
        "hint": 'Multiply: (5 × 2) × (10³ × 10⁴) = 10 × 10⁷ = 1 × 10⁸',
        "options": [
            {"text": '1 × 10⁸', "correct": True},
            {"text": '10 × 10⁷', "correct": False},
            {"text": '1 × 10⁷', "correct": False},
            {"text": '1 × 10⁶', "correct": False},
        ]
    },
]
