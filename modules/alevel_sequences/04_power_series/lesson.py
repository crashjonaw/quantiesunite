TITLE = "Power Series and Taylor Expansions"

SECTIONS = [
    {
        "title": "Power Series Fundamentals",
        "body": """
<h3>Power Series Definition</h3>

<div class="formula-box">
<h4>Power Series</h4>
<p>A power series centered at \\( x = a \\) is:</p>
$$\\sum_{n=0}^{\\infty} c_n (x - a)^n$$
<p>The <strong>radius of convergence</strong> \\( R \\) determines where the series converges.</p>
</div>

<div class="example-box">
<h4>Example 1: Radius of Convergence</h4>
<p><strong>Find \\( R \\) for \\( \\sum_{n=0}^{\\infty} \\frac{(x-2)^n}{n!} \\):</strong></p>
<p>By the ratio test:</p>
$$\\left|\\frac{c_{n+1}}{c_n}\\right| = \\frac{1}{n+1} \\to 0 < 1$$
<p>So \\( R = \\infty \\) (converges for all \\( x \\)).</p>
</div>

<h3>Operations on Power Series</h3>

<div class="success-box">
<h4>Differentiation and Integration</h4>
<p>Within the radius of convergence:</p>
$$\\frac{d}{dx} \\sum a_n x^n = \\sum n a_n x^{n-1}$$
$$\\int \\sum a_n x^n \\, dx = \\sum \\frac{a_n}{n+1} x^{n+1} + C$$
</div>

<div class="example-box">
<h4>Example 2: Integrating a Series</h4>
<p><strong>Given \\( \\ln(1+x) = \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} x^n}{n} \\), find \\( \\int_0^x \\ln(1+t)\\,dt \\):</strong></p>
$$\\int_0^x \\ln(1+t)\\,dt = \\int_0^x \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} t^n}{n} \\, dt = \\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1} x^{n+1}}{n(n+1)}$$
</div>
"""
    },
    {
        "title": "Taylor and Maclaurin Series",
        "body": """
<h3>Taylor Series Formula</h3>

<div class="formula-box">
<h4>Taylor Series</h4>
<p>If \\( f \\) is infinitely differentiable at \\( x = a \\):</p>
$$\\sum_{n=0}^{\\infty} \\frac{f^{(n)}(a)}{n!}(x-a)^n$$
<p><strong>Maclaurin series</strong> (special case, \\( a = 0 \\)):</p>
$$\\sum_{n=0}^{\\infty} \\frac{f^{(n)}(0)}{n!}x^n$$
</div>

<div class="example-box">
<h4>Example 3: Maclaurin Series for \\( e^x \\)</h4>
<p><strong>Find Maclaurin series for \\( e^x \\):</strong></p>
<p>\\( f^{(n)}(x) = e^x \\), so \\( f^{(n)}(0) = 1 \\) for all \\( n \\).</p>
$$e^x = \\sum_{n=0}^{\\infty} \\frac{x^n}{n!} = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\ldots$$
</div>

<div class="example-box">
<h4>Example 4: Trigonometric Maclaurin Series</h4>
<p><strong>Standard expansions:</strong></p>
$$\\sin(x) = \\sum_{n=0}^{\\infty} \\frac{(-1)^n x^{2n+1}}{(2n+1)!}$$
$$\\cos(x) = \\sum_{n=0}^{\\infty} \\frac{(-1)^n x^{2n}}{(2n)!}$$
</div>

<h3>Binomial Series</h3>

<div class="formula-box">
<h4>Binomial Expansion</h4>
<p>For any real \\( \\alpha \\):</p>
$$(1+x)^\\alpha = \\sum_{n=0}^{\\infty} \\binom{\\alpha}{n} x^n$$
<p>where \\( \\binom{\\alpha}{n} = \\frac{\\alpha(\\alpha-1)\\cdots(\\alpha-n+1)}{n!} \\)</p>
</div>

<div class="example-box">
<h4>Example 5: Binomial Series for \\( \\sqrt{1+x} \\)</h4>
<p><strong>Expand \\( \\sqrt{1+x} = (1+x)^{1/2} \\):</strong></p>
$$\\sqrt{1+x} = 1 + \\frac{1}{2}x - \\frac{1}{8}x^2 + \\frac{1}{16}x^3 - \\ldots$$
<p>Valid for \\( |x| < 1 \\).</p>
</div>
"""
    }
]
