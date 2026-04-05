MINDMAP = {
    "concepts": [
        {
            "title": "Eigenvalues & Eigenvectors",
            "points": [
                "\\(Av = \\lambda v\\) where \\(\\lambda\\) is an eigenvalue and \\(v \\neq 0\\) is the corresponding eigenvector",
                "Eigenvectors are directions that are only scaled (not rotated) by the transformation",
            ],
        },
        {
            "title": "Characteristic Equation",
            "points": [
                "\\(\\det(A - \\lambda I) = 0\\) gives the characteristic polynomial",
                "Roots of the characteristic polynomial are the eigenvalues",
                "For \\(2 \\times 2\\): \\(\\lambda^2 - \\text{tr}(A)\\lambda + \\det(A) = 0\\)",
            ],
        },
        {
            "title": "Eigenspaces",
            "points": [
                "The eigenspace for \\(\\lambda\\) is \\(\\text{Nul}(A - \\lambda I)\\)",
                "Algebraic multiplicity: multiplicity of \\(\\lambda\\) as a root of the characteristic polynomial",
                "Geometric multiplicity: \\(\\dim(\\text{Nul}(A - \\lambda I))\\); always \\(\\leq\\) algebraic multiplicity",
            ],
        },
        {
            "title": "Diagonalisation",
            "points": [
                "\\(A = PDP^{-1}\\) where \\(D\\) is diagonal (eigenvalues) and \\(P\\) has eigenvector columns",
                "Possible iff \\(A\\) has \\(n\\) linearly independent eigenvectors",
                "Powers become easy: \\(A^k = PD^kP^{-1}\\)",
            ],
        },
        {
            "title": "Symmetric Matrices",
            "points": [
                "Real symmetric matrices always have real eigenvalues",
                "Eigenvectors of distinct eigenvalues are orthogonal",
                "Spectral theorem: \\(A = Q\\Lambda Q^T\\) with \\(Q\\) orthogonal",
            ],
        },
    ],
    "formulas": [
        {"label": "Eigen Equation", "expr": "\\(Av = \\lambda v\\)"},
        {"label": "Characteristic Polynomial", "expr": "\\(\\det(A - \\lambda I) = 0\\)"},
        {"label": "Diagonalisation", "expr": "\\(A = PDP^{-1}\\)"},
        {"label": "Matrix Power", "expr": "\\(A^k = PD^kP^{-1}\\)"},
        {"label": "Trace & Determinant", "expr": "\\(\\text{tr}(A) = \\sum \\lambda_i, \\quad \\det(A) = \\prod \\lambda_i\\)"},
    ],
    "tips": [
        "The trace equals the sum of eigenvalues and the determinant equals their product -- useful sanity checks.",
        "If geometric multiplicity < algebraic multiplicity for any eigenvalue, the matrix is not diagonalisable.",
        "For symmetric matrices, you can always find an orthonormal eigenbasis.",
    ],
}
