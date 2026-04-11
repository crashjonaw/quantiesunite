QUIZ = [
    {
        "question": "Solve \\(3x^2 + 7x - 20 = 0\\) using the quadratic formula.",
        "options": [
            "\\(x = \\frac{5}{3}\\) or \\(x = -4\\)",
            "\\(x = \\frac{3}{5}\\) or \\(x = -4\\)",
            "\\(x = 5\\) or \\(x = -\\frac{4}{3}\\)",
            "\\(x = \\frac{7}{3}\\) or \\(x = -3\\)"
        ],
        "correct": 0,
        "explanation": "\\(a=3, b=7, c=-20\\). \\(\\Delta = 49 + 240 = 289 = 17^2\\). \\(x = \\frac{-7 \\pm 17}{6}\\) gives \\(\\frac{10}{6} = \\frac{5}{3}\\) or \\(\\frac{-24}{6} = -4\\)."
    },
    {
        "question": "A rectangle has perimeter 24 cm. What width \\(w\\) gives the maximum area?",
        "options": ["4 cm", "6 cm", "8 cm", "12 cm"],
        "correct": 1,
        "explanation": "If width is \\(w\\), length is \\(12-w\\). Area \\(A = w(12-w)\\). Vertex at \\(w = \\frac{12}{2} = 6\\), giving \\(A = 36\\) cm²."
    },
    {
        "question": "Show that \\(x^2 + x + 1 = 0\\) has no real roots. What is the discriminant?",
        "options": ["\\(\\Delta = 3\\)", "\\(\\Delta = -3\\)", "\\(\\Delta = 0\\)", "\\(\\Delta = 5\\)"],
        "correct": 1,
        "explanation": "\\(\\Delta = 1^2 - 4(1)(1) = 1 - 4 = -3 < 0\\), so no real roots. The parabola's vertex is above the x-axis."
    },
    {
        "question": "If \\(\\alpha\\) and \\(\\beta\\) are roots of \\(x^2 - 6x + 8 = 0\\), find \\(\\alpha^2 + \\beta^2\\).",
        "options": ["20", "28", "36", "12"],
        "correct": 0,
        "explanation": "\\(\\alpha + \\beta = 6\\), \\(\\alpha\\beta = 8\\). Then \\(\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = 36 - 16 = 20\\)."
    },
    {
        "question": "What are the roots of \\(x^2 - 2x - 2 = 0\\)?",
        "options": [
            "\\(x = 1 \\pm \\sqrt{3}\\)",
            "\\(x = 2 \\pm \\sqrt{3}\\)",
            "\\(x = 1 \\pm \\sqrt{2}\\)",
            "\\(x = -1 \\pm \\sqrt{3}\\)"
        ],
        "correct": 0,
        "explanation": "\\(x = \\frac{2 \\pm \\sqrt{4 + 8}}{2} = \\frac{2 \\pm \\sqrt{12}}{2} = 1 \\pm \\sqrt{3}\\)."
    },
    {
        "question": "A projectile follows \\(h(t) = -5t^2 + 30t + 5\\). When does it reach 35 m?",
        "options": [
            "\\(t = 3 \\pm \\sqrt{3}\\)",
            "\\(t = 3 \\pm \\sqrt{2}\\)",
            "\\(t = 1\\) or \\(t = 5\\)",
            "\\(t = 2\\) or \\(t = 4\\)"
        ],
        "correct": 0,
        "explanation": "\\(-5t^2 + 30t + 5 = 35 \\Rightarrow t^2 - 6t + 6 = 0\\). \\(t = \\frac{6 \\pm \\sqrt{36-24}}{2} = 3 \\pm \\sqrt{3}\\)."
    },
    {
        "question": "Find the range of \\(f(x) = -x^2 + 4x - 3\\).",
        "options": ["\\((-\\infty, 1]\\)", "\\((-\\infty, 3]\\)", "\\([1, \\infty)\\)", "\\((-\\infty, -3]\\)"],
        "correct": 0,
        "explanation": "\\(a = -1 < 0\\), opens downward. Vertex at \\(x = 2\\), \\(f(2) = -4 + 8 - 3 = 1\\). Maximum is 1."
    },
    {
        "question": "Solve \\(x^2 - 5x + 6 = 0\\).",
        "options": ["\\(x = 2\\) or \\(x = 3\\)", "\\(x = 1\\) or \\(x = 6\\)", "\\(x = -2\\) or \\(x = -3\\)", "\\(x = 2\\) or \\(x = -3\\)"],
        "correct": 0,
        "explanation": "Factor: \\((x-2)(x-3) = 0\\). So \\(x = 2\\) or \\(x = 3\\)."
    },
    {
        "question": "Expand \\((x - 2)(x + 3)\\).",
        "options": ["\\(x^2 + x - 6\\)", "\\(x^2 - x - 6\\)", "\\(x^2 + x + 6\\)", "\\(x^2 + 5x - 6\\)"],
        "correct": 0,
        "explanation": "\\((x-2)(x+3) = x^2 + 3x - 2x - 6 = x^2 + x - 6\\)."
    },
    {
        "question": "A box is made by cutting \\(x\\) cm squares from corners of a 10 cm × 8 cm rectangle. The volume is:",
        "options": [
            "\\(V = x(10-2x)(8-2x)\\)",
            "\\(V = x(10-x)(8-x)\\)",
            "\\(V = 2x(10-2x)(8-2x)\\)",
            "\\(V = x \\cdot 10 \\cdot 8\\)"
        ],
        "correct": 0,
        "explanation": "After cutting and folding, height = \\(x\\), length = \\(10-2x\\), width = \\(8-2x\\). Volume = \\(x(10-2x)(8-2x)\\)."
    }
]
