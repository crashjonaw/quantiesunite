"""
Long Multiplication & Division - Check Questions
"""

CHECKS = [
    {
        "q": "Calculate 23 × 14 using long multiplication. Show your partial products.",
        "a": "23 × 4 = 92, 23 × 10 = 230, 92 + 230 = 322",
        "hint": "Multiply 23 by the ones digit (4), then by the tens digit (1), shift left, and add."
    },
    {
        "q": "What does it mean when a long division problem has a remainder? Give an example.",
        "a": "It means the divisor doesn't divide evenly into the dividend. For example, 23 ÷ 5 = 4 R3 means 5×4=20 with 3 left over.",
        "hint": "A remainder is what's left over after dividing. Always check: (quotient × divisor) + remainder = dividend"
    },
    {
        "q": "Divide 345 ÷ 15 using long division.",
        "a": "23",
        "hint": "15 goes into 34 twice (15×2=30), leaving 4. Bring down 5 to make 45. 15 goes into 45 three times (15×3=45)."
    },
    {
        "q": "Check if 47 × 23 = 1,081 by estimating. Is this reasonable?",
        "a": "Yes, 47 ≈ 50 and 23 ≈ 20, so 50 × 20 = 1,000, which is close to 1,081.",
        "hint": "Round to easier numbers and multiply mentally to check if the exact answer makes sense."
    },
    {
        "q": "In the division problem 256 ÷ 8 = 32, verify this is correct by multiplying.",
        "a": "32 × 8 = 256, so it's correct.",
        "hint": "To check division, multiply the quotient by the divisor. You should get the original dividend."
    }
]
