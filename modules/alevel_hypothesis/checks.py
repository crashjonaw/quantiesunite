CHECKS = [
    {
        "q": "State the null and alternative hypotheses for testing if a coin is fair (p = 0.5)",
        "a": "H₀: p = 0.5; H₁: p ≠ 0.5 (two-tailed)",
        "hint": "The null assumes the default (fairness). The alternative tests whether the coin is biased."
    },
    {
        "q": "In a Z-test, you get Z = 2.3 for a two-tailed test at α = 0.05. Reject or fail to reject H₀?",
        "a": "Reject H₀ (critical values are ±1.96)",
        "hint": "For two-tailed α = 0.05, critical values are ±1.96. Since |2.3| > 1.96, reject H₀."
    },
    {
        "q": "What is the difference between Type I and Type II error?",
        "a": "Type I: rejecting H₀ when true (false positive, prob α). Type II: failing to reject H₀ when false (false negative, prob β)",
        "hint": "Remember: Type I = false alarm, Type II = missed detection."
    },
    {
        "q": "If p-value = 0.032, and α = 0.05, what conclusion do you draw?",
        "a": "Reject H₀. The data provides sufficient evidence against H₀ at the 0.05 significance level.",
        "hint": "Since 0.032 < 0.05, the evidence is strong enough to reject the null hypothesis."
    },
    {
        "q": "Construct a 95% confidence interval for μ with X̄ = 50, σ = 8, n = 64",
        "a": "[48.04, 51.96]",
        "hint": "CI = X̄ ± z₀.₀₂₅ × (σ/√n) = 50 ± 1.96 × (8/8) = 50 ± 1.96"
    }
]
