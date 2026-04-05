TITLE = "Addition Formulae"

SECTIONS = [
    {
        "title": "Sine and Cosine Addition Formulas",
        "body": """
        <div class="concept-box">
            <h3>Expressing sin(A ± B) and cos(A ± B)</h3>
            <p>These formulas are central to advanced trigonometry. They allow us to express the sine and cosine of a sum or difference of angles.</p>
        </div>

        <h4>The Addition Formulas</h4>
        <div class="formula">$$\\sin(A + B) = \\sin A \\cos B + \\cos A \\sin B$$</div>
        <div class="formula">$$\\sin(A - B) = \\sin A \\cos B - \\cos A \\sin B$$</div>
        <div class="formula">$$\\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B$$</div>
        <div class="formula">$$\\cos(A - B) = \\cos A \\cos B + \\sin A \\sin B$$</div>

        <p><strong>Memory tip:</strong> For sine addition, both terms have the form sin-cos or cos-sin. For cosine addition, both are cos-cos and sin-sin.</p>

        <div class="worked-example">
            <h4>Worked Example: Finding sin(75°)</h4>
            <p><strong>Problem:</strong> Find the exact value of \\(\\sin(75°)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Express 75° as a sum of standard angles: \\(75° = 45° + 30°\\)</li>
                <li>Apply the sine addition formula:</li>
                <li>$$\\sin(75°) = \\sin(45° + 30°)$$</li>
                <li>$$= \\sin(45°)\\cos(30°) + \\cos(45°)\\sin(30°)$$</li>
                <li>Substitute exact values:</li>
                <li>$$= \\frac{\\sqrt{2}}{2} \\cdot \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{2}}{2} \\cdot \\frac{1}{2}$$</li>
                <li>$$= \\frac{\\sqrt{6}}{4} + \\frac{\\sqrt{2}}{4}$$</li>
                <li>$$= \\frac{\\sqrt{6} + \\sqrt{2}}{4}$$</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Tangent Addition Formula",
        "body": """
        <h4>The Tangent Addition Formula</h4>
        <p>Just as we have formulas for sine and cosine of sums, we can derive a formula for tangent:</p>
        <div class="formula">$$\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A \\tan B}$$</div>
        <div class="formula">$$\\tan(A - B) = \\frac{\\tan A - \\tan B}{1 + \\tan A \\tan B}$$</div>

        <p><strong>Key difference:</strong> Note the signs in the denominator are opposite to those in the numerator.</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> If \\(\\tan(A+B) = 1\\) and \\(\\tan A = \\frac{1}{2}\\), find \\(\\tan B\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Use the tangent addition formula:</li>
                <li>$$1 = \\frac{\\frac{1}{2} + \\tan B}{1 - \\frac{1}{2}\\tan B}$$</li>
                <li>Multiply both sides by the denominator:</li>
                <li>$$1 - \\frac{1}{2}\\tan B = \\frac{1}{2} + \\tan B$$</li>
                <li>$$1 - \\frac{1}{2} = \\tan B + \\frac{1}{2}\\tan B$$</li>
                <li>$$\\frac{1}{2} = \\frac{3}{2}\\tan B$$</li>
                <li>$$\\tan B = \\frac{1}{3}$$</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Applications to Equation Solving",
        "body": """
        <div class="concept-box">
            <h3>Using Addition Formulas to Solve Equations</h3>
            <p>The addition formulas are powerful tools for solving trigonometric equations that involve sums or differences of angles.</p>
        </div>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Solve \\(\\sin(x + 30°) = 0.5\\) for \\(0° \\leq x < 360°\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Let \\(y = x + 30°\\). Then \\(\\sin y = 0.5\\)</li>
                <li>The general solutions for \\(\\sin y = 0.5\\) are \\(y = 30°\\) or \\(y = 150°\\)</li>
                <li>In the range \\([0°, 360°)\\): \\(y = 30°, 150°, 390°, 510°, ...\\)</li>
                <li>Accounting for periodicity within our range: \\(y = 30°, 150°\\)</li>
                <li>Substitute back: \\(x + 30° = 30°\\) or \\(x + 30° = 150°\\)</li>
                <li>$$x = 0° \\text{ or } x = 120°$$</li>
                <li><strong>Solutions:</strong> \\(x = 0°, 120°\\)</li>
            </ol>
        </div>

        <div class="success-box">
            <h4>Key Insight</h4>
            <p>When you have addition formulas in an equation, you often can:</p>
            <ol>
                <li>Expand the formula to get a single sine, cosine, or tangent</li>
                <li>Use algebraic techniques (factoring, substitution) to reduce to a standard form</li>
                <li>Solve the simpler equation</li>
            </ol>
        </div>
        """
    }
]
