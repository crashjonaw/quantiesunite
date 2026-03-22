CHECKS = [
    {
        "q": "State Bayes' Theorem in terms of θ (parameter) and y (data).",
        "a": "p(θ|y) = p(y|θ)p(θ) / p(y), where p(y) = ∫ p(y|θ)p(θ) dθ.",
        "hint": "Posterior = (Likelihood × Prior) / Evidence. The evidence normalizes the posterior."
    },
    {
        "q": "For Bernoulli with Beta(2, 2) prior and data: 3 successes in 5 trials, find the posterior.",
        "a": "Posterior = Beta(2 + 3, 2 + 5 - 3) = Beta(5, 4).",
        "hint": "For Bernoulli-Beta conjugate: posterior Beta(α + k, β + n - k) where k = successes."
    },
    {
        "q": "What is a conjugate prior? Give one example.",
        "a": "A prior where the posterior has the same distribution family as the prior. Example: Beta is conjugate for Bernoulli.",
        "hint": "Conjugacy simplifies computation; posterior can be computed in closed form."
    },
    {
        "q": "How does the Bayesian credible interval differ from a frequentist confidence interval?",
        "a": "Credible interval: P(θ ∈ interval | data) = 95% (direct probability about θ). CI: P(interval covers θ) = 95% over repeated sampling.",
        "hint": "Bayesian intervals have a direct probability interpretation; frequentist intervals are about sampling properties."
    },
    {
        "q": "What is the Bayes Factor and what does BF > 10 indicate?",
        "a": "BF = p(y|M1)/p(y|M2) is the likelihood ratio of two models. BF > 10 indicates strong evidence for M1 over M2.",
        "hint": "Bayes Factor combines model fit and complexity; larger BF favors the first model."
    }
]
