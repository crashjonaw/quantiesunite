TITLE = "Sequences and Limits: Foundations"

SECTIONS = [
    {
        "title": "Sequences: Definitions and Fundamental Properties",
        "body": """
<h3>What is a Sequence?</h3>
<p>A <strong>sequence</strong> is an ordered list of numbers, typically indexed by positive integers:</p>

<div class="formula-box">
<h4>Formal Definition</h4>
<p>A sequence is a function \\( a: \\mathbb{N} \\to \\mathbb{R} \\), often written as \\( \\{a_n\\}_{n=1}^{\\infty} \\) or \\( (a_1, a_2, a_3, \\ldots) \\).</p>
<p>The <strong>general term</strong> is \\( a_n \\), the \\( n \\)-th element.</p>
</div>

<h3>Convergence and Limits of Sequences</h3>

<div class="formula-box">
<h4>Limit Definition (Epsilon-Delta)</h4>
<p>We say \\( a_n \\to L \\) (or \\( \\lim_{n \\to \\infty} a_n = L \\)) if:</p>
<p>For every \\( \\epsilon > 0 \\), there exists \\( N \\in \\mathbb{N} \\) such that</p>
$$|a_n - L| < \\epsilon \\quad \\text{for all } n > N$$
<p>If the limit exists and is finite, the sequence <strong>converges</strong>; otherwise, it <strong>diverges</strong>.</p>
</div>

<div class="example-box">
<h4>Example 1: Proving Convergence</h4>
<p><strong>Prove:</strong> \\( \\lim_{n \\to \\infty} \\frac{1}{n} = 0 \\)</p>
<p><strong>Solution:</strong> Given \\( \\epsilon > 0 \\), we need \\( |\\frac{1}{n} - 0| = \\frac{1}{n} < \\epsilon \\).</p>
<p>This holds when \\( n > \\frac{1}{\\epsilon} \\). Choose \\( N = \\lceil \\frac{1}{\\epsilon} \\rceil \\). Then for all \\( n > N \\), we have \\( \\frac{1}{n} < \\epsilon \\).</p>
</div>

<h3>Monotonicity and Boundedness</h3>

<div class="formula-box">
<h4>Classification of Sequences</h4>
<ul>
<li><strong>Increasing:</strong> \\( a_n < a_{n+1} \\) for all \\( n \\)</li>
<li><strong>Decreasing:</strong> \\( a_n > a_{n+1} \\) for all \\( n \\)</li>
<li><strong>Monotonic:</strong> Either increasing or decreasing</li>
<li><strong>Bounded above:</strong> \\( \\exists M \\text{ such that } a_n \\leq M \\) for all \\( n \\)</li>
<li><strong>Bounded below:</strong> \\( \\exists m \\text{ such that } a_n \\geq m \\) for all \\( n \\)</li>
<li><strong>Bounded:</strong> Both bounded above and below</li>
</ul>
</div>

<h3>Monotone Convergence Theorem</h3>

<div class="success-box">
<h4>Theorem</h4>
<p>If \\( \\{a_n\\} \\) is monotonically increasing and bounded above, then \\( \\{a_n\\} \\) converges.</p>
<p>Similarly, a monotonically decreasing sequence bounded below converges.</p>
</div>

<div class="example-box">
<h4>Example 2: MCT Application</h4>
<p><strong>Analyze:</strong> \\( a_n = 1 - \\frac{1}{2^n} \\)</p>
<ul>
<li><strong>Monotonicity:</strong> \\( a_{n+1} - a_n = \\frac{1}{2^{n+1}} > 0 \\) → increasing</li>
<li><strong>Boundedness:</strong> \\( a_n < 1 \\) for all \\( n \\) (bounded above)</li>
<li><strong>Conclusion:</strong> By MCT, the sequence converges. Indeed, \\( \\lim_{n \\to \\infty} a_n = 1 \\).</li>
</ul>
</div>

<h3>Algebra of Limits</h3>

<div class="success-box">
<h4>Limit Laws</h4>
<p>If \\( a_n \\to L \\) and \\( b_n \\to M \\), then:</p>
<ul>
<li>\\( (a_n + b_n) \\to L + M \\)</li>
<li>\\( (a_n - b_n) \\to L - M \\)</li>
<li>\\( (a_n b_n) \\to LM \\)</li>
<li>\\( \\frac{a_n}{b_n} \\to \\frac{L}{M} \\) (if \\( M \\neq 0 \\))</li>
</ul>
</div>

<div class="example-box">
<h4>Example 3: Using Limit Laws</h4>
<p><strong>Find:</strong> \\( \\lim_{n \\to \\infty} \\frac{3n^2 + 2n + 1}{5n^2 - n} \\)</p>
<p><strong>Solution:</strong> Divide by \\( n^2 \\):</p>
$$\\lim_{n \\to \\infty} \\frac{3 + \\frac{2}{n} + \\frac{1}{n^2}}{5 - \\frac{1}{n}} = \\frac{3}{5}$$
</div>
"""
    }
]
