CHECKS = [
    {
        "q": "Calculate 23 \u00d7 14 using long multiplication. Show your partial products and explain why you shift.",
        "hint": "First multiply by the ones digit, then by the tens digit. Remember to shift the second partial product one place to the left.",
        "options": [
            {"text": "46", "correct": False},
            {"text": "22", "correct": False},
            {"text": "24", "correct": False},
            {"text": "322", "correct": True},
        ]
    },
    {
        "q": "Calculate 56 \u00d7 43. Which partial product is larger and why?",
        "hint": "The partial products represent 56 \u00d7 3 and 56 \u00d7 40. The second one is larger because 40 > 3.",
        "options": [
            {"text": "56 \u00d7 3 = 168. 56 \u00d7 4 = 224, shifted = 2240. The second partial product (2240) is larger because it represents multiplying by 40, not 4.", "correct": True},
            {"text": "55", "correct": False},
            {"text": "112", "correct": False},
            {"text": "57", "correct": False},
        ]
    },
]
