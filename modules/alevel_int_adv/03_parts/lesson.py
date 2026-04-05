"""Integration by Parts — Concept lesson."""

TITLE = "Integration by Parts"

SECTIONS = [
    {
        "title": "The Integration by Parts Formula",
        "body": """
        <p >Integration by parts is derived from the product rule for differentiation. It is used to integrate products of different types of functions.</p>
        <div class="concept-box">
            <strong>Integration by Parts Formula:</strong>
            $$\\int u\\,dv = uv - \\int v\\,du$$
        </div>
        <p >The goal is to choose $$u$$ and $$dv$$ so that $$\\int v\\,du$$ is easier to integrate than the original integral.</p>
        """
    },
    {
        "title": "The LIATE Rule for Choosing u",
        "body": """
        <div class="concept-box">
            <strong>LIATE Priority (choose $$u$$ from highest priority):</strong>
            <ul >
                <li><strong>L</strong> — Logarithmic: $$\\ln(x)$$</li>
                <li><strong>I</strong> — Inverse trigonometric: $$\\arcsin(x), \\arccos(x), \\arctan(x)$$</li>
                <li><strong>A</strong> — Algebraic: $$x, x^2, 3x$$, etc.</li>
                <li><strong>T</strong> — Trigonometric: $$\\sin(x), \\cos(x)$$</li>
                <li><strong>E</strong> — Exponential: $$e^x, a^x$$</li>
            </ul>
        </div>
        <p >The term chosen as $$u$$ should be differentiated (to make it simpler), and $$dv$$ should be integrated.</p>
        """
    },
    {
        "title": "Worked Examples",
        "body": """
        <div class="worked-example">
            <strong>Example 1:</strong> $$\\int x e^x\\,dx$$
            <br><br>
            Choose $$u = x$$ (Algebraic) and $$dv = e^x\\,dx$$
            <br>
            Then $$du = dx$$ and $$v = e^x$$
            <br>
            $$\\int x e^x\\,dx = xe^x - \\int e^x\\,dx = xe^x - e^x + C = e^x(x-1) + C$$
        </div>
        <div class="worked-example">
            <strong>Example 2:</strong> $$\\int x\\cos(x)\\,dx$$
            <br><br>
            Choose $$u = x$$ and $$dv = \\cos(x)\\,dx$$
            <br>
            Then $$du = dx$$ and $$v = \\sin(x)$$
            <br>
            $$\\int x\\cos(x)\\,dx = x\\sin(x) - \\int \\sin(x)\\,dx = x\\sin(x) + \\cos(x) + C$$
        </div>
        """
    },
    {
        "title": "Repeated Integration by Parts",
        "body": """
        <p >Sometimes you need to apply integration by parts more than once. This happens with polynomials of degree 2 or higher.</p>
        <div class="worked-example">
            <strong>Example:</strong> $$\\int x^2 e^x\\,dx$$
            <br><br>
            First application: $$u = x^2, dv = e^x\\,dx$$
            <br>
            $$= x^2 e^x - 2\\int x e^x\\,dx$$
            <br><br>
            Second application on $$\\int x e^x\\,dx$$:
            <br>
            $$= x^2 e^x - 2(xe^x - e^x) + C = e^x(x^2 - 2x + 2) + C$$
        </div>
        """
    }
]
