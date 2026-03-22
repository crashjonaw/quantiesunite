SECTIONS = [
    {
        "title": "Hypothesis Testing Framework: Null and Alternative",
        "body": """
<h3>The Hypothesis Testing Process</h3>
<p>Hypothesis testing uses sample data to decide whether to reject a claim about the population parameter.</p>

<h3>Null and Alternative Hypotheses</h3>
<p><strong>Null hypothesis (H₀):</strong> The "default" claim, usually stating no effect or no difference. Always written with equality (=, ≤, or ≥).</p>
<p><strong>Alternative hypothesis (H₁ or H_a):</strong> The claim we're testing for. Usually states there IS an effect or difference (≠, <, or >).</p>

<div class="example-box">
<h4>Example 1: Setting Up Hypotheses</h4>
<p>A manufacturer claims their light bulbs last 1000 hours on average.</p>
<p>H₀: μ = 1000 (the claim)</p>
<p>H₁: μ ≠ 1000 (two-tailed: testing if different)</p>
<p>OR</p>
<p>H₁: μ < 1000 (one-tailed: testing if shorter lifespan)</p>
</div>

<h3>Test Statistics and Significance Level</h3>
<p>The <strong>test statistic</strong> is a function of sample data that measures evidence against H₀.</p>

<p>The <strong>significance level</strong> α is the probability of rejecting H₀ when it's actually true (Type I error).</p>

<p><strong>Common values:</strong> α = 0.05, 0.01, 0.10</p>

<h3>Decision Rule</h3>
<p>Compare the test statistic to a critical value (determined by α) or compute a p-value:</p>
<ul>
<li>If p-value < α, reject H₀ (evidence supports H₁)</li>
<li>If p-value ≥ α, fail to reject H₀ (insufficient evidence)</li>
</ul>

<p><strong>Note:</strong> "Fail to reject" doesn't mean "accept H₀"; it means we don't have enough evidence against it.</p>
"""
    },
    {
        "title": "Z-Test for Population Mean: Known Variance",
        "body": """
<h3>Assumptions</h3>
<p>The Z-test applies when:</p>
<ul>
<li>Population is normally distributed OR sample size n ≥ 30 (by CLT)</li>
<li>Population standard deviation σ is known</li>
<li>Sample is random</li>
</ul>

<h3>Test Statistic Formula</h3>
<p>For a sample of size n with mean X̄ and population mean μ₀ (from H₀):</p>
<p style="text-align: center; font-weight: bold;">Z = (X̄ - μ₀) / (σ/√n)</p>

<p>Under H₀, Z follows a standard normal distribution.</p>

<div class="example-box">
<h4>Example 2: Z-Test Calculation</h4>
<p>A random sample of 36 students has mean test score 78. Population σ = 12, and we're testing μ₀ = 75 vs H₁: μ > 75 at α = 0.05</p>
<p><strong>Solution:</strong></p>
<p>Z = (78 - 75) / (12/√36) = 3 / 2 = 1.5</p>
<p>For one-tailed test (μ > 75): critical value Z₀.₀₅ = 1.645</p>
<p>Since 1.5 < 1.645, fail to reject H₀</p>
<p>Alternatively, p-value = P(Z > 1.5) ≈ 0.067 > 0.05, so fail to reject</p>
</div>

<h3>One-Tailed vs Two-Tailed Tests</h3>
<p><strong>Two-tailed (H₁: μ ≠ μ₀):</strong> Critical region in both tails. Split α equally: α/2 in each tail.</p>
<p><strong>One-tailed (H₁: μ > μ₀ or μ < μ₀):</strong> Critical region in one tail. All α in one direction.</p>

<p><strong>Example critical values at α = 0.05:</strong></p>
<ul>
<li>Two-tailed: ±1.96</li>
<li>One-tailed (right): 1.645</li>
<li>One-tailed (left): -1.645</li>
</ul>

<div class="example-box">
<h4>Example 3: Two-Tailed Z-Test</h4>
<p>Testing μ = 100 vs μ ≠ 100 with α = 0.01, n = 50, X̄ = 105, σ = 10</p>
<p><strong>Solution:</strong></p>
<p>Z = (105 - 100) / (10/√50) = 5 / 1.414 ≈ 3.54</p>
<p>Critical values: ±2.576</p>
<p>Since |3.54| > 2.576, reject H₀ at 0.01 level</p>
<p>Strong evidence that μ ≠ 100</p>
</div>
"""
    },
    {
        "title": "Type I and Type II Errors, and Power of a Test",
        "body": """
<h3>Error Types</h3>

<table style="width:100%; border-collapse:collapse;">
<tr style="border: 1px solid black;">
<th style="border: 1px solid black;">Decision</th>
<th style="border: 1px solid black;">H₀ is true</th>
<th style="border: 1px solid black;">H₀ is false</th>
</tr>
<tr style="border: 1px solid black;">
<td style="border: 1px solid black;">Reject H₀</td>
<td style="border: 1px solid black;"><strong>Type I Error</strong> (prob α)</td>
<td style="border: 1px solid black;">Correct ✓</td>
</tr>
<tr style="border: 1px solid black;">
<td style="border: 1px solid black;">Fail to reject H₀</td>
<td style="border: 1px solid black;">Correct ✓</td>
<td style="border: 1px solid black;"><strong>Type II Error</strong> (prob β)</td>
</tr>
</table>

<p><strong>Type I Error (α):</strong> Reject H₀ when it's true. Called "false positive".</p>
<p><strong>Type II Error (β):</strong> Fail to reject H₀ when it's false. Called "false negative".</p>

<h3>Power of a Test</h3>
<p>The <strong>power</strong> of a test is the probability of correctly rejecting H₀ when it's false:</p>
<p style="text-align: center; font-weight: bold;">Power = 1 - β = P(reject H₀ | H₀ is false)</p>

<p><strong>Relationship:</strong></p>
<ul>
<li>Increasing α increases power (but also increases Type I error)</li>
<li>Increasing sample size n increases power</li>
<li>Effect size (how far true parameter is from H₀) increases power</li>
</ul>

<div class="example-box">
<h4>Example 4: Error Probabilities</h4>
<p>In a drug trial, H₀: drug has no effect vs H₁: drug works</p>
<p>Type I error: Conclude drug works when it doesn't (dangerous—false hope)</p>
<p>Type II error: Conclude drug doesn't work when it does (missed opportunity)</p>
<p>In this context, we might prefer small α (strict evidence for approval)</p>
</div>

<h3>Relationship Between α, β, and Sample Size</h3>
<p>Given a specific alternative μ₁ (true parameter value under H₁):</p>

<p>The critical value c satisfies P(Z > c) = α (for one-tailed right test)</p>
<p>β = P(fail to reject H₀ | true param is μ₁) = P(Z ≤ c when sampling from μ₁)</p>

<p>Decreasing α increases c, which increases β. We trade off Type I for Type II.</p>

<div class="example-box">
<h4>Example 5: Computing β</h4>
<p>H₀: μ = 100 vs H₁: μ = 105 (true value), α = 0.05, σ = 10, n = 25</p>
<p>Critical value: c = 100 + 1.645(10/5) = 103.29</p>
<p>β = P(X̄ ≤ 103.29 | true mean = 105) = P(Z ≤ (103.29-105)/(10/5)) = P(Z ≤ -0.855) ≈ 0.196</p>
<p>Power = 1 - 0.196 = 0.804</p>
</div>
"""
    },
    {
        "title": "P-Values: Interpretation and Computation",
        "body": """
<h3>Definition of P-Value</h3>
<p>The <strong>p-value</strong> is the probability of observing a test statistic as extreme as (or more extreme than) the one computed, assuming H₀ is true.</p>

<p><strong>Interpretation:</strong> A small p-value provides strong evidence against H₀.</p>

<p><strong>Decision:</strong> Reject H₀ if p-value < α</p>

<h3>Computing P-Values for Z-Tests</h3>

<p><strong>One-tailed right (H₁: μ > μ₀):</strong> p-value = P(Z > z_obs)</p>
<p><strong>One-tailed left (H₁: μ < μ₀):</strong> p-value = P(Z < z_obs)</p>
<p><strong>Two-tailed (H₁: μ ≠ μ₀):</strong> p-value = 2 × P(Z > |z_obs|)</p>

<div class="example-box">
<h4>Example 6: P-Value Calculation</h4>
<p>From Example 2: Z = 1.5, one-tailed test (right)</p>
<p>p-value = P(Z > 1.5) = 1 - Φ(1.5) ≈ 1 - 0.933 = 0.067</p>
<p>At α = 0.05: 0.067 > 0.05, so fail to reject</p>
<p>At α = 0.10: 0.067 < 0.10, so reject</p>
</div>

<h3>Misinterpretations to Avoid</h3>
<ul>
<li><strong>NOT:</strong> "p-value is the probability H₀ is true" ✗</li>
<li><strong>NOT:</strong> "If p > α, H₀ is true" ✗</li>
<li><strong>CORRECT:</strong> "Given H₀ is true, p-value is P(data as extreme as observed)" ✓</li>
<li><strong>CORRECT:</strong> "If p < α, the data are inconsistent with H₀" ✓</li>
</ul>

<h3>Significance vs Practical Significance</h3>
<p>A small p-value indicates statistical significance, but doesn't necessarily imply practical importance.</p>

<div class="example-box">
<h4>Example 7: Statistical vs Practical Significance</h4>
<p>Large sample (n = 10,000) shows average weight increase of 0.1 kg, with p-value = 0.02 < 0.05</p>
<p>Statistically significant difference, but a 100-gram change might be practically negligible</p>
<p>Report both p-value and effect size (mean difference, confidence interval)</p>
</div>
"""
    },
    {
        "title": "Confidence Intervals: Interval Estimation",
        "body": """
<h3>Confidence Interval Concept</h3>
<p>A <strong>confidence interval (CI)</strong> is a range of values likely to contain the true population parameter.</p>

<p><strong>95% CI:</strong> If we repeat the study many times and compute a CI each time, about 95% of these intervals will contain the true parameter.</p>

<p><strong>NOT:</strong> "There's 95% probability the parameter is in this interval" (the parameter is fixed, we're uncertain about it)</p>

<h3>Z-Confidence Interval for Mean (Known σ)</h3>
<p style="text-align: center; font-weight: bold;">CI = X̄ ± z_{α/2} × (σ/√n)</p>

<p>where z_{α/2} is the critical z-value for the desired confidence level.</p>

<p><strong>Common critical values:</strong></p>
<ul>
<li>90% confidence: z₀.₀₅ = 1.645</li>
<li>95% confidence: z₀.₀₂₅ = 1.96</li>
<li>99% confidence: z₀.₀₀₅ = 2.576</li>
</ul>

<div class="example-box">
<h4>Example 8: Computing Confidence Interval</h4>
<p>Sample of 50: X̄ = 82, σ = 10. Find 95% CI for μ</p>
<p><strong>Solution:</strong></p>
<p>Margin of error = 1.96 × (10/√50) = 1.96 × 1.414 ≈ 2.77</p>
<p>95% CI = 82 ± 2.77 = (79.23, 84.77)</p>
<p>We're 95% confident that the population mean is between 79.23 and 84.77</p>
</div>

<h3>Relationship Between Confidence Intervals and Hypothesis Tests</h3>
<p>A two-tailed hypothesis test at level α is equivalent to checking if the null value lies in the (1-α)×100% CI.</p>

<p>If μ₀ is NOT in the CI, reject H₀: μ = μ₀ at level α.</p>

<p>If μ₀ IS in the CI, fail to reject H₀.</p>

<div class="example-box">
<h4>Example 9: CI and Hypothesis Test Equivalence</h4>
<p>From Example 8: 95% CI = (79.23, 84.77)</p>
<p>Test H₀: μ = 80 vs H₁: μ ≠ 80 at α = 0.05</p>
<p>Since 80 ∈ (79.23, 84.77), fail to reject H₀</p>
<p>Test H₀: μ = 85 vs H₁: μ ≠ 85 at α = 0.05</p>
<p>Since 85 ∉ (79.23, 84.77), reject H₀</p>
</div>

<h3>Interpreting Confidence Level</h3>
<p>Higher confidence level (99% vs 95%) gives wider interval (more certainty but less precision).</p>
<p>Larger sample size narrows the interval (better precision).</p>
"""
    }
]
