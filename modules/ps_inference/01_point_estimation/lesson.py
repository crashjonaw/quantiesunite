"""
Point Estimation: Foundations of Statistical Inference
First principles introduction to estimating unknown parameters
"""

TITLE = "Point Estimation"

SECTIONS = [
    {
        "title": "What is Point Estimation?",
        "body": """
        <p>Point estimation is the process of using sample data to calculate a single value (a point estimate) that serves as our best guess for an unknown population parameter.</p>

        <div class='concept-box'>
            <p><strong>Core Idea:</strong> We observe data from a population with unknown parameter $\\theta$, and we want to find $\\hat{\\theta}$, a single number that best represents $\\theta$.</p>
        </div>

        <p><strong>Key Components:</strong></p>
        <ul>
            <li><strong>Parameter $\\theta$:</strong> The unknown fixed value we wish to estimate (e.g., population mean $\\mu$, variance $\\sigma^2$, or probability $p$)</li>
            <li><strong>Estimator $\\hat{\\theta}$:</strong> A function of the sample data (a statistic) used to estimate $\\theta$</li>
            <li><strong>Estimate:</strong> The actual numerical value $\\hat{\\theta}$ takes for a specific sample</li>
        </ul>

        <p><strong>Notation:</strong> We denote estimators with a hat ($\\hat{}$) symbol. For example:</p>
        <pre class='code-block'>$\\hat{\\mu}$ = estimate of population mean
$\\hat{\\sigma}^2$ = estimate of population variance
$\\hat{p}$ = estimate of population proportion</pre>

        <p>The fundamental challenge: different estimators can estimate the same parameter. How do we choose the best one?</p>
        """
    },
    {
        "title": "Desirable Properties of Estimators",
        "body": """
        <p>Not all estimators are equally good. We evaluate them using several criteria:</p>

        <div class='concept-box'>
            <p><strong>Unbiasedness:</strong> An estimator $\\hat{\\theta}$ is unbiased if $E[\\hat{\\theta}] = \\theta$. On average, it hits the true value.</p>
        </div>

        <p><strong>Example:</strong> The sample mean $\\bar{X}$ is an unbiased estimator of $\\mu$ because $E[\\bar{X}] = \\mu$.</p>

        <pre class='code-block'>Sample mean: $\\bar{X} = \\frac{1}{n} \\sum X_i$
$E[\\bar{X}] = E\\left[\\frac{1}{n} \\sum X_i\\right] = \\frac{1}{n} \\sum E[X_i] = \\frac{1}{n} \\cdot n \\cdot \\mu = \\mu$ ✓</pre>

        <div class='warning-box'>
            <p><strong>Bias:</strong> If $E[\\hat{\\theta}] \\neq \\theta$, the estimator has $\\text{bias} = E[\\hat{\\theta}] - \\theta$. A biased estimator is systematically off.</p>
        </div>

        <p><strong>Counter-example:</strong> Sample variance with denominator $n$ (not $n-1$) is biased:</p>
        <pre class='code-block'>$S^2 = \\frac{1}{n} \\sum(X_i - \\bar{X})^2$ is biased downward (underestimates $\\sigma^2$)
$s^2 = \\frac{1}{n-1} \\sum(X_i - \\bar{X})^2$ is unbiased</pre>

        <div class='concept-box'>
            <p><strong>Consistency:</strong> An estimator is consistent if it converges to the true parameter as sample size increases ($\\hat{\\theta} \\to \\theta$ as $n \\to \\infty$).</p>
        </div>

        <p>Intuitively: with enough data, we get arbitrarily close to the truth. Most well-behaved estimators are consistent even if biased for small $n$.</p>

        <div class='concept-box'>
            <p><strong>Efficiency:</strong> Among unbiased estimators, the most efficient has the smallest variance. Lower variance = more precise estimates.</p>
        </div>

        <p>Variance of $\\bar{X} = \\sigma^2/n$. As $n$ increases, variance decreases (we become more confident).</p>
        """
    },
    {
        "title": "Common Point Estimators",
        "body": """
        <p>For the most common parameters, standard estimators are used:</p>

        <table style='width: 100%; border-collapse: collapse; margin: 1em 0;'>
            <tr style=';'>
                <th style='padding: 0.5em;'>Parameter</th>
                <th style='padding: 0.5em;'>Estimator</th>
                <th style='padding: 0.5em;'>Properties</th>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Population mean $\\mu$</td>
                <td style='padding: 0.5em;'>$\\bar{X} = \\frac{1}{n} \\sum X_i$</td>
                <td style='padding: 0.5em;'>Unbiased, consistent, efficient</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Population variance $\\sigma^2$</td>
                <td style='padding: 0.5em;'>$s^2 = \\frac{1}{n-1} \\sum(X_i - \\bar{X})^2$</td>
                <td style='padding: 0.5em;'>Unbiased for normal data</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'>Population proportion $p$</td>
                <td style='padding: 0.5em;'>$\\hat{p} = X/n$ (# successes / $n$)</td>
                <td style='padding: 0.5em;'>Unbiased, consistent</td>
            </tr>
        </table>

        <div class='worked-example'>
            <p><strong>Example:</strong> Estimating a population proportion</p>
            <p>A survey of 400 voters finds 220 support a proposal. Estimate the population proportion:</p>
            <pre class='code-block'>$\\hat{p} = 220/400 = 0.55 = 55\\%$</pre>
            <p>This is our point estimate of the true population support.</p>
        </div>

        <div class='success-box'>
            <p><strong>Key Takeaway:</strong> Point estimators provide single-value guesses for parameters, but they don't tell us how uncertain we are. Interval estimation (confidence intervals) addresses this gap.</p>
        </div>
        """
    }
]
