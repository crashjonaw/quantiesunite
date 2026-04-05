CHECKS = [
    {
        "q": "Which is bigger: 0.7 or 0.42?",
        "hint": "Compare the tenths place first: 7 > 4, so 0.7 is bigger.",
        "options": [
            {"text": "0.7 is bigger (or 0.7 > 0.42)", "correct": True},
            {"text": "1", "correct": False},
            {"text": "Different operation", "correct": False},
            {"text": "Wrong method", "correct": False},
        ]
    },
    {
        "q": "Which is bigger: 0.1 or 0.09?",
        "hint": "Rewrite as 0.10 and 0.09. Now compare: 10 hundredths > 9 hundredths.",
        "options": [
            {"text": "0.1 is bigger (or 0.1 > 0.09)", "correct": True},
            {"text": "Wrong method", "correct": False},
            {"text": "Different operation", "correct": False},
            {"text": "1", "correct": False},
        ]
    },
    {
        "q": "Order from smallest to largest: 0.45, 0.54, 0.4, 0.5",
        "hint": "Rewrite with same decimal places: 0.40, 0.45, 0.50, 0.54. Then compare.",
        "options": [
            {"text": "Wrong method", "correct": False},
            {"text": "Different operation", "correct": False},
            {"text": "1", "correct": False},
            {"text": "0.4, 0.45, 0.5, 0.54 (or 0.40, 0.45, 0.50, 0.54)", "correct": True},
        ]
    },
    {
        "q": "Fill in the symbol: 0.32 ___ 0.31",
        "hint": "Both have 3 tenths. Compare hundredths: 2 > 1.",
        "options": [
            {"text": "Wrong method", "correct": False},
            {"text": "Different operation", "correct": False},
            {"text": "> (or greater than, or >)", "correct": True},
            {"text": "Different concept", "correct": False},
        ]
    },
    {
        "q": "Order from smallest to largest: 0.6, 0.06, 0.66",
        "hint": "Rewrite as 0.60, 0.06, 0.66. Compare tenths first: 0 < 6.",
        "options": [
            {"text": "0.06, 0.6, 0.66", "correct": True},
            {"text": "Wrong method", "correct": False},
            {"text": "Different operation", "correct": False},
            {"text": "1", "correct": False},
        ]
    },
]
