TITLE = "What is a Quadratic?"

SECTIONS = [
    {
        "title": "Definition: Quadratic Equations",
        "body": """
<h3>Axiomatic Definition</h3>
<p>A <strong>quadratic equation</strong> is a polynomial equation of degree 2. In standard form:</p>
<div class="formula-box">
<p>$$ax^2 + bx + c = 0, \\quad a, b, c \\in \\mathbb{R}, \\quad a \\neq 0$$</p>
</div>

<p>The condition <strong>a ≠ 0</strong> is essential; otherwise the equation would be linear, not quadratic.</p>

<h3>Why is the Highest Power 2?</h3>
<p>The term <strong>quadratic</strong> comes from the Latin "quadratus" (square). The equation must have an x² term. Think of it geometrically: quadratic equations describe area (which involves products of two dimensions).</p>

<h3>Recognizing Quadratics</h3>
<p>Any equation that can be rearranged to the form ax² + bx + c = 0 is quadratic:</p>
<ul style="line-height: 1.8;">
  <li>✓ 3x² + 2x + 1 = 0 (standard form)</li>
  <li>✓ x² = 5x - 6 (rearrange to x² - 5x + 6 = 0)</li>
  <li>✓ (x + 2)(x - 3) = 0 (expand to x² - x - 6 = 0)</li>
  <li>✗ 2x + 1 = 0 (linear, no x² term)</li>
  <li>✗ x³ + x² = 0 (cubic, highest power is 3)</li>
</ul>

<h3>Why Quadratics Matter</h3>
<p>Quadratic equations appear everywhere in real life:</p>
<ul style="line-height: 1.8;">
  <li><strong>Projectile Motion:</strong> Height vs time when throwing a ball</li>
  <li><strong>Area Optimization:</strong> Maximum area with limited fencing</li>
  <li><strong>Business:</strong> Profit maximization curves</li>
  <li><strong>Physics:</strong> Parabolic trajectories, energy equations</li>
  <li><strong>Engineering:</strong> Bridge arches, antenna dishes (parabolic shapes)</li>
</ul>
"""
    },
    {
        "title": "Transforming to Standard Form",
        "body": """
<h3>Why Standard Form Matters</h3>
<p>Having a quadratic in standard form ax² + bx + c = 0 allows us to use solving techniques and analyze it systematically. Any quadratic can be rearranged to this form through algebraic manipulation.</p>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Simple Rearrangement</h4>
<p><strong>Problem:</strong> Convert \\(x^2 + 6 = 4x\\) to standard form.</p>
<p><strong>Solution:</strong></p>
<p>$$x^2 + 6 = 4x$$</p>
<p>$$x^2 - 4x + 6 = 0$$</p>
<p class="text-muted-note">Here: a = 1, b = -4, c = 6</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 2: Factored Form to Standard</h4>
<p><strong>Problem:</strong> Rewrite (x - 2)² = 9 in standard form.</p>
<p><strong>Solution:</strong></p>
<p>$$\\begin{align}
(x-2)^2 &= 9 \\\\
x^2 - 4x + 4 &= 9 \\\\
x^2 - 4x - 5 &= 0
\\end{align}$$</p>
<p class="text-muted-note">Here: a = 1, b = -4, c = -5</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 3: Expanded Form</h4>
<p><strong>Problem:</strong> Expand (2x + 3)(x - 1) = 0 and write in standard form.</p>
<p><strong>Solution:</strong></p>
<p>$$\\begin{align}
(2x + 3)(x - 1) &= 0 \\\\
2x^2 - 2x + 3x - 3 &= 0 \\\\
2x^2 + x - 3 &= 0
\\end{align}$$</p>
<p class="text-muted-note">Here: a = 2, b = 1, c = -3</p>
</div>
"""
    },
    {
        "title": "The Discriminant: Predicting Solution Types",
        "body": """
<h3>What is the Discriminant?</h3>
<p>Before we even solve a quadratic, we can predict <strong>how many real solutions</strong> it has using the <strong>discriminant</strong>:</p>
<div class="formula-box">
<p>$$\\Delta = b^2 - 4ac$$</p>
</div>

<p style="font-size: 1.1em; margin: 20px 0"><strong>The discriminant tells us:</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0">
  <tr >
    <th style="padding: 12px; text-align: left"><strong>Δ Value</strong></th>
    <th style="padding: 12px; text-align: left"><strong>Number of Real Roots</strong></th>
    <th style="padding: 12px; text-align: left"><strong>Nature of Roots</strong></th>
  </tr>
  <tr >
    <td style="padding: 12px;">Δ > 0</td>
    <td style="padding: 12px;">Two distinct roots</td>
    <td style="padding: 12px;">Two different real numbers</td>
  </tr>
  <tr >
    <td style="padding: 12px;">Δ = 0</td>
    <td style="padding: 12px;">One repeated root</td>
    <td style="padding: 12px;">One real number (counted twice)</td>
  </tr>
  <tr >
    <td style="padding: 12px;">Δ < 0</td>
    <td style="padding: 12px;">No real roots</td>
    <td style="padding: 12px;">Two complex conjugates</td>
  </tr>
</table>

<div class="worked-example">
<h4 class="accent-heading">Example 4: Computing the Discriminant</h4>
<p><strong>Problem:</strong> For 2x² - 3x + 5 = 0, find the discriminant and predict the nature of roots.</p>
<p><strong>Solution:</strong></p>
<p>Here: a = 2, b = -3, c = 5</p>
<p>$$\\Delta = b^2 - 4ac = (-3)^2 - 4(2)(5) = 9 - 40 = -31$$</p>
<p style="margin-top: 10px"><strong>Interpretation:</strong> Since Δ = -31 < 0, this equation has <strong>no real solutions</strong>. The roots are complex numbers.</p>
</div>

<div class="warning-box">
<p ><strong>Key Insight:</strong> The discriminant is your quick check before solving. It tells you what to expect!</p>
</div>
"""
    }
]
