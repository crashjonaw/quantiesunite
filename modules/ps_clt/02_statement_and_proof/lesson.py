TITLE = "Statement and Proof Intuition of CLT"

SECTIONS = [
    {
        "title": "Formal Statement of the Central Limit Theorem",
        "body": """
        <p><strong>Central Limit Theorem (CLT):</strong> Let $X_1, X_2, \\ldots, X_n$ be independent and identically distributed (i.i.d.) random variables with mean $\\mu$ and variance $\\sigma^2$, both finite. Define the sample mean:</p>
        <p>$$\\bar{X}_n = \\frac{1}{n}(X_1 + X_2 + \\cdots + X_n)$$</p>

        <p>Then, as $n \\to \\infty$, the standardized sample mean:</p>
        <p>$$Z_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{\\sigma} \\xrightarrow{d} N(0, 1)$$</p>

        <p>converges in distribution to a standard normal variable. Equivalently:</p>
        <p>$$\\bar{X}_n \\approx N\\left(\\mu, \\frac{\\sigma^2}{n}\\right) \\quad \\text{for large } n$$</p>

        <div class='concept-box'>
        <p><strong>What does this mean?</strong></p>
        <ul>
        <li>The sample mean $\\bar{X}_n$ is approximately normally distributed</li>
        <li>Its center (mean) is at the true population mean $\\mu$</li>
        <li>Its spread (variance) decreases as $\\sigma^2/n$</li>
        <li>This holds for ANY distribution of the original $X_i$ (as long as mean and variance are finite)</li>
        </ul>
        </div>

        <p><strong>Remarkable fact:</strong> The CLT holds regardless of whether the population distribution is uniform, exponential, bimodal, skewed, or any other shape. The sample mean always becomes approximately normal for large $n$.</p>

        <p><strong>Convergence speed:</strong> Convergence is faster for symmetric, bell-shaped populations and slower for skewed distributions. Rule of thumb: $n \\geq 30$ often suffices, but this depends on the skewness of the original distribution.</p>
        """
    },
    {
        "title": "Proof Strategy Using Moment Generating Functions (MGF)",
        "body": """
        <p><strong>Proof idea:</strong> The CLT can be proven by showing that the MGF of the standardized sum converges to the MGF of the standard normal distribution. Since MGFs uniquely identify distributions, this convergence implies convergence in distribution.</p>

        <p><strong>Steps of the MGF proof:</strong></p>
        <ol>
        <li>Define $Z_n = \\sqrt{n}(\\bar{X}_n - \\mu) / \\sigma$ (standardized sample mean)</li>
        <li>Rewrite $Z_n$ in terms of standardized individual observations: $Z_n = \\frac{1}{\\sqrt{n}} \\sum_i Y_i$ where $Y_i = (X_i - \\mu)/\\sigma$</li>
        <li>Compute the MGF: $M_{Z_n}(t) = E[e^{tZ_n}] = E[e^{(t/\\sqrt{n}) \\sum_i Y_i}]$</li>
        <li>Use independence: $M_{Z_n}(t) = \\prod_i E[e^{(t/\\sqrt{n}) Y_i}]$</li>
        <li>Since all $Y_i$ are identically distributed: $M_{Z_n}(t) = [M_Y(t/\\sqrt{n})]^n$</li>
        <li>Take logarithm and expand: $\\ln M_Y(t/\\sqrt{n}) \\approx t^2/(2n) + \\text{higher order terms}$</li>
        <li>As $n \\to \\infty$: $[M_Y(t/\\sqrt{n})]^n \\to e^{t^2/2}$ (MGF of $N(0, 1)$)</li>
        </ol>

        <div class='worked-example'>
        <p><strong>Intuition for step 6:</strong> By Taylor expansion, if $Y$ has mean 0 and variance 1:</p>
        <pre class='code-block'>$M_Y(s) = E[e^{sY}] = 1 + sE[Y] + \\frac{s^2}{2}E[Y^2] + O(s^3)$
$= 1 + 0 + \\frac{s^2}{2} \\cdot 1 + O(s^3)$
$= 1 + \\frac{s^2}{2} + O(s^3)$</pre>
        <p>So $M_Y(t/\\sqrt{n}) \\approx 1 + \\frac{t^2}{2n} + O(1/n^{3/2})$</p>
        </div>

        <p><strong>Why this matters:</strong> The MGF proof is rigorous and works for any distribution with finite variance. It shows that the only thing that matters is the mean and variance—the entire shape of the population distribution "washes out" in the limit.</p>
        """
    },
    {
        "title": "Conditions for the CLT and When It Fails",
        "body": """
        <p><strong>Requirements for CLT:</strong></p>
        <ol>
        <li><strong>Independence:</strong> The observations $X_1, X_2, \\ldots, X_n$ must be independent (or weakly dependent under additional conditions).</li>
        <li><strong>Identical distribution:</strong> All $X_i$ must have the same distribution.</li>
        <li><strong>Finite mean and variance:</strong> $E[X_i] = \\mu$ and $\\text{Var}(X_i) = \\sigma^2 < \\infty$ must both exist.</li>
        </ol>

        <p><strong>Extensions of the CLT:</strong></p>
        <ul>
        <li><strong>Lindeberg CLT:</strong> Allows weakly dependent data under the Lindeberg condition</li>
        <li><strong>Multivariate CLT:</strong> For random vectors, the sample mean vector converges to a multivariate normal distribution</li>
        <li><strong>Lyapunov CLT:</strong> Allows non-identically distributed data under a growth condition on third moments</li>
        <li><strong>Berry-Esseen Theorem:</strong> Quantifies convergence rate: $|P(Z_n \\leq z) - \\Phi(z)| \\leq \\frac{C \\cdot E[|Y_1|^3]}{\\sqrt{n}}$</li>
        </ul>

        <div class='warning-box'>
        <p><strong>When the CLT fails:</strong></p>
        <ul>
        <li><strong>Heavy tails (infinite variance):</strong> E.g., Cauchy distribution. The sample mean doesn't converge to anything.</li>
        <li><strong>Strong dependence:</strong> Time series data with high autocorrelation. Use time series methods instead.</li>
        <li><strong>Non-identical distributions:</strong> Data from different populations. CLT can fail unless distributions are similar.</li>
        <li><strong>Extreme outliers:</strong> A few very large values can violate the finite variance assumption in practice.</li>
        </ul>
        </div>

        <p><strong>Practical implication:</strong> Before using normal approximations, verify that your data is approximately i.i.d. from a single population with finite variance. For real data with outliers, use robust methods or bootstrap.</p>
        """
    }
]
