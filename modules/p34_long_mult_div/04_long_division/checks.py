CHECKS = [
    {
        "q": "Solve 456 \u00f7 12 using long division. Show all steps.",
        "hint": "Look at the first two digits first. Does 12 fit into 4? No. Into 45? Yes. Then divide, multiply, subtract, bring down, and repeat.",
        "options": [
            {"text": "90", "correct": False},
            {"text": "44", "correct": False},
            {"text": "46", "correct": False},
            {"text": "45 \u00f7 12 = 3 (since 12 \u00d7 3 = 36). 45 - 36 = 9. Bring down 6 to make 96. 96 \u00f7 12 = 8. Answer: 38. Check: 38 \u00d7 12 = 456 \u2713", "correct": True},
        ]
    },
    {
        "q": "Divide 345 \u00f7 15. What quotient digit do you write in the tens place, and how did you find it?",
        "hint": "Estimate by rounding the divisor. For 15, round to 10 or 20 to help guess.",
        "options": [
            {"text": "The quotient digit in the tens place is 2. I found it by asking: how many times does 15 go into 34? 15 \u00d7 2 = 30, so 2 works. Then 34 - 30 = 4, bring down 5 to make 45, and 15 \u00d7 3 = 45. Final answer: 23.", "correct": True},
            {"text": "4", "correct": False},
            {"text": "3", "correct": False},
            {"text": "1", "correct": False},
        ]
    },
    {
        "q": "What is 457 \u00f7 12? Include the remainder.",
        "hint": "Be careful to keep track of remainders as you bring down digits. Always check your answer.",
        "options": [
            {"text": "A concept with no real-world application", "correct": False},
            {"text": "457 \u00f7 12 = 38 R1. (45 \u00f7 12 = 3 R9. Bring down 7 to make 97. 97 \u00f7 12 = 8 R1.) Check: (38 \u00d7 12) + 1 = 456 + 1 = 457 \u2713", "correct": True},
            {"text": "Something that cannot be measured or described", "correct": False},
            {"text": "A type of number that only exists in math textbooks", "correct": False},
        ]
    },
]
