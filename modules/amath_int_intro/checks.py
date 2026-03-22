CHECKS = [
    {
        "q": "Find the antiderivative of f(x) = 5x⁴ − 3x + 2",
        "a": "F(x) = x⁵ − (3/2)x² + 2x + C",
        "hint": "Use the power rule: ∫xⁿ dx = x^(n+1)/(n+1). Apply to each term."
    },
    {
        "q": "Evaluate ∫[0 to 3] (2x + 1) dx",
        "a": "12",
        "hint": "F(x) = x² + x. F(3) − F(0) = (9 + 3) − 0 = 12"
    },
    {
        "q": "Find ∫(6x² − 1)⁴ · 12x dx using substitution.",
        "a": "(6x² − 1)⁵ / 5 + C",
        "hint": "Let u = 6x² − 1, then du = 12x dx. ∫u⁴ du = u⁵/5"
    },
    {
        "q": "Calculate the definite integral ∫[1 to 4] 1/x dx",
        "a": "ln(4)",
        "hint": "Antiderivative of 1/x is ln|x|. [ln(x)]₁⁴ = ln(4) − ln(1)"
    },
    {
        "q": "Find the area between y = x and y = x² from x = 0 to x = 1.",
        "a": "1/6",
        "hint": "x ≥ x² on [0,1]. Area = ∫[0 to 1] (x − x²) dx"
    }
]
