TITLE = "Introduction to Logarithms"

SECTIONS = [
    {
        "title": "Logarithms as Inverse of Exponentials",
        "body": """
        <h3>The Inverse Relationship</h3>
        <p><strong>Logarithm</strong> is the inverse function of exponential.</p>

        <h4>Definition</h4>
        <p style="text-align: center; font-size: 1.2em;">
            <strong>If aˣ = y, then log_a(y) = x</strong>
        </p>

        <p>Read: "log base a of y equals x"</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Express in logarithmic form</p>
            <ul>
                <li>2⁵ = 32 ⟹ log₂(32) = 5</li>
                <li>10³ = 1000 ⟹ log₁₀(1000) = 3</li>
                <li>eˣ = y ⟹ ln(y) = x (natural logarithm)</li>
            </ul>
        </div>

        <h4>Key Properties</h4>
        <ul>
            <li>log_a(1) = 0 (since a⁰ = 1)</li>
            <li>log_a(a) = 1 (since a¹ = a)</li>
            <li>log_a(aˣ) = x (logarithm undoes exponent)</li>
            <li>a^(log_a(y)) = y (exponent undoes logarithm)</li>
        </ul>

        <div class="success-box">
            <p><strong>Key Insight:</strong> Logarithms "undo" exponents. If you know the exponent and base, use exponent. If you know the result and base, use logarithm.</p>
        </div>
        """
    },
    {
        "title": "Common Logarithms and Natural Logarithms",
        "body": """
        <h3>Two Important Bases</h3>

        <h4>Common Logarithm (Base 10)</h4>
        <p><strong>log₁₀(x)</strong> is often written simply as <strong>log(x)</strong></p>
        <ul>
            <li>log(10) = 1</li>
            <li>log(100) = 2</li>
            <li>log(1000) = 3</li>
            <li>Very useful for orders of magnitude</li>
        </ul>

        <h4>Natural Logarithm (Base e)</h4>
        <p><strong>ln(x) = log_e(x)</strong> where e ≈ 2.71828</p>
        <ul>
            <li>ln(e) = 1</li>
            <li>ln(1) = 0</li>
            <li>ln(eˣ) = x</li>
            <li>e^(ln(x)) = x</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 2:</strong> If eˣ = 50, find x</p>
            <p>x = ln(50) ≈ 3.912</p>
        </div>

        <div class="concept-box">
            <p><strong>Why base e?</strong> The number e appears naturally in continuous growth and decay problems. The derivative of eˣ is itself, making it unique in calculus.</p>
        </div>
        """
    }
]
