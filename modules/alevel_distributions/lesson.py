SECTIONS = [
    {
        "title": "Binomial Distribution: Bernoulli Trials and Probability",
        "body": """
<h3>Setting Up Binomial Experiments</h3>
<p>A <strong>Bernoulli trial</strong> is an experiment with two outcomes: success (probability p) or failure (probability 1-p).</p>

<p>A <strong>binomial experiment</strong> repeats n independent Bernoulli trials and counts X = number of successes.</p>

<p><strong>Conditions:</strong></p>
<ol>
<li>Fixed number n of trials</li>
<li>Each trial is independent</li>
<li>Two outcomes per trial (success/failure)</li>
<li>Probability p is constant across trials</li>
</ol>

<h3>Deriving the Binomial Probability Formula</h3>
<p>For X successes in n trials, we need exactly X successes and (n-X) failures.</p>

<p>Any specific sequence has probability p^X × (1-p)^(n-X)</p>

<p>The number of such sequences is nCX (choose which X of n trials are successes)</p>

<p style="text-align: center; font-weight: bold;">P(X = k) = nCk × p^k × (1-p)^(n-k)</p>

<div class="example-box">
<h4>Example 1: Binomial Probability</h4>
<p>A fair coin is flipped 5 times. Find P(exactly 2 heads)</p>
<p><strong>Solution:</strong> n = 5, k = 2, p = 0.5</p>
<p>P(X = 2) = 5C2 × (0.5)² × (0.5)³ = 10 × 0.25 × 0.125 = 0.3125</p>
</div>

<h3>Mean and Variance of Binomial Distribution</h3>
<p style="text-align: center; font-weight: bold;">E(X) = μ = np
<br>Var(X) = σ² = np(1-p)
<br>SD(X) = σ = √(np(1-p))</p>

<p><strong>Derivation (mean):</strong> X = X₁ + X₂ + ... + X_n where X_i are independent Bernoulli(p)</p>
<p>E(X) = E(X₁) + ... + E(X_n) = p + p + ... + p = np</p>

<div class="example-box">
<h4>Example 2: Mean and Variance</h4>
<p>In a binomial setting with n = 20, p = 0.3:</p>
<p>Mean: μ = 20 × 0.3 = 6
<br>Variance: σ² = 20 × 0.3 × 0.7 = 4.2
<br>SD: σ = √4.2 ≈ 2.05
</p>
</div>
"""
    },
    {
        "title": "Poisson Distribution: Rare Events in Time/Space",
        "body": """
<h3>Derivation from Binomial Limit</h3>
<p>The <strong>Poisson distribution</strong> arises when:</p>
<ul>
<li>Events occur randomly over time or space</li>
<li>Events are rare (small p)</li>
<li>We observe a long period/large area (large n)</li>
<li>Average rate λ = np stays constant</li>
</ul>

<p>Taking the limit of binomial as n → ∞ and p → 0 with np = λ:</p>
<p style="text-align: center; font-weight: bold;">P(X = k) = (λ^k × e^(-λ)) / k!</p>

<p>where λ is the average number of events in the interval.</p>

<h3>Parameters and Properties</h3>
<p style="text-align: center; font-weight: bold;">E(X) = λ
<br>Var(X) = λ
<br>SD(X) = √λ</p>

<p><strong>Key fact:</strong> Mean and variance are equal!</p>

<div class="example-box">
<h4>Example 3: Poisson Probability</h4>
<p>Traffic accidents at an intersection average 2 per week. Find P(exactly 3 accidents in a week)</p>
<p><strong>Solution:</strong> λ = 2</p>
<p>P(X = 3) = (2³ × e⁻²) / 3! = (8 × e⁻²) / 6 ≈ 0.180</p>
</div>

<h3>When to Use Poisson vs. Binomial</h3>
<ul>
<li><strong>Binomial:</strong> Fixed number n of trials, clear success/failure</li>
<li><strong>Poisson:</strong> Events occur in continuous time/space at a constant rate</li>
</ul>

<p>If n is large and p is small (np ≈ λ moderate), Poisson approximates Binomial well.</p>

<div class="example-box">
<h4>Example 4: Poisson Approximation</h4>
<p>Out of 1000 people, the probability of a rare disease is 0.001. Find P(exactly 2 people have it)</p>
<p><strong>Solution:</strong> Binomial: n = 1000, p = 0.001, so np = 1</p>
<p>Poisson approximation: λ = 1</p>
<p>P(X = 2) = (1² × e⁻¹) / 2! = e⁻¹/2 ≈ 0.184</p>
</div>
"""
    },
    {
        "title": "Normal Distribution: The Bell Curve and Standardization",
        "body": """
<h3>Properties of the Normal Distribution</h3>
<p>The <strong>normal (Gaussian) distribution</strong> with mean μ and standard deviation σ is:</p>

<p style="text-align: center; font-weight: bold;">f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²))</p>

<p><strong>Properties:</strong></p>
<ul>
<li>Symmetric about the mean</li>
<li>68% of data within 1 SD (μ ± σ)</li>
<li>95% of data within 2 SDs (μ ± 2σ)</li>
<li>99.7% of data within 3 SDs (μ ± 3σ)</li>
<li>Bell-shaped curve</li>
</ul>

<h3>Standardization: Z-scores</h3>
<p>Convert any normal distribution to the <strong>standard normal</strong> (μ = 0, σ = 1) using:</p>
<p style="text-align: center; font-weight: bold;">Z = (X - μ) / σ</p>

<p>Then use Z-tables to find probabilities.</p>

<div class="example-box">
<h4>Example 5: Z-score Calculation</h4>
<p>Heights are normally distributed with μ = 170 cm, σ = 10 cm. Find P(height > 185)</p>
<p><strong>Solution:</strong> Z = (185 - 170) / 10 = 1.5</p>
<p>P(Z > 1.5) = 1 - P(Z ≤ 1.5) = 1 - 0.9332 = 0.0668 ≈ 6.68%</p>
</div>

<h3>Finding Percentiles</h3>
<p>For a given probability, find the corresponding value using inverse Z-table lookup.</p>

<div class="example-box">
<h4>Example 6: Inverse Z Problem</h4>
<p>IQ scores: μ = 100, σ = 15. Find the 90th percentile</p>
<p><strong>Solution:</strong> Find Z such that P(Z ≤ z) = 0.90</p>
<p>From tables: z ≈ 1.28</p>
<p>X = μ + z·σ = 100 + 1.28(15) = 119.2</p>
</div>

<h3>Approximations to Binomial and Poisson</h3>
<p>When n is large:</p>
<ul>
<li><strong>Binomial to Normal:</strong> If np > 5 and n(1-p) > 5, X ~ approx N(np, np(1-p))</li>
<li><strong>Poisson to Normal:</strong> If λ > 10, X ~ approx N(λ, λ)</li>
</ul>

<p><strong>Continuity correction:</strong> When approximating discrete with continuous, adjust boundaries by ±0.5.</p>

<div class="example-box">
<h4>Example 7: Normal Approximation to Binomial</h4>
<p>Binomial: n = 100, p = 0.4. Find P(X ≥ 40)</p>
<p><strong>Solution:</strong> np = 40, n(1-p) = 60 (both > 5, so normal approximation valid)</p>
<p>μ = 40, σ = √(100 × 0.4 × 0.6) = √24 ≈ 4.90</p>
<p>With continuity correction: P(X ≥ 40) ≈ P(X > 39.5)</p>
<p>Z = (39.5 - 40) / 4.90 = -0.102</p>
<p>P(Z > -0.102) ≈ 0.541</p>
</div>
"""
    },
    {
        "title": "Properties and Parameters of Distributions",
        "body": """
<h3>Cumulative Distribution Function (CDF)</h3>
<p>The CDF F(x) = P(X ≤ x) gives cumulative probabilities.</p>

<p><strong>For discrete distributions:</strong> F(k) = Σ P(X = i) for i ≤ k</p>
<p><strong>For continuous distributions:</strong> F(x) = ∫_{-∞}^x f(t)dt</p>

<p><strong>Properties:</strong></p>
<ul>
<li>0 ≤ F(x) ≤ 1</li>
<li>F is non-decreasing</li>
<li>P(a ≤ X ≤ b) = F(b) - F(a)</li>
</ul>

<h3>Moment-Generating Functions (Advanced)</h3>
<p>The MGF M_X(t) = E[e^{tX}] encodes all moments:</p>
<p>E(X^n) = M_X^{(n)}(0)</p>

<p><strong>Binomial MGF:</strong> M(t) = (1 - p + pe^t)^n</p>
<p><strong>Poisson MGF:</strong> M(t) = e^{λ(e^t - 1)}</p>
<p><strong>Normal MGF:</strong> M(t) = e^{μt + σ²t²/2}</p>

<h3>Skewness and Kurtosis</h3>
<p><strong>Skewness:</strong> Measures asymmetry. Positive skew (right tail), negative skew (left tail)</p>
<p><strong>Kurtosis:</strong> Measures tail behavior. High kurtosis = heavy tails and sharp peak</p>

<p><strong>Normal distribution:</strong> Skewness = 0, Kurtosis = 3 (or excess kurtosis = 0)</p>

<div class="example-box">
<h4>Example 8: Comparing Distributions</h4>
<p>Compare Binomial(n=10, p=0.5) vs Normal(μ=5, σ²=2.5):</p>
<p>Binomial mean: 10(0.5) = 5
<br>Binomial variance: 10(0.5)(0.5) = 2.5
<br>Both match, so normal approximation applies well
<br>Binomial is symmetric (p=0.5), so skewness ≈ 0 like normal
</p>
</div>

<h3>Central Limit Theorem (Conceptual)</h3>
<p>If X₁, X₂, ..., X_n are independent random variables with finite mean μ and variance σ², then:</p>
<p style="text-align: center; font-weight: bold;">S_n = X₁ + ... + X_n ~ approx N(nμ, nσ²) as n → ∞</p>

<p>This justifies using the normal distribution for sample means and sums, regardless of the underlying distribution (if n is large enough).</p>
"""
    },
    {
        "title": "Probability Calculations and Application",
        "body": """
<h3>Using Distribution Tables</h3>

<p><strong>Binomial tables:</strong> Look up P(X ≤ k) for given n and p</p>
<p><strong>Z-tables (Normal):</strong> Look up P(Z ≤ z) for standard normal</p>
<p><strong>Poisson tables:</strong> Look up P(X ≤ k) for given λ</p>

<p><strong>Example table usage:</strong> For P(X ≥ k), use 1 - P(X ≤ k-1)</p>

<div class="example-box">
<h4>Example 9: Table Look-up</h4>
<p>From a Poisson table with λ = 3: Find P(X ≥ 2)</p>
<p><strong>Solution:</strong> P(X ≥ 2) = 1 - P(X ≤ 1) = 1 - [P(X=0) + P(X=1)]</p>
<p>From table: P(X ≤ 1) = 0.199</p>
<p>So P(X ≥ 2) = 1 - 0.199 = 0.801</p>
</div>

<h3>Real-World Applications</h3>

<div class="example-box">
<h4>Example 10: Combined Application</h4>
<p>A factory produces items; 2% are defective. In a batch of 150:</p>
<p>(a) Using Binomial: P(X = 3) where X = number defective</p>
<p>(b) Using Poisson approximation: λ = 150(0.02) = 3</p>
<p>(c) Using Normal approximation: μ = 3, σ = √(150 × 0.02 × 0.98) ≈ 1.72</p>
<p>All three methods give similar results, with Poisson/Normal being simpler for calculation</p>
</div>

<h3>Sampling Distributions</h3>
<p>When we take a sample and compute statistics (like sample mean X̄):</p>

<p>If X ~ N(μ, σ²), then sample mean X̄ ~ N(μ, σ²/n)</p>

<p>This allows us to make inferences about the population from sample data, forming the basis for hypothesis testing and confidence intervals.</p>
"""
    }
]
