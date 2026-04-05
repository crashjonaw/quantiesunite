MINDMAP = {
    "concepts": [
        {
            "title": "SVD Factorisation",
            "points": [
                "Any \\(m \\times n\\) matrix \\(A\\) can be written as \\(A = U \\Sigma V^T\\)",
                "\\(U\\) is \\(m \\times m\\) orthogonal (left singular vectors)",
                "\\(V\\) is \\(n \\times n\\) orthogonal (right singular vectors)",
                "\\(\\Sigma\\) is \\(m \\times n\\) diagonal with singular values \\(\\sigma_1 \\geq \\sigma_2 \\geq \\cdots \\geq 0\\)",
            ],
        },
        {
            "title": "Computing the SVD",
            "points": [
                "Singular values: \\(\\sigma_i = \\sqrt{\\lambda_i(A^T A)}\\)",
                "\\(V\\): eigenvectors of \\(A^T A\\)",
                "\\(U\\): eigenvectors of \\(AA^T\\), or compute \\(u_i = \\frac{1}{\\sigma_i} A v_i\\)",
            ],
        },
        {
            "title": "Reduced (Thin) SVD",
            "points": [
                "Keep only the \\(r\\) nonzero singular values (\\(r = \\text{rank}(A)\\))",
                "\\(A = U_r \\Sigma_r V_r^T\\) with \\(U_r\\) is \\(m \\times r\\), \\(\\Sigma_r\\) is \\(r \\times r\\), \\(V_r\\) is \\(n \\times r\\)",
            ],
        },
        {
            "title": "Low-Rank Approximation",
            "points": [
                "Best rank-\\(k\\) approximation (Eckart-Young theorem): \\(A_k = \\sum_{i=1}^{k} \\sigma_i u_i v_i^T\\)",
                "Minimises \\(\\|A - A_k\\|_F\\) over all rank-\\(k\\) matrices",
                "Used in image compression, dimensionality reduction, noise filtering",
            ],
        },
        {
            "title": "Applications",
            "points": [
                "Pseudoinverse: \\(A^+ = V \\Sigma^+ U^T\\)",
                "Principal Component Analysis (PCA) is built on the SVD",
                "Condition number: \\(\\kappa(A) = \\sigma_1 / \\sigma_r\\)",
                "Solving least squares problems numerically via SVD is more stable than normal equations",
            ],
        },
    ],
    "formulas": [
        {"label": "SVD", "expr": "\\(A = U \\Sigma V^T\\)"},
        {"label": "Singular Values", "expr": "\\(\\sigma_i = \\sqrt{\\lambda_i(A^T A)}\\)"},
        {"label": "Rank-k Approximation", "expr": "\\(A_k = \\sum_{i=1}^{k} \\sigma_i u_i v_i^T\\)"},
        {"label": "Pseudoinverse", "expr": "\\(A^+ = V \\Sigma^+ U^T\\)"},
        {"label": "Frobenius Error", "expr": "\\(\\|A - A_k\\|_F = \\sqrt{\\sigma_{k+1}^2 + \\cdots + \\sigma_r^2}\\)"},
    ],
    "tips": [
        "SVD exists for every matrix (not just square ones) -- it is the most general decomposition.",
        "The number of nonzero singular values equals the rank of the matrix.",
        "A large condition number \\(\\sigma_1/\\sigma_r\\) means the matrix is ill-conditioned and solutions are sensitive to perturbations.",
    ],
}
