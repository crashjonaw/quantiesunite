TITLE = "Series Convergence Tests and Analysis"

SECTIONS = [
    {
        "title": "Series Foundations and Divergence Test",
        "body": """
<h3>Definitions: Series vs. Sequences</h3>

<div class="formula-box">
<h4>Series Definition</h4>
<p>A <strong>series</strong> is the sum of terms of a sequence:</p>
$$\\sum_{n=1}^{\\infty} a_n = \\lim_{N \\to \\infty} \\sum_{n=1}^{N} a_n = \\lim_{N \\to \\infty} S_N$$
<p>where \\( S_N \\) is the \\( N \\)-th partial sum.</p>
</div>

<h3>Divergence Test</h3>

<div class="success-box">
<h4>Nth Term Test for Divergence</h4>
<p>If \\( \\lim_{n \\to \\infty} a_n \\neq 0 \\), then \\( \\sum a_n \\) diverges.</p>
<p><strong>Note:</strong> If \\( a_n \\to 0 \\), the test is inconclusive.</p>
</div>

<div class="example-box">
<h4>Example 1: Divergence Test</h4>
<p><strong>Does \\( \\sum_{n=1}^{\\infty} \\frac{2n}{3n+1} \\) converge?</strong></p>
<p>\\( \\lim_{n \\to \\infty} \\frac{2n}{3n+1} = \\frac{2}{3} \\neq 0 \\), so the series diverges.</p>
</div>

<h3>Integral Test</h3>

<div class="success-box">
<h4>Integral Test</h4>
<p>Let \\( f(x) \\) be positive, decreasing, continuous for \\( x \\geq 1 \\), and \\( a_n = f(n) \\). Then:</p>
$$\\sum_{n=1}^{\\infty} a_n \\text{ and } \\int_1^{\\infty} f(x)\\,dx$$
<p>either both converge or both diverge.</p>
</div>

<div class="example-box">
<h4>Example 2: Integral Test</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{1}{n^2} \\):</strong></p>
$$\\int_1^{\\infty} \\frac{1}{x^2}\\,dx = \\left[-\\frac{1}{x}\\right]_1^{\\infty} = 1$$
<p>The integral converges, so the series converges.</p>
</div>
"""
    },
    {
        "title": "Comparison and Advanced Tests",
        "body": """
<h3>Comparison Tests</h3>

<div class="success-box">
<h4>Direct Comparison Test</h4>
<p>If \\( 0 \\leq a_n \\leq b_n \\) for all \\( n \\):</p>
<ul>
<li>If \\( \\sum b_n \\) converges, then \\( \\sum a_n \\) converges</li>
<li>If \\( \\sum a_n \\) diverges, then \\( \\sum b_n \\) diverges</li>
</ul>
</div>

<div class="example-box">
<h4>Example 3: Direct Comparison</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{1}{2^n + n} \\):</strong></p>
<p>\\( \\frac{1}{2^n + n} < \\frac{1}{2^n} \\), and \\( \\sum \\frac{1}{2^n} \\) (geometric) converges.</p>
<p>By comparison, \\( \\sum \\frac{1}{2^n + n} \\) converges.</p>
</div>

<h3>Ratio and Root Tests</h3>

<div class="success-box">
<h4>Ratio Test</h4>
<p>For \\( a_n > 0 \\), let \\( L = \\lim_{n \\to \\infty} \\frac{a_{n+1}}{a_n} \\):</p>
<ul>
<li>If \\( L < 1 \\): \\( \\sum a_n \\) converges</li>
<li>If \\( L > 1 \\): \\( \\sum a_n \\) diverges</li>
<li>If \\( L = 1 \\): inconclusive</li>
</ul>
</div>

<div class="example-box">
<h4>Example 4: Ratio Test</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{n!}{2^n} \\):</strong></p>
$$\\frac{a_{n+1}}{a_n} = \\frac{(n+1)!}{2^{n+1}} \\times \\frac{2^n}{n!} = \\frac{n+1}{2} \\to \\infty$$
<p>Since \\( L > 1 \\), the series diverges.</p>
</div>

<h3>Alternating Series and Convergence Types</h3>

<div class="success-box">
<h4>Alternating Series Test</h4>
<p>If \\( a_n > 0 \\), decreasing, and \\( \\lim a_n = 0 \\), then \\( \\sum (-1)^{n+1} a_n \\) converges.</p>
</div>

<div class="example-box">
<h4>Example 5: Alternating Harmonic Series</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1}}{n} \\):</strong></p>
<p>\\( a_n = \\frac{1}{n} \\) is decreasing and \\( \\lim \\frac{1}{n} = 0 \\).</p>
<p>By the alternating series test, the series converges conditionally.</p>
</div>

<div class="formula-box">
<h4>Classifications of Convergence</h4>
<ul>
<li><strong>Absolutely convergent:</strong> \\( \\sum |a_n| \\) converges</li>
<li><strong>Conditionally convergent:</strong> \\( \\sum a_n \\) converges but \\( \\sum |a_n| \\) diverges</li>
</ul>
</div>

<div class="example-box">
<h4>Example 6: Absolute vs. Conditional</h4>
<p>\\( \\sum \\frac{(-1)^{n+1}}{n^2} \\): Since \\( \\sum \\frac{1}{n^2} \\) converges, this is absolutely convergent.</p>
<p>\\( \\sum \\frac{(-1)^{n+1}}{n} \\): Converges, but \\( \\sum \\frac{1}{n} \\) diverges, so conditionally convergent.</p>
</div>
"""
    },
    {
        "title": "Telescoping Series and Method of Differences",
        "body": """
<h3>Telescoping Series</h3>

<div class="example-box">
<h4>Example 7: Telescoping Sum</h4>
<p><strong>Find \\( \\sum_{n=1}^{N} \\frac{1}{n(n+1)} \\):</strong></p>
<p>Using partial fractions: \\( \\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1} \\)</p>
$$\\sum_{n=1}^{N} \\left(\\frac{1}{n} - \\frac{1}{n+1}\\right) = 1 - \\frac{1}{N+1} \\to 1$$
<p>as \\( N \\to \\infty \\).</p>
</div>

<h3>Method of Differences</h3>

<div class="formula-box">
<h4>Sigma Notation and Partial Fractions</h4>
<p>To evaluate \\( \\sum_{k=1}^{n} f(k) \\), decompose \\( f(k) \\) using partial fractions to reveal telescoping patterns.</p>
<p>This technique simplifies expressions like \\( \\sum \\frac{1}{k(k+p)} \\).</p>
</div>

<div class="example-box">
<h4>Example 8: Method of Differences</h4>
<p><strong>Find \\( \\sum_{k=1}^{n} \\frac{1}{k(k+2)} \\):</strong></p>
<p>Partial fractions: \\( \\frac{1}{k(k+2)} = \\frac{1}{2}\\left(\\frac{1}{k} - \\frac{1}{k+2}\\right) \\)</p>
<p>Telescoping gives: \\( \\sum_{k=1}^{n} = \\frac{1}{2}\\left(1 + \\frac{1}{2} - \\frac{1}{n+1} - \\frac{1}{n+2}\\right) = \\frac{3n^2 + 4n}{4n(n+1)(n+2)} \\)</p>
</div>
"""
    }
]
