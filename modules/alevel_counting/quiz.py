QUIZ = [
    {
        "question": "Prove that nCr = nC(n-r) and explain the combinatorial meaning",
        "answer": "nCr = n!/(r!(n-r)!) = n!/((n-r)!r!) = nC(n-r). Choosing r items to select is the same as choosing n-r items to exclude.",
        "explanation": "Algebraically: nCr = n!/(r!(n-r)!) and nC(n-r) = n!/((n-r)!r!) are identical. Combinatorially: selecting r people from n for a team is equivalent to deciding which n-r people are NOT on the team."
    },
    {
        "question": "In how many ways can 5 distinct books be arranged on a shelf if 2 specific books must be adjacent?",
        "answer": "48",
        "explanation": "Treat the 2 books as a single unit. Arrange 4 units: 4! = 24. The 2 books within their unit can be in 2 orders: 2! = 2. Total: 24 × 2 = 48."
    },
    {
        "question": "Use the inclusion-exclusion principle: Count integers from 1 to 100 divisible by 2, 3, or 5",
        "answer": "74",
        "explanation": "Divisible by 2: 50. By 3: 33. By 5: 20. By 2 and 3 (i.e., 6): 16. By 2 and 5 (i.e., 10): 10. By 3 and 5 (i.e., 15): 6. By 2, 3, and 5 (i.e., 30): 3. |A∪B∪C| = 50 + 33 + 20 - 16 - 10 - 6 + 3 = 74."
    },
    {
        "question": "How many 4-letter words can be formed from the letters of MISSISSIPPI (using each letter at most as many times as it appears)?",
        "answer": "Requires casework based on letter frequency",
        "explanation": "M(1), I(4), S(4), P(2). Choose 4 letters: cases are M1I3, M1I2S1, M1I2P1, M1I1S2, M1I1S1P1, M1S3, M1S2P1, M1S1P2, I4, I3S1, I3P1, I2S2, I2S1P1, I2P2, I1S3, I1S2P1, I1S1P2, S4, S3P1, S2P2, S1P2. For each case, compute arrangements using n!/(n₁!n₂!...)"
    },
    {
        "question": "How many surjective (onto) functions are there from a 5-element set to a 3-element set?",
        "answer": "3! × S(5, 3) = 6 × 25 = 150",
        "explanation": "A surjection partitions the 5-element set into 3 non-empty parts, then assigns each part to one of the 3 target elements. S(5, 3) = 25 (Stirling number of second kind). Multiply by 3! = 6 to account for the ordering (distinguishable) target elements. Total: 150."
    }
]
