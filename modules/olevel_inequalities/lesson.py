SECTIONS = [
    {
        "title": "Linear Inequalities: Properties and Solutions",
        "body": """
<h3>Definition and Axioms</h3>
<p>An inequality compares expressions using &lt;, &gt;, ≤, or ≥. Key property:</p>
<p><strong>If a < b, then a + c < b + c (addition axiom)</strong></p>
<p><strong>If a < b and c > 0, then ac < bc (multiplication axiom)</strong></p>
<p><strong>If a < b and c < 0, then ac > bc (reverse inequality when multiplying by negative)</strong></p>

<h3>Solving Linear Inequalities</h3>
<p>Solve as equations, but reverse the inequality sign if multiplying/dividing by a negative.</p>

<div class="example-box">
<h4>Example 1: Solving Inequalities</h4>
<p>Solve -2x + 5 > 11</p>
<p>-2x > 6 (subtract 5)</p>
<p>x < -3 (divide by -2, reverse)</p>
<p>Solution: x ∈ (-∞, -3)</p>
</div>

<h3>Interval Notation</h3>
<ul>
  <li>(a, b): Open interval, a < x < b</li>
  <li>[a, b]: Closed interval, a ≤ x ≤ b</li>
  <li>[a, b): Half-open, a ≤ x < b</li>
  <li>(a, ∞): Open ray, x > a</li>
</ul>

<h3>Compound Inequalities</h3>
<p>And (∩): Both conditions true</p>
<p>Or (∪): At least one condition true</p>

<div class="example-box">
<h4>Example 2: Compound Inequality</h4>
<p>Solve -3 ≤ 2x + 1 < 5</p>
<p>-4 ≤ 2x < 4 (subtract 1)</p>
<p>-2 ≤ x < 2 (divide by 2)</p>
<p>Solution: x ∈ [-2, 2)</p>
</div>
"""
    },
    {
        "title": "Quadratic Inequalities and Sign Analysis",
        "body": """
<h3>Solving Quadratic Inequalities</h3>
<p>Steps: (1) Find roots of f(x) = 0, (2) Analyze sign on each interval</p>

<div class="example-box">
<h4>Example 3: Quadratic Inequality</h4>
<p>Solve x² - 5x + 6 > 0</p>
<p>(x - 2)(x - 3) > 0</p>
<p>Roots at x = 2, 3. Test intervals:</p>
<p>x < 2: (+)(−) = negative ✗</p>
<p>2 < x < 3: (+)(+) = negative ✗</p>
<p>x > 3: (+)(+) = positive ✓</p>
<p>Solution: x ∈ (−∞, 2) ∪ (3, ∞)</p>
</div>

<h3>Rational Inequalities</h3>
<p>Find zeros of numerator and denominator. Analyze sign on each interval.</p>

<div class="example-box">
<h4>Example 4: Rational Inequality</h4>
<p>Solve (x+2)/(x-3) ≤ 0</p>
<p>Critical points: x = -2, x = 3</p>
<p>x < -2: (−)/(−) = positive ✗</p>
<p>-2 < x < 3: (+)/(−) = negative ✓</p>
<p>x > 3: (+)/(+) = positive ✗</p>
<p>Solution: x ∈ [-2, 3)</p>
</div>
"""
    },
    {
        "title": "Absolute Value Inequalities",
        "body": """
<h3>Definition and Properties</h3>
<p>|x| = x if x ≥ 0; |x| = -x if x < 0</p>

<h3>Key Formulas</h3>
<p>|x| < a ⟺ -a < x < a (a > 0)</p>
<p>|x| > a ⟺ x < -a or x > a (a > 0)</p>

<div class="example-box">
<h4>Example 5: Absolute Value Inequality</h4>
<p>Solve |2x - 3| ≤ 5</p>
<p>-5 ≤ 2x - 3 ≤ 5</p>
<p>-2 ≤ 2x ≤ 8</p>
<p>-1 ≤ x ≤ 4</p>
<p>Solution: x ∈ [-1, 4]</p>
</div>
"""
    },
    {
        "title": "Systems of Inequalities and Regions",
        "body": """
<h3>Linear Inequalities in Two Variables</h3>
<p>ax + by > c represents a half-plane. Boundary is ax + by = c</p>

<p><strong>Steps:</strong></p>
<ol>
  <li>Graph the boundary line (dashed if strict, solid if ≤ or ≥)</li>
  <li>Test a point not on the line</li>
  <li>Shade the appropriate half-plane</li>
</ol>

<h3>Systems of Inequalities</h3>
<p>Solution is the intersection of all half-planes</p>

<div class="example-box">
<h4>Example 6: System of Inequalities</h4>
<p>Solve: x + y ≤ 4 and x ≥ 0 and y ≥ 0</p>
<p>This is the region bounded by x = 0, y = 0, and x + y = 4 (triangle with vertices (0,0), (4,0), (0,4))</p>
</div>
"""
    },
    {
        "title": "Applications and Real-World Constraints",
        "body": """
<h3>Linear Programming</h3>
<p>Maximize/minimize an objective function subject to linear constraints</p>

<div class="example-box">
<h4>Example 7: Production Problem</h4>
<p>Factory makes chairs (profit $8) and tables (profit $12). Constraints:
<br>- Wood: 5 chairs + 10 tables ≤ 200 units
<br>- Labor: 1 chair + 2 tables ≤ 40 hours
<br>- x ≥ 0, y ≥ 0</p>
<p>Optimal solution at corner points of feasible region</p>
</div>

<h3>Inequalities in Science</h3>
<p>Temperature ranges, measurement tolerances, pH scales all use inequalities</p>
"""
    }
]
