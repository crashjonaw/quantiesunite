MINDMAP = {
    "concepts": [
        {
            "title": "Definition of a Linear Transformation",
            "points": [
                "A function \\(T: V \\to W\\) satisfying \\(T(u+v) = T(u)+T(v)\\) and \\(T(cv) = cT(v)\\)",
                "Equivalently: \\(T(c_1 v_1 + c_2 v_2) = c_1 T(v_1) + c_2 T(v_2)\\)",
                "Every linear transformation from \\(\\mathbb{R}^n\\) to \\(\\mathbb{R}^m\\) can be represented by an \\(m \\times n\\) matrix",
            ],
        },
        {
            "title": "Matrix Representation",
            "points": [
                "\\(T(x) = Ax\\) where columns of \\(A\\) are \\(T(e_1), T(e_2), \\ldots, T(e_n)\\)",
                "Composition of transformations = matrix multiplication: \\(T_2 \\circ T_1 \\leftrightarrow A_2 A_1\\)",
            ],
        },
        {
            "title": "Kernel & Image",
            "points": [
                "Kernel (null space): \\(\\ker(T) = \\{v \\in V : T(v) = 0\\}\\)",
                "Image (range): \\(\\text{Im}(T) = \\{T(v) : v \\in V\\}\\)",
                "\\(T\\) is injective (one-to-one) \\(\\iff \\ker(T) = \\{0\\}\\)",
                "\\(T\\) is surjective (onto) \\(\\iff \\text{Im}(T) = W\\)",
            ],
        },
        {
            "title": "Common Geometric Transformations in \\(\\mathbb{R}^2\\)",
            "points": [
                "Rotation by \\(\\theta\\): \\(\\begin{pmatrix}\\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta\\end{pmatrix}\\)",
                "Reflection across \\(x\\)-axis: \\(\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}\\)",
                "Scaling: \\(\\begin{pmatrix}k_1&0\\\\0&k_2\\end{pmatrix}\\)",
                "Shear: \\(\\begin{pmatrix}1&k\\\\0&1\\end{pmatrix}\\)",
            ],
        },
        {
            "title": "Change of Basis",
            "points": [
                "If \\(P\\) is the change-of-basis matrix from \\(\\mathcal{B}'\\) to \\(\\mathcal{B}\\), then \\([T]_{\\mathcal{B}'} = P^{-1}[T]_{\\mathcal{B}}P\\)",
                "Similar matrices represent the same transformation in different bases",
            ],
        },
    ],
    "formulas": [
        {"label": "Linearity Condition", "expr": "\\(T(\\alpha u + \\beta v) = \\alpha T(u) + \\beta T(v)\\)"},
        {"label": "Rotation Matrix", "expr": "\\(R_\\theta = \\begin{pmatrix}\\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta\\end{pmatrix}\\)"},
        {"label": "Rank-Nullity for T", "expr": "\\(\\dim(\\ker T) + \\dim(\\text{Im}\\ T) = \\dim(V)\\)"},
        {"label": "Change of Basis", "expr": "\\([T]_{\\mathcal{B}'} = P^{-1}[T]_{\\mathcal{B}}P\\)"},
    ],
    "tips": [
        "To find the matrix of a linear transformation, compute where each standard basis vector is sent.",
        "Injectivity and surjectivity can both be checked via the rank of the matrix representation.",
        "Composition order matters: \\(T_2 \\circ T_1\\) means apply \\(T_1\\) first, then \\(T_2\\).",
    ],
}
