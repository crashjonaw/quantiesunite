TITLE = "De Moivre's Theorem and Roots of Unity"

SECTIONS = [
    {
        "title": "De Moivre's Theorem: Powers of Complex Numbers",
        "body": """
<h3>The Theorem</h3>
<p>For any complex number z = r·cis(θ) and any integer n:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">z^n = r^n·cis(nθ) = r^n(cos(nθ) + i·sin(nθ))</p>
</div>

<p>This powerful theorem shows that raising a complex number to a power corresponds to raising the modulus to that power and multiplying the argument by that power.</p>

<h3>Proof by Induction</h3>
<p><strong>Base case:</strong> For n = 1, the statement is z = r·cis(θ), which is true by definition.</p>

<p><strong>Inductive step:</strong> Assume z^k = r^k·cis(kθ). Then:</p>
<p>z^(k+1) = z^k · z = r^k·cis(kθ) · r·cis(θ) = r^(k+1)·cis(kθ + θ) = r^(k+1)·cis((k+1)θ)</p>

<p>By induction, the theorem holds for all positive integers n. (Extensions to negative and rational exponents are also valid with appropriate care.)</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Powers using De Moivre's theorem</p>
<p>Find (1 + i)⁵</p>
<p>First, convert 1 + i to polar form:</p>
<p>r = \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\), θ = π/4</p>
<p>So 1 + i = \\(\\sqrt{2}·\\text{cis}(π/4)\\)</p>
<p>(1 + i)⁵ = (\\(\\sqrt{2}\\))⁵·cis(5π/4) = \\(4\\sqrt{2}·\\text{cis}(5π/4)\\)</p>
<p>= \\(4\\sqrt{2}[\\cos(5π/4) + i·\\sin(5π/4)]\\)</p>
<p>= \\(4\\sqrt{2}[-\\frac{1}{\\sqrt{2}} - i·\\frac{1}{\\sqrt{2}}]\\)</p>
<p>= -4 - 4i</p>
</div>

<div class="worked-example">
<p><strong>Example 2:</strong> Finding (√3 + i)³</p>
<p>r = \\(\\sqrt{3 + 1} = 2\\), tan(θ) = 1/√3, so θ = π/6</p>
<p>(√3 + i)³ = 2³·cis(3·π/6) = 8·cis(π/2) = 8i</p>
</div>

<h3>Trigonometric Identities from De Moivre</h3>
<p>By expanding (cos θ + i·sin θ)^n and comparing real and imaginary parts, we can derive identities like:</p>
<ul>
<li>cos(2θ) = 2cos²(θ) - 1 = cos²(θ) - sin²(θ)</li>
<li>sin(2θ) = 2sin(θ)cos(θ)</li>
<li>cos(3θ) = 4cos³(θ) - 3cos(θ)</li>
<li>sin(3θ) = 3sin(θ) - 4sin³(θ)</li>
</ul>
"""
    },
    {
        "title": "Finding Roots of Complex Numbers",
        "body": """
<h3>The n-th Roots Formula</h3>
<p>The n-th roots of z = r·cis(θ) are given by:</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">z^(1/n) = r^(1/n)·cis\\(\\left[\\frac{θ + 2πk}{n}\\right]\\), where k = 0, 1, 2, ..., n-1</p>
</div>

<p>There are exactly <strong>n distinct</strong> n-th roots, equally spaced around a circle of radius r^(1/n).</p>

<h3>Key Insight</h3>
<p>The multiple roots arise because adding 2π to the argument gives the same complex number. For the n-th root, we account for this periodicity by considering k = 0, 1, ..., n-1.</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 3:</strong> Cube roots of 8</p>
<p>8 = 8·cis(0). The three cube roots are:</p>
<ul>
<li>k=0: 8^(1/3)·cis(0/3) = 2·cis(0) = 2</li>
<li>k=1: 8^(1/3)·cis(2π/3) = 2·cis(2π/3) = 2(-1/2 + i√3/2) = -1 + i√3</li>
<li>k=2: 8^(1/3)·cis(4π/3) = 2·cis(4π/3) = 2(-1/2 - i√3/2) = -1 - i√3</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example 4:</strong> Cube roots of i</p>
<p>i = 1·cis(π/2). The three cube roots are:</p>
<ul>
<li>k=0: cis(π/6) = cos(π/6) + i·sin(π/6) = √3/2 + i/2</li>
<li>k=1: cis(π/6 + 2π/3) = cis(5π/6) = -√3/2 + i/2</li>
<li>k=2: cis(π/6 + 4π/3) = cis(3π/2) = -i</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example 5:</strong> Square roots of -1</p>
<p>-1 = 1·cis(π). The two square roots are:</p>
<ul>
<li>k=0: cis(π/2) = i</li>
<li>k=1: cis(π/2 + π) = cis(3π/2) = -i</li>
</ul>
<p>(These are the solutions to z² = -1, as expected.)</p>
</div>
"""
    },
    {
        "title": "Roots of Unity",
        "body": """
<h3>The n-th Roots of Unity</h3>
<p>The solutions to z^n = 1 are called the <strong>n-th roots of unity</strong>. Using our roots formula with z = 1·cis(0):</p>
<div class="concept-box">
<p style="text-align: center; font-weight: bold;">ω_k = cis(2πk/n) = e^(2πik/n), where k = 0, 1, 2, ..., n-1</p>
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
<li>The product of all n-th roots of unity is (-1)^(n-1)</li>
<li>The sum of all n-th roots of unity is 0 (for n > 1)</li>
<li>If ω = e^(2πi/n), then the roots are: 1, ω, ω², ..., ω^(n-1)</li>
</ul>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 6:</strong> Fourth roots of unity</p>
<p>z₀ = cis(0) = 1</p>
<p>z₁ = cis(π/2) = i</p>
<p>z₂ = cis(π) = -1</p>
<p>z₃ = cis(3π/2) = -i</p>
<p>Sum: 1 + i + (-1) + (-i) = 0 ✓</p>
</div>

<div class="worked-example">
<p><strong>Example 7:</strong> Sixth roots of unity</p>
<p>The six roots are at angles 0°, 60°, 120°, 180°, 240°, 300°:</p>
<p>1, cis(π/3), cis(2π/3), -1, cis(4π/3), cis(5π/3)</p>
<p>In rectangular form: 1, 1/2 + i√3/2, -1/2 + i√3/2, -1, -1/2 - i√3/2, 1/2 - i√3/2</p>
</div>
"""
    }
]
