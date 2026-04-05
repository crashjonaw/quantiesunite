MINDMAP = {
    "concepts": [
        {
            "title": "What is a Determinant?",
            "points": [
                "A scalar value computed from a square matrix that encodes key properties",
                "\\(\\det(A) \\neq 0 \\iff A\\) is invertible (nonsingular)",
                "Geometrically: absolute value of the determinant = scale factor of the linear map on volumes",
            ],
        },
        {
            "title": "2x2 and 3x3 Determinants",
            "points": [
                "\\(2 \\times 2\\): \\(\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix} = ad - bc\\)",
                "\\(3 \\times 3\\): expand along any row or column using cofactors (Sarrus' rule also works)",
            ],
        },
        {
            "title": "Cofactor Expansion",
            "points": [
                "\\(\\det(A) = \\sum_{j=1}^{n} a_{ij} C_{ij}\\) expanding along row \\(i\\)",
                "Cofactor \\(C_{ij} = (-1)^{i+j} M_{ij}\\) where \\(M_{ij}\\) is the minor",
                "Choose the row/column with the most zeros to simplify computation",
            ],
        },
        {
            "title": "Properties of Determinants",
            "points": [
                "\\(\\det(AB) = \\det(A)\\det(B)\\)",
                "\\(\\det(A^T) = \\det(A)\\)",
                "\\(\\det(cA) = c^n \\det(A)\\) for an \\(n \\times n\\) matrix",
                "Swapping two rows flips the sign; a row of zeros gives \\(\\det = 0\\)",
                "\\(\\det(A^{-1}) = \\frac{1}{\\det(A)}\\)",
            ],
        },
        {
            "title": "Applications",
            "points": [
                "Cramer's Rule: solve \\(Ax = b\\) via \\(x_i = \\frac{\\det(A_i)}{\\det(A)}\\)",
                "Area/volume calculations using determinants of coordinate matrices",
                "Test for linear independence of vectors",
            ],
        },
    ],
    "formulas": [
        {"label": "2x2 Determinant", "expr": "\\(\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix} = ad - bc\\)"},
        {"label": "Product Rule", "expr": "\\(\\det(AB) = \\det(A)\\det(B)\\)"},
        {"label": "Scalar Multiple", "expr": "\\(\\det(cA) = c^n \\det(A)\\)"},
        {"label": "Cramer's Rule", "expr": "\\(x_i = \\frac{\\det(A_i)}{\\det(A)}\\)"},
    ],
    "tips": [
        "A zero determinant means the matrix is singular -- no inverse exists and the system may have no or infinitely many solutions.",
        "Cofactor expansion along a row/column with many zeros saves effort.",
        "Row-reduce to upper-triangular form first; then \\(\\det = \\) product of diagonal entries (tracking row-swap sign changes).",
    ],
}
