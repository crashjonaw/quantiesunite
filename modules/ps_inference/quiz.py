QUIZ = [
    {
        "question": "What is the log-likelihood for a sample from Bernoulli(p): ℓ(p) with k successes in n trials?",
        "answer": "ℓ(p) = k log(p) + (n-k) log(1-p). Setting dℓ/dp = 0 gives p̂ = k/n.",
        "explanation": "Log-likelihood separates the terms, making optimization easier. The MLE is the sample proportion."
    },
    {
        "question": "In hypothesis testing, what is the relationship between Type I error, Type II error, and power?",
        "answer": "Type I error = α, Type II error = β, Power = 1 - β. We typically fix α (e.g., 0.05) and try to minimize β.",
        "explanation": "These are trade-offs: reducing both α and β simultaneously requires larger sample sizes."
    },
    {
        "question": "True or False: A p-value of 0.03 means there's a 3% chance the null hypothesis is true.",
        "answer": "False. The p-value is the probability of the observed data (or more extreme) given H₀ is true, not P(H₀ true | data).",
        "explanation": "This is a common misinterpretation. The p-value conditions on H₀; Bayesian methods directly estimate P(H₀ | data)."
    },
    {
        "question": "For linear regression, what does the slope coefficient β₁ represent?",
        "answer": "β₁ is the change in y for a one-unit increase in x (holding other variables constant in multiple regression).",
        "explanation": "The slope quantifies the strength and direction of the relationship. Its significance is tested via t-test."
    },
    {
        "question": "Method of Moments vs. MLE: which is more efficient asymptotically?",
        "answer": "MLE is more efficient (lower asymptotic variance). MoM is simpler but often suboptimal.",
        "explanation": "For large samples, MLE achieves the Cramér-Rao lower bound (best possible efficiency)."
    }
]
