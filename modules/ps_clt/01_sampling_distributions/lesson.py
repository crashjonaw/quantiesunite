TITLE = "Sampling Distributions"

SECTIONS = [
    {
        "title": "What is a Sampling Distribution?",
        "body": """
        <p><strong>Sampling distribution:</strong> The probability distribution of a sample statistic (like the sample mean, sample proportion, or sample variance) computed from repeated samples of size $n$ drawn from the same population.</p>

        <p><strong>Key insight:</strong> A single sample gives one value of the statistic. If we repeatedly sample, we get different values. The distribution of these values is the sampling distribution.</p>

        <p><strong>Example:</strong> Suppose we have a population of all exam scores. We draw $n = 50$ students and compute the sample mean $\\bar{X}$. If we repeat this 10,000 times, we get 10,000 sample means. The histogram of these 10,000 values forms the sampling distribution.</p>

        <div class='concept-box'>
        <p><strong>Why sampling distributions matter:</strong></p>
        <ul>
        <li>They describe the behavior of sample statistics</li>
        <li>They allow us to quantify uncertainty in our estimates</li>
        <li>They are the foundation for confidence intervals and hypothesis tests</li>
        <li>They tell us what variability to expect when sampling</li>
        </ul>
        </div>

        <p><strong>Theoretical vs. empirical sampling distributions:</strong> The theoretical sampling distribution is derived mathematically. An empirical sampling distribution is constructed by simulation (repeatedly sampling and computing the statistic).</p>
        """
    },
    {
        "title": "Sampling Distribution of the Mean",
        "body": """
        <p><strong>Setup:</strong> Population with mean $\\mu$ and variance $\\sigma^2$. Draw $n$ observations and compute sample mean $\\bar{X} = \\frac{1}{n}\\sum_{i} X_i$.</p>

        <p><strong>Properties of the sampling distribution of $\\bar{X}$:</strong></p>
        <pre class='code-block'>$E[\\bar{X}] = \\mu$ ($\\bar{X}$ is unbiased)
$\\text{Var}(\\bar{X}) = \\sigma^2/n$ (variance decreases with sample size)
$\\text{SD}(\\bar{X}) = \\sigma/\\sqrt{n}$ (standard error of the mean)</pre>

        <p><strong>Standard error (SE):</strong> The standard deviation of a sample statistic. For the sample mean, $SE = \\sigma/\\sqrt{n}$. When $\\sigma$ is unknown, we estimate it with the sample standard deviation $S$, giving $SE = S/\\sqrt{n}$.</p>

        <div class='worked-example'>
        <p><strong>Example: Sampling distribution of sample mean</strong></p>
        <p><strong>Population:</strong> All employees' salaries with $\\mu = \\$50{,}000$ and $\\sigma = \\$8{,}000$.</p>
        <p><strong>Draw samples of size $n = 100$.</strong></p>
        <pre class='code-block'>$E[\\bar{X}] = \\$50{,}000$
$\\text{Var}(\\bar{X}) = 8{,}000^2/100 = 640{,}000$
$\\text{SD}(\\bar{X}) = \\sqrt{640{,}000} = \\$800$</pre>
        <p><strong>Interpretation:</strong> If we repeatedly draw samples of 100 employees, the sample mean will vary with a standard deviation of \\$800 around the true mean of \\$50,000.</p>
        </div>

        <p><strong>Effect of sample size:</strong> As $n$ increases, the standard error $\\sigma/\\sqrt{n}$ decreases. Larger samples give more precise estimates (less variability in $\\bar{X}$).</p>
        """
    },
    {
        "title": "Sampling Distribution of Other Statistics",
        "body": """
        <p><strong>Sample proportion:</strong> If $X$ = number of successes in $n$ trials, then $\\hat{p} = X/n$ is the sample proportion.</p>
        <pre class='code-block'>$E[\\hat{p}] = p$ (unbiased)
$\\text{Var}(\\hat{p}) = p(1-p)/n$ (variance)
$\\text{SD}(\\hat{p}) = \\sqrt{p(1-p)/n}$ (standard error)</pre>

        <div class='example-box'>
        <p><strong>Polling example:</strong> True population support $p = 0.45$. Poll $n = 1{,}000$ voters.</p>
        <pre class='code-block'>$E[\\hat{p}] = 0.45$
$\\text{SD}(\\hat{p}) = \\sqrt{0.45 \\cdot 0.55 / 1{,}000} \\approx 0.0157 \\approx 1.57\\%$</pre>
        </div>

        <p><strong>Sample variance:</strong> The distribution of the sample variance $S^2$ is more complex. For normal populations, $S^2/\\sigma^2$ follows a chi-squared distribution with $n-1$ degrees of freedom.</p>

        <p><strong>Difference of means:</strong> When comparing two independent samples with means $\\bar{X}_1$ and $\\bar{X}_2$:</p>
        <pre class='code-block'>$E[\\bar{X}_1 - \\bar{X}_2] = \\mu_1 - \\mu_2$
$\\text{Var}(\\bar{X}_1 - \\bar{X}_2) = \\sigma_1^2/n_1 + \\sigma_2^2/n_2$
$\\text{SD}(\\bar{X}_1 - \\bar{X}_2) = \\sqrt{\\sigma_1^2/n_1 + \\sigma_2^2/n_2}$</pre>

        <p><strong>Key principle:</strong> The standard error of a statistic depends on the variability in the population and inversely on the sample size. Larger samples yield smaller standard errors, meaning more precise estimates.</p>
        """
    }
]
