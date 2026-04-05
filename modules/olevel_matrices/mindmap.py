MINDMAP = {
    "concepts": [
        {
            "title": "Matrix Basics",
            "points": [
                "A matrix is a rectangular array of numbers arranged in rows and columns",
                "Order of a matrix: rows x columns (e.g., \\(2 \\times 3\\))",
                "Two matrices are equal iff they have the same order and all corresponding entries are equal",
            ],
        },
        {
            "title": "Matrix Operations",
            "points": [
                "Addition/Subtraction: only for matrices of the same order; add/subtract corresponding entries",
                "Scalar multiplication: multiply every entry by the scalar",
                "Matrix multiplication: \\(A_{m \\times n} \\cdot B_{n \\times p} = C_{m \\times p}\\)",
                "Multiplication is NOT commutative: \\(AB \\neq BA\\) in general",
            ],
        },
        {
            "title": "Determinant & Inverse (2x2)",
            "points": [
                "For \\(A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\), determinant \\(|A| = ad - bc\\)",
                "If \\(|A| = 0\\), the matrix is singular (no inverse)",
                "Inverse: \\(A^{-1} = \\frac{1}{ad-bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}\\)",
                "\\(A \\cdot A^{-1} = A^{-1} \\cdot A = I\\)",
            ],
        },
        {
            "title": "Identity & Zero Matrices",
            "points": [
                "Identity matrix \\(I\\): 1s on diagonal, 0s elsewhere; \\(AI = IA = A\\)",
                "Zero matrix \\(O\\): all entries are 0; \\(A + O = A\\)",
            ],
        },
        {
            "title": "Solving Simultaneous Equations",
            "points": [
                "Write system as \\(AX = B\\), then \\(X = A^{-1}B\\)",
                "Only works when \\(A\\) is non-singular (\\(|A| \\neq 0\\))",
            ],
        },
    ],
    "formulas": [
        {"label": "Determinant (2x2)", "expr": "\\(\\det(A) = ad - bc\\)"},
        {"label": "Inverse (2x2)", "expr": "\\(A^{-1} = \\frac{1}{ad-bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}\\)"},
        {"label": "Matrix product entry", "expr": "\\(C_{ij} = \\sum_{k} A_{ik} B_{kj}\\)"},
        {"label": "Identity property", "expr": "\\(AI = IA = A\\)"},
    ],
    "tips": [
        "Check dimensions before multiplying: the number of columns of the first must equal the number of rows of the second.",
        "Swap main diagonal and negate off-diagonal entries to find the adjugate of a 2x2 matrix.",
        "When solving \\(AX = B\\), always pre-multiply by \\(A^{-1}\\): \\(X = A^{-1}B\\), not \\(BA^{-1}\\).",
    ],
}
