MINDMAP = {
    "concepts": [
        {
            "title": "Expectation (Mean)",
            "points": [
                "Discrete: \\(E[X] = \\sum_x x \\cdot p(x)\\)",
                "Continuous: \\(E[X] = \\int_{-\\infty}^{\\infty} x f(x)\\,dx\\)",
                "Linearity: \\(E[aX + bY] = aE[X] + bE[Y]\\) (always, even if dependent)",
            ],
        },
        {
            "title": "Variance & Standard Deviation",
            "points": [
                "\\(\\text{Var}(X) = E[(X - \\mu)^2] = E[X^2] - (E[X])^2\\)",
                "\\(\\text{SD}(X) = \\sqrt{\\text{Var}(X)}\\)",
                "\\(\\text{Var}(aX + b) = a^2 \\text{Var}(X)\\)",
                "If \\(X, Y\\) independent: \\(\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y)\\)",
            ],
        },
        {
            "title": "Covariance & Correlation",
            "points": [
                "\\(\\text{Cov}(X,Y) = E[XY] - E[X]E[Y]\\)",
                "Correlation: \\(\\rho_{XY} = \\frac{\\text{Cov}(X,Y)}{\\text{SD}(X)\\text{SD}(Y)}\\), with \\(-1 \\leq \\rho \\leq 1\\)",
                "\\(\\text{Var}(X+Y) = \\text{Var}(X) + \\text{Var}(Y) + 2\\text{Cov}(X,Y)\\)",
            ],
        },
        {
            "title": "Moments & MGF",
            "points": [
                "\\(k\\)-th moment: \\(E[X^k]\\); \\(k\\)-th central moment: \\(E[(X-\\mu)^k]\\)",
                "Moment generating function: \\(M_X(t) = E[e^{tX}]\\)",
                "\\(E[X^k] = M_X^{(k)}(0)\\) (\\(k\\)-th derivative at \\(t=0\\))",
            ],
        },
        {
            "title": "Key Distribution Parameters",
            "points": [
                "Binomial \\(B(n,p)\\): \\(E[X]=np\\), \\(\\text{Var}(X)=np(1-p)\\)",
                "Poisson \\(\\text{Poi}(\\lambda)\\): \\(E[X]=\\lambda\\), \\(\\text{Var}(X)=\\lambda\\)",
                "Normal \\(N(\\mu,\\sigma^2)\\): \\(E[X]=\\mu\\), \\(\\text{Var}(X)=\\sigma^2\\)",
                "Exponential \\(\\text{Exp}(\\lambda)\\): \\(E[X]=1/\\lambda\\), \\(\\text{Var}(X)=1/\\lambda^2\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Variance Shortcut", "expr": "\\(\\text{Var}(X) = E[X^2] - (E[X])^2\\)"},
        {"label": "Covariance", "expr": "\\(\\text{Cov}(X,Y) = E[XY] - E[X]E[Y]\\)"},
        {"label": "Linearity of E", "expr": "\\(E[aX + bY] = aE[X] + bE[Y]\\)"},
        {"label": "MGF", "expr": "\\(M_X(t) = E[e^{tX}]\\)"},
    ],
    "tips": [
        "Linearity of expectation holds regardless of dependence -- this is extremely powerful.",
        "Use the shortcut formula \\(E[X^2] - (E[X])^2\\) for variance; it is usually easier than the definition.",
        "Variance is always non-negative; if you get a negative value, recheck your calculations.",
    ],
}
