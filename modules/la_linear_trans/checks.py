CHECKS = [
    {
        "q": "Is T(x, y) = (x + 1, y) a linear transformation?",
        "a": "No. T(0, 0) = (1, 0) ≠ (0, 0), so it doesn't map zero to zero. Not linear.",
        "hint": "A linear transformation must satisfy T(0) = 0. Check if T(cu + dv) = cT(u) + dT(v)."
    },
    {
        "q": "Find the matrix representation of T(x, y) = (y, x).",
        "a": "T(e₁) = T(1, 0) = (0, 1), T(e₂) = T(0, 1) = (1, 0). A = [[0, 1], [1, 0]]",
        "hint": "The columns are T(e₁) and T(e₂). Stack them side by side."
    },
    {
        "q": "Find the kernel and image of T(x, y, z) = (x + y, x + y).",
        "a": "ker(T): Solve [1, 1, 0] · [x, y, z] = 0. Kernel is {t(−1, 1, 0) + s(0, 0, 1) : t, s ∈ ℝ}, dim = 2. Image: rank = 1, im(T) = span{(1, 1)}, dim = 1.",
        "hint": "Kernel: solve Ax = 0. Image: find rank of matrix [[1, 1, 0], [1, 1, 0]]. Use rank-nullity: rank + nullity = 3."
    },
    {
        "q": "For a 3×3 matrix A with rank 2, what is the dimension of the kernel?",
        "a": "dim(ker(A)) = 3 - 2 = 1 (by rank-nullity theorem).",
        "hint": "rank(T) + nullity(T) = dim(V). Here V = ℝ³, so dim(V) = 3."
    },
    {
        "q": "What does it mean for an eigenvector v with eigenvalue λ = 0?",
        "a": "It means Av = 0·v = 0, so v is in the kernel of A. Eigenvectors with eigenvalue 0 are exactly the nonzero kernel elements.",
        "hint": "If λ = 0 is an eigenvalue, the kernel is nontrivial, so A is singular (det(A) = 0)."
    }
]
