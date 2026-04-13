TITLE = "Introduction to Hypothesis Testing"

SECTIONS = [
    {
        "title": "The Hypothesis Testing Process",
        "body": """
<div class="concept-box">
<h3>The Hypothesis Testing Framework</h3>
<p>Hypothesis testing uses sample data to decide whether to reject a claim about the population parameter. It's a systematic approach based on probability theory.</p>
</div>

<h3>Null and Alternative Hypotheses</h3>
<p><strong>Null hypothesis (\(H_0\)):</strong> The "default" claim, usually stating no effect or no difference. Always written with equality (=, ≤, or ≥).</p>
<p><strong>Alternative hypothesis (\(H_1\) or \(H_a\)):</strong> The claim we're testing for. Usually states there IS an effect or difference (≠, &lt;, or &gt;).</p>

<div class="worked-example">
<h4>Example 1: Setting Up Hypotheses</h4>
<p>A manufacturer claims their light bulbs last 1000 hours on average.</p>
<p><strong>\(H_0\): \(\\mu = 1000\)</strong> (the claim)</p>
<p><strong>\(H_1\): \(\\mu \\neq 1000\)</strong> (two-tailed: testing if different)</p>
<p>OR</p>
<p><strong>\(H_1\): \(\\mu < 1000\)</strong> (one-tailed: testing if shorter lifespan)</p>
</div>

<h3>Test Statistics and Significance Level</h3>
<p>The <strong>test statistic</strong> is a function of sample data that measures evidence against \(H_0\).</p>
<p>The <strong>significance level</strong> \(\\alpha\) (alpha) is the probability of rejecting \(H_0\) when it's actually true—this is the threshold we set before conducting the test.</p>
<p><strong>Common values:</strong> \(\\alpha = 0.05, 0.01, 0.10\)</p>

<h3>Decision Rule</h3>
<p>Compare the test statistic to a critical value (determined by \(\\alpha\)) or compute a p-value:</p>
<ul>
<li>If p-value &lt; \(\\alpha\), reject \(H_0\) (evidence supports \(H_1\))</li>
<li>If p-value ≥ \(\\alpha\), fail to reject \(H_0\) (insufficient evidence)</li>
</ul>

<div class="warning-box">
<p><strong>Important Note:</strong> "Fail to reject" doesn't mean "accept \(H_0\)"; it means we don't have enough evidence against it. The null hypothesis could still be false.</p>
</div>
"""
    },
    {
        "title": "One-Tailed vs Two-Tailed Tests",
        "body": """
<h3>Understanding Test Direction</h3>
<p>The form of the alternative hypothesis determines whether we conduct a one-tailed or two-tailed test.</p>

<p><strong>Two-tailed test (\(H_1\): \(\\mu \\neq \\mu_0\)):</strong> We're testing if the parameter differs in either direction. The critical region is split between both tails of the distribution.</p>

<p><strong>One-tailed test:</strong> We're testing if the parameter is greater than OR less than the null value, but not both.</p>
<ul>
<li><strong>Right-tailed (\(H_1\): \(\\mu > \\mu_0\)):</strong> Testing if parameter is greater. Critical region in the right tail.</li>
<li><strong>Left-tailed (\(H_1\): \(\\mu < \\mu_0\)):</strong> Testing if parameter is less. Critical region in the left tail.</li>
</ul>

<h3>Critical Values for Z-Tests at \(\\alpha = 0.05\)</h3>
<ul>
<li><strong>Two-tailed:</strong> ±1.96 (\(\\alpha/2 = 0.025\) in each tail)</li>
<li><strong>One-tailed (right):</strong> 1.645 (all \(\\alpha = 0.05\) in right tail)</li>
<li><strong>One-tailed (left):</strong> -1.645 (all \(\\alpha = 0.05\) in left tail)</li>
</ul>

<div class="worked-example">
<h4>Example: Two-Tailed Z-Test</h4>
<p>Testing \(H_0\): \(\\mu = 100\) vs \(H_1\): \(\\mu \\neq 100\) with \(\\alpha = 0.01\), \(n = 50\), \(\\bar{X} = 105\), \(\\sigma = 10\)</p>
<p><strong>Solution:</strong></p>
<p style="text-align: center;">\(Z = \\frac{105 - 100}{10/\\sqrt{50}} = \\frac{5}{1.414} \\approx 3.54\)</p>
<p>Critical values: ±2.576</p>
<p>Since |3.54| &gt; 2.576, we <strong>reject \(H_0\)</strong> at the 0.01 level.</p>
<p>Strong evidence that \(\\mu \\neq 100\)</p>
</div>
"""
    }
]
