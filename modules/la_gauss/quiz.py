QUIZ = [
    {
        "question": "Convert to REF and determine rank: [[2, 4, 6], [1, 2, 3], [3, 6, 9]]",
        "answer": "REF: [[1, 2, 3], [0, 0, 0], [0, 0, 0]]. Rank = 1.",
        "explanation": "The second and third rows are multiples of the first. After elimination, only one independent equation remains."
    },
    {
        "question": "Solve using Gaussian elimination: x + y = 2, 2x + 2y = 4.",
        "answer": "Infinitely many solutions: (x, y) = (2 - t, t) for any t.",
        "explanation": "The second equation is 2 times the first. Rank(A) = rank([A|b]) = 1 < 2 variables, so infinitely many solutions."
    },
    {
        "question": "Use back substitution to solve from REF: [[1, 2, 3 | 4], [0, 1, 2 | 5], [0, 0, 1 | 6]]",
        "answer": "(x, y, z) = (-4, -7, 6)",
        "explanation": "From row 3: z = 6. From row 2: y + 2(6) = 5, so y = -7. From row 1: x + 2(-7) + 3(6) = 4, so x = -4."
    },
    {
        "question": "For a 3x3 system with rank(A) = 2 and rank([A|b]) = 2, how many solutions?",
        "answer": "Infinitely many (1-parameter family)",
        "explanation": "rank(A) = rank([A|b]) means consistent. rank < 3 means 3 - 2 = 1 free variable, giving infinitely many solutions."
    },
    {
        "question": "True or False: If A is 10x8 and rank(A) = 8, then for any b, the system Ax = b has at most one solution.",
        "answer": "True",
        "explanation": "rank(A) = 8 = number of variables means A has full column rank. The homogeneous system Ax = 0 has only the trivial solution, so Ax = b has at most one solution (unique if consistent)."
    }
]
