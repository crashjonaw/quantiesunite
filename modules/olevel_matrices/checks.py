CHECKS = [
    {
        "q": "Add matrices: \\(\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\) and \\(\\mathbf{B} = \\begin{pmatrix} 2 & 0 \\\\ 1 & 5 \\end{pmatrix}\\)",
        "a": "\\(\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} 3 & 2 \\\\ 4 & 9 \\end{pmatrix}\\)",
        "hint": "Add corresponding elements: (1+2, 2+0), (3+1, 4+5)"
    },
    {
        "q": "Multiply: \\(\\begin{pmatrix} 2 & 3 \\\\ 1 & 4 \\end{pmatrix} \\times \\begin{pmatrix} 1 & 0 \\\\ 2 & 1 \\end{pmatrix}\\)",
        "a": "\\(\\begin{pmatrix} 8 & 3 \\\\ 9 & 4 \\end{pmatrix}\\)",
        "hint": "(2,3)·(1,2) = 2+6=8; (2,3)·(0,1) = 0+3=3; (1,4)·(1,2) = 1+8=9; (1,4)·(0,1) = 0+4=4"
    },
    {
        "q": "Find \\(\\det(\\mathbf{A})\\) for \\(\\mathbf{A} = \\begin{pmatrix} 4 & 2 \\\\ 1 & 3 \\end{pmatrix}\\)",
        "a": "\\(\\det(\\mathbf{A}) = 12 - 2 = 10\\)",
        "hint": "\\(\\det = ad - bc = 4(3) - 2(1)\\)"
    },
    {
        "q": "Find \\(\\mathbf{A}^{-1}\\) for \\(\\mathbf{A} = \\begin{pmatrix} 2 & 1 \\\\ 3 & 2 \\end{pmatrix}\\)",
        "a": "\\(\\mathbf{A}^{-1} = \\begin{pmatrix} 2 & -1 \\\\ -3 & 2 \\end{pmatrix}\\)",
        "hint": "\\(\\det = 2(2) - 1(3) = 1\\). Swap 2 and 2, negate 1 and 3."
    },
    {
        "q": "Solve using matrices: \\(2x + y = 5\\), \\(x - y = 1\\)",
        "a": "\\(x = 2,\\ y = 1\\)",
        "hint": "Write as \\(\\mathbf{AX} = \\mathbf{B}\\), find \\(\\mathbf{A}^{-1}\\), then \\(\\mathbf{X} = \\mathbf{A}^{-1}\\mathbf{B}\\)"
    }
]
