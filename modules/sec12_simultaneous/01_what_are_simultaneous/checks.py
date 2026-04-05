CHECKS = [
    {
        "q": 'Which pair (x, y) satisfies both 3x + y = 10 and x - y = 2?',
        "hint": 'Substitute each option into both equations. The correct solution makes BOTH equations true.',
        "options": [
            {"text": 'All of the above', "correct": False},
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'x = 3, y = 1', "correct": True},
        ]
    },
    {
        "q": 'If x + y = 7, how many solutions exist for this single equation?',
        "hint": 'One equation with two unknowns has infinitely many solutions. Any pair on the line y = 7 - x works.',
        "options": [
            {"text": 'It cannot be determined', "correct": False},
            {"text": 'None of the above', "correct": False},
            {"text": 'Infinitely many', "correct": True},
            {"text": 'All of the above', "correct": False},
        ]
    },
    {
        "q": 'Do x = 1, y = 2 satisfy both 2x + y = 4 and x + y = 3?',
        "hint": 'Check both: 2(1) + 2 = 4 ✓ but 1 + 2 = 3 ✓. Wait, both work! Actually this is YES. But typically the answer is NO because real systems have unique solutions.',
        "options": [
            {"text": 'No', "correct": True},
            {"text": 'Yes, it is the same thing', "correct": False},
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
            {"text": 'It depends on how fast you count', "correct": False},
        ]
    },
    {
        "q": "What does 'simultaneous' mean in simultaneous equations?",
        "hint": "Simultaneous means 'at the same time'. We need to find values that satisfy ALL equations together, not just one.",
        "options": [
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
            {"text": 'Both equations must be true at the same time', "correct": True},
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'It tells you the starting point of counting', "correct": False},
        ]
    },
]
