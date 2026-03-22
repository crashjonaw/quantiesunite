SECTIONS = [
    {
        "id": "ps_rv_motivation",
        "title": "From Outcomes to Numbers",
        "content": """
<div class="concept-box">
<h3>Why Random Variables?</h3>
<p>Probability is about outcomes in abstract sample spaces. But to do mathematics and statistics, we need <em>numbers</em>. A random variable is a function that maps abstract outcomes to real numbers. This transforms a coin flip (H or T) into 0 and 1. A stock price change (up or down or flat) becomes a real number. Random variables are the bridge between abstract probability and quantitative analysis.</p>
</div>

<h3>The Definition</h3>

<div class="formula-box">
<h4>Random Variable</h4>
<p>A random variable \\(X\\) is a function from the sample space \\(\\Omega\\) to the real numbers \\(\\mathbb{R}\\):</p>
$$X: \\Omega \\to \\mathbb{R}$$
<p>Given an outcome \\(\\omega \\in \\Omega\\), the random variable produces \\(X(\\omega)\\), a real number.</p>
</div>

<div class="example-box">
<h4>Example: Fair Coin Flip</h4>
<p>Sample space: \\(\\Omega = \\{H, T\\}\\). Define \\(X(H) = 1\\) and \\(X(T) = 0\\). Then \\(X\\) is a random variable that encodes heads as 1 and tails as 0.</p>
</div>

<div class="example-box">
<h4>Example: Rolling a Die</h4>
<p>Sample space: \\(\\Omega = \\{1,2,3,4,5,6\\}\\). We can define \\(X(\\omega) = \\omega\\) (the number itself). Or \\(X(\\omega) = 2\\omega\\) (double the number). Or \\(X(\\omega) = 1\\) if \\(\\omega\\) is even, \\(0\\) if odd. The choice depends on what we care about.</p>
</div>

<h3>Why the Name Random?</h3>

<p>\\(X\\) is deterministic: given \\(\\omega\\), \\(X(\\omega)\\) is fixed. But we do not know \\(\\omega\\) beforehand. So \\(X\\) appears random from our perspective. In reality, it is a function that becomes random through our uncertainty about the input.</p>

<h3>Notation: Events in Terms of X</h3>

<p>Instead of talking about outcomes \\(\\omega\\), we talk about the values of \\(X\\):</p>

<div class="formula-box">
<h4>Event Notation</h4>
<p>The event \\(\\{X = x\\}\\) means all outcomes \\(\\omega\\) for which \\(X(\\omega) = x\\):</p>
$$\\{X = x\\} = \\{\\omega \\in \\Omega : X(\\omega) = x\\}$$
</div>

<p>Similarly, \\(\\{X \\leq x\\}\\) means \\(\\{\\omega : X(\\omega) \\leq x\\}\\).</p>

<h3>Probability Distribution of X</h3>

<p>The key question: what is \\(P(X = x)\\)? This is the probability of the event \\(\\{X = x\\}\\):</p>

$$P(X = x) = P(\\{\\omega : X(\\omega) = x\\})$$

<p>The <strong>probability distribution</strong> of \\(X\\) is the function that assigns probabilities to all possible values of \\(X\\).</p>

<h3>Two Classes: Discrete and Continuous</h3>

<p>Random variables fall into two categories:</p>

<div class="formula-box">
<h4>Discrete Random Variable</h4>
<p>\\(X\\) takes values in a countable set (like \\(\\{0,1,2,\\ldots\\}\\) or \\(\\{0,1\\}\\)). The distribution is described by a <strong>probability mass function (PMF)\\):</p>
$$p_X(x) = P(X = x)$$
</div>

<div class="formula-box">
<h4>Continuous Random Variable</h4>
<p>\\(X\\) takes values in an uncountable set (like \\(\\mathbb{R}\\) or an interval). The distribution is described by a <strong>probability density function (PDF)\\):</p>
$$f_X(x) = \\frac{d}{dx} P(X \\leq x) = \\frac{d}{dx} F_X(x)$$
</div>

<p>where \\(F_X(x) = P(X \\leq x)\\) is the <strong>cumulative distribution function (CDF)\\).</p>

<h3>Key Property</h3>

<p>Probabilities must sum/integrate to 1:</p>

<div class="success-box">
<h4>For Discrete RV:</h4>
$$\\sum_{x} p_X(x) = 1$$
</div>

<div class="success-box">
<h4>For Continuous RV:</h4>
$$\\int_{-\\infty}^{\\infty} f_X(x) \\, dx = 1$$
</div>
"""
    },
    {
        "id": "ps_rv_discrete",
        "title": "Discrete Random Variables and PMF",
        "content": """
<h3>Probability Mass Function (PMF)</h3>

<p>For a discrete random variable \\(X\\) taking values in \\(\\{x_1, x_2, x_3, \\ldots\\}\\), the <strong>probability mass function\\) assigns:</p>

$$p_X(x) = P(X = x)$$

<p>This function satisfies:</p>
<ul>
<li>\\(p_X(x) \\geq 0\\) for all \\(x\\)</li>
<li>\\(\\sum_{i} p_X(x_i) = 1\\)</li>
</ul>

<h3>Common Discrete Distributions</h3>

<div class="formula-box">
<h4>Bernoulli Distribution</h4>
<p>\\(X \\sim \\text{Bernoulli}(p)\\): a single trial with success probability \\(p\\).</p>
$$P(X = 1) = p, \\quad P(X = 0) = 1 - p$$
<p>Support: \\(\\{0, 1\\}\\)</p>
</div>

<div class="formula-box">
<h4>Binomial Distribution</h4>
<p>\\(X \\sim \\text{Binomial}(n, p)\\): number of successes in \\(n\\) independent Bernoulli trials.</p>
$$P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}$$
<p>Support: \\(\\{0, 1, \\ldots, n\\}\\). The binomial coefficient accounts for the different orderings of \\(k\\) successes in \\(n\\) trials.</p>
</div>

<div class="formula-box">
<h4>Poisson Distribution</h4>
<p>\\(X \\sim \\text{Poisson}(\\lambda)\\): counts rare events in a fixed time interval.</p>
$$P(X = k) = \\frac{e^{-\\lambda} \\lambda^k}{k!}$$
<p>Support: \\(\\{0, 1, 2, \\ldots\\}\\). The Poisson is the limit of Binomial as \\(n \\to \\infty\\) and \\(p \\to 0\\) with \\(np = \\lambda\\) fixed.</p>
</div>

<div class="formula-box">
<h4>Geometric Distribution</h4>
<p>\\(X \\sim \\text{Geometric}(p)\\): number of trials until the first success.</p>
$$P(X = k) = (1-p)^{k-1} p \\quad k = 1, 2, 3, \\ldots$$
<p>The geometric distribution is memoryless: future failures do not depend on past failures.</p>
</div>

<h3>Visualization: PMF as a Bar Chart</h3>

<p>Discrete distributions are visualized as bar charts. The height of each bar at \\(x_i\\) is \\(p_X(x_i)\\).</p>

<div class="chart-container">
<canvas data-chart='{
  "type": "bar",
  "data": {
    "labels": ["0", "1", "2", "3", "4", "5"],
    "datasets": [{
      "label": "Binomial(5, 0.5)",
      "data": [0.0313, 0.1563, 0.3125, 0.3125, 0.1563, 0.0313],
      "backgroundColor": "rgba(100, 150, 255, 0.7)"
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {"title": {"text": "PMF of Binomial(5, 0.5)"}},
    "scales": {"y": {"beginAtZero": true, "max": 0.35}}
  }
}'></canvas>
</div>

<h3>Cumulative Distribution Function (CDF)</h3>

<p>The CDF \\(F_X(x) = P(X \\leq x)\\) gives cumulative probabilities:</p>

<div class="formula-box">
<h4>CDF for Discrete RV</h4>
$$F_X(x) = \\sum_{x_i \\leq x} p_X(x_i)$$
</div>

<p>The CDF is non-decreasing, right-continuous, and satisfies \\(\\lim_{x \\to -\\infty} F_X(x) = 0\\) and \\(\\lim_{x \\to \\infty} F_X(x) = 1\\).</p>

<div class="example-box">
<h4>Example: Fair Die</h4>
<p>Rolling a fair die: \\(X \\in \\{1,2,3,4,5,6\\}\\) with \\(p_X(k) = 1/6\\).</p>
<p>Then \\(F_X(3.5) = P(X \\leq 3.5) = P(X \\in \\{1,2,3\\}) = 3/6 = 1/2\\).</p>
</div>
"""
    },
    {
        "id": "ps_rv_continuous",
        "title": "Continuous Random Variables and PDF",
        "content": """
<h3>Probability Density Function (PDF)</h3>

<p>For a continuous random variable \\(X\\), we cannot have \\(P(X = x) > 0\\) for individual points (otherwise probabilities would exceed 1). Instead, we describe the distribution using a <strong>probability density function</strong>.</p>

<div class="formula-box">
<h4>PDF Definition</h4>
<p>A PDF \\(f_X(x)\\) is a non-negative function such that:</p>
$$P(a \\leq X \\leq b) = \\int_a^b f_X(x) \\, dx$$
<p>and \\(\\int_{-\\infty}^{\\infty} f_X(x) \\, dx = 1\\).</p>
</div>

<p>Intuition: the area under the curve from \\(a\\) to \\(b\\) gives the probability that \\(X\\) falls in the interval \\([a, b]\\).</p>

<h3>Cumulative Distribution Function (CDF)</h3>

<div class="formula-box">
<h4>CDF for Continuous RV</h4>
$$F_X(x) = P(X \\leq x) = \\int_{-\\infty}^{x} f_X(t) \\, dt$$
<p>The PDF is the derivative of the CDF:</p>
$$f_X(x) = \\frac{d}{dx} F_X(x)$$
</div>

<h3>Common Continuous Distributions</h3>

<div class="formula-box">
<h4>Uniform Distribution</h4>
<p>\\(X \\sim \\text{Uniform}(a, b)\\): \\(X\\) is equally likely anywhere in \\([a, b]\\).</p>
$$f_X(x) = \\begin{cases} \\frac{1}{b-a} & \\text{if } a \\leq x \\leq b \\\\ 0 & \\text{otherwise} \\end{cases}$$
</div>

<div class="formula-box">
<h4>Normal (Gaussian) Distribution</h4>
<p>\\(X \\sim N(\\mu, \\sigma^2)\\): the bell curve, central to probability theory.</p>
$$f_X(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} \\exp\\left(-\\frac{(x - \\mu)^2}{2\\sigma^2}\\right)$$
<p>Parameters: \\(\\mu\\) is the mean (center), \\(\\sigma^2\\) is the variance (spread).</p>
</div>

<div class="formula-box">
<h4>Exponential Distribution</h4>
<p>\\(X \\sim \\text{Exp}(\\lambda)\\): waiting time until the next event.</p>
$$f_X(x) = \\lambda e^{-\\lambda x} \\text{ for } x \\geq 0$$
<p>The exponential is memoryless, like the geometric distribution.</p>
</div>

<div class="formula-box">
<h4>Beta Distribution</h4>
<p>\\(X \\sim \\text{Beta}(\\alpha, \\beta)\\): flexible distribution on \\([0,1]\\), useful for modeling proportions.</p>
$$f_X(x) = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha)\\Gamma(\\beta)} x^{\\alpha - 1}(1-x)^{\\beta - 1}$$
</div>

<h3>Visualization: PDF as a Curve</h3>

<div class="chart-container">
<canvas data-chart='{
  "type": "line",
  "data": {
    "labels": ["-4", "-2", "0", "2", "4"],
    "datasets": [{
      "label": "N(0, 1)",
      "data": [0.0540, 0.0540, 0.3989, 0.0540, 0.0540],
      "borderColor": "rgba(100, 200, 100, 1)",
      "fill": true,
      "backgroundColor": "rgba(100, 200, 100, 0.2)",
      "tension": 0.4
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {"title": {"text": "PDF of Standard Normal N(0,1)"}},
    "scales": {"y": {"beginAtZero": true}}
  }
}'></canvas>
</div>

<h3>Key Insight: Probability Zero Events</h3>

<p>For a continuous \\(X\\), \\(P(X = x) = 0\\) for any specific \\(x\\). This is because:</p>

$$P(X = x) = \\int_x^x f_X(t) \\, dt = 0$$

<p>This seems paradoxical, but it is consistent: probabilities apply to intervals, not points. The event \\(X = x\\) has measure zero.</p>
"""
    },
    {
        "id": "ps_rv_multivariate",
        "title": "Multivariate Distributions",
        "content": """
<h3>Joint Distribution of Multiple Variables</h3>

<p>Often we care about multiple random variables together. For instance, height \\(H\\) and weight \\(W\\) are not independent; they are described by a <strong>joint distribution</strong>.</p>

<div class="formula-box">
<h4>Joint PMF (Discrete Case)</h4>
<p>For discrete random variables \\(X\\) and \\(Y\\):</p>
$$p_{X,Y}(x, y) = P(X = x, Y = y)$$
</div>

<div class="formula-box">
<h4>Joint PDF (Continuous Case)</h4>
<p>For continuous random variables \\(X\\) and \\(Y\\):</p>
$$P(a \\leq X \\leq b, c \\leq Y \\leq d) = \\int_c^d \\int_a^b f_{X,Y}(x, y) \\, dx \\, dy$$
</div>

<h3>Marginal Distributions</h3>

<p>From the joint distribution, we recover the individual (marginal) distributions:</p>

<div class="formula-box">
<h4>Marginal PMF</h4>
$$p_X(x) = \\sum_y p_{X,Y}(x, y)$$
$$p_Y(y) = \\sum_x p_{X,Y}(x, y)$$
</div>

<div class="formula-box">
<h4>Marginal PDF</h4>
$$f_X(x) = \\int_{-\\infty}^{\\infty} f_{X,Y}(x, y) \\, dy$$
$$f_Y(y) = \\int_{-\\infty}^{\\infty} f_{X,Y}(x, y) \\, dx$$
</div>

<h3>Independence in Terms of Random Variables</h3>

<p>Two random variables \\(X\\) and \\(Y\\) are independent if:</p>

<div class="formula-box">
<h4>Independence (Discrete)</h4>
$$p_{X,Y}(x, y) = p_X(x) \\cdot p_Y(y) \\text{ for all } x, y$$
</div>

<div class="formula-box">
<h4>Independence (Continuous)</h4>
$$f_{X,Y}(x, y) = f_X(x) \\cdot f_Y(y) \\text{ for all } x, y$$
</div>

<p>Independence means the joint distribution factorizes into a product of marginals.</p>

<h3>Conditional Distributions</h3>

<p>The conditional distribution of \\(Y\\) given \\(X = x\\):</p>

<div class="formula-box">
<h4>Conditional PMF</h4>
$$p_{Y|X}(y|x) = \\frac{p_{X,Y}(x, y)}{p_X(x)}$$
</div>

<div class="formula-box">
<h4>Conditional PDF</h4>
$$f_{Y|X}(y|x) = \\frac{f_{X,Y}(x, y)}{f_X(x)}$$
</div>

<h3>The Bivariate Normal Distribution</h3>

<p>A fundamental example: two jointly normal random variables.</p>

<div class="formula-box">
<h4>Bivariate Normal</h4>
<p>\\((X, Y) \\sim N(\\mu_X, \\mu_Y, \\sigma_X^2, \\sigma_Y^2, \\rho)\\) has joint PDF:</p>
$$f_{X,Y}(x,y) = \\frac{1}{2\\pi \\sigma_X \\sigma_Y \\sqrt{1-\\rho^2}} \\exp\\left( -\\frac{1}{2(1-\\rho^2)} \\left[ \\frac{(x-\\mu_X)^2}{\\sigma_X^2} - 2\\rho \\frac{(x-\\mu_X)(y-\\mu_Y)}{\\sigma_X \\sigma_Y} + \\frac{(y-\\mu_Y)^2}{\\sigma_Y^2} \\right] \\right)$$
<p>where \\(\\rho \\in (-1, 1)\\) is the correlation coefficient.</p>
</div>

<p>The marginal distributions are \\(X \\sim N(\\mu_X, \\sigma_X^2)\\) and \\(Y \\sim N(\\mu_Y, \\sigma_Y^2)\\). The conditional distribution \\(Y|X\\) is also normal.</p>
"""
    },
    {
        "id": "ps_rv_functions",
        "title": "Functions of Random Variables",
        "content": """
<h3>Transforming Random Variables</h3>

<p>Often we care about transformations: if \\(X\\) is a random variable and \\(g\\) is a function, what is the distribution of \\(Y = g(X)\\)?</p>

<h3>Discrete Case: Direct Calculation</h3>

<p>For discrete \\(X\\), transformations are straightforward:</p>

$$P(Y = y) = \\sum_{x: g(x) = y} P(X = x)$$

<div class="example-box">
<h4>Example: Squaring a Bernoulli</h4>
<p>Let \\(X \\sim \\text{Bernoulli}(0.5)\\), so \\(X \\in \\{0, 1\\}\\). Define \\(Y = X^2\\).</p>
<p>Then \\(Y \\in \\{0, 1\\}\\) and \\(Y = X\\). (Squaring 0 and 1 does not change them.) So \\(P(Y=y) = P(X=y)\\).</p>
</div>

<h3>Continuous Case: Change of Variables</h3>

<p>For continuous \\(X\\) and a strictly monotonic function \\(g\\):</p>

<div class="formula-box">
<h4>Change of Variables Formula</h4>
<p>If \\(Y = g(X)\\) and \\(g\\) is strictly monotonic with inverse \\(g^{-1}\\), then:</p>
$$f_Y(y) = f_X(g^{-1}(y)) \\left| \\frac{d}{dy} g^{-1}(y) \\right|$$
<p>The derivative term is the <em>Jacobian</em> of the transformation.</p>
</div>

<div class="example-box">
<h4>Example: Logarithm Transformation</h4>
<p>Let \\(X \\sim \\text{Exp}(1)\\) with PDF \\(f_X(x) = e^{-x}\\) for \\(x \\geq 0\\). Define \\(Y = \\ln(X)\\).</p>
<p>Then \\(g^{-1}(y) = e^y\\) and \\(\\frac{d}{dy} e^y = e^y\\).</p>
$$f_Y(y) = f_X(e^y) \\cdot e^y = e^{-e^y} \\cdot e^y = e^{y - e^y}$$
<p>for \\(y \\in \\mathbb{R}\\).</p>
</div>

<h3>The Box-Muller Transform</h3>

<p>A famous example: generating normal random variables from uniforms.</p>

<div class="formula-box">
<h4>Box-Muller Method</h4>
<p>Let \\(U_1, U_2\\) be independent \\(\\text{Uniform}(0,1)\\). Define:</p>
$$Z_1 = \\sqrt{-2 \\ln U_1} \\cos(2\\pi U_2)$$
$$Z_2 = \\sqrt{-2 \\ln U_1} \\sin(2\\pi U_2)$$
<p>Then \\(Z_1, Z_2\\) are independent \\(N(0, 1)\\) standard normals.</p>
</div>

<h3>Order Statistics</h3>

<p>If \\(X_1, \\ldots, X_n\\) are independent copies of a continuous \\(X\\), and we sort them as \\(X_{(1)} \\leq X_{(2)} \\leq \\cdots \\leq X_{(n)}\\), these are the <strong>order statistics</strong>.</p>

<div class="formula-box">
<h4>Distribution of k-th Order Statistic</h4>
<p>The PDF of \\(X_{(k)}\\) is:</p>
$$f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F_X(x)]^{k-1} [1-F_X(x)]^{n-k} f_X(x)$$
</div>

<p>Order statistics are crucial in nonparametric statistics and confidence intervals.</p>
"""
    },
    {
        "id": "ps_rv_generation",
        "title": "Generating and Sampling Random Variables",
        "content": """
<h3>Inverse Transform Method</h3>

<p>A fundamental technique: generating samples from any distribution using uniform random numbers.</p>

<div class="formula-box">
<h4>Inverse Transform Sampling</h4>
<p>Let \\(U \\sim \\text{Uniform}(0, 1)\\) and \\(F_X\\) be the CDF of the target distribution. Then:</p>
$$X = F_X^{-1}(U)$$
<p>has CDF \\(F_X\\).</p>
</div>

<p><strong>Proof:</strong> \\(P(X \\leq x) = P(F_X^{-1}(U) \\leq x) = P(U \\leq F_X(x)) = F_X(x)\\).</p>

<div class="example-box">
<h4>Exponential Distribution</h4>
<p>The CDF of \\(\\text{Exp}(\\lambda)\\) is \\(F_X(x) = 1 - e^{-\\lambda x}\\).</p>
<p>Its inverse: \\(F_X^{-1}(u) = -\\frac{1}{\\lambda} \\ln(1 - u)\\).</p>
<p>So to generate \\(X \\sim \\text{Exp}(\\lambda)\\), sample \\(U \\sim \\text{Uniform}(0,1)\\) and compute \\(X = -\\frac{1}{\\lambda} \\ln(1 - U)\\).</p>
</div>

<h3>Rejection Sampling</h3>

<p>For distributions without a closed-form inverse CDF, rejection sampling is useful.</p>

<div class="formula-box">
<h4>Rejection Sampling Algorithm</h4>
<p>To sample from \\(f_X\\):</p>
<ol>
<li>Choose a proposal distribution \\(g(x)\\) with \\(f_X(x) \\leq M \\cdot g(x)\\) for some \\(M\\)</li>
<li>Sample \\(X \\sim g\\) and \\(U \\sim \\text{Uniform}(0,1)\\)</li>
<li>If \\(U \\leq \\frac{f_X(X)}{M \\cdot g(X)}\\), accept \\(X\\); otherwise reject and repeat</li>
</ol>
</div>

<p>The efficiency is \\(1/M\\): higher \\(M\\) means more rejections.</p>

<h3>Markov Chain Monte Carlo (MCMC)</h3>

<p>For high-dimensional distributions, specialized methods like MCMC are essential.</p>

<div class="concept-box">
<h4>Metropolis-Hastings Algorithm (Conceptual)</h4>
<p>MCMC constructs a Markov chain whose stationary distribution is the target \\(f_X\\). By running the chain long enough, samples approximate draws from \\(f_X\\). Gibbs sampling is a special case used extensively in Bayesian statistics.</p>
</div>

<h3>Common Computational Methods</h3>

<p>Modern simulation relies on:</p>
<ul>
<li><strong>Inverse transform:</strong> Exact, fast, when CDF is available</li>
<li><strong>Rejection sampling:</strong> Simple but slower for high dimensions</li>
<li><strong>MCMC (Gibbs, Metropolis):</strong> Handles complex, high-dimensional distributions</li>
<li><strong>Variational inference:</strong> Approximate posteriors by optimization</li>
</ul>

<p>These techniques power Bayesian inference, machine learning, and uncertainty quantification.</p>
"""
    }
]
