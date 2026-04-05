TITLE = "Integration Techniques: Substitution and Integration by Parts"

SECTIONS = [
    {
        "title": "Substitution (u-substitution)",
        "body": """
        <h3>Substitution (u-substitution)</h3>
        <p>For integrals of composite functions, use a substitution $u = g(x)$.</p>

        <h4>Method</h4>
        <ol>
            <li>Let $u = g(x)$</li>
            <li>Find $du = g'(x)\\,dx$</li>
            <li>Rewrite integral in terms of $u$</li>
            <li>Integrate with respect to $u$</li>
            <li>Substitute back to get answer in $x$</li>
        </ol>

        <div class="worked-example">
            <p><strong>Example 7:</strong> Find $\\int (3x + 1)^5\\,dx$</p>
            <p>Let $u = 3x + 1$, then $du = 3\\,dx$, so $dx = \\frac{du}{3}$</p>
            <p>$\\int (3x + 1)^5\\,dx = \\int u^5 \\cdot \\frac{du}{3} = \\frac{1}{3}\\int u^5\\,du$</p>
            <p>$= \\frac{1}{3} \\cdot \\frac{u^6}{6} + C = \\frac{u^6}{18} + C$</p>
            <p>$= \\frac{(3x + 1)^6}{18} + C$</p>
        </div>

        <h4>For Definite Integrals with Substitution</h4>
        <p>Change the limits of integration when you substitute:</p>

        <div class="worked-example">
            <p><strong>Example 8:</strong> Calculate $\\int_1^2 2x(x^2 + 1)^3\\,dx$</p>
            <p>Let $u = x^2 + 1$, then $du = 2x\\,dx$</p>
            <p>When $x = 1$: $u = 2$; when $x = 2$: $u = 5$</p>
            <p>$\\int_1^2 2x(x^2 + 1)^3\\,dx = \\int_2^5 u^3\\,du = \\left[\\frac{u^4}{4}\\right]_2^5$</p>
            <p>$= \\frac{625}{4} - \\frac{16}{4} = \\frac{609}{4}$</p>
        </div>
        """
    },
    {
        "title": "Integration by Parts",
        "body": """
        <h3>Integration by Parts</h3>
        <p>For products, use: <strong>$\\int u\\,dv = uv - \\int v\\,du$</strong></p>

        <p>Choose $u$ and $dv$ such that $\\int v\\,du$ is easier to integrate.</p>

        <div class="concept-box">
            <p><strong>Hint (LIATE Rule):</strong> Choose $u$ from functions that become simpler when differentiated:</p>
            <ul>
                <li><strong>L</strong>ogarithmic functions ($\\ln$)</li>
                <li><strong>I</strong>nverse trig functions ($\\arcsin$, $\\arccos$, etc.)</li>
                <li><strong>A</strong>lgebraic functions (polynomials)</li>
                <li><strong>T</strong>rigonometric functions ($\\sin$, $\\cos$)</li>
                <li><strong>E</strong>xponential functions ($e^x$)</li>
            </ul>
        </div>

        <div class="worked-example">
            <p><strong>Example 9:</strong> Find $\\int x e^x\\,dx$</p>
            <p>Let $u = x$, $dv = e^x\\,dx$</p>
            <p>Then $du = dx$, $v = e^x$</p>
            <p>$\\int x e^x\\,dx = x e^x - \\int e^x\\,dx = x e^x - e^x + C = (x - 1)e^x + C$</p>
        </div>
        """
    }
]
