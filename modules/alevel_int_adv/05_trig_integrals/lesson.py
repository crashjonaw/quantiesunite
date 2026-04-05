"""Trigonometric Integrals and Substitutions — Concept lesson."""

TITLE = "Trigonometric Integrals and Substitutions"

SECTIONS = [
    {
        "title": "Standard Trigonometric Integrals",
        "body": """
        <div class="concept-box">
            <strong>Fundamental Trig Integrals:</strong>
            <ul >
                <li>$$\\int \\sin(x)\\,dx = -\\cos(x) + C$$</li>
                <li>$$\\int \\cos(x)\\,dx = \\sin(x) + C$$</li>
                <li>$$\\int \\sec^2(x)\\,dx = \\tan(x) + C$$</li>
                <li>$$\\int \\csc^2(x)\\,dx = -\\cot(x) + C$$</li>
                <li>$$\\int \\sec(x)\\tan(x)\\,dx = \\sec(x) + C$$</li>
                <li>$$\\int \\csc(x)\\cot(x)\\,dx = -\\csc(x) + C$$</li>
            </ul>
        </div>
        <p >These are derived from the derivatives of trigonometric functions and are essential building blocks.</p>
        """
    },
    {
        "title": "Integrals of Powers of Sine and Cosine",
        "body": """
        <div class="worked-example">
            <strong>For odd powers:</strong> Factor out one trig function and use $$\\sin^2(x) + \\cos^2(x) = 1$$
            <br><br>
            Example: $$\\int \\sin^3(x)\\,dx$$
            <br>
            $$= \\int \\sin^2(x) \\sin(x)\\,dx = \\int (1-\\cos^2(x)) \\sin(x)\\,dx$$
            <br>
            Let $$u = \\cos(x)$$, then $$du = -\\sin(x)\\,dx$$
            <br>
            $$= -\\int (1-u^2)\\,du = -u + \\frac{u^3}{3} + C = -\\cos(x) + \\frac{\\cos^3(x)}{3} + C$$
        </div>
        <div class="worked-example">
            <strong>For even powers:</strong> Use double angle formulas: $$\\sin^2(x) = \\frac{1-\\cos(2x)}{2}, \\cos^2(x) = \\frac{1+\\cos(2x)}{2}$$
        </div>
        """
    },
    {
        "title": "Trigonometric Substitution",
        "body": """
        <div class="concept-box">
            <strong>When to use trig substitution:</strong>
            <ul >
                <li>$$\\sqrt{a^2 - x^2}$$ → Use $$x = a\\sin(\\theta)$$</li>
                <li>$$\\sqrt{a^2 + x^2}$$ → Use $$x = a\\tan(\\theta)$$</li>
                <li>$$\\sqrt{x^2 - a^2}$$ → Use $$x = a\\sec(\\theta)$$</li>
            </ul>
        </div>
        <div class="worked-example">
            <strong>Example:</strong> $$\\int \\sqrt{9-x^2}\\,dx$$
            <br><br>
            Let $$x = 3\\sin(\\theta)$$, then $$dx = 3\\cos(\\theta)\\,d\\theta$$
            <br>
            $$\\sqrt{9-x^2} = \\sqrt{9 - 9\\sin^2(\\theta)} = 3\\cos(\\theta)$$
            <br>
            $$= \\int 3\\cos(\\theta) \\cdot 3\\cos(\\theta)\\,d\\theta = 9\\int \\cos^2(\\theta)\\,d\\theta$$
            <br>
            $$= 9 \\cdot \\frac{\\theta + \\sin(\\theta)\\cos(\\theta)}{2} + C = \\frac{9}{2}\\arcsin\\left(\\frac{x}{3}\\right) + \\frac{x\\sqrt{9-x^2}}{2} + C$$
        </div>
        """
    }
]
