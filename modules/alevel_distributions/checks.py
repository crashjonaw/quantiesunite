CHECKS = [
    {
        "q": "If X ~ Binomial(10, 0.3), find P(X = 2)",
        "a": "0.2335 (or 45 × 0.3² × 0.7⁸)",
        "hint": "P(X=2) = 10C2 × 0.3² × 0.7⁸ = 45 × 0.09 × 0.0576 ≈ 0.2335"
    },
    {
        "q": "For a Poisson distribution with λ = 4, find E(X) and Var(X)",
        "a": "E(X) = 4, Var(X) = 4",
        "hint": "For Poisson(λ), both the mean and variance equal λ."
    },
    {
        "q": "If X ~ N(100, 15²), find the probability that X > 115",
        "a": "0.1587 (or approximately 15.87%)",
        "hint": "Z = (115 - 100)/15 = 1. P(Z > 1) = 1 - 0.8413 ≈ 0.1587."
    },
    {
        "q": "Explain when to use Poisson approximation to Binomial",
        "a": "When n is large and p is small, with λ = np moderate",
        "hint": "Typical rule: n ≥ 20 and p ≤ 0.05, or n ≥ 100 and p ≤ 0.10"
    },
    {
        "q": "A normal distribution has μ = 50, σ = 8. Find the 75th percentile",
        "a": "Approximately 55.4",
        "hint": "From Z-tables, the 75th percentile has Z ≈ 0.67. X = 50 + 0.67(8) ≈ 55.36"
    }
]
