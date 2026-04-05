CHECKS = [
    {
        "q": 'Write 3 × 3 × 3 × 3 in index form',
        "hint": 'Count how many times 3 appears (4 times). The base is 3 and the index is 4, so write 3⁴.',
        "options": [
            {"text": '3⁴', "correct": True},
            {"text": '4³', "correct": False},
            {"text": '3³', "correct": False},
            {"text": '3⁵', "correct": False},
        ]
    },
    {
        "q": 'Expand 5² and calculate the answer',
        "hint": 'The index is 2, so multiply 5 by itself 2 times: 5 × 5 = 25',
        "options": [
            {"text": '5 × 5 = 25', "correct": True},
            {"text": '5 + 5 = 10', "correct": False},
            {"text": '5 × 2 = 10', "correct": False},
            {"text": '2 × 2 = 4', "correct": False},
        ]
    },
    {
        "q": 'What is 100⁰?',
        "hint": 'Any non-zero number to the power 0 equals 1.',
        "options": [
            {"text": '1', "correct": True},
            {"text": '0', "correct": False},
            {"text": '100', "correct": False},
            {"text": 'undefined', "correct": False},
        ]
    },
    {
        "q": 'Simplify: 8¹',
        "hint": 'Any number to the power 1 equals itself.',
        "options": [
            {"text": '8', "correct": True},
            {"text": '1', "correct": False},
            {"text": '8¹ (no simplification)', "correct": False},
            {"text": '16', "correct": False},
        ]
    },
    {
        "q": 'Calculate: 2⁶',
        "hint": '2⁶ = 2 × 2 × 2 × 2 × 2 × 2. Calculate: 2 × 2 = 4, 4 × 2 = 8, 8 × 2 = 16, 16 × 2 = 32, 32 × 2 = 64',
        "options": [
            {"text": '64', "correct": True},
            {"text": '12', "correct": False},
            {"text": '32', "correct": False},
            {"text": '128', "correct": False},
        ]
    },
]
