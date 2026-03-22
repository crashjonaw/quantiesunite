CHECKS = [
    {
        "q": "Compute the dot product and check orthogonality: u = [1, 2, 3], v = [1, -1, 1].",
        "a": "u · v = 1(1) + 2(-1) + 3(1) = 1 - 2 + 3 = 2 ≠ 0. Not orthogonal (if were 0, they'd be orthogonal).",
        "hint": "Orthogonal means u · v = 0. Compute the sum of products of corresponding components."
    },
    {
        "q": "Normalize the vector v = [3, 4].",
        "a": "||v|| = √(9 + 16) = 5. v̂ = [3/5, 4/5].",
        "hint": "Divide each component by the norm ||v||."
    },
    {
        "q": "Is the set {[1, 0], [0, 1], [1, 1]} orthonormal?",
        "a": "No. [1, 0] and [0, 1] are orthonormal, but [1, 1] has norm √2 ≠ 1, and [1,0]·[1,1]=1≠0. Not orthonormal.",
        "hint": "Orthonormal requires: (1) pairwise orthogonal (dot products = 0), (2) each is unit vector (norm = 1)."
    },
    {
        "q": "Find the orthogonal projection of v = [1, 1] onto u = [1, 0].",
        "a": "proj_u(v) = (v·u / ||u||²)u = (1 / 1)[1, 0] = [1, 0].",
        "hint": "proj_u(v) = (v·u / ||u||²)u. Compute dot product, norm squared, then scale u."
    },
    {
        "q": "What are the normal equations for the least squares problem Ax = b?",
        "a": "AᵀAx = Aᵀb. These equations minimize ||Ax - b||².",
        "hint": "The least squares solution x̂ makes Aᵀ(b - Ax̂) = 0, leading to the normal equations."
    }
]
