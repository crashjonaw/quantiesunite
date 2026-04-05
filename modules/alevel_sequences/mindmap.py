MINDMAP = {
    "concepts": [
        {
            "title": "Arithmetic Progression (AP)",
            "points": [
                "Common difference \\(d = a_{n+1} - a_n\\)",
                "General term: \\(a_n = a + (n-1)d\\)",
                "Sum: \\(S_n = \\frac{n}{2}(2a + (n-1)d) = \\frac{n}{2}(a + l)\\)",
                "\\(a_n = S_n - S_{n-1}\\) for \\(n \\geq 2\\)",
            ],
        },
        {
            "title": "Geometric Progression (GP)",
            "points": [
                "Common ratio \\(r = \\frac{a_{n+1}}{a_n}\\)",
                "General term: \\(a_n = ar^{n-1}\\)",
                "Sum: \\(S_n = \\frac{a(1-r^n)}{1-r} = \\frac{a(r^n-1)}{r-1}\\)",
                "Sum to infinity (\\(|r|<1\\)): \\(S_\\infty = \\frac{a}{1-r}\\)",
            ],
        },
        {
            "title": "Summation Notation",
            "points": [
                "\\(\\sum_{r=1}^{n} r = \\frac{n(n+1)}{2}\\)",
                "\\(\\sum_{r=1}^{n} r^2 = \\frac{n(n+1)(2n+1)}{6}\\)",
                "\\(\\sum_{r=1}^{n} r^3 = \\left[\\frac{n(n+1)}{2}\\right]^2\\)",
                "Linearity: \\(\\sum (af(r) + bg(r)) = a\\sum f(r) + b\\sum g(r)\\)",
            ],
        },
        {
            "title": "Method of Differences",
            "points": [
                "Write \\(u_r = f(r) - f(r+1)\\), then \\(\\sum u_r\\) telescopes",
                "Most terms cancel; only boundary terms survive",
                "Often combined with partial fractions",
            ],
        },
        {
            "title": "Convergence & Recurrence",
            "points": [
                "A GP converges iff \\(|r| < 1\\)",
                "Recurrence relation: defines \\(a_{n+1}\\) in terms of previous terms",
                "Can be used to generate terms or prove results by induction",
            ],
        },
    ],
    "formulas": [
        {"label": "AP general term", "expr": "\\(a_n = a + (n-1)d\\)"},
        {"label": "AP sum", "expr": "\\(S_n = \\frac{n}{2}(2a + (n-1)d)\\)"},
        {"label": "GP general term", "expr": "\\(a_n = ar^{n-1}\\)"},
        {"label": "GP sum", "expr": "\\(S_n = \\frac{a(1-r^n)}{1-r}\\)"},
        {"label": "GP sum to infinity", "expr": "\\(S_\\infty = \\frac{a}{1-r}, \\; |r|<1\\)"},
    ],
    "tips": [
        "To test AP or GP: check if differences are constant (AP) or ratios are constant (GP).",
        "For sum to infinity, always verify \\(|r| < 1\\) first.",
        "When the sum \\(S_n\\) is given, find \\(a_n\\) using \\(a_n = S_n - S_{n-1}\\) and check \\(a_1 = S_1\\) separately.",
    ],
}
