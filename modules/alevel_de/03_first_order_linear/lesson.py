TITLE = "First-Order Linear Differential Equations"

SECTIONS = [
    {
        "title": "Integrating Factor Method: For Linear First-Order ODEs",
        "body": """
<h3>Linear First-Order Form</h3>
<p>A linear first-order ODE has the standard form:</p>
<p>$$\\frac{dy}{dx} + P(x)y = Q(x)$$</p>

<p>This is linear in $y$ and $\\frac{dy}{dx}$, but $P$ and $Q$ are arbitrary functions of $x$.</p>

<h3>The Integrating Factor Technique</h3>
<p>Multiply both sides by an <strong>integrating factor</strong> $\\mu(x)$ chosen so the left side becomes $\\frac{d}{dx}[\\mu y]$:</p>

<p>$$\\mu(x) = e^{\\int P(x)\\,dx}$$</p>

<p><strong>Why?</strong> The product rule gives: $\\frac{d}{dx}[\\mu y] = \\mu' y + \\mu \\frac{dy}{dx} = \\mu\\left(P(x)y + \\frac{dy}{dx}\\right)$</p>

<p>So multiplying $\\frac{dy}{dx} + P(x)y = Q(x)$ by $\\mu$ gives:</p>
<p>$$\\frac{d}{dx}[\\mu y] = \\mu Q(x)$$</p>

<p>Integrate: $\\mu y = \\int \\mu Q(x)\\,dx + C$</p>

<div class="worked-example">
<h4>Example 4: Using Integrating Factor</h4>
<p>Solve $\\frac{dy}{dx} + 2y = 6$</p>
<p><strong>Solution:</strong> $P(x) = 2$, so $\\mu(x) = e^{\\int 2\\,dx} = e^{2x}$</p>
<p>Multiply by $\\mu$: $e^{2x} \\cdot \\frac{dy}{dx} + 2e^{2x} \\cdot y = 6e^{2x}$</p>
<p>$\\frac{d}{dx}[e^{2x} \\cdot y] = 6e^{2x}$</p>
<p>Integrate: $e^{2x} \\cdot y = \\int 6e^{2x}\\,dx = 3e^{2x} + C$</p>
<p>$y = 3 + Ce^{-2x}$</p>
</div>

<div class="worked-example">
<h4>Example 5: With Initial Condition</h4>
<p>Solve $\\frac{dy}{dx} + \\frac{y}{x} = x$ with $y(1) = 0$</p>
<p><strong>Solution:</strong> $P(x) = \\frac{1}{x}$, so $\\mu(x) = e^{\\int \\frac{1}{x}\\,dx} = e^{\\ln|x|} = x$</p>
<p>Multiply: $x \\cdot \\frac{dy}{dx} + y = x^{2}$</p>
<p>$\\frac{d}{dx}[xy] = x^{2}$</p>
<p>$xy = \\int x^{2}\\,dx = \\frac{x^{3}}{3} + C$</p>
<p>$y = \\frac{x^{2}}{3} + \\frac{C}{x}$</p>
<p>Apply $y(1) = 0$: $0 = \\frac{1}{3} + C \\implies C = -\\frac{1}{3}$</p>
<p>$y = \\frac{x^{2}}{3} - \\frac{1}{3x}$</p>
</div>

<h3>When to Use Each Method</h3>
<ul>
<li><strong>Separable:</strong> If $\\frac{dy}{dx} = f(x)g(y)$, use separation</li>
<li><strong>Linear ($\\frac{dy}{dx} + P(x)y = Q(x)$):</strong> Use integrating factor</li>
<li><strong>Other forms:</strong> May require substitution or special techniques</li>
</ul>
"""
    }
]
