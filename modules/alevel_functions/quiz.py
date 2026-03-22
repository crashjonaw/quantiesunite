QUIZ = [
    {
        "question": "Find the range of \\( f(x) = \\frac{3x - 1}{x + 2} \\) for \\( x \\in \\mathbb{R} \\setminus \\{-2\\} \\)",
        "answer": "\\( \\mathbb{R} \\setminus \\{3\\} \\) or \\( (-\\infty, 3) \\cup (3, \\infty) \\)",
        "explanation": "Set \\( y = \\frac{3x-1}{x+2} \\) and solve for \\( x \\): \\( y(x+2) = 3x - 1 \\), \\( yx + 2y = 3x - 1 \\), \\( yx - 3x = -1 - 2y \\), \\( x(y-3) = -1-2y \\). This has a solution iff \\( y \\neq 3 \\). So range is \\( \\mathbb{R} \\setminus \\{3\\} \\)."
    },
    {
        "question": "Verify that \\( f(x) = 2x + 3 \\) and \\( g(x) = \\frac{x - 3}{2} \\) are inverses by checking \\( (f \\circ g)(x) = x \\) and \\( (g \\circ f)(x) = x \\)",
        "answer": "\\( (f \\circ g)(x) = 2 \\cdot \\frac{x-3}{2} + 3 = x - 3 + 3 = x \\). \\( (g \\circ f)(x) = \\frac{(2x+3)-3}{2} = \\frac{2x}{2} = x \\). Both equal \\( x \\), so they are inverses.",
        "explanation": "For \\( g = f^{-1} \\), we require \\( f(g(x)) = x \\) and \\( g(f(x)) = x \\) for all \\( x \\) in their respective domains. Both compositions yield the identity function."
    },
    {
        "question": "Given \\( f(x) = x^2 - 2x + 5 \\) and \\( g(x) = \\sqrt{x - 1} \\), find the domain of \\( (f \\circ g)(x) \\)",
        "answer": "\\( [1, \\infty) \\)",
        "explanation": "For \\( (f \\circ g)(x) = f(g(x)) = (\\sqrt{x-1})^2 - 2\\sqrt{x-1} + 5 \\) to be defined, we need \\( g(x) \\) to be defined, which requires \\( x - 1 \\geq 0 \\), so \\( x \\geq 1 \\). The domain is \\( [1, \\infty) \\)."
    },
    {
        "question": "A function has vertical asymptote \\( x = 1 \\) and horizontal asymptote \\( y = 2 \\). Which could it be? (A) \\( f(x) = \\frac{2x}{x-1} \\)  (B) \\( f(x) = \\frac{2}{x-1} \\)  (C) \\( f(x) = \\frac{2x + 1}{x - 1} \\)",
        "answer": "(C) \\( f(x) = \\frac{2x+1}{x-1} \\)",
        "explanation": "For horizontal asymptote \\( y = 2 \\) with equal degree numerator and denominator, the leading coefficient ratio must be \\( 2 \\). For (A): horizontal asymptote is \\( y = 2 \\) but vertical asymptote is \\( x = 1 \\) ✓. For (B): horizontal asymptote is \\( y = 0 \\) ✗. For (C): \\( \\lim_{x \\to \\infty} \\frac{2x+1}{x-1} = \\frac{2}{1} = 2 \\) ✓. Vertical asymptote at \\( x = 1 \\) for all. Answer is (C)."
    },
    {
        "question": "Solve \\( |2x - 3| < 5 \\)",
        "answer": "\\( -1 < x < 4 \\) or \\( (-1, 4) \\)",
        "explanation": "\\( |2x - 3| < 5 \\) means \\( -5 < 2x - 3 < 5 \\). Add 3: \\( -2 < 2x < 8 \\). Divide by 2: \\( -1 < x < 4 \\)."
    },
    {
        "question": "Find the inverse function \\( f^{-1}(x) \\) of \\( f(x) = e^{2x} - 3 \\) and state its domain",
        "answer": "\\( f^{-1}(x) = \\frac{1}{2}\\ln(x + 3) \\); domain: \\( x > -3 \\) or \\( (-3, \\infty) \\)",
        "explanation": "Set \\( y = e^{2x} - 3 \\). Solve for \\( x \\): \\( y + 3 = e^{2x} \\), \\( \\ln(y+3) = 2x \\), \\( x = \\frac{1}{2}\\ln(y+3) \\). Swap to get \\( f^{-1}(x) = \\frac{1}{2}\\ln(x+3) \\). Domain of \\( f^{-1} \\) = range of \\( f \\). Since \\( e^{2x} > 0 \\), we have \\( e^{2x} - 3 > -3 \\), so domain is \\( (-3, \\infty) \\)."
    },
    {
        "question": "Describe the transformations of \\( y = -(x + 2)^3 + 1 \\) from the parent function \\( y = x^3 \\)",
        "answer": "Shift left 2 units, reflect across x-axis, shift up 1 unit",
        "explanation": "Starting with \\( y = x^3 \\): Replace \\( x \\) with \\( x + 2 \\) to shift left (giving \\( y = (x+2)^3 \\)). Multiply by \\( -1 \\) to reflect across x-axis. Add 1 to shift up. The order of composition is: left 2, then reflect, then up 1."
    },
    {
        "question": "If \\( f(x) = 3x - 1 \\) and \\( g(x) = x^2 \\), find \\( (g \\circ f)'(x) \\) using the chain rule",
        "answer": "\\( (g \\circ f)'(x) = 6(3x - 1) = 18x - 6 \\)",
        "explanation": "\\( (g \\circ f)(x) = g(f(x)) = (3x-1)^2 = 9x^2 - 6x + 1 \\). By chain rule: \\( \\frac{d}{dx}[(3x-1)^2] = 2(3x-1) \\cdot 3 = 6(3x-1) = 18x - 6 \\)."
    },
    {
        "question": "Find all solutions to \\( |x - 1| = |x + 2| \\)",
        "answer": "\\( x = -\\frac{1}{2} \\)",
        "explanation": "\\( |x-1| = |x+2| \\) means either \\( x - 1 = x + 2 \\) (impossible: \\( -1 = 2 \\)) or \\( x - 1 = -(x+2) \\), giving \\( x - 1 = -x - 2 \\), \\( 2x = -1 \\), \\( x = -\\frac{1}{2} \\). Check: \\( |-\\frac{1}{2}-1| = \\frac{3}{2} \\) and \\( |-\\frac{1}{2}+2| = \\frac{3}{2} \\) ✓."
    },
    {
        "question": "Determine which function is even and which is odd: (A) \\( f(x) = x^3 - 2x \\)  (B) \\( g(x) = \\frac{1}{x^2 + 1} \\)",
        "answer": "(A) is odd; (B) is even",
        "explanation": "For (A): \\( f(-x) = (-x)^3 - 2(-x) = -x^3 + 2x = -(x^3 - 2x) = -f(x) \\), so \\( f \\) is odd. For (B): \\( g(-x) = \\frac{1}{(-x)^2+1} = \\frac{1}{x^2+1} = g(x) \\), so \\( g \\) is even."
    }
]
