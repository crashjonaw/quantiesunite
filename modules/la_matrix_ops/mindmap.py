MINDMAP = {
    "concepts": [
        {
            "title": "Matrix Basics",
            "points": [
                "A matrix is a rectangular array of numbers with \\(m\\) rows and \\(n\\) columns",
                "Entry in row \\(i\\), column \\(j\\) is denoted \\(a_{ij}\\)",
                "Special matrices: zero matrix \\(\\mathbf{0}\\), identity matrix \\(I_n\\), diagonal, symmetric (\\(A = A^T\\))",
            ],
        },
        {
            "title": "Matrix Addition & Scalar Multiplication",
            "points": [
                "Addition is element-wise: \\((A+B)_{ij} = a_{ij} + b_{ij}\\) (same dimensions required)",
                "Scalar multiplication: \\((cA)_{ij} = c \\cdot a_{ij}\\)",
                "Both operations are commutative and associative",
            ],
        },
        {
            "title": "Matrix Multiplication",
            "points": [
                "\\((AB)_{ij} = \\sum_{k=1}^{n} a_{ik} b_{kj}\\)",
                "Requires columns of \\(A\\) = rows of \\(B\\): \\(A_{m \\times n} \\cdot B_{n \\times p} = C_{m \\times p}\\)",
                "NOT commutative: \\(AB \\neq BA\\) in general",
                "Associative: \\(A(BC) = (AB)C\\); Distributive: \\(A(B+C) = AB + AC\\)",
            ],
        },
        {
            "title": "Transpose & Inverse",
            "points": [
                "Transpose: \\((A^T)_{ij} = a_{ji}\\); \\((AB)^T = B^T A^T\\)",
                "Inverse \\(A^{-1}\\) exists iff \\(\\det(A) \\neq 0\\) (square matrices only)",
                "\\(AA^{-1} = A^{-1}A = I\\); \\((AB)^{-1} = B^{-1}A^{-1}\\)",
                "For \\(2 \\times 2\\): \\(\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}^{-1} = \\frac{1}{ad-bc}\\begin{pmatrix}d&-b\\\\-c&a\\end{pmatrix}\\)",
            ],
        },
        {
            "title": "Elementary Row Operations",
            "points": [
                "Swap two rows; multiply a row by a nonzero scalar; add a multiple of one row to another",
                "Used in Gaussian elimination and finding inverses",
                "Each operation corresponds to left-multiplication by an elementary matrix",
            ],
        },
    ],
    "formulas": [
        {"label": "Matrix Product Entry", "expr": "\\((AB)_{ij} = \\sum_{k} a_{ik} b_{kj}\\)"},
        {"label": "2x2 Inverse", "expr": "\\(A^{-1} = \\frac{1}{ad - bc}\\begin{pmatrix}d & -b \\\\ -c & a\\end{pmatrix}\\)"},
        {"label": "Transpose of Product", "expr": "\\((AB)^T = B^T A^T\\)"},
        {"label": "Inverse of Product", "expr": "\\((AB)^{-1} = B^{-1} A^{-1}\\)"},
    ],
    "tips": [
        "Always check dimensions before multiplying: inner dimensions must match.",
        "Matrix multiplication order matters -- AB and BA are generally different (or one may not even exist).",
        "To verify an inverse, confirm both \\(AA^{-1} = I\\) and \\(A^{-1}A = I\\).",
    ],
}
