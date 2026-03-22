CHECKS = [
    {
        "q": "For A = UΣVᵀ, which matrices are orthogonal?",
        "a": "U and V are orthogonal (square orthogonal matrices). Σ is diagonal (not generally orthogonal).",
        "hint": "Orthogonal matrices satisfy Qᵀ = Q⁻¹ and have orthonormal columns."
    },
    {
        "q": "If A is 5×3 with rank 2, how many nonzero singular values does it have?",
        "a": "Exactly 2 nonzero singular values. rank(A) = number of nonzero singular values.",
        "hint": "Singular values correspond to independent rows/columns. Nonzero σᵢ ⟺ rank."
    },
    {
        "q": "For A = UΣVᵀ, how do you compute the low-rank approximation A_k using the first k singular values?",
        "a": "A_k = Σⱼ₌₁ᵏ σⱼ uⱼ vⱼᵀ, where uⱼ and vⱼ are the j-th columns of U and V.",
        "hint": "Keep only the first k columns of U and V, and set remaining singular values to 0 in Σ."
    },
    {
        "q": "What is the Moore-Penrose pseudoinverse A⁺ in terms of SVD?",
        "a": "A⁺ = VΣ⁺Uᵀ, where Σ⁺ is the diagonal matrix of reciprocals of nonzero singular values.",
        "hint": "Σ⁺ has 1/σᵢ for nonzero σᵢ and 0 for zero σᵢ."
    },
    {
        "q": "Why is SVD numerically more stable than computing (AᵀA)⁻¹Aᵀb for least squares?",
        "a": "SVD works directly with A, while (AᵀA) has condition number κ(AᵀA) = κ(A)², squaring the ill-conditioning. Also, AᵀA can lose information due to rounding.",
        "hint": "Computing AᵀA multiplies the condition number by itself, amplifying numerical errors."
    }
]
