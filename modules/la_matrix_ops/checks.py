CHECKS = [
    {
        "q": "Compute \\(\\begin{pmatrix} 1 & 2 \\end{pmatrix} + \\begin{pmatrix} 3 & 4 \\end{pmatrix}\\) and \\(2\\begin{pmatrix} 1 & 2 \\end{pmatrix}\\).",
        "a": "\\(\\begin{pmatrix} 1 & 2 \\end{pmatrix} + \\begin{pmatrix} 3 & 4 \\end{pmatrix} = \\begin{pmatrix} 4 & 6 \\end{pmatrix}\\). \\(2\\begin{pmatrix} 1 & 2 \\end{pmatrix} = \\begin{pmatrix} 2 & 4 \\end{pmatrix}\\).",
        "hint": "Add element-wise. Multiply each element by the scalar."
    },
    {
        "q": "Multiply \\(\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\) by \\(\\mathbf{B} = \\begin{pmatrix} 5 & 6 \\\\ 7 & 8 \\end{pmatrix}\\). What is \\(\\mathbf{AB}\\)?",
        "a": "\\(\\mathbf{AB} = \\begin{pmatrix} 1 \\cdot 5 + 2 \\cdot 7 & 1 \\cdot 6 + 2 \\cdot 8 \\\\ 3 \\cdot 5 + 4 \\cdot 7 & 3 \\cdot 6 + 4 \\cdot 8 \\end{pmatrix} = \\begin{pmatrix} 19 & 22 \\\\ 43 & 50 \\end{pmatrix}\\)",
        "hint": "\\(c_{ij}\\) = row \\(i\\) of \\(\\mathbf{A}\\) · column \\(j\\) of \\(\\mathbf{B}\\) (dot product)."
    },
    {
        "q": "If \\(\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}\\), what is \\(\\mathbf{A}^T\\) (transpose)?",
        "a": "\\(\\mathbf{A}^T = \\begin{pmatrix} 1 & 4 \\\\ 2 & 5 \\\\ 3 & 6 \\end{pmatrix}\\)",
        "hint": "Swap rows and columns: \\((\\mathbf{A}^T)_{ij} = a_{ji}\\)."
    },
    {
        "q": "Is \\(\\begin{pmatrix} 1 & 2 \\\\ 2 & 5 \\end{pmatrix}\\) symmetric? Is \\(\\begin{pmatrix} 0 & 3 \\\\ -3 & 0 \\end{pmatrix}\\) skew-symmetric?",
        "a": "Yes, \\(\\begin{pmatrix} 1 & 2 \\\\ 2 & 5 \\end{pmatrix}\\) is symmetric (entries are symmetric about the diagonal). Yes, \\(\\begin{pmatrix} 0 & 3 \\\\ -3 & 0 \\end{pmatrix}\\) is skew-symmetric (entries are negatives across the diagonal).",
        "hint": "\\(\\mathbf{A}\\) is symmetric if \\(\\mathbf{A}^T = \\mathbf{A}\\). \\(\\mathbf{A}\\) is skew-symmetric if \\(\\mathbf{A}^T = -\\mathbf{A}\\)."
    },
    {
        "q": "For a square matrix \\(\\mathbf{A}\\), when does \\(\\mathbf{A}^{-1}\\) exist?",
        "a": "When \\(\\det(\\mathbf{A}) \\neq 0\\), or equivalently, when \\(\\text{rank}(\\mathbf{A}) = n\\) (full rank), or when \\(\\mathbf{Ax} = \\mathbf{0}\\) has only the trivial solution \\(\\mathbf{x} = \\mathbf{0}\\).",
        "hint": "These three conditions are equivalent for square matrices. \\(\\mathbf{A}\\) is invertible if and only if it's nonsingular."
    }
]
