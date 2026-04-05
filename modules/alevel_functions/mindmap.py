MINDMAP = {
    "concepts": [
        {
            "title": "Functions & Mappings",
            "points": [
                "A function maps each input to exactly one output",
                "Domain: set of all valid inputs; Range: set of all outputs",
                "One-to-one (injective): each output has at most one input",
                "Onto (surjective): every element of the codomain is an output",
            ],
        },
        {
            "title": "Composite & Inverse Functions",
            "points": [
                "Composite: \\((f \\circ g)(x) = f(g(x))\\); apply \\(g\\) first, then \\(f\\)",
                "Inverse: \\(f^{-1}\\) exists iff \\(f\\) is one-to-one",
                "\\(f(f^{-1}(x)) = f^{-1}(f(x)) = x\\)",
                "Graph of \\(f^{-1}\\) is the reflection of \\(f\\) in \\(y = x\\)",
                "Domain of \\(f^{-1}\\) = Range of \\(f\\), and vice versa",
            ],
        },
        {
            "title": "Transformations of Graphs",
            "points": [
                "\\(f(x) + a\\): translate up by \\(a\\)",
                "\\(f(x + a)\\): translate left by \\(a\\)",
                "\\(af(x)\\): vertical stretch, factor \\(a\\)",
                "\\(f(ax)\\): horizontal compression, factor \\(\\frac{1}{a}\\)",
                "\\(-f(x)\\): reflect in x-axis; \\(f(-x)\\): reflect in y-axis",
                "\\(|f(x)|\\): reflect negative parts above x-axis",
            ],
        },
        {
            "title": "Asymptotes & Curve Sketching",
            "points": [
                "Vertical asymptote: where denominator = 0",
                "Horizontal asymptote: behaviour as \\(x \\to \\pm\\infty\\)",
                "Oblique asymptote: when degree of numerator = degree of denominator + 1",
                "Find intercepts, stationary points, and asymptotes to sketch",
            ],
        },
        {
            "title": "Modulus Function",
            "points": [
                "\\(|x| = x\\) if \\(x \\geq 0\\); \\(|x| = -x\\) if \\(x < 0\\)",
                "\\(|f(x)| = a \\implies f(x) = a\\) or \\(f(x) = -a\\)",
                "\\(|f(x)| < a \\implies -a < f(x) < a\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Composite", "expr": "\\((f \\circ g)(x) = f(g(x))\\)"},
        {"label": "Inverse condition", "expr": "\\(f(f^{-1}(x)) = x\\)"},
        {"label": "Modulus inequality", "expr": "\\(|f(x)| < a \\iff -a < f(x) < a\\)"},
    ],
    "tips": [
        "To find \\(f^{-1}\\): let \\(y = f(x)\\), swap \\(x\\) and \\(y\\), solve for \\(y\\).",
        "Restrict the domain to make a non-injective function invertible (e.g., \\(x^2\\) with \\(x \\geq 0\\)).",
        "For \\(|f(x)| = |g(x)|\\), square both sides to avoid case analysis.",
    ],
}
