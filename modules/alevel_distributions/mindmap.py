MINDMAP = {
    "concepts": [
        {"title": "Binomial Distribution", "points": [
            "\\(X \\sim B(n, p)\\): \\(n\\) independent trials, probability \\(p\\) each",
            "\\(P(X=k) = \\binom{n}{k}p^k(1-p)^{n-k}\\)",
            "\\(E(X) = np\\), \\(\\text{Var}(X) = np(1-p)\\)",
        ]},
        {"title": "Poisson Distribution", "points": [
            "\\(X \\sim \\text{Po}(\\lambda)\\): events in fixed interval, mean \\(\\lambda\\)",
            "\\(P(X=k) = \\frac{e^{-\\lambda}\\lambda^k}{k!}\\)",
            "\\(E(X) = \\text{Var}(X) = \\lambda\\)",
            "Poisson approximation to Binomial when \\(n\\) large, \\(p\\) small",
        ]},
        {"title": "Normal Distribution", "points": [
            "\\(X \\sim N(\\mu, \\sigma^2)\\): bell-shaped, symmetric about \\(\\mu\\)",
            "Standardise: \\(Z = \\frac{X - \\mu}{\\sigma}\\), then \\(Z \\sim N(0,1)\\)",
            "68-95-99.7 rule for 1, 2, 3 standard deviations",
        ]},
        {"title": "Normal Approximations", "points": [
            "\\(B(n,p) \\approx N(np, np(1-p))\\) when \\(np > 5\\) and \\(nq > 5\\)",
            "\\(\\text{Po}(\\lambda) \\approx N(\\lambda, \\lambda)\\) when \\(\\lambda > 10\\)",
            "Apply continuity correction: \\(P(X \\leq k) \\approx P(Y \\leq k + 0.5)\\)",
        ]},
    ],
    "formulas": [
        {"label": "Binomial PMF", "expr": "\\(P(X=k) = \\binom{n}{k}p^k q^{n-k}\\)"},
        {"label": "Poisson PMF", "expr": "\\(P(X=k) = \\frac{e^{-\\lambda}\\lambda^k}{k!}\\)"},
        {"label": "Standardise", "expr": "\\(Z = \\frac{X - \\mu}{\\sigma}\\)"},
        {"label": "E(aX+b)", "expr": "\\(E(aX+b) = aE(X)+b\\)"},
        {"label": "Var(aX+b)", "expr": "\\(\\text{Var}(aX+b) = a^2\\text{Var}(X)\\)"},
    ],
    "tips": [
        "Check conditions before using an approximation — state them in exams",
        "Continuity correction: discrete to continuous, adjust by 0.5",
        "If Var(X) is close to E(X), consider Poisson; if not, consider Binomial",
    ],
}
