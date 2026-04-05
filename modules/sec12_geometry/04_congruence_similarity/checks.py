CHECKS = [
    {
        "q": 'Two triangles have sides 3, 4, 5 cm and 3, 4, 5 cm. Are they congruent? What test?',
        "hint": 'All three sides match exactly. This is the SSS congruence test.',
        "options": [
            {"text": 'Yes, SSS (Side-Side-Side)', "correct": True},
            {"text": 'Yes, SAS (Side-Angle-Side)', "correct": False},
            {"text": 'Yes, ASA (Angle-Side-Angle)', "correct": False},
            {"text": 'No, not congruent', "correct": False},
        ]
    },
    {
        "q": 'Triangle A has sides 2, 3, 4 cm. Triangle B has sides 6, 9, 12 cm. What is the scale factor?',
        "hint": 'Scale factor = 6÷2 = 9÷3 = 12÷4 = 3. The triangles are similar with scale factor 3.',
        "options": [
            {"text": '3', "correct": True},
            {"text": '2', "correct": False},
            {"text": '6', "correct": False},
            {"text": '9', "correct": False},
        ]
    },
    {
        "q": 'Two right triangles have hypotenuse 10 cm and one side 6 cm. Are they congruent? What test?',
        "hint": 'The hypotenuse and one other side are equal, which is the RHS test for right triangles.',
        "options": [
            {"text": 'Yes, RHS (Right angle-Hypotenuse-Side)', "correct": True},
            {"text": 'Yes, SAS (Side-Angle-Side)', "correct": False},
            {"text": 'Yes, SSS (Side-Side-Side)', "correct": False},
            {"text": 'No, not congruent', "correct": False},
        ]
    },
    {
        "q": "Triangle A has area 20 cm². Triangle B is similar with linear scale factor 2. What is B's area?",
        "hint": 'Area scale factor = 2² = 4. New area = 20 × 4 = 80 cm²',
        "options": [
            {"text": '80 cm²', "correct": True},
            {"text": '40 cm²', "correct": False},
            {"text": '20 cm²', "correct": False},
            {"text": '160 cm²', "correct": False},
        ]
    },
    {
        "q": 'Are all congruent shapes similar?',
        "hint": 'Congruence is a special case of similarity where the shapes are identical (k = 1).',
        "options": [
            {"text": 'Yes, with scale factor 1', "correct": True},
            {"text": 'No, they are different concepts', "correct": False},
            {"text": 'Yes, with scale factor 2', "correct": False},
            {"text": 'Only if they are the same colour', "correct": False},
        ]
    },
]
