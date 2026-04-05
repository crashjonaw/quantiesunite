TITLE = "R-Formula and Auxiliary Angle Method"

SECTIONS = [
    {
        "title": "The R-Formula",
        "body": """
        <div class="concept-box">
            <h3>Converting a sin x + b cos x to R sin(x + α)</h3>
            <p>This is one of the most useful techniques in trigonometry. It allows us to express any linear combination of sine and cosine as a single sinusoidal function.</p>
        </div>

        <h4>The Formula</h4>
        <p>We want to express:</p>
        <div class="formula">$$a\\sin x + b\\cos x$$</div>

        <p>in the form:</p>
        <div class="formula">$$R\\sin(x + \\alpha)$$</div>

        <p><strong>where:</strong></p>
        <div class="formula">$$R = \\sqrt{a^2 + b^2}$$</div>
        <div class="formula">$$\\tan \\alpha = \\frac{b}{a}$$</div>

        <h4>Derivation</h4>
        <p>Expand \\(R\\sin(x + \\alpha)\\) using the addition formula:</p>
        <div class="formula">$$R\\sin(x + \\alpha) = R(\\sin x \\cos \\alpha + \\cos x \\sin \\alpha) = R\\cos \\alpha \\sin x + R\\sin \\alpha \\cos x$$</div>

        <p>Comparing with \\(a\\sin x + b\\cos x\\), we need:</p>
        <ul>
            <li>\\(R\\cos \\alpha = a\\)</li>
            <li>\\(R\\sin \\alpha = b\\)</li>
        </ul>

        <p>Squaring and adding: \\(R^2 = a^2 + b^2\\), so \\(R = \\sqrt{a^2 + b^2}\\)</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Express \\(3\\sin \\theta + 4\\cos \\theta\\) in the form \\(R\\sin(\\theta + \\alpha)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Calculate \\(R\\):</li>
                <li>$$R = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$$</li>
                <li>Calculate \\(\\alpha\\):</li>
                <li>$$\\tan \\alpha = \\frac{4}{3}$$</li>
                <li>$$\\alpha = \\arctan\\left(\\frac{4}{3}\\right) \\approx 53.1°$$</li>
                <li><strong>Therefore:</strong> \\(3\\sin \\theta + 4\\cos \\theta = 5\\sin(\\theta + 53.1°)\\)</li>
            </ol>
            <p><strong>Verification:</strong> \\(5\\sin(\\theta + 53.1°) = 5(\\sin\\theta \\cos(53.1°) + \\cos\\theta \\sin(53.1°)) = 5(\\sin\\theta \\cdot 0.6 + \\cos\\theta \\cdot 0.8) = 3\\sin\\theta + 4\\cos\\theta\\) ✓</p>
        </div>
        """
    },
    {
        "title": "Applications of the R-Formula",
        "body": """
        <div class="concept-box">
            <h3>Finding Maximum and Minimum Values</h3>
        </div>

        <h4>Finding Extrema</h4>
        <p>Once we've expressed \\(a\\sin x + b\\cos x = R\\sin(x + \\alpha)\\), we can immediately identify:</p>
        <ul>
            <li><strong>Maximum value:</strong> \\(R\\) (when \\(\\sin(x + \\alpha) = 1\\))</li>
            <li><strong>Minimum value:</strong> \\(-R\\) (when \\(\\sin(x + \\alpha) = -1\\))</li>
        </ul>

        <div class="worked-example">
            <h4>Worked Example: Finding Extrema</h4>
            <p><strong>Problem:</strong> Find the maximum and minimum values of \\(y = 3\\sin \\theta + 4\\cos \\theta\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>From the previous example: \\(y = 5\\sin(\\theta + 53.1°)\\)</li>
                <li>Since the range of \\(\\sin(\\theta + 53.1°)\\) is \\([-1, 1]\\):</li>
                <li><strong>Maximum:</strong> \\(y_{\\max} = 5 \\times 1 = 5\\)</li>
                <li><strong>Minimum:</strong> \\(y_{\\min} = 5 \\times (-1) = -5\\)</li>
            </ol>
        </div>

        <h4>Solving Equations</h4>
        <p>The R-formula also simplifies solving equations of the form \\(a\\sin x + b\\cos x = c\\).</p>

        <div class="worked-example">
            <h4>Worked Example: Solving an Equation</h4>
            <p><strong>Problem:</strong> Solve \\(3\\sin \\theta + 4\\cos \\theta = 3\\) for \\(0° \\leq \\theta < 360°\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Use the R-formula result: \\(5\\sin(\\theta + 53.1°) = 3\\)</li>
                <li>$$\\sin(\\theta + 53.1°) = \\frac{3}{5} = 0.6$$</li>
                <li>The general solutions are:</li>
                <li>$$\\theta + 53.1° = \\sin^{-1}(0.6) \\approx 36.9°$$</li>
                <li>$$\\theta + 53.1° = 180° - 36.9° = 143.1°$$</li>
                <li>Therefore: \\(\\theta \\approx 36.9° - 53.1° = -16.2°\\) (adjust: \\(343.8°\\)) or \\(\\theta \\approx 143.1° - 53.1° = 90°\\)</li>
                <li><strong>Solutions (approximately):</strong> \\(\\theta \\approx 90°\\)</li>
            </ol>
        </div>
        """
    },
    {
        "title": "The Cosine Form and Variations",
        "body": """
        <h4>Alternative Form: Using Cosine</h4>
        <p>We can also express \\(a\\sin x + b\\cos x\\) using cosine:</p>
        <div class="formula">$$a\\sin x + b\\cos x = R\\cos(x - \\beta)$$</div>

        <p><strong>where:</strong></p>
        <div class="formula">$$R = \\sqrt{a^2 + b^2}$$</div>
        <div class="formula">$$\\tan \\beta = \\frac{a}{b}$$</div>

        <h4>When to Use Each Form</h4>
        <ul>
            <li><strong>Sine form:</strong> \\(R\\sin(x + \\alpha)\\) - use when the formula asks specifically for sine form</li>
            <li><strong>Cosine form:</strong> \\(R\\cos(x - \\beta)\\) - use when the formula asks specifically for cosine form</li>
            <li>Both give equivalent results; choose based on context or preference</li>
        </ul>

        <div class="warning-box">
            <h4>Important: Signs and Quadrants</h4>
            <p>When finding \\(\\alpha\\) or \\(\\beta\\), pay attention to:</p>
            <ul>
                <li>Whether the angle should be in degrees or radians</li>
                <li>Whether we need to adjust for the correct quadrant (use CAST rule or check signs of \\(a\\) and \\(b\\))</li>
                <li>Whether negative coefficients affect the angle calculation</li>
            </ul>
        </div>

        <div class="worked-example">
            <h4>Worked Example: Negative Coefficients</h4>
            <p><strong>Problem:</strong> Express \\(5\\sin \\theta - 12\\cos \\theta\\) in the form \\(R\\sin(\\theta - \\phi)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Calculate \\(R\\):</li>
                <li>$$R = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13$$</li>
                <li>Rearrange: \\(5\\sin\\theta - 12\\cos\\theta = 5\\sin\\theta + (-12)\\cos\\theta\\)</li>
                <li>For the form \\(R\\sin(\\theta - \\phi)\\), we expand and match coefficients to find \\(\\tan\\phi = \\frac{12}{5}\\)</li>
                <li>$$\\phi = \\arctan\\left(\\frac{12}{5}\\right) \\approx 67.4°$$</li>
                <li><strong>Therefore:</strong> \\(5\\sin\\theta - 12\\cos\\theta = 13\\sin(\\theta - 67.4°)\\)</li>
            </ol>
        </div>
        """
    }
]
