MINDMAP = {
    "concepts": [
        {
            "title": "Random Variables",
            "points": [
                "A function \\(X: \\Omega \\to \\mathbb{R}\\) assigning a number to each outcome",
                "Discrete: countable set of values; Continuous: uncountable (interval) of values",
            ],
        },
        {
            "title": "Discrete Distributions",
            "points": [
                "PMF: \\(p(x) = P(X = x)\\), with \\(\\sum_x p(x) = 1\\)",
                "CDF: \\(F(x) = P(X \\leq x) = \\sum_{t \\leq x} p(t)\\)",
                "Key distributions: Bernoulli, Binomial \\(B(n,p)\\), Poisson \\(\\text{Poi}(\\lambda)\\), Geometric",
            ],
        },
        {
            "title": "Continuous Distributions",
            "points": [
                "PDF: \\(f(x) \\geq 0\\) with \\(\\int_{-\\infty}^{\\infty} f(x)\\,dx = 1\\)",
                "\\(P(a \\leq X \\leq b) = \\int_a^b f(x)\\,dx\\)",
                "CDF: \\(F(x) = \\int_{-\\infty}^{x} f(t)\\,dt\\); \\(f(x) = F'(x)\\)",
                "Key distributions: Uniform \\(U(a,b)\\), Exponential \\(\\text{Exp}(\\lambda)\\), Normal \\(N(\\mu, \\sigma^2)\\)",
            ],
        },
        {
            "title": "Common Distribution Formulas",
            "points": [
                "Binomial: \\(P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k}\\)",
                "Poisson: \\(P(X=k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}\\)",
                "Normal PDF: \\(f(x) = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-(x-\\mu)^2/(2\\sigma^2)}\\)",
            ],
        },
        {
            "title": "Joint & Marginal Distributions",
            "points": [
                "Joint PMF/PDF describes two or more random variables together",
                "Marginal: sum (or integrate) over the other variable(s)",
                "Independence: \\(f_{X,Y}(x,y) = f_X(x) f_Y(y)\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Binomial PMF", "expr": "\\(P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k}\\)"},
        {"label": "Poisson PMF", "expr": "\\(P(X=k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}\\)"},
        {"label": "Normal PDF", "expr": "\\(f(x) = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-(x-\\mu)^2/(2\\sigma^2)}\\)"},
        {"label": "CDF from PDF", "expr": "\\(F(x) = \\int_{-\\infty}^{x} f(t)\\,dt\\)"},
    ],
    "tips": [
        "For a continuous variable, \\(P(X = a) = 0\\); probabilities are found over intervals.",
        "The Poisson distribution approximates the Binomial when \\(n\\) is large and \\(p\\) is small (\\(\\lambda = np\\)).",
        "Always verify that your PMF sums to 1 (or PDF integrates to 1) as a sanity check.",
    ],
}
