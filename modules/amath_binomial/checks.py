CHECKS = [
    {
        "q": "Calculate C(8, 3).",
        "a": "56",
        "hint": "C(8,3) = 8!/(3!5!) = (8×7×6)/(3×2×1)"
    },
    {
        "q": "Expand (2x - 1)³ using the binomial theorem.",
        "a": "8x³ - 12x² + 6x - 1",
        "hint": "Use coefficients 1,3,3,1 from Pascal's Triangle row 3. Alternate signs for the -1 term."
    },
    {
        "q": "In the expansion of (3 + x)⁶, find the coefficient of x³.",
        "a": "540",
        "hint": "The x³ term comes from k=3. T₄ = C(6,3) × 3³ × x³"
    },
    {
        "q": "Find the middle term in the expansion of (a + b)⁵.",
        "a": "10a³b²",
        "hint": "n=5 is odd, so there are two middle terms. One is T₃ = C(5,2)a³b²"
    },
    {
        "q": "Prove that C(n,0) + C(n,1) + C(n,2) = C(n+1,2) for n≥1.",
        "a": "Use Pascal's identity repeatedly: C(n,0) + C(n,1) = C(n+1,1); then C(n+1,1) + C(n,2) = C(n+1,2)",
        "hint": "Apply C(n,k) + C(n,k+1) = C(n+1,k+1) twice."
    }
]
