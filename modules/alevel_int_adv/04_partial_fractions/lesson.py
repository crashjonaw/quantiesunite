"""Integration by Partial Fractions — Concept lesson."""

TITLE = "Integration by Partial Fractions"

SECTIONS = [
    {
        "title": "Decomposing Rational Functions",
        "body": """
        <p >When integrating rational functions (ratios of polynomials), partial fraction decomposition breaks the fraction into simpler parts that are easier to integrate.</p>
        <div class="concept-box">
            <strong>Key Idea:</strong> Express a complex rational function as a sum of simpler fractions with linear or quadratic denominators.
            $$\\frac{P(x)}{Q(x)} = A_1(x) + \\frac{A}{x-a} + \\frac{B}{x-b} + \\cdots$$
        </div>
        """
    },
    {
        "title": "Cases for Partial Fractions",
        "body": """
        <div class="concept-box">
            <strong>Case 1 — Distinct Linear Factors:</strong>
            $$\\frac{P(x)}{(x-a)(x-b)} = \\frac{A}{x-a} + \\frac{B}{x-b}$$
        </div>
        <div class="concept-box">
            <strong>Case 2 — Repeated Linear Factors:</strong>
            $$\\frac{P(x)}{(x-a)^2} = \\frac{A}{x-a} + \\frac{B}{(x-a)^2}$$
        </div>
        <div class="concept-box">
            <strong>Case 3 — Irreducible Quadratic Factors:</strong>
            $$\\frac{P(x)}{(x^2+bx+c)} = \\frac{Ax+B}{x^2+bx+c}$$
        </div>
        """
    },
    {
        "title": "Worked Example — Distinct Linear Factors",
        "body": """
        <div class="worked-example">
            <strong>Example:</strong> Integrate $$\\int \\frac{5}{(x-1)(x+2)}\\,dx$$
            <br><br>
            Step 1: Decompose $$\\frac{5}{(x-1)(x+2)} = \\frac{A}{x-1} + \\frac{B}{x+2}$$
            <br>
            Step 2: Multiply by $(x-1)(x+2)$: $$5 = A(x+2) + B(x-1)$$
            <br>
            Step 3: Set $x=1$: $$5 = 3A \\Rightarrow A = \\frac{5}{3}$$
            <br>
            Step 4: Set $x=-2$: $$5 = -3B \\Rightarrow B = -\\frac{5}{3}$$
            <br><br>
            $$\\int \\frac{5}{(x-1)(x+2)}\\,dx = \\frac{5}{3}\\ln|x-1| - \\frac{5}{3}\\ln|x+2| + C = \\frac{5}{3}\\ln\\left|\\frac{x-1}{x+2}\\right| + C$$
        </div>
        """
    }
]
