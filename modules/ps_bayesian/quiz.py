QUIZ = [
    {
        "question": "Explain the difference between the prior, likelihood, and posterior in Bayesian inference.",
        "answer": "Prior: initial belief about θ before data. Likelihood: data model p(y|θ). Posterior: updated belief p(θ|y) = p(y|θ)p(θ)/p(y).",
        "explanation": "Bayes' theorem combines these three components to produce the posterior, which is the basis for inference."
    },
    {
        "question": "True or False: The posterior is independent of the prior as the sample size increases.",
        "answer": "True (approximately). With large n, the likelihood dominates the prior, so posterior ≈ normal around the MLE.",
        "explanation": "This is called 'consistency': as data accumulates, Bayesian and frequentist inference agree."
    },
    {
        "question": "For Beta-Bernoulli with 20 successes in 30 trials and Beta(1,1) prior, what is the posterior distribution?",
        "answer": "Beta(1 + 20, 1 + 10) = Beta(21, 11)",
        "explanation": "Conjugate prior rule: Beta(α, β) with k successes and n-k failures gives Beta(α+k, β+n-k)."
    },
    {
        "question": "What is the posterior predictive distribution and why is it useful?",
        "answer": "p(y_new|y) = ∫ p(y_new|θ) p(θ|y) dθ. It predicts future observations, accounting for posterior uncertainty about θ.",
        "explanation": "This integrates out parameter uncertainty, giving a probabilistic prediction for new data."
    },
    {
        "question": "How does MCMC help in Bayesian inference?",
        "answer": "MCMC simulates draws from the posterior without computing the intractable normalizing constant p(y). Samples approximate the posterior distribution.",
        "explanation": "Methods like Metropolis-Hastings enable inference for complex models with high-dimensional parameters."
    }
]
