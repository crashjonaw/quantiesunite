QUIZ = [
    {
        "question": "State the Central Limit Theorem: What distribution does the sample mean approach?",
        "answer": "For i.i.d. X₁, ..., Xₙ with mean μ and variance σ², the sample mean X̄ₙ ≈ N(μ, σ²/n) for large n.",
        "explanation": "The CLT says X̄ₙ is approximately normal, regardless of the original distribution shape."
    },
    {
        "question": "True or False: To reduce CI width by half, you need to quadruple the sample size.",
        "answer": "True. Since margin of error ∝ 1/√n, to halve E you need to increase n by a factor of 4.",
        "explanation": "E = z · σ / √n, so 4n gives √(4n) = 2√n, making E half as large."
    },
    {
        "question": "Find the 99% confidence interval for μ given n = 64, X̄ = 30, σ = 8.",
        "answer": "CI = 30 ± 2.576 · (8/√64) = 30 ± 2.576 · 1 = 30 ± 2.576 = (27.424, 32.576)",
        "explanation": "For 99% confidence, z_{0.005} ≈ 2.576. Margin of error = 2.576."
    },
    {
        "question": "What conditions must hold for the CLT to apply?",
        "answer": "Observations must be i.i.d. (independent and identically distributed) with finite mean μ and variance σ².",
        "explanation": "These are the core requirements. Heavy-tailed distributions (infinite variance) violate CLT."
    },
    {
        "question": "If population is highly skewed, what's the effect on CLT convergence?",
        "answer": "Convergence is slower; a larger sample size is needed for X̄ to be approximately normal.",
        "explanation": "Skewed distributions have slower convergence rate than symmetric ones; the Berry-Esseen theorem quantifies this."
    }
]
