TITLE = "Continuous Random Variables: PDF and CDF"

SECTIONS = [
    {
        "id": "ps_rv_pdf_intro",
        "title": "Probability Density Function",
        "body": """
<h3>Why We Need PDF</h3>

<p>For a continuous random variable \\(X\\), we cannot have \\(P(X = x) > 0\\) for individual points (otherwise probabilities would exceed 1). Instead, we describe the distribution using a <strong>probability density function</strong> (PDF).</p>

<div class="concept-box">
<p><strong>Key Insight:</strong> For continuous \\(X\\), probability applies to <em>intervals</em>, not points. The PDF tells us the density of probability mass at each location.</p>
</div>

<h3>PDF Definition and Properties</h3>

<div class="formula-box">
<h4>Probability Density Function</h4>
<p>A PDF \\(f_X(x)\\) is a non-negative function such that:</p>
$$P(a \\leq X \\leq b) = \\int_a^b f_X(x) \\, dx$$
<p>and normalization requires:</p>
$$\\int_{-\\infty}^{\\infty} f_X(x) \\, dx = 1$$
</div>

<p><strong>Intuition:</strong> The area under the curve from \\(a\\) to \\(b\\) gives the probability that \\(X\\) falls in the interval \\([a, b]\\). The total area under the curve is 1.</p>

<h3>Key Property: Point Probability is Zero</h3>

<div class="warning-box">
<h4>Probability of a Single Point</h4>
<p>For any specific value \\(x\\), we have:</p>
$$P(X = x) = \\int_x^x f_X(t) \\, dt = 0$$
<p>This seems paradoxical, but it is mathematically consistent. Probabilities apply to intervals, not individual points. The event \\(X = x\\) has measure zero.</p>
</div>

<div class="worked-example">
<h4>Intuition: Why Is P(X = x) = 0?</h4>
<p>Think of a probability as "mass." If all mass is distributed continuously across an interval, no single point can have positive mass. But small intervals can. This is analogous to calculus: a continuous density \\(f(x)\\) has zero integral over a single point.</p>
</div>
"""
    },
    {
        "id": "ps_rv_cdf_continuous",
        "title": "CDF and Common Distributions",
        "body": """
<h3>Cumulative Distribution Function</h3>

<div class="formula-box">
<h4>CDF for Continuous RV</h4>
$$F_X(x) = P(X \\leq x) = \\int_{-\\infty}^{x} f_X(t) \\, dt$$
<p>The PDF is the derivative of the CDF:</p>
$$f_X(x) = \\frac{d}{dx} F_X(x)$$
</div>

<p>The CDF is continuous and strictly increasing (for distributions with positive density everywhere). It smoothly goes from 0 to 1.</p>

<h3>Key Continuous Distributions</h3>

<div class="formula-box">
<h4>Uniform Distribution</h4>
<p>\\(X \\sim \\text{Uniform}(a, b)\\): \\(X\\) is equally likely anywhere in \\([a, b]\\).</p>
$$f_X(x) = \\begin{cases} \\frac{1}{b-a} & \\text{if } a \\leq x \\leq b \\\\ 0 & \\text{otherwise} \\end{cases}$$
<p>Constant density over the interval—the simplest continuous distribution.</p>
</div>

<div class="formula-box">
<h4>Normal (Gaussian) Distribution</h4>
<p>\\(X \\sim N(\\mu, \\sigma^2)\\): the bell curve, central to probability theory and statistics.</p>
$$f_X(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} \\exp\\left(-\\frac{(x - \\mu)^2}{2\\sigma^2}\\right)$$
<p>Parameters: \\(\\mu\\) is the mean (center), \\(\\sigma^2\\) is the variance (spread).</p>
</div>

<div class="formula-box">
<h4>Exponential Distribution</h4>
<p>\\(X \\sim \\text{Exp}(\\lambda)\\): waiting time until the next event.</p>
$$f_X(x) = \\lambda e^{-\\lambda x} \\quad \\text{for } x \\geq 0$$
<p>Support: \\([0, \\infty)\\). The exponential is memoryless: \\(P(X > t+s | X > s) = P(X > t)\\).</p>
</div>

<div class="formula-box">
<h4>Beta Distribution</h4>
<p>\\(X \\sim \\text{Beta}(\\alpha, \\beta)\\): flexible distribution on \\([0,1]\\), useful for modeling proportions.</p>
$$f_X(x) = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha)\\Gamma(\\beta)} x^{\\alpha - 1}(1-x)^{\\beta - 1}$$
<p>Support: \\([0, 1]\\). Special case: \\(\\text{Beta}(1, 1) = \\text{Uniform}(0, 1)\\).</p>
</div>

<h3>Visualization: PDF as a Curve</h3>

<p>Continuous distributions are visualized as smooth curves. The area under the curve from \\(a\\) to \\(b\\) is the probability \\(P(a \\leq X \\leq b)\\).</p>

<div class="chart-container">
<canvas data-chart='{
  "type": "line",
  "data": {
    "labels": ["-4", "-2", "0", "2", "4"],
    "datasets": [{
      "label": "N(0, 1)",
      "data": [0.0540, 0.0540, 0.3989, 0.0540, 0.0540],
      "borderColor": "rgba(79, 142, 247, 1)",
      "fill": true,
      "backgroundColor": "rgba(79, 142, 247, 0.2)",
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
"""
    },
    {
        "id": "ps_rv_joint_continuous",
        "title": "Joint, Marginal, and Conditional Distributions",
        "body": """
<h3>Joint Distribution</h3>

<p>When we have multiple continuous random variables, their <strong>joint PDF</strong> describes their combined behavior.</p>

<div class="formula-box">
<h4>Joint PDF Definition</h4>
<p>For continuous random variables \\(X\\) and \\(Y\\):</p>
$$P(a \\leq X \\leq b, c \\leq Y \\leq d) = \\int_c^d \\int_a^b f_{X,Y}(x, y) \\, dx \\, dy$$
<p>Normalization: \\(\\int_{-\\infty}^{\\infty} \\int_{-\\infty}^{\\infty} f_{X,Y}(x, y) \\, dx \\, dy = 1\\).</p>
</div>

<h3>Marginal and Conditional Distributions</h3>

<p>From the joint PDF, we recover the individual marginal PDFs:</p>

<div class="formula-box">
<h4>Marginal PDF</h4>
$$f_X(x) = \\int_{-\\infty}^{\\infty} f_{X,Y}(x, y) \\, dy$$
$$f_Y(y) = \\int_{-\\infty}^{\\infty} f_{X,Y}(x, y) \\, dx$$
</div>

<p>The <strong>conditional PDF</strong> of \\(Y\\) given \\(X = x\\):</p>

<div class="formula-box">
<h4>Conditional PDF</h4>
$$f_{Y|X}(y|x) = \\frac{f_{X,Y}(x, y)}{f_X(x)}$$
</div>

<h3>Independence for Continuous Variables</h3>

<p>Two continuous random variables are independent if their joint PDF factorizes:</p>

<div class="formula-box">
<h4>Independence (Continuous)</h4>
$$f_{X,Y}(x, y) = f_X(x) \\cdot f_Y(y) \\quad \\text{for all } x, y$$
</div>

<h3>The Bivariate Normal Distribution</h3>

<p>A fundamental example: two jointly normal random variables with correlation.</p>

<div class="formula-box">
<h4>Bivariate Normal</h4>
<p>\\((X, Y) \\sim N(\\mu_X, \\mu_Y, \\sigma_X^2, \\sigma_Y^2, \\rho)\\) has joint PDF:</p>
$$f_{X,Y}(x,y) = \\frac{1}{2\\pi \\sigma_X \\sigma_Y \\sqrt{1-\\rho^2}} \\exp\\left( -\\frac{1}{2(1-\\rho^2)} \\left[ \\frac{(x-\\mu_X)^2}{\\sigma_X^2} - 2\\rho \\frac{(x-\\mu_X)(y-\\mu_Y)}{\\sigma_X \\sigma_Y} + \\frac{(y-\\mu_Y)^2}{\\sigma_Y^2} \\right] \\right)$$
<p>where \\(\\rho \\in (-1, 1)\\) is the correlation coefficient.</p>
</div>

<div class="success-box">
<p>The marginal distributions are \\(X \\sim N(\\mu_X, \\sigma_X^2)\\) and \\(Y \\sim N(\\mu_Y, \\sigma_Y^2)\\). The conditional distribution \\(Y|X\\) is also normal. Jointly normal variables are determined by their means, variances, and correlation.</p>
</div>
"""
    }
]
