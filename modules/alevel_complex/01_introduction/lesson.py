TITLE = "Introduction to Complex Numbers"

SECTIONS = [
    {
        "title": "The Imaginary Unit and Definition",
        "body": """
<h3>Fundamental Definition</h3>
<p>A <strong>complex number</strong> is defined as:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">z = a + bi</p>
<p style="text-align: center;">where a, b ∈ ℝ and <strong>i</strong> is the imaginary unit satisfying \\(i^2 = -1\\)</p>
</div>

<p>We call:</p>
<ul>
<li><strong>Re(z) = a</strong> the <em>real part</em> of z</li>
<li><strong>Im(z) = b</strong> the <em>imaginary part</em> of z</li>
</ul>

<h3>The Imaginary Unit</h3>
<p>The imaginary unit <strong>i</strong> is formally defined by the property \\(i^2 = -1\\). This allows us to take square roots of negative numbers:</p>
<ul>
<li>\\(\\sqrt{-1} = i\\)</li>
<li>\\(\\sqrt{-4} = 2i\\)</li>
<li>\\(\\sqrt{-9} = 3i\\)</li>
</ul>

<p>Powers of i follow a cyclic pattern:</p>
<ul>
<li>\\(i^1 = i\\)</li>
<li>\\(i^2 = -1\\)</li>
<li>\\(i^3 = -i\\)</li>
<li>\\(i^4 = 1\\)</li>
<li>\\(i^5 = i\\) (pattern repeats)</li>
</ul>

<h3>Examples of Complex Numbers</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Identify real and imaginary parts</p>
<p>For z = 3 + 2i:</p>
<ul>
<li>Re(z) = 3</li>
<li>Im(z) = 2</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example 2:</strong> Solve \\(x^2 + 1 = 0\\) in ℂ</p>
<p>In the real numbers, this has no solution. In complex numbers:</p>
<p>\\(x^2 = -1\\) implies \\(x = ±i\\)</p>
</div>
"""
    },
    {
        "title": "Complex Conjugate and Key Properties",
        "body": """
<h3>The Complex Conjugate</h3>
<p>For z = a + bi, the <strong>complex conjugate</strong> is:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">z* = a - bi</p>
</div>

<p>Geometrically, z* is the reflection of z across the real axis.</p>

<h3>Key Properties of the Conjugate</h3>
<ul>
<li>\\(z + z^* = 2a = 2 \\cdot \\text{Re}(z)\\)</li>
<li>\\(z - z^* = 2bi = 2i \\cdot \\text{Im}(z)\\)</li>
<li>\\(z \\cdot z^* = a^2 + b^2 = |z|^2\\)</li>
<li>\\((z^*)^* = z\\) (conjugate of conjugate is the original)</li>
<li>\\((z_1 + z_2)^* = z_1^* + z_2^*\\)</li>
<li>\\((z_1 z_2)^* = z_1^* z_2^*\\)</li>
</ul>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 3:</strong> Find the conjugate and verify properties</p>
<p>For z = 3 - 4i:</p>
<ul>
<li>z* = 3 + 4i</li>
<li>z + z* = (3 - 4i) + (3 + 4i) = 6 = 2 · Re(z)</li>
<li>z · z* = (3 - 4i)(3 + 4i) = 9 + 16 = 25 = |z|²</li>
</ul>
</div>
"""
    },
    {
        "title": "Modulus (Absolute Value)",
        "body": """
<h3>Definition of Modulus</h3>
<p>The <strong>modulus</strong> (or absolute value) of a complex number z = a + bi is the distance from the origin to the point (a, b):</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">|z| = \\(\\sqrt{a^2 + b^2}\\)</p>
</div>

<p>Note that |z| is always a non-negative real number.</p>

<h3>Properties of Modulus</h3>
<ul>
<li>\\(|z| \\geq 0\\), with equality iff z = 0</li>
<li>\\(|z_1 z_2| = |z_1| |z_2|\\)</li>
<li>\\(|z_1 / z_2| = |z_1| / |z_2|\\)</li>
<li><strong>Triangle Inequality:</strong> \\(|z_1 + z_2| \\leq |z_1| + |z_2|\\)</li>
<li>\\(z \\cdot z^* = |z|^2\\)</li>
</ul>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 4:</strong> Calculate the modulus</p>
<p>Find |3 - 4i|</p>
<p>\\(|3 - 4i| = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\\)</p>
</div>

<div class="worked-example">
<p><strong>Example 5:</strong> Modulus of a purely imaginary number</p>
<p>Find |5i|</p>
<p>\\(|5i| = \\sqrt{0^2 + 5^2} = \\sqrt{25} = 5\\)</p>
</div>
"""
    }
]
