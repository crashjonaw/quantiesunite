CHECKS = [
    {
        "q": "Is y = 2e^(3x) a solution to dy/dx = 3y?",
        "a": "Yes",
        "hint": "If y = 2e^(3x), then dy/dx = 6e^(3x) = 3(2e^(3x)) = 3y. ✓"
    },
    {
        "q": "Solve the separable equation dy/dx = (x²)/(y²)",
        "a": "y³ = x³ + C or y = ∛(x³ + C)",
        "hint": "Rearrange: y² dy = x² dx. Integrate: y³/3 = x³/3 + C. Simplify: y³ = x³ + C'."
    },
    {
        "q": "Solve dy/dx + (2/x)y = x using an integrating factor",
        "a": "y = x²/5 + C/x²",
        "hint": "P(x) = 2/x, so μ(x) = e^(∫2/x dx) = e^(2ln|x|) = x². Multiply to get d/dx[x²y] = x³."
    },
    {
        "q": "For dy/dx = 4y, find the general solution",
        "a": "y = Ce^(4x)",
        "hint": "This is separable: (1/y)dy = 4 dx. Integrate: ln|y| = 4x + C₁, so y = Ce^(4x)."
    },
    {
        "q": "Identify the equilibrium solutions for dy/dx = (y - 2)(y + 1)",
        "a": "y = 2 and y = -1",
        "hint": "Set dy/dx = 0: (y - 2)(y + 1) = 0. The solutions are y = 2 and y = -1."
    }
]
