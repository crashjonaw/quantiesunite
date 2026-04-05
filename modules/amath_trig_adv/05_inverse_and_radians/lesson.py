TITLE = "Inverse Trigonometric Functions and Radians"

SECTIONS = [
    {
        "title": "Inverse Trigonometric Functions",
        "body": """
        <div class="concept-box">
            <h3>Notation, Domains, and Ranges</h3>
            <p>The inverse trigonometric functions allow us to find angles given trigonometric values.</p>
        </div>

        <h4>Definition and Notation</h4>
        <p>If \\(\\sin \\theta = x\\), then \\(\\theta = \\sin^{-1}(x)\\) or \\(\\theta = \\arcsin(x)\\)</p>

        <p><strong>Domains and Ranges:</strong></p>
        <ul>
            <li>$$\\sin^{-1}(x) \\text{ or } \\arcsin(x): \\text{ Domain } [-1, 1], \\text{ Range } \\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right] \\text{ or } [-90°, 90°]$$</li>
            <li>$$\\cos^{-1}(x) \\text{ or } \\arccos(x): \\text{ Domain } [-1, 1], \\text{ Range } [0, \\pi] \\text{ or } [0°, 180°]$$</li>
            <li>$$\\tan^{-1}(x) \\text{ or } \\arctan(x): \\text{ Domain } \\mathbb{R}, \\text{ Range } \\left(-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right) \\text{ or } (-90°, 90°)$$</li>
        </ul>

        <p><strong>Note:</strong> These ranges are restricted to make the functions one-to-one (invertible).</p>

        <div class="worked-example">
            <h4>Worked Example</h4>
            <p><strong>Problem:</strong> Find \\(\\sin^{-1}\\left(\\frac{1}{2}\\right)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>We need the angle in \\([-90°, 90°]\\) whose sine is \\(\\frac{1}{2}\\)</li>
                <li>We know \\(\\sin(30°) = \\frac{1}{2}\\)</li>
                <li>Since \\(30° \\in [-90°, 90°]\\), we have \\(\\sin^{-1}\\left(\\frac{1}{2}\\right) = 30°\\) or \\(\\frac{\\pi}{6}\\) radians</li>
            </ol>
        </div>

        <h4>Key Properties</h4>
        <ul>
            <li>$$\\sin(\\sin^{-1}(x)) = x \\text{ for } x \\in [-1, 1]$$</li>
            <li>$$\\sin^{-1}(\\sin \\theta) = \\theta \\text{ only if } \\theta \\in \\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]$$</li>
            <li>$$\\sin^{-1}(x) + \\cos^{-1}(x) = \\frac{\\pi}{2} \\text{ (for } 0 \\leq x \\leq 1\\text{)}$$</li>
        </ul>
        """
    },
    {
        "title": "Solving with Inverse Trigonometric Functions",
        "body": """
        <div class="concept-box">
            <h3>Using Inverse Functions to Solve Equations</h3>
        </div>

        <p>Inverse trigonometric functions are essential for solving equations where the angle is not a standard value.</p>

        <div class="worked-example">
            <h4>Worked Example: Solving with Inverse Functions</h4>
            <p><strong>Problem:</strong> Solve \\(\\sin^{-1}(x) = \\frac{\\pi}{4}\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Apply \\(\\sin\\) to both sides:</li>
                <li>$$\\sin(\\sin^{-1}(x)) = \\sin\\left(\\frac{\\pi}{4}\\right)$$</li>
                <li>$$x = \\frac{\\sqrt{2}}{2}$$</li>
            </ol>
        </div>

        <h4>Important Considerations</h4>
        <p>When solving equations involving inverse trig functions:</p>
        <ul>
            <li>Always remember the restricted ranges of inverse functions</li>
            <li>A given \\(y\\)-value corresponds to <strong>multiple</strong> angles in the full range, but only <strong>one</strong> in the restricted range</li>
            <li>To find all solutions in a given range, use the inverse function to find one solution, then use symmetry properties to find others</li>
        </ul>

        <div class="worked-example">
            <h4>Worked Example: All Solutions in a Range</h4>
            <p><strong>Problem:</strong> Find all solutions to \\(\\sin x = 0.3\\) in \\([0, 2\\pi)\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Use the inverse function to find the principal value:</li>
                <li>$$x_1 = \\sin^{-1}(0.3) \\approx 0.305 \\text{ radians}$$</li>
                <li>The sine function is positive in the first and second quadrants</li>
                <li>In the second quadrant: \\(x_2 = \\pi - x_1 \\approx \\pi - 0.305 \\approx 2.837 \\text{ radians}\\)</li>
                <li><strong>Solutions:</strong> \\(x \\approx 0.305, 2.837\\)</li>
            </ol>
        </div>
        """
    },
    {
        "title": "Radians and Trigonometric Equations",
        "body": """
        <div class="concept-box">
            <h3>Working with Radians</h3>
            <p>Radians are the natural unit for trigonometry and calculus. One radian is the angle subtended by an arc equal in length to the radius of the circle.</p>
        </div>

        <h4>Degree-Radian Conversion</h4>
        <div class="formula">$$\\theta_{\\text{radians}} = \\theta_{\\text{degrees}} \\times \\frac{\\pi}{180}$$</div>
        <div class="formula">$$\\theta_{\\text{degrees}} = \\theta_{\\text{radians}} \\times \\frac{180}{\\pi}$$</div>

        <h4>Common Angles in Radians</h4>
        <ul>
            <li>\\(30° = \\frac{\\pi}{6}\\), \\(45° = \\frac{\\pi}{4}\\), \\(60° = \\frac{\\pi}{3}\\), \\(90° = \\frac{\\pi}{2}\\)</li>
            <li>\\(180° = \\pi\\), \\(270° = \\frac{3\\pi}{2}\\), \\(360° = 2\\pi\\)</li>
        </ul>

        <h4>Periodicity in Radians</h4>
        <p>Trigonometric functions have period \\(2\\pi\\) (in radians) or \\(360°\\) (in degrees):</p>
        <ul>
            <li>\\(\\sin(x) = \\sin(x + 2\\pi n)\\) for any integer \\(n\\)</li>
            <li>\\(\\cos(x) = \\cos(x + 2\\pi n)\\) for any integer \\(n\\)</li>
            <li>\\(\\tan(x) = \\tan(x + \\pi n)\\) for any integer \\(n\\)</li>
        </ul>

        <div class="worked-example">
            <h4>Worked Example: Solving in Radians</h4>
            <p><strong>Problem:</strong> Solve \\(\\sin(2\\theta) = \\frac{1}{2}\\) for \\(0 \\leq \\theta < 2\\pi\\).</p>
            <p><strong>Solution:</strong></p>
            <ol>
                <li>Find where \\(\\sin(2\\theta) = \\frac{1}{2}\\):</li>
                <li>$$2\\theta = \\frac{\\pi}{6} \\text{ or } 2\\theta = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}$$</li>
                <li>Within \\([0, 4\\pi)\\) for \\(2\\theta\\):</li>
                <li>$$2\\theta = \\frac{\\pi}{6}, \\frac{5\\pi}{6}, \\frac{\\pi}{6} + 2\\pi, \\frac{5\\pi}{6} + 2\\pi$$</li>
                <li>$$2\\theta = \\frac{\\pi}{6}, \\frac{5\\pi}{6}, \\frac{13\\pi}{6}, \\frac{17\\pi}{6}$$</li>
                <li>Divide by 2:</li>
                <li>$$\\theta = \\frac{\\pi}{12}, \\frac{5\\pi}{12}, \\frac{13\\pi}{12}, \\frac{17\\pi}{12}$$</li>
            </ol>
        </div>

        <h4>General Solutions in Radians</h4>
        <p>For the full set of solutions (all real numbers):</p>
        <ul>
            <li>$$\\sin(x) = k: x = \\sin^{-1}(k) + 2\\pi n \\text{ or } x = \\pi - \\sin^{-1}(k) + 2\\pi n \\text{ (for } n \\in \\mathbb{Z}\\text{)}$$</li>
            <li>$$\\cos(x) = k: x = \\pm\\cos^{-1}(k) + 2\\pi n \\text{ (for } n \\in \\mathbb{Z}\\text{)}$$</li>
            <li>$$\\tan(x) = k: x = \\tan^{-1}(k) + \\pi n \\text{ (for } n \\in \\mathbb{Z}\\text{)}$$</li>
        </ul>
        """
    }
]
