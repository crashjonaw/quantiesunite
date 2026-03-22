QUIZ = [
    {
        "question": "For X ~ Poisson(2), find P(X = 3).",
        "answer": "P(X = 3) = (e^(-2) · 2³) / 3! = (e^(-2) · 8) / 6 = 4e^(-2) / 3 ≈ 0.180",
        "explanation": "Use the Poisson formula: P(X=k) = (e^(-λ) · λ^k) / k! with λ = 2, k = 3."
    },
    {
        "question": "If X ~ Exponential(1), what is P(X > 2)?",
        "answer": "P(X > 2) = e^(-1·2) = e^(-2) ≈ 0.135",
        "explanation": "For exponential, P(X > t) = e^(-λt). Uses the memoryless property."
    },
    {
        "question": "True or False: If X and Y are independent, then Cov(X, Y) = 0.",
        "answer": "True",
        "explanation": "Independence implies zero covariance (they're uncorrelated). Converse is not always true."
    },
    {
        "question": "X ~ N(5, 9) (mean 5, variance 9). What is P(X < 2)?",
        "answer": "σ = 3, Z = (2-5)/3 = -1. P(X < 2) = P(Z < -1) ≈ 0.1587",
        "explanation": "Standardize to get a standard normal, then use tables or symmetry (P(Z < -1) = P(Z > 1))."
    },
    {
        "question": "If Y = 2X + 3 and X ~ Uniform(0, 1), what is the distribution of Y?",
        "answer": "Y ~ Uniform(3, 5) (linear transformation shifts and scales the uniform distribution)",
        "explanation": "Linear transformations of uniform variables are uniform on the transformed interval: [2·0+3, 2·1+3] = [3, 5]."
    }
]
