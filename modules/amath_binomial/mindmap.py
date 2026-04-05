MINDMAP = {
    "concepts": [
        {
            "title": "Binomial Theorem (Positive Integer Index)",
            "points": [
                "\\((a+b)^n = \\sum_{r=0}^{n} \\binom{n}{r} a^{n-r} b^r\\)",
                "General term: \\(T_{r+1} = \\binom{n}{r} a^{n-r} b^r\\)",
                "There are \\(n+1\\) terms in the expansion",
            ],
        },
        {
            "title": "Binomial Coefficients",
            "points": [
                "\\(\\binom{n}{r} = \\frac{n!}{r!(n-r)!}\\)",
                "Symmetry: \\(\\binom{n}{r} = \\binom{n}{n-r}\\)",
                "Pascal's triangle: \\(\\binom{n}{r} = \\binom{n-1}{r-1} + \\binom{n-1}{r}\\)",
            ],
        },
        {
            "title": "Finding Specific Terms",
            "points": [
                "Identify \\(a\\), \\(b\\), and \\(n\\), then use the general term formula",
                "For the coefficient of \\(x^k\\), set the power of \\(x\\) in \\(T_{r+1}\\) equal to \\(k\\) and solve for \\(r\\)",
                "Term independent of \\(x\\): set power of \\(x\\) to 0",
            ],
        },
        {
            "title": "Binomial with Negative/Fractional Index",
            "points": [
                "\\((1+x)^n = 1 + nx + \\frac{n(n-1)}{2!}x^2 + \\frac{n(n-1)(n-2)}{3!}x^3 + \\cdots\\)",
                "Valid only when \\(|x| < 1\\) for convergence",
                "Infinite series (does not terminate when \\(n\\) is not a positive integer)",
            ],
        },
    ],
    "formulas": [
        {"label": "Binomial Theorem", "expr": "\\((a+b)^n = \\sum_{r=0}^{n} \\binom{n}{r} a^{n-r} b^r\\)"},
        {"label": "General Term", "expr": "\\(T_{r+1} = \\binom{n}{r} a^{n-r} b^r\\)"},
        {"label": "nCr", "expr": "\\(\\binom{n}{r} = \\frac{n!}{r!(n-r)!}\\)"},
        {"label": "Series (any n)", "expr": "\\((1+x)^n = 1 + nx + \\frac{n(n-1)}{2!}x^2 + \\cdots, \\; |x|<1\\)"},
    ],
    "tips": [
        "Be careful with signs: if \\(b\\) is negative, the sign alternates with each power.",
        "For \\((2+3x)^n\\), rewrite as \\(2^n(1+\\frac{3x}{2})^n\\) before applying the series expansion.",
        "The middle term(s): if \\(n\\) is even there is one middle term \\(T_{n/2+1}\\); if \\(n\\) is odd there are two.",
    ],
}
