TITLE = "Discrete Random Variables: PMF and CDF"

SECTIONS = [
    {
        "id": "ps_rv_pmf",
        "title": "Probability Mass Function",
        "body": """
<h3>PMF Definition and Properties</h3>

<p>For a discrete random variable \\(X\\) taking values in \\(\\{x_1, x_2, x_3, \\ldots\\}\\), the <strong>probability mass function</strong> assigns:</p>

$$p_X(x) = P(X = x)$$

<p>This function satisfies two fundamental properties:</p>
<ul>
<li>\\(p_X(x) \\geq 0\\) for all \\(x\\) (non-negativity)</li>
<li>\\(\\sum_{i} p_X(x_i) = 1\\) (normalization)</li>
</ul>

<div class="success-box">
<p>The PMF completely describes the probability distribution of a discrete random variable. Every question about probabilities can be answered from the PMF.</p>
</div>

<h3>Key Discrete Distributions</h3>

<div class="formula-box">
<h4>Bernoulli Distribution</h4>
<p>\\(X \\sim \\text{Bernoulli}(p)\\): a single trial with success probability \\(p\\).</p>
$$P(X = 1) = p, \\quad P(X = 0) = 1 - p$$
<p>Support: \\(\\{0, 1\\}\\). Models a single coin flip or binary outcome.</p>
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
<p>The geometric distribution is <strong>memoryless</strong>: future failures do not depend on past failures.</p>
</div>

<h3>Visualization: PMF as a Bar Chart</h3>

<p>Discrete distributions are best visualized as bar charts. The height of each bar at \\(x_i\\) is \\(p_X(x_i)\\).</p>

<div class="chart-container">
<canvas data-chart='{
  "type": "bar",
  "data": {
    "labels": ["0", "1", "2", "3", "4", "5"],
    "datasets": [{
      "label": "Binomial(5, 0.5)",
      "data": [0.0313, 0.1563, 0.3125, 0.3125, 0.1563, 0.0313],
      "backgroundColor": "rgba(79, 142, 247, 0.8)"
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {"title": {"text": "PMF of Binomial(5, 0.5)"}},
    "scales": {"y": {"beginAtZero": true, "max": 0.35}}
  }
}'></canvas>
</div>
"""
    },
    {
        "id": "ps_rv_cdf_discrete",
        "title": "Cumulative Distribution Function",
        "body": """
<h3>CDF Definition and Properties</h3>

<p>The CDF \\(F_X(x) = P(X \\leq x)\\) gives cumulative probabilities:</p>

<div class="formula-box">
<h4>CDF for Discrete RV</h4>
$$F_X(x) = \\sum_{x_i \\leq x} p_X(x_i)$$
</div>

<p>The CDF tells us: "What is the probability that \\(X\\) is at most \\(x\\)?"</p>

<h3>Key Properties of the CDF</h3>

<div class="success-box">
<ul>
<li>\\(F_X(x)\\) is non-decreasing: if \\(a < b\\), then \\(F_X(a) \\leq F_X(b)\\)</li>
<li>\\(F_X(x)\\) is right-continuous</li>
<li>\\(\\lim_{x \\to -\\infty} F_X(x) = 0\\) and \\(\\lim_{x \\to \\infty} F_X(x) = 1\\)</li>
<li>For discrete \\(X\\), \\(F_X\\) is a step function with jumps at the support points</li>
</ul>
</div>

<h3>Relationship Between PMF and CDF</h3>

<p>The PMF and CDF encode the same information in different forms:</p>

$$p_X(x) = F_X(x) - F_X(x^-)$$

<p>where \\(F_X(x^-)\\) is the limit as we approach \\(x\\) from the left. For a discrete RV, this is the size of the jump at \\(x\\).</p>

<div class="worked-example">
<h4>Example: Fair Die</h4>
<p>Rolling a fair die: \\(X \\in \\{1,2,3,4,5,6\\}\\) with \\(p_X(k) = 1/6\\).</p>
<p>Then \\(F_X(3.5) = P(X \\leq 3.5) = P(X \\in \\{1,2,3\\}) = 3/6 = 1/2\\).</p>
<p>The CDF jumps by \\(1/6\\) at each integer in \\(\\{1, 2, \\ldots, 6\\}\\).</p>
</div>

<h3>Using the CDF for Probabilities</h3>

<p>Any probability of a range can be computed from the CDF:</p>

<div class="formula-box">
<h4>Range Probability</h4>
$$P(a \\leq X \\leq b) = F_X(b) - F_X(a^-)$$
</div>

<p>For discrete \\(X\\) with integer support, this becomes \\(F_X(b) - F_X(a-1)\\).</p>
"""
    },
    {
        "id": "ps_rv_joint_discrete",
        "title": "Joint and Conditional Distributions",
        "body": """
<h3>Joint PMF</h3>

<p>When we have multiple discrete random variables, their <strong>joint PMF</strong> describes their combined behavior:</p>

<div class="formula-box">
<h4>Joint PMF Definition</h4>
<p>For discrete random variables \\(X\\) and \\(Y\\):</p>
$$p_{X,Y}(x, y) = P(X = x, Y = y)$$
<p>This satisfies \\(p_{X,Y}(x,y) \\geq 0\\) and \\(\\sum_{x,y} p_{X,Y}(x,y) = 1\\).</p>
</div>

<h3>Marginal and Conditional Distributions</h3>

<p>From the joint distribution, we can recover individual (marginal) distributions:</p>

<div class="formula-box">
<h4>Marginal PMF</h4>
$$p_X(x) = \\sum_y p_{X,Y}(x, y)$$
$$p_Y(y) = \\sum_x p_{X,Y}(x, y)$$
</div>

<p>The <strong>conditional PMF</strong> describes the distribution of \\(Y\\) given that \\(X = x\\):</p>

<div class="formula-box">
<h4>Conditional PMF</h4>
$$p_{Y|X}(y|x) = \\frac{p_{X,Y}(x, y)}{p_X(x)}$$
</div>

<h3>Independence</h3>

<p>Two discrete random variables \\(X\\) and \\(Y\\) are <strong>independent</strong> if:</p>

<div class="formula-box">
<h4>Independence Condition</h4>
$$p_{X,Y}(x, y) = p_X(x) \\cdot p_Y(y) \\quad \\text{for all } x, y$$
</div>

<p>Independence means knowing the value of \\(X\\) tells us nothing about \\(Y\\). The joint distribution factorizes into a product of marginals.</p>

<div class="success-box">
<p>Independence is a strong assumption. In real data, variables are often correlated. Always check whether independence is reasonable for your problem.</p>
</div>
"""
    }
]
