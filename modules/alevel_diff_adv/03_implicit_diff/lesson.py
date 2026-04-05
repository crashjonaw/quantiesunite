TITLE = "Implicit Differentiation: Variables on Both Sides"

SECTIONS = [
    {
        "title": "Method and Principle",
        "body": """
<h3>Method and Principle</h3>
<p>When an equation relates $x$ and $y$ implicitly (not $y = f(x)$ explicitly), differentiate both sides with respect to $x$:</p>

<p><strong>Key principle:</strong> When differentiating terms in $y$, multiply by $\\frac{dy}{dx}$ (chain rule).</p>

<div class="worked-example">
<h4>Example 5: Implicit Differentiation</h4>
<p>Find $\\frac{dy}{dx}$ if $x^{2} + y^{2} = 25$</p>
<p><strong>Solution:</strong> Differentiate both sides:</p>
<p>$\\frac{d}{dx}[x^{2}] + \\frac{d}{dx}[y^{2}] = \\frac{d}{dx}[25]$</p>
<p>$2x + 2y\\frac{dy}{dx} = 0$</p>
<p>$2y\\frac{dy}{dx} = -2x$</p>
<p>$\\frac{dy}{dx} = -\\frac{x}{y}$</p>
</div>

<div class="worked-example">
<h4>Example 6: More Complex Implicit Function</h4>
<p>Find $\\frac{dy}{dx}$ if $xy + e^{y} = 5$</p>
<p><strong>Solution:</strong></p>
<p>$\\frac{d}{dx}[xy] + \\frac{d}{dx}[e^{y}] = 0$</p>
<p>$y + x\\frac{dy}{dx} + e^{y}\\frac{dy}{dx} = 0$</p>
<p>$(x + e^{y})\\frac{dy}{dx} = -y$</p>
<p>$\\frac{dy}{dx} = \\frac{-y}{x + e^{y}}$</p>
</div>
"""
    },
    {
        "title": "Finding the Derivative Explicitly",
        "body": """
<h3>Finding the Derivative Explicitly</h3>
<p>After finding $\\frac{dy}{dx}$ in terms of both $x$ and $y$, we can evaluate it at specific points.</p>

<p>To find $\\frac{d^{2}y}{dx^{2}}$ (second derivative), differentiate $\\frac{dy}{dx}$ again, treating $\\frac{dy}{dx}$ as a function.</p>

<div class="worked-example">
<h4>Example 7: Second Derivative</h4>
<p>Find $\\frac{d^{2}y}{dx^{2}}$ for $x^{2} + y^{2} = 25$</p>
<p><strong>Solution:</strong> From Example 5: $\\frac{dy}{dx} = -\\frac{x}{y}$</p>
<p>Differentiate again: $\\frac{d}{dx}\\left[\\frac{dy}{dx}\\right] = \\frac{d}{dx}\\left[-\\frac{x}{y}\\right]$</p>
<p>$= \\frac{-y - x\\frac{dy}{dx}}{y^{2}} = \\frac{-y - x\\left(-\\frac{x}{y}\\right)}{y^{2}}$</p>
<p>$= \\frac{-y + \\frac{x^{2}}{y}}{y^{2}} = \\frac{x^{2} - y^{2}}{y^{3}} = \\frac{-25}{y^{3}}$ (since $x^{2} + y^{2} = 25$)</p>
</div>

<div class="concept-box">
<h4>Key Strategy</h4>
<p>When finding higher-order derivatives implicitly, remember that $\\frac{dy}{dx}$ is itself a function of $x$ and $y$. Substitute known expressions and use the constraint equation to simplify.</p>
</div>
"""
    }
]
