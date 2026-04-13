TITLE = "De Moivre's Theorem and Roots of Unity"

SECTIONS = [
    {
        "title": "De Moivre's Theorem: Powers of Complex Numbers",
        "body": """
<h3>The Theorem</h3>
<p>For any complex number \(z = r \\cdot \\text{cis}(\\theta)\) and any integer n:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\(z^n = r^n \\cdot \\text{cis}(n\\theta) = r^n(\cos(n\\theta) + i \\cdot \sin(n\\theta))\)</p>
</div>

<p>This powerful theorem shows that raising a complex number to a power corresponds to raising the modulus to that power and multiplying the argument by that power.</p>

<h3>Proof by Induction</h3>
<p><strong>Base case:</strong> For n = 1, the statement is \(z = r \\cdot \\text{cis}(\\theta)\), which is true by definition.</p>

<p><strong>Inductive step:</strong> Assume \(z^k = r^k \\cdot \\text{cis}(k\\theta)\). Then:</p>
<p>\(z^{k+1} = z^k \\cdot z = r^k \\cdot \\text{cis}(k\\theta) \\cdot r \\cdot \\text{cis}(\\theta) = r^{k+1} \\cdot \\text{cis}(k\\theta + \\theta) = r^{k+1} \\cdot \\text{cis}((k+1)\\theta)\)</p>

<p>By induction, the theorem holds for all positive integers n. (Extensions to negative and rational exponents are also valid with appropriate care.)</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Powers using De Moivre's theorem</p>
<p>Find \((1 + i)^5\)</p>
<p>First, convert \(1 + i\) to polar form:</p>
<p>\(r =\) \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\), \(\\theta = \\pi/4\)</p>
<p>So \(1 + i =\) \\(\\sqrt{2} \\cdot \\text{cis}(\\pi/4)\\)</p>
<p>\((1 + i)^5 = (\)\\(\\sqrt{2}\\)\()^5 \\cdot \\text{cis}(5\\pi/4) =\) \\(4\\sqrt{2} \\cdot \\text{cis}(5\\pi/4)\\)</p>
<p>\(=\) \\(4\\sqrt{2}[\\cos(5\\pi/4) + i \\cdot \\sin(5\\pi/4)]\\)</p>
<p>\(=\) \\(4\\sqrt{2}[-\\frac{1}{\\sqrt{2}} - i \\cdot \\frac{1}{\\sqrt{2}}]\\)</p>
<p>\(= -4 - 4i\)</p>
</div>

<div class="worked-example">
<p><strong>Example 2:</strong> Finding \((\\sqrt{3} + i)^3\)</p>
<p>\(r =\) \\(\\sqrt{3 + 1} = 2\\), \(\tan(\\theta) = 1/\\sqrt{3}\), so \(\\theta = \\pi/6\)</p>
<p>\((\\sqrt{3} + i)^3 = 2^3 \\cdot \\text{cis}(3 \\cdot \\pi/6) = 8 \\cdot \\text{cis}(\\pi/2) = 8i\)</p>
</div>

<h3>Trigonometric Identities from De Moivre</h3>
<p>By expanding \((\cos\\theta + i \\cdot \sin\\theta)^n\) and comparing real and imaginary parts, we can derive identities like:</p>
<ul>
<li>\(\cos(2\\theta) = 2\cos^2(\\theta) - 1 = \cos^2(\\theta) - \sin^2(\\theta)\)</li>
<li>\(\sin(2\\theta) = 2\sin(\\theta)\cos(\\theta)\)</li>
<li>\(\cos(3\\theta) = 4\cos^3(\\theta) - 3\cos(\\theta)\)</li>
<li>\(\sin(3\\theta) = 3\sin(\\theta) - 4\sin^3(\\theta)\)</li>
</ul>
"""
    },
    {
        "title": "Finding Roots of Complex Numbers",
        "body": """
<h3>The n-th Roots Formula</h3>
<p>The n-th roots of \(z = r \\cdot \\text{cis}(\\theta)\) are given by:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\(z^{1/n} = r^{1/n} \\cdot \\text{cis}\)\\(\\left[\\frac{\\theta + 2\\pi k}{n}\\right]\\), where \(k = 0, 1, 2, \ldots, n-1\)</p>
</div>

<p>There are exactly <strong>n distinct</strong> n-th roots, equally spaced around a circle of radius \(r^{1/n}\).</p>

<h3>Key Insight</h3>
<p>The multiple roots arise because adding \(2\\pi\) to the argument gives the same complex number. For the n-th root, we account for this periodicity by considering \(k = 0, 1, \ldots, n-1\).</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 3:</strong> Cube roots of 8</p>
<p>\(8 = 8 \\cdot \\text{cis}(0)\). The three cube roots are:</p>
<ul>
<li>\(k=0\): \(8^{1/3} \\cdot \\text{cis}(0/3) = 2 \\cdot \\text{cis}(0) = 2\)</li>
<li>\(k=1\): \(8^{1/3} \\cdot \\text{cis}(2\\pi/3) = 2 \\cdot \\text{cis}(2\\pi/3) = 2(-1/2 + i\\sqrt{3}/2) = -1 + i\\sqrt{3}\)</li>
<li>\(k=2\): \(8^{1/3} \\cdot \\text{cis}(4\\pi/3) = 2 \\cdot \\text{cis}(4\\pi/3) = 2(-1/2 - i\\sqrt{3}/2) = -1 - i\\sqrt{3}\)</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example 4:</strong> Cube roots of i</p>
<p>\(i = 1 \\cdot \\text{cis}(\\pi/2)\). The three cube roots are:</p>
<ul>
<li>\(k=0\): \(\\text{cis}(\\pi/6) = \cos(\\pi/6) + i \\cdot \sin(\\pi/6) = \\sqrt{3}/2 + i/2\)</li>
<li>\(k=1\): \(\\text{cis}(\\pi/6 + 2\\pi/3) = \\text{cis}(5\\pi/6) = -\\sqrt{3}/2 + i/2\)</li>
<li>\(k=2\): \(\\text{cis}(\\pi/6 + 4\\pi/3) = \\text{cis}(3\\pi/2) = -i\)</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example 5:</strong> Square roots of -1</p>
<p>\(-1 = 1 \\cdot \\text{cis}(\\pi)\). The two square roots are:</p>
<ul>
<li>\(k=0\): \(\\text{cis}(\\pi/2) = i\)</li>
<li>\(k=1\): \(\\text{cis}(\\pi/2 + \\pi) = \\text{cis}(3\\pi/2) = -i\)</li>
</ul>
<p>(These are the solutions to \(z^2 = -1\), as expected.)</p>
</div>
"""
    },
    {
        "title": "Roots of Unity",
        "body": """
<h3>The n-th Roots of Unity</h3>
<p>The solutions to \(z^n = 1\) are called the <strong>n-th roots of unity</strong>. Using our roots formula with \(z = 1 \\cdot \\text{cis}(0)\):</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">\(\omega_k = \\text{cis}(2\\pi k/n) = e^{2\\pi i k/n}\), where \(k = 0, 1, 2, \ldots, n-1\)</p>
</div>

<p>These n distinct points lie equally spaced on the unit circle, forming a regular n-gon.</p>

<h3>Geometric Pattern</h3>
<p>The roots of unity form a regular polygon:</p>
<ul>
<li><strong>n = 2:</strong> Two points: 1 and -1 (the real axis)</li>
<li><strong>n = 3:</strong> Equilateral triangle with vertices at 120° intervals</li>
<li><strong>n = 4:</strong> Square with vertices at 90° intervals: 1, i, -1, -i</li>
<li><strong>n = 6:</strong> Regular hexagon with vertices at 60° intervals</li>
</ul>

<h3>Key Properties</h3>
<ul>
<li>The product of all n-th roots of unity is \((-1)^{n-1}\)</li>
<li>The sum of all n-th roots of unity is 0 (for n > 1)</li>
<li>If \(\omega = e^{2\\pi i/n}\), then the roots are: \(1, \omega, \omega^2, \ldots, \omega^{n-1}\)</li>
</ul>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 6:</strong> Fourth roots of unity</p>
<p>\(z_0 = \\text{cis}(0) = 1\)</p>
<p>\(z_1 = \\text{cis}(\\pi/2) = i\)</p>
<p>\(z_2 = \\text{cis}(\\pi) = -1\)</p>
<p>\(z_3 = \\text{cis}(3\\pi/2) = -i\)</p>
<p>Sum: \(1 + i + (-1) + (-i) = 0\) ✓</p>
</div>

<div class="worked-example">
<p><strong>Example 7:</strong> Sixth roots of unity</p>
<p>The six roots are at angles 0°, 60°, 120°, 180°, 240°, 300°:</p>
<p>\(1, \\text{cis}(\\pi/3), \\text{cis}(2\\pi/3), -1, \\text{cis}(4\\pi/3), \\text{cis}(5\\pi/3)\)</p>
<p>In rectangular form: \(1, 1/2 + i\\sqrt{3}/2, -1/2 + i\\sqrt{3}/2, -1, -1/2 - i\\sqrt{3}/2, 1/2 - i\\sqrt{3}/2\)</p>
</div>
"""
    }
]
