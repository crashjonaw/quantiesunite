CHECKS = [
    {
        "q": 'What is the hypotenuse of a right-angled triangle?',
        "hint": "The hypotenuse is ALWAYS the longest side in a right-angled triangle, and it's always opposite the right angle.",
        "options": [
            {"text": 'A concept with no real-world application', "correct": False},
            {"text": 'The longest side, opposite the right angle', "correct": True},
            {"text": 'Something that cannot be measured or described', "correct": False},
            {"text": 'A type of number that only exists in math textbooks', "correct": False},
        ]
    },
    {
        "q": "True or False: In Pythagoras' Theorem, a² + b² = c², the letter c always represents the hypotenuse.",
        "hint": 'Yes! In the formula a² + b² = c², c is always the hypotenuse (the longest side). The other two letters represent the shorter sides.',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'All of the above', "correct": False},
            {"text": 'True', "correct": True},
            {"text": 'None of the above', "correct": False},
        ]
    },
    {
        "q": 'Is a triangle with sides 5 cm, 12 cm, 13 cm right-angled? Check: Does 5² + 12² = 13²?',
        "hint": '5² = 25, 12² = 144, so 5² + 12² = 169. And 13² = 169. They match! So this IS a right-angled triangle.',
        "options": [
            {"text": 'Only sometimes', "correct": False},
            {"text": 'Yes, 25 + 144 = 169, which equals 13²', "correct": True},
            {"text": 'No, they are completely different', "correct": False},
            {"text": 'It depends on the situation', "correct": False},
        ]
    },
    {
        "q": 'Is a triangle with sides 3 cm, 4 cm, 6 cm right-angled?',
        "hint": 'Check: 3² + 4² = 9 + 16 = 25, but 6² = 36. Since 25 ≠ 36, this is NOT a right-angled triangle.',
        "options": [
            {"text": 'Yes, it is the same thing', "correct": False},
            {"text": 'It depends on how fast you count', "correct": False},
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
            {"text": 'No, because 3² + 4² ≠ 6²', "correct": True},
        ]
    },
]
