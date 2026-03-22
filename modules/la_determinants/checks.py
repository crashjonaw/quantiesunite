CHECKS = [
    {
        "q": "Compute det([[2, 5], [1, 3]]).",
        "a": "det = 2(3) - 5(1) = 6 - 5 = 1",
        "hint": "For a 2x2 matrix [[a, b], [c, d]], det = ad - bc."
    },
    {
        "q": "Compute det([[1, 0, 2], [0, 1, 0], [3, 0, 1]]) using cofactor expansion along row 2.",
        "a": "det = 0·C₂₁ + 1·C₂₂ + 0·C₂₃ = C₂₂ = (-1)^(2+2)·det([[1,2],[3,1]]) = 1·(1-6) = -5",
        "hint": "Expand along row 2 (which has mostly zeros). C₂₂ = (-1)^(2+2) times the minor M₂₂."
    },
    {
        "q": "How does the determinant change when you perform: R₁ ↔ R₂ (row swap)?",
        "a": "The determinant changes sign: det → -det.",
        "hint": "Row swaps multiply the determinant by -1."
    },
    {
        "q": "Is the matrix [[1, 2, 3], [2, 4, 6], [1, 1, 1]] invertible? Why?",
        "a": "No. Row 2 = 2·Row 1, so the rows are linearly dependent. Thus det(A) = 0, and A is not invertible.",
        "hint": "A is invertible iff det(A) ≠ 0 iff the rows are linearly independent."
    },
    {
        "q": "Use Cramer's Rule to solve: x + 2y = 5, 3x - y = 4.",
        "a": "det(A) = 1(-1) - 2(3) = -7. x = det([[5,-2],[4,-1]])/(-7) = (-5+8)/(-7) = 3/(-7) = -3/7. y = det([[1,5],[3,4]])/(-7) = (4-15)/(-7) = -11/(-7) = 11/7.",
        "hint": "x = det(A_x)/det(A), y = det(A_y)/det(A), where A_x replaces column 1 with b, A_y replaces column 2 with b."
    }
]
