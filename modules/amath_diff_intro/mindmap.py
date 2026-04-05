MINDMAP = {
    "concepts": [
        {
            "title": "First Principles & Power Rule",
            "points": [
                "Derivative from first principles: \\(f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}\\)",
                "Power rule: \\(\\frac{d}{dx}(x^n) = nx^{n-1}\\)",
                "Constant rule: \\(\\frac{d}{dx}(c) = 0\\)",
                "Sum/difference: \\(\\frac{d}{dx}[f \\pm g] = f' \\pm g'\\)",
            ],
        },
        {
            "title": "Chain, Product & Quotient Rules",
            "points": [
                "Chain rule: \\(\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)\\)",
                "Product rule: \\(\\frac{d}{dx}[uv] = u'v + uv'\\)",
                "Quotient rule: \\(\\frac{d}{dx}\\left[\\frac{u}{v}\\right] = \\frac{u'v - uv'}{v^2}\\)",
            ],
        },
        {
            "title": "Standard Derivatives",
            "points": [
                "\\(\\frac{d}{dx}(\\sin x) = \\cos x\\), \\(\\frac{d}{dx}(\\cos x) = -\\sin x\\)",
                "\\(\\frac{d}{dx}(\\tan x) = \\sec^2 x\\)",
                "\\(\\frac{d}{dx}(e^x) = e^x\\), \\(\\frac{d}{dx}(\\ln x) = \\frac{1}{x}\\)",
            ],
        },
        {
            "title": "Tangents & Normals",
            "points": [
                "Gradient of tangent at \\((a, f(a))\\) is \\(f'(a)\\)",
                "Equation: \\(y - f(a) = f'(a)(x - a)\\)",
                "Normal is perpendicular: gradient = \\(-\\frac{1}{f'(a)}\\)",
            ],
        },
        {
            "title": "Stationary Points & Applications",
            "points": [
                "Stationary points where \\(f'(x) = 0\\)",
                "Second derivative test: \\(f''(x) > 0\\) means minimum; \\(f''(x) < 0\\) means maximum",
                "Rate of change: \\(\\frac{dy}{dt} = \\frac{dy}{dx} \\cdot \\frac{dx}{dt}\\) (connected rates)",
            ],
        },
    ],
    "formulas": [
        {"label": "Power rule", "expr": "\\(\\frac{d}{dx}(x^n) = nx^{n-1}\\)"},
        {"label": "Chain rule", "expr": "\\(\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}\\)"},
        {"label": "Product rule", "expr": "\\((uv)' = u'v + uv'\\)"},
        {"label": "Quotient rule", "expr": "\\(\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}\\)"},
    ],
    "tips": [
        "Expand and simplify before differentiating when possible — it is often faster than using product/quotient rules.",
        "For connected rates of change, identify the chain of variables and apply the chain rule.",
        "If the second derivative is 0, the second derivative test is inconclusive — use the first derivative (sign change) test.",
    ],
}
