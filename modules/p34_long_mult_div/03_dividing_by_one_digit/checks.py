CHECKS = [
    {
        "q": "Divide 84 \u00f7 4 using short division. Show your steps.",
        "hint": "Divide each digit from left to right. If the first digit is too small, start with the first two digits.",
        "options": [
            {"text": "9", "correct": False},
            {"text": "16", "correct": False},
            {"text": "8 \u00f7 4 = 2. 4 \u00f7 4 = 1. Answer: 21. Check: 21 \u00d7 4 = 84 \u2713", "correct": True},
            {"text": "7", "correct": False},
        ]
    },
    {
        "q": "Divide 456 \u00f7 6. Explain why you start with 45, not just 4.",
        "hint": "Always check: does the first digit divide evenly by the divisor? If not, use the first two digits.",
        "options": [
            {"text": "45 \u00f7 6 = 7 remainder 3. Bring down 6 to make 36. 36 \u00f7 6 = 6. Answer: 76. Check: 76 \u00d7 6 = 456 \u2713", "correct": True},
            {"text": "455", "correct": False},
            {"text": "912", "correct": False},
            {"text": "457", "correct": False},
        ]
    },
]
