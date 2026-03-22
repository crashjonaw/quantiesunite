CHECKS = [
    {
        "q": "Simplify (2 + 3i) + (4 - i) - (1 + 2i)",
        "a": "5",
        "hint": "Combine real parts: 2 + 4 - 1 = 5. Combine imaginary parts: 3i - i - 2i = 0."
    },
    {
        "q": "Express 3 - 3i in polar form (modulus-argument form)",
        "a": "3√2·cis(7π/4) or 3√2·cis(-π/4)",
        "hint": "r = |3 - 3i| = √(9 + 9) = 3√2. arg(3 - 3i) = -π/4 (fourth quadrant)."
    },
    {
        "q": "Find the cube roots of 27. (Hint: use De Moivre's theorem)",
        "a": "3, 3·e^(2πi/3), 3·e^(4πi/3) or 3, -3/2 + 3√3i/2, -3/2 - 3√3i/2",
        "hint": "27 = 27·cis(0). The cube roots are 27^(1/3)·cis(2πk/3) for k = 0, 1, 2."
    },
    {
        "q": "Find |z| if z = (1 + i)/(1 - i)",
        "a": "1",
        "hint": "z = (1 + i)(1 + i)/[(1 - i)(1 + i)] = (1 + 2i - 1)/2 = i. So |z| = |i| = 1."
    },
    {
        "q": "Describe the locus |z - 2| = |z + 2|",
        "a": "The imaginary axis (the line x = 0)",
        "hint": "Points equidistant from 2 and -2 lie on the perpendicular bisector, which is the vertical line through their midpoint."
    }
]
