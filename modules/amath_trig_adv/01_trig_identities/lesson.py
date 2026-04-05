TITLE = "Trigonometric Identities"

SECTIONS = [
    {
        "title": "Fundamental Identities",
        "body": """
        <div class="concept-box">
            <h3>Key Identities</h3>
            <p>These foundational identities form the basis for all trigonometric manipulation.</p>
        </div>

        <h4>Pythagorean Identity</h4>
        <p>The most fundamental relationship between sine and cosine:</p>
        <div class="formula">$$\\sin^2 \\theta + \\cos^2 \\theta = 1$$</div>
        <p>This comes directly from the Pythagorean theorem applied to the unit circle.</p>

        <h4>Quotient Identity</h4>
        <div class="formula">$$\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$$</div>

        <h4>Reciprocal Identities</h4>
        <ul>
            <li>$$\\csc \\theta = \\frac{1}{\\sin \\theta}$$</li>
            <li>$$\\sec \\theta = \\frac{1}{\\cos \\theta}$$</li>
            <li>$$\\cot \\theta = \\frac{1}{\\tan \\theta} = \\frac{\\cos \\theta}{\\sin \\theta}$$</li>
        </ul>
        """
    },
    {
        "title": "Double Angle Formulas",
        "body": """
        <div class="concept-box">
            <h3>Expressing sin(2θ), cos(2θ), tan(2θ)</h3>
        </div>

        <h4>Double Angle Formulas</h4>
        <p>These express trigonometric functions of twice an angle in terms of the original angle:</p>
        <div class="formula">$$\\sin(2\\theta) = 2\\sin \\theta \\cos \\theta$$</div>
        <div class="formula">$$\\cos(2\\theta) = \\cos^2 \\theta - \\sin^2 \\theta = 2\\cos^2 \\theta - 1 = 1 - 2\\sin^2 \\theta$$</div>
        <div class="formula">$$\\tan(2\\theta) = \\frac{2\\tan \\theta}{1 - \\tan^2 \\theta}$$</div>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> If \\(\\sin \\theta = \\frac{3}{5}\\) and \\(\\theta\\) is acute, find \\(\\sin(2\\theta)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>First find \\(\\cos \\theta\\) using \\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\):</li>
                <li>$$\\left(\\frac{3}{5}\\right)^2 + \\cos^2 \\theta = 1$$</li>
                <li>$$\\cos^2 \\theta = 1 - \\frac{9}{25} = \\frac{16}{25}$$</li>
                <li>$$\\cos \\theta = \\frac{4}{5}$$ (positive since \\(\\theta\\) is acute)</li>
                <li>Now apply the double angle formula:</li>
                <li>$$\\sin(2\\theta) = 2 \\sin \\theta \\cos \\theta = 2 \\cdot \\frac{3}{5} \\cdot \\frac{4}{5} = \\frac{24}{25}$$</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Using Identities to Solve Equations",
        "body": """
        <div class="concept-box">
            <h3>Strategy: Simplify Using Identities, Then Solve</h3>
        </div>

        <p>When solving trigonometric equations, the key is to use identities to express everything in terms of a single trigonometric function.</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Solve \\(\\sin(2\\theta) = \\sin \\theta\\) for \\(0° \\leq \\theta \\leq 360°\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Replace \\(\\sin(2\\theta)\\) using the double angle formula:</li>
                <li>$$2\\sin \\theta \\cos \\theta = \\sin \\theta$$</li>
                <li>Rearrange:</li>
                <li>$$2\\sin \\theta \\cos \\theta - \\sin \\theta = 0$$</li>
                <li>Factor out \\(\\sin \\theta\\):</li>
                <li>$$\\sin \\theta (2\\cos \\theta - 1) = 0$$</li>
                <li>Set each factor to zero:</li>
                <li>$$\\sin \\theta = 0 \\text{ or } 2\\cos \\theta - 1 = 0$$</li>
                <li>$$\\sin \\theta = 0 \\text{ or } \\cos \\theta = \\frac{1}{2}$$</li>
                <li>From \\(\\sin \\theta = 0\\): \\(\\theta = 0°, 180°, 360°\\)</li>
                <li>From \\(\\cos \\theta = \\frac{1}{2}\\): \\(\\theta = 60°, 300°\\)</li>
                <li><strong>Solutions:</strong> \\(\\theta = 0°, 60°, 180°, 300°, 360°\\)</li>
            </ol>
        </div>

        <div class="warning-box">
            <h4>Important</h4>
            <p>When factoring equations like this, be careful not to divide both sides by a variable expression (like \\(\\sin \\theta\\)), as you may lose solutions. Instead, factor and set each factor equal to zero.</p>
        </div>
        """
    }
]
