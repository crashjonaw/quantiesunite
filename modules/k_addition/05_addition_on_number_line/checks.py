"""Concept 5: Addition on the Number Line — Checks."""

CHECKS = [
    {
        "q": 'Start at 4 on the number line. Jump forward 2 steps. Where do you land?',
        "hint": '4 → 5, 6. Count each jump.',
        "options": [
            {"text": '6', "correct": True},
            {"text": '12', "correct": False},
            {"text": '8', "correct": False},
            {"text": '7', "correct": False},
        ]
    },
    {
        "q": 'What does addition mean on the number line?',
        "hint": 'Addition moves to the right, toward bigger numbers.',
        "options": [
            {"text": 'It tells you the starting point of counting', "correct": False},
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'jumping forward', "correct": True},
        ]
    },
    {
        "q": '3 + 5 = ? (Use the number line: start at 3, jump 5 times)',
        "hint": 'Count on from 3: 4, 5, 6, 7, 8.',
        "options": [
            {"text": '7', "correct": False},
            {"text": '18', "correct": False},
            {"text": '6', "correct": False},
            {"text": '8', "correct": True},
        ]
    },
]
