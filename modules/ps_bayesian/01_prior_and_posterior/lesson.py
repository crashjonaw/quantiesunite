TITLE = "Prior and Posterior in Bayesian Framework"

SECTIONS = [
    {
        "title": "Understanding Prior and Posterior Distributions",
        "body": """
        <div class='concept-box'>
        <p><strong>Foundation of Bayesian thinking:</strong> Bayesian inference revolves around two key probability distributions that represent our knowledge at different stages.</p>
        </div>

        <p><strong>The Prior $p(\\theta)$:</strong> Our beliefs about the parameter $\\theta$ <em>before</em> observing any data.</p>
        <ul>
        <li>Encodes existing knowledge or assumptions</li>
        <li>Can be uninformative (flat), weakly informative, or informed by domain expertise</li>
        <li>Philosophical statement: "What do we believe before seeing evidence?"</li>
        </ul>

        <p><strong>The Posterior $p(\\theta|y)$:</strong> Our updated beliefs about $\\theta$ <em>after</em> observing data $y$.</p>
        <ul>
        <li>Combines prior belief with new evidence</li>
        <li>Represents the complete state of knowledge after inference</li>
        <li>The starting point for decision-making and prediction</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Intuitive Example: Medical Diagnosis</strong></p>
        <p>Suppose $\\theta$ represents the probability that a patient has a disease.</p>
        <ul>
        <li><strong>Prior:</strong> Population prevalence is 1%, so $p(\\theta)$ is centered around 0.01</li>
        <li><strong>Data:</strong> Patient takes a test; positive result (likelihood updates belief)</li>
        <li><strong>Posterior:</strong> Updated probability that patient actually has the disease, accounting for test accuracy</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Prior Selection: Philosophy and Practice",
        "body": """
        <p><strong>Types of Priors:</strong></p>

        <p><strong>1. Uninformative/Flat Prior:</strong> $p(\\theta) \\propto \\text{constant}$</p>
        <ul>
        <li>Represents maximum ignorance or indifference</li>
        <li>Problematic: Can lead to improper posteriors in some models</li>
        <li>Use cautiously; not always truly "uninformative"</li>
        </ul>

        <p><strong>2. Weakly Informative Prior:</strong> Mild constraints without strong bias</p>
        <ul>
        <li>Example: $N(0, 1)$ for a regression coefficient (allows $\\pm 2\\sigma$ range of reasonable values)</li>
        <li>Stabilizes computation and prevents extreme estimates</li>
        <li>Modern recommendation for many applications</li>
        </ul>

        <p><strong>3. Expert Prior:</strong> Encodes domain knowledge</p>
        <ul>
        <li>Informed by domain experts or historical data</li>
        <li>Requires careful elicitation to match expert opinion</li>
        <li>Common in clinical trials and engineering</li>
        </ul>

        <div class='concept-box'>
        <p><strong>Prior Sensitivity Analysis:</strong> Always check: How much does the posterior change if we use a different (plausible) prior? Robust Bayesian inference acknowledges this dependency.</p>
        </div>
        """
    },
    {
        "title": "From Prior to Posterior: The Fundamental Update",
        "body": """
        <p><strong>The Update Mechanism:</strong> Data pulls our beliefs from prior toward the likelihood.</p>

        <p>$$\\text{Posterior} \\propto \\text{Likelihood} \\times \\text{Prior}$$</p>
        <p>$$p(\\theta|y) \\propto p(y|\\theta) \\cdot p(\\theta)$$</p>

        <p>The normalizing constant $p(y)$ ensures the posterior integrates to 1:</p>

        <p>$$p(\\theta|y) = \\frac{p(y|\\theta)\\, p(\\theta)}{p(y)}$$</p>

        <p>$$\\text{where } p(y) = \\int p(y|\\theta)\\, p(\\theta)\\, d\\theta$$</p>

        <div class='worked-example'>
        <p><strong>Concrete Example: Coin Flipping</strong></p>
        <p>Let $\\theta$ = probability of heads. Flip coin 10 times, observe 7 heads.</p>

        <p><strong>Prior:</strong> $\\text{Beta}(1, 1)$ — uniform on $[0, 1]$ (maximum ignorance)</p>
        <p><strong>Likelihood:</strong> Binomial: $\\theta^7 (1-\\theta)^3$</p>
        <p><strong>Posterior:</strong> $\\text{Beta}(1+7, 1+3) = \\text{Beta}(8, 4)$</p>

        <pre class='code-block'>Prior mean: $0.5$
Posterior mean: $8/12 \\approx 0.667$
Data shifted belief toward the observed frequency.</pre>
        </div>

        <div class='warning-box'>
        <p><strong>Key insight:</strong> As we collect more data, the posterior becomes increasingly concentrated around the true value, independent of the prior (under regularity conditions). This is Bayesian <em>consistency</em>.</p>
        </div>
        """
    }
]
