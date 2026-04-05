TITLE = "Conjugate Priors and Computational Tractability"

SECTIONS = [
    {
        "title": "What is a Conjugate Prior?",
        "body": """
        <p><strong>Definition:</strong> A prior is conjugate to a likelihood if the posterior has the same functional form as the prior.</p>

        <pre class='code-block'>Prior $p(\\theta) \\in$ Family $\\mathcal{F}$
Likelihood $p(y|\\theta)$
        $\\downarrow$ Bayes' rule
Posterior $p(\\theta|y) \\in$ Family $\\mathcal{F}$  (same family!)</pre>

        <p><strong>Why is this powerful?</strong></p>
        <ul>
        <li><strong>Closed form:</strong> Posterior has explicit formula; no numerical integration needed</li>
        <li><strong>Analytic simplicity:</strong> Update rules are often just addition/subtraction of parameters</li>
        <li><strong>Interpretation:</strong> Prior and posterior are directly comparable</li>
        <li><strong>Sequential updating:</strong> Easy to incorporate new data one observation at a time</li>
        </ul>

        <div class='concept-box'>
        <p><strong>Key insight:</strong> Conjugate priors aren't just computationally convenient—they offer insight into how priors and data combine in Bayesian inference.</p>
        </div>
        """
    },
    {
        "title": "Common Conjugate Pairs",
        "body": """
        <p><strong>Likelihood: Bernoulli, Prior: Beta</strong></p>
        <pre class='code-block'>Data: $X \\sim \\text{Bernoulli}(p)$, $n$ observations, $k$ successes
Prior: $p \\sim \\text{Beta}(\\alpha, \\beta)$
Posterior: $p \\mid \\text{data} \\sim \\text{Beta}(\\alpha + k, \\beta + (n - k))$</pre>

        <p>Update rule: Add successes to first parameter, failures to second. Simple!</p>

        <p><strong>Likelihood: Normal (known $\\sigma^2$), Prior: Normal</strong></p>
        <pre class='code-block'>Data: $y \\sim N(\\mu, \\sigma^2)$, $\\sigma^2$ known
Prior: $\\mu \\sim N(m_0, s_0^2)$
Posterior: $\\mu \\mid \\text{data} \\sim N(\\mu_1, s_1^2)$

where $\\mu_1$ and $s_1^2$ are weighted averages of prior and data estimates.</pre>

        <p><strong>Likelihood: Poisson, Prior: Gamma</strong></p>
        <pre class='code-block'>Data: $X \\sim \\text{Poisson}(\\lambda)$, observed sum $S = \\sum x_i$
Prior: $\\lambda \\sim \\text{Gamma}(\\alpha, \\beta)$
Posterior: $\\lambda \\mid \\text{data} \\sim \\text{Gamma}(\\alpha + S, \\beta + n)$</pre>

        <p><strong>Likelihood: Normal (known $\\mu$), Prior: Inverse Gamma</strong></p>
        <pre class='code-block'>Data: $y \\sim N(\\mu, \\sigma^2)$, $\\mu$ known, $\\sigma^2$ unknown
Prior: $\\sigma^2 \\sim \\text{Inverse-Gamma}(\\alpha, \\beta)$
Posterior: $\\sigma^2 \\mid \\text{data} \\sim \\text{Inverse-Gamma}(\\alpha + n/2, \\beta + \\sum(y_i - \\mu)^2/2)$</pre>

        <div class='worked-example'>
        <p><strong>Detailed Example: Beta-Bernoulli</strong></p>
        <p>Flip a coin 15 times, observe 9 heads, 6 tails.</p>

        <p><strong>Prior:</strong> $\\text{Beta}(1, 1)$ — uniform, "no prior knowledge"</p>

        <p><strong>Posterior:</strong> $\\text{Beta}(1 + 9, 1 + 6) = \\text{Beta}(10, 7)$</p>

        <pre class='code-block'>Posterior mean: $10/(10+7) = 10/17 \\approx 0.588$
Posterior mode: $(10-1)/(10+7-2) = 9/15 = 0.6$
Posterior SD: $\\sqrt{10 \\cdot 7 / (17^2 \\cdot 18)} \\approx 0.116$</pre>

        <p>Without conjugacy, we'd need numerical integration to compute these. With conjugacy, it's arithmetic.</p>
        </div>

        <div class='warning-box'>
        <p><strong>Limitation:</strong> Conjugacy is a computational convenience, not a requirement. For complex models, we use MCMC or variational inference, which don't require conjugacy. Conjugate priors are most useful when analytical simplicity matters (teaching, certain applications).</p>
        </div>
        """
    },
    {
        "title": "The Power of Conjugate Prior Structure",
        "body": """
        <p><strong>Example: Sequential Coin Flips with Beta-Bernoulli</strong></p>

        <p>Start with $\\text{Beta}(1, 1)$ prior. Flip coin repeatedly:</p>

        <pre class='code-block'>After 1 flip (H): $\\text{Beta}(2, 1) \\to$ mean $= 2/3$
After 2 flips (H, T): $\\text{Beta}(2, 2) \\to$ mean $= 2/4 = 0.5$
After 3 flips (H, T, H): $\\text{Beta}(3, 2) \\to$ mean $= 3/5 = 0.6$
...
After $n$ flips ($k$ heads): $\\text{Beta}(1+k, 1+n-k) \\to$ mean $= (1+k)/(2+n)$</pre>

        <p>Each flip updates parameters by simple increment. No recomputation of the entire integral. This is the beauty of conjugacy: <em>sequential updating is trivial</em>.</p>

        <p><strong>Posterior as Prior:</strong> Once we have $\\text{Beta}(10, 7)$ from our 15 flips, if we flip 5 more times and get 3 heads, the new posterior is:</p>

        <p>$$\\text{Beta}(10 + 3, 7 + 2) = \\text{Beta}(13, 9)$$</p>

        <p>All prior information is encoded in the $\\text{Beta}(10, 7)$; we don't forget or need to re-process old flips.</p>

        <div class='success-box'>
        <p><strong>Insight:</strong> Conjugate priors reveal the structure of Bayesian learning. The posterior parameters are just the prior parameters plus counts of the observed data. This mirrors how humans naturally update beliefs: "I thought this, now I see that, so I believe this"—all in simple, incremental steps.</p>
        </div>
        """
    },
    {
        "title": "When Conjugacy Breaks Down: Beyond the Textbook",
        "body": """
        <p><strong>Real-world models often lack conjugate priors:</strong></p>
        <ul>
        <li><strong>Nonlinear models:</strong> Logistic regression, neural networks</li>
        <li><strong>Hierarchical models:</strong> Shared parameters across groups (Bayesian mixed models)</li>
        <li><strong>Complex likelihoods:</strong> Mixture models, survival analysis</li>
        <li><strong>High-dimensional inference:</strong> Gene expression, image analysis</li>
        </ul>

        <p><strong>Solution: Computational methods</strong></p>
        <ul>
        <li><strong>MCMC (Markov Chain Monte Carlo):</strong> Simulate samples from posterior; works for any prior and likelihood</li>
        <li><strong>Variational Inference:</strong> Approximate posterior with simpler distribution</li>
        <li><strong>Expectation Propagation:</strong> Iterative refinement of posterior approximation</li>
        </ul>

        <p><strong>Key point:</strong> Conjugacy is nice when it applies, but modern Bayesian inference doesn't depend on it. Computational methods have democratized Bayesian analysis for complex, realistic models.</p>

        <div class='concept-box'>
        <p>Learning conjugate priors provides <em>intuition</em> about Bayesian inference and builds comfort with the framework. In practice, the choice between conjugate and non-conjugate priors is guided by which better reflects your domain knowledge and computational resources.</p>
        </div>
        """
    }
]
