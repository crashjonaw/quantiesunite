MINDMAP = {
    "concepts": [
        {"title": "Hypothesis Testing Framework", "points": [
            "\\(H_0\\): null hypothesis (status quo), \\(H_1\\): alternative hypothesis",
            "One-tailed (>, <) vs two-tailed (\\(\\neq\\)) tests",
            "Significance level \\(\\alpha\\): typically 5% or 1%",
        ]},
        {"title": "Test for Population Mean", "points": [
            "Known \\(\\sigma\\): use \\(Z = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}\\)",
            "Unknown \\(\\sigma\\), small \\(n\\): use \\(t = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}\\)",
            "Reject \\(H_0\\) if test statistic falls in the critical region",
        ]},
        {"title": "Test for Proportion", "points": [
            "\\(X \\sim B(n, p)\\) under \\(H_0\\)",
            "Find \\(P(X \\leq x)\\) or \\(P(X \\geq x)\\) and compare with \\(\\alpha\\)",
            "For large \\(n\\): use Normal approximation",
        ]},
        {"title": "Errors & p-values", "points": [
            "Type I error: reject \\(H_0\\) when it is true (probability = \\(\\alpha\\))",
            "Type II error: fail to reject \\(H_0\\) when it is false",
            "p-value: smallest \\(\\alpha\\) at which we would reject \\(H_0\\)",
        ]},
    ],
    "formulas": [
        {"label": "Z-test", "expr": "\\(Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}}\\)"},
        {"label": "t-test", "expr": "\\(t = \\frac{\\bar{X} - \\mu_0}{s / \\sqrt{n}}\\)"},
        {"label": "Unbiased Variance", "expr": "\\(s^2 = \\frac{\\sum(x_i - \\bar{x})^2}{n-1}\\)"},
    ],
    "tips": [
        "Always state H₀ and H₁ clearly before computing anything",
        "A non-significant result does NOT prove H₀ — it only fails to reject it",
        "In exams, always state your conclusion in context of the question",
    ],
}
