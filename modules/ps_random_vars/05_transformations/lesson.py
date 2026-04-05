TITLE = "Transformations of Random Variables"

SECTIONS = [
    {
        "id": "ps_rv_transformations_intro",
        "title": "Transforming Random Variables",
        "body": """
<h3>The Core Problem</h3>

<p>In many applications, we have a random variable \\(X\\) with a known distribution, and we care about a function of it: \\(Y = g(X)\\). How do we find the distribution of \\(Y\\)?</p>

<div class="concept-box">
<p><strong>Question:</strong> If \\(X \\sim f_X\\) and \\(Y = g(X)\\), what is \\(f_Y\\)?</p>
</div>

<h3>Discrete Case: Direct Calculation</h3>

<p>For discrete \\(X\\), transformations are straightforward. We sum the probabilities of all \\(x\\) values that map to \\(y\\):</p>

<div class="formula-box">
<h4>Discrete Transformation</h4>
$$P(Y = y) = \\sum_{x: g(x) = y} P(X = x) = \\sum_{x: g(x) = y} p_X(x)$$
</div>

<div class="worked-example">
<h4>Example: Squaring a Bernoulli</h4>
<p>Let \\(X \\sim \\text{Bernoulli}(0.5)\\), so \\(X \\in \\{0, 1\\}\\). Define \\(Y = X^2\\).</p>
<p>Then \\(Y \\in \\{0, 1\\}\\) and \\(Y = X\\) (squaring 0 and 1 does not change them).</p>
<p>So \\(P(Y = y) = P(X = y)\\) and \\(Y \\sim \\text{Bernoulli}(0.5)\\).</p>
</div>

<div class="worked-example">
<h4>Example: Absolute Value of Normal</h4>
<p>Let \\(X \\sim N(0, 1)\\) (standard normal). Define \\(Y = |X|\\).</p>
<p>For \\(y > 0\\), the values \\(x = y\\) and \\(x = -y\\) both map to \\(Y = y\\):</p>
$$P(Y \\in dy) = P(X \\in dy) + P(X \\in -dy) = 2 \\cdot f_X(y) dy$$
<p>So \\(f_Y(y) = 2 \\phi(y)\\) for \\(y > 0\\), where \\(\\phi\\) is the standard normal PDF.</p>
</div>
"""
    },
    {
        "id": "ps_rv_change_of_variables",
        "title": "Change of Variables for Continuous Distributions",
        "body": """
<h3>The Jacobian Formula</h3>

<p>For continuous \\(X\\) and a strictly monotonic function \\(g\\), we can derive the PDF of \\(Y = g(X)\\):</p>

<div class="formula-box">
<h4>Change of Variables Formula</h4>
<p>If \\(Y = g(X)\\) where \\(g\\) is strictly monotonic (either increasing or decreasing) with inverse \\(g^{-1}\\), then:</p>
$$f_Y(y) = f_X(g^{-1}(y)) \\left| \\frac{d}{dy} g^{-1}(y) \\right|$$
<p>The absolute value of the derivative is called the <strong>Jacobian</strong> of the transformation.</p>
</div>

<p><strong>Intuition:</strong> The Jacobian accounts for how the transformation stretches or compresses probability density. If \\(g\\) is steep, the Jacobian is small, and probability gets compressed.</p>

<h3>Examples of Change of Variables</h3>

<div class="worked-example">
<h4>Example: Logarithm Transformation</h4>
<p>Let \\(X \\sim \\text{Exp}(1)\\) with PDF \\(f_X(x) = e^{-x}\\) for \\(x \\geq 0\\). Define \\(Y = \\ln(X)\\).</p>
<p>The inverse is \\(g^{-1}(y) = e^y\\) and the Jacobian is \\(\\frac{d}{dy} e^y = e^y\\).</p>
$$f_Y(y) = f_X(e^y) \\cdot e^y = e^{-e^y} \\cdot e^y = e^{y - e^y}$$
<p>for \\(y \\in \\mathbb{R}\\). This distribution (of log of exponential) is used in extreme value theory.</p>
</div>

<div class="worked-example">
<h4>Example: Linear Transformation</h4>
<p>Let \\(X \\sim N(\\mu, \\sigma^2)\\) and \\(Y = aX + b\\) where \\(a \\neq 0\\).</p>
<p>The inverse is \\(g^{-1}(y) = \\frac{y-b}{a}\\) and the Jacobian is \\(\\left|\\frac{1}{a}\\right|\\).</p>
$$f_Y(y) = f_X\\left(\\frac{y-b}{a}\\right) \\cdot \\left|\\frac{1}{a}\\right| = \\frac{1}{|a|\\sigma\\sqrt{2\\pi}} \\exp\\left(-\\frac{(y-b-a\\mu)^2}{2a^2\\sigma^2}\\right)$$
<p>Therefore \\(Y \\sim N(a\\mu + b, a^2\\sigma^2)\\): linear transformations of normals are normal.</p>
</div>

<h3>Multivariate Change of Variables</h3>

<div class="formula-box">
<h4>Multivariate Jacobian</h4>
<p>For a vector transformation \\(\\mathbf{Y} = \\mathbf{g}(\\mathbf{X})\\), the Jacobian is a determinant:</p>
$$f_\\mathbf{Y}(\\mathbf{y}) = f_\\mathbf{X}(\\mathbf{g}^{-1}(\\mathbf{y})) \\left| \\det \\frac{\\partial \\mathbf{g}^{-1}}{\\partial \\mathbf{y}} \\right|$$
<p>The determinant of the Jacobian matrix accounts for how the transformation stretches volumes in \\(\\mathbb{R}^d\\).</p>
</div>
"""
    },
    {
        "id": "ps_rv_order_stats",
        "title": "Order Statistics and Sampling Methods",
        "body": """
<h3>Order Statistics</h3>

<p>If \\(X_1, \\ldots, X_n\\) are independent identically distributed (i.i.d.) continuous random variables, and we sort them as \\(X_{(1)} \\leq X_{(2)} \\leq \\cdots \\leq X_{(n)}\\), these are the <strong>order statistics</strong>.</p>

<div class="formula-box">
<h4>Distribution of k-th Order Statistic</h4>
<p>The PDF of \\(X_{(k)}\\), the \\(k\\)-th smallest value, is:</p>
$$f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F_X(x)]^{k-1} [1-F_X(x)]^{n-k} f_X(x)$$
</div>

<p><strong>Interpretation:</strong> The formula comes from counting: we need \\(k-1\\) samples below \\(x\\), one sample near \\(x\\), and \\(n-k\\) samples above \\(x\\).</p>

<div class="worked-example">
<h4>Example: Maximum of Uniforms</h4>
<p>Let \\(X_i \\sim \\text{Uniform}(0, 1)\\) independently. The maximum \\(X_{(n)}\\) has CDF:</p>
$$F_{X_{(n)}}(x) = [F_X(x)]^n = x^n \\quad \\text{for } x \\in [0,1]$$
<p>So \\(f_{X_{(n)}}(x) = n x^{n-1}\\). The maximum is biased toward values close to 1.</p>
</div>

<h3>Inverse Transform Sampling</h3>

<p>A fundamental technique for generating samples from any continuous distribution:</p>

<div class="formula-box">
<h4>Inverse Transform Method</h4>
<p>Let \\(U \\sim \\text{Uniform}(0, 1)\\) and \\(F_X\\) be the CDF of the target distribution. Then:</p>
$$X = F_X^{-1}(U)$$
<p>has CDF \\(F_X\\).</p>
</div>

<p><strong>Proof:</strong> \\(P(X \\leq x) = P(F_X^{-1}(U) \\leq x) = P(U \\leq F_X(x)) = F_X(x)\\).</p>

<div class="worked-example">
<h4>Sampling Exponential Distribution</h4>
<p>The CDF of \\(\\text{Exp}(\\lambda)\\) is \\(F_X(x) = 1 - e^{-\\lambda x}\\).</p>
<p>Its inverse: \\(F_X^{-1}(u) = -\\frac{1}{\\lambda} \\ln(1 - u)\\).</p>
<p><strong>Algorithm:</strong> Sample \\(U \\sim \\text{Uniform}(0,1)\\) and compute \\(X = -\\frac{1}{\\lambda} \\ln(1 - U)\\).</p>
</div>

<h3>Rejection Sampling</h3>

<p>For distributions without a closed-form inverse CDF:</p>

<div class="formula-box">
<h4>Rejection Sampling Algorithm</h4>
<p>To sample from target PDF \\(f_X\\):</p>
<ol>
<li>Choose a proposal distribution \\(g(x)\\) such that \\(f_X(x) \\leq M \\cdot g(x)\\) for some constant \\(M\\)</li>
<li>Sample \\(X \\sim g\\) and \\(U \\sim \\text{Uniform}(0,1)\\) independently</li>
<li>If \\(U \\leq \\frac{f_X(X)}{M \\cdot g(X)}\\), accept \\(X\\); otherwise reject and repeat</li>
</ol>
</div>

<p><strong>Efficiency:</strong> The acceptance rate is \\(1/M\\). Higher \\(M\\) means more rejections but is necessary if the proposal is much larger than the target.</p>

<h3>Markov Chain Monte Carlo (MCMC)</h3>

<div class="success-box">
<h4>When to Use MCMC</h4>
<p>For high-dimensional distributions (where rejection sampling is prohibitively slow), MCMC methods like Metropolis-Hastings and Gibbs sampling are essential. These construct a Markov chain whose stationary distribution is the target. After a burn-in period, samples approximate draws from the target distribution.</p>
</div>

<p>MCMC is the workhorse of Bayesian inference and modern computational statistics. Its power is that it works in high dimensions where other methods fail.</p>
"""
    }
]
