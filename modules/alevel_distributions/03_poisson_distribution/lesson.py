TITLE = "Poisson Distribution"

SECTIONS = [
    {
        "title": "Derivation from Binomial Limit and Real-World Applications",
        "body": """
<h3>When Does Poisson Arise?</h3>
<p>The <strong>Poisson distribution</strong> arises as a limiting case of the binomial distribution when:</p>
<ul>
<li>Events occur randomly over time or space</li>
<li>Events are rare ($p$ is very small)</li>
<li>We observe a long period or large area ($n$ is very large)</li>
<li>The average rate $\\lambda = np$ stays moderate and constant</li>
</ul>

<p>Mathematically, as $n \\to \\infty$ and $p \\to 0$ with $np = \\lambda$ constant:</p>
<p>$$\\text{Binomial}(n, p) \\to \\text{Poisson}(\\lambda)$$</p>

<h3>The Poisson Probability Formula</h3>
<p>For a Poisson random variable $X$ with parameter $\\lambda$ (the expected number of events in the interval):</p>

<p>$$P(X = k) = \\frac{\\lambda^{k} e^{-\\lambda}}{k!}$$</p>

<p>where $k = 0, 1, 2, 3, \\ldots$ and $e \\approx 2.71828$ is Euler's number.</p>

<p>The Poisson distribution is determined entirely by its parameter $\\lambda$.</p>

<div class="worked-example">
<h4>Example 1: Poisson Probability</h4>
<p>Traffic accidents at an intersection average 2 per week. Assuming a Poisson model, find $P(\\text{exactly 3 accidents in a week})$.</p>
<p><strong>Solution:</strong> $\\lambda = 2$, $k = 3$</p>
<p>$P(X = 3) = \\frac{2^{3} \\times e^{-2}}{3!} = \\frac{8 \\times e^{-2}}{6}$</p>
<p>$e^{-2} \\approx 0.1353$, so $P(X = 3) \\approx \\frac{8 \\times 0.1353}{6} \\approx 0.180$</p>
</div>

<h3>Real-World Applications</h3>
<p>Poisson models are used for:</p>
<ul>
<li><strong>Traffic:</strong> Cars passing a point, accidents per time interval</li>
<li><strong>Phone calls:</strong> Number of calls to a customer service in an hour</li>
<li><strong>Biology:</strong> Number of mutations in a DNA sequence</li>
<li><strong>Astronomy:</strong> Number of photons detected per second</li>
<li><strong>Manufacturing:</strong> Number of defects in a roll of fabric (area-based)</li>
<li><strong>Medical:</strong> Number of rare disease cases in a region per year</li>
</ul>

<div class="success-box">
<h4>Key Insight</h4>
<p>Poisson is ideal when you're counting rare, randomly occurring events in a fixed time or space interval, where the rate is stable.</p>
</div>

<h3>Poisson vs. Binomial: When to Use Each</h3>
<p><strong>Use Binomial when:</strong></p>
<ul>
<li>Fixed number $n$ of trials is specified</li>
<li>Success/failure is clear and well-defined</li>
<li>Probability $p$ is reasonable (not too small)</li>
<li>Example: "In a survey of 500 people, how many prefer brand A?"</li>
</ul>

<p><strong>Use Poisson when:</strong></p>
<ul>
<li>Events occur in continuous time/space, not discrete trials</li>
<li>Events are rare and random</li>
<li>You know the average rate $\\lambda$</li>
<li>Example: "In an 8-hour shift, how many customer calls arrive?"</li>
</ul>

<div class="warning-box">
<h4>Important Note</h4>
<p>If you have a binomial problem with large $n$ and small $p$, you can use Poisson as an approximation (with $\\lambda = np$). This avoids tedious binomial calculations!</p>
</div>
"""
    },
    {
        "title": "Mean, Variance, and Properties",
        "body": """
<h3>Mean and Variance of Poisson Distribution</h3>
<p>For $X \\sim \\text{Poisson}(\\lambda)$:</p>

<p>$$E(X) = \\lambda$$</p>
<p>$$\\text{Var}(X) = \\lambda$$</p>
<p>$$\\text{SD}(X) = \\sqrt{\\lambda}$$</p>

<p><strong>A remarkable property:</strong> The mean and variance are equal!</p>

<h3>Intuition Behind Mean = Variance</h3>
<p>Since Poisson arises from $\\text{Binomial}(n, p)$ with $np = \\lambda$ and $n(1-p) \\approx n$ (when $p$ is tiny):</p>

<p>$\\text{Var}(\\text{Binomial}) = np(1-p) \\approx np \\times 1 = \\lambda$ (when $p \\to 0$)</p>

<p>So as the binomial approaches Poisson, both mean and variance converge to $\\lambda$.</p>

<div class="worked-example">
<h4>Example 2: Mean and Variance</h4>
<p>Email arrives at an average rate of 5 per hour. Model this as $\\text{Poisson}(\\lambda = 5)$.</p>
<p><strong>Mean:</strong> $E(X) = 5$ emails per hour</p>
<p><strong>Variance:</strong> $\\text{Var}(X) = 5$</p>
<p><strong>Standard deviation:</strong> $\\text{SD}(X) = \\sqrt{5} \\approx 2.24$ emails</p>
<p>On average we expect 5 emails, with a typical deviation of about 2-3 emails.</p>
</div>

<h3>Additivity Property of Poisson</h3>
<p>If $X_1 \\sim \\text{Poisson}(\\lambda_1)$ and $X_2 \\sim \\text{Poisson}(\\lambda_2)$ are independent, then:</p>

<p>$$X_1 + X_2 \\sim \\text{Poisson}(\\lambda_1 + \\lambda_2)$$</p>

<p>This is unique to Poisson! Poisson distributions "add" by adding their rate parameters.</p>

<div class="worked-example">
<h4>Example 3: Combined Poisson Processes</h4>
<p>A store receives customer arrivals: 3 per hour on average at the front door, 2 per hour on average at the side entrance.</p>
<p>Total arrivals $\\sim \\text{Poisson}(3 + 2) = \\text{Poisson}(5)$</p>
<p>$P(\\text{exactly 4 arrivals total}) = \\frac{5^{4} \\times e^{-5}}{4!} \\approx 0.176$</p>
</div>

<h3>Shape and Characteristics</h3>
<ul>
<li><strong>For $\\lambda < 1$:</strong> Distribution is right-skewed, mode at 0</li>
<li><strong>For $\\lambda \\approx 1$ to 3:</strong> Noticeably right-skewed</li>
<li><strong>For $\\lambda > 10$:</strong> Becomes approximately symmetric and bell-shaped (approaching normal)</li>
<li><strong>Mode:</strong> At $\\lfloor \\lambda \\rfloor$ or $\\lfloor \\lambda \\rfloor + 1$ (roughly at the mean)</li>
</ul>

<div class="success-box">
<h4>Key Properties</h4>
<ul>
<li>$\\text{Poisson}(\\lambda)$ can take any non-negative integer value</li>
<li>Mean = variance = $\\lambda$ is a distinctive feature</li>
<li>Sum of independent Poisson variables is Poisson</li>
<li>For large $\\lambda$, Poisson $\\approx$ Normal (we use this for approximations)</li>
</ul>
</div>
"""
    }
]
