SECTIONS = [
    {
        "title": "Quadratic Equations: Definition and Standard Form",
        "body": """
<h3>Axiomatic Definition</h3>
<p>A <strong>quadratic equation</strong> is a polynomial equation of degree 2. In standard form:</p>
<div class="formula-box">
<p>$$ax^2 + bx + c = 0, \\quad a, b, c \\in \\mathbb{R}, \\quad a \\neq 0$$</p>
</div>

<p>The condition a ≠ 0 is essential; otherwise the equation would be linear.</p>

<h3>Why Quadratics Matter</h3>
<p>Quadratic equations model:</p>
<ul>
  <li>Projectile motion (height vs time)</li>
  <li>Area and optimization problems</li>
  <li>Natural phenomena with parabolic behavior</li>
</ul>

<h3>Transformation to Standard Form</h3>
<p>Any quadratic can be rearranged to standard form. For example:</p>
<p>$$3x^2 - 5x + 2 = 0 \\quad (\\text{already standard})$$</p>
<p>$$x^2 + 6 = 4x \\Rightarrow x^2 - 4x + 6 = 0$$</p>

<div class="example-box">
<h4>Example 1: Converting to Standard Form</h4>
<p><strong>Problem:</strong> Rewrite (x-2)² = 9 in standard form.</p>
<p><strong>Solution:</strong></p>
<p>\\begin{align}
(x-2)^2 &= 9 \\\\
x^2 - 4x + 4 &= 9 \\\\
x^2 - 4x - 5 &= 0
\\end{align}</p>
</div>

<h3>Key Insight: The Discriminant</h3>
<p>The <strong>discriminant</strong> Δ = b² - 4ac determines the nature of roots:</p>
<ul>
  <li>If Δ > 0: Two distinct real roots</li>
  <li>If Δ = 0: One repeated real root</li>
  <li>If Δ < 0: Two complex conjugate roots</li>
</ul>
"""
    },
    {
        "title": "Solving Quadratics: Factorization and Completing the Square",
        "body": """
<h3>Method 1: Factorization</h3>
<p>If ax² + bx + c = 0 can be factored as a(x - α)(x - β) = 0, then by the zero-product property:</p>
<div class="formula-box">
<p>$$x = \\alpha \\quad \\text{or} \\quad x = \\beta$$</p>
</div>

<p><strong>Key insight:</strong> We seek two numbers that multiply to c/a and add to b/a.</p>

<div class="example-box">
<h4>Example 2: Factorization</h4>
<p><strong>Problem:</strong> Solve 2x² + 5x + 3 = 0</p>
<p><strong>Solution:</strong></p>
<p>We need factors of 2 · 3 = 6 that add to 5: these are 2 and 3.</p>
<p>\\begin{align}
2x^2 + 5x + 3 &= 2x^2 + 2x + 3x + 3 \\\\
&= 2x(x + 1) + 3(x + 1) \\\\
&= (2x + 3)(x + 1) = 0
\\end{align}</p>
<p>Therefore: x = -3/2 or x = -1</p>
</div>

<h3>Method 2: Completing the Square</h3>
<p>We transform ax² + bx + c into the form a(x + p)² + q by algebraic manipulation.</p>

<p><strong>Derivation:</strong> Starting with x² + bx, we add and subtract (b/2)²:</p>
<p>$$x^2 + bx = \\left(x + \\frac{b}{2}\\right)^2 - \\left(\\frac{b}{2}\\right)^2$$</p>

<div class="example-box">
<h4>Example 3: Completing the Square</h4>
<p><strong>Problem:</strong> Solve x² + 6x + 4 = 0</p>
<p><strong>Solution:</strong></p>
<p>\\begin{align}
x^2 + 6x + 4 &= 0 \\\\
(x + 3)^2 - 9 + 4 &= 0 \\\\
(x + 3)^2 &= 5 \\\\
x + 3 &= \\pm \\sqrt{5} \\\\
x &= -3 \\pm \\sqrt{5}
\\end{align}</p>
</div>

<h3>The Vertex Form</h3>
<p>Completing the square gives us the <strong>vertex form</strong> of a quadratic:</p>
<div class="formula-box">
<p>$$f(x) = a(x - h)^2 + k$$</p>
</div>
<p>where the vertex is at (h, k).</p>
"""
    },
    {
        "title": "The Quadratic Formula: Complete Derivation",
        "body": """
<h3>Deriving the Quadratic Formula</h3>
<p>We derive x = (-b ± √(b² - 4ac))/(2a) from first principles using completing the square.</p>

<p><strong>Starting equation:</strong> ax² + bx + c = 0 with a ≠ 0</p>

<p><strong>Step 1:</strong> Divide by a</p>
<p>$$x^2 + \\frac{b}{a}x + \\frac{c}{a} = 0$$</p>

<p><strong>Step 2:</strong> Complete the square</p>
<p>$$\\left(x + \\frac{b}{2a}\\right)^2 - \\left(\\frac{b}{2a}\\right)^2 + \\frac{c}{a} = 0$$</p>

<p><strong>Step 3:</strong> Combine constants</p>
<p>$$\\left(x + \\frac{b}{2a}\\right)^2 = \\frac{b^2 - 4ac}{4a^2}$$</p>

<p><strong>Step 4:</strong> Take square roots</p>
<p>$$x + \\frac{b}{2a} = \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}$$</p>

<p><strong>Step 5:</strong> Solve for x</p>
<div class="formula-box">
<p>$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$</p>
</div>

<div class="example-box">
<h4>Example 4: Using the Quadratic Formula</h4>
<p><strong>Problem:</strong> Solve 3x² - 4x - 5 = 0</p>
<p><strong>Solution:</strong> Here a = 3, b = -4, c = -5</p>
<p>Δ = (-4)² - 4(3)(-5) = 16 + 60 = 76</p>
<p>$$x = \\frac{4 \\pm \\sqrt{76}}{6} = \\frac{4 \\pm 2\\sqrt{19}}{6} = \\frac{2 \\pm \\sqrt{19}}{3}$$</p>
</div>
"""
    },
    {
        "title": "The Quadratic Function and Its Graph",
        "body": """
<h3>Definition: The Quadratic Function</h3>
<p>A <strong>quadratic function</strong> is f(x) = ax² + bx + c (a ≠ 0). Its graph is a <strong>parabola</strong>.</p>

<h3>Key Properties of the Parabola</h3>

<p><strong>1. Direction of Opening:</strong></p>
<ul>
  <li>If a > 0: parabola opens upward (has a minimum)</li>
  <li>If a < 0: parabola opens downward (has a maximum)</li>
</ul>

<p><strong>2. Vertex (Turning Point):</strong> From the vertex form f(x) = a(x - h)² + k, the vertex is (h, k).</p>

<p>Alternatively, from standard form:</p>
<div class="formula-box">
<p>$$x_v = -\\frac{b}{2a}, \\quad y_v = f\\left(-\\frac{b}{2a}\\right)$$</p>
</div>

<p><strong>3. Axis of Symmetry:</strong> The vertical line x = -b/(2a) divides the parabola into two mirror images.</p>

<p><strong>4. y-intercept:</strong> Set x = 0: f(0) = c</p>

<p><strong>5. x-intercepts (Roots):</strong> Solve ax² + bx + c = 0 using the quadratic formula.</p>

<div class="example-box">
<h4>Example 5: Analyzing a Quadratic</h4>
<p><strong>Problem:</strong> Analyze f(x) = -2x² + 8x - 6</p>
<p><strong>Solution:</strong></p>
<ul>
  <li>a = -2 < 0: Opens downward (maximum exists)</li>
  <li>Vertex x-coordinate: x = -8/(2(-2)) = 2</li>
  <li>Vertex y-coordinate: f(2) = -2(4) + 16 - 6 = 2</li>
  <li>Vertex: (2, 2)</li>
  <li>y-intercept: f(0) = -6</li>
  <li>x-intercepts: -2x² + 8x - 6 = 0 ⟹ x² - 4x + 3 = 0 ⟹ (x-1)(x-3) = 0
    <br>So x = 1 or x = 3</li>
</ul>
</div>

<h3>Range and Restrictions</h3>
<ul>
  <li><strong>Domain:</strong> All real numbers ℝ</li>
  <li><strong>Range (if a > 0):</strong> [y_v, ∞) where y_v is the minimum</li>
  <li><strong>Range (if a < 0):</strong> (-∞, y_v] where y_v is the maximum</li>
</ul>
"""
    },
    {
        "title": "Vieta's Formulas and Sum/Product of Roots",
        "body": """
<h3>Deriving Vieta's Formulas</h3>
<p>For the quadratic ax² + bx + c = 0 with roots α and β:</p>

<p><strong>Factored Form:</strong></p>
<p>$$a(x - \\alpha)(x - \\beta) = ax^2 - a(\\alpha + \\beta)x + a\\alpha\\beta$$</p>

<p>Comparing with ax² + bx + c:</p>
<div class="formula-box">
<p>$$\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha \\beta = \\frac{c}{a}$$</p>
</div>

<p><strong>Proof by quadratic formula:</strong></p>
<p>$$\\alpha + \\beta = \\frac{-b + \\sqrt{\\Delta}}{2a} + \\frac{-b - \\sqrt{\\Delta}}{2a} = \\frac{-2b}{2a} = -\\frac{b}{a}$$</p>

<p>$$\\alpha \\beta = \\frac{(-b)^2 - \\Delta}{4a^2} = \\frac{b^2 - (b^2 - 4ac)}{4a^2} = \\frac{c}{a}$$</p>

<div class="example-box">
<h4>Example 6: Using Vieta's Formulas</h4>
<p><strong>Problem:</strong> Find two numbers whose sum is 7 and whose product is 12.</p>
<p><strong>Solution:</strong> If the numbers are α and β, they are roots of:</p>
<p>$$x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0$$
<br>$$x^2 - 7x + 12 = 0$$
<br>$$(x - 3)(x - 4) = 0$$</p>
<p>So the numbers are 3 and 4.</p>
</div>

<h3>Constructing Quadratics from Roots</h3>
<p>If we know the roots α and β, we can construct a quadratic:</p>
<p>$$x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0$$</p>

<div class="example-box">
<h4>Example 7: Building a Quadratic</h4>
<p><strong>Problem:</strong> Write a quadratic with roots 2 + √3 and 2 - √3</p>
<p><strong>Solution:</strong></p>
<p>$$\\alpha + \\beta = (2 + \\sqrt{3}) + (2 - \\sqrt{3}) = 4$$
<br>$$\\alpha\\beta = (2 + \\sqrt{3})(2 - \\sqrt{3}) = 4 - 3 = 1$$
<br>$$x^2 - 4x + 1 = 0$$</p>
</div>
"""
    },
    {
        "title": "Applications: Optimization and Real-World Problems",
        "body": """
<h3>Optimization: Finding Maxima and Minima</h3>
<p>Since a quadratic function has a unique extremum at its vertex, it naturally solves optimization problems.</p>

<div class="example-box">
<h4>Example 8: Maximizing Area</h4>
<p><strong>Problem:</strong> A farmer has 100 meters of fencing to enclose a rectangular field against a river. What dimensions maximize the area?</p>
<p><strong>Solution:</strong></p>
<p>Let x = width perpendicular to river, y = length parallel to river</p>
<p>Constraint: 2x + y = 100</p>
<p>Area: A = xy = x(100 - 2x) = 100x - 2x²</p>
<p>This has a = -2 < 0, so maximum at:</p>
<p>$$x = -\\frac{100}{2(-2)} = 25 \\text{ meters}$$
<br>$$y = 100 - 2(25) = 50 \\text{ meters}$$
<br>$$A_{\\max} = 25 \\times 50 = 1250 \\text{ m}^2$$</p>
</div>

<h3>Projectile Motion</h3>
<p>The height of a projectile launched vertically with initial speed v₀ is:</p>
<div class="formula-box">
<p>$$h(t) = -\\frac{1}{2}gt^2 + v_0 t + h_0$$</p>
</div>
<p>where g ≈ 9.8 m/s² and h₀ is the initial height.</p>

<div class="example-box">
<h4>Example 9: Time to Impact</h4>
<p><strong>Problem:</strong> A ball is thrown upward from ground level with initial velocity 20 m/s. When does it return to ground level?</p>
<p><strong>Solution:</strong></p>
<p>$$h(t) = -5t^2 + 20t = 0$$
<br>$$5t(4 - t) = 0$$
<br>$$t = 0 \\text{ or } t = 4\\text{ seconds}$$</p>
<p>Maximum height at t = 2 s: h(2) = -5(4) + 20(2) = 20 m</p>
</div>

<h3>Economics: Revenue Maximization</h3>
<div class="example-box">
<h4>Example 10: Optimal Pricing</h4>
<p><strong>Problem:</strong> Weekly demand is q = 500 - 2p units at price p dollars. Maximize revenue.</p>
<p><strong>Solution:</strong></p>
<p>$$R(p) = p(500 - 2p) = 500p - 2p^2$$
<br>Maximum at \\(p = -\\frac{500}{2(-2)} = 125\\text{ dollars}$$
<br>$$q = 500 - 2(125) = 250\\text{ units}$$
<br>$$R_{\\max} = 31,250\\text{ dollars}$$</p>
</div>
"""
    },
    {
        "title": "Graphical Solutions and Discriminant Analysis",
        "body": """
<h3>Connection Between Algebra and Geometry</h3>
<p>The solutions to ax² + bx + c = 0 are the x-coordinates where the parabola y = ax² + bx + c crosses the x-axis (where y = 0).</p>

<h3>Case Analysis Using the Discriminant</h3>

<p><strong>Case 1: Δ > 0 (Two distinct real roots)</strong></p>
<p>The parabola intersects the x-axis at two distinct points.</p>

<p><strong>Case 2: Δ = 0 (One repeated real root)</strong></p>
<p>The parabola is tangent to the x-axis at one point. The quadratic is a perfect square: a(x - α)².</p>

<p><strong>Case 3: Δ < 0 (No real roots)</strong></p>
<p>The parabola does not intersect the x-axis. All roots are complex conjugates. The quadratic is always positive (if a > 0) or always negative (if a < 0).</p>

<h3>Sign Analysis</h3>
<p>For a quadratic f(x) = ax² + bx + c, knowing the roots and the sign of a tells us when f(x) > 0 and when f(x) < 0.</p>

<div class="example-box">
<h4>Example 11: Sign Analysis</h4>
<p><strong>Problem:</strong> Determine the sign of f(x) = -2x² + 8x - 6</p>
<p><strong>Solution:</strong> Factoring: -2x² + 8x - 6 = -2(x-1)(x-3)</p>
<p>Since a = -2 < 0, the parabola opens downward:</p>
<ul>
  <li>f(x) > 0 when 1 < x < 3 (between the roots)</li>
  <li>f(x) < 0 when x < 1 or x > 3 (outside the roots)</li>
  <li>f(x) = 0 when x = 1 or x = 3</li>
</ul>
</div>

<h3>Summary Table</h3>
<table style="width:100%; border-collapse: collapse; margin:15px 0;">
  <tr style="background-color:#f0f0f0; color:#1a1a2e;">
    <th style="border:1px solid #ddd; padding:10px;"><strong>Discriminant</strong></th>
    <th style="border:1px solid #ddd; padding:10px;"><strong>Nature of Roots</strong></th>
    <th style="border:1px solid #ddd; padding:10px;"><strong>Graph Behavior</strong></th>
  </tr>
  <tr>
    <td style="border:1px solid #ddd; padding:10px;">Δ > 0</td>
    <td style="border:1px solid #ddd; padding:10px;">Two distinct real roots</td>
    <td style="border:1px solid #ddd; padding:10px;">Crosses x-axis twice</td>
  </tr>
  <tr style="background-color:#f9f9f9; color:#1a1a2e;">
    <td style="border:1px solid #ddd; padding:10px;">Δ = 0</td>
    <td style="border:1px solid #ddd; padding:10px;">One repeated real root</td>
    <td style="border:1px solid #ddd; padding:10px;">Tangent to x-axis</td>
  </tr>
  <tr>
    <td style="border:1px solid #ddd; padding:10px;">Δ < 0</td>
    <td style="border:1px solid #ddd; padding:10px;">Two complex conjugate roots</td>
    <td style="border:1px solid #ddd; padding:10px;">No x-intercepts</td>
  </tr>
</table>
"""
    }
]
