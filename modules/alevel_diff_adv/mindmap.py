MINDMAP = {
    "concepts": [
        {"title": "Chain Rule", "points": [
            "If \\(y = f(g(x))\\), then \\(\\frac{dy}{dx} = f'(g(x)) \\cdot g'(x)\\)",
            "Used when differentiating composite functions",
            "Example: \\(\\frac{d}{dx}(\\sin(x^2)) = 2x\\cos(x^2)\\)",
        ]},
        {"title": "Product & Quotient Rules", "points": [
            "Product: \\(\\frac{d}{dx}(uv) = u'v + uv'\\)",
            "Quotient: \\(\\frac{d}{dx}\\left(\\frac{u}{v}\\right) = \\frac{u'v - uv'}{v^2}\\)",
        ]},
        {"title": "Implicit Differentiation", "points": [
            "Differentiate both sides with respect to \\(x\\), treating \\(y\\) as a function of \\(x\\)",
            "Apply chain rule: \\(\\frac{d}{dx}(y^2) = 2y\\frac{dy}{dx}\\)",
            "Collect \\(\\frac{dy}{dx}\\) terms and solve",
        ]},
        {"title": "Parametric Differentiation", "points": [
            "If \\(x = f(t)\\), \\(y = g(t)\\), then \\(\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt}\\)",
            "Second derivative: \\(\\frac{d^2y}{dx^2} = \\frac{\\frac{d}{dt}(dy/dx)}{dx/dt}\\)",
        ]},
        {"title": "Applications", "points": [
            "Connected rates of change using chain rule",
            "Maclaurin series: \\(f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\cdots\\)",
            "Small angle approximations for trig functions",
        ]},
    ],
    "formulas": [
        {"label": "Chain Rule", "expr": "\\(\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}\\)"},
        {"label": "Product Rule", "expr": "\\((uv)' = u'v + uv'\\)"},
        {"label": "Quotient Rule", "expr": "\\(\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}\\)"},
        {"label": "Parametric", "expr": "\\(\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt}\\)"},
        {"label": "Inverse Trig", "expr": "\\(\\frac{d}{dx}(\\sin^{-1}x) = \\frac{1}{\\sqrt{1-x^2}}\\)"},
    ],
    "tips": [
        "For implicit differentiation, always remember to multiply by dy/dx when differentiating y terms",
        "Connected rates: identify what you have (e.g. dr/dt) and what you need, then chain them together",
        "Check your parametric second derivative — it's NOT simply d²y/dt² divided by d²x/dt²",
    ],
}
