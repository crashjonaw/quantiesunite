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
            <li><strong>Sample size n:</strong> Larger n → narrower CI (more data = less uncertainty)</li>
            <li><strong>Confidence level:</strong> Higher confidence (e.g., 99% vs 95%) → wider interval (more certainty requires broader range)</li>
            <li><strong>Population variability σ:</strong> Higher σ → wider CI (more variable data = more uncertainty)</li>
        </ul>
        """
    },
    {
        "title": "Constructing Confidence Intervals",
        "body": """
        <p>The key to building a CI is finding a <strong>pivotal quantity</strong>: a function of the data and parameter whose distribution is known and doesn't depend on unknown parameters.</p>

        <div class='concept-box'>
            <p><strong>Pivotal Quantity:</strong> A statistic g(X₁,...,Xₙ, θ) whose distribution is known completely. Use it to create bounds for θ.</p>
        </div>

        <p><strong>General Recipe:</strong></p>
        <ol>
            <li>Find a pivotal quantity Q(data, θ)</li>
            <li>Find the distribution of Q (e.g., normal, t, chi-squared)</li>
            <li>Find the α/2 quantiles: q_lower and q_upper such that P(q_lower ≤ Q ≤ q_upper) = 1 - α</li>
            <li>Solve for θ to get CI endpoints</li>
        </ol>

        <div class='worked-example'>
            <p><strong>Example: CI for population mean (known σ)</strong></p>
            <p>Data: X₁,...,Xₙ ~ N(μ, σ²), σ is known, want 95% CI for μ.</p>
            <pre class='code-block'>Pivotal quantity: Z = (X̄ - μ)/(σ/√n) ~ N(0,1)

P(-1.96 ≤ Z ≤ 1.96) = 0.95

P(-1.96 ≤ (X̄ - μ)/(σ/√n) ≤ 1.96) = 0.95

Rearrange for μ:
P(X̄ - 1.96·σ/√n ≤ μ ≤ X̄ + 1.96·σ/√n) = 0.95

95% CI: [X̄ - 1.96·σ/√n, X̄ + 1.96·σ/√n]</pre>
            <p><strong>Interpretation:</strong> The interval extends 1.96 standard errors on either side of the point estimate.</p>
        </div>

        <div class='concept-box'>
            <p><strong>t-intervals (unknown σ):</strong> When σ is unknown, use the sample standard deviation s and the t-distribution with n-1 degrees of freedom.</p>
        </div>

        <pre class='code-block'>CI for μ: X̄ ± t_{α/2,n-1} · (s/√n)

where t_{α/2,n-1} is the critical value from t(n-1)</pre>

        <p>The t-interval is slightly wider than the z-interval (accounting for the extra uncertainty from estimating σ), and the difference shrinks as n grows large.</p>
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
                <td style='padding: 0.5em;'>Mean, σ known</td>
                <td style='padding: 0.5em;'>X̄ ± z_{α/2} · σ/√n</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Mean, σ unknown</td>
                <td style='padding: 0.5em;'>X̄ ± t_{α/2,n-1} · s/√n</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Proportion p (large n)</td>
                <td style='padding: 0.5em;'>p̂ ± z_{α/2} · √(p̂(1-p̂)/n)</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Difference of means</td>
                <td style='padding: 0.5em;'>(X̄₁ - X̄₂) ± t · SE_pooled</td>
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

        <p><strong>Bayesian credible intervals:</strong> An alternative perspective treats the parameter as random and uses prior beliefs. A credible interval directly gives P(θ ∈ [L,U] | data)—but requires specifying a prior.</p>
        """
    }
]
