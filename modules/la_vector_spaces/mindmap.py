MINDMAP = {
    "concepts": [
        {
            "title": "Vector Space Definition",
            "points": [
                "A set \\(V\\) with addition and scalar multiplication satisfying 8 axioms (closure, associativity, commutativity, identity, inverses, distributivity)",
                "Common examples: \\(\\mathbb{R}^n\\), polynomial spaces \\(P_n\\), function spaces",
            ],
        },
        {
            "title": "Subspaces",
            "points": [
                "A subset \\(W \\subseteq V\\) that is itself a vector space under the same operations",
                "Subspace test: (1) \\(\\mathbf{0} \\in W\\), (2) closed under addition, (3) closed under scalar multiplication",
                "Column space \\(\\text{Col}(A)\\), null space \\(\\text{Nul}(A)\\), row space \\(\\text{Row}(A)\\)",
            ],
        },
        {
            "title": "Linear Independence & Span",
            "points": [
                "Vectors \\(\\{v_1, \\ldots, v_k\\}\\) are linearly independent if \\(c_1 v_1 + \\cdots + c_k v_k = 0 \\implies\\) all \\(c_i = 0\\)",
                "\\(\\text{Span}\\{v_1, \\ldots, v_k\\}\\) = set of all linear combinations",
            ],
        },
        {
            "title": "Basis & Dimension",
            "points": [
                "A basis is a linearly independent spanning set",
                "Every basis of a vector space has the same number of vectors: the dimension \\(\\dim(V)\\)",
                "Standard basis for \\(\\mathbb{R}^n\\): \\(\\{e_1, e_2, \\ldots, e_n\\}\\)",
            ],
        },
        {
            "title": "Rank-Nullity Theorem",
            "points": [
                "For \\(A_{m \\times n}\\): \\(\\text{rank}(A) + \\text{nullity}(A) = n\\)",
                "\\(\\text{rank}(A) = \\dim(\\text{Col}(A)) = \\dim(\\text{Row}(A))\\)",
                "\\(\\text{nullity}(A) = \\dim(\\text{Nul}(A))\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Rank-Nullity", "expr": "\\(\\text{rank}(A) + \\text{nullity}(A) = n\\)"},
        {"label": "Linear Combination", "expr": "\\(v = c_1 v_1 + c_2 v_2 + \\cdots + c_k v_k\\)"},
        {"label": "Dimension of R^n", "expr": "\\(\\dim(\\mathbb{R}^n) = n\\)"},
    ],
    "tips": [
        "To check if vectors form a basis: verify they are linearly independent AND span the space (or just check that the count equals the dimension).",
        "The null space always contains the zero vector -- if that is the only element, the matrix has full column rank.",
        "Coordinate vectors change when you change the basis; the abstract vector stays the same.",
    ],
}
