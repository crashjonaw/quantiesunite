CHECKS = [
    {
        "q": "Find d/dx[sin(3x²)]",
        "a": "6x·cos(3x²)",
        "hint": "Use chain rule. Let u = 3x². Then d/dx[sin(3x²)] = cos(3x²) · 6x."
    },
    {
        "q": "Find d/dx[(2x + 1)e^x]",
        "a": "(2x + 3)e^x",
        "hint": "Use product rule: d/dx[uv] = u'v + uv'. u = 2x + 1, u' = 2, v = e^x, v' = e^x."
    },
    {
        "q": "Find dy/dx if x² + xy + y² = 3",
        "a": "dy/dx = -(2x + y)/(x + 2y)",
        "hint": "Differentiate implicitly. 2x + y + x(dy/dx) + 2y(dy/dx) = 0. Solve for dy/dx."
    },
    {
        "q": "For the parametric curve x = t² - 1, y = 2t + 1, find dy/dx at t = 1",
        "a": "1",
        "hint": "dy/dx = (dy/dt)/(dx/dt) = 2/(2t) = 1/t. At t = 1, dy/dx = 1."
    },
    {
        "q": "Write the first three non-zero terms of the Maclaurin series for cos(x)",
        "a": "1 - x²/2! + x⁴/4!",
        "hint": "Derivatives of cos(x) at 0 alternate: 1, 0, -1, 0, 1, .... Only even derivatives are non-zero."
    }
]
