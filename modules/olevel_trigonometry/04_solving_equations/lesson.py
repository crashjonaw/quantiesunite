TITLE = "Solving Trigonometric Equations"

SECTIONS = [
    {
        "title": "What Are Trigonometric Equations and Why Solve Them?",
        "body": """
<h3>Equations vs Identities</h3>
<p>An <strong>identity</strong> is true for all values of the variable. An <strong>equation</strong> is true only for specific values.</p>

<p>For example:</p>
<ul>
  <li>\\(\\sin^2(\\theta) + \\cos^2(\\theta) = 1\\) is an identity (always true)</li>
  <li>\\(\\sin(\\theta) = 0.5\\) is an equation (true only when \\(\\theta = 30°\\) or \\(150°\\) or...)</li>
</ul>

<h3>Why Solve Them?</h3>
<p>In real-world applications, you often know a relationship (equation) and need to find the angle. For example:</p>
<ul>
  <li><strong>Engineering:</strong> "At what angle must a ramp be tilted so that an object slides at constant velocity?" leads to an equation to solve</li>
  <li><strong>Physics:</strong> "When is a vibrating object at maximum displacement?" requires solving a trig equation</li>
  <li><strong>Navigation:</strong> "What bearing achieves a specific course?" involves trig equations</li>
</ul>

<h3>The Challenge</h3>
<p>Unlike algebraic equations, trigonometric equations often have infinite solutions. For example, \\(\\sin(\\theta) = 0.5\\) is true at \\(30°\\), \\(150°\\), \\(390°\\), \\(510°\\), etc.</p>

<p>We solve by finding solutions in a specified interval (like \\([0°, 360°)\\) or \\([0, 2\\pi)\\)), then use periodicity to write the general solution.</p>
"""
    },
    {
        "title": "General Approach: Strategy and Process",
        "body": """
<h3>The Four-Step Process</h3>

<div class="concept-box">
<p><strong>Step 1: Simplify</strong> Use identities to rewrite the equation in terms of a single trig function</p>
<p><strong>Step 2: Solve the algebraic equation</strong> Treat it like a normal equation (quadratic, linear, etc.)</p>
<p><strong>Step 3: Solve for the angle</strong> Use inverse trig functions to find angle values in the given interval</p>
<p><strong>Step 4: Write the general solution</strong> Account for periodicity (angles differing by 360° or 2π)</p>
</div>

<h3>Worked Example: Simple Case</h3>

<div class="worked-example">
<p><strong>Solve \\(2\\sin(\\theta) - 1 = 0\\) for \\(\\theta \\in [0°, 360°)\\)</strong></p>

<p><strong>Step 1: Simplify (algebra)</strong></p>
<p>\\(2\\sin(\\theta) = 1\\)</p>
<p>\\(\\sin(\\theta) = 0.5\\)</p>

<p><strong>Step 2: Find the reference angle</strong></p>
<p>\\(\\sin^{-1}(0.5) = 30°\\)</p>

<p><strong>Step 3: Find all solutions in the interval using the ASTC rule</strong></p>
<p>Sine is positive in Quadrants I and II:</p>
<ul>
  <li>Quadrant I: \\(\\theta = 30°\\)</li>
  <li>Quadrant II: \\(\\theta = 180° - 30° = 150°\\)</li>
</ul>

<p><strong>Answer:</strong> \\(\\theta = 30°\\) or \\(150°\\)</p>
</div>

<h3>Worked Example: Using Identities First</h3>

<div class="worked-example">
<p><strong>Solve \\(\\sin(2\\theta) = \\sin(\\theta)\\) for \\(\\theta \\in [0, 2\\pi)\\)</strong></p>

<p><strong>Step 1: Use the double angle identity</strong></p>
<p>\\(2\\sin(\\theta)\\cos(\\theta) = \\sin(\\theta)\\)</p>

<p><strong>Step 2: Move everything to one side</strong></p>
<p>\\(2\\sin(\\theta)\\cos(\\theta) - \\sin(\\theta) = 0\\)</p>

<p><strong>Step 3: Factor</strong></p>
<p>\\(\\sin(\\theta)(2\\cos(\\theta) - 1) = 0\\)</p>

<p><strong>Step 4: Apply the zero product property</strong></p>
<p>Either \\(\\sin(\\theta) = 0\\) or \\(2\\cos(\\theta) - 1 = 0\\)</p>

<p><strong>Step 5: Solve each equation</strong></p>

<p>From \\(\\sin(\\theta) = 0\\): \\(\\theta = 0, \\pi\\)</p>

<p>From \\(\\cos(\\theta) = \\frac{1}{2}\\): \\(\\theta = \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\)</p>

<p><strong>Answer:</strong> \\(\\theta = 0, \\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\)</p>
</div>
"""
    },
    {
        "title": "Solving Quadratic Trig Equations",
        "body": """
<h3>When You Get a Quadratic</h3>
<p>Some equations reduce to quadratic form in a trig function. For example:</p>

<p>\\(2\\sin^2(\\theta) - 3\\sin(\\theta) + 1 = 0\\)</p>

<p>This is quadratic in \\(\\sin(\\theta)\\). Let \\(u = \\sin(\\theta)\\):</p>

<p>\\(2u^2 - 3u + 1 = 0\\)</p>

<h3>Approach: Substitution Method</h3>

<div class="worked-example">
<p><strong>Solve \\(2\\sin^2(\\theta) - 3\\sin(\\theta) + 1 = 0\\) for \\(\\theta \\in [0°, 360°)\\)</strong></p>

<p><strong>Step 1: Let \\(u = \\sin(\\theta)\\) and solve the quadratic</strong></p>
<p>\\(2u^2 - 3u + 1 = 0\\)</p>

<p><strong>Step 2: Factor (or use the quadratic formula)</strong></p>
<p>\\((2u - 1)(u - 1) = 0\\)</p>

<p><strong>Step 3: Solve for \\(u\\)</strong></p>
<p>\\(u = \\frac{1}{2}\\) or \\(u = 1\\)</p>

<p><strong>Step 4: Substitute back \\(\\sin(\\theta)\\) and solve</strong></p>

<p><strong>Case 1:</strong> \\(\\sin(\\theta) = \\frac{1}{2}\\)</p>
<p>\\(\\theta = 30°\\) or \\(150°\\)</p>

<p><strong>Case 2:</strong> \\(\\sin(\\theta) = 1\\)</p>
<p>\\(\\theta = 90°\\)</p>

<p><strong>Answer:</strong> \\(\\theta = 30°, 90°, 150°\\)</p>
</div>

<h3>Important Caution: Invalid Solutions</h3>

<div class="warning-box">
<p>Sometimes a quadratic solution gives a value outside the valid range. For example, if solving \\(\\sin(\\theta) = k\\), remember that \\(|k| \\leq 1\\).</p>

<p>If you get \\(\\sin(\\theta) = 2\\) from a quadratic, that's impossible, so discard that solution.</p>
</div>

<h3>Worked Example: Recognizing Invalid Solutions</h3>

<div class="worked-example">
<p><strong>Solve \\(\\cos^2(\\theta) + \\cos(\\theta) - 2 = 0\\) for \\(\\theta \\in [0, 2\\pi)\\)</strong></p>

<p><strong>Step 1: Let \\(u = \\cos(\\theta)\\)</strong></p>
<p>\\(u^2 + u - 2 = 0\\)</p>

<p><strong>Step 2: Factor</strong></p>
<p>\\((u + 2)(u - 1) = 0\\)</p>

<p><strong>Step 3: Solve for \\(u\\)</strong></p>
<p>\\(u = -2\\) or \\(u = 1\\)</p>

<p><strong>Step 4: Check validity and solve</strong></p>

<p>\\(u = -2\\) is impossible because \\(|\\cos(\\theta)| \\leq 1\\). Discard.</p>

<p>\\(u = 1\\) gives \\(\\cos(\\theta) = 1\\), so \\(\\theta = 0\\)</p>

<p><strong>Answer:</strong> \\(\\theta = 0\\)</p>
</div>
"""
    },
    {
        "title": "General Solutions and Periodicity",
        "body": """
<h3>From Specific Solutions to General Solutions</h3>
<p>So far, we've found all solutions in a specific interval like \\([0°, 360°)\\). To write the <strong>general solution</strong> that accounts for all possible angles, we use periodicity.</p>

<h3>Periodicity of Trigonometric Functions</h3>

<div class="concept-box">
<p>\\(\\sin(\\theta + 360°) = \\sin(\\theta)\\) (or \\(\\sin(\\theta + 2\\pi) = \\sin(\\theta)\\))</p>
<p>\\(\\cos(\\theta + 360°) = \\cos(\\theta)\\) (or \\(\\cos(\\theta + 2\\pi) = \\cos(\\theta)\\))</p>
<p>\\(\\tan(\\theta + 180°) = \\tan(\\theta)\\) (or \\(\\tan(\\theta + \\pi) = \\tan(\\theta)\\))</p>
</div>

<p><strong>Key point:</strong> Sine and cosine repeat every 360° (or \\(2\\pi\\) radians). Tangent repeats every 180° (or \\(\\pi\\) radians).</p>

<h3>Writing General Solutions</h3>

<div class="concept-box">
<p><strong>For sine equations:</strong></p>
<p>If \\(\\sin(\\theta) = a\\) and one solution is \\(\\theta_0\\), then:</p>
<p>\\(\\theta = \\theta_0 + 360°k\\) or \\(\\theta = 180° - \\theta_0 + 360°k\\), where \\(k\\) is any integer</p>

<p><strong>For cosine equations:</strong></p>
<p>If \\(\\cos(\\theta) = a\\) and one solution is \\(\\theta_0\\), then:</p>
<p>\\(\\theta = \\pm\\theta_0 + 360°k\\), where \\(k\\) is any integer</p>

<p><strong>For tangent equations:</strong></p>
<p>If \\(\\tan(\\theta) = a\\) and one solution is \\(\\theta_0\\), then:</p>
<p>\\(\\theta = \\theta_0 + 180°k\\), where \\(k\\) is any integer</p>
</div>

<h3>Worked Example: General Solution from Specific Solutions</h3>

<div class="worked-example">
<p><strong>Find the general solution for \\(\\sin(\\theta) = 0.5\\)</strong></p>

<p><strong>Step 1: Find solutions in \\([0°, 360°)\\)</strong></p>
<p>\\(\\theta = 30°\\) or \\(\\theta = 150°\\)</p>

<p><strong>Step 2: Write the general solution</strong></p>
<p>For \\(\\theta = 30°\\): Add multiples of 360°</p>
<p>\\(\\theta = 30° + 360°k\\)</p>

<p>For \\(\\theta = 150°\\): Also add multiples of 360°</p>
<p>\\(\\theta = 150° + 360°k\\)</p>

<p>Alternatively, using the complementary angle:</p>
<p>\\(\\theta = 30° + 360°k\\) or \\(\\theta = (180° - 30°) + 360°k = 150° + 360°k\\)</p>

<p><strong>Combined form:</strong></p>
<p>\\(\\theta = 30° + 360°k\\) or \\(180° - 30° + 360°k\\), where \\(k \\in \\mathbb{Z}\\)</p>
</div>

<h3>Verification: Why Periodicity Works</h3>

<div class="worked-example">
<p><strong>Verify:</strong> If \\(\\sin(30°) = 0.5\\), then \\(\\sin(30° + 360°) = \\sin(390°) = 0.5\\)</p>

<p>\\(390° = 360° + 30°\\), so by the periodicity property:</p>
<p>\\(\\sin(390°) = \\sin(30°) = 0.5\\) ✓</p>
</div>
"""
    }
]
