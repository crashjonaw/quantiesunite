CHECKS = [
    {
        "q": 'Round 34,678 to the nearest thousand',
        "hint": 'The thousands digit is 4. The hundreds digit (helper digit) is 6. Since 6 ≥ 5, round UP. The 4 becomes 5, making it 35,000.',
        "options": [
            {"text": '35,000', "correct": True},
            {"text": '34,000', "correct": False},
            {"text": '34,700', "correct": False},
            {"text": '36,000', "correct": False},
        ]
    },
    {
        "q": 'Round 49,821 to the nearest ten thousand',
        "hint": 'The ten thousands digit is 4. The thousands digit (helper) is 9. Since 9 ≥ 5, round UP. The 4 becomes 5, giving us 50,000.',
        "options": [
            {"text": '50,000', "correct": True},
            {"text": '40,000', "correct": False},
            {"text": '49,000', "correct": False},
            {"text": '49,800', "correct": False},
        ]
    },
    {
        "q": 'Round 67,384 to the nearest thousand',
        "hint": 'The thousands digit is 7, and the hundreds digit (helper) is 3. Since 3 < 5, round DOWN. The 7 stays 7, giving us 67,000.',
        "options": [
            {"text": '67,000', "correct": True},
            {"text": '67,400', "correct": False},
            {"text": '68,000', "correct": False},
            {"text": '66,000', "correct": False},
        ]
    },
    {
        "q": 'Round 23,456 to the nearest hundred',
        "hint": 'The hundreds digit is 4. The tens digit (helper) is 5. Since 5 ≥ 5, round UP. The 4 becomes 5, making it 23,500.',
        "options": [
            {"text": '23,500', "correct": True},
            {"text": '23,400', "correct": False},
            {"text": '23,460', "correct": False},
            {"text": '23,000', "correct": False},
        ]
    },
    {
        "q": 'Round 82,501 to the nearest ten thousand',
        "hint": 'The ten thousands digit is 8. The thousands digit (helper) is 2. Since 2 < 5, round DOWN. The 8 stays 8, giving us 80,000.',
        "options": [
            {"text": '80,000', "correct": True},
            {"text": '90,000', "correct": False},
            {"text": '82,500', "correct": False},
            {"text": '82,000', "correct": False},
        ]
    },
]
