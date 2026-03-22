QUIZ = [
    {
        "question": "For a 3×3 diagonal matrix D = diag(2, -3, 5), what is det(D)?",
        "answer": "det(D) = 2·(-3)·5 = -30",
        "explanation": "For a diagonal matrix, the determinant is the product of diagonal entries."
    },
    {
        "question": "If det(A) = 4 and A is 2×2, what is det(2A)?",
        "answer": "det(2A) = 2²·det(A) = 4·4 = 16",
        "explanation": "For an n×n matrix, det(cA) = c^n·det(A). Here n=2, c=2."
    },
    {
        "question": "True or False: det(AB) = det(A)·det(B) for all square matrices A, B.",
        "answer": "True",
        "explanation": "The multiplicativity property holds: det(AB) = det(A)·det(B)."
    },
    {
        "question": "If a matrix A has eigenvalues 2, 3, and 5, what is det(A)?",
        "answer": "det(A) = 2·3·5 = 30",
        "explanation": "The determinant equals the product of eigenvalues: det(A) = ∏λᵢ."
    },
    {
        "question": "For an invertible matrix A, relate det(A) and det(A^(-1)).",
        "answer": "det(A^(-1)) = 1/det(A)",
        "explanation": "Since AA^(-1) = I, we have det(A)·det(A^(-1)) = det(I) = 1, so det(A^(-1)) = 1/det(A)."
    }
]
