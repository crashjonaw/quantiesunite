CHECKS = [
    {
        "q": 'Find the range of: 12, 25, 18, 40, 15',
        "hint": 'Range = highest - lowest = 40 - 12 = 28',
        "options": [
            {"text": '26', "correct": False},
            {"text": '56', "correct": False},
            {"text": '28', "correct": True},
            {"text": '30', "correct": False},
        ]
    },
    {
        "q": 'Data: 3, 5, 7, 9, 11, 13, 15, 17. Find Q1 (first quartile).',
        "hint": 'Lower half: 3, 5, 7, 9. Q1 = median of lower half = (5 + 7) ÷ 2 = 6',
        "options": [
            {"text": '7', "correct": False},
            {"text": '8', "correct": False},
            {"text": '6', "correct": True},
            {"text": '12', "correct": False},
        ]
    },
    {
        "q": 'Data: 3, 5, 7, 9, 11, 13, 15, 17. Find the interquartile range (IQR).',
        "hint": 'Q1 = 6, Q3 = 14 (median of upper half: 11, 13, 15, 17 is (13+15)÷2). IQR = 14 - 6 = 8',
        "options": [
            {"text": '6', "correct": False},
            {"text": '18', "correct": False},
            {"text": '7', "correct": False},
            {"text": '8', "correct": True},
        ]
    },
    {
        "q": 'Two datasets both have a range of 20. Why might one have a wider IQR than the other?',
        "hint": 'Range only measures extreme values. IQR measures the middle 50%, so same range can come with different middle spreads.',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'All of the above', "correct": False},
            {"text": 'Because the outliers (min and max) could be positioned differently. One dataset might have data clustered in the middle, the other spread throughout.', "correct": True},
        ]
    },
]
