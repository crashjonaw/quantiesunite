QUIZ = [
    {
        "question": "Is T(p(x)) = p'(x) (differentiation) a linear transformation from P₃(ℝ) to P₂(ℝ)?",
        "answer": "Yes. T(p+q) = (p+q)' = p' + q' = T(p) + T(q). T(cp) = (cp)' = cp' = cT(p).",
        "explanation": "Differentiation preserves linear combinations, making it a linear transformation."
    },
    {
        "question": "Find eigenvalues of A = [[2, 1], [0, 3]].",
        "answer": "det(A - λI) = det([[2-λ, 1], [0, 3-λ]]) = (2-λ)(3-λ) = 0. Eigenvalues: λ = 2, 3.",
        "explanation": "For upper triangular matrices, eigenvalues are the diagonal entries."
    },
    {
        "question": "If A is 5×3 with rank 2, what is dim(ker(A))?",
        "answer": "dim(ker(A)) = 3 - rank(A) = 3 - 2 = 1",
        "explanation": "The rank-nullity theorem: rank + nullity = number of columns."
    },
    {
        "question": "True or False: A 2×2 matrix with eigenvalues 2 and 3 is diagonalizable.",
        "answer": "True",
        "explanation": "Distinct eigenvalues guarantee diagonalizability. The eigenvectors are linearly independent."
    },
    {
        "question": "What is the image of T(x, y) = (x, x)?",
        "answer": "im(T) = {(a, a) : a ∈ ℝ} = span{(1, 1)}, which is a 1-dimensional subspace.",
        "explanation": "The image consists of all possible outputs T(x,y). Here, all outputs have equal components."
    }
]
