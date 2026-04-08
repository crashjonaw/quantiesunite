QUIZ = [
    {
        "question": "Given \\(\\mathbf{A} = \\begin{pmatrix} 3 & 1 \\\\ 2 & 4 \\end{pmatrix}\\) and \\(\\mathbf{B} = \\begin{pmatrix} 1 & 2 \\\\ 0 & 1 \\end{pmatrix}\\), compute \\(\\mathbf{AB}\\) and \\(\\mathbf{BA}\\). Are they equal?",
        "answer": "\\(\\mathbf{AB} = \\begin{pmatrix} 3 & 7 \\\\ 2 & 8 \\end{pmatrix}\\); \\(\\mathbf{BA} = \\begin{pmatrix} 7 & 9 \\\\ 2 & 4 \\end{pmatrix}\\). No, they are not equal (\\(\\mathbf{AB} \\neq \\mathbf{BA}\\))",
        "explanation": "For \\(\\mathbf{AB}\\): (3)(1)+(1)(0)=3, (3)(2)+(1)(1)=7; (2)(1)+(4)(0)=2, (2)(2)+(4)(1)=8. Matrix multiplication is not commutative."
    },
    {
        "question": "A point P has coordinates (2, 3). Apply a reflection across the x-axis, then a rotation of 180°. What are the final coordinates?",
        "answer": "Final coordinates: \\((-2, 3)\\)",
        "explanation": "Reflection across x-axis: \\(\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix}\\). Then rotation 180°: \\(\\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix} = \\begin{pmatrix} -2 \\\\ 3 \\end{pmatrix}\\)."
    },
    {
        "question": "Find the inverse of \\(\\mathbf{M} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\) and verify \\(\\mathbf{M}\\mathbf{M}^{-1} = \\mathbf{I}\\).",
        "answer": "\\(\\det(\\mathbf{M}) = 4 - 6 = -2\\). \\(\\mathbf{M}^{-1} = \\begin{pmatrix} -2 & 1 \\\\ \\frac{3}{2} & -\\frac{1}{2} \\end{pmatrix}\\). Verification: \\(\\mathbf{M}\\mathbf{M}^{-1} = \\mathbf{I}\\).",
        "explanation": "\\(\\mathbf{M}^{-1} = \\frac{1}{-2}\\begin{pmatrix} 4 & -2 \\\\ -3 & 1 \\end{pmatrix} = \\begin{pmatrix} -2 & 1 \\\\ \\frac{3}{2} & -\\frac{1}{2} \\end{pmatrix}\\). Multiply to verify the identity matrix."
    },
    {
        "question": "A system of equations: \\(3x + 2y = 11\\), \\(2x - y = 7\\). Solve using the matrix method.",
        "answer": "\\(x = 3,\\ y = 1\\)",
        "explanation": "Matrix form: \\(\\begin{pmatrix} 3 & 2 \\\\ 2 & -1 \\end{pmatrix}\\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} 11 \\\\ 7 \\end{pmatrix}\\). \\(\\det = -3 - 4 = -7\\). Solve \\(\\mathbf{X} = \\mathbf{A}^{-1}\\mathbf{B}\\)."
    },
    {
        "question": "A \\(2 \\times 2\\) matrix has determinant 0. What can you conclude about the matrix?",
        "answer": "The matrix is singular (non-invertible). Its inverse does not exist. The corresponding system of equations has either no solution or infinitely many solutions.",
        "explanation": "A zero determinant means the matrix's rows (or columns) are linearly dependent. Geometrically, the transformation collapses the plane onto a line or point."
    }
]
