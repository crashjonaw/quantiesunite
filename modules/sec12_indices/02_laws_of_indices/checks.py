CHECKS = [
    {
        "q": 'Simplify: 2⁴ × 2³',
        "hint": 'When multiplying powers with the same base, add the indices: 2⁴ × 2³ = 2⁴⁺³ = 2⁷ = 128',
        "options": [
            {"text": '2⁷ = 128', "correct": True},
            {"text": '2⁵ = 32', "correct": False},
            {"text": '2¹² = 4096', "correct": False},
            {"text": '4 × 8 = 32', "correct": False},
        ]
    },
    {
        "q": 'Simplify: x⁸ ÷ x⁵',
        "hint": 'When dividing powers with the same base, subtract the indices: x⁸ ÷ x⁵ = x⁸⁻⁵ = x³',
        "options": [
            {"text": 'x³', "correct": True},
            {"text": 'x¹³', "correct": False},
            {"text": 'x⁵', "correct": False},
            {"text": 'x¹', "correct": False},
        ]
    },
    {
        "q": 'Simplify: (3²)⁴',
        "hint": 'When raising a power to a power, multiply the indices: (3²)⁴ = 3²ˣ⁴ = 3⁸',
        "options": [
            {"text": '3⁸ = 6561', "correct": True},
            {"text": '3⁶ = 729', "correct": False},
            {"text": '3¹⁰ = 59049', "correct": False},
            {"text": '9⁴ = 6561', "correct": False},
        ]
    },
    {
        "q": 'Simplify: (a⁵)²',
        "hint": 'Multiply the indices: (a⁵)² = a⁵ˣ² = a¹⁰',
        "options": [
            {"text": 'a¹⁰', "correct": True},
            {"text": 'a⁷', "correct": False},
            {"text": 'a²⁵', "correct": False},
            {"text": 'a³', "correct": False},
        ]
    },
    {
        "q": 'Simplify: (2³ × 2²) ÷ 2⁴',
        "hint": 'First: 2³ × 2² = 2⁵. Then: 2⁵ ÷ 2⁴ = 2⁵⁻⁴ = 2¹ = 2',
        "options": [
            {"text": '2¹ = 2', "correct": True},
            {"text": '2² = 4', "correct": False},
            {"text": '2⁵ = 32', "correct": False},
            {"text": '2⁻¹ = 0.5', "correct": False},
        ]
    },
]
