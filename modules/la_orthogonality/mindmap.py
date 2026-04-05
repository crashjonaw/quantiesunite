MINDMAP = {
    "concepts": [
        {
            "title": "Inner Product & Orthogonality",
            "points": [
                "Dot product: \\(u \\cdot v = u^T v = \\sum u_i v_i\\)",
                "Vectors are orthogonal if \\(u \\cdot v = 0\\)",
                "Norm: \\(\\|v\\| = \\sqrt{v \\cdot v}\\)",
            ],
        },
        {
            "title": "Orthogonal & Orthonormal Sets",
            "points": [
                "Orthogonal set: all pairs have dot product 0",
                "Orthonormal set: orthogonal + every vector has unit length",
                "Orthogonal sets of nonzero vectors are always linearly independent",
            ],
        },
        {
            "title": "Gram-Schmidt Process",
            "points": [
                "Converts any basis into an orthogonal (or orthonormal) basis",
                "\\(u_1 = v_1\\), then \\(u_k = v_k - \\sum_{j=1}^{k-1} \\frac{v_k \\cdot u_j}{u_j \\cdot u_j} u_j\\)",
                "Normalise each \\(u_k\\) to get an orthonormal basis",
            ],
        },
        {
            "title": "Orthogonal Projections",
            "points": [
                "Projection of \\(v\\) onto \\(u\\): \\(\\text{proj}_u v = \\frac{v \\cdot u}{u \\cdot u} u\\)",
                "Projection onto a subspace \\(W\\): \\(\\hat{x} = (A^T A)^{-1} A^T b\\) where columns of \\(A\\) span \\(W\\)",
            ],
        },
        {
            "title": "Least Squares",
            "points": [
                "When \\(Ax = b\\) has no exact solution, find \\(\\hat{x}\\) minimising \\(\\|Ax - b\\|\\)",
                "Normal equations: \\(A^T A \\hat{x} = A^T b\\)",
                "Applications: line of best fit, polynomial regression, data fitting",
            ],
        },
        {
            "title": "Orthogonal Matrices",
            "points": [
                "\\(Q^T Q = I\\), so \\(Q^{-1} = Q^T\\)",
                "Preserve lengths and angles: \\(\\|Qx\\| = \\|x\\|\\)",
                "Columns form an orthonormal set",
            ],
        },
    ],
    "formulas": [
        {"label": "Projection onto u", "expr": "\\(\\text{proj}_u v = \\frac{v \\cdot u}{u \\cdot u} u\\)"},
        {"label": "Normal Equations", "expr": "\\(A^T A \\hat{x} = A^T b\\)"},
        {"label": "Gram-Schmidt Step", "expr": "\\(u_k = v_k - \\sum_{j<k} \\frac{v_k \\cdot u_j}{u_j \\cdot u_j} u_j\\)"},
        {"label": "Orthogonal Matrix", "expr": "\\(Q^T Q = QQ^T = I\\)"},
    ],
    "tips": [
        "Least squares gives the best approximate solution when an exact one does not exist.",
        "Always check that \\(A^T A\\) is invertible before using the normal equations directly.",
        "Gram-Schmidt is numerically sensitive; in practice, modified Gram-Schmidt or QR factorisation is preferred.",
    ],
}
