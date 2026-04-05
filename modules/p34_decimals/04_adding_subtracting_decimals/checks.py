CHECKS = [
    {
        "q": "What is the most important rule when adding or subtracting decimals?",
        "hint": "This ensures that tenths add to tenths, ones add to ones, etc.",
        "options": [
            {"text": "A concept with no real-world application", "correct": False},
            {"text": "Something that cannot be measured or described", "correct": False},
            {"text": "A type of number that only exists in math textbooks", "correct": False},
            {"text": "line up the decimal points (or decimal points must be directly above/below each other)", "correct": True},
        ]
    },
    {
        "q": "Calculate 2.5 + 1.3.",
        "hint": "Line up decimal points. Tenths: 5+3=8. Ones: 2+1=3. Answer: 3.8",
        "options": [
            {"text": "3.8", "correct": True},
            {"text": "4.3", "correct": False},
            {"text": "2.8", "correct": False},
            {"text": "4.8", "correct": False},
        ]
    },
    {
        "q": "Calculate 3.2 + 1.45.",
        "hint": "Rewrite as 3.20 + 1.45. Then add: ones 3+1=4, tenths 2+4=6, hundredths 0+5=5.",
        "options": [
            {"text": "5.15", "correct": False},
            {"text": "4.65", "correct": True},
            {"text": "4.15", "correct": False},
            {"text": "3.6500000000000004", "correct": False},
        ]
    },
    {
        "q": "Calculate 5.74 - 2.31.",
        "hint": "Line up decimals. Ones: 5-2=3. Tenths: 7-3=4. Hundredths: 4-1=3.",
        "options": [
            {"text": "4.43", "correct": False},
            {"text": "2.43", "correct": False},
            {"text": "2.93", "correct": False},
            {"text": "3.43", "correct": True},
        ]
    },
]
