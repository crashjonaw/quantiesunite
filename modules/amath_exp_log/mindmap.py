MINDMAP = {
    "concepts": [
        {
            "title": "Exponential Functions",
            "points": [
                "\\(y = a^x\\) where \\(a > 0, a \\neq 1\\)",
                "Always passes through \\((0, 1)\\); always positive",
                "\\(a > 1\\): increasing; \\(0 < a < 1\\): decreasing",
                "Natural exponential: \\(e \\approx 2.718\\); \\(y = e^x\\) is its own derivative",
            ],
        },
        {
            "title": "Logarithmic Functions",
            "points": [
                "\\(\\log_a x = y \\iff a^y = x\\)",
                "Domain: \\(x > 0\\); passes through \\((1, 0)\\)",
                "Natural log: \\(\\ln x = \\log_e x\\)",
                "\\(\\ln\\) and \\(e^x\\) are inverse functions",
            ],
        },
        {
            "title": "Laws of Logarithms",
            "points": [
                "\\(\\log_a (xy) = \\log_a x + \\log_a y\\)",
                "\\(\\log_a \\left(\\frac{x}{y}\\right) = \\log_a x - \\log_a y\\)",
                "\\(\\log_a (x^n) = n \\log_a x\\)",
                "Change of base: \\(\\log_a b = \\frac{\\log_c b}{\\log_c a}\\)",
            ],
        },
        {
            "title": "Solving Equations",
            "points": [
                "Exponential equations: take log of both sides",
                "Logarithmic equations: convert to exponential form",
                "Equations of the form \\(a^{2x} + a^x + c = 0\\): substitute \\(u = a^x\\)",
            ],
        },
        {
            "title": "Linear Law",
            "points": [
                "Convert \\(y = ax^n\\) to \\(\\ln y = n \\ln x + \\ln a\\) (plot \\(\\ln y\\) vs \\(\\ln x\\))",
                "Convert \\(y = ab^x\\) to \\(\\lg y = x \\lg b + \\lg a\\) (plot \\(\\lg y\\) vs \\(x\\))",
            ],
        },
    ],
    "formulas": [
        {"label": "Log definition", "expr": "\\(\\log_a x = y \\iff a^y = x\\)"},
        {"label": "Product rule", "expr": "\\(\\log_a(xy) = \\log_a x + \\log_a y\\)"},
        {"label": "Power rule", "expr": "\\(\\log_a(x^n) = n\\log_a x\\)"},
        {"label": "Change of base", "expr": "\\(\\log_a b = \\frac{\\ln b}{\\ln a}\\)"},
        {"label": "Special values", "expr": "\\(\\log_a 1 = 0, \\quad \\log_a a = 1\\)"},
    ],
    "tips": [
        "Always check the domain: \\(\\log\\) is only defined for positive arguments.",
        "When solving, check for extraneous solutions — log equations can introduce invalid roots.",
        "For the linear law, identify Y, X, gradient, and y-intercept carefully before reading values off the graph.",
    ],
}
