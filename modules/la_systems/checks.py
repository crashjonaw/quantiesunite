CHECKS = [
    {
        "q": "Write the augmented matrix [A|b] for: 2x + 3y - z = 5, x - y + 2z = 3, 3x + 2y = 1",
        "a": "[2, 3, -1 | 5; 1, -1, 2 | 3; 3, 2, 0 | 1]",
        "hint": "The augmented matrix combines the coefficient matrix A and the constant vector b. Each row represents one equation."
    },
    {
        "q": "For the system: x + 2y = 3 and 2x + 4y = 6, determine the solution type and find the general solution.",
        "a": "Infinitely many solutions. The equations are dependent (second is 2× first). General solution: (x, y) = (3 - 2t, t) for t in R, or equivalently (x, y) = (3, 0) + t(-2, 1).",
        "hint": "Check if one equation is a scalar multiple of the other. If so, they represent the same line."
    },
    {
        "q": "For the homogeneous system Ax = 0, prove that if x1 and x2 are solutions, then x1 + x2 is also a solution.",
        "a": "If Ax1 = 0 and Ax2 = 0, then A(x1 + x2) = Ax1 + Ax2 = 0 + 0 = 0, so x1 + x2 is a solution.",
        "hint": "Use the distributive property of matrix multiplication: A(x1 + x2) = Ax1 + Ax2."
    },
    {
        "q": "State the Rouché-Capelli theorem conditions for consistency of Ax = b.",
        "a": "The system is consistent iff rank(A) = rank([A|b]). If consistent, unique solution iff rank(A) = n (number of unknowns). Infinitely many if rank(A) = rank([A|b]) < n.",
        "hint": "Consistency requires the augmented matrix to have the same rank as the coefficient matrix. Uniqueness requires the rank to equal the number of variables."
    },
    {
        "q": "Prove that if x_p is a particular solution to Ax = b and x_h is any solution to Ax = 0, then x_p + x_h is a solution to Ax = b.",
        "a": "A(x_p + x_h) = Ax_p + Ax_h = b + 0 = b. Therefore x_p + x_h satisfies Ax = b.",
        "hint": "Apply the distributive property of matrix multiplication and substitute the given conditions."
    }
]
