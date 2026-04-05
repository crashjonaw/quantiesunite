"""03. Numbers 0 to 20 — Check questions."""

CHECKS = [
    {
        "q": 'What is the number that comes right after 17?',
        "hint": 'It follows the -teen pattern. After 17 comes 18.',
        "options": [
            {"text": '18', "correct": True},
            {"text": '17', "correct": False},
            {"text": '36', "correct": False},
            {"text": '19', "correct": False},
        ]
    },
    {
        "q": "Write the number for the word 'fifteen'",
        "hint": 'Fifteen = 10 + 5. So we write 15.',
        "options": [
            {"text": '13', "correct": False},
            {"text": '25', "correct": False},
            {"text": '15', "correct": True},
            {"text": '14', "correct": False},
        ]
    },
    {
        "q": "What are the two special numbers that don't follow the -teen pattern?",
        "hint": 'All the other teens (13-19) follow a pattern, but 11 and 12 have special names.',
        "options": [
            {"text": '1 and 2', "correct": False},
            {"text": '11, 12', "correct": True},
            {"text": '10 and 20', "correct": False},
            {"text": '13 and 14', "correct": False},
        ]
    },
]
