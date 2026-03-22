QUIZ = [
    {
        "question": "Is ℝ² a vector space over ℝ? Verify two axioms: closure under addition and existence of zero element.",
        "answer": "Yes. (1) If (x₁,y₁), (x₂,y₂) ∈ ℝ², then (x₁+x₂, y₁+y₂) ∈ ℝ². (2) Zero element (0,0) is in ℝ² and (x,y) + (0,0) = (x,y).",
        "explanation": "These two properties, along with the other 8 axioms, make ℝ² a vector space."
    },
    {
        "question": "Find a basis for W = span{[1,0,1], [0,1,2], [1,1,3]}. What is dim(W)?",
        "answer": "Form matrix: [[1,0,1],[0,1,2],[1,1,3]]. RREF: [[1,0,1],[0,1,2],[0,0,0]]. Basis: {[1,0,1], [0,1,2]}. dim(W) = 2.",
        "explanation": "The rank of the matrix equals the dimension of the span. Use row reduction to find linearly independent vectors."
    },
    {
        "question": "If A is 4×6 with rank 3, what is dim(Null(A))?",
        "answer": "dim(Null(A)) = 6 - 3 = 3",
        "explanation": "By rank-nullity theorem: rank(A) + nullity(A) = number of columns."
    },
    {
        "question": "True or False: A linearly independent set can have more vectors than any spanning set of the same space.",
        "answer": "False",
        "explanation": "All bases of a finite-dimensional vector space have the same size (the dimension). Any linearly independent set has at most dim(V) vectors."
    },
    {
        "question": "In ℝ³, are [1,2,0], [0,1,1], [1,0,2] linearly independent?",
        "answer": "Yes. Form matrix and compute determinant: det([[1,0,1],[2,1,0],[0,1,2]]) = 1(2-0) - 0 + 1(2-0) = 4 ≠ 0.",
        "explanation": "For a square matrix, linear independence (rank = 3) is equivalent to det ≠ 0."
    }
]
