TITLE = "Separable Differential Equations"

SECTIONS = [
    {
        "title": "Separable Equations: Integration Approach",
        "body": """
<h3>Separable Equations</h3>
<p>A first-order ODE is <strong>separable</strong> if it can be written as:</p>
<p>$$\\frac{dy}{dx} = \\frac{f(x)}{g(y)} \\quad \\text{or equivalently} \\quad g(y)\\,dy = f(x)\\,dx$$</p>

<p><strong>Solution method:</strong> Integrate both sides:</p>
<p>$$\\int g(y)\\,dy = \\int f(x)\\,dx + C$$</p>

<div class="worked-example">
<h4>Example 2: Separable Equation</h4>
<p>Solve $\\frac{dy}{dx} = 2xy$</p>
<p><strong>Solution:</strong> Rearrange: $\\frac{1}{y}\\,dy = 2x\\,dx$</p>
<p>Integrate: $\\int \\frac{1}{y}\\,dy = \\int 2x\\,dx$</p>
<p>$\\ln|y| = x^{2} + C_1$</p>
<p>$|y| = e^{x^{2} + C_1} = e^{C_1} \\cdot e^{x^{2}} = Ae^{x^{2}}$, where $A = e^{C_1} > 0$</p>
<p>General solution: $y = Ce^{x^{2}}$, where $C$ is arbitrary (can be positive, negative, or zero)</p>
</div>

<div class="worked-example">
<h4>Example 3: Separable with Initial Condition</h4>
<p>Solve $\\frac{dy}{dx} = y^{2}$ with $y(0) = 1$</p>
<p><strong>Solution:</strong> Rearrange: $\\frac{1}{y^{2}}\\,dy = dx$</p>
<p>Integrate: $\\int y^{-2}\\,dy = \\int dx$</p>
<p>$-\\frac{1}{y} = x + C$</p>
<p>Apply $y(0) = 1$: $-\\frac{1}{1} = 0 + C \\implies C = -1$</p>
<p>$-\\frac{1}{y} = x - 1 \\implies y = \\frac{1}{1 - x}$</p>
</div>

<h3>Checking Separability</h3>
<p>Not all equations are separable. For example, $\\frac{dy}{dx} = x + y$ cannot be written as a product of a function of $x$ and a function of $y$ alone.</p>
"""
    }
]
