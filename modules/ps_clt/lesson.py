SECTIONS = [
    {
        "title": "Statement of the Central Limit Theorem",
        "body": """
        <p><strong>Central Limit Theorem (CLT):</strong> Let X₁, X₂, ..., Xₙ be independent and identically distributed (i.i.d.) random variables with mean μ and variance σ², both finite. Define the sample mean:</p>
        <pre class='code-block'>X̄ₙ = (1/n)(X₁ + X₂ + ... + Xₙ)</pre>

        <p>Then, as n → ∞:</p>
        <pre class='code-block'>Z_n = √n(X̄ₙ - μ) / σ →ᵈ N(0, 1)  (converges in distribution to standard normal)</pre>

        <p>Equivalently:</p>
        <pre class='code-block'>X̄ₙ ≈ N(μ, σ²/n)  for large n</pre>

        <p><strong>Remarkable fact:</strong> The CLT holds for ANY distribution of the Xᵢ with finite mean and variance, not just normal distributions!</p>

        <p><strong>Convergence speed:</strong> Convergence is faster for symmetric distributions and slower for skewed ones. Rule of thumb: n ≥ 30 often suffices for reasonable approximation (varies by distribution).</p>

        <p><strong>Implications:</strong></p>
        <ul>
        <li>Sample means are approximately normal (large sample property)</li>
        <li>Confidence intervals can be constructed using normal quantiles</li>
        <li>Hypothesis tests use normal/t distributions for inference</li>
        <li>Error distributions in regression are approximately normal</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: CLT with uniform distribution</strong></p>
        <pre class='code-block'>X₁, X₂, ..., X₁₀₀ ~ Uniform(0, 1) independently
μ = 0.5, σ² = 1/12, σ ≈ 0.289

Sample mean X̄₁₀₀ has approximately N(0.5, (1/12)/100) = N(0.5, 0.0001)
SD of X̄₁₀₀ ≈ 0.0289

By CLT, P(X̄₁₀₀ < 0.48) ≈ Φ((0.48 - 0.5) / 0.0289) = Φ(-0.692) ≈ 0.244</pre>

        <p><strong>Example: CLT with exponential distribution</strong></p>
        <pre class='code-block'>X₁, X₂, ..., Xₙ ~ Exponential(1) independently
μ = 1, σ² = 1

For large n, X̄ₙ ≈ N(1, 1/n)

With n = 100: X̄₁₀₀ ≈ N(1, 0.01), so SD ≈ 0.1
P(0.9 < X̄₁₀₀ < 1.1) ≈ Φ(1) - Φ(-1) ≈ 0.683 (68% within 1 SD)</pre>
        </div>

        <p><strong>Why the CLT works:</strong> Intuitively, averaging many independent random quantities smooths out individual variation and produces a stable, bell-shaped distribution. This averaging effect is universal across distributions.</p>
        """
    },
    {
        "title": "Proof Sketch and Conditions for Validity",
        "body": """
        <p><strong>Proof strategy using MGF:</strong> The CLT can be proven by showing that the MGF of the standardized sum converges to the MGF of N(0, 1):</p>

        <pre class='code-block'>M_{Z_n}(t) = E[e^(t·Z_n)] → e^(t²/2)  as n → ∞</pre>

        <p>Since MGFs uniquely identify distributions, this convergence implies convergence in distribution to the normal.</p>

        <p><strong>Conditions for CLT:</strong></p>
        <ol>
        <li><strong>Independence:</strong> Xᵢ must be independent</li>
        <li><strong>Identical distribution:</strong> Xᵢ must be i.i.d.</li>
        <li><strong>Finite mean and variance:</strong> E[Xᵢ] = μ and Var(Xᵢ) = σ² < ∞</li>
        </ol>

        <p><strong>Extensions and refinements:</strong></p>
        <ul>
        <li><strong>Lindeberg CLT:</strong> Allows weakly dependent data under additional conditions</li>
        <li><strong>Multivariate CLT:</strong> For random vectors, the sample mean vector converges to multivariate normal</li>
        <li><strong>Berry-Esseen Theorem:</strong> Quantifies the rate of convergence: |P(Z_n ≤ z) - Φ(z)| ≤ constant · E[|X₁|³] / (n^(1/2)σ³)</li>
        </ul>

        <p><strong>When CLT fails:</strong></p>
        <ul>
        <li><strong>Heavy tails:</strong> If variance is infinite (e.g., Cauchy distribution), CLT doesn't apply; other limit theorems may</li>
        <li><strong>Strong dependence:</strong> If observations are highly correlated, standard CLT fails (need time series methods)</li>
        <li><strong>Non-identical distributions:</strong> CLT can sometimes still hold with additional conditions (Lyapunov CLT)</li>
        </ul>

        <p><strong>Practical implications:</strong> When constructing confidence intervals or hypothesis tests, check that your sample size is large enough and data doesn't have extreme outliers or strong dependence.</p>

        <div class='example-box'>
        <p><strong>Example: When sample size matters</strong></p>
        <pre class='code-block'>Binomial(10, 0.1): p = 0.1 (rare event)
Normal approximation: ≈ N(1, 0.9)
For small n, the discrete distribution is quite different from normal.
Rule of thumb: np and n(1-p) both ≥ 5 for reasonable approximation.
Here np = 1 < 5, so n = 10 is borderline.

Binomial(100, 0.1): np = 10, n(1-p) = 90
Normal approximation: ≈ N(10, 9), SD = 3
Much better approximation at n = 100.</pre>
        </div>
        """
    },
    {
        "title": "Confidence Intervals and Sample Size",
        "body": """
        <p><strong>Confidence Interval:</strong> Given a sample X₁, ..., Xₙ, an estimate of the population mean μ with confidence level 1 - α (typically 95%):</p>
        <pre class='code-block'>X̄ ± z_{α/2} · (σ / √n)  when σ is known

X̄ ± t_{α/2, n-1} · (S / √n)  when σ is unknown (S is sample SD)</pre>

        <p><strong>Interpretation:</strong> If we repeat the sampling many times, approximately (1 - α)·100% of the constructed intervals will contain the true μ.</p>

        <p><strong>Key quantities:</strong></p>
        <ul>
        <li>z_{α/2}: critical value from standard normal (e.g., z_{0.025} ≈ 1.96 for 95% CI)</li>
        <li>t_{α/2, n-1}: critical value from t-distribution (larger than z for small n)</li>
        <li>Margin of error: E = z_{α/2} · σ / √n</li>
        </ul>

        <p><strong>Sample size for desired margin of error:</strong> To ensure margin of error ≤ E:</p>
        <pre class='code-block'>n ≥ (z_{α/2} · σ / E)²</pre>

        <p><strong>Factors affecting CI width:</strong></p>
        <ul>
        <li><strong>Larger n → narrower CI</strong> (inverse square root relationship)</li>
        <li><strong>Higher confidence (1-α) → wider CI</strong> (larger z critical value)</li>
        <li><strong>Larger σ → wider CI</strong> (more variability in data)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: CI for mean with known σ</strong></p>
        <pre class='code-block'>Sample: n = 100, X̄ = 50.5, σ = 2 (known), α = 0.05
95% CI: 50.5 ± 1.96 · (2 / √100) = 50.5 ± 1.96 · 0.2 = 50.5 ± 0.392
CI: (50.108, 50.892)</pre>

        <p><strong>Example: Required sample size</strong></p>
        <pre class='code-block'>Want 95% CI with margin of error E = 0.5
Population σ ≈ 2 (estimated from pilot study)
n ≥ (1.96 · 2 / 0.5)² = (7.84)² ≈ 61.5
Need at least n = 62 observations</pre>
        </div>

        <p><strong>t-distribution vs Normal:</strong> When σ is unknown and estimated by sample SD, use t-distribution (has heavier tails). For large n, t and normal are similar.</p>
        """
    },
    {
        "title": "Practical Applications and Limitations",
        "body": """
        <p><strong>Applications of CLT:</strong></p>

        <p><strong>1. Quality Control:</strong> Monitor process mean via sample means. If sample mean falls outside control limits, investigate the process.</p>

        <p><strong>2. Polling and Surveys:</strong> Estimate population proportion p from sample. For large n, sample proportion p̂ ≈ N(p, p(1-p)/n).</p>

        <p><strong>3. Drug Trials:</strong> Compare treatment vs. control using sample means. CLT justifies normal-based inference.</p>

        <p><strong>4. Regression Analysis:</strong> With many observations, residuals are approximately normal. Enables valid inference on slopes.</p>

        <p><strong>Limitations and pitfalls:</strong></p>

        <ul>
        <li><strong>Small samples:</strong> Convergence to normal may be slow. Rule of thumb n ≥ 30, but depends on skewness.</li>
        <li><strong>Outliers:</strong> Extreme values can skew the distribution and inflate the variance. Robust methods preferred.</li>
        <li><strong>Dependence:</strong> If data are correlated (time series), standard CLT doesn't apply. Need adjusted methods.</li>
        <li><strong>Assumption of identical distribution:</strong> If data are from different populations, CLT fails.</li>
        <li><strong>"MSE is a myth":</strong> Even with n = 300, data from a heavy-tailed distribution may not look normal.</li>
        </ul>

        <p><strong>Checking CLT assumptions:</strong></p>
        <ul>
        <li>Q-Q plot: Visual check of normality</li>
        <li>Histogram: Look for extreme skewness or bimodality</li>
        <li>Outlier detection: Identify extreme values that might violate finite variance</li>
        <li>Autocorrelation: For time series, check independence</li>
        </ul>

        <p><strong>When to use bootstrap instead:</strong> If CLT assumptions are violated (small n, heavy tails, dependence), bootstrap resampling provides valid CIs without normality assumption.</p>

        <div class='example-box'>
        <p><strong>Example: CLT in regression</strong></p>
        <pre class='code-block'>Fit y = β₀ + β₁x + ε, where ε ~ some distribution
With large n, the OLS estimator β̂₁ ≈ N(β₁, Var(β̂₁))
Even if ε is not normal, by CLT the estimator is approximately normal.
This justifies using t-tests and confidence intervals for slope.</pre>

        <p><strong>Example: Polling accuracy</strong></p>
        <pre class='code-block'>Poll n = 1,000 voters for preference (p = true support)
Sample proportion p̂ ≈ N(p, p(1-p)/1000)
If p = 0.5: SD(p̂) = √(0.25/1000) ≈ 0.016 = 1.6%
95% CI: p̂ ± 1.96 · 1.6% ≈ p̂ ± 3.1%
(Explains why polls have ~3% margin of error for 1,000 respondents)</pre>
        </div>

        <p><strong>Modern perspective:</strong> CLT is a cornerstone of frequentist inference but not the final word. Bayesian methods, permutation tests, and bootstrap provide alternatives that may be more robust or appropriate in specific contexts.</p>
        """
    }
]
