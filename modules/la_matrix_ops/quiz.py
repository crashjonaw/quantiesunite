QUIZ = [
    {
        "question": "Compute \\(\\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\times \\begin{pmatrix} 1 & 2 \\\\ 4 & 0 \\end{pmatrix}\\).",
        "answer": "\\(\\begin{pmatrix} 6 & 4 \\\\ 12 & 0 \\end{pmatrix}\\)",
        "explanation": "First row: \\((2)(1)+(1)(4)=6\\), \\((2)(2)+(1)(0)=4\\). Second row: \\((0)(1)+(3)(4)=12\\), \\((0)(2)+(3)(0)=0\\)."
    },
    {
        "question": "If \\((\\mathbf{AB})^T = \\mathbf{B}^T \\mathbf{A}^T\\), verify this property with \\(\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\end{pmatrix}\\), \\(\\mathbf{B} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\).",
        "answer": "\\(\\mathbf{AB} = (11)\\), \\((\\mathbf{AB})^T = (11)\\). \\(\\mathbf{B}^T \\mathbf{A}^T = \\begin{pmatrix} 3 & 4 \\end{pmatrix}\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = (11)\\). Both equal \\((11)\\). ✓",
        "explanation": "The property \\((\\mathbf{AB})^T = \\mathbf{B}^T \\mathbf{A}^T\\) is a fundamental identity (note order reversal)."
    },
    {
        "question": "True or False: Matrix multiplication is commutative (\\(\\mathbf{AB} = \\mathbf{BA}\\) for all invertible matrices \\(\\mathbf{A}, \\mathbf{B}\\)).",
        "answer": "False",
        "explanation": "Even for invertible matrices, generally \\(\\mathbf{AB} \\neq \\mathbf{BA}\\). They commute only in special cases (e.g., if one is a scalar multiple of the identity)."
    },
    {
        "question": "Find the inverse of \\(\\mathbf{A} = \\begin{pmatrix} 2 & 0 \\\\ 0 & 3 \\end{pmatrix}\\) using Gauss-Jordan.",
        "answer": "\\(\\mathbf{A}^{-1} = \\begin{pmatrix} \\frac{1}{2} & 0 \\\\ 0 & \\frac{1}{3} \\end{pmatrix}\\)",
        "explanation": "\\([\\mathbf{A} \\mid \\mathbf{I}] = \\left(\\begin{array}{cc|cc} 2 & 0 & 1 & 0 \\\\ 0 & 3 & 0 & 1 \\end{array}\\right)\\). Scale \\(R_1\\) by \\(\\frac{1}{2}\\), \\(R_2\\) by \\(\\frac{1}{3}\\) to get \\([\\mathbf{I} \\mid \\mathbf{A}^{-1}]\\)."
    },
    {
        "question": "For a \\(3 \\times 3\\) matrix, \\((\\mathbf{A}^{-1})^{-1}\\) equals what?",
        "answer": "\\(\\mathbf{A}\\)",
        "explanation": "Applying inverse twice returns the original matrix: \\((\\mathbf{A}^{-1})^{-1} = \\mathbf{A}\\)."
    }
]
