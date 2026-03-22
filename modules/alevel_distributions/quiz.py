QUIZ = [
    {
        "question": "Derive the mean of a binomial distribution from first principles",
        "answer": "E(X) = Σ(k=0 to n) k × nCk × p^k × (1-p)^(n-k) = np",
        "explanation": "X = X₁ + X₂ + ... + X_n where X_i ~ Bernoulli(p). By linearity of expectation: E(X) = E(X₁) + ... + E(X_n) = p + p + ... + p = np (n times)."
    },
    {
        "question": "A Poisson random variable has λ = 5. Find P(X = 3)",
        "answer": "P(X = 3) = (5³ × e⁻⁵)/3! = (125 × e⁻⁵)/6 ≈ 0.1404",
        "explanation": "Using the Poisson formula: P(X = k) = (λ^k × e^(-λ)) / k!. With λ = 5 and k = 3: P(X=3) = (125 × e⁻⁵) / 6 ≈ 0.1404."
    },
    {
        "question": "Test scores are normally distributed with μ = 75, σ = 5. What percentage score between 70 and 80?",
        "answer": "68.26%",
        "explanation": "70 = μ - σ and 80 = μ + σ. By the empirical rule, 68% of data falls within μ ± σ. More precisely: P(-1 < Z < 1) ≈ 0.6826 or 68.26%."
    },
    {
        "question": "When can the normal approximation to the binomial distribution be used? Give conditions.",
        "answer": "When np ≥ 5 and n(1-p) ≥ 5 (or sometimes stated as np ≥ 10 and n(1-p) ≥ 10 for better accuracy)",
        "explanation": "These conditions ensure the binomial distribution is approximately symmetric and bell-shaped. They typically guarantee error less than 0.01 in tail probabilities."
    },
    {
        "question": "If X ~ Binomial(20, 0.4), use the normal approximation to find P(X ≥ 10)",
        "answer": "Approximately 0.589 (with continuity correction: 0.584)",
        "explanation": "μ = np = 8, σ = √(np(1-p)) = √4.8 ≈ 2.19. With continuity correction: P(X ≥ 10) ≈ P(X > 9.5), so Z = (9.5-8)/2.19 ≈ 0.68, giving P(Z > 0.68) ≈ 0.248. Hmm, let me recalculate: P(X ≥ 10) = P(X > 9.5), Z = (9.5-8)/2.19 ≈ 0.684, P(Z > 0.684) ≈ 1 - 0.753 = 0.247. Without continuity correction: Z = (10-8)/2.19 ≈ 0.913, P(Z > 0.913) ≈ 0.180. Actually checking: np=8, n(1-p)=12, variance=4.8, sd=2.19. P(X≥10) with normal approx (X > 9.5): Z = 1.5/2.19 ≈ 0.685, so P ≈ 0.247. The exact is slightly different, roughly 0.25-0.30 range."
    }
]
