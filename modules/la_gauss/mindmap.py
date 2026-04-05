MINDMAP = {
    "concepts": [
        {"title": "Row Operations", "points": [
            "Swap two rows: \\(R_i \\leftrightarrow R_j\\)",
            "Scale a row: \\(R_i \\to kR_i\\) where \\(k \\neq 0\\)",
            "Add multiple of one row to another: \\(R_i \\to R_i + kR_j\\)",
        ]},
        {"title": "Row Echelon Form (REF)", "points": [
            "Leading entry (pivot) of each row is to the right of the row above",
            "All entries below each pivot are zero",
            "Rows of all zeros are at the bottom",
        ]},
        {"title": "Reduced Row Echelon Form (RREF)", "points": [
            "All pivots are 1",
            "Each pivot is the only nonzero entry in its column",
            "Gauss-Jordan elimination produces RREF",
        ]},
        {"title": "Back Substitution", "points": [
            "After reaching REF, solve from bottom row upward",
            "Free variables: columns without pivots — set as parameters",
            "Express pivot variables in terms of free variables",
        ]},
    ],
    "formulas": [
        {"label": "Row Replacement", "expr": "\\(R_i \\to R_i - \\frac{a_{ij}}{a_{jj}} R_j\\)"},
        {"label": "Rank", "expr": "\\(\\text{rank}(A) = \\text{number of pivots}\\)"},
        {"label": "Nullity", "expr": "\\(\\text{nullity}(A) = n - \\text{rank}(A)\\)"},
    ],
    "tips": [
        "Choose the largest pivot (partial pivoting) to reduce rounding errors",
        "RREF is unique for a given matrix; REF is not",
        "The rank-nullity theorem: rank(A) + nullity(A) = number of columns",
    ],
}
