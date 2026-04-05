TITLE = "Approximations and Advanced Properties"

SECTIONS = [
    {
        "title": "Normal Approximation to Binomial and Poisson",
        "body": """
<h3>Normal Approximation to Binomial Distribution</h3>
<p>When $n$ is large, computing $\\text{Binomial}(n, p)$ probabilities using the formula is tedious. The <strong>normal approximation</strong> makes this easier.</p>

<p><strong>Conditions for Normal Approximation to Binomial:</strong></p>
<ul>
<li>$np \\geq 5$ and $n(1-p) \\geq 5$ (common rule of thumb)</li>
<li>Some sources use $np \\geq 10$ and $n(1-p) \\geq 10$ for better accuracy</li>
</ul>

<p>When conditions are met, $X \\sim \\text{Binomial}(n, p)$ is approximately:</p>

<p>$$X \\approx N(\\mu = np,\\; \\sigma^{2} = np(1-p))$$</p>

<p>Convert to standard normal using $Z = \\frac{X - np}{\\sqrt{np(1-p)}}$ and use z-tables.</p>

<h3>Continuity Correction</h3>
<p>Since Binomial is discrete and Normal is continuous, use a <strong>continuity correction</strong> for better accuracy:</p>

<ul>
<li>$P(X = k) \\approx P(k - 0.5 < X < k + 0.5)$</li>
<li>$P(X \\geq k) \\approx P(X > k - 0.5)$</li>
<li>$P(X \\leq k) \\approx P(X < k + 0.5)$</li>
<li>$P(X > k) \\approx P(X > k + 0.5)$</li>
<li>$P(X < k) \\approx P(X < k - 0.5)$</li>
</ul>

<div class="worked-example">
<h4>Example 1: Normal Approximation to Binomial</h4>
<p>$\\text{Binomial}(n = 100, p = 0.4)$. Find $P(X \\geq 40)$.</p>
<p><strong>Check conditions:</strong> $np = 40 > 5$ ✓, $n(1-p) = 60 > 5$ ✓</p>
<p><strong>Normal parameters:</strong> $\\mu = 40$, $\\sigma = \\sqrt{100 \\times 0.4 \\times 0.6} = \\sqrt{24} \\approx 4.90$</p>
<p><strong>With continuity correction:</strong> $P(X \\geq 40) \\approx P(X > 39.5)$</p>
<p>$Z = \\frac{39.5 - 40}{4.90} \\approx -0.102$</p>
<p>$P(Z > -0.102) = 1 - P(Z \\leq -0.102) \\approx 1 - 0.459 = 0.541$</p>
</div>

<h3>Normal Approximation to Poisson Distribution</h3>
<p>When $\\lambda$ is large (typically $\\lambda > 10$), $\\text{Poisson}(\\lambda)$ is approximately:</p>

<p>$$X \\approx N(\\mu = \\lambda,\\; \\sigma^{2} = \\lambda)$$</p>

<p>This allows us to use z-tables for Poisson problems without computing factorials.</p>

<div class="worked-example">
<h4>Example 2: Normal Approximation to Poisson</h4>
<p>A website receives traffic following $\\text{Poisson}(\\lambda = 30)$ page views per minute. Find $P(X \\leq 25)$.</p>
<p><strong>Check condition:</strong> $\\lambda = 30 > 10$ ✓</p>
<p><strong>Normal parameters:</strong> $\\mu = 30$, $\\sigma = \\sqrt{30} \\approx 5.48$</p>
<p><strong>With continuity correction:</strong> $P(X \\leq 25) \\approx P(X < 25.5)$</p>
<p>$Z = \\frac{25.5 - 30}{5.48} \\approx -0.821$</p>
<p>$P(Z < -0.821) \\approx 0.206$ or $20.6\\%$</p>
</div>

<h3>When to Use Each Approximation</h3>
<p><strong>Poisson to Binomial:</strong> Use $\\text{Poisson}(\\lambda = np)$ for $\\text{Binomial}(n, p)$ when $n$ is large and $p$ is small.</p>

<p><strong>Either to Normal:</strong> Use Normal when the discrete distribution's conditions are met.</p>

<p><strong>Computational Rule of Thumb:</strong></p>
<ul>
<li>If $n$ and $p$ make Binomial formula feasible, use exact formula</li>
<li>Otherwise, try Poisson approximation first (simpler)</li>
<li>If Poisson $\\lambda$ is large, use Normal approximation</li>
</ul>

<div class="success-box">
<h4>Key Insight</h4>
<p>Approximations reduce computational burden and provide insights into distribution relationships. All three distributions—Binomial, Poisson, and Normal—are connected through limiting processes!</p>
</div>
"""
    },
    {
        "title": "Advanced Properties and Applications",
        "body": """
<h3>Cumulative Distribution Functions (CDF)</h3>
<p>The <strong>cumulative distribution function</strong> $F(x) = P(X \\leq x)$ gives the total probability up to $x$.</p>

<p><strong>For discrete distributions:</strong></p>
<p>$$F(k) = \\sum_{i \\leq k} P(X = i)$$</p>

<p><strong>For continuous distributions:</strong></p>
<p>$$F(x) = \\int_{-\\infty}^{x} f(t)\\,dt$$</p>

<p><strong>Using CDFs to find probabilities:</strong></p>
<ul>
<li>$P(X \\leq b) = F(b)$</li>
<li>$P(a < X \\leq b) = F(b) - F(a)$</li>
<li>$P(X > a) = 1 - F(a)$</li>
</ul>

<p>For the standard normal, $\\Phi(z)$ denotes the CDF, and z-tables give these values.</p>

<h3>Central Limit Theorem (Conceptual Overview)</h3>
<p>The <strong>Central Limit Theorem (CLT)</strong> is one of the most powerful results in statistics:</p>

<p><strong>Statement:</strong> If $X_1, X_2, \\ldots, X_n$ are independent random variables with the same distribution, finite mean $\\mu$, and finite variance $\\sigma^{2}$, then the sample mean:</p>

<p>$$\\bar{X} = \\frac{X_1 + X_2 + \\cdots + X_n}{n}$$</p>

<p>is approximately normally distributed as $n \\to \\infty$, with:</p>

<p>$$\\bar{X} \\sim \\text{approx } N\\left(\\mu,\\; \\frac{\\sigma^{2}}{n}\\right)$$</p>

<p><strong>Key implication:</strong> The sum $S_n = X_1 + \\cdots + X_n$ satisfies:</p>

<p>$$S_n \\sim \\text{approx } N(n\\mu,\\; n\\sigma^{2})$$</p>

<p>This holds <strong>regardless of the shape of the original distribution</strong>—it only needs finite mean and variance!</p>

<div class="worked-example">
<h4>Example 3: Central Limit Theorem</h4>
<p>A restaurant's customers order amounts with mean \\$25 and SD \\$8 (unknown original distribution).</p>
<p>For a day with 100 customers, the total revenue $S_{100}$ has:</p>
<p><strong>Mean:</strong> $E(S_{100}) = 100 \\times 25 = \\$2500$</p>
<p><strong>SD:</strong> $\\text{SD}(S_{100}) = \\sqrt{100 \\times 8^{2}} = \\sqrt{6400} = 80$ dollars</p>
<p><strong>Distribution:</strong> $S_{100} \\approx N(2500, 80^{2})$ by CLT</p>
<p>$P(S_{100} > 2600) = P\\left(Z > \\frac{2600-2500}{80}\\right) = P(Z > 1.25) \\approx 0.106$</p>
</div>

<h3>Sampling Distributions</h3>
<p>When we collect data and compute statistics, those statistics themselves have distributions.</p>

<p><strong>Distribution of Sample Mean:</strong> If we take random samples of size $n$ from $N(\\mu, \\sigma^{2})$:</p>

<p>$$\\bar{X} \\sim N\\left(\\mu,\\; \\frac{\\sigma^{2}}{n}\\right)$$</p>

<p>Key observation: As $n$ increases, the sample mean becomes more concentrated around $\\mu$ (standard error $= \\frac{\\sigma}{\\sqrt{n}}$ decreases).</p>

<p><strong>Why This Matters:</strong></p>
<ul>
<li>Allows us to estimate population parameters from sample data</li>
<li>Enables hypothesis testing and confidence intervals</li>
<li>Justifies using sample mean as an estimate of population mean</li>
</ul>

<div class="success-box">
<h4>Summary of Relationships</h4>
<ul>
<li><strong>Binomial:</strong> Counts successes in $n$ fixed trials</li>
<li><strong>Poisson:</strong> Counts rare events in time/space; limit of $\\text{Binomial}(n,p)$ as $n \\to \\infty$, $p \\to 0$, $np \\to \\lambda$</li>
<li><strong>Normal:</strong> Bell-shaped continuous distribution; limit of Binomial/Poisson with appropriate parameters; distribution of sample means (CLT)</li>
</ul>
</div>
"""
    }
]
