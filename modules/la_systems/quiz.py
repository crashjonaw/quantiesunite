QUIZ = [
    {
        "question": "Solve the system: x + 2y = 5, 2x - y = 0. Give the unique solution.",
        "answer": "(x, y) = (1, 2)",
        "explanation": "From equation 2: x = y/2. Substitute into equation 1: y/2 + 2y = 5, so (5/2)y = 5, thus y = 2 and x = 1. Verify: 1 + 2(2) = 5 ✓ and 2(1) - 2 = 0 ✓."
    },
    {
        "question": "For the system 2x + 3y = 6 and 4x + 6y = 12, determine the solution type and express the general solution.",
        "answer": "Infinitely many solutions (dependent). General solution: (x, y) = (3 - (3/2)t, t) for t ∈ ℝ, or (x, y) = (3, 0) + t(-3/2, 1).",
        "explanation": "The second equation is 2× the first, so they represent the same line. Any point (x, y) with 2x + 3y = 6 is a solution. Set y = t (free variable), then x = (6 - 3t)/2 = 3 - (3/2)t."
    },
    {
        "question": "For a 3×3 system Ax = b where rank(A) = 2 and rank([A|b]) = 3, determine consistency and the number of solutions.",
        "answer": "Inconsistent; no solutions exist.",
        "explanation": "By Rouché-Capelli theorem, if rank([A|b]) > rank(A), the system is inconsistent. There exists a row equation of the form 0 = c (with c ≠ 0), a contradiction."
    },
    {
        "question": "Consider the homogeneous system: 2x + 3y = 0, x - 2y = 0. Find all solutions and describe the solution space geometrically.",
        "answer": "Only the trivial solution (x, y) = (0, 0). The solution space is a single point (0-dimensional).",
        "explanation": "From equation 2: x = 2y. Substitute into equation 1: 2(2y) + 3y = 0, so 7y = 0, thus y = 0 and x = 0. The coefficient matrix has rank 2 = n, so the null space is {0}."
    },
    {
        "question": "State and explain the relationship between the dimension of the null space and the number of free variables in Ax = 0.",
        "answer": "They are equal. dim(Null(A)) = nullity(A) = n - rank(A) = number of free variables.",
        "explanation": "Free variables correspond to non-pivot columns in row echelon form. The number of non-pivot columns equals n - rank(A), which is the dimension of the null space (by Rank-Nullity theorem)."
    },
    {
        "question": "Prove: If x_p is a solution to Ax = b and x_h is a solution to Ax = 0, then x_p + x_h solves Ax = b.",
        "answer": "A(x_p + x_h) = Ax_p + Ax_h = b + 0 = b. So x_p + x_h is a solution.",
        "explanation": "By distributive property of matrix multiplication, A(x_p + x_h) = Ax_p + Ax_h. Since Ax_p = b and Ax_h = 0 by assumption, we get A(x_p + x_h) = b + 0 = b."
    },
    {
        "question": "Use Rouché-Capelli to determine when the system Ax = b (with A being 4×3) has a unique solution, infinitely many, or no solution.",
        "answer": "Unique: impossible (rank(A) ≤ 3 < 4). Infinitely many: rank(A) = rank([A|b]) = 3. No solution: rank(A) = rank([A|b]) = 1 or 2, or rank([A|b]) > rank(A).",
        "explanation": "With 4 equations and 3 unknowns, we have rank(A) ≤ 3. A unique solution requires rank(A) = n = 3, but then rank(A) ≤ rank([A|b]) ≤ 4. So: 3 indep. equations → unique if consistent; fewer indep. eqs. → infinitely many if consistent."
    },
    {
        "question": "Find the general solution to the homogeneous system: x + 2y - z = 0, 2x + 4y - 2z = 0, 3x + 6y - 3z = 0.",
        "answer": "General solution: (x, y, z) = s(-2, 1, 0) + t(1, 0, 1) for s, t ∈ ℝ. Or: x = -2s + t, y = s, z = t.",
        "explanation": "All three equations are multiples of the first: x + 2y - z = 0. This is one independent equation in 3 unknowns, so 2 free variables. Let y = s and z = t. Then x = -2s + t. The null space is 2-dimensional, spanned by (-2, 1, 0) and (1, 0, 1)."
    }
]
