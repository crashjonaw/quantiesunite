CHECKS = [
    {
        "q": "Compute [1, 2] + [3, 4] and 2[1, 2].",
        "a": "[1, 2] + [3, 4] = [4, 6]. 2[1, 2] = [2, 4].",
        "hint": "Add element-wise. Multiply each element by the scalar."
    },
    {
        "q": "Multiply A = [[1, 2], [3, 4]] by B = [[5, 6], [7, 8]]. What is AB?",
        "a": "AB = [[1·5 + 2·7, 1·6 + 2·8], [3·5 + 4·7, 3·6 + 4·8]] = [[19, 22], [43, 50]]",
        "hint": "c_ij = row i of A · column j of B (dot product)."
    },
    {
        "q": "If A = [[1, 2, 3], [4, 5, 6]], what is A^T (transpose)?",
        "a": "A^T = [[1, 4], [2, 5], [3, 6]]",
        "hint": "Swap rows and columns: (A^T)_ij = A_ji."
    },
    {
        "q": "Is the matrix [[1, 2], [2, 5]] symmetric? Is [[0, 3], [-3, 0]] skew-symmetric?",
        "a": "Yes, [[1, 2], [2, 5]] is symmetric (entries are symmetric about the diagonal). Yes, [[0, 3], [-3, 0]] is skew-symmetric (entries are negatives across the diagonal).",
        "hint": "A is symmetric if A^T = A. A is skew-symmetric if A^T = -A."
    },
    {
        "q": "For a square matrix A, when does A^(-1) exist?",
        "a": "When det(A) ≠ 0, or equivalently, when rank(A) = n (full rank), or when Ax = 0 has only the trivial solution x = 0.",
        "hint": "These three conditions are equivalent for square matrices. A is invertible if and only if it's nonsingular."
    }
]
