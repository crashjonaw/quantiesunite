"""Integration by Substitution (u-substitution) — Concept lesson."""

TITLE = "Integration by Substitution"

SECTIONS = [
    {
        "title": "The Substitution Method",
        "body": """
        <p >Substitution is used when an integrand is a composite function. The key is to recognize a function and its derivative within the integrand.</p>
        <div class="concept-box">
            <strong>Substitution Rule:</strong> If $$u = g(x)$$, then $$du = g'(x)\\,dx$$
            $$\\int f(g(x))\\,g'(x)\\,dx = \\int f(u)\\,du$$
        </div>
        """
    },
    {
        "title": "Step-by-Step Process",
        "body": """
        <div class="concept-box">
            <strong>Steps:</strong>
            <ol >
                <li>Identify the inner function; let $$u$$ equal it</li>
                <li>Compute $$du = g'(x)\\,dx$$</li>
                <li>Rewrite the integral in terms of $$u$$</li>
                <li>Integrate with respect to $$u$$</li>
                <li>Substitute back the original variable</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Worked Examples",
        "body": """
        <div class="worked-example">
            <strong>Example 1:</strong> $$\\int 2x(x^2+1)^5\\,dx$$
            <br><br>
            Let $$u = x^2 + 1$$, then $$du = 2x\\,dx$$
            <br>
            $$\\int 2x(x^2+1)^5\\,dx = \\int u^5\\,du = \\frac{u^6}{6} + C = \\frac{(x^2+1)^6}{6} + C$$
        </div>
        <div class="worked-example">
            <strong>Example 2:</strong> $$\\int e^{3x}\\,dx$$
            <br><br>
            Let $$u = 3x$$, then $$du = 3\\,dx$$ so $$dx = \\frac{du}{3}$$
            <br>
            $$\\int e^{3x}\\,dx = \\int e^u\\,\\frac{du}{3} = \\frac{1}{3}e^u + C = \\frac{1}{3}e^{3x} + C$$
        </div>
        """
    }
]
