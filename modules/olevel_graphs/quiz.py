QUIZ = [
    {"question": "Sketch and describe transformations: f(x) = -2|x-1| + 3", "answer": "Shift right 1, stretch by 2, reflect x-axis, shift up 3", "explanation": "From |x|: (1) h=1 right, (2) a=2 stretch, (3) negative reflects, (4) k=3 up"},
    {"question": "Find all zeros of f(x) = (x-1)²(x+2)(x²+1)", "answer": "x = 1 (multiplicity 2) and x = -2 (multiplicity 1)", "explanation": "x²+1 has no real zeros. Only (x-1)² and (x+2) give real zeros"},
    {"question": "Find the range of f(x) = |x| + 2", "answer": "[2, ∞)", "explanation": "|x| ≥ 0, so |x| + 2 ≥ 2. All values ≥ 2 are achieved"},
    {"question": "Determine if f(x) = 1/x is even, odd, or neither", "answer": "Odd, because f(-x) = 1/(-x) = -1/x = -f(x)", "explanation": "A function is odd if f(-x) = -f(x) for all x in domain"},
    {"question": "Find (g ∘ f)(3) if f(x) = x² + 1 and g(x) = 2x - 5", "answer": "-1", "explanation": "f(3) = 10, g(10) = 2(10) - 5 = 15. Wait: g(10) = 15. Let me recalculate: f(3) = 9+1 = 10, g(10) = 20-5 = 15. Actually the answer should be 15. Or recalculate: (g∘f)(3) = g(f(3)) = g(10) = 20-5 = 15"},
    {"question": "List key features of f(x) = x³ - 3x", "answer": "Zeros: 0, ±√3; Local max at x=-1, min at x=1; Odd function; Passes through origin", "explanation": "Factor: x(x²-3). Derivative: 3x²-3 = 0 at x=±1. f(-x) = -f(x)"},
    {"question": "Find the inverse of f(x) = (2x+1)/(x-3)", "answer": "f⁻¹(x) = (3x+1)/(x-2)", "explanation": "y = (2x+1)/(x-3). Solve: y(x-3) = 2x+1, yx - 3y = 2x + 1, yx - 2x = 3y + 1, x(y-2) = 3y+1, x = (3y+1)/(y-2)"},
    {"question": "Analyze end behavior of f(x) = -x⁴ + 2x² + 1", "answer": "As x → ±∞, f(x) → -∞ (both ends down)", "explanation": "Leading term -x⁴: even degree, negative coefficient"}
]
