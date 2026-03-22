QUIZ = [
    {
        "question": "For A = [[1, 0], [0, 2], [0, 0]], describe its SVD A = UΣVᵀ. What are the dimensions?",
        "answer": "U is 3×3, Σ is 3×2 with σ₁=2, σ₂=1, rest 0, V is 2×2. rank(A) = 2.",
        "explanation": "The matrix is already almost diagonal. U is 3×3 orthogonal, Σ is 3×2 diagonal with 2 nonzero entries, V is 2×2 orthogonal."
    },
    {
        "question": "If A has singular values 10, 5, 1, 0.1, what percentage of variance is explained by the first two principal components?",
        "answer": "(10² + 5²)/(10² + 5² + 1² + 0.1²) = 125/126.01 ≈ 99.2%",
        "explanation": "Variance explained = (sum of first k singular values squared) / (sum of all singular values squared)."
    },
    {
        "question": "True or False: For any matrix A, the SVD always exists and is unique.",
        "answer": "True (existence). Unique for singular values and up to sign for singular vectors.",
        "explanation": "SVD exists for any matrix A (unlike eigendecomposition). Singular vectors can have sign ambiguity but singular values are unique."
    },
    {
        "question": "What is the least squares solution to Ax = b using SVD?",
        "answer": "x̂ = VΣ⁺Uᵀb, where Σ⁺ is the pseudoinverse of Σ (reciprocals of nonzero singular values).",
        "explanation": "This formula works even for rank-deficient A and gives the minimum-norm solution."
    },
    {
        "question": "For a noisy image, why does truncating small singular values help denoise?",
        "answer": "Small singular values typically correspond to noise (high-frequency variations), while large singular values capture the true image structure. Truncating removes the noise component.",
        "explanation": "Noise is spread across all singular values, but true signal dominates large singular values. Low-rank reconstruction filters out noise."
    }
]
