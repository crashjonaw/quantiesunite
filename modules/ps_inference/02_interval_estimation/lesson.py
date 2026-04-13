"""
Interval Estimation & Confidence Intervals
From point estimates to ranges of plausible parameter values
"""

TITLE = "Interval Estimation & Confidence Intervals"

SECTIONS = [
    {
        "title": "Why Intervals, Not Points?",
        "body": """
        <p>A point estimate like X̄ = 52 tells us one value, but it ignores uncertainty. In reality, the true parameter likely falls in a range around our estimate.</p>

        <div class='concept-box'>
            <p><strong>Confidence Interval (CI):</strong> A range [L, U] computed from sample data such that we have high confidence the true parameter lies within it.</p>
        </div>

        <p><strong>Confidence Level:</strong> A CI is typically stated with a confidence level (e.g., 95%), meaning if we repeated our sampling procedure many times, about 95% of the computed intervals would contain the true parameter.</p>

        <pre class='code-block'>Interpretation: In the long run, 95% of 95%-CIs capture the true value
NOT: "There's a 95% chance the true value is in THIS interval"
     (Frequentist: the true value is fixed; it's either in or out)</pre>

        <div class='warning-box'>
            <p><strong>Common Misconception:</strong> A 95% CI does NOT mean there's a 95% probability the parameter is in the interval for this specific sample. The interval is fixed once computed; probability is about the method, not the outcome.</p>
        </div>

        <p>The width of a CI depends on:</p>
        <ul>
            <li><strong>Sample size \(n\):</strong> Larger \(n\) → narrower CI (more data = less uncertainty)</li>
            <li><strong>Confidence level:</strong> Higher confidence (e.g., 99% vs 95%) → wider interval (more certainty requires broader range)</li>
            <li><strong>Population variability \(\\sigma\):</strong> Higher \(\\sigma\) → wider CI (more variable data = more uncertainty)</li>
        </ul>
        """
    },
    {
        "title": "Constructing Confidence Intervals",
        "body": """
        <p>The key to building a CI is finding a <strong>pivotal quantity</strong>: a function of the data and parameter whose distribution is known and doesn't depend on unknown parameters.</p>

        <div class='concept-box'>
            <p><strong>Pivotal Quantity:</strong> A statistic \(g(X_1,\ldots,X_n, \\theta)\) whose distribution is known completely. Use it to create bounds for \(\\theta\).</p>
        </div>

        <p><strong>General Recipe:</strong></p>
        <ol>
            <li>Find a pivotal quantity \(Q(\\text{data}, \\theta)\)</li>
            <li>Find the distribution of Q (e.g., normal, t, chi-squared)</li>
            <li>Find the \(\\alpha/2\) quantiles: \(q_\\text{lower}\) and \(q_\\text{upper}\) such that \(P(q_\\text{lower} \\leq Q \\leq q_\\text{upper}) = 1 - \\alpha\)</li>
            <li>Solve for \(\\theta\) to get CI endpoints</li>
        </ol>

        <div class='worked-example'>
            <p><strong>Example: CI for population mean (known \(\\sigma\))</strong></p>
            <p>Data: \(X_1,\ldots,X_n \sim N(\\mu, \\sigma^2)\), \(\\sigma\) is known, want 95% CI for \(\\mu\).</p>
            <pre class='code-block'>Pivotal quantity: \(Z = (\\bar{X} - \\mu)/(\\sigma/\\sqrt{n}) \sim N(0,1)\)

\(P(-1.96 \\leq Z \\leq 1.96) = 0.95\)

\(P(-1.96 \\leq (\\bar{X} - \\mu)/(\\sigma/\\sqrt{n}) \\leq 1.96) = 0.95\)

Rearrange for \(\\mu\):
\(P(\\bar{X} - 1.96 \\cdot \\sigma/\\sqrt{n} \\leq \\mu \\leq \\bar{X} + 1.96 \\cdot \\sigma/\\sqrt{n}) = 0.95\)

95% CI: \([\\bar{X} - 1.96 \\cdot \\sigma/\\sqrt{n},\ \\bar{X} + 1.96 \\cdot \\sigma/\\sqrt{n}]\)</pre>
            <p><strong>Interpretation:</strong> The interval extends 1.96 standard errors on either side of the point estimate.</p>
        </div>

        <div class='concept-box'>
            <p><strong>t-intervals (unknown \(\\sigma\)):</strong> When \(\\sigma\) is unknown, use the sample standard deviation \(s\) and the t-distribution with \(n-1\) degrees of freedom.</p>
        </div>

        <pre class='code-block'>CI for \(\\mu\): \(\\bar{X} \pm t_{\\alpha/2,n-1} \\cdot (s/\\sqrt{n})\)

where \(t_{\\alpha/2,n-1}\) is the critical value from \(t(n-1)\)</pre>

        <p>The t-interval is slightly wider than the z-interval (accounting for the extra uncertainty from estimating \(\\sigma\)), and the difference shrinks as \(n\) grows large.</p>
        """
    },
    {
        "title": "Confidence Intervals in Practice",
        "body": """
        <p><strong>Common CI formulas:</strong></p>

        <table style='width: 100%; border-collapse: collapse; margin: 1em 0;'>
            <tr style=';'>
                <th style='padding: 0.5em;'>Scenario</th>
                <th style='padding: 0.5em;'>Interval Formula</th>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Mean, \(\\sigma\) known</td>
                <td style='padding: 0.5em;'>\(\\bar{X} \pm z_{\\alpha/2} \\cdot \\sigma/\\sqrt{n}\)</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Mean, \(\\sigma\) unknown</td>
                <td style='padding: 0.5em;'>\(\\bar{X} \pm t_{\\alpha/2,n-1} \\cdot s/\\sqrt{n}\)</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Proportion \(p\) (large \(n\))</td>
                <td style='padding: 0.5em;'>\(\\hat{p} \pm z_{\\alpha/2} \\cdot \\sqrt{\\hat{p}(1-\\hat{p})/n}\)</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Difference of means</td>
                <td style='padding: 0.5em;'>\((\\bar{X}_1 - \\bar{X}_2) \pm t \\cdot SE_\\text{pooled}\)</td>
            </tr>
        </table>

        <div class='worked-example'>
            <p><strong>Example: 95% CI for a proportion</strong></p>
            <p>Sample of n=100, observed p̂ = 0.35. Find 95% CI for true proportion.</p>
            <pre class='code-block'>SE = √(0.35 · 0.65 / 100) = √(0.2275/100) ≈ 0.047

95% CI: 0.35 ± 1.96 · 0.047
       = 0.35 ± 0.092
       = [0.258, 0.442]

Interpretation: We're 95% confident the true proportion lies between 25.8% and 44.2%</pre>
        </div>

        <div class='success-box'>
            <p><strong>Margin of Error:</strong> The width of a CI (e.g., ±0.092) depends on sample size and desired confidence. Doubling precision requires 4× larger sample sizes!</p>
        </div>

        <p><strong>Bayesian credible intervals:</strong> An alternative perspective treats the parameter as random and uses prior beliefs. A credible interval directly gives \(P(\\theta \in [L,U] \mid \\text{data})\)—but requires specifying a prior.</p>
        """
    }
]
