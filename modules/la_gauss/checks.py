CHECKS = [
    {
        "q": "Apply the row operation R₂ - 2R₁ → R₂ to the matrix [[1, 2, 3], [2, 5, 8]]. What is the result?",
        "a": "[[1, 2, 3], [0, 1, 2]]",
        "hint": "Subtract 2 times the first row from the second row element-wise."
    },
    {
        "q": "Transform to Row Echelon Form: [[1, 2, -1], [2, 4, -2], [1, 1, 1]]. What do you observe?",
        "a": "After R₂ - 2R₁ → R₂ and R₃ - R₁ → R₃, we get [[1, 2, -1], [0, 0, 0], [0, -1, 2]]. Then swap rows 2 and 3 to get [[1, 2, -1], [0, -1, 2], [0, 0, 0]]. There are 2 pivots (in positions (1,1) and (2,2)).",
        "hint": "First eliminate below the first pivot. Then move to the second column and repeat. All zero rows go to the bottom."
    },
    {
        "q": "For the augmented matrix in REF [[1, 3, 2 | 5], [0, 1, -1 | 2], [0, 0, 0 | 1]], is the system consistent? Why?",
        "a": "No, inconsistent. The last row says 0 = 1, which is a contradiction.",
        "hint": "Look at the last row. Does it represent a valid equation? What does it say?"
    },
    {
        "q": "If a 4x3 matrix A is in REF and has 3 pivots, what is rank(A)?",
        "a": "rank(A) = 3. Rank equals the number of pivots (nonzero rows) in REF.",
        "hint": "Pivots are the leading nonzero entries in each row. Count them to find the rank."
    },
    {
        "q": "For Ax = b with A being 5x7 (5 equations, 7 unknowns), if rank(A) = rank([A|b]) = 4, how many free variables are there?",
        "a": "7 - 4 = 3 free variables. Dimension of solution set = number of variables - rank.",
        "hint": "Free variables = total variables - number of pivot variables."
    }
]
