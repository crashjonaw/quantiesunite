TITLE = "Laws of Logarithms"

SECTIONS = [
    {
        "title": "The Product, Quotient, and Power Rules",
        "body": """
        <h3>Three Core Laws</h3>

        <h4>The Power Rule</h4>
        <p>$$\\log_a(x^y) = y \\cdot \\log_a(x)$$</p>
        <p>The exponent "comes out front"</p>

        <h4>The Product Rule</h4>
        <p>$$\\log_a(xy) = \\log_a(x) + \\log_a(y)$$</p>
        <p>Logarithm of a product is the sum of logarithms</p>

        <h4>The Quotient Rule</h4>
        <p>$$\\log_a\\left(\\frac{x}{y}\\right) = \\log_a(x) - \\log_a(y)$$</p>
        <p>Logarithm of a quotient is the difference of logarithms</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Expand $\\log_2(8x^2 y)$</p>
            <p>$\\log_2(8x^2 y) = \\log_2(8) + \\log_2(x^2) + \\log_2(y)$</p>
            <p>$= 3 + 2\\log_2(x) + \\log_2(y)$</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Expand $\\log_5\\left(\\frac{25x^2}{y}\\right)$</p>
            <p>$\\log_5\\left(\\frac{25x^2}{y}\\right) = \\log_5(25) + \\log_5(x^2) - \\log_5(y)$</p>
            <p>$= 2 + 2\\log_5(x) - \\log_5(y)$</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Expand $\\ln(\\sqrt{x^2 y})$</p>
            <p>$\\ln(\\sqrt{x^2 y}) = \\ln((x^2 y)^{1/2})$</p>
            <p>$= \\frac{1}{2} \\ln(x^2 y)$</p>
            <p>$= \\frac{1}{2}[\\ln(x^2) + \\ln(y)]$</p>
            <p>$= \\frac{1}{2}[2\\ln(x) + \\ln(y)]$</p>
            <p>$= \\ln(x) + \\frac{1}{2}\\ln(y)$</p>
        </div>
        """
    },
    {
        "title": "Change of Base Formula",
        "body": """
        <h3>Converting Between Bases</h3>

        <h4>The Change of Base Formula</h4>
        <p>$$\\log_a(x) = \\frac{\\log_b(x)}{\\log_b(a)}$$</p>

        <p>This formula allows you to convert logarithms from any base to a base your calculator understands (usually base 10 or $e$).</p>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Calculate $\\log_3(27)$</p>
            <p><strong>Method 1:</strong> Recognize $3^x = 27 = 3^3$, so $x = 3$</p>
            <p><strong>Method 2 (Using change of base):</strong></p>
            <p>$\\log_3(27) = \\frac{\\log_{10}(27)}{\\log_{10}(3)} = \\frac{1.431}{0.477} \\approx 3$</p>
        </div>

        <h4>Why This Works</h4>
        <p>If $\\log_a(x) = y$, then $a^y = x$. Taking $\\log_b$ of both sides: $\\log_b(a^y) = \\log_b(x)$, so $y \\cdot \\log_b(a) = \\log_b(x)$, thus $y = \\frac{\\log_b(x)}{\\log_b(a)}$.</p>

        <div class="concept-box">
            <p><strong>Practical Tip:</strong> Always convert to $\\log$ or $\\ln$ for calculator work. Most scientific calculators have only these two functions.</p>
        </div>
        """
    }
]
