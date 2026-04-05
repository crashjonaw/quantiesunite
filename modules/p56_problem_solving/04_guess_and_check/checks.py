CHECKS = [
    {
        "q": "Two numbers add to 9 and their product is 20. Using guess and check, which pair works?",
        "hint": "Try pairs that add to 9: 3+6, 4+5... Check: 4 + 5 = 9 and 4 × 5 = 20. Both correct!",
        "options": [
            {"text": "3 and 6", "correct": False},
            {"text": "4 and 5", "correct": True},
            {"text": "2 and 7", "correct": False},
            {"text": "1 and 8", "correct": False},
        ]
    },
    {
        "q": "There are 8 bicycles and tricycles with 19 wheels total. Which is the correct answer?",
        "hint": "Try guesses: If all 8 were bicycles = 16 wheels. Need 3 more wheels, so 3 tricycles instead. Check: 5 bicycles (10) + 3 tricycles (9) = 19 wheels.",
        "options": [
            {"text": "3 bicycles and 5 tricycles", "correct": False},
            {"text": "4 bicycles and 4 tricycles", "correct": False},
            {"text": "5 bicycles and 3 tricycles", "correct": True},
            {"text": "6 bicycles and 2 tricycles", "correct": False},
        ]
    },
    {
        "q": "A number multiplied by 2 and then 3 is added gives 15. What is the number? (Use guess and check)",
        "hint": "Try: If n = 5: (5 × 2) + 3 = 10 + 3 = 13 (no). If n = 6: (6 × 2) + 3 = 12 + 3 = 15 (yes!).",
        "options": [
            {"text": "5", "correct": False},
            {"text": "6", "correct": True},
            {"text": "7", "correct": False},
            {"text": "4", "correct": False},
        ]
    },
    {
        "q": "Why is guess and check a good strategy for this problem? 'Two numbers have a sum of 10 and a difference of 4.'",
        "hint": "Sometimes it's hard to write equations. Making organized guesses helps you find the answer systematically.",
        "options": [
            {"text": "It's always faster than other methods", "correct": False},
            {"text": "When the problem has two related unknowns, organized guesses can find the answer", "correct": True},
            {"text": "It's the only way to solve word problems", "correct": False},
            {"text": "Calculators can only use this method", "correct": False},
        ]
    },
]
