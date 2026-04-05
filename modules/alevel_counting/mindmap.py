MINDMAP = {
    "concepts": [
        {"title": "Fundamental Counting Principle", "points": [
            "If task A has \\(m\\) ways and task B has \\(n\\) ways, together: \\(m \\times n\\) ways",
            "Addition principle: either A or B = \\(m + n\\) (mutually exclusive)",
        ]},
        {"title": "Permutations", "points": [
            "Arrangements where order matters",
            "\\(n\\) objects: \\(n!\\) arrangements",
            "\\(r\\) from \\(n\\): \\(^nP_r = \\frac{n!}{(n-r)!}\\)",
            "With repetitions: \\(\\frac{n!}{n_1! \\cdot n_2! \\cdots}\\)",
        ]},
        {"title": "Combinations", "points": [
            "Selections where order does not matter",
            "\\(^nC_r = \\binom{n}{r} = \\frac{n!}{r!(n-r)!}\\)",
            "\\(\\binom{n}{r} = \\binom{n}{n-r}\\) — symmetry property",
        ]},
        {"title": "Special Cases", "points": [
            "Circular arrangements: \\((n-1)!\\)",
            "Identical objects: divide by \\(k!\\) for each group of \\(k\\) identical items",
            "At least one / none: use complement — total minus unwanted",
        ]},
    ],
    "formulas": [
        {"label": "Permutation", "expr": "\\(^nP_r = \\frac{n!}{(n-r)!}\\)"},
        {"label": "Combination", "expr": "\\(^nC_r = \\frac{n!}{r!(n-r)!}\\)"},
        {"label": "Circular", "expr": "\\((n-1)!\\)"},
        {"label": "With Repetition", "expr": "\\(\\frac{n!}{n_1! n_2! \\cdots n_k!}\\)"},
    ],
    "tips": [
        "Ask: does ORDER matter? Yes = permutation, No = combination",
        "For 'at least one' problems, use complement: total - none",
        "Draw slots for restricted problems — place the restricted items first",
    ],
}
