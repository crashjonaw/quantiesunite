"""
Method of Moments (MoM)
A simple and intuitive approach to parameter estimation
"""

TITLE = "Method of Moments"

SECTIONS = [
    {
        "title": "The Core Principle",
        "body": """
        <p>The Method of Moments is based on a simple idea: sample characteristics should match population characteristics. Estimate population parameters by equating sample moments to population moments.</p>

        <div class='concept-box'>
            <p><strong>Sample Moment:</strong> The $k$-th sample moment is:</p>
            <p>$$m_k = \\frac{1}{n} \\sum_{i=1}^{n} X_i^k$$</p>
            <p><strong>Population Moment:</strong> The $k$-th population moment is:</p>
            <p>$$\\mu_k' = E[X^k]$$</p>
        </div>

        <p><strong>Method of Moments Principle:</strong> Estimate parameters by solving:</p>
        <p>$$m_k = \\mu_k' \\quad \\text{(match sample to population moments)}$$</p>

        <p><strong>How many equations?</strong> If you have $p$ parameters to estimate, you need $p$ equations. Use the first $p$ moments.</p>

        <div class='worked-example'>
            <p><strong>Example: Estimating $\\mu$ for $N(\\mu, \\sigma^2)$</strong></p>
            <p>We know $E[X] = \\mu$. The first sample moment is $\\bar{X} = \\frac{1}{n} \\sum X_i$.</p>
            <pre class='code-block'>Set: $\\bar{X} = E[X] = \\mu$
Therefore: $\\hat{\\mu} = \\bar{X}$

Simple and intuitive!</pre>
        </div>

        <p><strong>Why use Method of Moments?</strong></p>
        <ul>
            <li><strong>Simplicity:</strong> Direct, no calculus or optimization needed</li>
            <li><strong>Intuition:</strong> Obvious and easy to understand</li>
            <li><strong>Guaranteed existence:</strong> Solutions always exist (sample moments always exist)</li>
            <li><strong>Computational ease:</strong> No numerical methods required in many cases</li>
        </ul>

        <div class='warning-box'>
            <p><strong>Trade-off:</strong> While simple, MoM estimators are often less efficient than MLEs. They have larger variance and may not achieve the theoretical lower bound on variance.</p>
        </div>
        """
    },
    {
        "title": "Multi-Parameter Cases",
        "body": """
        <p>When estimating multiple parameters, use as many moment equations as parameters.</p>

        <div class='worked-example'>
            <p><strong>Example: $N(\\mu, \\sigma^2)$ with both unknown</strong></p>
            <p>We have two unknowns, so use the first two moments:</p>
            <pre class='code-block'>First moment:
$E[X] = \\mu$, so set $m_1 = \\hat{\\mu}$
$m_1 = \\bar{X} \\to \\hat{\\mu} = \\bar{X}$

Second moment:
$E[X^2] = \\mu^2 + \\sigma^2$, so set $m_2 = \\mu^2 + \\sigma^2$
$m_2 = \\frac{1}{n} \\sum X_i^2$

Solving:
$\\hat{\\sigma}^2 = m_2 - (m_1)^2 = \\frac{1}{n} \\sum X_i^2 - \\bar{X}^2$

This is the biased sample variance (with denominator $n$, not $n-1$)</pre>
        </div>

        <div class='worked-example'>
            <p><strong>Example: $\\text{Exponential}(\\lambda)$ distribution</strong></p>
            <p>For $\\text{Exponential}(\\lambda)$, the population mean is $E[X] = 1/\\lambda$.</p>
            <pre class='code-block'>Method of Moments equation:
$\\bar{X} = 1/\\lambda$

Solving for $\\lambda$:
$\\hat{\\lambda} = 1/\\bar{X}$

Intuition: If the sample average is 5, our estimate of $\\lambda$ is $1/5 = 0.2$</pre>
        </div>

        <div class='worked-example'>
            <p><strong>Example: $\\text{Uniform}(a, b)$</strong></p>
            <p>Two parameters, so use two moment equations:</p>
            <pre class='code-block'>Population moments:
$E[X] = (a + b)/2$
$E[X^2] = (a^2 + ab + b^2)/3$

Set sample moments equal:
$\\bar{X} = (a + b)/2$
$m_2 = (a^2 + ab + b^2)/3$

Solve this system to get $\\hat{a}$ and $\\hat{b}$
(details omitted, but algebraically straightforward)</pre>
        </div>
        """
    },
    {
        "title": "MLE vs. Method of Moments",
        "body": """
        <p>Both methods produce estimators, but they differ in their properties and approach:</p>

        <table style='width: 100%; border-collapse: collapse; margin: 1em 0;'>
            <tr style=';'>
                <th style='padding: 0.5em;'>Aspect</th>
                <th style='padding: 0.5em;'>Method of Moments</th>
                <th style='padding: 0.5em;'>Maximum Likelihood</th>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Philosophy</strong></td>
                <td style='padding: 0.5em;'>Match sample to population moments</td>
                <td style='padding: 0.5em;'>Maximize plausibility of observed data</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Computation</strong></td>
                <td style='padding: 0.5em;'>Direct algebraic solution</td>
                <td style='padding: 0.5em;'>Requires optimization/calculus</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Efficiency</strong></td>
                <td style='padding: 0.5em;'>Often suboptimal</td>
                <td style='padding: 0.5em;'>Asymptotically efficient</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Bias (small $n$)</strong></td>
                <td style='padding: 0.5em;'>Can be biased</td>
                <td style='padding: 0.5em;'>Can be biased</td>
            </tr>
            <tr>
                <td style='padding: 0.5em;'><strong>Consistency</strong></td>
                <td style='padding: 0.5em;'>Generally consistent</td>
                <td style='padding: 0.5em;'>Always consistent*</td>
            </tr>
        </table>

        <div class='concept-box'>
            <p><strong>When are they the same?</strong> For the normal distribution, MoM and MLE give identical estimators for $\\mu$. For other distributions, they typically differ.</p>
        </div>

        <div class='success-box'>
            <p><strong>Practical Use:</strong> In modern practice, MLE is preferred when computation is feasible. Method of Moments is useful when:</p>
            <ul>
                <li>You need a quick, simple estimator</li>
                <li>MLE is intractable (complex distributions)</li>
                <li>You want to use MoM as a starting point for numerical MLE optimization</li>
            </ul>
        </div>
        """
    }
]
