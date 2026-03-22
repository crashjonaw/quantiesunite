CHECKS = [
    {
        "q": "For a discrete random variable with PMF p(x) = c·x for x ∈ {1, 2, 3}, find c.",
        "a": "Σₓ p(x) = 1 gives c(1 + 2 + 3) = 1, so 6c = 1, thus c = 1/6.",
        "hint": "The PMF must sum to 1. Use Σₓ₌₁³ c·x = 1."
    },
    {
        "q": "If X ~ Uniform(0, 2), find P(0.5 < X < 1.5).",
        "a": "f(x) = 1/2 for x ∈ [0, 2]. P(0.5 < X < 1.5) = ∫₀.₅^1.5 (1/2) dx = (1/2) · 1 = 0.5.",
        "hint": "For uniform, probability = (interval length) / (distribution width)."
    },
    {
        "q": "X ~ Binomial(5, 0.3). Find P(X = 2).",
        "a": "P(X = 2) = C(5, 2) (0.3)² (0.7)³ = 10 · 0.09 · 0.343 ≈ 0.309.",
        "hint": "Use the binomial formula: P(X=k) = C(n,k) p^k (1-p)^(n-k) where C(n,k) = n!/(k!(n-k)!)."
    },
    {
        "q": "X ~ N(10, 4) (mean 10, variance 4). Find P(X > 12) using the standard normal.",
        "a": "Z = (X - 10)/2 ~ N(0, 1). P(X > 12) = P(Z > 1) ≈ 0.1587.",
        "hint": "Standardize: Z = (X - μ)/σ. Then use standard normal table for P(Z > 1)."
    },
    {
        "q": "X and Y are independent with X ~ N(0, 1), Y ~ N(0, 1). What is the distribution of X + Y?",
        "a": "X + Y ~ N(0 + 0, 1 + 1) = N(0, 2). Sum of independent normals is normal with mean sum of means, variance sum of variances.",
        "hint": "For independent normals, X ~ N(μ₁, σ₁²) and Y ~ N(μ₂, σ₂²), we have X+Y ~ N(μ₁+μ₂, σ₁²+σ₂²)."
    }
]
