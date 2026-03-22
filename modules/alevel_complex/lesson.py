SECTIONS = [
    {
        "title": "Complex Numbers: Definition and Arithmetic",
        "body": """
<h3>Fundamental Definition</h3>
<p>A <strong>complex number</strong> is defined as z = a + bi, where a, b ∈ ℝ and i is the imaginary unit satisfying <strong>i² = -1</strong>.</p>

<p>We call a = Re(z) the real part and b = Im(z) the imaginary part.</p>

<h3>Arithmetic Operations</h3>
<p><strong>Addition/Subtraction:</strong> (a + bi) ± (c + di) = (a ± c) + (b ± d)i</p>

<p><strong>Multiplication:</strong> (a + bi)(c + di) = ac + adi + bci + bdi² = (ac - bd) + (ad + bc)i</p>

<p><strong>Division:</strong> Multiply numerator and denominator by the conjugate of the denominator:</p>
<p style="text-align: center; font-weight: bold;">(a + bi)/(c + di) = [(a + bi)(c - di)]/[(c + di)(c - di)] = [(ac + bd) + (bc - ad)i]/(c² + d²)</p>

<div class="example-box">
<h4>Example 1: Complex Arithmetic</h4>
<p>Calculate (3 + 2i)(1 - i) and (2 + i)/(1 - i)</p>
<p><strong>Solution:</strong></p>
<p>(3 + 2i)(1 - i) = 3 - 3i + 2i - 2i² = 3 - i + 2 = 5 - i</p>
<p>(2 + i)/(1 - i) = [(2 + i)(1 + i)]/[(1 - i)(1 + i)] = [(2 + 2i + i + i²)]/(1 + 1) = [(2 + 3i - 1)]/2 = (1 + 3i)/2</p>
</div>

<h3>Complex Conjugate</h3>
<p>The <strong>complex conjugate</strong> of z = a + bi is z* = a - bi.</p>

<p><strong>Key properties:</strong></p>
<ul>
<li>z + z* = 2a = 2·Re(z)</li>
<li>z - z* = 2bi = 2i·Im(z)</li>
<li>z·z* = a² + b² = |z|²</li>
<li>(z*)* = z</li>
<li>(z₁ + z₂)* = z₁* + z₂*</li>
<li>(z₁z₂)* = z₁*z₂*</li>
</ul>

<h3>Modulus and Argument</h3>
<p>The <strong>modulus</strong> (or absolute value) of z = a + bi is:</p>
<p style="text-align: center; font-weight: bold;">|z| = √(a² + b²)</p>

<p><strong>Triangle inequality:</strong> |z₁ + z₂| ≤ |z₁| + |z₂|</p>

<div class="example-box">
<h4>Example 2: Modulus</h4>
<p>Find |3 - 4i|</p>
<p><strong>Solution:</strong> |3 - 4i| = √(9 + 16) = √25 = 5</p>
</div>
"""
    },
    {
        "title": "Argand Diagram and Polar Form",
        "body": """
<h3>The Argand Diagram</h3>
<p>Complex numbers are plotted on the <strong>Argand diagram</strong> (complex plane):</p>
<ul>
<li>Horizontal axis: Real part (Re)</li>
<li>Vertical axis: Imaginary part (Im)</li>
<li>Point (a, b) represents z = a + bi</li>
</ul>

<p>Geometrically:</p>
<ul>
<li>|z| is the distance from the origin to point z</li>
<li>Addition of complex numbers corresponds to vector addition</li>
<li>Modulus represents the length of the position vector</li>
</ul>

<h3>Argument and Polar Form</h3>
<p>The <strong>argument</strong> of z = a + bi (with z ≠ 0) is the angle θ from the positive real axis:</p>
<p style="text-align: center; font-weight: bold;">arg(z) = θ, where tan(θ) = b/a  (adjusted for quadrant)</p>

<p>The <strong>principal argument</strong> is chosen to lie in (-π, π] or [0, 2π).</p>

<p>In <strong>polar form</strong>:</p>
<p style="text-align: center; font-weight: bold;">z = r(cos θ + i sin θ) = r·cis(θ) = re^(iθ)</p>

<p>where r = |z| and θ = arg(z).</p>

<div class="example-box">
<h4>Example 3: Converting to Polar Form</h4>
<p>Express z = 1 + i in polar form</p>
<p><strong>Solution:</strong></p>
<p>r = |1 + i| = √(1 + 1) = √2
<br>tan(θ) = 1/1 = 1, and z is in the first quadrant, so θ = π/4
<br>z = √2·cis(π/4) = √2·e^(iπ/4)
</p>
</div>

<h3>Multiplication and Division in Polar Form</h3>
<p><strong>Multiplication:</strong> z₁z₂ = r₁r₂·cis(θ₁ + θ₂)</p>
<p><strong>Division:</strong> z₁/z₂ = (r₁/r₂)·cis(θ₁ - θ₂)</p>

<p>This shows that multiplying complex numbers corresponds to rotating and scaling in the complex plane.</p>

<div class="example-box">
<h4>Example 4: Multiplication in Polar Form</h4>
<p>Multiply z₁ = 2·cis(π/6) and z₂ = 3·cis(π/3)</p>
<p><strong>Solution:</strong> z₁z₂ = (2)(3)·cis(π/6 + π/3) = 6·cis(π/2) = 6i</p>
</div>
"""
    },
    {
        "title": "De Moivre's Theorem: Powers and Roots",
        "body": """
<h3>De Moivre's Theorem</h3>
<p>For any complex number z = r·cis(θ) and any integer n:</p>
<p style="text-align: center; font-weight: bold;">z^n = r^n·cis(nθ) = r^n(cos(nθ) + i·sin(nθ))</p>

<p><strong>Proof (by induction):</strong> For n = 1, the statement is trivial. If true for n = k, then:
<br>z^(k+1) = z^k · z = r^k·cis(kθ) · r·cis(θ) = r^(k+1)·cis(kθ + θ) = r^(k+1)·cis((k+1)θ) ✓
</p>

<p>De Moivre's theorem also holds for rational and real exponents (with appropriate care about branches).</p>

<div class="example-box">
<h4>Example 5: Powers Using De Moivre's Theorem</h4>
<p>Find (1 + i)^5</p>
<p><strong>Solution:</strong> 1 + i = √2·cis(π/4)</p>
<p>(1 + i)^5 = (√2)^5·cis(5π/4) = 4√2·cis(5π/4)</p>
<p>= 4√2[-cos(π/4) - i·sin(π/4)]</p>
<p>= 4√2[-1/√2 - i/√2] = -4 - 4i</p>
</div>

<h3>Finding Roots</h3>
<p>The n-th roots of z = r·cis(θ) are given by:</p>
<p style="text-align: center; font-weight: bold;">z^(1/n) = r^(1/n)·cis[(θ + 2πk)/n], where k = 0, 1, 2, ..., n-1</p>

<p>There are exactly n distinct n-th roots, equally spaced on a circle of radius r^(1/n).</p>

<div class="example-box">
<h4>Example 6: Cube Roots</h4>
<p>Find the cube roots of 8</p>
<p><strong>Solution:</strong> 8 = 8·cis(0). The cube roots are:
<br>8^(1/3)·cis(0/3) = 2·cis(0) = 2
<br>8^(1/3)·cis(2π/3) = 2·cis(2π/3) = 2(-1/2 + i√3/2) = -1 + i√3
<br>8^(1/3)·cis(4π/3) = 2·cis(4π/3) = 2(-1/2 - i√3/2) = -1 - i√3
</p>
</div>

<h3>Expressing Trigonometric Functions Using De Moivre</h3>
<p>From De Moivre's theorem: cos(nθ) + i·sin(nθ) = (cos θ + i·sin θ)^n</p>

<p>Expanding the right side and comparing real and imaginary parts yields expressions for cos(nθ) and sin(nθ) in terms of cos θ and sin θ. For example:</p>
<p>cos(3θ) = 4cos³(θ) - 3cos(θ)</p>
<p>sin(3θ) = 3sin(θ) - 4sin³(θ)</p>
"""
    },
    {
        "title": "Roots of Unity and Geometric Patterns",
        "body": """
<h3>n-th Roots of Unity</h3>
<p>The solutions to z^n = 1 are called the <strong>n-th roots of unity</strong>:</p>
<p style="text-align: center; font-weight: bold;">z_k = cis(2πk/n) = e^(2πik/n), where k = 0, 1, 2, ..., n-1</p>

<p>These are n distinct points equally spaced on the unit circle, forming a regular n-gon.</p>

<div class="example-box">
<h4>Example 7: Fourth Roots of Unity</h4>
<p>Find the fourth roots of unity</p>
<p><strong>Solution:</strong></p>
<p>z₀ = cis(0) = 1
<br>z₁ = cis(π/2) = i
<br>z₂ = cis(π) = -1
<br>z₃ = cis(3π/2) = -i
</p>
</div>

<h3>Geometric Interpretation</h3>
<p>The n-th roots of unity form a regular n-gon centered at the origin. Successive roots differ by a rotation of 2π/n.</p>

<p>If ω = e^(2πi/n), then the n-th roots are: 1, ω, ω², ..., ω^(n-1)</p>

<h3>Key Properties</h3>
<ul>
<li>The product of all n-th roots of unity is (-1)^(n-1)</li>
<li>The sum of all n-th roots of unity is 0 (for n > 1)</li>
<li>Proof: Sum = (1 - ω^n)/(1 - ω) = (1 - 1)/(1 - ω) = 0 for ω ≠ 1</li>
</ul>

<h3>n-th Roots of General Complex Numbers</h3>
<p>For any complex number w = s·cis(φ), the n-th roots are:</p>
<p>w^(1/n) · ω^k, where ω = e^(2πi/n) and k = 0, 1, ..., n-1</p>

<p>Geometrically, these form a regular n-gon rotated and scaled appropriately.</p>

<div class="example-box">
<h4>Example 8: Cubic Roots of i</h4>
<p>Find the cube roots of i</p>
<p><strong>Solution:</strong> i = 1·cis(π/2)</p>
<p>The cube roots are: cis(π/6), cis(π/6 + 2π/3), cis(π/6 + 4π/3)</p>
<p>= cis(π/6), cis(5π/6), cis(3π/2)
<br>= (√3/2 + i/2), (-√3/2 + i/2), -i
</p>
</div>

<h3>Applications: Polynomial Equations</h3>
<p>Complex numbers allow us to factor polynomials completely. Every polynomial of degree n has exactly n roots (counting multiplicities) in ℂ.</p>

<p>For equations like z^n = c (where c is complex), we now have n solutions guaranteed (unlike in ℝ).</p>
"""
    },
    {
        "title": "Locus and Region Problems in the Complex Plane",
        "body": """
<h3>Equations as Loci</h3>
<p>In the complex plane, equations define curves or regions:</p>

<p><strong>|z - a| = r:</strong> Circle centered at a with radius r</p>
<p><strong>|z - a| = |z - b|:</strong> Perpendicular bisector of segment joining a and b</p>
<p><strong>|z - a| < r:</strong> Interior of circle (open disk)</p>
<p><strong>|z - a| ≤ r:</strong> Closed disk</p>

<div class="example-box">
<h4>Example 9: Describing a Locus</h4>
<p>Describe the locus of points satisfying |z - 1| = |z - i|</p>
<p><strong>Solution:</strong> These are points equidistant from 1 and i. Let z = x + yi:
<br>|x + yi - 1| = |x + yi - i|
<br>|(x-1) + yi| = |x + (y-1)i|
<br>√[(x-1)² + y²] = √[x² + (y-1)²]
<br>(x-1)² + y² = x² + (y-1)²
<br>x² - 2x + 1 + y² = x² + y² - 2y + 1
<br>-2x = -2y ⟹ x = y
<br>The locus is the line y = x (the perpendicular bisector).
</p>
</div>

<h3>Argument Conditions</h3>
<p><strong>arg(z) = θ:</strong> Ray from origin at angle θ</p>
<p><strong>arg(z - a) = θ:</strong> Ray from a at angle θ</p>
<p><strong>α < arg(z) < β:</strong> Angular sector</p>

<div class="example-box">
<h4>Example 10: Angular Region</h4>
<p>Describe the region satisfying π/4 < arg(z) < π/2 and |z| < 2</p>
<p><strong>Solution:</strong> This is the open sector of the unit disk between angles π/4 and π/2, a "pizza slice" shape centered at the origin with radius less than 2.</p>
</div>

<h3>Inequalities and Regions</h3>
<p>Combining modulus and argument conditions yields regions in the complex plane:</p>
<ul>
<li>Annulus (ring): r₁ < |z - a| < r₂</li>
<li>Sector: α < arg(z - a) < β and |z - a| < r</li>
<li>Half-plane: Re(z) > c or Im(z) < d</li>
</ul>

<p>These form the basis for complex analysis and contour integration (advanced topics).</p>
"""
    }
]
