MINDMAP = {
    "concepts": [
        {
            "title": "Point Estimation",
            "points": [
                "An estimator \\(\\hat{\\theta}\\) is a statistic used to estimate a parameter \\(\\theta\\)",
                "Desirable properties: unbiased (\\(E[\\hat{\\theta}] = \\theta\\)), consistent, efficient",
                "Methods: method of moments, maximum likelihood estimation (MLE)",
            ],
        },
        {
            "title": "Maximum Likelihood Estimation",
            "points": [
                "Likelihood function: \\(L(\\theta) = \\prod_{i=1}^n f(x_i | \\theta)\\)",
                "MLE: \\(\\hat{\\theta}_{\\text{MLE}} = \\arg\\max_\\theta L(\\theta)\\)",
                "Often easier to maximise \\(\\ell(\\theta) = \\ln L(\\theta)\\)",
            ],
        },
        {
            "title": "Confidence Intervals",
            "points": [
                "A \\(100(1-\\alpha)\\%\\) CI contains the true parameter with probability \\(1-\\alpha\\) (frequentist interpretation)",
                "For mean (known \\(\\sigma\\)): \\(\\bar{X} \\pm z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}}\\)",
                "For mean (unknown \\(\\sigma\\)): \\(\\bar{X} \\pm t_{\\alpha/2, n-1} \\frac{s}{\\sqrt{n}}\\)",
            ],
        },
        {
            "title": "Hypothesis Testing",
            "points": [
                "Null hypothesis \\(H_0\\) vs alternative \\(H_1\\)",
                "Test statistic, rejection region, significance level \\(\\alpha\\)",
                "Type I error (reject true \\(H_0\\)): probability = \\(\\alpha\\)",
                "Type II error (fail to reject false \\(H_0\\)): probability = \\(\\beta\\); Power = \\(1 - \\beta\\)",
            ],
        },
        {
            "title": "p-Values",
            "points": [
                "The probability of observing data as extreme (or more) than what was seen, assuming \\(H_0\\) is true",
                "Reject \\(H_0\\) if p-value \\(< \\alpha\\)",
                "A small p-value indicates strong evidence against \\(H_0\\)",
            ],
        },
        {
            "title": "Common Tests",
            "points": [
                "Z-test (known \\(\\sigma\\)), t-test (unknown \\(\\sigma\\)), chi-squared test (variance, goodness of fit)",
                "Two-sample t-test for comparing two means",
            ],
        },
    ],
    "formulas": [
        {"label": "Z-test Statistic", "expr": "\\(Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}}\\)"},
        {"label": "t-test Statistic", "expr": "\\(t = \\frac{\\bar{X} - \\mu_0}{s / \\sqrt{n}}\\)"},
        {"label": "CI (unknown sigma)", "expr": "\\(\\bar{X} \\pm t_{\\alpha/2,\\, n-1} \\frac{s}{\\sqrt{n}}\\)"},
        {"label": "Log-Likelihood", "expr": "\\(\\ell(\\theta) = \\sum_{i=1}^n \\ln f(x_i | \\theta)\\)"},
    ],
    "tips": [
        "Failing to reject \\(H_0\\) does not mean \\(H_0\\) is true -- it means there is insufficient evidence against it.",
        "Use the t-distribution instead of Z when the population standard deviation is unknown and \\(n\\) is small.",
        "Increasing sample size reduces both Type I and Type II error rates and tightens confidence intervals.",
    ],
}
