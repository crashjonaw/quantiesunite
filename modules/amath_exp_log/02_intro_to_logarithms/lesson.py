TITLE = "Introduction to Logarithms"

SECTIONS = [
    {
        "title": "Logarithms as Inverse of Exponentials",
        "body": """
        <h3>The Inverse Relationship</h3>
        <p><strong>Logarithm</strong> is the inverse function of exponential.</p>

        <h4>Definition</h4>
        <p style="text-align: center; font-size: 1.2em;">
            <strong>If \\(a^x = y\\), then \\(\\log_a(y) = x\\)</strong>
        </p>

        <p>Read: "log base a of y equals x"</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Express in logarithmic form</p>
            <ul>
                <li>\\(2^5 = 32 \\Rightarrow \\log_2(32) = 5\\)</li>
                <li>\\(10^3 = 1000 \\Rightarrow \\log_{10}(1000) = 3\\)</li>
                <li>\\(e^x = y \\Rightarrow \\ln(y) = x\\) (natural logarithm)</li>
            </ul>
        </div>

        <h4>Key Properties</h4>
        <ul>
            <li>\\(\\log_a(1) = 0\\) (since \\(a^0 = 1\\))</li>
            <li>\\(\\log_a(a) = 1\\) (since \\(a^1 = a\\))</li>
            <li>\\(\\log_a(a^x) = x\\) (logarithm undoes exponent)</li>
            <li>\\(a^{\\log_a(y)} = y\\) (exponent undoes logarithm)</li>
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
        <p>\\(\\log_{10}(x)\\) is often written simply as \\(\\log(x)\\)</p>
        <ul>
            <li>\\(\\log(10) = 1\\)</li>
            <li>\\(\\log(100) = 2\\)</li>
            <li>\\(\\log(1000) = 3\\)</li>
            <li>Very useful for orders of magnitude</li>
        </ul>

        <h4>Natural Logarithm (Base e)</h4>
        <p>\\(\\ln(x) = \\log_e(x)\\) where \\(e \\approx 2.71828\\)</p>
        <ul>
            <li>\\(\\ln(e) = 1\\)</li>
            <li>\\(\\ln(1) = 0\\)</li>
            <li>\\(\\ln(e^x) = x\\)</li>
            <li>\\(e^{\\ln(x)} = x\\)</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 2:</strong> If \\(e^x = 50\\), find \\(x\\)</p>
            <p>\\(x = \\ln(50) \\approx 3.912\\)</p>
        </div>

        <div class="concept-box">
            <p><strong>Why base e?</strong> The number \\(e\\) appears naturally in continuous growth and decay problems. The derivative of \\(e^x\\) is itself, making it unique in calculus.</p>
        </div>
        """
    }
]
