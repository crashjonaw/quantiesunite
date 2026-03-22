CHECKS = [
    {
        "q": "Find the domain of \\( f(x) = \\sqrt{6 - x - x^2} \\)",
        "a": "[-3, 2]",
        "hint": "Solve \\( 6 - x - x^2 \\geq 0 \\). Rearrange: \\( -x^2 - x + 6 \\geq 0 \\) or \\( x^2 + x - 6 \\leq 0 \\). Factor: \\( (x+3)(x-2) \\leq 0 \\). Solution: \\( -3 \\leq x \\leq 2 \\)."
    },
    {
        "q": "If \\( f(x) = \\frac{3x + 2}{2x - 1} \\), find \\( f^{-1}(x) \\)",
        "a": "\\( f^{-1}(x) = \\frac{x + 2}{2x - 3} \\)",
        "hint": "Set \\( y = \\frac{3x+2}{2x-1} \\), solve for \\( x \\): \\( y(2x-1) = 3x+2 \\), \\( 2xy - y = 3x + 2 \\), \\( 2xy - 3x = y + 2 \\), \\( x(2y-3) = y+2 \\), \\( x = \\frac{y+2}{2y-3} \\). Swap variables."
    },
    {
        "q": "Let \\( f(x) = \\sin(x) \\) and \\( g(x) = 2x - \\pi \\). Compute \\( (f \\circ g)(\\pi/2) \\)",
        "a": "0",
        "hint": "Apply \\( g \\) first: \\( g(\\pi/2) = 2(\\pi/2) - \\pi = \\pi - \\pi = 0 \\). Then \\( f(0) = \\sin(0) = 0 \\)."
    },
    {
        "q": "Describe transformations from \\( y = |x| \\) to \\( y = -|x - 2| + 3 \\)",
        "a": "Shift right 2 units, reflect across x-axis, shift up 3 units",
        "hint": "Start with \\( y = |x| \\). Apply \\( x \\to x - 2 \\) to shift right. Multiply by \\( -1 \\) to reflect. Add 3 to shift up."
    },
    {
        "q": "Find the range of \\( f(x) = 1 + \\frac{1}{1 + e^{-x}} \\) (logistic transform)",
        "a": "(1, 2)",
        "hint": "As \\( x \\to -\\infty \\), \\( e^{-x} \\to \\infty \\), so \\( \\frac{1}{1+e^{-x}} \\to 0 \\), thus \\( f(x) \\to 1 \\). As \\( x \\to \\infty \\), \\( e^{-x} \\to 0 \\), so \\( \\frac{1}{1+e^{-x}} \\to 1 \\), thus \\( f(x) \\to 2 \\). Since \\( \\frac{1}{1+e^{-x}} \\in (0, 1) \\), the range is \\( (1, 2) \\)."
    },
    {
        "q": "Find the vertical asymptotes of \\( f(x) = \\frac{x^2 - 1}{x^3 - x^2 - 2x} \\)",
        "a": "\\( x = 0, x = 2 \\) (removable at \\( x = -1 \\))",
        "hint": "Factor numerator: \\( (x-1)(x+1) \\). Factor denominator: \\( x(x^2 - x - 2) = x(x-2)(x+1) \\). Cancel \\( (x+1) \\). Vertical asymptotes where remaining denominator is zero."
    },
    {
        "q": "Solve \\( |3x - 5| = 7 \\)",
        "a": "\\( x = 4 \\) or \\( x = -\\frac{2}{3} \\)",
        "hint": "Either \\( 3x - 5 = 7 \\) giving \\( x = 4 \\), or \\( 3x - 5 = -7 \\) giving \\( x = -\\frac{2}{3} \\)."
    },
    {
        "q": "If \\( g(x) = \\sqrt{x} \\) and \\( h(x) = x^2 - 4 \\), what is the domain of \\( (g \\circ h)(x) \\)?",
        "a": "\\( (-\\infty, -2] \\cup [2, \\infty) \\)",
        "hint": "For \\( g(h(x)) = \\sqrt{x^2 - 4} \\) to be defined, we need \\( x^2 - 4 \\geq 0 \\), which means \\( x^2 \\geq 4 \\), so \\( |x| \\geq 2 \\)."
    }
]
