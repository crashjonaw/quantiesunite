MINDMAP = {
    "concepts": [
        {
            "title": "Set Notation",
            "points": [
                "A set is a collection of distinct objects (elements/members)",
                "Listed: \\(A = \\{1, 2, 3\\}\\); Described: \\(A = \\{x : x \\text{ is a prime} < 10\\}\\)",
                "\\(\\in\\) means 'is an element of'; \\(\\notin\\) means 'is not an element of'",
                "\\(n(A)\\) = number of elements in \\(A\\)",
            ],
        },
        {
            "title": "Special Sets",
            "points": [
                "\\(\\xi\\) (universal set): the set of all elements under consideration",
                "\\(\\emptyset\\) or \\(\\{\\}\\): the empty set (no elements)",
                "Subsets: \\(A \\subseteq B\\) means every element of \\(A\\) is in \\(B\\)",
            ],
        },
        {
            "title": "Set Operations",
            "points": [
                "Union: \\(A \\cup B\\) — elements in \\(A\\) OR \\(B\\) (or both)",
                "Intersection: \\(A \\cap B\\) — elements in BOTH \\(A\\) AND \\(B\\)",
                "Complement: \\(A'\\) — elements in \\(\\xi\\) but NOT in \\(A\\)",
            ],
        },
        {
            "title": "Venn Diagrams",
            "points": [
                "Circles represent sets within a rectangle (\\(\\xi\\))",
                "Overlapping region = intersection",
                "Shade or label regions to represent operations",
                "Fill in values starting from the intersection outwards",
            ],
        },
        {
            "title": "Key Results",
            "points": [
                "\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)",
                "If \\(A \\cap B = \\emptyset\\), the sets are disjoint (mutually exclusive)",
            ],
        },
    ],
    "formulas": [
        {"label": "Addition principle", "expr": "\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)"},
        {"label": "Complement", "expr": "\\(n(A') = n(\\xi) - n(A)\\)"},
        {"label": "De Morgan's Laws", "expr": "\\((A \\cup B)' = A' \\cap B'\\) and \\((A \\cap B)' = A' \\cup B'\\)"},
    ],
    "tips": [
        "Always start filling a Venn diagram from the innermost region (intersection).",
        "Check that all regions add up to \\(n(\\xi)\\).",
        "Use curly braces \\(\\{\\}\\) when listing set elements — order doesn't matter and no repeats.",
    ],
}
