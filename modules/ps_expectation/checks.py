CHECKS = [
    {
        "q": "X ~ Poisson(3). Find E[X] and Var(X).",
        "a": "E[X] = 3, Var(X) = 3. For Poisson(λ): E[X] = λ and Var(X) = λ.",
        "hint": "Poisson distributions have mean and variance equal to the parameter λ."
    },
    {
        "q": "If Y = 2X - 5 and Var(X) = 4, find Var(Y).",
        "a": "Var(Y) = 2² · Var(X) = 4 · 4 = 16. (Constant shift doesn't affect variance; scaling by 2 multiplies variance by 4.)",
        "hint": "Var(aX + b) = a² Var(X). Here a = 2, b = -5."
    },
    {
        "q": "X and Y are independent with E[X] = 2, E[Y] = 3. Find E[XY].",
        "a": "E[XY] = E[X]·E[Y] = 2·3 = 6. (Independence implies E[XY] = E[X]E[Y].)",
        "hint": "For independent RVs, the expectation of the product equals the product of expectations."
    },
    {
        "q": "If X ~ Exponential(λ), what is Var(X)?",
        "a": "E[X] = 1/λ, E[X²] = 2/λ², so Var(X) = 2/λ² - (1/λ)² = 1/λ².",
        "hint": "Var(X) = E[X²] - (E[X])². First compute E[X²] using integration."
    },
    {
        "q": "For X ~ N(0, 1), what is M_X(t)?",
        "a": "M_X(t) = e^(t²/2). For standard normal, the MGF is the exponential of (variance · t²)/2.",
        "hint": "For Normal(μ, σ²): M(t) = exp(μt + σ²t²/2). Here μ = 0, σ² = 1."
    }
]
