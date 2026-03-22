QUIZ = [
    {
        "question": "Explain why Type I error is often considered more serious than Type II error, and vice versa, depending on context.",
        "answer": "Type I (false positive): rejects H₀ incorrectly, causing false claims. Type II (false negative): misses a true effect. Context determines severity: drug safety vs. effectiveness, legal vs. medical decisions, etc.",
        "explanation": "Example 1: Drug testing. Type I (approving a bad drug) is dangerous. Type II (missing a good drug) is unfortunate but less critical. Example 2: Quality control. Type II (passing defective products) is costly. Example 3: Disease screening. Type II (missing disease cases) affects patient care. The choice of α should reflect the real-world consequences."
    },
    {
        "question": "A sample of 100 people has mean salary X̄ = $50,000 with σ = $8,000. Construct a 95% CI for μ.",
        "answer": "[48,432, 51,568]",
        "explanation": "CI = X̄ ± z₀.₀₂₅ × (σ/√n) = 50000 ± 1.96 × (8000/10) = 50000 ± 1.96 × 800 = 50000 ± 1568 = [48432, 51568]."
    },
    {
        "question": "A researcher tests H₀: μ = 10 vs H₁: μ ≠ 10. The p-value is 0.15. Interpret this result.",
        "answer": "If H₀ is true (μ = 10), there's a 15% chance of observing data as extreme as what was collected. This is not statistically significant at typical levels (α = 0.05 or 0.01), so we fail to reject H₀.",
        "explanation": "P-value = 0.15 means the observed data is not unusual under H₀. Since 0.15 > 0.05, we don't have sufficient evidence to conclude μ ≠ 10. The difference observed (if any) could easily be due to sampling variability."
    },
    {
        "question": "A medical test has a true positive rate of 90% and false positive rate of 5%. If 1% of the population has the disease, what's the probability someone testing positive actually has the disease? (Bayesian approach)",
        "answer": "Approximately 15.4% (using Bayes' theorem)",
        "explanation": "P(disease | positive) = P(positive | disease) × P(disease) / P(positive) = 0.9 × 0.01 / [0.9 × 0.01 + 0.05 × 0.99] = 0.009 / (0.009 + 0.0495) ≈ 0.154. This shows that despite a positive test, the probability of actually having the disease is low when the disease is rare."
    },
    {
        "question": "Compare the margin of error for 90%, 95%, and 99% confidence levels with the same sample size.",
        "answer": "As confidence level increases, margin of error increases: 90% (z=1.645) < 95% (z=1.96) < 99% (z=2.576)",
        "explanation": "Higher confidence requires a wider interval to be more certain the true parameter is captured. The critical values increase with confidence level. This is a trade-off: higher confidence = wider CI = less precise estimate."
    }
]
