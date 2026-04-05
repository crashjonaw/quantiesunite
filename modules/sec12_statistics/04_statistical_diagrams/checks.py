CHECKS = [
    {
        "q": 'In a histogram, what does the X-axis represent?',
        "hint": 'X-axis shows the grouped intervals (e.g., 50-60, 60-70). Y-axis shows frequency.',
        "options": [
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'It tells you the starting point of counting', "correct": False},
            {"text": 'The intervals or bins (ranges of values)', "correct": True},
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
        ]
    },
    {
        "q": 'Should the bars in a histogram touch or have gaps?',
        "hint": 'Histogram bars touch because data is continuous. Bar charts have gaps because data is categorical.',
        "options": [
            {"text": 'Touch', "correct": True},
            {"text": 'All of the above', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
        ]
    },
    {
        "q": 'In a stem-and-leaf diagram, 5|3 represents which number?',
        "hint": 'The stem (5) is the tens digit. The leaf (3) is the ones digit. So 5|3 = 53.',
        "options": [
            {"text": '51', "correct": False},
            {"text": '53', "correct": True},
            {"text": '55', "correct": False},
            {"text": '54', "correct": False},
        ]
    },
    {
        "q": "A graph's Y-axis goes from 98 to 102 instead of 0 to 102. Why might this be misleading?",
        "hint": "When the axis doesn't start at 0, small changes appear magnified. Always check if the Y-axis starts at 0.",
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'All of the above', "correct": False},
            {"text": 'Because a small change (like from 100 to 101) will look like a huge jump, exaggerating the difference.', "correct": True},
            {"text": 'None of the above', "correct": False},
        ]
    },
]
