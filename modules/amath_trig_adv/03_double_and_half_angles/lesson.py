TITLE = "Double and Half Angle Formulae"

SECTIONS = [
    {
        "title": "Double Angle Formulas (Comprehensive)",
        "body": """
        <div class="concept-box">
            <h3>Expressing Trigonometric Functions of 2θ</h3>
            <p>Double angle formulas are special cases of the addition formulas when we set \\(A = B = \\theta\\).</p>
        </div>

        <h4>Double Angle Formulas</h4>
        <div class="formula">$$\\sin(2\\theta) = 2\\sin \\theta \\cos \\theta$$</div>
        <div class="formula">$$\\cos(2\\theta) = \\cos^2 \\theta - \\sin^2 \\theta$$</div>

        <p><strong>Alternative forms for cosine double angle:</strong></p>
        <div class="formula">$$\\cos(2\\theta) = 2\\cos^2 \\theta - 1$$</div>
        <div class="formula">$$\\cos(2\\theta) = 1 - 2\\sin^2 \\theta$$</div>

        <p>These alternative forms are useful when you have a quadratic in \\(\\sin^2 \\theta\\) or \\(\\cos^2 \\theta\\).</p>

        <div class="formula">$$\\tan(2\\theta) = \\frac{2\\tan \\theta}{1 - \\tan^2 \\theta}$$</div>

        <div class="worked-example">
            <h4>Worked Example: Using cos(2θ) = 2cos²θ - 1</h4>
            <p><strong>Problem:</strong> Solve \\(2\\cos^2 \\theta - 1 = 0\\) for \\(0° \\leq \\theta < 360°\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Recognize this is \\(\\cos(2\\theta) = 0\\)</li>
                <li>The general solution for \\(\\cos(2\\theta) = 0\\) is \\(2\\theta = 90°, 270°, 450°, ...\\)</li>
                <li>In the range \\([0°, 360°)\\) for \\(2\\theta\\): \\(2\\theta = 90°, 270°\\)</li>
                <li>Divide by 2: \\(\\theta = 45°, 135°\\)</li>
                <li>But we need \\(\\theta \\in [0°, 360°)\\), so all solutions for \\(2\\theta \\in [0°, 720°)\\) are: \\(2\\theta = 90°, 270°, 450°, 630°\\)</li>
                <li>Therefore: \\(\\theta = 45°, 135°, 225°, 315°\\)</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Half Angle Formulas",
        "body": """
        <h4>Half Angle Formulas</h4>
        <p>We can derive formulas for \\(\\sin(\\theta/2)\\), \\(\\cos(\\theta/2)\\), and \\(\\tan(\\theta/2)\\) from the double angle formulas by rearranging.</p>

        <p>Starting with \\(\\cos(2\\theta) = 1 - 2\\sin^2 \\theta\\), let \\(\\alpha = \\theta/2\\):</p>
        <div class="formula">$$\\sin^2 \\left(\\frac{\\alpha}{2}\\right) = \\frac{1 - \\cos \\alpha}{2}$$</div>
        <div class="formula">$$\\cos^2 \\left(\\frac{\\alpha}{2}\\right) = \\frac{1 + \\cos \\alpha}{2}$$</div>

        <p>Taking square roots:</p>
        <div class="formula">$$\\sin \\left(\\frac{\\alpha}{2}\\right) = \\pm\\sqrt{\\frac{1 - \\cos \\alpha}{2}}$$</div>
        <div class="formula">$$\\cos \\left(\\frac{\\alpha}{2}\\right) = \\pm\\sqrt{\\frac{1 + \\cos \\alpha}{2}}$$</div>

        <p><strong>For tangent:</strong></p>
        <div class="formula">$$\\tan \\left(\\frac{\\alpha}{2}\\right) = \\pm\\sqrt{\\frac{1 - \\cos \\alpha}{1 + \\cos \\alpha}} = \\frac{\\sin \\alpha}{1 + \\cos \\alpha} = \\frac{1 - \\cos \\alpha}{\\sin \\alpha}$$</div>

        <p><strong>Note:</strong> The ± sign depends on which quadrant \\(\\alpha/2\\) lies in. The last two forms for tangent don't require the ± sign.</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Find the exact value of \\(\\sin(22.5°)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Note that \\(22.5° = 45°/2\\)</li>
                <li>Use the half-angle formula with \\(\\alpha = 45°\\):</li>
                <li>$$\\sin(22.5°) = \\sqrt{\\frac{1 - \\cos(45°)}{2}}$$ (positive since \\(22.5°\\) is in the first quadrant)</li>
                <li>$$= \\sqrt{\\frac{1 - \\frac{\\sqrt{2}}{2}}{2}}$$</li>
                <li>$$= \\sqrt{\\frac{2 - \\sqrt{2}}{4}}$$</li>
                <li>$$= \\frac{\\sqrt{2 - \\sqrt{2}}}{2}$$</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Problem Solving with Double and Half Angles",
        "body": """
        <div class="concept-box">
            <h3>Strategy for Equation Solving</h3>
        </div>

        <p>When you encounter equations with multiple angles like \\(\\theta, 2\\theta,\\) or \\(\\theta/2\\), use these formulas to express everything in terms of a single angle.</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Solve \\(\\sin(2\\theta) = \\sin \\theta\\) for \\(0° \\leq \\theta \\leq 360°\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Replace \\(\\sin(2\\theta)\\) with the double angle formula:</li>
                <li>$$2\\sin \\theta \\cos \\theta = \\sin \\theta$$</li>
                <li>Rearrange:</li>
                <li>$$2\\sin \\theta \\cos \\theta - \\sin \\theta = 0$$</li>
                <li>Factor:</li>
                <li>$$\\sin \\theta(2\\cos \\theta - 1) = 0$$</li>
                <li>Set each factor to zero:</li>
                <li>$$\\sin \\theta = 0 \\Rightarrow \\theta = 0°, 180°, 360°$$</li>
                <li>$$\\cos \\theta = \\frac{1}{2} \\Rightarrow \\theta = 60°, 300°$$</li>
                <li><strong>Solutions:</strong> \\(\\theta = 0°, 60°, 180°, 300°, 360°\\)</li>
            </ol>
        </div>

        <div class="success-box">
            <h4>Key Strategy</h4>
            <p>The goal is always to reduce your equation to involve only a single trigonometric function (like \\(\\sin \\theta\\)) or a single angle.</p>
        </div>
        """
    }
]
