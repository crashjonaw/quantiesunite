MINDMAP = {
    "concepts": [
        {"title": "Bayes' Theorem", "points": [
            "\\(P(\\theta | D) = \\frac{P(D | \\theta) P(\\theta)}{P(D)}\\)",
            "Posterior is proportional to likelihood times prior",
            "Updates belief about \\(\\theta\\) after observing data \\(D\\)",
        ]},
        {"title": "Prior, Likelihood, Posterior", "points": [
            "Prior \\(P(\\theta)\\): what we believe before seeing data",
            "Likelihood \\(P(D|\\theta)\\): probability of data given parameter",
            "Posterior \\(P(\\theta|D)\\): updated belief after data",
            "Evidence \\(P(D)\\): normalising constant",
        ]},
        {"title": "Conjugate Priors", "points": [
            "Prior and posterior are in the same family",
            "Beta-Binomial, Normal-Normal, Gamma-Poisson",
            "Makes computation tractable without numerical methods",
        ]},
        {"title": "Bayesian vs Frequentist", "points": [
            "Bayesian: parameters are random variables with distributions",
            "Frequentist: parameters are fixed, data is random",
            "Credible interval (Bayesian) vs confidence interval (frequentist)",
        ]},
    ],
    "formulas": [
        {"label": "Bayes' Theorem", "expr": "\\(P(\\theta|D) = \\frac{P(D|\\theta)P(\\theta)}{P(D)}\\)"},
        {"label": "Proportionality", "expr": "\\(P(\\theta|D) \\propto P(D|\\theta) \\cdot P(\\theta)\\)"},
        {"label": "Beta Prior", "expr": "\\(\\theta \\sim \\text{Beta}(\\alpha, \\beta)\\)"},
        {"label": "Beta-Binomial Update", "expr": "\\(\\text{Beta}(\\alpha + k, \\beta + n - k)\\)"},
    ],
    "tips": [
        "The posterior becomes less sensitive to the prior as more data is observed",
        "Conjugate priors simplify maths but aren't always the best modelling choice",
        "MAP (maximum a posteriori) estimate is the mode of the posterior",
    ],
}
