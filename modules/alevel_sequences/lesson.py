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
    },
    {
        "title": "Arithmetic and Geometric Sequences",
        "body": """
<h3>Arithmetic Sequences (AP)</h3>

<div class="formula-box">
<h4>Definition and General Term</h4>
<p>An arithmetic sequence has constant common difference \\( d \\):</p>
$$a_{n+1} = a_n + d$$
<p>The general term is:</p>
$$a_n = a_1 + (n-1)d$$
</div>

<div class="example-box">
<h4>Example 4: AP General Term</h4>
<p><strong>Find the 20th term of:</strong> \\( 3, 7, 11, 15, \\ldots \\)</p>
<p><strong>Solution:</strong> \\( a_1 = 3 \\), \\( d = 4 \\)</p>
$$a_{20} = 3 + 19 \\cdot 4 = 79$$
</div>

<h3>Sum of an AP</h3>

<div class="formula-box">
<h4>AP Sum Formula</h4>
<p>The sum of the first \\( n \\) terms of an AP is:</p>
$$S_n = \\frac{n}{2}(a_1 + a_n) = \\frac{n}{2}[2a_1 + (n-1)d]$$
</div>

<div class="example-box">
<h4>Example 5: Sum of AP</h4>
<p><strong>Find:</strong> \\( 1 + 4 + 7 + \\ldots + 100 \\)</p>
<p>With \\( a_1 = 1 \\), \\( d = 3 \\): \\( 100 = 1 + (n-1) \\cdot 3 \\) gives \\( n = 34 \\)</p>
$$S_{34} = \\frac{34}{2}(1 + 100) = 17 \\times 101 = 1717$$
</div>

<h3>Geometric Sequences (GP)</h3>

<div class="formula-box">
<h4>Definition and General Term</h4>
<p>A geometric sequence has constant common ratio \\( r \\):</p>
$$a_{n+1} = r \\cdot a_n$$
<p>General term:</p>
$$a_n = a_1 \\cdot r^{n-1}$$
</div>

<div class="example-box">
<h4>Example 6: GP General Term</h4>
<p><strong>Find the 10th term of:</strong> \\( 2, 6, 18, 54, \\ldots \\)</p>
<p>\\( a_1 = 2 \\), \\( r = 3 \\):</p>
$$a_{10} = 2 \\times 3^9 = 39366$$
</div>

<h3>Sum of a GP</h3>

<div class="formula-box">
<h4>Finite GP Sum</h4>
<p>For \\( r \\neq 1 \\):</p>
$$S_n = a_1 \\cdot \\frac{1 - r^n}{1 - r} = a_1 \\cdot \\frac{r^n - 1}{r - 1}$$
</div>

<div class="example-box">
<h4>Example 7: Sum of Finite GP</h4>
<p><strong>Find:</strong> \\( 1 + 2 + 4 + 8 + \\ldots + 512 \\)</p>
<p>\\( a_1 = 1 \\), \\( r = 2 \\), \\( a_n = 512 \\) gives \\( n = 10 \\)</p>
$$S_{10} = 1 \\times \\frac{2^{10} - 1}{2 - 1} = 1023$$
</div>

<h3>Infinite Geometric Series</h3>

<div class="formula-box">
<h4>Convergence of Infinite GP</h4>
<p>For geometric series \\( \\sum_{n=0}^{\\infty} a_1 r^{n-1} \\):</p>
<ul>
<li>If \\( |r| < 1 \\): series converges to \\( S = \\frac{a_1}{1-r} \\)</li>
<li>If \\( |r| \\geq 1 \\): series diverges</li>
</ul>
</div>

<div class="example-box">
<h4>Example 8: Infinite GP Sum</h4>
<p><strong>Find:</strong> \\( 1 + \\frac{1}{2} + \\frac{1}{4} + \\ldots \\)</p>
<p>\\( a_1 = 1 \\), \\( r = \\frac{1}{2} \\) (and \\( |r| < 1 \\))</p>
$$S = \\frac{1}{1 - 0.5} = 2$$
</div>
"""
    },
    {
        "title": "Series and Convergence Tests",
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
<h4>Example 9: Divergence Test</h4>
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
<h4>Example 10: Integral Test</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{1}{n^2} \\):</strong></p>
$$\\int_1^{\\infty} \\frac{1}{x^2}\\,dx = \\left[-\\frac{1}{x}\\right]_1^{\\infty} = 1$$
<p>The integral converges, so the series converges.</p>
</div>

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
<h4>Example 11: Direct Comparison</h4>
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
<h4>Example 12: Ratio Test</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{n!}{2^n} \\):</strong></p>
$$\\frac{a_{n+1}}{a_n} = \\frac{(n+1)!}{2^{n+1}} \\times \\frac{2^n}{n!} = \\frac{n+1}{2} \\to \\infty$$
<p>Since \\( L > 1 \\), the series diverges.</p>
</div>

<h3>Alternating Series</h3>

<div class="success-box">
<h4>Alternating Series Test</h4>
<p>If \\( a_n > 0 \\), decreasing, and \\( \\lim a_n = 0 \\), then \\( \\sum (-1)^{n+1} a_n \\) converges.</p>
</div>

