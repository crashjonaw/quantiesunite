SECTIONS = [
    {
        "title": "Differential Equations: Types and First Principles",
        "body": """
<h3>What is a Differential Equation?</h3>
<p>A <strong>differential equation</strong> is an equation involving a function and its derivatives.</p>

<p>Example: dy/dx + 2y = 6 or y'' + y' - 6y = 0</p>

<h3>Classification</h3>
<ul>
<li><strong>Order:</strong> The highest derivative present (first-order, second-order, etc.)</li>
<li><strong>Linearity:</strong> Linear (y and derivatives appear to power 1) vs. nonlinear</li>
<li><strong>Ordinary (ODE) vs. Partial (PDE):</strong> Ordinary = one independent variable; Partial = multiple independent variables</li>
</ul>

<p>We focus on first-order ODEs: dy/dx = f(x, y)</p>

<h3>Solution and Initial Conditions</h3>
<p>A <strong>general solution</strong> contains arbitrary constants. A <strong>particular solution</strong> satisfies an initial condition.</p>

<p>For dy/dx = f(x, y), an initial condition is y(x₀) = y₀ (specifies the function at one point).</p>

<div class="example-box">
<h4>Example 1: Verifying a Solution</h4>
<p>Verify that y = Ce^(2x) is a solution to dy/dx = 2y</p>
<p><strong>Solution:</strong> If y = Ce^(2x), then dy/dx = 2Ce^(2x) = 2y ✓</p>
<p>The general solution is y = Ce^(2x) with arbitrary constant C</p>
</div>
"""
    },
    {
        "title": "Separable Differential Equations: Integration Approach",
        "body": """
<h3>Separable Equations</h3>
<p>A first-order ODE is <strong>separable</strong> if it can be written as:</p>
<p style="text-align: center; font-weight: bold;">dy/dx = f(x)/g(y)  or equivalently  g(y)dy = f(x)dx</p>

<p><strong>Solution method:</strong> Integrate both sides:</p>
<p>∫g(y)dy = ∫f(x)dx + C</p>

<div class="example-box">
<h4>Example 2: Separable Equation</h4>
<p>Solve dy/dx = 2xy</p>
<p><strong>Solution:</strong> Rearrange: (1/y)dy = 2x dx</p>
<p>Integrate: ∫(1/y)dy = ∫2x dx</p>
<p>ln|y| = x² + C₁</p>
<p>|y| = e^(x² + C₁) = e^(C₁) · e^(x²) = Ae^(x²), where A = e^(C₁) > 0</p>
<p>General solution: y = Ce^(x²), where C is arbitrary (can be positive, negative, or zero)
</p>
</div>

<div class="example-box">
<h4>Example 3: Separable with Initial Condition</h4>
<p>Solve dy/dx = y² with y(0) = 1</p>
<p><strong>Solution:</strong> Rearrange: (1/y²)dy = dx</p>
<p>Integrate: ∫y⁻² dy = ∫dx</p>
<p>-1/y = x + C</p>
<p>Apply y(0) = 1: -1/1 = 0 + C ⟹ C = -1</p>
<p>-1/y = x - 1 ⟹ y = 1/(1 - x)</p>
</div>

<h3>Checking Separability</h3>
<p>Not all equations are separable. For example, dy/dx = x + y cannot be written as a product of a function of x and a function of y alone.</p>
"""
    },
    {
        "title": "Integrating Factor Method: For Linear First-Order ODEs",
        "body": """
<h3>Linear First-Order Form</h3>
<p>A linear first-order ODE has the standard form:</p>
<p style="text-align: center; font-weight: bold;">dy/dx + P(x)y = Q(x)</p>

<p>This is linear in y and dy/dx, but P and Q are arbitrary functions of x.</p>

<h3>The Integrating Factor Technique</h3>
<p>Multiply both sides by an <strong>integrating factor</strong> μ(x) chosen so the left side becomes d/dx[μy]:</p>

<p style="text-align: center; font-weight: bold;">μ(x) = e^(∫P(x)dx)</p>

<p><strong>Why?</strong> The product rule gives: d/dx[μy] = μ'y + μ(dy/dx) = μ(P(x)y + dy/dx)</p>

<p>So multiplying dy/dx + P(x)y = Q(x) by μ gives:</p>
<p>d/dx[μy] = μQ(x)</p>

<p>Integrate: μy = ∫μQ(x)dx + C</p>

<div class="example-box">
<h4>Example 4: Using Integrating Factor</h4>
<p>Solve dy/dx + 2y = 6</p>
<p><strong>Solution:</strong> P(x) = 2, so μ(x) = e^(∫2 dx) = e^(2x)</p>
<p>Multiply by μ: e^(2x)·dy/dx + 2e^(2x)·y = 6e^(2x)</p>
<p>d/dx[e^(2x)·y] = 6e^(2x)</p>
<p>Integrate: e^(2x)·y = ∫6e^(2x)dx = 3e^(2x) + C</p>
<p>y = 3 + Ce^(-2x)</p>
</div>

<div class="example-box">
<h4>Example 5: With Initial Condition</h4>
<p>Solve dy/dx + y/x = x with y(1) = 0</p>
<p><strong>Solution:</strong> P(x) = 1/x, so μ(x) = e^(∫(1/x)dx) = e^(ln|x|) = x</p>
<p>Multiply: x·dy/dx + y = x²</p>
<p>d/dx[xy] = x²</p>
<p>xy = ∫x² dx = x³/3 + C</p>
<p>y = x²/3 + C/x</p>
<p>Apply y(1) = 0: 0 = 1/3 + C ⟹ C = -1/3</p>
<p>y = x²/3 - 1/(3x)</p>
</div>

<h3>When to Use Each Method</h3>
<ul>
<li><strong>Separable:</strong> If dy/dx = f(x)g(y), use separation</li>
<li><strong>Linear (dy/dx + P(x)y = Q(x)):</strong> Use integrating factor</li>
<li><strong>Other forms:</strong> May require substitution or special techniques</li>
</ul>
"""
    },
    {
        "title": "Modelling with Differential Equations",
        "body": """
<h3>Setting Up Models</h3>
<p>Many real-world phenomena lead to differential equations:</p>

<p><strong>Newton's Second Law:</strong> F = ma = m(dv/dt) (force-mass-acceleration)</p>
<p><strong>Exponential growth/decay:</strong> dN/dt = kN (population, radioactivity)</p>
<p><strong>Cooling/heating:</strong> dT/dt = k(T - T_ambient) (Newton's Law of Cooling)</p>

<div class="example-box">
<h4>Example 6: Exponential Decay</h4>
<p>A radioactive substance decays at a rate proportional to its amount. If 100 g remains after 10 years and 80 g after 20 years, find the half-life.</p>
<p><strong>Solution:</strong> Let N(t) = amount at time t. The model is dN/dt = -kN (negative = decay)</p>
<p>This is separable: (1/N)dN = -k dt ⟹ ln|N| = -kt + C</p>
<p>N(t) = N₀e^(-kt), where N₀ is initial amount</p>
<p>From conditions: N(10) = 100, N(20) = 80</p>
<p>100 = N₀e^(-10k) and 80 = N₀e^(-20k)</p>
<p>Dividing: 100/80 = e^(10k) ⟹ 5/4 = e^(10k) ⟹ k = ln(5/4)/10 ≈ 0.0223 per year</p>
<p>Half-life: t₁/₂ where N(t₁/₂) = N₀/2 ⟹ e^(-kt₁/₂) = 1/2 ⟹ t₁/₂ = ln(2)/k ≈ 31 years</p>
</div>

<div class="example-box">
<h4>Example 7: Newton's Law of Cooling</h4>
<p>A cup of tea at 95°C is placed in a room at 20°C. After 5 minutes, it cools to 75°C. When will it reach 40°C?</p>
<p><strong>Solution:</strong> dT/dt = k(T - 20), where k is a constant</p>
<p>This is linear: dT/dt - kT = -20k</p>
<p>Using integrating factor: T(t) = 20 + Ce^(kt)</p>
<p>T(0) = 95: 95 = 20 + C ⟹ C = 75, so T(t) = 20 + 75e^(kt)</p>
<p>T(5) = 75: 75 = 20 + 75e^(5k) ⟹ e^(5k) = 11/15 ⟹ k = ln(11/15)/5 ≈ -0.0675</p>
<p>T(t) = 20 + 75e^(-0.0675t)</p>
<p>Find t when T = 40: 40 = 20 + 75e^(-0.0675t) ⟹ e^(-0.0675t) = 4/15</p>
<p>t = -ln(4/15)/0.0675 ≈ 18.4 minutes</p>
</div>

<h3>Validating Solutions</h3>
<p>Always check that the solution:</p>
<ol>
<li>Satisfies the differential equation (substitute back)</li>
<li>Satisfies initial conditions if given</li>
<li>Makes physical sense (reasonable units, sign, limiting behavior)</li>
</ol>
"""
    },
    {
        "title": "Direction Fields and Qualitative Analysis",
        "body": """
<h3>Direction Fields (Slope Fields)</h3>
<p>For dy/dx = f(x, y), a <strong>direction field</strong> plots small line segments with slope f(x, y) at each point (x, y).</p>

<p>Integral curves (solutions) flow along these direction segments, providing geometric insight without solving explicitly.</p>

<h3>Constructing Direction Fields</h3>
<p><strong>Procedure:</strong></p>
<ol>
<li>Choose a grid of points (x, y)</li>
<li>At each point, compute the slope m = f(x, y)</li>
<li>Draw a short line segment with slope m centered at (x, y)</li>
</ol>

<div class="example-box">
<h4>Example 8: Direction Field for dy/dx = y</h4>
<p>For the equation dy/dx = y:</p>
<p>At (0, 1): slope = 1</p>
<p>At (1, 1): slope = 1</p>
<p>At (1, 2): slope = 2</p>
<p>At (1, 0): slope = 0</p>
<p>At (1, -1): slope = -1</p>
<p>The field shows exponential-like behavior: curves flattening as y → 0, steepening as |y| increases</p>
</div>

<h3>Equilibrium Solutions and Stability</h3>
<p>A <strong>constant solution</strong> y = c satisfies dy/dx = 0. Setting f(x, c) = 0 gives equilibrium points.</p>

<p><strong>Stability:</strong></p>
<ul>
<li><strong>Stable (sink):</strong> Nearby solutions approach the equilibrium</li>
<li><strong>Unstable (source):</strong> Nearby solutions diverge from the equilibrium</li>
<li><strong>Neutrally stable:</strong> Solutions remain nearby but don't converge</li>
</ul>

<div class="example-box">
<h4>Example 9: Equilibria and Stability</h4>
<p>For dy/dx = y(1 - y), find equilibria and analyze stability</p>
<p><strong>Solution:</strong> Set dy/dx = 0: y(1 - y) = 0 ⟹ y = 0 or y = 1</p>
<p>At y = 0.5 (between 0 and 1): dy/dx = 0.5(0.5) = 0.25 > 0 (increasing)</p>
<p>At y = -0.5 (below 0): dy/dx = -0.5(1.5) = -0.75 < 0 (decreasing)</p>
<p>At y = 1.5 (above 1): dy/dx = 1.5(-0.5) = -0.75 < 0 (decreasing)</p>
<p>Conclusion: y = 0 is unstable (source); y = 1 is stable (sink)</p>
</div>

<h3>Qualitative Behavior Without Solving</h3>
<p>From a direction field, we can understand:</p>
<ul>
<li>Monotonicity (increasing/decreasing along solution curves)</li>
<li>Concavity (using d²y/dx² if available)</li>
<li>Asymptotic behavior (where solutions go as t → ∞)</li>
<li>Existence and uniqueness of solutions</li>
</ul>
"""
    }
]
