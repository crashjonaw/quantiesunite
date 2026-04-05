TITLE = "The Derivative from First Principles"

SECTIONS = [
    {
        "title": "Definition of the Derivative",
        "body": """
        <h3>The Derivative Formula</h3>
        <p>The <strong>derivative</strong> of $f(x)$ at point $x$ is defined as:</p>

        <div class="concept-box" style="text-align: center; font-size: 1.15em; padding: 16px; margin: 12px 0">
            <p>$$f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$$</p>
            <em style="font-size: 0.85em; margin-top: 8px; display: block;">Also written as: $\\frac{dy}{dx}$ or $\\frac{d}{dx}[f(x)]$</em>
        </div>

        <h3>What the Derivative Represents</h3>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>Instantaneous rate of change:</strong> How fast $f$ is changing at $x$</li>
            <li><strong>Slope of tangent line:</strong> Slope of the line touching the curve at $x$</li>
            <li><strong>Local behavior:</strong> Describes the function's behavior near $x$</li>
        </ul>

        <div class="warning-box formula-box">
            <p><strong>Note:</strong> The derivative may not exist everywhere. If the function has a corner, cusp, or vertical tangent, the derivative is undefined at that point.</p>
        </div>
        """
    },
    {
        "title": "Derivatives from First Principles: Examples",
        "body": """
        <h3>Example 1: Linear Function</h3>
        <p>Find $f'(x)$ for $f(x) = 3x + 2$</p>

        <div class="worked-example formula-box">
            <p>$f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{3(x+h) + 2 - (3x + 2)}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{3x + 3h + 2 - 3x - 2}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{3h}{h} = \\lim_{h \\to 0} 3 = $ <strong>3</strong></p>
            <p><em>The derivative is constant (the function is linear with slope 3).</em></p>
        </div>

        <h3>Example 2: Quadratic Function</h3>
        <p>Find $f'(x)$ for $f(x) = x^2$</p>

        <div class="worked-example formula-box">
            <p>$f'(x) = \\lim_{h \\to 0} \\frac{(x+h)^2 - x^2}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{x^2 + 2xh + h^2 - x^2}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{2xh + h^2}{h}$</p>
            <p>$= \\lim_{h \\to 0} (2x + h) = $ <strong>$2x$</strong></p>
        </div>

        <h3>Example 3: Square Root Function</h3>
        <p>Find $f'(x)$ for $f(x) = \\sqrt{x}$</p>

        <div class="worked-example formula-box">
            <p>$f'(x) = \\lim_{h \\to 0} \\frac{\\sqrt{x+h} - \\sqrt{x}}{h}$</p>
            <p><strong>Rationalize:</strong> Multiply by $\\frac{\\sqrt{x+h} + \\sqrt{x}}{\\sqrt{x+h} + \\sqrt{x}}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{(x+h) - x}{h(\\sqrt{x+h} + \\sqrt{x})}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{h}{h(\\sqrt{x+h} + \\sqrt{x})}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{1}{\\sqrt{x+h} + \\sqrt{x}} = $ <strong>$\\frac{1}{2\\sqrt{x}}$</strong></p>
        </div>

        <div class="success-box formula-box">
            <p><strong>Key Technique:</strong> When the limit gives $\\frac{0}{0}$, algebraically manipulate (factor, rationalize, conjugate) to cancel the $h$ in the denominator.</p>
        </div>
        """
    },
    {
        "title": "Notation and Higher Derivatives",
        "body": """
        <h3>Notation</h3>
        <p>The derivative of $f(x)$ can be written as:</p>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>$f'(x)$</strong> — Lagrange notation</li>
            <li><strong>$\\frac{dy}{dx}$</strong> — Leibniz notation (treats as ratio of infinitesimals)</li>
            <li><strong>$\\frac{d}{dx}[f(x)]$</strong> — Operator notation</li>
            <li><strong>$Df(x)$</strong> — D-operator notation</li>
        </ul>

        <h3>Second Derivative</h3>
        <p>The derivative of the derivative measures the <strong>rate of change of the slope</strong>:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$f''(x) = \\frac{d}{dx}[f'(x)] = \\frac{d^2y}{dx^2}$$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> For $f(x) = x^3$</p>
            <p>$f'(x) = 3x^2$</p>
            <p>$f''(x) = 6x$</p>
            <p>$f'''(x) = 6$</p>
        </div>

        <h3>Interpretation</h3>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>$f'(x) > 0$:</strong> Function is increasing</li>
            <li><strong>$f'(x) < 0$:</strong> Function is decreasing</li>
            <li><strong>$f''(x) > 0$:</strong> Function is concave up ($\\cup$)</li>
            <li><strong>$f''(x) < 0$:</strong> Function is concave down ($\\cap$)</li>
        </ul>
        """
    }
]
