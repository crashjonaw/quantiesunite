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
<li><strong>Point (a, b):</strong> Represents the complex number z = a + bi</li>
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
<li>z₁ = 2 + 3i is at position (2, 3)</li>
<li>z₂ = -1 + 2i is at position (-1, 2)</li>
<li>z₃ = 4 - i is at position (4, -1)</li>
<li>z₄ = -2 - 2i is at position (-2, -2)</li>
</ul>
</div>

<h3>Vector Addition in the Argand Diagram</h3>
<p>Addition of complex numbers corresponds to <em>vector addition</em> in the Argand diagram. The sum z₁ + z₂ is obtained by the parallelogram law: place vectors for z₁ and z₂ tail-to-tail, and their sum is the diagonal of the resulting parallelogram.</p>

<div class="worked-example">
<p><strong>Example 2:</strong> Visualizing addition</p>
<p>If z₁ = 1 + i and z₂ = 2 + i, then z₁ + z₂ = 3 + 2i</p>
<p>Geometrically, we move 1 unit right and 1 unit up (for z₁), then 2 more units right and 1 more unit up (for z₂), ending at (3, 2).</p>
</div>
"""
    },
    {
        "title": "Argument and Polar Form",
        "body": """
<h3>The Argument of a Complex Number</h3>
<p>For a non-zero complex number z = a + bi, the <strong>argument</strong> is the angle θ measured counterclockwise from the positive real axis to the position vector of z:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">arg(z) = θ, where \\(\\tan(θ) = \\frac{b}{a}\\)</p>
</div>

<p><strong>Important:</strong> The angle must be adjusted based on which quadrant z is in:</p>
<ul>
<li><strong>Q1:</strong> a > 0, b ≥ 0: θ ∈ [0, π/2)</li>
<li><strong>Q2:</strong> a ≤ 0, b > 0: θ ∈ (π/2, π]</li>
<li><strong>Q3:</strong> a < 0, b ≤ 0: θ ∈ (π, 3π/2) or [-π, -π/2)</li>
<li><strong>Q4:</strong> a ≥ 0, b < 0: θ ∈ (3π/2, 2π) or [-π/2, 0)</li>
</ul>

<p>The <strong>principal argument</strong> is typically chosen in the range (-π, π].</p>

<h3>Polar Form of Complex Numbers</h3>
<p>A complex number can be written in <strong>polar form</strong> using its modulus r = |z| and argument θ:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">z = r(cos θ + i sin θ) = r · cis(θ) = re^(iθ)</p>
</div>

<p>where:</p>
<ul>
<li>r = |z| = \\(\\sqrt{a^2 + b^2}\\)</li>
<li>\\(\\cos(θ) = \\frac{a}{r}\\) and \\(\\sin(θ) = \\frac{b}{r}\\)</li>
</ul>

<h3>Converting Between Forms</h3>
<div class="worked-example">
<p><strong>Example 3:</strong> Rectangular to polar form</p>
<p>Express z = 1 + i in polar form</p>
<p>r = |1 + i| = \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\)</p>
<p>\\(\\tan(θ) = \\frac{1}{1} = 1\\), and z is in Q1, so θ = π/4</p>
<p>Therefore: z = \\(\\sqrt{2} \\cdot \\text{cis}(π/4) = \\sqrt{2} e^{i\\pi/4}\\)</p>
</div>

<div class="worked-example">
<p><strong>Example 4:</strong> Polar to rectangular form</p>
<p>Express w = 2·cis(2π/3) in rectangular form</p>
<p>\\(\\cos(2π/3) = -1/2\\) and \\(\\sin(2π/3) = \\sqrt{3}/2\\)</p>
<p>w = 2(-1/2 + i·√3/2) = -1 + i√3</p>
</div>
"""
    },
    {
        "title": "Multiplication and Division in Polar Form",
        "body": """
<h3>Products and Quotients</h3>
<p>Polar form makes multiplication and division much simpler:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">If z₁ = r₁·cis(θ₁) and z₂ = r₂·cis(θ₂), then:</p>
<p style="text-align: center;">z₁z₂ = r₁r₂·cis(θ₁ + θ₂)</p>
<p style="text-align: center;">z₁/z₂ = (r₁/r₂)·cis(θ₁ - θ₂)</p>
</div>

<p><strong>Interpretation:</strong> Multiplying complex numbers scales by r₁r₂ and rotates by angle θ₁ + θ₂.</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 5:</strong> Multiplication in polar form</p>
<p>Multiply z₁ = 2·cis(π/6) and z₂ = 3·cis(π/3)</p>
<p>z₁z₂ = (2)(3)·cis(π/6 + π/3) = 6·cis(π/2) = 6(cos(π/2) + i·sin(π/2)) = 6i</p>
</div>

<div class="worked-example">
<p><strong>Example 6:</strong> Division in polar form</p>
<p>Divide z₁ = 8·cis(3π/4) by z₂ = 2·cis(π/4)</p>
<p>z₁/z₂ = (8/2)·cis(3π/4 - π/4) = 4·cis(π/2) = 4i</p>
</div>

<div class="worked-example">
<p><strong>Example 7:</strong> Geometric significance of multiplication</p>
<p>To find i · (1 + i) = i + i² = -1 + i:</p>
<p>In polar form: 1 + i = \\(\\sqrt{2}·\\text{cis}(π/4)\\) and i = cis(π/2)</p>
<p>Product = \\(\\sqrt{2}·1·\\text{cis}(π/4 + π/2) = \\sqrt{2}·\\text{cis}(3π/4) = \\sqrt{2}(-\\frac{1}{\\sqrt{2}} + i\\frac{1}{\\sqrt{2}}) = -1 + i\\)</p>
<p>(This rotation by π/2 is the same as multiplication by i!)</p>
</div>
"""
    }
]
