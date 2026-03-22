SECTIONS = [
    {
        "title": "Bayes' Theorem and the Bayesian Framework",
        "body": """
        <p><strong>Bayes' Theorem:</strong> For events A and B:</p>
        <pre class='code-block'>P(A|B) = P(B|A)P(A) / P(B)</pre>

        <p><strong>In the context of statistics:</strong> For parameter θ and data y:</p>
        <pre class='code-block'>Posterior = (Likelihood × Prior) / Evidence
p(θ|y) = p(y|θ) p(θ) / p(y)

where p(y) = ∫ p(y|θ) p(θ) dθ (marginalizes over θ)</pre>

        <p><strong>Components:</strong></p>
        <ul>
        <li><strong>Prior p(θ):</strong> Beliefs about θ before seeing data</li>
        <li><strong>Likelihood p(y|θ):</strong> Data model; how likely the data is given θ</li>
        <li><strong>Posterior p(θ|y):</strong> Updated beliefs after observing data</li>
        <li><strong>Evidence p(y):</strong> Normalizing constant (marginal likelihood)</li>
        </ul>

        <p><strong>Bayesian interpretation:</strong> The posterior combines prior knowledge with data. As more data arrives, posterior concentrates around the true value.</p>

        <p><strong>Contrast with frequentist:</strong> Frequentists treat θ as fixed (unknown constant); Bayesians treat θ as random (with a distribution). This philosophical difference leads to different inference methods.</p>

        <div class='example-box'>
        <p><strong>Example: Bernoulli with Beta prior</strong></p>
        <pre class='code-block'>Likelihood: X₁,...,Xₙ ~ Bernoulli(p)
Prior: p ~ Beta(α, β) (captures prior belief about p)
Posterior: p|data ~ Beta(α + k, β + n - k)  (k = number of successes)

If α = β = 1 (uniform prior), posterior ~ Beta(1 + k, 1 + n - k)
As n → ∞, posterior concentrates at p̂ = k/n (MLE)</pre>
        </div>

        <p><strong>Conjugate priors:</strong> Priors where the posterior has the same form as the prior. Examples: Beta for Bernoulli, Normal for Normal, Gamma for Poisson. Conjugacy makes computation tractable.</p>
        """
    },
    {
        "title": "Prior Selection and Posterior Analysis",
        "body": """
        <p><strong>Choosing a prior:</strong></p>

        <ul>
        <li><strong>Uninformative/Flat prior:</strong> p(θ) ∝ constant. Represents lack of prior knowledge (problematic for some parameters; improper priors can cause issues).</li>
        <li><strong>Conjugate prior:</strong> Chosen for computational convenience. Prior and posterior are in the same family.</li>
        <li><strong>Weakly informative prior:</strong> Incorporates mild constraints (e.g., positive variance) without strongly biasing toward specific values.</li>
        <li><strong>Expert prior:</strong> Encodes domain knowledge from subject matter experts.</li>
        </ul>

        <p><strong>Prior sensitivity:</strong> How much does the posterior depend on the prior? Robust Bayesian analysis checks sensitivity across plausible priors.</p>

        <p><strong>Posterior inference:</strong></p>
        <ul>
        <li><strong>Point estimate:</strong> Mean E[θ|y], median, or mode of posterior</li>
        <li><strong>Credible interval:</strong> Range [a, b] such that P(a < θ < b | y) = 0.95 (Bayesian analogue of CI)</li>
        <li><strong>Posterior predictive:</strong> Distribution of future data y_new: p(y_new|y) = ∫ p(y_new|θ) p(θ|y) dθ</li>
        </ul>

        <p><strong>Example calculation:</strong> For Beta-Bernoulli with 10 successes in 20 trials and Beta(1,1) prior:</p>
        <pre class='code-block'>Posterior: Beta(11, 11)
Posterior mean: E[p|y] = 11/22 = 0.5
Posterior SD: √(11·11 / (22²·23)) ≈ 0.105
95% credible interval: (0.29, 0.71)  (from Beta quantiles)</pre>

        <p><strong>Model comparison (Bayes Factor):</strong> Compare two models via their marginal likelihoods:</p>
        <pre class='code-block'>BF_{M1 vs M2} = p(y|M1) / p(y|M2)</pre>

        <p>BF > 10 strongly favors M1, BF < 0.1 strongly favors M2.</p>
        """
    },
    {
        "title": "Computational Methods: MCMC and Approximations",
        "body": """
        <p><strong>Computational challenge:</strong> Computing the posterior p(θ|y) requires integrating over high-dimensional θ space (the evidence p(y) is intractable for many models).</p>

        <p><strong>Markov Chain Monte Carlo (MCMC):</strong> Simulate draws from the posterior without computing p(y) explicitly:</p>
        <ul>
        <li><strong>Metropolis-Hastings:</strong> Propose a new θ, accept with probability α = min(1, [p(y|θ_new)p(θ_new)] / [p(y|θ_old)p(θ_old)])</li>
        <li><strong>Gibbs Sampling:</strong> Iteratively sample each parameter from its conditional posterior given others</li>
        <li><strong>Hamiltonian MC:</strong> Uses gradient information for more efficient sampling (e.g., in Stan, PyMC)</li>
        </ul>

        <p><strong>MCMC diagnostics:</strong></p>
        <ul>
        <li>Trace plots: Visual check of chain mixing</li>
        <li>Effective sample size: Account for autocorrelation in chains</li>
        <li>Gelman-Rubin R̂: Compare multiple chains; R̂ ≈ 1 indicates convergence</li>
        </ul>

        <p><strong>Approximate inference:</strong></p>
        <ul>
        <li><strong>Variational Inference:</strong> Approximate posterior with a simple distribution (e.g., normal) by minimizing KL divergence</li>
        <li><strong>Expectation Propagation:</strong> Iteratively refine approximations to the posterior</li>
        <li><strong>Laplace approximation:</strong> Approximate posterior as normal around the mode (useful for asymptotic inference)</li>
        </ul>

        <p><strong>Computational tools:</strong> Modern software (Stan, PyMC, JAGS) automate MCMC and variational inference, making Bayesian analysis practical for complex models.</p>

        <div class='example-box'>
        <p><strong>Example: Metropolis-Hastings for Bernoulli</strong></p>
        <pre class='code-block'>Algorithm:
1. Start with p₀
2. For t = 1 to T:
   - Propose p_new ~ N(p_old, σ²)
   - Compute α = min(1, [p(y|p_new)p(p_new)] / [p(y|p_old)p(p_old)])
   - Accept p_new with probability α; else keep p_old
   - Store p_t

After burnin period, {p_t} are samples from posterior.
Estimate E[p|y] ≈ mean of samples</pre>
        </div>
        """
    },
    {
        "title": "Bayesian vs. Frequentist Comparison and Applications",
        "body": """
        <p><strong>Key differences:</strong></p>

        <table border='1'>
        <tr><th>Aspect</th><th>Frequentist</th><th>Bayesian</th></tr>
        <tr><td>Parameter θ</td><td>Fixed (unknown) constant</td><td>Random variable</td></tr>
        <tr><td>Probability</td><td>Limiting frequency</td><td>Degree of belief</td></tr>
        <tr><td>CI/Credible interval</td><td>P(CI covers θ) = 95% over repeated sampling</td><td>P(θ ∈ interval | data) = 95%</td></tr>
        <tr><td>p-value</td><td>P(data | H₀ true)</td><td>Not directly used; compare posterior probabilities</td></tr>
        <tr><td>Prior</td><td>None (or pretend uninformative)</td><td>Explicit, reflects prior knowledge</td></tr>
        </table>

        <p><strong>Advantages of Bayesian approach:</strong></p>
        <ul>
        <li>Natural way to incorporate prior information</li>
        <li>Posterior distributions directly answer questions (P(θ > 0 | data))</li>
        <li>Principled handling of missing data and model uncertainty</li>
        <li>Prediction is straightforward (posterior predictive)</li>
        <li>No multiple testing problem (naturally accounts for uncertainty)</li>
        </ul>

        <p><strong>Limitations:</strong></p>
        <ul>
        <li>Computationally intensive (though improving with modern methods)</li>
        <li>Prior choice can be subjective</li>
        <li>Less widely taught/understood historically</li>
        </ul>

        <p><strong>Applications:</strong></p>
        <ul>
        <li><strong>Medical trials:</strong> Incorporate efficacy data as priors for new treatments</li>
        <li><strong>Machine learning:</strong> Neural networks with Bayesian uncertainty quantification</li>
        <li><strong>Finance:</strong> Update belief about asset returns as new data arrives</li>
        <li><strong>Hierarchical models:</strong> Naturally share information across groups</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Bayesian vs. Frequentist inference for μ</strong></p>
        <pre class='code-block'>Data: n = 20, X̄ = 5.2, S = 1 (small sample)

Frequentist 95% CI: 5.2 ± t₀.₀₂₅,₁₉ · (1/√20) ≈ 5.2 ± 0.47 = (4.73, 5.67)
Interpretation: If we repeated the sampling infinitely, 95% of such intervals contain μ.

Bayesian with N(5, 1) prior: 
Posterior ≈ N(5.16, 0.091) (weighted average of prior and data)
95% credible interval: (4.60, 5.72)
Interpretation: Given the data (and prior), there's 95% probability that μ ∈ (4.60, 5.72).</pre>
        </div>

        <p><strong>Modern consensus:</strong> Both approaches are valid; choice depends on context. Bayesian for forward-looking prediction and incorporating knowledge; frequentist for hypothesis testing and large-sample asymptotic theory. Many modern methods (regularization, empirical Bayes) blend both perspectives.</p>
        """
    }
]
