QUIZ = [
    {
        "question": "Find the term independent of x in the expansion of (2x - 1/x)⁶.",
        "answer": "The term independent of x occurs when the power of x is 0. General term: C(6,k)(2x)^(6-k)(-1/x)^k = C(6,k)×2^(6-k)×(-1)^k×x^(6-2k). For x⁰: 6-2k=0, so k=3. T₄ = C(6,3)×2³×(-1)³ = 20×8×(-1) = -160",
        "explanation": "Set the exponent of x equal to zero: (6-k) + (-k) = 6 - 2k = 0, giving k = 3. Substitute into the general term."
    },
    {
        "question": "In the expansion of (1 + 2x)ⁿ, the coefficient of x² is 240. Find n.",
        "answer": "C(n,2)×2² = 240; [n(n-1)/2]×4 = 240; n(n-1) = 120; n² - n - 120 = 0; (n-12)(n+10) = 0; n = 12",
        "explanation": "The x² term corresponds to k=2. Set C(n,2)×2² = 240 and solve for n."
    },
    {
        "question": "Use the binomial theorem to estimate (1.01)¹⁰ to 4 decimal places.",
        "answer": "(1.01)¹⁰ = (1 + 0.01)¹⁰ ≈ 1 + 10(0.01) + 45(0.01)² + ... ≈ 1 + 0.1 + 0.0045 + ... ≈ 1.1046",
        "explanation": "First few terms: 1 + C(10,1)×0.01 + C(10,2)×(0.01)² = 1 + 10×0.01 + 45×0.0001 = 1.1045 (exact to 4 places: 1.1046)"
    },
    {
        "question": "Show that the sum 2⁰ + 2¹ + 2² + ... + 2ⁿ = 2^(n+1) - 1 using the binomial theorem.",
        "answer": "This is a geometric series, not directly from binomial, but can relate: 2ⁿ = Σ C(n,k). Actually, the binomial sum C(n,0) + C(n,1) + ... + C(n,n) = 2ⁿ is related. The sum 2⁰ + 2¹ + ... + 2ⁿ = (2^(n+1) - 1)/(2-1) is a geometric series formula.",
        "explanation": "This is more of a geometric series proof than binomial theorem, but the binomial theorem gives C(n,0)+...+C(n,n)=2ⁿ, which is a useful identity."
    },
    {
        "question": "Expand (x + y)⁴ fully and verify by expanding (x + y)²(x + y)² directly.",
        "answer": "x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴. Check: (x²+2xy+y²)² = x⁴ + 2x³y + x²y² + 2x³y + 4x²y² + 2xy³ + x²y² + 2xy³ + y⁴ = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴ ✓",
        "explanation": "Use binomial coefficients 1,4,6,4,1 from Pascal's Triangle row 4. Verify by multiplying (x+y)² by itself."
    }
]
