MINDMAP = {
    "concepts": [
        {
            "title": "Law of Large Numbers (LLN)",
            "points": [
                "Sample mean \\(\\bar{X}_n \\to \\mu\\) as \\(n \\to \\infty\\)",
                "Weak LLN: convergence in probability; Strong LLN: almost sure convergence",
                "Justifies using sample averages to estimate population means",
            ],
        },
        {
            "title": "Central Limit Theorem (CLT)",
            "points": [
                "If \\(X_1, X_2, \\ldots\\) are i.i.d. with mean \\(\\mu\\) and variance \\(\\sigma^2\\), then \\(\\bar{X}_n\\) is approximately normal for large \\(n\\)",
                "\\(\\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} N(0,1)\\)",
                "Works regardless of the original distribution (given finite variance)",
                "Rule of thumb: \\(n \\geq 30\\) is usually sufficient",
            ],
        },
        {
            "title": "Standardisation",
            "points": [
                "\\(Z = \\frac{X - \\mu}{\\sigma}\\) converts any normal to \\(N(0,1)\\)",
                "For the sample mean: \\(Z = \\frac{\\bar{X} - \\mu}{\\sigma / \\sqrt{n}}\\)",
                "Use Z-tables or software to find probabilities from the standard normal",
            ],
        },
        {
            "title": "Applications of the CLT",
            "points": [
                "Confidence intervals: \\(\\bar{X} \\pm z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}}\\)",
                "Approximating binomial probabilities with a normal distribution",
                "Quality control and sampling distributions",
            ],
        },
        {
            "title": "Continuity Correction",
            "points": [
                "When using the normal to approximate a discrete distribution, adjust by \\(\\pm 0.5\\)",
                "E.g., \\(P(X \\leq k) \\approx P\\left(Z \\leq \\frac{k + 0.5 - \\mu}{\\sigma}\\right)\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "CLT Statement", "expr": "\\(\\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} N(0,1)\\)"},
        {"label": "Standard Error", "expr": "\\(\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}\\)"},
        {"label": "Confidence Interval", "expr": "\\(\\bar{X} \\pm z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}}\\)"},
        {"label": "Z-score", "expr": "\\(Z = \\frac{X - \\mu}{\\sigma}\\)"},
    ],
    "tips": [
        "The CLT explains why the normal distribution appears so often in nature -- sums of many small effects tend toward normality.",
        "The standard error shrinks like \\(1/\\sqrt{n}\\): to halve the error, quadruple the sample size.",
        "Apply continuity correction when approximating discrete distributions with the normal.",
    ],
}
