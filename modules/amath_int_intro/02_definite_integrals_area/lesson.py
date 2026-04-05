TITLE = "Definite Integrals and Area Under Curves"

SECTIONS = [
    {
        "title": "The Definite Integral",
        "body": """
        <h3>The Definite Integral</h3>
        <p>The <strong>definite integral</strong> of $f(x)$ from $a$ to $b$ gives the signed area under the curve:</p>

        <p>$$\\int_a^b f(x)\\,dx = F(b) - F(a)$$</p>

        <p>where $F$ is any antiderivative of $f$. This is the <strong>Fundamental Theorem of Calculus</strong>.</p>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Calculate $\\int_1^3 x^2\\,dx$</p>
            <p>$F(x) = \\frac{x^3}{3}$ (an antiderivative)</p>
            <p>$\\int_1^3 x^2\\,dx = \\left[\\frac{x^3}{3}\\right]_1^3 = \\frac{27}{3} - \\frac{1}{3} = \\frac{26}{3}$</p>
        </div>

        <h4>Interpretation</h4>
        <ul>
            <li>If $f(x) \\geq 0$ on $[a, b]$: definite integral = area under the curve</li>
            <li>If $f(x) < 0$ on $[a, b]$: definite integral = negative of area above the curve</li>
            <li>For mixed signs: integral = area above $x$-axis minus area below</li>
        </ul>

        <h4>Properties</h4>
        <ul>
            <li>$\\int_a^b f(x)\\,dx = -\\int_b^a f(x)\\,dx$ (reversing limits negates)</li>
            <li>$\\int_a^c f(x)\\,dx = \\int_a^b f(x)\\,dx + \\int_b^c f(x)\\,dx$ (splitting interval)</li>
            <li>$\\int_a^b [f(x) + g(x)]\\,dx = \\int_a^b f(x)\\,dx + \\int_a^b g(x)\\,dx$</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 5:</strong> Find the area under $y = 2x$ from $x = 1$ to $x = 4$</p>
            <p>Area $= \\int_1^4 2x\\,dx = \\left[x^2\\right]_1^4 = 16 - 1 = 15$</p>
        </div>
        """
    },
    {
        "title": "Area Between Two Curves",
        "body": """
        <h4>Area Between Two Curves</h4>
        <p>If $f(x) \\geq g(x)$ on $[a, b]$, the area between them is:</p>

        <p>$$\\text{Area} = \\int_a^b [f(x) - g(x)]\\,dx$$</p>

        <div class="worked-example">
            <p><strong>Example 6:</strong> Find the area between $y = x^2$ and $y = 2x$ from $x = 0$ to $x = 2$</p>
            <p>First, find which curve is on top. At $x = 1$: $y = 1$ for $x^2$, $y = 2$ for $2x$. So $2x \\geq x^2$</p>
            <p>Area $= \\int_0^2 (2x - x^2)\\,dx = \\left[x^2 - \\frac{x^3}{3}\\right]_0^2 = 4 - \\frac{8}{3} = \\frac{4}{3}$</p>
        </div>

        <div class="concept-box">
            <p><strong>Key Steps:</strong></p>
            <ol>
                <li>Find intersection points by solving $f(x) = g(x)$</li>
                <li>Determine which curve is on top in the interval</li>
                <li>Integrate the difference</li>
            </ol>
        </div>
        """
    }
]
