TITLE = "Direction Fields and Qualitative Analysis"

SECTIONS = [
    {
        "title": "Direction Fields and Qualitative Analysis",
        "body": """
<h3>Direction Fields (Slope Fields)</h3>
<p>For $\\frac{dy}{dx} = f(x, y)$, a <strong>direction field</strong> plots small line segments with slope $f(x, y)$ at each point $(x, y)$.</p>

<p>Integral curves (solutions) flow along these direction segments, providing geometric insight without solving explicitly.</p>

<h3>Constructing Direction Fields</h3>
<p><strong>Procedure:</strong></p>
<ol>
<li>Choose a grid of points $(x, y)$</li>
<li>At each point, compute the slope $m = f(x, y)$</li>
<li>Draw a short line segment with slope $m$ centered at $(x, y)$</li>
</ol>

<div class="worked-example">
<h4>Example 8: Direction Field for $\\frac{dy}{dx} = y$</h4>
<p>For the equation $\\frac{dy}{dx} = y$:</p>
<p>At $(0, 1)$: slope $= 1$</p>
<p>At $(1, 1)$: slope $= 1$</p>
<p>At $(1, 2)$: slope $= 2$</p>
<p>At $(1, 0)$: slope $= 0$</p>
<p>At $(1, -1)$: slope $= -1$</p>
<p>The field shows exponential-like behavior: curves flattening as $y \\to 0$, steepening as $|y|$ increases</p>
</div>

<h3>Equilibrium Solutions and Stability</h3>
<p>A <strong>constant solution</strong> $y = c$ satisfies $\\frac{dy}{dx} = 0$. Setting $f(x, c) = 0$ gives equilibrium points.</p>

<p><strong>Stability:</strong></p>
<ul>
<li><strong>Stable (sink):</strong> Nearby solutions approach the equilibrium</li>
<li><strong>Unstable (source):</strong> Nearby solutions diverge from the equilibrium</li>
<li><strong>Neutrally stable:</strong> Solutions remain nearby but don't converge</li>
</ul>

<div class="worked-example">
<h4>Example 9: Equilibria and Stability</h4>
<p>For $\\frac{dy}{dx} = y(1 - y)$, find equilibria and analyze stability</p>
<p><strong>Solution:</strong> Set $\\frac{dy}{dx} = 0$: $y(1 - y) = 0 \\implies y = 0$ or $y = 1$</p>
<p>At $y = 0.5$ (between 0 and 1): $\\frac{dy}{dx} = 0.5(0.5) = 0.25 > 0$ (increasing)</p>
<p>At $y = -0.5$ (below 0): $\\frac{dy}{dx} = -0.5(1.5) = -0.75 < 0$ (decreasing)</p>
<p>At $y = 1.5$ (above 1): $\\frac{dy}{dx} = 1.5(-0.5) = -0.75 < 0$ (decreasing)</p>
<p>Conclusion: $y = 0$ is unstable (source); $y = 1$ is stable (sink)</p>
</div>

<h3>Qualitative Behavior Without Solving</h3>
<p>From a direction field, we can understand:</p>
<ul>
<li>Monotonicity (increasing/decreasing along solution curves)</li>
<li>Concavity (using $\\frac{d^{2}y}{dx^{2}}$ if available)</li>
<li>Asymptotic behavior (where solutions go as $t \\to \\infty$)</li>
<li>Existence and uniqueness of solutions</li>
</ul>
"""
    }
]
