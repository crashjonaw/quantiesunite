MINDMAP = {
    "concepts": [
        {
            "title": "What is a Vector?",
            "points": [
                "A vector has magnitude (size) AND direction",
                "Written as \\(\\vec{AB}\\), \\(\\mathbf{a}\\), or \\(\\begin{pmatrix} x \\\\ y \\end{pmatrix}\\)",
                "A scalar has magnitude only (just a number)",
            ],
        },
        {
            "title": "Column Vectors",
            "points": [
                "\\(\\begin{pmatrix} x \\\\ y \\end{pmatrix}\\): \\(x\\) = horizontal, \\(y\\) = vertical",
                "Positive \\(x\\) → right; positive \\(y\\) → up",
                "Example: \\(\\begin{pmatrix} 3 \\\\ -2 \\end{pmatrix}\\) means 3 right, 2 down",
            ],
        },
        {
            "title": "Vector Operations",
            "points": [
                "Addition: \\(\\begin{pmatrix} a \\\\ b \\end{pmatrix} + \\begin{pmatrix} c \\\\ d \\end{pmatrix} = \\begin{pmatrix} a+c \\\\ b+d \\end{pmatrix}\\)",
                "Subtraction: \\(\\vec{AB} = \\vec{OB} - \\vec{OA} = \\mathbf{b} - \\mathbf{a}\\)",
                "Scalar multiplication: \\(k\\begin{pmatrix} a \\\\ b \\end{pmatrix} = \\begin{pmatrix} ka \\\\ kb \\end{pmatrix}\\)",
            ],
        },
        {
            "title": "Magnitude of a Vector",
            "points": [
                "\\(|\\mathbf{a}| = \\sqrt{x^2 + y^2}\\)",
                "This is the length of the vector (using Pythagoras)",
            ],
        },
        {
            "title": "Parallel & Equal Vectors",
            "points": [
                "Parallel vectors: one is a scalar multiple of the other, \\(\\mathbf{b} = k\\mathbf{a}\\)",
                "Equal vectors: same magnitude AND direction (same column vector)",
                "Negative vector: \\(-\\mathbf{a}\\) has same magnitude but opposite direction",
            ],
        },
        {
            "title": "Position Vectors & Midpoint",
            "points": [
                "Position vector of \\(A\\) = \\(\\vec{OA}\\) where \\(O\\) is the origin",
                "\\(\\vec{AB} = \\vec{OB} - \\vec{OA}\\)",
                "Midpoint \\(M\\): \\(\\vec{OM} = \\frac{1}{2}(\\vec{OA} + \\vec{OB})\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Magnitude", "expr": "\\(|\\mathbf{a}| = \\sqrt{x^2 + y^2}\\)"},
        {"label": "Vector between points", "expr": "\\(\\vec{AB} = \\vec{OB} - \\vec{OA}\\)"},
        {"label": "Midpoint vector", "expr": "\\(\\vec{OM} = \\frac{1}{2}(\\vec{OA} + \\vec{OB})\\)"},
        {"label": "Scalar multiple", "expr": "\\(k\\mathbf{a} = k\\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} kx \\\\ ky \\end{pmatrix}\\)"},
    ],
    "tips": [
        "To go from A to B via the origin: \\(\\vec{AB} = -\\vec{OA} + \\vec{OB} = \\mathbf{b} - \\mathbf{a}\\).",
        "Parallel vectors: check if one column vector is a scalar multiple of the other.",
        "Vectors are equal only if BOTH components match — check \\(x\\) and \\(y\\) separately.",
    ],
}
