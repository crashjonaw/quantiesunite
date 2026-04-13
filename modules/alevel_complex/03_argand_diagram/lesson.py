TITLE = "Argand Diagram and Modulus-Argument Form"

SECTIONS = [
    {
        "title": "The Argand Diagram (Complex Plane)",
        "body": """
<h3>Plotting Complex Numbers</h3>
<p>The <strong>Argand diagram</strong> (also called the <em>complex plane</em>) allows us to visualize complex numbers geometrically:</p>
<ul>
<li><strong>Horizontal axis (Re):</strong> Represents the real part a</li>
<li><strong>Vertical axis (Im):</strong> Represents the imaginary part b</li>
<li><strong>Point (a, b):</strong> Represents the complex number \(z = a + bi\)</li>
</ul>

<h3>Geometric Interpretation</h3>
<p>In the Argand diagram:</p>
<ul>
<li>The origin represents 0</li>
<li>The positive real axis represents positive real numbers</li>
<li>The positive imaginary axis represents positive imaginary numbers (points above the real axis)</li>
<li>|z| is the distance from the origin to the point z</li>
<li>Each complex number is uniquely determined by its position</li>
</ul>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Plotting complex numbers</p>
<p>Plot the following on the Argand diagram:</p>
<ul>
<li>\(z_1 = 2 + 3i\) is at position (2, 3)</li>
<li>\(z_2 = -1 + 2i\) is at position (-1, 2)</li>
<li>\(z_3 = 4 - i\) is at position (4, -1)</li>
<li>\(z_4 = -2 - 2i\) is at position (-2, -2)</li>
</ul>
</div>

<h3>Vector Addition in the Argand Diagram</h3>
<p>Addition of complex numbers corresponds to <em>vector addition</em> in the Argand diagram. The sum \(z_1 + z_2\) is obtained by the parallelogram law: place vectors for \(z_1\) and \(z_2\) tail-to-tail, and their sum is the diagonal of the resulting parallelogram.</p>

<div class="worked-example">
<p><strong>Example 2:</strong> Visualizing addition</p>
<p>If \(z_1 = 1 + i\) and \(z_2 = 2 + i\), then \(z_1 + z_2 = 3 + 2i\)</p>
<p>Geometrically, we move 1 unit right and 1 unit up (for \(z_1\)), then 2 more units right and 1 more unit up (for \(z_2\)), ending at (3, 2).</p>
</div>
"""
    },
    {
        "title": "Argument and Polar Form",
        "body": """
<h3>The Argument of a Complex Number</h3>
<p>For a non-zero complex number \(z = a + bi\), the <strong>argument</strong> is the angle \(\\theta\) measured counterclockwise from the positive real axis to the position vector of z:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">arg(z) = \(\\theta\), where \\(\\tan(\\theta) = \\frac{b}{a}\\)</p>
</div>

<p><strong>Important:</strong> The angle must be adjusted based on which quadrant z is in:</p>
<ul>
<li><strong>Q1:</strong> \(a > 0, b \\geq 0\): \(\\theta \in [0, \\pi/2)\)</li>
<li><strong>Q2:</strong> \(a \\leq 0, b > 0\): \(\\theta \in (\\pi/2, \\pi]\)</li>
<li><strong>Q3:</strong> \(a < 0, b \\leq 0\): \(\\theta \in (\\pi, 3\\pi/2)\) or \([-\\pi, -\\pi/2)\)</li>
<li><strong>Q4:</strong> \(a \\geq 0, b < 0\): \(\\theta \in (3\\pi/2, 2\\pi)\) or \([-\\pi/2, 0)\)</li>
</ul>

<p>The <strong>principal argument</strong> is typically chosen in the range \((-\\pi, \\pi]\).</p>

<h3>Polar Form of Complex Numbers</h3>
<p>A complex number can be written in <strong>polar form</strong> using its modulus \(r = |z|\) and argument \(\\theta\):</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\(z = r(\cos\\theta + i\sin\\theta) = r \\cdot \\text{cis}(\\theta) = re^{i\\theta}\)</p>
</div>

<p>where:</p>
<ul>
<li>\(r = |z| =\) \\(\\sqrt{a^2 + b^2}\\)</li>
<li>\\(\\cos(\\theta) = \\frac{a}{r}\\) and \\(\\sin(\\theta) = \\frac{b}{r}\\)</li>
</ul>

<h3>Converting Between Forms</h3>
<div class="worked-example">
<p><strong>Example 3:</strong> Rectangular to polar form</p>
<p>Express \(z = 1 + i\) in polar form</p>
<p>\(r = |1 + i| =\) \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\)</p>
<p>\\(\\tan(\\theta) = \\frac{1}{1} = 1\\), and z is in Q1, so \(\\theta = \\pi/4\)</p>
<p>Therefore: \(z =\) \\(\\sqrt{2} \\cdot \\text{cis}(\\pi/4) = \\sqrt{2} e^{i\\pi/4}\\)</p>
</div>

<div class="worked-example">
<p><strong>Example 4:</strong> Polar to rectangular form</p>
<p>Express \(w = 2 \\cdot \\text{cis}(2\\pi/3)\) in rectangular form</p>
<p>\\(\\cos(2\\pi/3) = -1/2\\) and \\(\\sin(2\\pi/3) = \\sqrt{3}/2\\)</p>
<p>\(w = 2(-1/2 + i \\cdot \\sqrt{3}/2) = -1 + i\\sqrt{3}\)</p>
</div>
"""
    },
    {
        "title": "Multiplication and Division in Polar Form",
        "body": """
<h3>Products and Quotients</h3>
<p>Polar form makes multiplication and division much simpler:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">If \(z_1 = r_1 \\cdot \\text{cis}(\\theta_1)\) and \(z_2 = r_2 \\cdot \\text{cis}(\\theta_2)\), then:</p>
<p style="text-align: center;">\(z_1 z_2 = r_1 r_2 \\cdot \\text{cis}(\\theta_1 + \\theta_2)\)</p>
<p style="text-align: center;">\(z_1/z_2 = (r_1/r_2) \\cdot \\text{cis}(\\theta_1 - \\theta_2)\)</p>
</div>

<p><strong>Interpretation:</strong> Multiplying complex numbers scales by \(r_1 r_2\) and rotates by angle \(\\theta_1 + \\theta_2\).</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 5:</strong> Multiplication in polar form</p>
<p>Multiply \(z_1 = 2 \\cdot \\text{cis}(\\pi/6)\) and \(z_2 = 3 \\cdot \\text{cis}(\\pi/3)\)</p>
<p>\(z_1 z_2 = (2)(3) \\cdot \\text{cis}(\\pi/6 + \\pi/3) = 6 \\cdot \\text{cis}(\\pi/2) = 6(\cos(\\pi/2) + i \\cdot \sin(\\pi/2)) = 6i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 6:</strong> Division in polar form</p>
<p>Divide \(z_1 = 8 \\cdot \\text{cis}(3\\pi/4)\) by \(z_2 = 2 \\cdot \\text{cis}(\\pi/4)\)</p>
<p>\(z_1/z_2 = (8/2) \\cdot \\text{cis}(3\\pi/4 - \\pi/4) = 4 \\cdot \\text{cis}(\\pi/2) = 4i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 7:</strong> Geometric significance of multiplication</p>
<p>To find \(i \\cdot (1 + i) = i + i^2 = -1 + i\):</p>
<p>In polar form: \(1 + i =\) \\(\\sqrt{2} \\cdot \\text{cis}(\\pi/4)\\) and \(i = \\text{cis}(\\pi/2)\)</p>
<p>Product = \\(\\sqrt{2} \\cdot 1 \\cdot \\text{cis}(\\pi/4 + \\pi/2) = \\sqrt{2} \\cdot \\text{cis}(3\\pi/4) = \\sqrt{2}(-\\frac{1}{\\sqrt{2}} + i\\frac{1}{\\sqrt{2}}) = -1 + i\\)</p>
<p>(This rotation by \(\\pi/2\) is the same as multiplication by i!)</p>
</div>
"""
    }
]
