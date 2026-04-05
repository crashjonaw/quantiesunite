"""Taking Away Objects — Check questions."""

CHECKS = [
    {
        "q": 'You have 11 pencils. You lose 3. How many do you have left?',
        "hint": 'Start with 11. Take away 3. Count on your fingers: 10, 9, 8. You have 8 left.',
        "options": [
            {"text": '18', "correct": False},
            {"text": '7', "correct": False},
            {"text": '6', "correct": False},
            {"text": '8', "correct": True},
        ]
    },
    {
        "q": 'There are 5 dogs. 2 dogs run away. How many dogs are still there?',
        "hint": '5 − 2 = 3. Use your fingers or draw circles to see the dogs left.',
        "options": [
            {"text": '1', "correct": False},
            {"text": '3', "correct": True},
            {"text": '6', "correct": False},
            {"text": '13', "correct": False},
        ]
    },
    {
        "q": 'You draw 7 hearts. You color 4 of them red. How many hearts are not red?',
        "hint": '7 hearts total − 4 colored = 3 not colored.',
        "options": [
            {"text": '3', "correct": True},
            {"text": '13', "correct": False},
            {"text": '6', "correct": False},
            {"text": '1', "correct": False},
        ]
    },
    {
        "q": 'A box has 10 blocks. You use 6 blocks to build. How many blocks are still in the box?',
        "hint": '10 − 6. Try using real blocks or drawing them to see.',
        "options": [
            {"text": '14', "correct": False},
            {"text": '6', "correct": False},
            {"text": '8', "correct": False},
            {"text": '4', "correct": True},
        ]
    },
]
