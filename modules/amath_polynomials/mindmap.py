MINDMAP = {
    "concepts": [
        {
            "title": "Polynomial Division",
            "points": [
                "Long division: divide leading terms, multiply back, subtract, repeat",
                "If \\(P(x) = D(x) \\cdot Q(x) + R(x)\\), then \\(Q(x)\\) is quotient and \\(R(x)\\) is remainder",
                "Degree of remainder < degree of divisor",
            ],
        },
        {
            "title": "Remainder & Factor Theorems",
            "points": [
                "Remainder Theorem: when \\(P(x)\\) is divided by \\((x - a)\\), remainder = \\(P(a)\\)",
                "Factor Theorem: \\((x - a)\\) is a factor of \\(P(x)\\) iff \\(P(a) = 0\\)",
                "Use factor theorem to find one root, then factorise the quotient",
            ],
        },
        {
            "title": "Partial Fractions",
            "points": [
                "Decompose proper fractions into simpler parts",
                "Linear factors: \\(\\frac{f(x)}{(x-a)(x-b)} = \\frac{A}{x-a} + \\frac{B}{x-b}\\)",
                "Repeated factor: \\(\\frac{f(x)}{(x-a)^2} = \\frac{A}{x-a} + \\frac{B}{(x-a)^2}\\)",
                "Irreducible quadratic: \\(\\frac{f(x)}{(x-a)(x^2+bx+c)} = \\frac{A}{x-a} + \\frac{Bx+C}{x^2+bx+c}\\)",
            ],
        },
        {
            "title": "Improper Fractions",
            "points": [
                "If degree of numerator >= degree of denominator, perform long division first",
                "Express as polynomial + proper fraction, then decompose the proper part",
            ],
        },
    ],
    "formulas": [
        {"label": "Remainder Theorem", "expr": "\\(\\text{Remainder} = P(a) \\text{ when dividing by } (x-a)\\)"},
        {"label": "Factor Theorem", "expr": "\\((x-a) \\text{ is a factor} \\iff P(a) = 0\\)"},
        {"label": "Linear PF", "expr": "\\(\\frac{f(x)}{(x-a)(x-b)} = \\frac{A}{x-a} + \\frac{B}{x-b}\\)"},
        {"label": "Repeated PF", "expr": "\\(\\frac{f(x)}{(x-a)^2(x-b)} = \\frac{A}{x-a} + \\frac{B}{(x-a)^2} + \\frac{C}{x-b}\\)"},
    ],
    "tips": [
        "To find constants in partial fractions, substitute the root of each denominator factor (cover-up method).",
        "Always check that the fraction is proper before decomposing — divide first if it is not.",
        "Equating coefficients is useful when cover-up alone does not determine all constants.",
    ],
}
