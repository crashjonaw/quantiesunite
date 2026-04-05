TITLE = "Discrete Random Variables and Probability Distributions"

SECTIONS = [
    {
        "title": "Foundations: Random Variables and Probability",
        "body": """
<h3>What is a Random Variable?</h3>
<p>A <strong>random variable</strong> $X$ is a function that assigns numerical values to outcomes of an experiment.</p>

<p><strong>Example:</strong> Flip a coin 3 times and count heads. $X$ can be 0, 1, 2, or 3.</p>

<p>A <strong>discrete random variable</strong> takes on countable values (0, 1, 2, 3, ...). This contrasts with <strong>continuous</strong> variables that can take any value in an interval.</p>

<div class="concept-box">
<h4>Key Definitions</h4>
<ul>
<li><strong>Sample space:</strong> Set of all possible outcomes</li>
<li><strong>Event:</strong> A subset of the sample space</li>
<li><strong>Probability:</strong> A number between 0 and 1 assigned to each outcome</li>
</ul>
</div>

<h3>Probability Mass Function (PMF)</h3>
<p>For a discrete random variable $X$, the <strong>probability mass function</strong> is:</p>

<p>$$P(X = k) = p_k$$</p>

<p>This gives the probability that $X$ equals exactly $k$.</p>

<p><strong>Properties of a PMF:</strong></p>
<ol>
<li>$0 \\leq P(X = k) \\leq 1$ for all $k$</li>
<li>$\\sum P(X = k) = 1$ (probabilities sum to 1)</li>
<li>$P(X = k) = 0$ for values not in the support of $X$</li>
</ol>

<div class="worked-example">
<h4>Example 1: Fair Six-Sided Die</h4>
<p>Roll a die once. Let $X$ = the face value shown.</p>
<p><strong>PMF:</strong> $P(X = k) = \\frac{1}{6}$ for $k \\in \\{1, 2, 3, 4, 5, 6\\}$</p>
<p><strong>Verification:</strong> $\\sum P(X = k) = 6 \\times \\frac{1}{6} = 1$ ✓</p>
</div>

<h3>Cumulative Distribution Function (CDF)</h3>
<p>The <strong>cumulative distribution function</strong> is:</p>

<p>$$F(x) = P(X \\leq x) = \\sum_{k \\leq x} P(X = k)$$</p>

<p>This gives the total probability that $X$ is at most $x$.</p>

<p><strong>Properties of a CDF:</strong></p>
<ul>
<li>$0 \\leq F(x) \\leq 1$</li>
<li>$F$ is non-decreasing (right-continuous)</li>
<li>$\\lim_{x \\to -\\infty} F(x) = 0$ and $\\lim_{x \\to \\infty} F(x) = 1$</li>
<li>$P(a \\leq X \\leq b) = F(b) - F(a-1)$ for discrete $X$</li>
</ul>

<div class="worked-example">
<h4>Example 2: CDF for a Die Roll</h4>
<p>For the die example, the CDF is:</p>
<p>$F(x) = 0$ if $x < 1$</p>
<p>$F(x) = \\frac{k}{6}$ if $k \\leq x < k+1$, for $k \\in \\{1, 2, 3, 4, 5\\}$</p>
<p>$F(x) = 1$ if $x \\geq 6$</p>
<p><strong>Calculate:</strong> $P(X \\leq 3) = F(3) = \\frac{3}{6} = 0.5$</p>
</div>
"""
    },
    {
        "title": "Expected Value and Variance",
        "body": """
<h3>Expected Value (Mean)</h3>
<p>The <strong>expected value</strong> or <strong>mean</strong> of $X$ is:</p>

<p>$$E(X) = \\mu = \\sum k \\times P(X = k)$$</p>

<p>This is the long-run average value if we repeat the experiment many times.</p>

<div class="worked-example">
<h4>Example 3: Expected Value of a Die Roll</h4>
<p>$E(X) = 1\\left(\\frac{1}{6}\\right) + 2\\left(\\frac{1}{6}\\right) + 3\\left(\\frac{1}{6}\\right) + 4\\left(\\frac{1}{6}\\right) + 5\\left(\\frac{1}{6}\\right) + 6\\left(\\frac{1}{6}\\right)$</p>
<p>$$E(X) = \\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \\frac{21}{6} = 3.5$$</p>
</div>

<h3>Variance and Standard Deviation</h3>
<p>The <strong>variance</strong> measures spread around the mean:</p>

<p>$$\\text{Var}(X) = \\sigma^{2} = E[(X - \\mu)^{2}] = E(X^{2}) - [E(X)]^{2}$$</p>

<p>The <strong>standard deviation</strong> is the square root:</p>

<p>$$\\text{SD}(X) = \\sigma = \\sqrt{\\text{Var}(X)}$$</p>

<div class="worked-example">
<h4>Example 4: Variance of a Die Roll</h4>
<p>$E(X^{2}) = 1^{2}\\left(\\frac{1}{6}\\right) + 2^{2}\\left(\\frac{1}{6}\\right) + \\cdots + 6^{2}\\left(\\frac{1}{6}\\right) = \\frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \\frac{91}{6}$</p>
<p>$\\text{Var}(X) = E(X^{2}) - [E(X)]^{2} = \\frac{91}{6} - (3.5)^{2} = \\frac{91}{6} - 12.25 \\approx 2.917$</p>
<p>$\\text{SD}(X) = \\sqrt{2.917} \\approx 1.708$</p>
</div>

<h3>Properties of Expectation and Variance</h3>
<p><strong>Linearity of Expectation:</strong></p>
<ul>
<li>$E(aX + b) = aE(X) + b$</li>
<li>$E(X + Y) = E(X) + E(Y)$ (always true, even if $X$ and $Y$ are dependent)</li>
</ul>

<p><strong>Variance Properties:</strong></p>
<ul>
<li>$\\text{Var}(aX + b) = a^{2}\\text{Var}(X)$ (constant $b$ doesn't affect variance)</li>
<li>$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y)$ if $X$ and $Y$ are independent</li>
</ul>

<div class="success-box">
<h4>Key Insight</h4>
<p>These properties let us compute means and variances of sums without knowing the full distribution. This is fundamental to understanding how distributions of sums (like sample totals) relate to individual distributions.</p>
</div>
"""
    }
]
