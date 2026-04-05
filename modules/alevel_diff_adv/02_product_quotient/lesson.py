TITLE = "Product and Quotient Rules: Complete Derivation"

SECTIONS = [
    {
        "title": "Product Rule",
        "body": """
<h3>Product Rule</h3>
<p>If $y = u(x) \\cdot v(x)$, then:</p>
<p>$$\\frac{dy}{dx} = u'v + uv' \\quad \\text{or} \\quad (uv)' = u'v + uv'$$</p>

<p><strong>Derivation:</strong> From first principles:</p>
<p>$y(x+h) - y(x) = u(x+h)v(x+h) - u(x)v(x)$</p>
<p>$= u(x+h)[v(x+h) - v(x)] + v(x)[u(x+h) - u(x)]$</p>
<p>Dividing by $h$ and taking $h \\to 0$:</p>
<p>$\\frac{dy}{dx} = u(x) \\cdot v'(x) + v(x) \\cdot u'(x)$</p>

<div class="worked-example">
<h4>Example 3: Product Rule</h4>
<p>Find $\\frac{d}{dx}\\left[x \\cdot e^{x}\\right]$</p>
<p><strong>Solution:</strong> $\\frac{d}{dx}\\left[x \\cdot e^{x}\\right] = 1 \\cdot e^{x} + x \\cdot e^{x} = e^{x}(1 + x)$</p>
</div>
"""
    },
    {
        "title": "Quotient Rule",
        "body": """
<h3>Quotient Rule</h3>
<p>If $y = \\frac{u(x)}{v(x)}$, then:</p>
<p>$$\\frac{dy}{dx} = \\frac{u'v - uv'}{v^{2}} \\quad \\text{or} \\quad \\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^{2}}$$</p>

<p><strong>Derivation:</strong> Apply product rule to $\\frac{u}{v} = u \\cdot \\frac{1}{v}$:</p>
<p>$\\frac{d}{dx}\\left[\\frac{u}{v}\\right] = u' \\cdot \\frac{1}{v} + u \\cdot \\frac{d}{dx}\\left[\\frac{1}{v}\\right]$</p>
<p>Now $\\frac{d}{dx}\\left[\\frac{1}{v}\\right] = -\\frac{v'}{v^{2}}$ (by chain rule)</p>
<p>So: $\\frac{d}{dx}\\left[\\frac{u}{v}\\right] = \\frac{u'}{v} - \\frac{uv'}{v^{2}} = \\frac{u'v - uv'}{v^{2}}$</p>

<div class="worked-example">
<h4>Example 4: Quotient Rule</h4>
<p>Find $\\frac{d}{dx}\\left[\\frac{x^{2} + 1}{x - 1}\\right]$</p>
<p><strong>Solution:</strong> $u = x^{2} + 1$, $u' = 2x$; $v = x - 1$, $v' = 1$</p>
<p>$\\frac{dy}{dx} = \\frac{(2x)(x - 1) - (x^{2} + 1)(1)}{(x - 1)^{2}}$</p>
<p>$= \\frac{2x^{2} - 2x - x^{2} - 1}{(x - 1)^{2}} = \\frac{x^{2} - 2x - 1}{(x - 1)^{2}}$</p>
</div>
"""
    },
    {
        "title": "Selecting Rules Wisely",
        "body": """
<h3>Selecting Rules Wisely</h3>
<p>When a quotient can be simplified or rewritten, it's often easier:</p>
<p>$\\frac{d}{dx}\\left[\\frac{x}{x^{2} + 1}\\right] = \\frac{d}{dx}\\left[x \\cdot (x^{2} + 1)^{-1}\\right]$ (product rule)</p>
<p>Or directly with quotient rule—choose whichever is simplest.</p>

<div class="success-box">
<h4>Tip: Strategic Approach</h4>
<p>Always look for ways to simplify your expression before choosing a differentiation rule. Sometimes rewriting the function makes the calculation more efficient.</p>
</div>
"""
    }
]
