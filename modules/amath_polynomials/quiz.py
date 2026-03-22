QUIZ = [
    {
        "question": "Prove that (x - 2) is a factor of f(x) = x³ - 4x² + x + 6. Then fully factor f(x).",
        "answer": "f(2) = 8 - 16 + 2 + 6 = 0, so (x-2) is a factor. f(x) = (x-2)(x² - 2x - 3) = (x-2)(x-3)(x+1)",
        "explanation": "Use the Factor Theorem to confirm (x-2) is a factor. Use synthetic division to find the quotient x² - 2x - 3, then factor that quadratic."
    },
    {
        "question": "Decompose (3x² + 5)/(x³ - 1) into partial fractions. [Hint: x³ - 1 = (x-1)(x² + x + 1)]",
        "answer": "A/(x-1) + (Bx+C)/(x²+x+1) where A = 8/3, B = 1/3, C = -8/3. Or: 8/3 · 1/(x-1) + (1/3·x - 8/3)/(x²+x+1)",
        "explanation": "Set 3x² + 5 = A(x² + x + 1) + (Bx + C)(x - 1). Expand and compare coefficients or substitute convenient values."
    },
    {
        "question": "Find all roots of x⁴ - 5x² + 4 = 0.",
        "a": "x = ±1, ±2",
        "explanation": "Let y = x². Then y² - 5y + 4 = 0, giving (y-1)(y-4) = 0, so y = 1 or 4. Thus x² = 1 or x² = 4, giving x = ±1, ±2."
    },
    {
        "question": "A cubic polynomial has roots 1, 2, and -1. Write the polynomial in the form ax³ + bx² + cx + d if the leading coefficient is 3.",
        "answer": "f(x) = 3(x - 1)(x - 2)(x + 1) = 3(x² - 3x + 2)(x + 1) = 3(x³ - 2x² - x + 2) = 3x³ - 6x² - 3x + 6",
        "explanation": "Start with the factored form using the roots, expand step by step, and multiply by the leading coefficient."
    },
    {
        "question": "Given that 2 + i is a root of a polynomial with real coefficients, what other complex root must exist? Write a quadratic with these roots.",
        "answer": "The other root is 2 - i. The quadratic is (x - (2+i))(x - (2-i)) = (x-2)² + 1 = x² - 4x + 5",
        "explanation": "By the Conjugate Root Theorem, complex roots of polynomials with real coefficients come in conjugate pairs. Multiply out using the difference of squares pattern."
    }
]
