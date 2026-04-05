MINDMAP = {
    "concepts": [
        {
            "title": "Complex Number Basics",
            "points": [
                "\\(i = \\sqrt{-1}\\), so \\(i^2 = -1\\)",
                "General form: \\(z = a + bi\\) (real part \\(a\\), imaginary part \\(b\\))",
                "Complex conjugate: \\(z^* = a - bi\\)",
                "\\(z \\cdot z^* = a^2 + b^2 = |z|^2\\)",
            ],
        },
        {
            "title": "Argand Diagram & Polar Form",
            "points": [
                "Plot \\(z = a + bi\\) as point \\((a, b)\\) on the Argand diagram",
                "Modulus: \\(|z| = \\sqrt{a^2 + b^2}\\)",
                "Argument: \\(\\arg(z) = \\tan^{-1}\\left(\\frac{b}{a}\\right)\\) (adjusted for quadrant)",
                "Polar form: \\(z = r(\\cos\\theta + i\\sin\\theta) = re^{i\\theta}\\)",
            ],
        },
        {
            "title": "Operations in Polar Form",
            "points": [
                "Multiplication: multiply moduli, add arguments",
                "Division: divide moduli, subtract arguments",
                "\\(z_1 z_2 = r_1 r_2 e^{i(\\theta_1+\\theta_2)}\\)",
            ],
        },
        {
            "title": "De Moivre's Theorem",
            "points": [
                "\\((\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta\\)",
                "Useful for finding powers and roots of complex numbers",
                "\\(n\\)th roots of \\(z\\): \\(n\\) equally spaced points on a circle of radius \\(|z|^{1/n}\\)",
            ],
        },
        {
            "title": "Loci in the Complex Plane",
            "points": [
                "\\(|z - z_1| = r\\): circle centre \\(z_1\\), radius \\(r\\)",
                "\\(|z - z_1| = |z - z_2|\\): perpendicular bisector of \\(z_1\\) and \\(z_2\\)",
                "\\(\\arg(z - z_1) = \\alpha\\): half-line from \\(z_1\\) at angle \\(\\alpha\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Euler's form", "expr": "\\(e^{i\\theta} = \\cos\\theta + i\\sin\\theta\\)"},
        {"label": "De Moivre's", "expr": "\\((\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta\\)"},
        {"label": "Modulus product", "expr": "\\(|z_1 z_2| = |z_1||z_2|\\)"},
        {"label": "Argument product", "expr": "\\(\\arg(z_1 z_2) = \\arg(z_1) + \\arg(z_2)\\)"},
        {"label": "nth roots", "expr": "\\(z^{1/n} = r^{1/n} e^{i(\\theta + 2k\\pi)/n}, \\; k=0,1,\\ldots,n-1\\)"},
    ],
    "tips": [
        "Complex roots of real polynomials always come in conjugate pairs.",
        "When dividing complex numbers in Cartesian form, multiply numerator and denominator by the conjugate of the denominator.",
        "For loci problems, let \\(z = x + iy\\) and convert to a Cartesian equation if the geometric form is not obvious.",
    ],
}
