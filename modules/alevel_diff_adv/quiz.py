QUIZ = [
    {
        "question": "Differentiate f(x) = (x² + 1)³(2x - 1)² using the product rule.",
        "answer": "f'(x) = 6x(x² + 1)²(2x - 1)² + 4(x² + 1)³(2x - 1)",
        "explanation": "Let u = (x² + 1)³ and v = (2x - 1)². u' = 3(x² + 1)² · 2x = 6x(x² + 1)², v' = 2(2x - 1) · 2 = 4(2x - 1). f'(x) = u'v + uv' = 6x(x² + 1)²(2x - 1)² + 4(x² + 1)³(2x - 1)."
    },
    {
        "question": "Find d/dx of ln(sin(x)). Use the chain rule.",
        "answer": "cot(x)",
        "explanation": "Let u = sin(x). Then d/dx[ln(sin(x))] = (1/sin(x)) · cos(x) = cos(x)/sin(x) = cot(x)."
    },
    {
        "question": "A spherical balloon is inflated. Its radius increases at 2 cm/s. How fast is its volume increasing when r = 5 cm?",
        "answer": "200π cm³/s",
        "explanation": "Volume of sphere: V = (4/3)πr³. dV/dt = 4πr² · dr/dt. When r = 5 and dr/dt = 2: dV/dt = 4π(25)(2) = 200π cm³/s."
    },
    {
        "question": "Show that d/dx[tan(x)] = sec²(x) using the quotient rule.",
        "answer": "tan(x) = sin(x)/cos(x). d/dx[tan(x)] = [cos(x)·cos(x) - sin(x)·(-sin(x))]/cos²(x) = (cos²(x) + sin²(x))/cos²(x) = 1/cos²(x) = sec²(x).",
        "explanation": "Using quotient rule with u = sin(x), v = cos(x): d/dx[sin(x)/cos(x)] = (cos(x)·cos(x) - sin(x)·(-sin(x)))/cos²(x) = (cos²(x) + sin²(x))/cos²(x) = 1/cos²(x) = sec²(x)."
    },
    {
        "question": "Find the Maclaurin series for 1/(1-x) and state its radius of convergence.",
        "answer": "1 + x + x² + x³ + ... = Σ(n=0 to ∞) x^n, with |x| < 1",
        "explanation": "f(x) = 1/(1-x) = (1-x)⁻¹. f^(n)(x) = n!(1-x)^(-(n+1)), so f^(n)(0) = n!. The series is Σ(n=0 to ∞) x^n. This is a geometric series converging for |x| < 1."
    }
]
