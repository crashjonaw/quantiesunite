TITLE = "Confidence Intervals: Interval Estimation"

SECTIONS = [
    {
        "title": "Confidence Interval Concept",
        "body": """
<div class="concept-box">
<h3>What is a Confidence Interval?</h3>
<p>A <strong>confidence interval (CI)</strong> is a range of values computed from sample data that is likely to contain the true population parameter.</p>
</div>

<h3>The 95% Confidence Interval Interpretation</h3>
<p>If we were to repeat the study many times and compute a 95% CI each time, approximately 95% of these intervals would contain the true population parameter.</p>

<div class="warning-box">
<h4>⚠️ Common Misunderstanding</h4>
<p><strong>❌ WRONG:</strong> "There's a 95% probability that the parameter is in this interval"</p>
<p><strong>✓ CORRECT:</strong> "About 95% of such intervals (from repeated sampling) would contain the parameter"</p>
<p>The parameter is fixed but unknown. Once we compute a specific interval, it either contains the parameter (100%) or it doesn't (0%).</p>
</div>

<h3>Confidence Level and Width Trade-Off</h3>
<ul>
<li><strong>Higher confidence level (99% vs 95%):</strong> Wider interval, more certainty</li>
<li><strong>Lower confidence level (90% vs 95%):</strong> Narrower interval, less certainty</li>
<li><strong>Larger sample size:</strong> Narrower interval for the same confidence level</li>
</ul>

<div class="worked-example">
<h4>Example: Interpreting Different Confidence Levels</h4>
<p>A pollster estimates the proportion of voters supporting a candidate.</p>
<ul>
<li><strong>90% CI:</strong> [0.45, 0.55] — Narrower, less confident</li>
<li><strong>95% CI:</strong> [0.44, 0.56] — Medium width, standard level</li>
<li><strong>99% CI:</strong> [0.42, 0.58] — Wider, very confident</li>
</ul>
<p>To be more confident the interval contains the true value, we must make the interval wider.</p>
</div>
"""
    },
    {
        "title": "Computing Confidence Intervals for the Mean",
        "body": """
<h3>Z-Confidence Interval (Known \(\sigma\))</h3>
<p style="text-align: center; font-weight: bold;">\(\text{CI} = \bar{X} \pm z_{\alpha/2} \times (\sigma/\sqrt{n})\)</p>

<p>where \(z_{\alpha/2}\) is the critical z-value for the desired confidence level.</p>

<h3>Critical Z-Values for Common Confidence Levels</h3>
<ul>
<li><strong>90% confidence:</strong> \(z_{0.05} = 1.645\)</li>
<li><strong>95% confidence:</strong> \(z_{0.025} = 1.96\)</li>
<li><strong>99% confidence:</strong> \(z_{0.005} = 2.576\)</li>
</ul>

<div class="worked-example">
<h4>Example: Computing a Confidence Interval</h4>
<p>Sample of 50 students: \(\bar{X} = 82\), \(\sigma = 10\). Find 95% CI for \(\mu\)</p>
<p><strong>Solution:</strong></p>
<p>Margin of error \(= 1.96 \times (10/\sqrt{50})\)</p>
<p style="text-align: center;">\(= 1.96 \times (10/7.071)\)</p>
<p style="text-align: center;">\(= 1.96 \times 1.414 \approx 2.77\)</p>
<p><strong>95% CI = \(82 \pm 2.77 = (79.23, 84.77)\)</strong></p>
<p><em>Interpretation:</em> We are 95% confident that the true population mean lies between 79.23 and 84.77.</p>
</div>

<h3>T-Confidence Interval (Unknown \(\sigma\))</h3>
<p>When \(\sigma\) is unknown, use sample standard deviation s and the t-distribution:</p>
<p style="text-align: center; font-weight: bold;">\(\text{CI} = \bar{X} \pm t_{\alpha/2,\, n-1} \times (s/\sqrt{n})\)</p>

<p>where \(t_{\alpha/2,\, n-1}\) is the critical t-value with \(\text{df} = n - 1\) degrees of freedom.</p>

<div class="worked-example">
<h4>Example: T-Confidence Interval</h4>
<p>Sample of 20 patients: \(\bar{X} = 150\), \(s = 12\). Find 95% CI for \(\mu\)</p>
<p><strong>Solution:</strong></p>
<p>\(\text{df} = 20 - 1 = 19\)</p>
<p>\(t_{0.025,\,19} \approx 2.093\)</p>
<p>Margin of error \(= 2.093 \times (12/\sqrt{20}) = 2.093 \times 2.683 \approx 5.61\)</p>
<p><strong>95% CI = \(150 \pm 5.61 = (144.39, 155.61)\)</strong></p>
</div>

<h3>Margin of Error</h3>
<p>The <strong>margin of error</strong> is half the width of the confidence interval:</p>
<p style="text-align: center; font-weight: bold;">\(\text{Margin of Error} = z_{\alpha/2} \times (\sigma/\sqrt{n})\)</p>

<p>Factors that reduce margin of error:</p>
<ul>
<li>Lower confidence level (smaller z or t critical value)</li>
<li>Larger sample size (larger \(\sqrt{n}\) in denominator)</li>
<li>Smaller population standard deviation \(\sigma\)</li>
</ul>
"""
    },
    {
        "title": "Relationship Between Confidence Intervals and Hypothesis Tests",
        "body": """
<h3>The CI-Test Connection</h3>
<p>A two-tailed hypothesis test at level \(\alpha\) is equivalent to checking whether the null value lies in the \((1-\alpha) \times 100\%\) confidence interval.</p>

<p><strong>Rule:</strong></p>
<ul>
<li>If \(\mu_0\) is <strong>NOT in</strong> the CI, reject \(H_0\): \(\mu = \mu_0\) at level \(\alpha\)</li>
<li>If \(\mu_0\) <strong>IS in</strong> the CI, fail to reject \(H_0\)</li>
</ul>

<div class="worked-example">
<h4>Example: Using CI to Make Hypothesis Test Decisions</h4>
<p>From a previous example: 95% CI = (79.23, 84.77)</p>

<p><strong>Test 1:</strong> \(H_0\): \(\mu = 80\) vs \(H_1\): \(\mu \neq 80\) at \(\alpha = 0.05\)</p>
<p>Since \(80 \in (79.23, 84.77)\), <strong>fail to reject \(H_0\)</strong></p>

<p><strong>Test 2:</strong> \(H_0\): \(\mu = 85\) vs \(H_1\): \(\mu \neq 85\) at \(\alpha = 0.05\)</p>
<p>Since \(85 \notin (79.23, 84.77)\), <strong>reject \(H_0\)</strong></p>
<p>The sample evidence contradicts the claim that \(\mu = 85\).</p>
</div>

<h3>Why Report Both?</h3>
<p>A confidence interval provides more information than a hypothesis test alone:</p>
<ul>
<li><strong>Hypothesis test:</strong> Yes/No decision (reject or fail to reject)</li>
<li><strong>Confidence interval:</strong> Range of plausible values + direction + magnitude</li>
</ul>

<p>Best practice: Report the 95% CI along with the test result to give readers a complete picture of the effect.</p>

<div class="success-box">
<p><strong>Key Insight:</strong> The confidence interval is more informative than the p-value alone. Always report effect sizes and confidence intervals in your statistical conclusions.</p>
</div>
"""
    }
]
