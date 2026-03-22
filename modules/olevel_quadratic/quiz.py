QUIZ = [
    {
        "question": "Solve 3x² + 7x - 20 = 0 using the quadratic formula",
        "answer": "x = 5/3 or x = -4",
        "explanation": "a=3, b=7, c=-20. Δ = 49 + 240 = 289 = 17². x = (-7 ± 17)/6 gives 10/6 = 5/3 or -24/6 = -4"
    },
    {
        "question": "A rectangle has perimeter 24 cm. Express area A as a function of width w, then find the maximum area",
        "answer": "A(w) = w(12-w) = 12w - w². Maximum area = 36 cm² at w = 6 cm",
        "explanation": "If width is w, length is 12-w. Area A = w(12-w). Vertex at w = 12/2 = 6, giving A = 36."
    },
    {
        "question": "Show that x² + x + 1 = 0 has no real roots and explain why geometrically",
        "answer": "Δ = 1 - 4 = -3 < 0, so no real roots. The parabola y = x² + x + 1 has its vertex above the x-axis and opens upward, so it never crosses the x-axis.",
        "explanation": "Vertex at x = -1/2, y = 1/4 - 1/2 + 1 = 3/4 > 0. Since a = 1 > 0 and vertex is above x-axis, parabola stays entirely above x-axis."
    },
    {
        "question": "If α and β are roots of x² - 6x + 8 = 0, find α² + β² without solving for α and β",
        "answer": "α² + β² = 20",
        "explanation": "α + β = 6, αβ = 8. Then α² + β² = (α + β)² - 2αβ = 36 - 16 = 20"
    },
    {
        "question": "Verify that the roots of x² - 2x - 2 = 0 are x = 1 ± √3",
        "answer": "Substituting x = 1 ± √3: (1±√3)² - 2(1±√3) - 2 = (1 ± 2√3 + 3) - (2 ± 2√3) - 2 = 4 - 2 - 2 = 0",
        "explanation": "Verify by substitution into the original equation."
    },
    {
        "question": "A projectile is launched with v₀ = 30 m/s from height h₀ = 5 m. When does it reach 35 m height?",
        "answer": "t ≈ 0.166 s or t ≈ 5.834 s (using h(t) = -5t² + 30t + 5 = 35)",
        "explanation": "-5t² + 30t + 5 = 35 → -5t² + 30t - 30 = 0 → t² - 6t + 6 = 0. t = (6 ± √(36-24))/2 = (6 ± √12)/2 = 3 ± √3"
    },
    {
        "question": "Find the range of f(x) = -x² + 4x - 3",
        "answer": "(-∞, 1]",
        "explanation": "a = -1 < 0, opens downward. Vertex at x = 2, f(2) = -4 + 8 - 3 = 1. Maximum is 1."
    },
    {
        "question": "Solve |x² - 5x + 4| = 2 (hint: consider two cases)",
        "answer": "x = 1 ± √2 or x = 4 ± √2",
        "explanation": "Case 1: x² - 5x + 4 = 2 → x² - 5x + 2 = 0 → x = (5 ± √17)/2. Case 2: x² - 5x + 4 = -2 → x² - 5x + 6 = 0 → (x-2)(x-3) = 0."
    },
    {
        "question": "Prove that (x - 2)(x + 3) = x² + x - 6 by expanding",
        "answer": "(x-2)(x+3) = x² + 3x - 2x - 6 = x² + x - 6",
        "explanation": "Direct expansion using FOIL or distributive property."
    },
    {
        "question": "A box is made by cutting x cm squares from corners of a 10 cm × 8 cm rectangle. Express volume as a function of x",
        "answer": "V(x) = x(10 - 2x)(8 - 2x) = 4x³ - 36x² + 80x (or evaluate as quadratic if x is fixed)",
        "explanation": "After cutting and folding, height = x, length = 10-2x, width = 8-2x. Volume = x(10-2x)(8-2x)"
    }
]
