TITLE = "Binomial Distribution"

SECTIONS = [
    {
        "title": "Bernoulli Trials and Binomial Experiments",
        "body": """
<h3>Setting Up Binomial Experiments</h3>
<p>A <strong>Bernoulli trial</strong> is an experiment with two outcomes: success (probability p) or failure (probability 1-p).</p>

<p>A <strong>binomial experiment</strong> repeats n independent Bernoulli trials and counts X = number of successes.</p>

<p><strong>Conditions for a Binomial Setting:</strong></p>
<ol>
<li>Fixed number n of trials</li>
<li>Each trial is independent</li>
<li>Two outcomes per trial (success/failure)</li>
<li>Probability p is constant across all trials</li>
</ol>

<div class="success-box">
<h4>Examples of Binomial Settings</h4>
<ul>
<li>Flipping a coin n times; count heads (p = 0.5)</li>
<li>Surveying n people; count who prefer brand A (p = % preference)</li>
<li>Manufacturing: inspect n items; count defectives (p = defect rate)</li>
<li>Medical: treat n patients; count who recover (p = recovery rate)</li>
</ul>
</div>

<h3>Deriving the Binomial Probability Formula</h3>
<p>For exactly k successes in n trials, we need:</p>
<ul>
<li>Exactly k trials to succeed, each with probability p</li>
<li>Exactly (n-k) trials to fail, each with probability (1-p)</li>
<li>Any arrangement of these k successes among n trials</li>
</ul>

<p>Any specific sequence of k successes and (n-k) failures has probability:</p>
<p style="text-align: center;">\(p^k \\times (1-p)^{n-k}\)</p>

<p>The number of such sequences is the binomial coefficient (n choose k):</p>
<p style="text-align: center; font-weight: bold;">\(\binom{n}{k} = \\frac{n!}{k!(n-k)!}\)</p>

<p><strong>Binomial Probability Formula:</strong></p>
<p style="text-align: center; font-weight: bold;">\(P(X = k) = \binom{n}{k} \\times p^k \\times (1-p)^{n-k}\)</p>

<p>where \(X \sim \\text{Binomial}(n, p)\).</p>

<div class="worked-example">
<h4>Example 1: Coin Flips</h4>
<p>A fair coin is flipped 5 times. Find \(P(\\text{exactly 2 heads})\).</p>
<p><strong>Solution:</strong></p>
<p>n = 5, k = 2, p = 0.5</p>
<p>\(\binom{5}{2} = \\frac{5!}{2! \\cdot 3!} = 10\)</p>
<p>\(P(X = 2) = 10 \\times (0.5)^2 \\times (0.5)^3 = 10 \\times 0.25 \\times 0.125 = 0.3125\)</p>
</div>

<div class="warning-box">
<h4>Common Mistakes</h4>
<ul>
<li>Forgetting the binomial coefficient \(\binom{n}{k}\) (just using \(p^k(1-p)^{n-k}\))</li>
<li>Not checking independence: are trials truly independent?</li>
<li>Confusing "exactly k" with "at least k" or "at most k"</li>
</ul>
</div>
"""
    },
    {
        "title": "Mean, Variance, and Properties of Binomial Distribution",
        "body": """
<h3>Mean and Variance of Binomial Distribution</h3>
<p><strong>Expected Value:</strong></p>
<p style="text-align: center; font-weight: bold;">\(E(X) = \\mu = np\)</p>

<p><strong>Variance:</strong></p>
<p style="text-align: center; font-weight: bold;">\(\\text{Var}(X) = \\sigma^2 = np(1-p)\)</p>

<p><strong>Standard Deviation:</strong></p>
<p style="text-align: center; font-weight: bold;">\(\\text{SD}(X) = \\sigma = \\sqrt{np(1-p)}\)</p>

<h3>Deriving the Mean from First Principles</h3>
<p>Let \(X_1, X_2, \ldots, X_n\) be indicator variables where \(X_i = 1\) if trial i succeeds, 0 otherwise.</p>

<p>Each \(X_i\) is Bernoulli(p), so \(E(X_i) = p\) and \(\\text{Var}(X_i) = p(1-p)\).</p>

<p>The total number of successes is:</p>
<p style="text-align: center;">\(X = X_1 + X_2 + \\cdots + X_n\)</p>

<p>By linearity of expectation:</p>
<p style="text-align: center;">\(E(X) = E(X_1) + E(X_2) + \\cdots + E(X_n) = p + p + \\cdots + p = np\)</p>

<p>Since trials are independent:</p>
<p style="text-align: center;">\(\\text{Var}(X) = \\text{Var}(X_1) + \\text{Var}(X_2) + \\cdots + \\text{Var}(X_n) = p(1-p) + \\cdots + p(1-p) = np(1-p)\)</p>

<div class="worked-example">
<h4>Example 2: Manufacturing Quality</h4>
<p>A factory produces items; 5% are defective. In a batch of 200:</p>
<p><strong>Expected number defective:</strong> \(\\mu = 200 \\times 0.05 = 10\)</p>
<p><strong>Variance:</strong> \(\\sigma^2 = 200 \\times 0.05 \\times 0.95 = 9.5\)</p>
<p><strong>Standard deviation:</strong> \(\\sigma = \\sqrt{9.5} \\approx 3.08\)</p>
<p>We expect about 10 defective items, with a standard deviation of roughly 3 items.</p>
</div>

<h3>Shape and Behavior</h3>
<p>The binomial distribution's shape depends on p:</p>
<ul>
<li><strong>p = 0.5:</strong> Symmetric bell-shaped curve (most balanced)</li>
<li><strong>p &lt; 0.5:</strong> Right-skewed (tail extends to the right)</li>
<li><strong>p &gt; 0.5:</strong> Left-skewed (tail extends to the left)</li>
<li><strong>p close to 0 or 1:</strong> Highly skewed, concentrated at one end</li>
</ul>

<p>As n increases, the binomial distribution becomes more bell-shaped and symmetric (approaching a normal distribution).</p>

<div class="success-box">
<h4>Key Properties</h4>
<ul>
<li>The mode (most probable value) is near np</li>
<li>The spread (standard deviation) increases with n, but more slowly (proportional to \(\\sqrt{n}\))</li>
<li>The probability of any single value decreases as n increases (density spreads over more values)</li>
</ul>
</div>
"""
    }
]
