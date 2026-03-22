QUIZ = [
    {
        "question": "What angle θ do vectors [1, 0] and [1, 1] make? (Use cos(θ) = (u·v)/(||u||||v||))",
        "answer": "u·v = 1, ||u|| = 1, ||v|| = √2. cos(θ) = 1/√2, so θ = 45° or π/4 radians.",
        "explanation": "The formula cos(θ) = (u·v)/(||u||||v||) comes from the definition of dot product in terms of angle."
    },
    {
        "question": "True or False: If Q is an orthogonal matrix, then ||Qv|| = ||v|| for all vectors v.",
        "answer": "True",
        "explanation": "||Qv||² = (Qv)·(Qv) = vᵀQᵀQv = vᵀIv = vᵀv = ||v||². Orthogonal matrices preserve length."
    },
    {
        "question": "Apply one step of Gram-Schmidt to v₁ = [1, 0], v₂ = [1, 1]. What is w₂ (before normalizing)?",
        "answer": "w₁ = [1, 0], u₁ = [1, 0]. w₂ = v₂ - (v₂·u₁)u₁ = [1, 1] - 1·[1, 0] = [0, 1].",
        "explanation": "Subtract the projection of v₂ onto u₁ to make w₂ orthogonal to w₁."
    },
    {
        "question": "If A = QR with orthonormal Q, what is the least squares solution to Ax = b?",
        "answer": "x̂ = R⁻¹Qᵀb",
        "explanation": "The QR decomposition gives a numerically stable way to solve least squares: Ax = b becomes QRx = b, so Rx = Qᵀb."
    },
    {
        "question": "What does it mean geometrically when b is in the column space of A?",
        "answer": "It means Ax = b has an exact solution (not just a least squares solution). The projection of b onto Col(A) is b itself.",
        "explanation": "If b ∈ Col(A), then b = Ax for some x. The residual is zero: ||Ax - b|| = 0."
    }
]
