TITLE = "Parametric Differentiation: dy/dx from Parametric Equations"

SECTIONS = [
    {
        "title": "Parametric Forms and Their Derivatives",
        "body": """
<h3>Parametric Forms and Their Derivatives</h3>
<p>A curve can be defined parametrically: $x = x(t)$, $y = y(t)$, where $t$ is the parameter.</p>

<p>To find $\\frac{dy}{dx}$ (the slope of the curve), use:</p>
<p>$$\\frac{dy}{dx} = \\frac{\\frac{dy}{dt}}{\\frac{dx}{dt}} = \\frac{y'(t)}{x'(t)}, \\quad \\text{provided } x'(t) \\neq 0$$</p>

<p><strong>Justification:</strong> By the chain rule: $\\frac{dy}{dx} = \\frac{dy}{dt} \\cdot \\frac{dt}{dx} = \\frac{\\frac{dy}{dt}}{\\frac{dx}{dt}}$</p>

<div class="worked-example">
<h4>Example 8: Parametric Derivative</h4>
<p>A curve is given by $x = t^{2}$, $y = t^{3}$. Find $\\frac{dy}{dx}$ at $t = 2$</p>
<p><strong>Solution:</strong></p>
<p>$\\frac{dx}{dt} = 2t$, $\\frac{dy}{dt} = 3t^{2}$</p>
<p>$\\frac{dy}{dx} = \\frac{3t^{2}}{2t} = \\frac{3t}{2}$</p>
<p>At $t = 2$: $\\frac{dy}{dx} = \\frac{3(2)}{2} = 3$</p>
</div>
"""
    },
    {
        "title": "Second Derivatives for Parametric Equations",
        "body": """
<h3>Second Derivatives for Parametric Equations</h3>
<p>To find $\\frac{d^{2}y}{dx^{2}}$, differentiate $\\frac{dy}{dx}$ with respect to $t$, then divide by $\\frac{dx}{dt}$:</p>
<p>$$\\frac{d^{2}y}{dx^{2}} = \\frac{\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)}{\\frac{dx}{dt}}$$</p>

<div class="worked-example">
<h4>Example 9: Second Derivative Parametric</h4>
<p>For $x = \\cos(t)$, $y = \\sin(t)$, find $\\frac{d^{2}y}{dx^{2}}$ at $t = \\frac{\\pi}{4}$</p>
<p><strong>Solution:</strong></p>
<p>$\\frac{dx}{dt} = -\\sin(t)$, $\\frac{dy}{dt} = \\cos(t)$</p>
<p>$\\frac{dy}{dx} = \\frac{-\\cos(t)}{\\sin(t)} = -\\cot(t)$</p>
<p>$\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right) = \\frac{d}{dt}[-\\cot(t)] = \\csc^{2}(t)$</p>
<p>$\\frac{d^{2}y}{dx^{2}} = \\frac{\\csc^{2}(t)}{-\\sin(t)} = -\\csc^{3}(t)$</p>
<p>At $t = \\frac{\\pi}{4}$: $\\frac{d^{2}y}{dx^{2}} = -\\csc^{3}\\left(\\frac{\\pi}{4}\\right) = -(\\sqrt{2})^{3} = -2\\sqrt{2}$</p>
</div>
"""
    },
    {
        "title": "Applications: Speed and Velocity",
        "body": """
<h3>Applications: Speed and Velocity</h3>
<p>In parametric form with parameter $t$ = time, the speed along the curve is:</p>
<p>$$\\text{speed} = \\sqrt{\\left(\\frac{dx}{dt}\\right)^{2} + \\left(\\frac{dy}{dt}\\right)^{2}}$$</p>

<p>This represents the magnitude of the velocity vector.</p>

<div class="concept-box">
<h4>Physical Interpretation</h4>
<p>When $t$ represents time, $\\left(\\frac{dx}{dt}, \\frac{dy}{dt}\\right)$ is the velocity vector, and its magnitude gives the speed of an object moving along the parametric curve.</p>
</div>
"""
    }
]
