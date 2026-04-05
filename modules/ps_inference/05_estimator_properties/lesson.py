"""
Properties of Estimators: Bias, Consistency, and Efficiency
Evaluating the quality of statistical estimators
"""

TITLE = "Properties of Estimators"

SECTIONS = [
    {
        "title": "Unbiasedness and Bias",
        "body": """
        <p>An estimator's bias measures how far it is "off target" on average.</p>

        <div class='concept-box'>
            <p><strong>Unbiased Estimator:</strong> An estimator $\\hat{\\theta}$ is unbiased if:</p>
            <p>$$E[\\hat{\\theta}] = \\theta$$</p>
            <p>On average, it hits the true value.</p>
        </div>

        <p><strong>Bias:</strong> If the estimator is not unbiased, its bias is:</p>
        <p>$$\\text{Bias}(\\hat{\\theta}) = E[\\hat{\\theta}] - \\theta$$</p>

        <div class='worked-example'>
            <p><strong>Example: Sample mean is unbiased for population mean</strong></p>
            <pre class='code-block'>$\\hat{\\theta} = \\bar{X} = \\frac{1}{n} \\sum X_i$
$E[\\bar{X}] = E\\left[\\frac{1}{n} \\sum X_i\\right] = \\frac{1}{n} \\sum E[X_i] = \\frac{1}{n} \\cdot n \\cdot \\mu = \\mu$ ✓

$\\text{Bias}(\\bar{X}) = \\mu - \\mu = 0$. It's unbiased!</pre>
        </div>

        <div class='warning-box'>
            <p><strong>Biased estimator example:</strong> The sample variance with denominator $n$ (not $n-1$) is biased:</p>
            <pre class='code-block'>$S^2 = \\frac{1}{n} \\sum(X_i - \\bar{X})^2$
$E[S^2] \\neq \\sigma^2$ (it underestimates)

The unbiased version uses $n-1$:
$s^2 = \\frac{1}{n-1} \\sum(X_i - \\bar{X})^2$
$E[s^2] = \\sigma^2$ ✓</pre>
        </div>

        <p><strong>Why does the $n-1$ correction matter?</strong> Using $n-1$ accounts for the fact that $\\bar{X}$ is estimated from the same data, which reduces the sum of squared deviations. Dividing by $n-1$ instead of $n$ corrects for this downward bias.</p>

        <div class='concept-box'>
            <p><strong>Mean Squared Error (MSE):</strong> A more comprehensive measure that combines bias and variance:</p>
            <p>$$\\text{MSE}(\\hat{\\theta}) = E[(\\hat{\\theta} - \\theta)^2] = \\text{Var}(\\hat{\\theta}) + [\\text{Bias}(\\hat{\\theta})]^2$$</p>
        </div>

        <p>Sometimes a slightly biased estimator with much lower variance is preferable to an unbiased estimator with high variance.</p>
        """
    },
    {
        "title": "Consistency",
        "body": """
        <p>Consistency is about behavior as sample size increases: does the estimator converge to the truth?</p>

        <div class='concept-box'>
            <p><strong>Consistent Estimator:</strong> $\\hat{\\theta}_n$ is consistent if it converges in probability to $\\theta$ as $n \\to \\infty$:</p>
            <p>$$\\text{For any } \\varepsilon > 0: \\lim_{n \\to \\infty} P(|\\hat{\\theta}_n - \\theta| > \\varepsilon) = 0$$</p>
            <p>In symbols: $\\hat{\\theta}_n \\xrightarrow{p} \\theta$</p>
        </div>

        <p><strong>Intuition:</strong> With enough data, the estimator gets arbitrarily close to the true value with high probability. The estimator "zeros in" on the truth.</p>

        <div class='worked-example'>
            <p><strong>Example: Sample mean is consistent for population mean</strong></p>
            <p>As $n \\to \\infty$, $\\bar{X}$ converges to $\\mu$ by the Law of Large Numbers:</p>
            <pre class='code-block'>$\\bar{X} = \\frac{1}{n} \\sum X_i \\xrightarrow{p} \\mu$

$\\text{Var}(\\bar{X}) = \\sigma^2/n \\to 0$ as $n \\to \\infty$
(the variance shrinks)</pre>
        </div>

        <div class='concept-box'>
            <p><strong>Sufficient condition for consistency:</strong> If $\\hat{\\theta}_n$ is unbiased and $\\text{Var}(\\hat{\\theta}_n) \\to 0$ as $n \\to \\infty$, then $\\hat{\\theta}_n$ is consistent.</p>
        </div>

        <p>This covers most well-behaved estimators. Unbiasedness plus vanishing variance guarantees consistency.</p>

        <div class='warning-box'>
            <p><strong>Consistency doesn't mean quick convergence:</strong> An estimator can be consistent but require enormous sample sizes to be reliable. Consistency is a weak guarantee (asymptotic).</p>
        </div>

        <div class='success-box'>
            <p><strong>Why consistency matters:</strong> Consistency ensures that statistical inference works in the limit. Without it, no amount of data helps us estimate the parameter accurately.</p>
        </div>
        """
    },
    {
        "title": "Efficiency and the Cramer-Rao Bound",
        "body": """
        <p>Among unbiased estimators, which has the smallest variance? Efficiency measures this.</p>

        <div class='concept-box'>
            <p><strong>Relative Efficiency:</strong> For two unbiased estimators $\\hat{\\theta}_1$ and $\\hat{\\theta}_2$, the relative efficiency of $\\hat{\\theta}_1$ with respect to $\\hat{\\theta}_2$ is:</p>
            <p>$$\\text{Efficiency} = \\frac{\\text{Var}(\\hat{\\theta}_2)}{\\text{Var}(\\hat{\\theta}_1)}$$</p>
            <p>An efficiency $> 1$ means $\\hat{\\theta}_1$ is more efficient (lower variance).</p>
        </div>

        <div class='worked-example'>
            <p><strong>Example: Comparing estimators for the mean</strong></p>
            <p>For normally distributed data, two unbiased estimators of $\\mu$ are:</p>
            <pre class='code-block'>$\\hat{\\theta}_1 = \\bar{X}$ (sample mean)
$\\hat{\\theta}_2 = \\text{Median of sample}$

$\\text{Var}(\\bar{X}) = \\sigma^2/n$
$\\text{Var}(\\text{Median}) \\approx \\frac{\\pi \\sigma^2}{2n}$ for large $n$

Efficiency $= \\frac{\\pi \\sigma^2/(2n)}{\\sigma^2/n} = \\frac{\\pi}{2} \\approx 1.57$

$\\bar{X}$ is more efficient!</pre>
        </div>

        <div class='concept-box'>
            <p><strong>Cramer-Rao Lower Bound (CRLB):</strong> For an unbiased estimator $\\hat{\\theta}$, the variance is bounded below:</p>
            <p>$$\\text{Var}(\\hat{\\theta}) \\geq \\frac{1}{nI(\\theta)}$$</p>
            <p>where $I(\\theta)$ is the Fisher Information:</p>
            <p>$$I(\\theta) = -E\\left[\\frac{d^2\\ell}{d\\theta^2}\\right] \\quad \\text{(expected curvature of log-likelihood)}$$</p>
        </div>

        <p><strong>What this means:</strong> No unbiased estimator can have variance smaller than the Cramer-Rao bound. An estimator that achieves this bound is called efficient.</p>

        <div class='worked-example'>
            <p><strong>Example: Fisher Information for $\\text{Bernoulli}(p)$</strong></p>
            <pre class='code-block'>Log-likelihood: $\\ell(p) = k \\ln p + (n-k) \\ln(1-p)$
$\\frac{d^2\\ell}{dp^2} = -\\frac{k}{p^2} - \\frac{n-k}{(1-p)^2}$

$I(p) = nE\\left[-\\frac{d^2\\ell}{dp^2}\\right] = n \\cdot \\frac{1}{p(1-p)} = \\frac{n}{p(1-p)}$

CRLB $= \\frac{1}{nI(p)} = \\frac{p(1-p)}{n}$

This is the variance of $\\hat{p} = k/n$, so $\\hat{p}$ is efficient!</pre>
        </div>

        <div class='success-box'>
            <p><strong>Asymptotic Efficiency:</strong> MLEs are asymptotically efficient—for large $n$, they achieve the Cramer-Rao bound. This is one reason MLEs are preferred.</p>
        </div>

        <div class='concept-box'>
            <p><strong>Trade-offs:</strong> Sometimes we trade a tiny bit of bias for much lower variance (regularization, shrinkage estimators). MSE can improve even though bias increases.</p>
        </div>
        """
    },
    {
        "title": "A Unified Framework",
        "body": """
        <p>Understanding estimator properties helps us choose the right tool for the job:</p>

        <table style='width: 100%; border-collapse: collapse; margin: 1em 0;'>
            <tr style=';'>
                <th style='padding: 0.5em;'>Property</th>
                <th style='padding: 0.5em;'>What It Means</th>
                <th style='padding: 0.5em;'>When to Care</th>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Unbiased</strong></td>
                <td style='padding: 0.5em;'>$E[\\hat{\\theta}] = \\theta$ (no systematic error)</td>
                <td style='padding: 0.5em;'>When you want on-target estimates</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Consistent</strong></td>
                <td style='padding: 0.5em;'>$\\hat{\\theta}_n \\xrightarrow{p} \\theta$ as $n \\to \\infty$</td>
                <td style='padding: 0.5em;'>Always desirable (essential for large $n$)</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Efficient</strong></td>
                <td style='padding: 0.5em;'>Minimum variance among unbiased</td>
                <td style='padding: 0.5em;'>When sample size is limited</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Robust</strong></td>
                <td style='padding: 0.5em;'>Works well under model violations</td>
                <td style='padding: 0.5em;'>When you distrust assumptions</td>
            </tr>
        </table>

        <div class='concept-box'>
            <p><strong>Typical hierarchy (for well-behaved estimators):</strong></p>
            <ul>
                <li>Consistency is essential (non-negotiable)</li>
                <li>Unbiasedness is nice (but not required if bias shrinks)</li>
                <li>Efficiency matters for limited data</li>
                <li>Robustness matters in real-world applications</li>
            </ul>
        </div>

        <p><strong>In practice:</strong> MLEs often excel on most criteria (consistent, asymptotically efficient) but may have bias for small $n$. Method of Moments is simpler and robust, but less efficient. Choose based on your specific problem and data.</p>
        """
    }
]
