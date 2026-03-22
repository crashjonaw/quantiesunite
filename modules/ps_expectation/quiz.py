QUIZ = [
    {
        "question": "X ~ Binomial(n=20, p=0.4). Find E[X] and SD(X).",
        "answer": "E[X] = np = 20·0.4 = 8. Var(X) = np(1-p) = 20·0.4·0.6 = 4.8. SD(X) = √4.8 ≈ 2.19.",
        "explanation": "For binomial, μ = np and σ² = np(1-p)."
    },
    {
        "question": "Cov(X, Y) = 0.5, σ_X = 2, σ_Y = 3. Find the correlation ρ(X,Y).",
        "answer": "ρ(X,Y) = 0.5 / (2·3) = 0.5/6 ≈ 0.083",
        "explanation": "Correlation = Covariance / (product of standard deviations)."
    },
    {
        "question": "If E[X] = 5 and Var(X) = 9, what is E[X²]?",
        "answer": "E[X²] = Var(X) + (E[X])² = 9 + 25 = 34",
        "explanation": "Var(X) = E[X²] - (E[X])², so E[X²] = Var(X) + (E[X])²."
    },
    {
        "question": "True or False: If Cov(X,Y) = 0, then X and Y are independent.",
        "answer": "False",
        "explanation": "Covariance 0 means uncorrelated, but independence is stronger. Uncorrelated does not imply independent (example: X~N(0,1), Y=X²)."
    },
    {
        "question": "X and Y are independent, Var(X) = 4, Var(Y) = 6. Find Var(3X - 2Y).",
        "answer": "Var(3X - 2Y) = 3²·Var(X) + (-2)²·Var(Y) = 9·4 + 4·6 = 36 + 24 = 60",
        "explanation": "For independent RVs: Var(aX + bY) = a²Var(X) + b²Var(Y)."
    }
]
