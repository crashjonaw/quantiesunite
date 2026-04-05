TITLE = "Related Rates and Maclaurin Series"

SECTIONS = [
    {
        "title": "Related Rates: Connecting Changing Quantities",
        "body": """
<h3>Related Rates: Connecting Changing Quantities</h3>
<p>When two variables both change with time, their rates of change are related via implicit differentiation.</p>

<p><strong>Strategy:</strong></p>
<ol>
<li>Set up an equation relating the variables</li>
<li>Differentiate both sides with respect to time $t$</li>
<li>Solve for the desired rate of change</li>
</ol>

<div class="worked-example">
<h4>Example 10: Related Rates Problem</h4>
<p>A ladder of length 5 m leans against a wall. If the base is being pulled away at 1 m/s, how fast is the top sliding down when the base is 3 m from the wall?</p>
<p><strong>Solution:</strong> Let $x$ = distance from wall, $y$ = height on wall.</p>
<p>Constraint: $x^{2} + y^{2} = 25$</p>
<p>Given: $\\frac{dx}{dt} = 1$ m/s at $x = 3$</p>
<p>At $x = 3$: $y = \\sqrt{25 - 9} = 4$</p>
<p>Differentiate: $2x\\frac{dx}{dt} + 2y\\frac{dy}{dt} = 0$</p>
<p>$2(3)(1) + 2(4)\\frac{dy}{dt} = 0$</p>
<p>$6 + 8\\frac{dy}{dt} = 0$</p>
<p>$\\frac{dy}{dt} = -\\frac{3}{4}$ m/s (negative means descending)</p>
</div>
"""
    },
    {
        "title": "Maclaurin Series: Taylor Series Centered at Zero",
        "body": """
<h3>Maclaurin Series: Taylor Series Centered at Zero</h3>
<p>A differentiable function can be approximated by a power series:</p>
<p>$$f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^{2} + \\frac{f'''(0)}{3!}x^{3} + \\cdots$$</p>

<p><strong>General coefficient:</strong> $a_{n} = \\frac{f^{(n)}(0)}{n!}$ (where $f^{(n)}$ is the $n$-th derivative)</p>

<p><strong>Convergence:</strong> For many functions, this series converges for all $x$ (or at least in an interval around 0).</p>

<div class="worked-example">
<h4>Example 11: Maclaurin Series for $e^{x}$</h4>
<p>Find the first four terms of the Maclaurin series for $e^{x}$</p>
<p><strong>Solution:</strong> $f(x) = e^{x}$, so $f^{(n)}(x) = e^{x}$ for all $n$</p>
<p>$f^{(n)}(0) = 1$ for all $n$</p>
<p>$e^{x} = 1 + x + \\frac{x^{2}}{2!} + \\frac{x^{3}}{3!} + \\cdots = \\sum_{n=0}^{\\infty} \\frac{x^{n}}{n!}$</p>
</div>

<div class="worked-example">
<h4>Example 12: Maclaurin Series for $\\sin(x)$</h4>
<p>Find the Maclaurin series for $\\sin(x)$</p>
<p><strong>Solution:</strong> $f(x) = \\sin(x)$</p>
<p>$f(0) = 0$, $f'(x) = \\cos(x) \\Rightarrow f'(0) = 1$</p>
<p>$f''(x) = -\\sin(x) \\Rightarrow f''(0) = 0$</p>
<p>$f'''(x) = -\\cos(x) \\Rightarrow f'''(0) = -1$</p>
<p>$f^{(4)}(x) = \\sin(x) \\Rightarrow f^{(4)}(0) = 0$</p>
<p>$\\sin(x) = x - \\frac{x^{3}}{3!} + \\frac{x^{5}}{5!} - \\frac{x^{7}}{7!} + \\cdots = \\sum_{n=0}^{\\infty} \\frac{(-1)^{n} \\cdot x^{2n+1}}{(2n+1)!}$</p>
</div>
"""
    },
    {
        "title": "Radius of Convergence",
        "body": """
<h3>Radius of Convergence</h3>
<p>A Maclaurin series converges within a radius $R$ of $x = 0$. Common series:</p>
<ul>
<li>$e^{x}$: converges for all $x$ ($R = \\infty$)</li>
<li>$\\sin(x)$, $\\cos(x)$: converge for all $x$ ($R = \\infty$)</li>
<li>$\\frac{1}{1-x}$: converges for $|x| < 1$ ($R = 1$)</li>
<li>$\\ln(1+x)$: converges for $-1 < x \\leq 1$ ($R = 1$)</li>
</ul>

<div class="concept-box">
<h4>Understanding Convergence</h4>
<p>The radius of convergence tells us the interval around $x = 0$ where the series accurately represents the function. Outside this interval, the series diverges and does not give valid approximations.</p>
</div>
"""
    }
]
