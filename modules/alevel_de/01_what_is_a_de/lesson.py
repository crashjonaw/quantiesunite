TITLE = "What is a Differential Equation?"

SECTIONS = [
    {
        "title": "Differential Equations: Types and First Principles",
        "body": """
<h3>What is a Differential Equation?</h3>
<p>A <strong>differential equation</strong> is an equation involving a function and its derivatives.</p>

<p>Example: $\\frac{dy}{dx} + 2y = 6$ or $y'' + y' - 6y = 0$</p>

<h3>Classification</h3>
<ul>
<li><strong>Order:</strong> The highest derivative present (first-order, second-order, etc.)</li>
<li><strong>Linearity:</strong> Linear ($y$ and derivatives appear to power 1) vs. nonlinear</li>
<li><strong>Ordinary (ODE) vs. Partial (PDE):</strong> Ordinary = one independent variable; Partial = multiple independent variables</li>
</ul>

<p>We focus on first-order ODEs: $\\frac{dy}{dx} = f(x, y)$</p>

<h3>Solution and Initial Conditions</h3>
<p>A <strong>general solution</strong> contains arbitrary constants. A <strong>particular solution</strong> satisfies an initial condition.</p>

<p>For $\\frac{dy}{dx} = f(x, y)$, an initial condition is $y(x_0) = y_0$ (specifies the function at one point).</p>

<div class="concept-box">
<h4>Example 1: Verifying a Solution</h4>
<p>Verify that $y = Ce^{2x}$ is a solution to $\\frac{dy}{dx} = 2y$</p>
<p><strong>Solution:</strong> If $y = Ce^{2x}$, then $\\frac{dy}{dx} = 2Ce^{2x} = 2y$ ✓</p>
<p>The general solution is $y = Ce^{2x}$ with arbitrary constant $C$</p>
</div>
"""
    }
]
