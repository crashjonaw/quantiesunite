TITLE = "Common Distributions in Probability and Statistics"

SECTIONS = [
    {
        "id": "ps_rv_discrete_summary",
        "title": "Summary of Discrete Distributions",
        "body": """
<h3>Overview Table</h3>

<p>The following table summarizes key discrete distributions, their PMFs, supports, and moments:</p>

<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align:left; padding:8px;">Distribution</th>
<th style="text-align:left; padding:8px;">PMF \\(p_X(x)\\)</th>
<th style="text-align:left; padding:8px;">Mean \\(E[X]\\)</th>
<th style="text-align:left; padding:8px;">Variance \\(\\text{Var}(X)\\)</th>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Bernoulli}(p)\\)</td>
<td style="padding:8px;">\\(p^x(1-p)^{1-x}\\), \\(x \\in \\{0,1\\}\\)</td>
<td style="padding:8px;">\\(p\\)</td>
<td style="padding:8px;">\\(p(1-p)\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Binomial}(n,p)\\)</td>
<td style="padding:8px;">\\(\\binom{n}{x}p^x(1-p)^{n-x}\\)</td>
<td style="padding:8px;">\\(np\\)</td>
<td style="padding:8px;">\\(np(1-p)\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Poisson}(\\lambda)\\)</td>
<td style="padding:8px;">\\(\\frac{e^{-\\lambda}\\lambda^x}{x!}\\)</td>
<td style="padding:8px;">\\(\\lambda\\)</td>
<td style="padding:8px;">\\(\\lambda\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Geometric}(p)\\)</td>
<td style="padding:8px;">\\((1-p)^{x-1}p\\), \\(x = 1, 2, \\ldots\\)</td>
<td style="padding:8px;">\\(\\frac{1}{p}\\)</td>
<td style="padding:8px;">\\(\\frac{1-p}{p^2}\\)</td>
</tr>
</table>
</div>

<h3>When to Use Each Distribution</h3>

<div class="worked-example">
<h4>Bernoulli: Single Binary Outcome</h4>
<p>Use Bernoulli when you have one trial with two possible outcomes (success/failure). Example: does a customer click on an ad (1) or not (0)?</p>
</div>

<div class="worked-example">
<h4>Binomial: Counting Successes</h4>
<p>Use Binomial when you perform \\(n\\) independent trials, each with success probability \\(p\\), and count total successes. Example: number of heads in 10 coin flips.</p>
</div>

<div class="worked-example">
<h4>Poisson: Rare Event Counts</h4>
<p>Use Poisson when counting rare events over a fixed time or space interval. The parameter \\(\\lambda\\) is the average count. Example: number of emails arriving in 1 hour, number of typos on a page.</p>
</div>

<div class="worked-example">
<h4>Geometric: Time to First Success</h4>
<p>Use Geometric when you repeat trials until the first success. The memoryless property is key: waiting more time doesn't change future probabilities. Example: number of card flips until you get an ace.</p>
</div>
"""
    },
    {
        "id": "ps_rv_continuous_summary",
        "title": "Summary of Continuous Distributions",
        "body": """
<h3>Overview Table</h3>

<p>The following table summarizes key continuous distributions, their PDFs, supports, and moments:</p>

<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align:left; padding:8px;">Distribution</th>
<th style="text-align:left; padding:8px;">Mean \\(E[X]\\)</th>
<th style="text-align:left; padding:8px;">Variance \\(\\text{Var}(X)\\)</th>
<th style="text-align:left; padding:8px;">Support</th>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Uniform}(a,b)\\)</td>
<td style="padding:8px;">\\(\\frac{a+b}{2}\\)</td>
<td style="padding:8px;">\\(\\frac{(b-a)^2}{12}\\)</td>
<td style="padding:8px;">\\([a, b]\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(N(\\mu, \\sigma^2)\\)</td>
<td style="padding:8px;">\\(\\mu\\)</td>
<td style="padding:8px;">\\(\\sigma^2\\)</td>
<td style="padding:8px;">\\(\\mathbb{R}\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Exp}(\\lambda)\\)</td>
<td style="padding:8px;">\\(\\frac{1}{\\lambda}\\)</td>
<td style="padding:8px;">\\(\\frac{1}{\\lambda^2}\\)</td>
<td style="padding:8px;">\\([0, \\infty)\\)</td>
</tr>
<tr >
<td style="padding:8px;">\\(\\text{Beta}(\\alpha, \\beta)\\)</td>
<td style="padding:8px;">\\(\\frac{\\alpha}{\\alpha+\\beta}\\)</td>
<td style="padding:8px;">\\(\\frac{\\alpha\\beta}{(\\alpha+\\beta)^2(\\alpha+\\beta+1)}\\)</td>
<td style="padding:8px;">\\([0, 1]\\)</td>
</tr>
</table>
</div>

<h3>When to Use Each Distribution</h3>

<div class="worked-example">
<h4>Uniform: No Information About Where</h4>
<p>Use Uniform when all points in an interval are equally likely. Example: random number generators, picking a random time in a day with no prior knowledge.</p>
</div>

<div class="worked-example">
<h4>Normal: Central Limit Theorem</h4>
<p>Use Normal when data represents a sum or average of many independent random effects. The Bell Curve is ubiquitous in nature, measurements, and statistical inference. Most of statistics relies on Normality.</p>
</div>

<div class="worked-example">
<h4>Exponential: Waiting Times</h4>
<p>Use Exponential for time until the next event in a memoryless process (like customer arrivals, radioactive decay, equipment failure). The memoryless property: \\(P(X > t+s | X > t) = P(X > s)\\).</p>
</div>

<div class="worked-example">
<h4>Beta: Proportions and Probabilities</h4>
<p>Use Beta to model quantities constrained to \\([0, 1]\\): proportions, probabilities, success rates. The Beta distribution is flexible: it can be symmetric, skewed left, skewed right, or U-shaped depending on \\(\\alpha\\) and \\(\\beta\\).</p>
</div>
"""
    },
    {
        "id": "ps_rv_relationships",
        "title": "Connections Between Distributions",
        "body": """
<h3>Limits and Approximations</h3>

<p>Many distributions are limits or special cases of others:</p>

<div class="formula-box">
<h4>Poisson as Limit of Binomial</h4>
<p>When \\(n \\to \\infty\\), \\(p \\to 0\\), and \\(np = \\lambda\\) stays fixed:</p>
$$\\text{Binomial}(n, p) \\xrightarrow{d} \\text{Poisson}(\\lambda)$$
<p><strong>Intuition:</strong> Many trials with small success probability approximates counting rare events.</p>
</div>

<div class="formula-box">
<h4>Normal as Limit of Binomial</h4>
<p>When \\(n\\) is large and \\(p\\) is not too close to 0 or 1:</p>
$$\\text{Binomial}(n, p) \\approx N(np, np(1-p))$$
<p>This is the content of the Central Limit Theorem for Binomial variables.</p>
</div>

<div class="formula-box">
<h4>Exponential and Poisson Connection</h4>
<p>If events arrive as a Poisson process with rate \\(\\lambda\\), then the time between events follows \\(\\text{Exp}(\\lambda)\\). These are dual perspectives on the same process.</p>
</div>

<h3>Relationships Involving Normal Distribution</h3>

<p>The Normal distribution connects to many others through transformations:</p>

<div class="success-box">
<ul>
<li><strong>Chi-Square:</strong> Sum of squared standard normals: if \\(Z_i \\sim N(0,1)\\) independently, then \\(\\sum_{i=1}^k Z_i^2 \\sim \\chi^2(k)\\)</li>
<li><strong>t-distribution:</strong> Ratio of normal to chi-square: \\(t = \\frac{Z}{\\sqrt{V/k}}\\) where \\(Z \\sim N(0,1)\\) and \\(V \\sim \\chi^2(k)\\)</li>
<li><strong>F-distribution:</strong> Ratio of two chi-squares: \\(F = \\frac{V_1/k_1}{V_2/k_2}\\) where \\(V_i \\sim \\chi^2(k_i)\\)</li>
</ul>
</div>

<p>These relationships are why the Normal distribution is central to statistics: transforming normals gives us the entire toolkit for inference.</p>
"""
    }
]
