TITLE = "What is a Random Variable?"

SECTIONS = [
    {
        "id": "ps_rv_motivation",
        "title": "From Outcomes to Numbers",
        "body": """
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

<div class="worked-example">
<h4>Example: Fair Coin Flip</h4>
<p>Sample space: \\(\\Omega = \\{H, T\\}\\). Define \\(X(H) = 1\\) and \\(X(T) = 0\\). Then \\(X\\) is a random variable that encodes heads as 1 and tails as 0.</p>
</div>

<div class="worked-example">
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
"""
    },
    {
        "id": "ps_rv_distribution",
        "title": "Probability Distribution and Classification",
        "body": """
<h3>Probability Distribution of X</h3>

<p>The key question: what is \\(P(X = x)\\)? This is the probability of the event \\(\\{X = x\\):</p>

$$P(X = x) = P(\\{\\omega : X(\\omega) = x\\})$$

<p>The <strong>probability distribution</strong> of \\(X\\) is the function that assigns probabilities to all possible values of \\(X\\).</p>

<h3>Two Classes: Discrete and Continuous</h3>

<p>Random variables fall into two fundamental categories:</p>

<div class="formula-box">
<h4>Discrete Random Variable</h4>
<p>\\(X\\) takes values in a countable set (like \\(\\{0,1,2,\\ldots\\}\\) or \\(\\{0,1\\}\\)). The distribution is described by a <strong>probability mass function (PMF)</strong>:</p>
$$p_X(x) = P(X = x)$$
</div>

<div class="formula-box">
<h4>Continuous Random Variable</h4>
<p>\\(X\\) takes values in an uncountable set (like \\(\\mathbb{R}\\) or an interval). The distribution is described by a <strong>probability density function (PDF)</strong>:</p>
$$f_X(x) = \\frac{d}{dx} P(X \\leq x) = \\frac{d}{dx} F_X(x)$$
</div>

<p>where \\(F_X(x) = P(X \\leq x)\\) is the <strong>cumulative distribution function (CDF)</strong>.</p>

<h3>Key Property: Normalization</h3>

<p>Probabilities must sum/integrate to 1:</p>

<div class="success-box">
<h4>For Discrete RV:</h4>
$$\\sum_{x} p_X(x) = 1$$
</div>

<div class="success-box">
<h4>For Continuous RV:</h4>
$$\\int_{-\\infty}^{\\infty} f_X(x) \\, dx = 1$$
</div>

<p>This normalization ensures that the total probability is 1—certain that \\(X\\) takes some value.</p>
"""
    }
]
