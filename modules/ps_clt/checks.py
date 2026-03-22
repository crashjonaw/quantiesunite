CHECKS = [
    {
        "q": "For X₁, ..., X₅₀ ~ Uniform(0, 1) i.i.d., what is the approximate distribution of X̄₅₀?",
        "a": "μ = 0.5, σ² = 1/12 ≈ 0.0833. By CLT, X̄₅₀ ≈ N(0.5, 0.0833/50) = N(0.5, 0.001667).",
        "hint": "For Uniform(0,1): E[X] = 0.5, Var(X) = 1/12. Sample mean variance = population variance / n."
    },
    {
        "q": "Calculate the 95% confidence interval for μ given n = 100, X̄ = 25, σ = 5 (known).",
        "a": "CI = 25 ± 1.96 · (5/√100) = 25 ± 1.96 · 0.5 = 25 ± 0.98 = (24.02, 25.98)",
        "hint": "For known σ: CI = X̄ ± z_{α/2} · (σ/√n), where z_{0.025} ≈ 1.96."
    },
    {
        "q": "If you want a 95% CI with margin of error E = 1.5 and σ = 3, what sample size do you need?",
        "a": "n ≥ (1.96 · 3 / 1.5)² = (3.92)² ≈ 15.37, so n ≥ 16.",
        "hint": "Sample size formula: n ≥ (z_{α/2} · σ / E)². Use z_{0.025} = 1.96 for 95% confidence."
    },
    {
        "q": "True or False: The CLT requires that X_i be normally distributed.",
        "a": "False. CLT holds for ANY distribution (with finite mean and variance), not just normal.",
        "hint": "This is the remarkable power of CLT—it doesn't assume normality of the original data."
    },
    {
        "q": "Why does margin of error decrease when sample size increases?",
        "a": "Margin of error E = z_{α/2} · σ / √n is proportional to 1/√n. As n increases, √n increases, so E decreases.",
        "hint": "The relationship is 1/√n, so to halve the margin of error requires 4 times as many observations."
    }
]
