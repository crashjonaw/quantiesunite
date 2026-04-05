MINDMAP = {
    "concepts": [
        {
            "title": "Sample Spaces & Events",
            "points": [
                "Sample space \\(\\Omega\\): set of all possible outcomes",
                "An event \\(A \\subseteq \\Omega\\) is a subset of outcomes",
                "Complement: \\(A^c\\); Union: \\(A \\cup B\\); Intersection: \\(A \\cap B\\)",
            ],
        },
        {
            "title": "Axioms of Probability (Kolmogorov)",
            "points": [
                "\\(P(A) \\geq 0\\) for all events \\(A\\)",
                "\\(P(\\Omega) = 1\\)",
                "For mutually exclusive events: \\(P(A \\cup B) = P(A) + P(B)\\)",
            ],
        },
        {
            "title": "Key Rules",
            "points": [
                "Addition rule: \\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\\)",
                "Complement rule: \\(P(A^c) = 1 - P(A)\\)",
                "Multiplication rule: \\(P(A \\cap B) = P(A)P(B|A)\\)",
            ],
        },
        {
            "title": "Conditional Probability",
            "points": [
                "\\(P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\) provided \\(P(B) > 0\\)",
                "Events are independent if \\(P(A \\cap B) = P(A)P(B)\\)",
                "Independence \\(\\neq\\) mutually exclusive",
            ],
        },
        {
            "title": "Bayes' Theorem & Law of Total Probability",
            "points": [
                "Total probability: \\(P(B) = \\sum_i P(B|A_i)P(A_i)\\) for a partition \\(\\{A_i\\}\\)",
                "Bayes: \\(P(A_i|B) = \\frac{P(B|A_i)P(A_i)}{P(B)}\\)",
            ],
        },
        {
            "title": "Counting Methods",
            "points": [
                "Permutations: \\(P(n,r) = \\frac{n!}{(n-r)!}\\)",
                "Combinations: \\(\\binom{n}{r} = \\frac{n!}{r!(n-r)!}\\)",
                "Multiplication principle for sequential choices",
            ],
        },
    ],
    "formulas": [
        {"label": "Conditional Probability", "expr": "\\(P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\)"},
        {"label": "Bayes' Theorem", "expr": "\\(P(A|B) = \\frac{P(B|A)P(A)}{P(B)}\\)"},
        {"label": "Addition Rule", "expr": "\\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\\)"},
        {"label": "Combinations", "expr": "\\(\\binom{n}{r} = \\frac{n!}{r!(n-r)!}\\)"},
    ],
    "tips": [
        "When stuck, draw a tree diagram or Venn diagram to visualise the problem.",
        "Independent events: knowing one occurred does not change the probability of the other.",
        "'At least one' problems are often easiest via the complement: \\(P(\\text{at least 1}) = 1 - P(\\text{none})\\).",
    ],
}
