MINDMAP = {
    "concepts": [
        {
            "title": "Tree Diagrams",
            "points": [
                "Each branch represents an outcome with its probability",
                "Multiply along branches for combined probability (AND)",
                "Add across branches for alternative outcomes (OR)",
                "All branches from a node must sum to 1",
            ],
        },
        {
            "title": "Combined Events",
            "points": [
                "Addition rule: \\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\\)",
                "For mutually exclusive events: \\(P(A \\cup B) = P(A) + P(B)\\)",
                "Multiplication rule (independent): \\(P(A \\cap B) = P(A) \\times P(B)\\)",
                "Complement: \\(P(A') = 1 - P(A)\\)",
            ],
        },
        {
            "title": "Conditional Probability",
            "points": [
                "Probability of A given B has occurred",
                "\\(P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\)",
                "Without replacement problems change probabilities on second draw",
                "Two-way tables and Venn diagrams help organise conditional data",
            ],
        },
        {
            "title": "Independent vs Dependent Events",
            "points": [
                "Independent: occurrence of one does not affect the other",
                "Test: events are independent iff \\(P(A \\cap B) = P(A) \\times P(B)\\)",
                "Sampling without replacement creates dependent events",
            ],
        },
    ],
    "formulas": [
        {"label": "Addition Rule", "expr": "\\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\\)"},
        {"label": "Conditional Probability", "expr": "\\(P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\)"},
        {"label": "Independent Events", "expr": "\\(P(A \\cap B) = P(A) \\cdot P(B)\\)"},
        {"label": "Complement", "expr": "\\(P(A') = 1 - P(A)\\)"},
        {"label": "At least one (independent)", "expr": "\\(P(\\text{at least 1}) = 1 - P(\\text{none})\\)"},
    ],
    "tips": [
        "For 'at least one' problems, use the complement: \\(1 - P(\\text{none})\\).",
        "In without-replacement problems, update both numerator and denominator at each stage.",
        "Always check whether events are mutually exclusive or independent — they are different concepts.",
    ],
}
