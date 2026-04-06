TITLE = "Applications and Confidence Intervals"

SECTIONS = [
    {
        "title": "Confidence Intervals from the CLT",
        "body": """
        <p><strong>Core idea:</strong> The CLT tells us that \(\bar{X} \approx N(\mu, \sigma^2/n)\). We can use this to construct confidence intervals for \(\mu\).</p>

        <p><strong>When \(\sigma\) is known:</strong> A \((1 - \alpha) \cdot 100\%\) confidence interval is:</p>
        <pre class='code-block'>\(\bar{X} \pm z_{\alpha/2} \cdot (\sigma / \sqrt{n})\)</pre>

        <p>where \(z_{\alpha/2}\) is the critical value such that \(P(Z \leq z_{\alpha/2}) = 1 - \alpha/2\) for standard normal \(Z\).</p>

        <p><strong>When \(\sigma\) is unknown:</strong> Replace \(\sigma\) with the sample standard deviation \(S\) and use \(t_{\alpha/2, n-1}\):</p>
        <pre class='code-block'>\(\bar{X} \pm t_{\alpha/2, n-1} \cdot (S / \sqrt{n})\)</pre>

        <p>The t-distribution accounts for the extra uncertainty from estimating \(\sigma\). It has heavier tails than normal, giving wider intervals.</p>

        <div class='worked-example'>
        <p><strong>Example: CI with known \(\sigma\)</strong></p>
        <pre class='code-block'>Data: \(n = 100\) test scores, \(\bar{X} = 75.2\), \(\sigma = 8\) (from historical data)
Confidence level: 95% (\(\alpha = 0.05\))
Critical value: z_{0.025} = 1.96

CI = 75.2 ± 1.96 · (8 / √100)
   = 75.2 ± 1.96 · 0.8
   = 75.2 ± 1.568
   = (73.632, 76.768)</pre>
        <p><strong>Interpretation:</strong> We are 95% confident that the true mean test score is between 73.63 and 76.77.</p>
        </div>

        <p><strong>Key quantities:</strong></p>
        <ul>
        <li><strong>Margin of error (ME):</strong> \(E = z_{\alpha/2} \cdot \sigma / \sqrt{n}\) (half-width of the interval)</li>
        <li><strong>Standard error (SE):</strong> \(\sigma / \sqrt{n}\) (denominator of ME)</li>
        <li><strong>Confidence level:</strong> \(1 - \alpha\) (e.g., 0.95 for 95% CI, meaning \(\alpha = 0.05\))</li>
        </ul>
        """
    },
    {
        "title": "Determining Sample Size",
        "body": """
        <p><strong>Question:</strong> How many observations do we need to achieve a desired margin of error?</p>

        <p><strong>Formula:</strong> To ensure margin of error \(\leq E\) with confidence \(1 - \alpha\):</p>
        <pre class='code-block'>\(n \geq (z_{\alpha/2} \cdot \sigma / E)^2\)</pre>

        <div class='worked-example'>
        <p><strong>Example: Hospital patient satisfaction survey</strong></p>
        <pre class='code-block'>Goal: 95% CI with margin of error E = 3 percentage points
From pilot study, estimate \(\sigma = 25\) (satisfaction score out of 100)
z_{0.025} = 1.96

\(n \geq (1.96 \cdot 25 / 3)^2\)
  = (16.33)²
  ≈ 267

Need at least 267 patients surveyed.</pre>
        </div>

        <p><strong>Factors affecting required sample size:</strong></p>
        <ul>
        <li><strong>Smaller margin of error (\(E\)) → larger \(n\):</strong> \(E\) and \(n\) are inversely related. To halve \(E\) requires \(4\times\) the sample size.</li>
        <li><strong>Higher confidence (larger \(1 - \alpha\)) → larger \(n\):</strong> 99% CI (\(z = 2.576\)) requires more data than 95% CI (\(z = 1.96\)).</li>
        <li><strong>Larger \(\sigma\) → larger \(n\):</strong> More variable populations require larger samples.</li>
        </ul>

        <div class='success-box'>
        <p><strong>Rule of thumb:</strong> To halve the margin of error, quadruple the sample size (since \(\text{ME} \propto 1/\sqrt{n}\)).</p>
        </div>
        """
    },
    {
        "title": "Real-World Applications of the CLT",
        "body": """
        <p><strong>1. Quality Control:</strong> Monitor manufacturing processes. If sample mean of measurements falls outside control limits based on normal approximation, investigate the process.</p>

        <p><strong>2. Polling and Elections:</strong> Estimate population support from a sample of voters. Sample proportion p̂ has approximately normal distribution for large n.</p>

        <div class='worked-example'>
        <p><strong>Polling example:</strong></p>
        <pre class='code-block'>Poll n = 1,000 voters about a ballot measure
Sample support: p̂ = 0.52 (52%)
95% CI: 0.52 ± 1.96 · √(0.52 · 0.48 / 1000)
      = 0.52 ± 1.96 · 0.0158
      = 0.52 ± 0.031
      = (0.489, 0.551)

Interpretation: 95% confident true support is between 48.9% and 55.1% (±3.1% margin)</pre>
        </div>

        <p><strong>3. Clinical Trials:</strong> Compare treatment vs. control groups. CLT justifies using normal-based t-tests even if individual measurements aren't normally distributed.</p>

        <p><strong>4. Regression Analysis:</strong> With many observations, OLS estimators are approximately normal by CLT. Enables valid confidence intervals and tests for slopes.</p>

        <p><strong>5. Financial Markets:</strong> Daily returns don't follow normal distributions, but with large sample sizes, portfolio means can be approximated normally.</p>

        <div class='warning-box'>
        <p><strong>Limitations in practice:</strong></p>
        <ul>
        <li><strong>Outliers:</strong> Extreme values violate finite variance assumption. Consider robust methods.</li>
        <li><strong>Dependence:</strong> Time series data are not i.i.d. Autocorrelation must be accounted for.</li>
        <li><strong>Small samples:</strong> Rule of thumb \(n \geq 30\), but depends on data distribution.</li>
        <li><strong>Non-identical distributions:</strong> Data from different subpopulations violate i.i.d. assumption.</li>
        </ul>
        </div>

        <p><strong>Modern alternatives:</strong> Bootstrap resampling, permutation tests, and Bayesian methods provide robust alternatives that don't rely on normality or CLT assumptions.</p>
        """
    }
]
