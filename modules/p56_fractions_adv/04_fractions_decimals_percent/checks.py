CHECKS = [
    {
        "q": "Convert 1/5 to a decimal.",
        "hint": "Divide 1 by 5. Or think: 1/5 = 2/10 = 0.2",
        "options": [
            {"text": "0.2", "correct": True},
            {"text": "0.5", "correct": False},
            {"text": "0.15", "correct": False},
            {"text": "1.5", "correct": False},
        ]
    },
    {
        "q": "What is 3/8 as a percentage?",
        "hint": "Convert to decimal first: 3 ÷ 8 = 0.375. Then multiply by 100: 0.375 × 100 = ?",
        "options": [
            {"text": "30%", "correct": False},
            {"text": "37.5%", "correct": True},
            {"text": "35%", "correct": False},
            {"text": "80%", "correct": False},
        ]
    },
    {
        "q": "Express 0.45 as a fraction in lowest terms.",
        "hint": "0.45 = 45/100. Find the GCF of 45 and 100, which is 5. Divide both by 5.",
        "options": [
            {"text": "45/100", "correct": False},
            {"text": "9/20", "correct": True},
            {"text": "4/10", "correct": False},
            {"text": "9/100", "correct": False},
        ]
    },
    {
        "q": "Which of the following represents the same amount: 1/4, 0.25, and 25%?",
        "hint": "1/4 = 0.25 (divide 1 by 4). 0.25 = 25% (multiply by 100). They're all equal!",
        "options": [
            {"text": "Only 1/4 and 0.25 are equal", "correct": False},
            {"text": "Only 0.25 and 25% are equal", "correct": False},
            {"text": "All three are equal", "correct": True},
            {"text": "None of them are equal", "correct": False},
        ]
    },
]
