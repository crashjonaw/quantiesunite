TITLE = "Trigonometric Identities and Relationships"

SECTIONS = [
    {
        "title": "What Are Identities and Why Do We Care?",
        "body": """
<h3>The Concept of an Identity</h3>
<p>An <strong>identity</strong> is an equation that is true for all values of the variable. For example, \\(2x = x + x\\) is an identity because it's true no matter what \\(x\\) is.</p>

<p>A <strong>trigonometric identity</strong> is an equation involving trigonometric functions that is true for all valid angle values.</p>

<h3>Why Identities Matter</h3>
<p>Trigonometric identities allow us to:</p>
<ul>
  <li><strong>Simplify complex expressions</strong> by replacing them with simpler equivalent forms</li>
  <li><strong>Solve equations</strong> that would otherwise be impossible</li>
  <li><strong>Prove relationships</strong> between different trigonometric functions</li>
  <li><strong>Calculate exact values</strong> for unusual angles</li>
</ul>

<p>Think of identities as different ways of writing the same mathematical truth.</p>

<h3>The Three Main Categories</h3>
<div class="concept-box">
<p><strong>Fundamental identities:</strong> The most basic relationships derived directly from definitions</p>
<p><strong>Sum and difference formulas:</strong> Express trig functions of sums and differences of angles</p>
<p><strong>Double angle formulas:</strong> Express trig functions of doubled angles</p>
</div>
"""
    },
    {
        "title": "Fundamental Identities: The Building Blocks",
        "body": """
<h3>The Pythagorean Identity: The Most Important One</h3>

<div class="concept-box">
<p>\\(\\sin^2(\\theta) + \\cos^2(\\theta) = 1\\)</p>
</div>

<h3>Where Does This Come From?</h3>
<p>Remember the unit circle! A point on the unit circle at angle \\(\\theta\\) has coordinates \\((\\cos(\\theta), \\sin(\\theta))\\). Since the circle has radius 1, the distance from the origin to any point on it is always 1.</p>

<p>By the Pythagorean theorem:</p>
<p>\\((\\cos(\\theta))^2 + (\\sin(\\theta))^2 = 1^2\\)</p>

<p>This identity is true for <strong>every</strong> angle \\(\\theta\\)—positive, negative, greater than 360°, radians, degrees—everything.</p>

<h3>Using the Pythagorean Identity to Find Missing Values</h3>

<div class="worked-example">
<p><strong>If \\(\\sin(\\theta) = \\frac{3}{5}\\) and \\(\\theta\\) is in Quadrant I, find \\(\\cos(\\theta)\\).</strong></p>

<p><strong>Step 1:</strong> Use the Pythagorean identity.</p>
<p>\\(\\sin^2(\\theta) + \\cos^2(\\theta) = 1\\)</p>

<p><strong>Step 2:</strong> Substitute \\(\\sin(\\theta) = \\frac{3}{5}\\).</p>
<p>\\(\\left(\\frac{3}{5}\\right)^2 + \\cos^2(\\theta) = 1\\)</p>
<p>\\(\\frac{9}{25} + \\cos^2(\\theta) = 1\\)</p>

<p><strong>Step 3:</strong> Solve for \\(\\cos^2(\\theta)\\).</p>
<p>\\(\\cos^2(\\theta) = 1 - \\frac{9}{25} = \\frac{16}{25}\\)</p>

<p><strong>Step 4:</strong> Take the square root.</p>
<p>\\(\\cos(\\theta) = \\pm\\frac{4}{5}\\)</p>

<p><strong>Step 5:</strong> Use the quadrant to determine the sign.</p>
<p>In Quadrant I, cosine is positive: \\(\\cos(\\theta) = \\frac{4}{5}\\)</p>
</div>

<h3>Other Fundamental Identities</h3>

<p><strong>Quotient identity:</strong></p>
<p>\\(\\tan(\\theta) = \\frac{\\sin(\\theta)}{\\cos(\\theta)}\\)</p>

<p><strong>Reciprocal identities:</strong></p>
<p>\\(\\csc(\\theta) = \\frac{1}{\\sin(\\theta)}, \\quad \\sec(\\theta) = \\frac{1}{\\cos(\\theta)}, \\quad \\cot(\\theta) = \\frac{1}{\\tan(\\theta)}\\)</p>

<h3>Why the Quotient Identity Works</h3>
<p>From the unit circle, \\(\\sin(\\theta)\\) is the y-coordinate and \\(\\cos(\\theta)\\) is the x-coordinate. In a right triangle context, \\(\\tan(\\theta) = \\frac{\\text{opposite}}{\\text{adjacent}}\\) is the ratio of the sides, which equals the ratio of coordinates.</p>
"""
    },
    {
        "title": "Sum, Difference, and Double Angle Formulas",
        "body": """
<h3>Sum and Difference Formulas</h3>
<p>These formulas tell us how to express \\(\\sin(A + B)\\) and \\(\\cos(A + B)\\) in terms of \\(A\\) and \\(B\\) separately.</p>

<div class="concept-box">
<p>\\(\\sin(A + B) = \\sin(A)\\cos(B) + \\cos(A)\\sin(B)\\)</p>
<p>\\(\\sin(A - B) = \\sin(A)\\cos(B) - \\cos(A)\\sin(B)\\)</p>
<p>\\(\\cos(A + B) = \\cos(A)\\cos(B) - \\sin(A)\\sin(B)\\)</p>
<p>\\(\\cos(A - B) = \\cos(A)\\cos(B) + \\sin(A)\\sin(B)\\)</p>
</div>

<h3>Why These Formulas Are Useful</h3>
<p>Many angles can be written as sums of familiar angles. For example, 75° = 45° + 30°. If you know the trig values of 45° and 30°, you can find the exact value of trig functions at 75°.</p>

<h3>Worked Example: Finding Exact Values</h3>

<div class="worked-example">
<p><strong>Find the exact value of \\(\\sin(75°)\\)</strong></p>

<p><strong>Step 1:</strong> Write 75° as a sum of familiar angles.</p>
<p>\\(75° = 45° + 30°\\)</p>

<p><strong>Step 2:</strong> Apply the sine addition formula.</p>
<p>\\(\\sin(75°) = \\sin(45° + 30°) = \\sin(45°)\\cos(30°) + \\cos(45°)\\sin(30°)\\)</p>

<p><strong>Step 3:</strong> Substitute known values.</p>
<p>\\(= \\frac{\\sqrt{2}}{2} \\cdot \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{2}}{2} \\cdot \\frac{1}{2}\\)</p>

<p><strong>Step 4:</strong> Simplify.</p>
<p>\\(= \\frac{\\sqrt{6}}{4} + \\frac{\\sqrt{2}}{4} = \\frac{\\sqrt{6} + \\sqrt{2}}{4}\\)</p>
</div>

<h3>Double Angle Formulas</h3>
<p>When \\(A = B\\), the sum formulas become double angle formulas:</p>

<div class="concept-box">
<p>\\(\\sin(2\\theta) = 2\\sin(\\theta)\\cos(\\theta)\\)</p>
<p>\\(\\cos(2\\theta) = \\cos^2(\\theta) - \\sin^2(\\theta)\\)</p>

<p><strong>Alternative forms for cosine double angle:</strong></p>
<p>\\(\\cos(2\\theta) = 2\\cos^2(\\theta) - 1\\)</p>
<p>\\(\\cos(2\\theta) = 1 - 2\\sin^2(\\theta)\\)</p>
</div>

<h3>Deriving the Double Angle Formulas</h3>

<div class="worked-example">
<p><strong>Start with:</strong> \\(\\sin(A + B) = \\sin(A)\\cos(B) + \\cos(A)\\sin(B)\\)</p>

<p><strong>Let \\(A = B = \\theta\\):</strong></p>
<p>\\(\\sin(\\theta + \\theta) = \\sin(\\theta)\\cos(\\theta) + \\cos(\\theta)\\sin(\\theta)\\)</p>

<p><strong>Simplify:</strong></p>
<p>\\(\\sin(2\\theta) = 2\\sin(\\theta)\\cos(\\theta)\\) ✓</p>
</div>

<h3>Worked Example: Using Double Angle Formulas</h3>

<div class="worked-example">
<p><strong>If \\(\\sin(\\theta) = \\frac{1}{3}\\) and \\(\\theta\\) is acute, find \\(\\sin(2\\theta)\\).</strong></p>

<p><strong>Step 1:</strong> Find \\(\\cos(\\theta)\\) using the Pythagorean identity.</p>
<p>\\(\\cos^2(\\theta) = 1 - \\sin^2(\\theta) = 1 - \\frac{1}{9} = \\frac{8}{9}\\)</p>
<p>\\(\\cos(\\theta) = \\frac{2\\sqrt{2}}{3}\\) (positive because acute)</p>

<p><strong>Step 2:</strong> Apply the double angle formula.</p>
<p>\\(\\sin(2\\theta) = 2\\sin(\\theta)\\cos(\\theta) = 2 \\cdot \\frac{1}{3} \\cdot \\frac{2\\sqrt{2}}{3} = \\frac{4\\sqrt{2}}{9}\\)</p>
</div>
"""
    },
    {
        "title": "Proving Identities: The Art and Strategy",
        "body": """
<h3>What Does "Proving" an Identity Mean?</h3>
<p>To prove an identity, you must show that the left side can be algebraically transformed into the right side (or vice versa). You cannot assume they're equal and work backwards—that's circular reasoning.</p>

<h3>General Strategy</h3>
<ul>
  <li><strong>Pick the more complicated side</strong> and try to simplify it to look like the other side</li>
  <li><strong>Look for opportunities to use fundamental identities</strong> (especially the Pythagorean identity)</li>
  <li><strong>Factor and combine fractions</strong> when you see polynomials in trig functions</li>
  <li><strong>Don't be afraid to take detours</strong>—sometimes you need to go roundabout to get where you need</li>
</ul>

<h3>Worked Example: A Step-by-Step Proof</h3>

<div class="worked-example">
<p><strong>Prove: \\(\\tan(\\theta)\\sin(\\theta) + \\cos(\\theta) = \\sec(\\theta)\\)</strong></p>

<p><strong>Step 1:</strong> Convert \\(\\tan(\\theta)\\) to sine and cosine.</p>
<p>LHS \\(= \\frac{\\sin(\\theta)}{\\cos(\\theta)} \\cdot \\sin(\\theta) + \\cos(\\theta)\\)</p>

<p><strong>Step 2:</strong> Simplify the first term.</p>
<p>\\(= \\frac{\\sin^2(\\theta)}{\\cos(\\theta)} + \\cos(\\theta)\\)</p>

<p><strong>Step 3:</strong> Combine into a single fraction.</p>
<p>\\(= \\frac{\\sin^2(\\theta)}{\\cos(\\theta)} + \\frac{\\cos^2(\\theta)}{\\cos(\\theta)}\\)</p>
<p>\\(= \\frac{\\sin^2(\\theta) + \\cos^2(\\theta)}{\\cos(\\theta)}\\)</p>

<p><strong>Step 4:</strong> Apply the Pythagorean identity.</p>
<p>\\(= \\frac{1}{\\cos(\\theta)}\\)</p>

<p><strong>Step 5:</strong> Recognize this as the reciprocal identity for secant.</p>
<p>\\(= \\sec(\\theta)\\) = RHS ✓</p>
</div>

<h3>Worked Example: Proving a Less Obvious Identity</h3>

<div class="worked-example">
<p><strong>Prove: \\(\\frac{1 + \\cos(\\theta)}{\\sin(\\theta)} = \\frac{\\sin(\\theta)}{1 - \\cos(\\theta)}\\)</strong></p>

<p><strong>Strategy:</strong> Cross-multiply (or use the conjugate trick).</p>

<p><strong>Step 1:</strong> Multiply the left side by \\(\\frac{1 - \\cos(\\theta)}{1 - \\cos(\\theta)}\\).</p>
<p>\\(\\frac{1 + \\cos(\\theta)}{\\sin(\\theta)} \\cdot \\frac{1 - \\cos(\\theta)}{1 - \\cos(\\theta)} = \\frac{(1 + \\cos(\\theta))(1 - \\cos(\\theta))}{\\sin(\\theta)(1 - \\cos(\\theta))}\\)</p>

<p><strong>Step 2:</strong> Use the difference of squares: \\((a + b)(a - b) = a^2 - b^2\\)</p>
<p>\\(= \\frac{1 - \\cos^2(\\theta)}{\\sin(\\theta)(1 - \\cos(\\theta))}\\)</p>

<p><strong>Step 3:</strong> Apply the Pythagorean identity: \\(\\sin^2(\\theta) + \\cos^2(\\theta) = 1\\), so \\(1 - \\cos^2(\\theta) = \\sin^2(\\theta)\\)</p>
<p>\\(= \\frac{\\sin^2(\\theta)}{\\sin(\\theta)(1 - \\cos(\\theta))}\\)</p>

<p><strong>Step 4:</strong> Cancel \\(\\sin(\\theta)\\).</p>
<p>\\(= \\frac{\\sin(\\theta)}{1 - \\cos(\\theta)}\\) = RHS ✓</p>
</div>

<h3>Common Pitfalls to Avoid</h3>

<div class="warning-box">
<p><strong>Don't:</strong> Assume both sides are equal from the start and manipulate both sides simultaneously</p>
<p><strong>Do:</strong> Work with one side (usually the more complex) until it becomes the other side</p>

<p><strong>Don't:</strong> Use inverse trig functions or take square roots without careful consideration of signs</p>
<p><strong>Do:</strong> Work algebraically with the functions themselves</p>

<p><strong>Don't:</strong> Forget special angle values can help you check if an identity is true before you prove it</p>
<p><strong>Do:</strong> Substitute a specific angle (like 30° or 45°) to verify your identity makes sense</p>
</div>
"""
    }
]
