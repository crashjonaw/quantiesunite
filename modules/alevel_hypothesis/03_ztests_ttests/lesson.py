TITLE = "Z-Tests and T-Tests"

SECTIONS = [
    {
        "title": "Z-Test for Population Mean: Known Variance",
        "body": """
<h3>When Do We Use the Z-Test?</h3>
<p>The Z-test applies when the following conditions are met:</p>
<ul>
<li>Population is normally distributed <strong>OR</strong> sample size \(n \geq 30\) (by Central Limit Theorem)</li>
<li>Population standard deviation \(\sigma\) is <strong>known</strong></li>
<li>Sample is random and independent</li>
</ul>

<h3>Z-Test Statistic Formula</h3>
<p>For a sample of size n with mean \(\bar{X}\) and population mean \(\mu_0\) (from \(H_0\)):</p>
<p style="text-align: center; font-weight: bold;">\(Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}\)</p>

<p>Under \(H_0\), Z follows a standard normal distribution \(N(0,1)\).</p>

<h3>Step-by-Step Z-Test Procedure</h3>
<ol>
<li><strong>State hypotheses:</strong> \(H_0\): \(\mu = \mu_0\) and choose \(H_1\) (one-tailed or two-tailed)</li>
<li><strong>Choose significance level:</strong> \(\alpha\) (typically 0.05 or 0.01)</li>
<li><strong>Calculate test statistic:</strong> \(Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}\)</li>
<li><strong>Find critical value(s):</strong> Based on \(\alpha\) and \(H_1\)</li>
<li><strong>Make decision:</strong> Reject \(H_0\) if |Z| exceeds the critical value (or use p-value approach)</li>
</ol>

<div class="worked-example">
<h4>Example: Z-Test with One-Tailed Alternative</h4>
<p>A student claims the average commute is longer than 25 minutes. Sample of 36 commuters: \(\bar{X} = 27.5\) minutes, \(\sigma = 6\) minutes. Test at \(\alpha = 0.05\).</p>
<p><strong>Hypotheses:</strong> \(H_0\): \(\mu = 25\) vs \(H_1\): \(\mu > 25\) (one-tailed)</p>
<p><strong>Test statistic:</strong></p>
<p style="text-align: center;">\(Z = \frac{27.5 - 25}{6/\sqrt{36}} = \frac{2.5}{1} = 2.5\)</p>
<p><strong>Critical value:</strong> \(z_{0.05} = 1.645\) (one-tailed right)</p>
<p><strong>Conclusion:</strong> Since 2.5 &gt; 1.645, <strong>reject \(H_0\)</strong>. There is sufficient evidence that the mean commute exceeds 25 minutes.</p>
</div>
"""
    },
    {
        "title": "T-Test: When Variance is Unknown",
        "body": """
<h3>Why We Need the T-Test</h3>
<p>In practice, we rarely know the population standard deviation \(\sigma\). When \(\sigma\) is unknown, we use the <strong>sample standard deviation s</strong> instead, which introduces additional uncertainty.</p>

<p>This uncertainty is captured by using the t-distribution instead of the standard normal distribution.</p>

<h3>T-Test Statistic Formula</h3>
<p>For a sample of size n with mean \(\bar{X}\), sample standard deviation s, and population mean \(\mu_0\) (from \(H_0\)):</p>
<p style="text-align: center; font-weight: bold;">\(t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}\)</p>

<p>Under \(H_0\), t follows a t-distribution with \(\text{df} = n - 1\) degrees of freedom.</p>

<h3>Properties of the T-Distribution</h3>
<ul>
<li>Symmetric and bell-shaped, like the normal distribution</li>
<li>Has heavier tails than the normal distribution (more uncertainty)</li>
<li>Critical values are larger than z-values (harder to reject \(H_0\))</li>
<li>Approaches the normal distribution as n increases (\(\text{df} \to \infty\))</li>
<li>Shape depends on degrees of freedom (\(\text{df} = n - 1\))</li>
</ul>

<div class="worked-example">
<h4>Example: One-Sample T-Test</h4>
<p>A quality control inspector tests if bottles contain 500 mL on average. Sample: \(n = 25\), \(\bar{X} = 498\) mL, \(s = 4\) mL. Test at \(\alpha = 0.05\).</p>
<p><strong>Hypotheses:</strong> \(H_0\): \(\mu = 500\) vs \(H_1\): \(\mu \neq 500\) (two-tailed)</p>
<p><strong>Test statistic:</strong></p>
<p style="text-align: center;">\(t = \frac{498 - 500}{4/\sqrt{25}} = \frac{-2}{0.8} = -2.5\)</p>
<p><strong>Degrees of freedom:</strong> \(\text{df} = 25 - 1 = 24\)</p>
<p><strong>Critical value:</strong> \(t_{0.025,\,24} \approx \pm 2.064\) (two-tailed)</p>
<p><strong>Conclusion:</strong> Since |-2.5| &gt; 2.064, <strong>reject \(H_0\)</strong>. There is significant evidence that the average volume differs from 500 mL.</p>
</div>

<h3>Z-Test vs T-Test: Quick Comparison</h3>
<table style="width:100%; border-collapse:collapse;">
<tr style="border: 1px solid;">
<th style="border: 1px solid; padding: 8px;"><strong>Feature</strong></th>
<th style="border: 1px solid; padding: 8px;"><strong>Z-Test</strong></th>
<th style="border: 1px solid; padding: 8px;"><strong>T-Test</strong></th>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 8px;">\(\sigma\) known?</td>
<td style="border: 1px solid; padding: 8px;">Yes</td>
<td style="border: 1px solid; padding: 8px;">No (use s)</td>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 8px;">Distribution</td>
<td style="border: 1px solid; padding: 8px;">\(N(0,1)\)</td>
<td style="border: 1px solid; padding: 8px;">t with df=n-1</td>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 8px;">Critical values</td>
<td style="border: 1px solid; padding: 8px;">Smaller (1.96 at \(\alpha=0.05\))</td>
<td style="border: 1px solid; padding: 8px;">Larger (2.064 at n=25, \(\alpha=0.05\))</td>
</tr>
<tr style="border: 1px solid;">
<td style="border: 1px solid; padding: 8px;">When to use</td>
<td style="border: 1px solid; padding: 8px;">Large n or known \(\sigma\)</td>
<td style="border: 1px solid; padding: 8px;">Small n, unknown \(\sigma\) (most practice)</td>
</tr>
</table>
"""
    }
]
