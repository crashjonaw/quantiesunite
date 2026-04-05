MINDMAP = {
    "concepts": [
        {"title": "Matrix Form", "points": [
            "System \\(A\\mathbf{x} = \\mathbf{b}\\) where \\(A\\) is the coefficient matrix",
            "Augmented matrix: \\([A | \\mathbf{b}]\\) for row reduction",
        ]},
        {"title": "Types of Solutions", "points": [
            "Unique solution: one intersection point (consistent, independent)",
            "No solution: parallel planes/lines (inconsistent)",
            "Infinitely many: dependent equations, free variables",
        ]},
        {"title": "Existence & Uniqueness", "points": [
            "If \\(\\det(A) \\neq 0\\): unique solution \\(\\mathbf{x} = A^{-1}\\mathbf{b}\\)",
            "If \\(\\det(A) = 0\\): either no solution or infinitely many",
            "Rank determines number of free variables: \\(n - \\text{rank}(A)\\)",
        ]},
        {"title": "Homogeneous Systems", "points": [
            "\\(A\\mathbf{x} = \\mathbf{0}\\) always has the trivial solution \\(\\mathbf{x} = \\mathbf{0}\\)",
            "Non-trivial solutions exist iff \\(\\det(A) = 0\\)",
            "Solution set forms a subspace (null space of \\(A\\))",
        ]},
    ],
    "formulas": [
        {"label": "Matrix Equation", "expr": "\\(A\\mathbf{x} = \\mathbf{b}\\)"},
        {"label": "Inverse Solution", "expr": "\\(\\mathbf{x} = A^{-1}\\mathbf{b}\\)"},
        {"label": "Free Variables", "expr": "\\(\\text{free vars} = n - \\text{rank}(A)\\)"},
    ],
    "tips": [
        "Always check rank(A) vs rank([A|b]) to determine solution type",
        "Homogeneous systems always have at least the zero solution",
        "More unknowns than equations guarantees infinitely many solutions (if consistent)",
    ],
}
