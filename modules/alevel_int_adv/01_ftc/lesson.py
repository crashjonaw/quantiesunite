"""The Fundamental Theorem of Calculus — Concept lesson."""

TITLE = "The Fundamental Theorem of Calculus"

SECTIONS = [
    {
        "title": "Understanding the FTC",
        "body": """
        <p >The Fundamental Theorem of Calculus establishes that differentiation and integration are inverse operations. This profound connection is the foundation of all calculus.</p>
        <div class="concept-box">
            <strong>FTC (Part 1):</strong> If $$F'(x) = f(x)$$ for all $$x$$ in $$[a, b]$$, then:
            $$\\int_a^b f(x)\\,dx = F(b) - F(a)$$
        </div>
        <p >This means: to evaluate a definite integral, find an antiderivative $$F(x)$$ and subtract its values at the bounds.</p>
        """
    },
    {
        "title": "Evaluating Definite Integrals",
        "body": """
        <div class="worked-example">
            <strong>Example:</strong> Evaluate $$\\int_1^3 2x\\,dx$$
            <br><br>
            Step 1: Find the antiderivative: $$F(x) = x^2$$
            <br>
            Step 2: Evaluate at bounds: $$F(3) - F(1) = 9 - 1 = 8$$
            <br><br>
            Therefore, $$\\int_1^3 2x\\,dx = 8$$
        </div>
        <p >The power of FTC is that it converts the problem from "finding area under a curve" to "finding an antiderivative and evaluating".</p>
        """
    },
    {
        "title": "Connection Between FTC Part 1 and Part 2",
        "body": """
        <div class="concept-box">
            <strong>FTC (Part 2):</strong> If $$f$$ is continuous on $$[a, b]$$, then:
            $$\\frac{d}{dx}\\left(\\int_a^x f(t)\\,dt\\right) = f(x)$$
        </div>
        <p >Part 2 shows that differentiation and integration undo each other. Taking the derivative of an integral returns the original function.</p>
        """
    }
]
