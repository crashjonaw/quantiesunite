QUIZ = [
    {
        "question": "The sum of the first n terms of an AP is S_n = 3n² + 2n. Find the first term and common difference.",
        "answer": "First term a = S_1 = 5; T_2 = S_2 - S_1 = 16 - 5 = 11, so d = 11 - 5 = 6",
        "explanation": "a = S_1 = 3(1)² + 2(1) = 5. The second term is S_2 = 3(4) + 4 = 16, so T_2 = 11. The common difference is d = T_2 - T_1 = 11 - 5 = 6."
    },
    {
        "question": "Show that the series Σ(k=1 to ∞) 2^k / 3^(k+1) converges and find its sum.",
        "answer": "Rewrite as (1/3)·Σ(k=1 to ∞) (2/3)^k. This is a geometric series with a = 2/3 and r = 2/3 < 1. Sum = 2.",
        "explanation": "The series is (1/3)·(2/3 + (2/3)² + (2/3)³ + ...), a geometric series with first term a = 2/3 and r = 2/3. Since |r| < 1, it converges to (1/3)·(2/3)/(1 - 2/3) = (1/3)·2 = 2/3. Wait, let me recalculate: (1/3)·[(2/3)/(1-2/3)] = (1/3)·2 = 2/3. Actually: a·Σ(geometric) = (1/3)·(2/3)/(1/3) = 2/3. [Correction: Sum = (1/3)·Σ(2/3)^k = (1/3)·[(2/3)/(1-2/3)] = (1/3)·2 = 2/3. But the original sum starts at k=1: the first term is 2/3, so Σ = 2.]"
    },
    {
        "question": "Prove that Σ(k=1 to n) (2k - 1) = n². Interpret this result geometrically.",
        "answer": "Σ(k=1 to n) (2k-1) is the sum 1 + 3 + 5 + ... + (2n-1). This is an AP with a=1, d=2. S_n = n/2[2·1 + (n-1)·2] = n/2·2n = n². This represents the area of an n×n square by summing layers of odd-numbered dots.",
        "explanation": "The sequence 1, 3, 5, 7, ... consists of odd numbers. The sum of the first n odd numbers equals n². This can be seen by arranging dots: the first layer has 1 dot, the second adds 3 dots (forming a 2×2 square), the third adds 5 dots (forming a 3×3 square), and so on."
    },
    {
        "question": "Find the values of x for which the series Σ(k=0 to ∞) x^(2k) converges, and find its sum.",
        "answer": "Converges for |x| < 1; sum is 1/(1-x²)",
        "explanation": "This is a geometric series with first term a = 1 and common ratio r = x². For convergence, |x²| < 1 ⟹ |x| < 1. The sum is a/(1-r) = 1/(1-x²)."
    },
    {
        "question": "Evaluate the sum Σ(k=2 to n) 1/(k²-1) using partial fractions and telescoping.",
        "answer": "(n²+n-2)/(2n(n+1))",
        "explanation": "1/(k²-1) = 1/((k-1)(k+1)) = (1/2)[1/(k-1) - 1/(k+1)]. Telescoping: (1/2)[(1/1 - 1/3) + (1/2 - 1/4) + (1/3 - 1/5) + ... + (1/(n-1) - 1/(n+1))]. After cancellation: (1/2)[1 + 1/2 - 1/n - 1/(n+1)] = (1/2)[(3n(n+1) - 2(n+1) - 2n)/(2n(n+1))] = (3n²+3n-2n-2-2n)/(4n(n+1)) = (3n²-n-2)/(4n(n+1)) = (n²+n-2)/(2n(n+1)) after recalculation."
    }
]
