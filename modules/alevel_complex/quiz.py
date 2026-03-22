QUIZ = [
    {
        "question": "Calculate (1 + i)² and express your answer in the form a + bi",
        "answer": "2i",
        "explanation": "(1 + i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i"
    },
    {
        "question": "If z = 2 + 3i, find z⁻¹ (the multiplicative inverse of z)",
        "answer": "(2 - 3i)/13",
        "explanation": "z⁻¹ = 1/z = (1/(2 + 3i)) · (2 - 3i)/(2 - 3i) = (2 - 3i)/(4 + 9) = (2 - 3i)/13"
    },
    {
        "question": "Show that the fourth roots of unity satisfy w⁴ = 1 and sum to 0",
        "answer": "The fourth roots are 1, i, -1, -i. Their sum is 1 + i - 1 - i = 0. Each raised to the fourth power equals 1.",
        "explanation": "In polar form: w_k = cis(πk/2) for k = 0, 1, 2, 3. These give 1, i, -1, -i respectively. Sum = 1 + i + (-1) + (-i) = 0. Also, 1⁴ = i⁴ = (-1)⁴ = (-i)⁴ = 1."
    },
    {
        "question": "Use De Moivre's theorem to find (cos θ + i sin θ)¹⁰ and identify a trigonometric identity.",
        "answer": "cos(10θ) + i sin(10θ). This shows that cos(10θ) = Re[(cos θ + i sin θ)¹⁰] and sin(10θ) = Im[(cos θ + i sin θ)¹⁰].",
        "explanation": "By De Moivre's theorem, (cos θ + i sin θ)¹⁰ = cos(10θ) + i sin(10θ). Expanding the left side (binomial theorem) and comparing real and imaginary parts yields formulas for cos(10θ) and sin(10θ) as polynomials in cos θ and sin θ."
    },
    {
        "question": "Find all complex numbers z such that z² = 1 + i",
        "answer": "z = ±(1 + i)^(1/2) = ±(√(2√2/2)(cos(π/8) + i sin(π/8))) or z = ±((1+√2)/√2 + i(√2-1)/√2)^(1/2)",
        "explanation": "Convert 1 + i to polar: 1 + i = √2·cis(π/4). Then (1+i)^(1/2) = 2^(1/4)·cis(π/8) and 2^(1/4)·cis(π/8 + π) = 2^(1/4)·cis(9π/8). These are the two square roots: z = ±2^(1/4)[cos(π/8) + i sin(π/8)]."
    }
]