<div class="example-box">
<h4>Example 13: Alternating Harmonic Series</h4>
<p><strong>Test \\( \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1}}{n} \\):</strong></p>
<p>\\( a_n = \\frac{1}{n} \\) is decreasing and \\( \\lim \\frac{1}{n} = 0 \\).</p>
<p>By the alternating series test, the series converges conditionally.</p>
</div>

<h3>Absolute vs. Conditional Convergence</h3>

<div class="formula-box">
<h4>Classifications</h4>
<ul>
<li><strong>Absolutely convergent:</strong> \\( \\sum |a_n| \\) converges</li>
<li><strong>Conditionally convergent:</strong> \\( \\sum a_n \\) converges but \\( \\sum |a_n| \\) diverges</li>
</ul>
</div>

<div class="example-box">
<h4>Example 14: Absolute vs. Conditional</h4>
<p>\\( \\sum \\frac{(-1)^{n+1}}{n^2} \\): Since \\( \\sum \\frac{1}{n^2} \\) converges, this is absolutely convergent.</p>
<p>\\( \\sum \\frac{(-1)^{n+1}}{n} \\): Converges, but \\( \\sum \\frac{1}{n} \\) diverges, so conditionally convergent.</p>
</div>

<h3>Telescoping Series</h3>

<div class="example-box">
<h4>Example 15: Telescoping Sum</h4>
<p><strong>Find \\( \\sum_{n=1}^{N} \\frac{1}{n(n+1)} \\):</strong></p>
<p>Using partial fractions: \\( \\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1} \\)</p>
$$\\sum_{n=1}^{N} \\left(\\frac{1}{n} - \\frac{1}{n+1}\\right) = 1 - \\frac{1}{N+1} \\to 1$$
<p>as \\( N \\to \\infty \\).</p>
</div>
"""
    },
    {
        "title": "Power Series and Taylor Expansions",
        "body": """
<h3>Power Series Definition</h3>

<div class="formula-box">
<h4>Power Series</h4>
<p>A power series centered at \\( x = a \\) is:</p>
$$\\sum_{n=0}^{\\infty} c_n (x - a)^n$$
<p>The <strong>radius of convergence</strong> \\( R \\) determines where the series converges.</p>
</div>

<div class="example-box">
<h4>Example 16: Radius of Convergence</h4>
<p><strong>Find \\( R \\) for \\( \\sum_{n=0}^{\\infty} \\frac{(x-2)^n}{n!} \\):</strong></p>
<p>By the ratio test:</p>
$$\\left|\\frac{c_{n+1}}{c_n}\\right| = \\frac{1}{n+1} \\to 0 < 1$$
<p>So \\( R = \\infty \\) (converges for all \\( x \\)).</p>
</div>

<h3>Taylor Series</h3>

<div class="formula-box">
<h4>Taylor Series Formula</h4>
<p>If \\( f \\) is infinitely differentiable at \\( x = a \\):</p>
$$\\sum_{n=0}^{\\infty} \\frac{f^{(n)}(a)}{n!}(x-a)^n$$
<p><strong>Maclaurin series</strong> (special case, \\( a = 0 \\)):</p>
$$\\sum_{n=0}^{\\infty} \\frac{f^{(n)}(0)}{n!}x^n$$
</div>

<div class="example-box">
<h4>Example 17: Maclaurin Series</h4>
<p><strong>Find Maclaurin series for \\( e^x \\):</strong></p>
<p>\\( f^{(n)}(x) = e^x \\), so \\( f^{(n)}(0) = 1 \\) for all \\( n \\).</p>
$$e^x = \\sum_{n=0}^{\\infty} \\frac{x^n}{n!} = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\ldots$$
</div>

<div class="example-box">
<h4>Example 18: Trigonometric Maclaurin Series</h4>
<p><strong>Standard expansions:</strong></p>
$$\\sin(x) = \\sum_{n=0}^{\\infty} \\frac{(-1)^n x^{2n+1}}{(2n+1)!}$$
$$\\cos(x) = \\sum_{n=0}^{\\infty} \\frac{(-1)^n x^{2n}}{(2n)!}$$
</div>

<h3>Operations on Power Series</h3>

<div class="success-box">
<h4>Differentiation and Integration</h4>
<p>Within the radius of convergence:</p>
$$\\frac{d}{dx} \\sum a_n x^n = \\sum n a_n x^{n-1}$$
$$\\int \\sum a_n x^n \\, dx = \\sum \\frac{a_n}{n+1} x^{n+1} + C$$
</div>

<div class="example-box">
<h4>Example 19: Integrating a Series</h4>
<p><strong>Given \\( \\ln(1+x) = \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} x^n}{n} \\), find \\( \\int_0^x \\ln(1+t)\\,dt \\):</strong></p>
$$\\int_0^x \\ln(1+t)\\,dt = \\int_0^x \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} t^n}{n} \\, dt = \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} x^{n+1}}{n(n+1)}$$
</div>

<h3>Binomial Series</h3>

