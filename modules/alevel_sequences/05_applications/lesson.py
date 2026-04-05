TITLE = "Recurrence Relations and Real-World Applications"

SECTIONS = [
    {
        "title": "First and Second-Order Linear Recurrence Relations",
        "body": """
<h3>First-Order Linear Recurrence Relations</h3>

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
<h4>Example 1: First-Order Recurrence</h4>
<p><strong>Solve \\( a_n = 2a_{n-1} + 3 \\) with \\( a_1 = 5 \\):</strong></p>
<p>Try \\( a_n^{(p)} = k \\): \\( k = 2k + 3 \\) gives \\( k = -3 \\)</p>
<p>General: \\( a_n = A \\cdot 2^{n-1} - 3 \\)</p>
<p>Initial: \\( 5 = A - 3 \\) gives \\( A = 8 \\)</p>
<p><strong>Solution:</strong> \\( a_n = 4 \\cdot 2^n - 3 \\)</p>
</div>

<h3>Second-Order Linear Recurrence Relations</h3>

<div class="formula-box">
<h4>Standard Form and Characteristic Equation</h4>
<p>\\( a_n = ca_{n-1} + da_{n-2} \\)</p>
<p>Characteristic equation: \\( r^2 - cr - d = 0 \\)</p>
<p>If roots are \\( r_1, r_2 \\):</p>
$$a_n = Ar_1^n + Br_2^n$$
<p>(assuming \\( r_1 \\neq r_2 \\); if equal, use \\( An r_1^n \\))</p>
</div>

<div class="example-box">
<h4>Example 2: Fibonacci Sequence</h4>
<p><strong>Solve \\( a_n = a_{n-1} + a_{n-2} \\) with \\( a_1 = 1, a_2 = 1 \\):</strong></p>
<p>Characteristic: \\( r^2 - r - 1 = 0 \\) gives \\( r = \\frac{1 \\pm \\sqrt{5}}{2} \\)</p>
<p>Let \\( \\phi = \\frac{1+\\sqrt{5}}{2} \\) (golden ratio), \\( \\psi = \\frac{1-\\sqrt{5}}{2} \\)</p>
<p><strong>Binet's formula:</strong></p>
$$F_n = \\frac{\\phi^n - \\psi^n}{\\sqrt{5}}$$
</div>
"""
    },
    {
        "title": "Growth Models and Financial Applications",
        "body": """
<h3>Exponential and Logistic Growth Models</h3>

<div class="example-box">
<h4>Example 3: Exponential Growth</h4>
<p><strong>Bacteria double every hour, starting with 100:</strong></p>
<p>Recurrence: \\( P_n = 2P_{n-1} \\)</p>
<p>Solution: \\( P_n = 100 \\cdot 2^n \\)</p>
<p>After 10 hours: \\( P_{10} = 100 \\cdot 1024 = 102400 \\)</p>
</div>

<div class="example-box">
<h4>Example 4: Logistic Growth Model</h4>
<p><strong>Model with carrying capacity \\( K \\):</strong></p>
$$P_n = rP_{n-1}\\left(1 - \\frac{P_{n-1}}{K}\\right)$$
<p>Equilibrium at \\( P = 0 \\) and \\( P = K \\).</p>
<p>Behaviour depends on growth rate \\( r \\): stable for \\( r < 1 \\), oscillates for \\( 1 < r < 3 \\), chaotic for \\( r > 3.57 \\).</p>
</div>

<h3>Compound Interest and Financial Mathematics</h3>

<div class="example-box">
<h4>Example 5: Compound Interest</h4>
<p><strong>Amount after \\( n \\) years at interest rate \\( r \\) compounded annually:</strong></p>
$$A_n = A_0(1+r)^n$$
<p>This is a geometric sequence with ratio \\( 1 + r \\).</p>
<p>If \\( A_0 = 1000 \\) and \\( r = 0.05 \\): \\( A_{20} = 1000 \\times 1.05^{20} \\approx 2653 \\)</p>
</div>

<div class="example-box">
<h4>Example 6: Annuities and Present Value</h4>
<p><strong>Sum of geometrically-scaled payments determines loan amortization and pension valuations:</strong></p>
<p>Present value of an annuity: \\( PV = \\frac{PMT}{r} \\left[1 - \\frac{1}{(1+r)^n}\\right] \\)</p>
<p>Key insight: This is the sum of a geometric series, essential for understanding mortgages and retirement planning.</p>
</div>
"""
    }
]
