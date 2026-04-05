TITLE = "Type I and Type II Errors, and Power of a Test"

SECTIONS = [
    {
        "title": "Understanding Type I and Type II Errors",
        "body": """
<div class="concept-box">
<h3>The Error Decision Table</h3>
</div>

<table style="width:100%; border-collapse:collapse;">
<tr style="border: 1px solid">
<th style="border: 1px solid; padding: 12px; text-align: left;"><strong>Decision</strong></th>
<th style="border: 1px solid; padding: 12px; text-align: left;"><strong>H₀ is True</strong></th>
<th style="border: 1px solid; padding: 12px; text-align: left;"><strong>H₀ is False</strong></th>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 12px;"><strong>Reject H₀</strong></td>
<td style="border: 1px solid; padding: 12px"><strong>Type I Error</strong> (prob = α)<br/>False Positive</td>
<td style="border: 1px solid; padding: 12px"><strong>Correct ✓</strong><br/>True Positive</td>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 12px;"><strong>Fail to Reject H₀</strong></td>
<td style="border: 1px solid; padding: 12px"><strong>Correct ✓</strong><br/>True Negative</td>
<td style="border: 1px solid; padding: 12px"><strong>Type II Error</strong> (prob = β)<br/>False Negative</td>
</tr>
</table>

<h3>Type I Error (α)</h3>
<p><strong>Definition:</strong> Rejecting H₀ when it's actually true.</p>
<p><strong>Also called:</strong> "False positive" or "false alarm"</p>
<p><strong>Probability:</strong> P(Type I error) = α (the significance level we set)</p>

<h3>Type II Error (β)</h3>
<p><strong>Definition:</strong> Failing to reject H₀ when it's actually false.</p>
<p><strong>Also called:</strong> "False negative" or "missed detection"</p>
<p><strong>Probability:</strong> P(Type II error) = β (determined by sample size, effect size, and α)</p>

<div class="worked-example">
<h4>Example: Error Types in Medical Testing</h4>
<p>Testing a new drug: H₀: drug has no effect vs H₁: drug works</p>
<ul>
<li><strong>Type I error:</strong> Conclude the drug works when it doesn't. <em>Dangerous—false hope, wasted resources</em></li>
<li><strong>Type II error:</strong> Conclude the drug doesn't work when it does. <em>Unfortunate—miss an effective treatment</em></li>
</ul>
<p>In drug approval, we choose a stricter α (like 0.01) to minimize Type I error—the consequences of approving a bad drug are severe.</p>
</div>

<h3>The Trade-Off Between α and β</h3>
<p>We cannot minimize both Type I and Type II errors simultaneously. Reducing α (being stricter about rejecting H₀) increases β.</p>

<p><strong>How to balance?</strong> Consider the real-world costs:</p>
<ul>
<li><strong>High cost of Type I:</strong> Use small α (0.01, 0.001)</li>
<li><strong>High cost of Type II:</strong> Use larger α (0.10)</li>
<li><strong>Balanced cost:</strong> Use α = 0.05 (default)</li>
</ul>
"""
    },
    {
        "title": "Power of a Test",
        "body": """
<h3>What is Statistical Power?</h3>
<p>The <strong>power</strong> of a test is the probability of correctly rejecting H₀ when it's actually false:</p>
<p style="text-align: center; font-weight: bold;">Power = 1 - β = P(Reject H₀ | H₀ is False)</p>

<p><strong>Interpretation:</strong> Power is our ability to detect a true effect when it exists.</p>

<h3>Factors that Increase Power</h3>
<ul>
<li><strong>Larger significance level α:</strong> Easier to reject H₀ (but increases Type I error)</li>
<li><strong>Larger sample size n:</strong> More precise estimates, smaller standard error</li>
<li><strong>Larger effect size:</strong> Bigger difference between true parameter and H₀ value</li>
<li><strong>One-tailed test (vs two-tailed):</strong> All α concentrated in one direction</li>
<li><strong>Smaller population variance σ:</strong> Less noise in the data</li>
</ul>

<div class="success-box">
<p><strong>Standard target:</strong> Power = 0.80 is a common benchmark in study design, meaning an 80% chance of detecting a true effect.</p>
</div>

<div class="worked-example">
<h4>Example: Computing Power and β</h4>
<p>Testing H₀: μ = 100 vs H₁: μ = 105 (the true value), α = 0.05, σ = 10, n = 25</p>
<p><strong>Step 1:</strong> Find the critical value under H₀</p>
<p style="text-align: center;">c = 100 + 1.645(10/√25) = 100 + 1.645(2) = 103.29</p>

<p><strong>Step 2:</strong> Compute β = P(fail to reject H₀ | true mean = 105)</p>
<p style="text-align: center;">β = P(X̄ ≤ 103.29 | μ = 105)</p>
<p style="text-align: center;">= P(Z ≤ (103.29 - 105)/(10/5)) = P(Z ≤ -0.855) ≈ 0.196</p>

<p><strong>Step 3:</strong> Power = 1 - β = 1 - 0.196 = <strong>0.804</strong></p>
<p>We have about 80.4% power to detect this effect size.</p>
</div>

<h3>Sample Size Determination</h3>
<p>Before conducting a study, researchers often calculate the sample size needed to achieve desired power (usually 0.80).</p>

<p><strong>Key insight:</strong> As sample size increases, power increases and β decreases. This is why large studies are more likely to detect small but real effects.</p>

<div class="warning-box">
<p><strong>Caution:</strong> High power with huge samples can detect trivial effects. Always consider practical significance alongside statistical significance.</p>
</div>
"""
    }
]