<div class="formula-box">
<h4>Binomial Expansion</h4>
<p>For any real \\( \\alpha \\):</p>
$$(1+x)^\\alpha = \\sum_{n=0}^{\\infty} \\binom{\\alpha}{n} x^n$$
<p>where \\( \\binom{\\alpha}{n} = \\frac{\\alpha(\\alpha-1)\\cdots(\\alpha-n+1)}{n!} \\)</p>
</div>

<div class="example-box">
<h4>Example 20: Binomial Series</h4>
<p><strong>Expand \\( \\sqrt{1+x} = (1+x)^{1/2} \\):</strong></p>
$$\\sqrt{1+x} = 1 + \\frac{1}{2}x - \\frac{1}{8}x^2 + \\frac{1}{16}x^3 - \\ldots$$
<p>Valid for \\( |x| < 1 \\).</p>
</div>
"""
    },
    {
        "title": "Recurrence Relations and Applications",
        "body": """
<h3>Linear Recurrence Relations</h3>

<div class="formula-box">
<h4>First-Order Linear Recurrence</h4>
<p>Form: \\( a_n = ca_{n-1} + d \\)</p>
<p><strong>Solution method:</strong></p>
<ol>
<li>Homogeneous solution: \\( a_n^{(h)} = Ac^{n-1} \\)</li>
<li>Particular solution: try constant \\( a_n^{(p)} = k \\)</li>
<li>General: \\( a_n = Ac^{n-1} + k \\)</li>
<li>Use initial condition to find \\( A \\)</li>
</ol>
</div>

<div class="example-box">
<h4>Example 21: First-Order Recurrence</h4>
<p><strong>Solve \\( a_n = 2a_{n-1} + 3 \\) with \\( a_1 = 5 \\):</strong></p>
<p>Try \\( a_n^{(p)} = k \\): \\( k = 2k + 3 \\) gives \\( k = -3 \\)</p>
<p>General: \\( a_n = A \\cdot 2^{n-1} - 3 \\)</p>
<p>Initial: \\( 5 = A - 3 \\) gives \\( A = 8 \\)</p>
<p><strong>Solution:</strong> \\( a_n = 4 \\cdot 2^n - 3 \\)</p>
</div>

<h3>Second-Order Linear Recurrence</h3>

<div class="formula-box">
<h4>Standard Form and Characteristic Equation</h4>
<p>\\( a_n = ca_{n-1} + da_{n-2} \\)</p>
<p>Characteristic equation: \\( r^2 - cr - d = 0 \\)</p>
<p>If roots are \\( r_1, r_2 \\):</p>
$$a_n = Ar_1^n + Br_2^n$$
<p>(assuming \\( r_1 \\neq r_2 \\); if equal, use \\( An r_1^n \\))</p>
</div>

<div class="example-box">
<h4>Example 22: Fibonacci</h4>
<p><strong>Solve \\( a_n = a_{n-1} + a_{n-2} \\) with \\( a_1 = 1, a_2 = 1 \\):</strong></p>
<p>Characteristic: \\( r^2 - r - 1 = 0 \\) gives \\( r = \\frac{1 \\pm \\sqrt{5}}{2} \\)</p>
<p>Let \\( \\phi = \\frac{1+\\sqrt{5}}{2} \\) (golden ratio), \\( \\psi = \\frac{1-\\sqrt{5}}{2} \\)</p>
<p><strong>Binet's formula:</strong></p>
$$F_n = \\frac{\\phi^n - \\psi^n}{\\sqrt{5}}$$
</div>

<h3>Applications: Exponential and Logistic Growth</h3>

<div class="example-box">
<h4>Example 23: Exponential Growth</h4>
<p><strong>Bacteria double every hour, starting with 100:</strong></p>
<p>Recurrence: \\( P_n = 2P_{n-1} \\)</p>
<p>Solution: \\( P_n = 100 \\cdot 2^n \\)</p>
<p>After 10 hours: \\( P_{10} = 100 \\cdot 1024 = 102400 \\)</p>
</div>

<div class="example-box">
<h4>Example 24: Logistic Growth</h4>
<p><strong>Model with carrying capacity \\( K \\):</strong></p>
$$P_n = rP_{n-1}\\left(1 - \\frac{P_{n-1}}{K}\\right)$$
<p>Equilibrium at \\( P = 0 \\) and \\( P = K \\).</p>
<p>Behaviour depends on growth rate \\( r \\): stable for \\( r < 1 \\), oscillates for \\( 1 < r < 3 \\), chaotic for \\( r > 3.57 \\).</p>
</div>

<h3>Financial Applications</h3>

<div class="example-box">
<h4>Example 25: Compound Interest</h4>
<p><strong>Amount after \\( n \\) years at interest rate \\( r \\) compounded annually:</strong></p>
$$A_n = A_0(1+r)^n$$
<p>This is a geometric sequence with ratio \\( 1 + r \\).</p>
<p>If \\( A_0 = 1000 \\) and \\( r = 0.05 \\): \\( A_{20} = 1000 \\times 1.05^{20} \\approx 2653 \\)</p>
</div>
"""
    }
]
