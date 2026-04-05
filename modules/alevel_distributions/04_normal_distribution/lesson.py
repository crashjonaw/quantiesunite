TITLE = "Normal Distribution"

SECTIONS = [
    {
        "title": "The Normal Distribution and Its Properties",
        "body": """
<h3>What is the Normal Distribution?</h3>
<p>The <strong>normal (Gaussian) distribution</strong> is the most important distribution in statistics. A random variable $X$ is normally distributed with mean $\\mu$ and standard deviation $\\sigma$ if its probability density function is:</p>

<p>$$f(x) = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-\\frac{(x-\\mu)^{2}}{2\\sigma^{2}}}$$</p>

<p>We write: $X \\sim N(\\mu, \\sigma^{2})$ or $X \\sim N(\\mu, \\sigma)$ depending on notation convention.</p>

<h3>Key Properties of the Normal Distribution</h3>
<p><strong>Shape and Symmetry:</strong></p>
<ul>
<li>Bell-shaped curve, symmetric about the mean $\\mu$</li>
<li>The mean, median, and mode are all equal</li>
<li>Total area under the curve equals 1 (it's a probability density)</li>
</ul>

<p><strong>The Empirical Rule (68-95-99.7):</strong></p>
<ul>
<li>Approximately 68% of data falls within $\\mu \\pm 1\\sigma$</li>
<li>Approximately 95% of data falls within $\\mu \\pm 2\\sigma$</li>
<li>Approximately 99.7% of data falls within $\\mu \\pm 3\\sigma$</li>
</ul>

<p><strong>Effect of Parameters:</strong></p>
<ul>
<li><strong>$\\mu$:</strong> Controls the center (location) of the distribution</li>
<li><strong>$\\sigma$:</strong> Controls the spread (width) of the distribution</li>
<li>Larger $\\sigma$ means flatter, wider curve; smaller $\\sigma$ means taller, narrower curve</li>
</ul>

<div class="worked-example">
<h4>Example 1: Empirical Rule</h4>
<p>Adult heights are approximately $N(170\\text{ cm}, 10^{2}\\text{ cm}^{2})$, so $\\mu = 170$, $\\sigma = 10$.</p>
<p><strong>Within 1 SD:</strong> Between 160 and 180 cm contains ~68% of adults</p>
<p><strong>Within 2 SDs:</strong> Between 150 and 190 cm contains ~95% of adults</p>
<p><strong>Between 180 and 190 cm:</strong> Contains $(95\\% - 68\\%)/2 = 13.5\\%$ of adults</p>
</div>

<h3>Why Is Normal Distribution So Important?</h3>
<p>Many real-world measurements follow (approximately) normal distributions:</p>
<ul>
<li>Heights, weights, test scores</li>
<li>Measurement errors and noise</li>
<li>Distribution of sample means (Central Limit Theorem)</li>
<li>Many natural phenomena in biology, physics, economics</li>
</ul>

<p>Moreover, sums and averages of independent random variables tend toward normal distributions, making it essential for inference and hypothesis testing.</p>

<div class="success-box">
<h4>Key Insight</h4>
<p>The normal distribution is the workhorse of statistics. It appears naturally (via Central Limit Theorem) and allows us to make probabilistic statements about data and samples.</p>
</div>
"""
    },
    {
        "title": "Standardization and Z-Scores",
        "body": """
<h3>The Standard Normal Distribution</h3>
<p>The <strong>standard normal distribution</strong> has $\\mu = 0$ and $\\sigma = 1$. We denote it $Z \\sim N(0, 1)$.</p>

<p>Its probability density function simplifies to:</p>

<p>$$f(z) = \\frac{1}{\\sqrt{2\\pi}} e^{-z^{2}/2}$$</p>

<p>Standard normal tables give cumulative probabilities $\\Phi(z) = P(Z \\leq z)$ for any $z$ value.</p>

<h3>Z-Scores: Converting to Standard Normal</h3>
<p>To convert any normal variable $X \\sim N(\\mu, \\sigma^{2})$ to the standard normal, use the <strong>z-score transformation</strong>:</p>

<p>$$Z = \\frac{X - \\mu}{\\sigma}$$</p>

<p>This transforms any normal problem into a standard normal problem, allowing us to use standard normal tables.</p>

<p><strong>Properties of z-scores:</strong></p>
<ul>
<li>$Z$ measures how many standard deviations $X$ is from its mean</li>
<li>Positive $Z$: $X$ is above the mean</li>
<li>Negative $Z$: $X$ is below the mean</li>
<li>$Z = 0$ corresponds to $X = \\mu$</li>
</ul>

<div class="worked-example">
<h4>Example 2: Z-Score Calculation</h4>
<p>Heights $\\sim N(170\\text{ cm}, 10^{2}\\text{ cm}^{2})$. Find $P(\\text{height} > 185\\text{ cm})$.</p>
<p><strong>Step 1:</strong> Convert to z-score: $Z = \\frac{185 - 170}{10} = 1.5$</p>
<p><strong>Step 2:</strong> Find $P(Z > 1.5)$ from standard normal tables</p>
<p>$P(Z \\leq 1.5) \\approx 0.9332$ (from tables)</p>
<p>$P(Z > 1.5) = 1 - 0.9332 = 0.0668 \\approx 6.68\\%$</p>
<p><strong>Interpretation:</strong> About 6.68% of adults are taller than 185 cm.</p>
</div>

<h3>Finding Percentiles and Inverse Problems</h3>
<p>Sometimes we know a probability and want to find the corresponding value.</p>

<p><strong>Method:</strong> Use inverse z-table lookup (or "percentile tables"):</p>
<ol>
<li>Find the $z$ value where $P(Z \\leq z)$ equals the desired probability</li>
<li>Convert back using $X = \\mu + z \\cdot \\sigma$</li>
</ol>

<div class="worked-example">
<h4>Example 3: Finding a Percentile</h4>
<p>IQ scores $\\sim N(100, 15^{2}\\text{ pts}^{2})$. Find the 90th percentile.</p>
<p><strong>Step 1:</strong> Find $z$ such that $P(Z \\leq z) = 0.90$</p>
<p>From inverse z-tables: $z \\approx 1.28$</p>
<p><strong>Step 2:</strong> Convert back: $X = 100 + 1.28(15) = 119.2$</p>
<p><strong>Interpretation:</strong> 90% of people have IQ $\\leq 119.2$</p>
</div>

<div class="warning-box">
<h4>Common Mistakes with Z-Scores</h4>
<ul>
<li>Forgetting the denominator $\\sigma$ (using $X - \\mu$ instead of $\\frac{X - \\mu}{\\sigma}$)</li>
<li>Confusing $P(Z \\leq z)$ with $P(Z > z)$ (remember they sum to 1)</li>
<li>Misreading z-tables (check if they give left-tail or right-tail probabilities)</li>
<li>Not converting back to $X$ when finding percentiles</li>
</ul>
</div>
"""
    }
]
