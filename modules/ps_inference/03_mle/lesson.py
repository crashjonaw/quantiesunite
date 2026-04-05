"""
Maximum Likelihood Estimation (MLE)
The principle of choosing parameters that make observed data most probable
"""

TITLE = "Maximum Likelihood Estimation (MLE)"

SECTIONS = [
    {
        "title": "The Likelihood Function",
        "body": """
        <p>The likelihood function turns the probability model "backwards"—instead of asking "what's the probability of the data given $\\theta$?", we ask "for which $\\theta$ is the observed data most probable?"</p>

        <div class='concept-box'>
            <p><strong>Likelihood Function:</strong> Given observed data $X_1, \\ldots, X_n$ and parameter $\\theta$, the likelihood is:</p>
            <p>$$L(\\theta; \\text{data}) = f(X_1, \\ldots, X_n \\mid \\theta) = \\prod_{i=1}^{n} f(X_i \\mid \\theta)$$</p>
            <p>for independent observations. It's the joint PDF/PMF viewed as a function of $\\theta$ (not of the data).</p>
        </div>

        <p><strong>Key insight:</strong> $L(\\theta)$ gives the relative plausibility of different $\\theta$ values given the data. Larger $L(\\theta)$ means $\\theta$ is more consistent with what we observed.</p>

        <div class='warning-box'>
            <p><strong>Likelihood $\\neq$ Probability:</strong> A likelihood is not a probability—it's a relative measure of plausibility. It doesn't integrate or sum to 1 over $\\theta$.</p>
        </div>

        <div class='worked-example'>
            <p><strong>Example: Likelihood for Bernoulli data</strong></p>
            <p>Data: Flip a coin 3 times, observe $\\{H, T, H\\}$. Let $p = P(\\text{Heads})$.</p>
            <pre class='code-block'>$f(H,T,H \\mid p) = p \\cdot (1-p) \\cdot p = p^2(1-p)$

Likelihood: $L(p) = p^2(1-p)$

At $p=0.5$: $L(0.5) = 0.25 \\cdot 0.5 = 0.125$
At $p=0.7$: $L(0.7) = 0.49 \\cdot 0.3 = 0.147$
At $p=0.8$: $L(0.8) = 0.64 \\cdot 0.2 = 0.128$

$p=0.7$ makes the data most likely!</pre>
        </div>

        <p><strong>Why use log-likelihood?</strong> Computing products of many small probabilities risks numerical underflow. The log-likelihood is easier to maximize:</p>
        <p>$$\\ell(\\theta) = \\ln L(\\theta) = \\sum_i \\ln f(X_i \\mid \\theta)$$</p>
        <p>Maximizing $\\ell(\\theta)$ is equivalent to maximizing $L(\\theta)$.</p>
        """
    },
    {
        "title": "Finding the Maximum Likelihood Estimator",
        "body": """
        <p>The Maximum Likelihood Estimator (MLE) is the value of $\\theta$ that maximizes the likelihood:</p>

        <div class='concept-box'>
            <p><strong>Definition:</strong> $\\hat{\\theta}_{\\text{MLE}} = \\arg\\max_{\\theta} L(\\theta; \\text{data})$</p>
            <p>Or equivalently: $\\hat{\\theta}_{\\text{MLE}} = \\arg\\max_{\\theta} \\ell(\\theta; \\text{data})$</p>
        </div>

        <p><strong>How to find it:</strong></p>
        <ol>
            <li>Write down the log-likelihood: $\\ell(\\theta) = \\sum \\ln f(X_i \\mid \\theta)$</li>
            <li>Take the derivative with respect to $\\theta$: $d\\ell/d\\theta$</li>
            <li>Set it to zero: $d\\ell/d\\theta = 0$ (first-order condition)</li>
            <li>Solve for $\\theta$ to get $\\hat{\\theta}_{\\text{MLE}}$</li>
            <li>Verify it's a maximum (check second derivative $d^2\\ell/d\\theta^2 < 0$)</li>
        </ol>

        <div class='worked-example'>
            <p><strong>Example: MLE for $\\text{Poisson}(\\lambda)$</strong></p>
            <p>Data: $X_1, \\ldots, X_n \\sim \\text{Poisson}(\\lambda)$, observed values $x_1, \\ldots, x_n$.</p>
            <pre class='code-block'>Likelihood: $L(\\lambda) = \\prod \\frac{e^{-\\lambda} \\lambda^{x_i}}{x_i!} = e^{-n\\lambda} \\lambda^{\\sum x_i} / (\\prod x_i!)$

Log-likelihood: $\\ell(\\lambda) = -n\\lambda + (\\sum x_i) \\ln \\lambda - \\text{const}$

First order condition:
$\\frac{d\\ell}{d\\lambda} = -n + \\frac{\\sum x_i}{\\lambda} = 0$

Solving: $\\hat{\\lambda}_{\\text{MLE}} = \\frac{\\sum x_i}{n} = \\bar{X}$

The MLE is simply the sample mean!</pre>
        </div>

        <div class='worked-example'>
            <p><strong>Example: MLE for $\\text{Bernoulli}(p)$</strong></p>
            <p>Data: $k$ successes in $n$ trials.</p>
            <pre class='code-block'>Log-likelihood: $\\ell(p) = k \\ln p + (n-k) \\ln(1-p)$

$\\frac{d\\ell}{dp} = \\frac{k}{p} - \\frac{n-k}{1-p} = 0$

Solving: $\\frac{k}{p} = \\frac{n-k}{1-p}$
$k(1-p) = (n-k)p$
$k = np$
$\\hat{p}_{\\text{MLE}} = k/n$ = sample proportion</pre>
        </div>

        <p><strong>Computational note:</strong> Many distributions have closed-form MLEs. When they don't, numerical optimization (gradient descent, Newton-Raphson) is needed.</p>
        """
    },
    {
        "title": "Properties of MLEs",
        "body": """
        <p>MLEs have several desirable asymptotic (large-sample) properties that make them popular:</p>

        <div class='concept-box'>
            <p><strong>1. Consistency:</strong> $\\hat{\\theta}_{\\text{MLE}}$ converges to the true $\\theta_0$ as $n \\to \\infty$ with probability 1.</p>
        </div>

        <p>This means: with enough data, the MLE gets arbitrarily close to the truth.</p>

        <div class='concept-box'>
            <p><strong>2. Asymptotic Normality:</strong> For large $n$, $\\hat{\\theta}_{\\text{MLE}}$ is approximately normally distributed:</p>
            <p>$$\\hat{\\theta}_{\\text{MLE}} \\sim N\\left(\\theta_0, \\frac{1}{nI(\\theta_0)}\\right) \\quad \\text{approximately}$$</p>
            <p>where $I(\\theta)$ is the Fisher Information.</p>
        </div>

        <p>This allows us to construct confidence intervals using the normal distribution for large samples.</p>

        <div class='concept-box'>
            <p><strong>3. Efficiency:</strong> Among all consistent estimators, the MLE achieves the smallest asymptotic variance (it's efficient). It attains the Cramer-Rao lower bound.</p>
        </div>

        <p>In plain language: no other estimator can be more precise asymptotically.</p>

        <div class='concept-box'>
            <p><strong>4. Invariance:</strong> If $\\phi = g(\\theta)$ is a transformation, then $\\hat{\\phi}_{\\text{MLE}} = g(\\hat{\\theta}_{\\text{MLE}})$.</p>
        </div>

        <p><strong>Example:</strong> If $\\hat{\\theta}_{\\text{MLE}} = 0.4$ is the MLE for $p$, and we want to estimate odds $= p/(1-p)$, then the MLE for odds is $0.4/0.6 = 2/3$.</p>

        <div class='warning-box'>
            <p><strong>Important caveat:</strong> MLEs may be biased for finite samples. For example, the MLE of $\\sigma$ in a normal distribution is biased (it underestimates). However, the bias shrinks as $n$ grows.</p>
        </div>

        <div class='success-box'>
            <p><strong>Fisher Information:</strong> $I(\\theta) = -E\\left[\\frac{d^2\\ell}{d\\theta^2}\\right]$ measures the curvature of the log-likelihood. Larger $I$ means $\\theta$ is estimated more precisely (smaller variance for the MLE).</p>
        </div>
        """
    }
]
