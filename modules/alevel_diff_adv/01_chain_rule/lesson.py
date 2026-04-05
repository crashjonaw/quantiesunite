TITLE = "Chain Rule: Derivation and Application"

SECTIONS = [
    {
        "title": "Chain Rule: Derivation and Application",
        "body": """
<h3>The Chain Rule Theorem</h3>
<p>If $y = f(u)$ and $u = g(x)$, then:</p>
<p>$$\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$$</p>

<p><strong>Proof (informal):</strong> For small changes $\\delta x$ and $\\delta u$:</p>
<p>$\\delta y \\approx \\frac{dy}{du} \\cdot \\delta u$ and $\\delta u \\approx \\frac{du}{dx} \\cdot \\delta x$</p>
<p>Therefore: $\\delta y \\approx \\frac{dy}{du} \\cdot \\frac{du}{dx} \\cdot \\delta x$</p>
<p>As $\\delta x \\to 0$: $\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$</p>

<p><strong>In Leibniz notation:</strong> The $d$'s appear to "cancel": $\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$</p>

<h3>Examples and Applications</h3>

<div class="concept-box">
<h4>Example 1: Simple Chain Rule</h4>
<p>Find $\\frac{d}{dx}\\left[(3x^{2} + 1)^{5}\\right]$</p>
<p><strong>Solution:</strong> Let $u = 3x^{2} + 1$. Then $\\frac{d}{dx}\\left[(3x^{2} + 1)^{5}\\right] = 5u^{4} \\cdot \\frac{du}{dx} = 5(3x^{2} + 1)^{4} \\cdot 6x = 30x(3x^{2} + 1)^{4}$</p>
</div>

<div class="worked-example">
<h4>Example 2: Composite with Trigonometry</h4>
<p>Find $\\frac{d}{dx}\\left[\\sin(x^{2})\\right]$</p>
<p><strong>Solution:</strong> Let $u = x^{2}$. Then $\\frac{d}{dx}\\left[\\sin(x^{2})\\right] = \\cos(x^{2}) \\cdot 2x = 2x \\cos(x^{2})$</p>
</div>

<h3>General Form: Nested Functions</h3>
<p>For $y = f(g(h(x)))$, the chain rule extends:</p>
<p>$$\\frac{dy}{dx} = \\frac{df}{dg} \\cdot \\frac{dg}{dh} \\cdot \\frac{dh}{dx}$$</p>

<p>We differentiate from the outside in, multiplying derivatives at each layer.</p>
"""
    }
]
