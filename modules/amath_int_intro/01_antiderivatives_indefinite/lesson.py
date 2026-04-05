TITLE = "Antiderivatives and Indefinite Integrals"

SECTIONS = [
    {
        "title": "The Antiderivative",
        "body": """
        <h3>The Antiderivative</h3>
        <p>An <strong>antiderivative</strong> of $f(x)$ is a function $F(x)$ such that $F'(x) = f(x)$.</p>

        <p>$$\\text{If } F'(x) = f(x), \\text{ then } F \\text{ is an antiderivative of } f$$</p>

        <div class="concept-box">
            <p><strong>Example 1:</strong> Find an antiderivative of $f(x) = 3x^2$</p>
            <p>We need $F(x)$ such that $F'(x) = 3x^2$</p>
            <p>$F(x) = x^3$ works, because $(x^3)' = 3x^2$</p>
        </div>

        <h4>The Indefinite Integral</h4>
        <p>The <strong>indefinite integral</strong> is the family of all antiderivatives:</p>

        <p>$$\\int f(x)\\,dx = F(x) + C$$</p>

        <p>where $C$ is the <strong>constant of integration</strong>.</p>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Find $\\int 3x^2\\,dx$</p>
            <p>$\\int 3x^2\\,dx = x^3 + C$</p>
            <p>(Check: $\\frac{d}{dx}[x^3 + C] = 3x^2$ )</p>
        </div>

        <h4>Why the Constant?</h4>
        <p>If $F(x)$ is an antiderivative, so is $F(x) + C$ for any constant $C$, because the derivative of $C$ is 0.</p>
        """
    },
    {
        "title": "Basic Integration Rules",
        "body": """
        <h4>Basic Integration Rules</h4>
        <ul>
            <li><strong>Power Rule:</strong> $\\int x^n\\,dx = \\frac{x^{n+1}}{n+1} + C$ (for $n \\neq -1$)</li>
            <li><strong>Constant Multiple:</strong> $\\int k f(x)\\,dx = k\\int f(x)\\,dx$</li>
            <li><strong>Sum/Difference:</strong> $\\int [f(x) + g(x)]\\,dx = \\int f(x)\\,dx + \\int g(x)\\,dx$</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Find $\\int (4x^3 - 2x + 5)\\,dx$</p>
            <p>$= 4\\int x^3\\,dx - 2\\int x\\,dx + 5\\int 1\\,dx$</p>
            <p>$= 4 \\cdot \\frac{x^4}{4} - 2 \\cdot \\frac{x^2}{2} + 5x + C$</p>
            <p>$= x^4 - x^2 + 5x + C$</p>
        </div>

        <h4>Special Integrals</h4>
        <ul>
            <li>$\\int e^x\\,dx = e^x + C$</li>
            <li>$\\int \\frac{1}{x}\\,dx = \\ln|x| + C$</li>
            <li>$\\int \\sin(x)\\,dx = -\\cos(x) + C$</li>
            <li>$\\int \\cos(x)\\,dx = \\sin(x) + C$</li>
            <li>$\\int \\sec^2(x)\\,dx = \\tan(x) + C$</li>
        </ul>

        <div class="concept-box">
            <p><strong>Tip:</strong> Always check your answer by taking the derivative!</p>
        </div>
        """
    }
]
