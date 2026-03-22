QUIZ = [
    {
        "question": "A rectangular box has a square base with side x cm. Its height is h cm, and volume is fixed at 500 cm³. Express the surface area in terms of x only, then find the dimensions that minimize surface area.",
        "answer": "V = x²h = 500, so h = 500/x². Surface area = 2x² + 4xh = 2x² + 2000/x. Minimize: dS/dx = 4x − 2000/x² = 0 gives x³ = 500, so x ≈ 7.94 cm and h = 500/63 ≈ 7.94 cm.",
        "explanation": "The optimal box is a cube (x = h). Set dS/dx = 0 and solve."
    },
    {
        "question": "Using first principles, find the derivative of f(x) = √x",
        "answer": "f'(x) = 1/(2√x)",
        "explanation": "f'(x) = lim(h→0) [√(x+h) − √x]/h. Rationalize: [√(x+h) − √x][√(x+h) + √x]/[h(√(x+h) + √x)] = h/[h(√(x+h) + √x)]. As h→0, this becomes 1/(2√x)."
    },
    {
        "question": "Find the values of x where f(x) = x⁴ − 4x³ is increasing and decreasing.",
        "answer": "Increasing for x < 0 and x > 3; Decreasing for 0 < x < 3",
        "explanation": "f'(x) = 4x³ − 12x² = 4x²(x − 3). Critical points: x = 0, 3. Test intervals: f'(x) > 0 when x < 0 (increasing) and x > 3 (increasing); f'(x) < 0 when 0 < x < 3 (decreasing)."
    },
    {
        "question": "Find the second derivative of y = e^x sin(x) and determine the concavity at x = 0.",
        "answer": "y' = e^x sin(x) + e^x cos(x) = e^x[sin(x) + cos(x)]. y'' = e^x[sin(x) + cos(x)] + e^x[cos(x) − sin(x)] = 2e^x cos(x). At x=0: y'' = 2e^0 cos(0) = 2 > 0, so concave up.",
        "explanation": "Use product rule twice. First derivative: (e^x)' sin(x) + e^x (sin(x))' = e^x sin(x) + e^x cos(x). Second derivative requires product rule again on each term."
    },
    {
        "question": "A particle moves along a line with position s = t³ − 6t² + 9t. Find when the particle is at rest (v = 0), and determine if these are local maxima or minima of position.",
        "answer": "Particle at rest at t = 1 and t = 3. At t=1 (local max, s=4); at t=3 (local min, s=0)",
        "explanation": "v = ds/dt = 3t² − 12t + 9 = 3(t² − 4t + 3) = 3(t−1)(t−3) = 0 at t=1, 3. a = dv/dt = 6t − 12. At t=1: a = −6 < 0 (max); at t=3: a = 6 > 0 (min)."
    }
]
