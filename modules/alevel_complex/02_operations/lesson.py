TITLE = "Operations on Complex Numbers"

SECTIONS = [
    {
        "title": "Addition and Subtraction",
        "body": """
<h3>Adding and Subtracting Complex Numbers</h3>
<p>Complex numbers are added (and subtracted) by combining their real parts and imaginary parts separately:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\((a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i\)</p>
</div>

<p><strong>In words:</strong> Add (or subtract) the real parts, and add (or subtract) the imaginary parts.</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Addition of complex numbers</p>
<p>\((3 + 2i) + (1 + 5i) = (3 + 1) + (2 + 5)i = 4 + 7i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 2:</strong> Subtraction of complex numbers</p>
<p>\((5 + 3i) - (2 - i) = (5 - 2) + (3 - (-1))i = 3 + 4i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 3:</strong> Combining multiple complex numbers</p>
<p>\((2 + 3i) + (4 - i) - (1 + 2i)\)</p>
<p>\(= (2 + 4 - 1) + (3 - 1 - 2)i\)</p>
<p>\(= 5 + 0i = 5\)</p>
</div>

<h3>Geometric Interpretation</h3>
<p>In the complex plane (which we'll study in more detail), addition of complex numbers corresponds to <em>vector addition</em>. The complex number \(z_1 + z_2\) is obtained by placing the vector for \(z_2\) at the head of the vector for \(z_1\).</p>
"""
    },
    {
        "title": "Multiplication of Complex Numbers",
        "body": """
<h3>Multiplying Complex Numbers</h3>
<p>To multiply two complex numbers, expand using the distributive property and use \\(i^2 = -1\\):</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\((a + bi)(c + di) = ac + adi + bci + bdi^2\)</p>
<p style="text-align: center; font-weight: bold;">\(= (ac - bd) + (ad + bc)i\)</p>
</div>

<h3>Derivation</h3>
<p>\\((a + bi)(c + di) = ac + adi + bci + bd i^2\\)</p>
<p>\\(= ac + adi + bci - bd\\) (since \\(i^2 = -1\\))</p>
<p>\\(= (ac - bd) + (ad + bc)i\\)</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 4:</strong> Simple multiplication</p>
<p>\((2 + i)(3 + 4i)\)</p>
<p>\(= 2 \cdot 3 + 2 \cdot 4i + i \cdot 3 + i \cdot 4i\)</p>
<p>\(= 6 + 8i + 3i + 4i^2\)</p>
<p>\(= 6 + 11i - 4\)</p>
<p>\(= 2 + 11i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 5:</strong> Multiplying a complex number by its conjugate</p>
<p>\((3 - 2i)(3 + 2i) = 9 + 6i - 6i - 4i^2 = 9 + 4 = 13\)</p>
<p>(This gives \\(|3 - 2i|^2 = 9 + 4 = 13\\))</p>
</div>

<div class="worked-example">
<p><strong>Example 6:</strong> Multiplication involving the imaginary unit</p>
<p>\(i \cdot i = i^2 = -1\)</p>
<p>\(i \cdot (2 + 3i) = 2i + 3i^2 = 2i - 3 = -3 + 2i\)</p>
</div>
"""
    },
    {
        "title": "Division of Complex Numbers",
        "body": """
<h3>Dividing Complex Numbers</h3>
<p>To divide \(z_1\) by \(z_2\), multiply both numerator and denominator by the <strong>complex conjugate</strong> of the denominator:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\\(\\frac{a + bi}{c + di} = \\frac{(a + bi)(c - di)}{(c + di)(c - di)} = \\frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}\\)</p>
</div>

<p><strong>Why?</strong> Multiplying by the conjugate makes the denominator a real number: \\((c + di)(c - di) = c^2 + d^2\\)</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 7:</strong> Dividing complex numbers</p>
<p>\\(\\frac{2 + i}{1 - i}\\)</p>
<p>Multiply by the conjugate of 1 - i, which is 1 + i:</p>
<p>\\(= \\frac{(2 + i)(1 + i)}{(1 - i)(1 + i)}\\)</p>
<p>\\(= \\frac{2 + 2i + i + i^2}{1 + 1}\\)</p>
<p>\\(= \\frac{2 + 3i - 1}{2}\\)</p>
<p>\\(= \\frac{1 + 3i}{2}\\)</p>
</div>

<div class="worked-example">
<p><strong>Example 8:</strong> Division by a purely imaginary number</p>
<p>\\(\\frac{3}{2i}\\)</p>
<p>Multiply by \\(\\frac{-2i}{-2i}\\):</p>
<p>\\(= \\frac{3 \\cdot (-2i)}{2i \\cdot (-2i)} = \\frac{-6i}{-4i^2} = \\frac{-6i}{4} = -\\frac{3i}{2}\\)</p>
</div>

<div class="worked-example">
<p><strong>Example 9:</strong> Finding the multiplicative inverse</p>
<p>Find \\(z^{-1}\\) if z = 2 + 3i</p>
<p>\\(z^{-1} = \\frac{1}{2 + 3i} = \\frac{1 \\cdot (2 - 3i)}{(2 + 3i)(2 - 3i)} = \\frac{2 - 3i}{4 + 9} = \\frac{2 - 3i}{13}\\)</p>
</div>
"""
    }
]
