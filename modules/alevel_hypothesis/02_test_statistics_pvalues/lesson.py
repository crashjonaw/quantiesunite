TITLE = "Test Statistics and P-Values"

SECTIONS = [
    {
        "title": "P-Values: Definition and Interpretation",
        "body": """
<div class="concept-box">
<h3>What is a P-Value?</h3>
<p>The <strong>p-value</strong> is the probability of observing a test statistic as extreme as (or more extreme than) the one computed from our sample, assuming H₀ is true.</p>
</div>

<h3>P-Value Interpretation</h3>
<p>A <strong>small p-value</strong> provides strong evidence against H₀. It tells us the data would be unlikely if the null hypothesis were true.</p>
<p><strong>Decision Rule:</strong> Reject H₀ if p-value < α</p>

<div class="warning-box">
<h4>Common Misinterpretations (Avoid These!)</h4>
<ul>
<li><strong>❌ NOT:</strong> "p-value is the probability H₀ is true"</li>
<li><strong>❌ NOT:</strong> "If p > α, then H₀ is true"</li>
<li><strong>✓ CORRECT:</strong> "Given H₀ is true, p-value is P(data as extreme as observed)"</li>
<li><strong>✓ CORRECT:</strong> "If p < α, the data are inconsistent with H₀"</li>
</ul>
</div>

<h3>Computing P-Values for Z-Tests</h3>
<p><strong>One-tailed right (H₁: μ > μ₀):</strong></p>
<p style="text-align: center;">p-value = P(Z > z_obs)</p>

<p><strong>One-tailed left (H₁: μ < μ₀):</strong></p>
<p style="text-align: center;">p-value = P(Z < z_obs)</p>

<p><strong>Two-tailed (H₁: μ ≠ μ₀):</strong></p>
<p style="text-align: center;">p-value = 2 × P(Z > |z_obs|)</p>

<div class="worked-example">
<h4>Example: P-Value Calculation</h4>
<p>A sample of 36 students has mean test score X̄ = 78. Population σ = 12, testing μ₀ = 75 vs H₁: μ > 75.</p>
<p style="text-align: center;">Z = (78 - 75) / (12/√36) = 3 / 2 = 1.5</p>
<p>p-value = P(Z > 1.5) = 1 - Φ(1.5) ≈ 1 - 0.933 = 0.067</p>
<p>At α = 0.05: 0.067 > 0.05, so <strong>fail to reject H₀</strong></p>
<p>At α = 0.10: 0.067 < 0.10, so <strong>reject H₀</strong></p>
</div>
"""
    },
    {
        "title": "Statistical Significance vs Practical Significance",
        "body": """
<h3>The Importance of Effect Size</h3>
<p>A small p-value indicates statistical significance, but doesn't necessarily imply practical importance.</p>

<p>With large sample sizes, even tiny differences from the null hypothesis can be statistically significant while remaining irrelevant in practice.</p>

<div class="worked-example">
<h4>Example: When Statistical Significance Misleads</h4>
<p>A large study (n = 10,000) shows an average weight increase of 0.1 kg with p-value = 0.02 < 0.05.</p>
<p><strong>Statistically significant?</strong> Yes.</p>
<p><strong>Practically significant?</strong> Questionable—a 100-gram change might be negligible in many contexts.</p>
<p><strong>Best practice:</strong> Report both the p-value AND the effect size (mean difference, confidence interval).</p>
</div>

<h3>P-Value and Sample Size Relationship</h3>
<p>Larger sample sizes make it easier to detect small differences. This is why:</p>
<ul>
<li>Huge datasets can find statistical significance in trivial effects</li>
<li>We should always consider practical significance alongside p-values</li>
<li>Effect size measures (like Cohen's d) complement p-value reporting</li>
</ul>

<div class="success-box">
<p><strong>Summary:</strong> P-values tell us IF there's evidence of an effect, but effect size tells us HOW BIG that effect is. Both are essential for good statistical reporting.</p>
</div>
"""
    }
]
