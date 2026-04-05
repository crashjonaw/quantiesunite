"""One-to-One Correspondence — Concept checks."""

CHECKS = [
    {
        "q": 'If you count 3 toys and point to the first toy twice, did you use one-to-one correspondence?',
        "hint": 'Each object should get exactly one number.',
        "options": [
            {"text": 'Yes, it is the same thing', "correct": False},
            {"text": 'It depends on how fast you count', "correct": False},
            {"text": 'no, you double-counted that toy', "correct": True},
            {"text": 'Yes, as long as you say the numbers correctly', "correct": False},
        ]
    },
    {
        "q": 'What does one-to-one correspondence mean?',
        "hint": 'Think about perfect matching — one to one.',
        "options": [
            {"text": 'It has no special meaning, it is just a number', "correct": False},
            {"text": 'It tells you the starting point of counting', "correct": False},
            {"text": 'each object matches exactly one number, and each number matches exactly one object', "correct": True},
            {"text": 'It tells you which number comes next in the sequence', "correct": False},
        ]
    },
    {
        "q": 'Name two strategies for counting with one-to-one correspondence.',
        "hint": 'Think about how to stay organized when counting.',
        "options": [
            {"text": 'Memorising numbers, saying them fast, writing them down', "correct": False},
            {"text": 'Counting forward, counting backward, counting by twos', "correct": False},
            {"text": 'point to each object, arrange in a line and push aside, count slowly', "correct": True},
            {"text": 'Addition, subtraction, multiplication', "correct": False},
        ]
    },
]
