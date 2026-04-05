CHECKS = [
    {
        "q": "I think of a number, add 8, and get 15. What was the original number? (Work backwards)",
        "hint": "Start from 15. Reverse the operation: subtract 8. So 15 - 8 = 7.",
        "options": [
            {"text": "23", "correct": False},
            {"text": "7", "correct": True},
            {"text": "8", "correct": False},
            {"text": "15", "correct": False},
        ]
    },
    {
        "q": "Priya started with some money. She spent $25 and had $45 left. How much money did she start with?",
        "hint": "Work backwards from the final amount. Start = Amount left + Amount spent = $45 + $25.",
        "options": [
            {"text": "$20", "correct": False},
            {"text": "$45", "correct": False},
            {"text": "$70", "correct": True},
            {"text": "$65", "correct": False},
        ]
    },
    {
        "q": "A number is multiplied by 3, then 6 is added to get 21. What was the original number? (Work backwards)",
        "hint": "Reverse the operations in order: 21 - 6 = 15, then 15 ÷ 3 = 5.",
        "options": [
            {"text": "9", "correct": False},
            {"text": "5", "correct": True},
            {"text": "15", "correct": False},
            {"text": "3", "correct": False},
        ]
    },
    {
        "q": "After giving 12 apples to his friend and eating 3, Omar has 10 apples left. How many did he start with?",
        "hint": "Work backwards: he lost 12 + 3 = 15 apples total. So starting amount = 10 + 15 = 25.",
        "options": [
            {"text": "22", "correct": False},
            {"text": "25", "correct": True},
            {"text": "35", "correct": False},
            {"text": "15", "correct": False},
        ]
    },
]
