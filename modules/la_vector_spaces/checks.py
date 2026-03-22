CHECKS = [
    {
        "q": "Is W = {(x, y) ∈ ℝ² : xy = 0} a subspace of ℝ²?",
        "a": "No. For example, (1, 0) and (0, 1) are in W (products are 0), but (1, 0) + (0, 1) = (1, 1) is not in W (product is 1 ≠ 0). Not closed under addition.",
        "hint": "Check all three subspace conditions: (1) contains 0? (2) closed under addition? (3) closed under scalar multiplication?"
    },
    {
        "q": "Are v₁ = [1, 2, 1], v₂ = [2, 4, 2], v₃ = [1, 1, 1] linearly independent?",
        "a": "No. v₂ = 2v₁, so they're linearly dependent. More generally, v₁ and v₂ are scalar multiples, making the set dependent.",
        "hint": "Check if there exist non-trivial scalars c₁, c₂, c₃ such that c₁v₁ + c₂v₂ + c₃v₃ = 0."
    },
    {
        "q": "What is dim(P₃(ℝ)), the space of polynomials of degree ≤ 3?",
        "a": "dim(P₃(ℝ)) = 4. A basis is {1, x, x², x³}.",
        "hint": "The dimension is the number of vectors in a basis. For P_n, the basis {1, x, x², ..., x^n} has n+1 elements."
    },
    {
        "q": "For a 5×3 matrix A with rank 3, what is the dimension of Null(A)?",
        "a": "dim(Null(A)) = 3 - rank(A) = 3 - 3 = 0. The null space contains only the zero vector.",
        "hint": "Use rank-nullity: rank(A) + nullity(A) = n, where n is the number of columns."
    },
    {
        "q": "What is a basis for the null space of A = [[1, 2, 3], [2, 4, 6]]?",
        "a": "Row reduce: [[1, 2, 3], [0, 0, 0]]. Free variables: x₂ = s, x₃ = t. From x₁ + 2s + 3t = 0: x₁ = -2s - 3t. General solution: x = s[-2, 1, 0] + t[-3, 0, 1]. Basis: {[-2, 1, 0], [-3, 0, 1]}.",
        "hint": "Solve Ax = 0. Set each free variable to 1 (others to 0) and solve for dependent variables."
    }
]
