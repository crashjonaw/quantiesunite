SECTIONS = [
    {
        "title": "Chain Rule: Derivation and Application",
        "body": """
<h3>The Chain Rule Theorem</h3>
<p>If y = f(u) and u = g(x), then:</p>
<p style="text-align: center; font-weight: bold;">dy/dx = (dy/du) · (du/dx)</p>

<p><strong>Proof (informal):</strong> For small changes δx and δu:</p>
<p>δy ≈ (dy/du)·δu and δu ≈ (du/dx)·δx</p>
<p>Therefore: δy ≈ (dy/du)·(du/dx)·δx</p>
<p>As δx → 0: dy/dx = (dy/du)·(du/dx)</p>

<p><strong>In Leibniz notation:</strong> The d's appear to "cancel": (dy/dx) = (dy/du)(du/dx)</p>

<h3>Examples and Applications</h3>

<div class="example-box">
<h4>Example 1: Simple Chain Rule</h4>
<p>Find d/dx[(3x² + 1)⁵]</p>
<p><strong>Solution:</strong> Let u = 3x² + 1. Then d/dx[(3x² + 1)⁵] = 5u⁴ · du/dx = 5(3x² + 1)⁴ · 6x = 30x(3x² + 1)⁴</p>
</div>

<div class="example-box">
<h4>Example 2: Composite with Trigonometry</h4>
<p>Find d/dx[sin(x²)]</p>
<p><strong>Solution:</strong> Let u = x². Then d/dx[sin(x²)] = cos(x²) · 2x = 2x·cos(x²)</p>
</div>

<h3>General Form: Nested Functions</h3>
<p>For y = f(g(h(x))), the chain rule extends:</p>
<p>dy/dx = (df/dg)(dg/dh)(dh/dx)</p>

<p>We differentiate from the outside in, multiplying derivatives at each layer.</p>
"""
    },
    {
        "title": "Product and Quotient Rules: Complete Derivation",
        "body": """
<h3>Product Rule</h3>
<p>If y = u(x) · v(x), then:</p>
<p style="text-align: center; font-weight: bold;">dy/dx = u'v + uv'  or  (uv)' = u'v + uv'</p>

<p><strong>Derivation:</strong> From first principles:</p>
<p>y(x+h) - y(x) = u(x+h)v(x+h) - u(x)v(x)</p>
<p>= u(x+h)[v(x+h) - v(x)] + v(x)[u(x+h) - u(x)]</p>
<p>Dividing by h and taking h → 0:</p>
<p>dy/dx = u(x)·v'(x) + v(x)·u'(x)</p>

<div class="example-box">
<h4>Example 3: Product Rule</h4>
<p>Find d/dx[x·e^x]</p>
<p><strong>Solution:</strong> d/dx[x·e^x] = 1·e^x + x·e^x = e^x(1 + x)</p>
</div>

<h3>Quotient Rule</h3>
<p>If y = u(x)/v(x), then:</p>
<p style="text-align: center; font-weight: bold;">dy/dx = (u'v - uv')/v²  or  (u/v)' = (u'v - uv')/v²</p>

<p><strong>Derivation:</strong> Apply product rule to u/v = u · (1/v):</p>
<p>d/dx[u/v] = u' · (1/v) + u · d/dx[1/v]</p>
<p>Now d/dx[1/v] = -v'/v² (by chain rule)</p>
<p>So: d/dx[u/v] = u'/v - uv'/v² = (u'v - uv')/v²</p>

<div class="example-box">
<h4>Example 4: Quotient Rule</h4>
<p>Find d/dx[(x² + 1)/(x - 1)]</p>
<p><strong>Solution:</strong> u = x² + 1, u' = 2x; v = x - 1, v' = 1</p>
<p>dy/dx = [(2x)(x - 1) - (x² + 1)(1)]/(x - 1)²</p>
<p>= [2x² - 2x - x² - 1]/(x - 1)² = (x² - 2x - 1)/(x - 1)²</p>
</div>

<h3>Selecting Rules Wisely</h3>
<p>When a quotient can be simplified or rewritten, it's often easier:</p>
<p>d/dx[x/(x² + 1)] = d/dx[x·(x² + 1)⁻¹]  (product rule)</p>
<p>Or directly with quotient rule—choose whichever is simplest.</p>
"""
    },
    {
        "title": "Implicit Differentiation: Variables on Both Sides",
        "body": """
<h3>Method and Principle</h3>
<p>When an equation relates x and y implicitly (not y = f(x) explicitly), differentiate both sides with respect to x:</p>

<p><strong>Key principle:</strong> When differentiating terms in y, multiply by dy/dx (chain rule).</p>

<div class="example-box">
<h4>Example 5: Implicit Differentiation</h4>
<p>Find dy/dx if x² + y² = 25</p>
<p><strong>Solution:</strong> Differentiate both sides:</p>
<p>d/dx[x²] + d/dx[y²] = d/dx[25]</p>
<p>2x + 2y(dy/dx) = 0</p>
<p>2y(dy/dx) = -2x</p>
<p>dy/dx = -x/y</p>
</div>

<div class="example-box">
<h4>Example 6: More Complex Implicit Function</h4>
<p>Find dy/dx if xy + e^y = 5</p>
<p><strong>Solution:</strong></p>
<p>d/dx[xy] + d/dx[e^y] = 0</p>
<p>y + x(dy/dx) + e^y(dy/dx) = 0</p>
<p>(x + e^y)(dy/dx) = -y</p>
<p>dy/dx = -y/(x + e^y)</p>
</div>

<h3>Finding the Derivative Explicitly</h3>
<p>After finding dy/dx in terms of both x and y, we can evaluate it at specific points.</p>

<p>To find d²y/dx² (second derivative), differentiate dy/dx again, treating dy/dx as a function.</p>

<div class="example-box">
<h4>Example 7: Second Derivative</h4>
<p>Find d²y/dx² for x² + y² = 25</p>
<p><strong>Solution:</strong> From Example 5: dy/dx = -x/y</p>
<p>Differentiate again: d/dx[dy/dx] = d/dx[-x/y]</p>
<p>= [-y - x(dy/dx)]/y² = [-y - x(-x/y)]/y²</p>
<p>= [-y + x²/y]/y² = [x² - y²]/y³ = -25/y³  (since x² + y² = 25)
</p>
</div>
"""
    },
    {
        "title": "Parametric Differentiation: dy/dx from Parametric Equations",
        "body": """
<h3>Parametric Forms and Their Derivatives</h3>
<p>A curve can be defined parametrically: x = x(t), y = y(t), where t is the parameter.</p>

<p>To find dy/dx (the slope of the curve), use:</p>
<p style="text-align: center; font-weight: bold;">dy/dx = (dy/dt) / (dx/dt) = y'(t) / x'(t), provided x'(t) ≠ 0</p>

<p><strong>Justification:</strong> By the chain rule: dy/dx = (dy/dt)(dt/dx) = (dy/dt) / (dx/dt)</p>

<div class="example-box">
<h4>Example 8: Parametric Derivative</h4>
<p>A curve is given by x = t², y = t³. Find dy/dx at t = 2</p>
<p><strong>Solution:</strong></p>
<p>dx/dt = 2t, dy/dt = 3t²</p>
<p>dy/dx = 3t² / 2t = 3t/2</p>
<p>At t = 2: dy/dx = 3(2)/2 = 3</p>
</div>

<h3>Second Derivatives for Parametric Equations</h3>
<p>To find d²y/dx², differentiate dy/dx with respect to t, then divide by dx/dt:</p>
<p style="text-align: center; font-weight: bold;">d²y/dx² = d/dt(dy/dx) / (dx/dt)</p>

<div class="example-box">
<h4>Example 9: Second Derivative Parametric</h4>
<p>For x = cos(t), y = sin(t), find d²y/dx² at t = π/4</p>
<p><strong>Solution:</strong></p>
<p>dx/dt = -sin(t), dy/dt = cos(t)</p>
<p>dy/dx = -cos(t)/sin(t) = -cot(t)</p>
<p>d/dt(dy/dx) = d/dt[-cot(t)] = csc²(t)</p>
<p>d²y/dx² = csc²(t) / (-sin(t)) = -csc³(t)</p>
<p>At t = π/4: d²y/dx² = -csc³(π/4) = -(√2)³ = -2√2</p>
</div>

<h3>Applications: Speed and Velocity</h3>
<p>In parametric form with parameter t = time, the speed along the curve is:</p>
<p style="text-align: center; font-weight: bold;">speed = √[(dx/dt)² + (dy/dt)²]</p>

<p>This represents the magnitude of the velocity vector.</p>
"""
    },
    {
        "title": "Related Rates and Maclaurin Series Introduction",
        "body": """
<h3>Related Rates: Connecting Changing Quantities</h3>
<p>When two variables both change with time, their rates of change are related via implicit differentiation.</p>

<p><strong>Strategy:</strong></p>
<ol>
<li>Set up an equation relating the variables</li>
<li>Differentiate both sides with respect to time t</li>
<li>Solve for the desired rate of change</li>
</ol>

<div class="example-box">
<h4>Example 10: Related Rates Problem</h4>
<p>A ladder of length 5 m leans against a wall. If the base is being pulled away at 1 m/s, how fast is the top sliding down when the base is 3 m from the wall?</p>
<p><strong>Solution:</strong> Let x = distance from wall, y = height on wall.</p>
<p>Constraint: x² + y² = 25</p>
<p>Given: dx/dt = 1 m/s at x = 3</p>
<p>At x = 3: y = √(25 - 9) = 4
<br>Differentiate: 2x(dx/dt) + 2y(dy/dt) = 0
<br>2(3)(1) + 2(4)(dy/dt) = 0
<br>6 + 8(dy/dt) = 0
<br>dy/dt = -3/4 m/s (negative means descending)
</p>
</div>

<h3>Maclaurin Series: Taylor Series Centered at Zero</h3>
<p>A differentiable function can be approximated by a power series:</p>
<p style="text-align: center; font-weight: bold;">f(x) = f(0) + f'(0)x + f''(0)x²/2! + f'''(0)x³/3! + ...</p>

<p><strong>General coefficient:</strong> a_n = f^(n)(0)/n!  (where f^(n) is the n-th derivative)</p>

<p><strong>Convergence:</strong> For many functions, this series converges for all x (or at least in an interval around 0).</p>

<div class="example-box">
<h4>Example 11: Maclaurin Series for e^x</h4>
<p>Find the first four terms of the Maclaurin series for e^x</p>
<p><strong>Solution:</strong> f(x) = e^x, so f^(n)(x) = e^x for all n</p>
<p>f^(n)(0) = 1 for all n
<br>e^x = 1 + x + x²/2! + x³/3! + ... = Σ(n=0 to ∞) x^n/n!
</p>
</div>

<div class="example-box">
<h4>Example 12: Maclaurin Series for sin(x)</h4>
<p>Find the Maclaurin series for sin(x)</p>
<p><strong>Solution:</strong> f(x) = sin(x)</p>
<p>f(0) = 0, f'(x) = cos(x) ⟹ f'(0) = 1
<br>f''(x) = -sin(x) ⟹ f''(0) = 0
<br>f'''(x) = -cos(x) ⟹ f'''(0) = -1
<br>f⁽⁴⁾(x) = sin(x) ⟹ f⁽⁴⁾(0) = 0
<br>sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ... = Σ(n=0 to ∞) (-1)^n · x^(2n+1) / (2n+1)!
</p>
</div>

<h3>Radius of Convergence</h3>
<p>A Maclaurin series converges within a radius R of x = 0. Common series:</p>
<ul>
<li>e^x: converges for all x (R = ∞)</li>
<li>sin(x), cos(x): converge for all x (R = ∞)</li>
<li>1/(1-x): converges for |x| < 1 (R = 1)</li>
<li>ln(1+x): converges for -1 < x ≤ 1 (R = 1)</li>
</ul>
"""
    }
]
