QUIZ = [
    {
        "question": "Two forces act on an object: F₁ = (5, 12) N and F₂ = (−3, 4) N. Find the magnitude of the resultant force.",
        "answer": "Resultant = (2, 16) N; magnitude = √(4 + 256) = √260 = 2√65 ≈ 16.12 N",
        "explanation": "Resultant force = F₁ + F₂ = (5−3, 12+4) = (2, 16). Magnitude = √(2² + 16²) = √(4+256) = √260."
    },
    {
        "question": "Points A, B, C have position vectors a = (1, 2), b = (3, 5), c = (5, 8). Show that A, B, C are collinear.",
        "answer": "AB⃗ = (2, 3) and AC⃗ = (4, 6) = 2·AB⃗. Since AC⃗ is a scalar multiple of AB⃗, the points are collinear.",
        "explanation": "To show collinearity, we check if one vector is a scalar multiple of another. AC⃗ = c − a = (5−1, 8−2) = (4, 6). AB⃗ = b − a = (3−1, 5−2) = (2, 3). Indeed, (4, 6) = 2(2, 3)."
    },
    {
        "question": "Find the angle between vectors u = (1, √3) and v = (1, 0).",
        "answer": "60°",
        "explanation": "cos(θ) = (u·v)/(|u||v|). u·v = 1(1) + √3(0) = 1. |u| = √(1+3) = 2. |v| = 1. cos(θ) = 1/2, so θ = 60°."
    },
    {
        "question": "Find a vector perpendicular to u = (4, 3).",
        "answer": "Any scalar multiple of (−3, 4) or (3, −4) works, e.g., (−3, 4)",
        "explanation": "For perpendicularity, u·v = 0. If v = (a, b), then 4a + 3b = 0. One solution is a = 3, b = −4, giving v = (3, −4). Another is v = (−3, 4). Check: (4, 3)·(−3, 4) = −12 + 12 = 0 ✓"
    },
    {
        "question": "A line passes through point P(2, 1) in the direction of vector d = (2, −1). Write the vector equation of the line and find two points on it.",
        "answer": "Vector equation: r = (2, 1) + t(2, −1). Two points: at t=0, (2, 1); at t=1, (4, 0); at t=2, (6, −1), etc.",
        "explanation": "The parametric form r = a + td gives all points on the line. Substituting different values of t yields different points."
    }
]
