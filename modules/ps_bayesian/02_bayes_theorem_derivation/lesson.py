TITLE = "Bayes' Theorem Derivation and Components"

SECTIONS = [
    {
        "title": "From Conditional Probability to Bayes' Theorem",
        "body": """
        <p><strong>Starting from first principles:</strong> Bayes' theorem emerges naturally from the definition of conditional probability.</p>

        <p>Recall: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ (conditional probability)</p>

        <p>Rearranging: $P(A \\cap B) = P(A|B)\\, P(B)$</p>

        <p>By symmetry: $P(A \\cap B) = P(B|A)\\, P(A)$</p>

        <p><strong>Combining:</strong> Since both equal $P(A \\cap B)$:</p>

        <p>$$P(A|B)\\, P(B) = P(B|A)\\, P(A)$$</p>

        <p>$$P(A|B) = \\frac{P(B|A)\\, P(A)}{P(B)}$$</p>

        <div class='success-box'>
        <p><strong>This is Bayes' Theorem!</strong> It's not mysterious—just algebra from conditional probability.</p>
        </div>
        """
    },
    {
        "title": "Bayes' Theorem in Statistical Language",
        "body": """
        <p>Translate events $A$ and $B$ into statistical parameters and data:</p>
        <ul>
        <li>Event $A \\to$ Parameter $\\theta$ (unknown, what we want to learn)</li>
        <li>Event $B \\to$ Data $y$ (observed, what we have)</li>
        </ul>

        <p><strong>Bayes' Theorem becomes:</strong></p>

        <p>$$p(\\theta|y) = \\frac{p(y|\\theta)\\, p(\\theta)}{p(y)}$$</p>

        <p><strong>Component interpretation:</strong></p>
        <ul>
        <li><strong>$p(\\theta|y)$:</strong> Posterior — probability of $\\theta$ given data $y$</li>
        <li><strong>$p(y|\\theta)$:</strong> Likelihood — probability of observing $y$ under model with parameter $\\theta$</li>
        <li><strong>$p(\\theta)$:</strong> Prior — marginal probability of $\\theta$ before seeing data</li>
        <li><strong>$p(y)$:</strong> Evidence or marginal likelihood (normalizing constant)</li>
        </ul>

        <p><strong>The evidence $p(y)$:</strong> How likely are the observed data, averaging over all possible parameter values?</p>

        <p>$$p(y) = \\int p(y|\\theta)\\, p(\\theta)\\, d\\theta$$</p>

        <p>In practice, we often ignore $p(y)$ and write:</p>

        <p>$$p(\\theta|y) \\propto p(y|\\theta)\\, p(\\theta)$$</p>

        <p>The proportionality ($\\propto$) means we normalize afterward to ensure the posterior integrates to 1.</p>

        <div class='concept-box'>
        <p><strong>Verbal translation:</strong> "Posterior is proportional to likelihood times prior."</p>
        </div>
        """
    },
    {
        "title": "The Evidence and Why It Matters",
        "body": """
        <p><strong>What is $p(y)$?</strong> The probability of observing the data, marginalized over all parameter values:</p>

        <p>$$p(y) = \\int p(y|\\theta)\\, p(\\theta)\\, d\\theta$$</p>

        <p><strong>Why is it called 'evidence'?</strong></p>
        <ul>
        <li>Measures how well the model explains the data overall</li>
        <li>Used in Bayes Factor for model comparison</li>
        <li>High $p(y)$ means the data is likely under the model; low $p(y)$ suggests poor model fit</li>
        </ul>

        <p><strong>Computational challenge:</strong> For many models, $p(y)$ is intractable (requires high-dimensional integration). This motivates approximations like MCMC.</p>

        <p><strong>For likelihood-free inference:</strong> We can sample from the posterior without computing $p(y)$ explicitly, by using ratios of unnormalized distributions.</p>

        <div class='worked-example'>
        <p><strong>Example: Normal Model with Known Variance</strong></p>
        <p>Data: $y_1, \\ldots, y_n \\sim N(\\mu, \\sigma^2)$ where $\\sigma^2$ is known.</p>
        <p>Prior: $\\mu \\sim N(m, s^2)$</p>

        <p>The evidence $p(y)$ has a closed form:</p>

        <pre class='code-block'>$p(y) = (2\\pi\\sigma^2)^{-n/2} \\cdot (2\\pi s^2)^{-1/2}$
$\\cdot \\exp\\left\\{-\\left[\\frac{\\sum(y_i - m)^2}{2\\sigma^2} + \\frac{(\\bar{y} - m)^2 s^2}{2\\sigma^2(s^2 + \\sigma^2/n)}\\right] / s^2\\right\\}$</pre>

        <p>Posterior is also normal: $\\mu|y \\sim N(\\mu_{\\text{post}}, \\sigma^2_{\\text{post}})$ where the posterior mean and variance depend on both prior and data.</p>
        </div>

        <div class='warning-box'>
        <p><strong>Be careful:</strong> $p(y)$ is not the same as the likelihood. The likelihood $p(y|\\theta)$ is a function of $\\theta$ given $y$; the evidence $p(y)$ is a single number (the integral of likelihood $\\times$ prior over $\\theta$).</p>
        </div>
        """
    }
]
