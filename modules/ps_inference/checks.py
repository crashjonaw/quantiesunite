CHECKS = [
    {
        "q": "For X₁,...,X₅ = {2, 4, 3, 5, 6}, estimate the parameter of Poisson(λ) using MLE.",
        "a": "For Poisson, λ̂_MLE = X̄ = (2+4+3+5+6)/5 = 20/5 = 4",
        "hint": "The MLE for Poisson λ is the sample mean."
    },
    {
        "q": "Explain the difference between p-value and Type I error rate.",
        "a": "p-value is the observed tail probability for a specific dataset. Type I error rate α is the preset threshold for rejection (e.g., 0.05). If p < α, reject H₀.",
        "hint": "p-value is data-dependent; α is predetermined."
    },
    {
        "q": "For testing H₀: μ = 0 vs H₁: μ ≠ 0, n=100, X̄=0.5, S=2. Compute the test statistic t.",
        "a": "t = (0.5 - 0) / (2 / √100) = 0.5 / 0.2 = 2.5",
        "hint": "t = (X̄ - μ₀) / (S / √n) where S is sample standard deviation."
    },
    {
        "q": "What does the power of a test measure?",
        "a": "Power = P(reject H₀ | H₁ true) = 1 - β. It's the probability of correctly detecting an effect if it exists.",
        "hint": "Power measures sensitivity; higher power is better. Depends on effect size, sample size, and α."
    },
    {
        "q": "In linear regression, what does R² measure?",
        "a": "R² = proportion of variance in y explained by x. Ranges from 0 to 1, with higher values indicating better fit.",
        "hint": "R² = 1 - (SS_residual / SS_total). It's a measure of goodness-of-fit."
    }
]
