TITLE = "What is a System of Linear Equations?"

SECTIONS = [
    {
        "title": "Linear Equation (First-Principles Definition)",
        "body": """
<div class="concept-box">
<h3>Linear Equation</h3>
<p>A <strong>linear equation in n variables</strong> \\(x_1, x_2, \\ldots, x_n\\) is an equation of the form:</p>

$$a_1 x_1 + a_2 x_2 + \\cdots + a_n x_n = b$$

<p>where \\(a_1, a_2, \\ldots, a_n, b \\in \\mathbb{R}\\) (or \\(\\mathbb{C}\\)), and "linear" means each variable appears with exponent exactly 1 (no squares, products, or transcendental functions).</p>
</div>

<h4>Key Properties</h4>
<ul>
<li><strong>First-degree:</strong> Each variable has exponent 1</li>
<li><strong>No products:</strong> No terms like \\(xy\\) or \\(x^2\\)</li>
<li><strong>No transcendental functions:</strong> No \\(\\sin(x)\\), \\(e^x\\), \\(\\ln(x)\\)</li>
<li><strong>Constant coefficients:</strong> \\(a_i\\) and \\(b\\) are fixed scalars</li>
</ul>

<div class="worked-example">
<h4>Examples of Linear Equations</h4>
<p><strong>Linear:</strong></p>
<ul>
<li>\\(2x + 3y = 5\\) (two variables)</li>
<li>\\(3x - 2y + 7z = 1\\) (three variables)</li>
<li>\\(x_1 + x_2 + \\cdots + x_n = 0\\) (n variables)</li>
</ul>

<p><strong>Non-Linear (not linear):</strong></p>
<ul>
<li>\\(x^2 + y = 5\\) (exponent 2)</li>
<li>\\(xy + z = 1\\) (product of variables)</li>
<li>\\(\\sin(x) + y = 2\\) (transcendental function)</li>
</ul>
</div>
"""
    },
    {
        "title": "System of Linear Equations",
        "body": """
<div class="concept-box">
<h3>Definition: System of Linear Equations</h3>
<p>A <strong>system of m linear equations in n unknowns</strong> is a collection:</p>

$$\\begin{align}
a_{11}x_1 + a_{12}x_2 + \\cdots + a_{1n}x_n &= b_1 \\\\
a_{21}x_1 + a_{22}x_2 + \\cdots + a_{2n}x_n &= b_2 \\\\
&\\vdots \\\\
a_{m1}x_1 + a_{m2}x_2 + \\cdots + a_{mn}x_n &= b_m
\\end{align}$$

<p>A <strong>solution</strong> is a vector \\((x_1^*, x_2^*, \\ldots, x_n^*) \\in \\mathbb{R}^n\\) that satisfies <em>all m equations simultaneously</em>.</p>
</div>

<h4>Understanding the Notation</h4>
<ul>
<li>\\(m\\) = number of equations</li>
<li>\\(n\\) = number of unknowns (variables)</li>
<li>\\(a_{ij}\\) = coefficient of variable \\(x_j\\) in equation \\(i\\)</li>
<li>\\(b_i\\) = constant term (right-hand side) of equation \\(i\\)</li>
</ul>

<div class="worked-example">
<h4>Simple Example: 2 Equations, 2 Unknowns</h4>
$$\\begin{align}
2x + 3y &= 8 \\\\
x - y &= 1
\\end{align}$$

<p>Here: \\(m = 2\\), \\(n = 2\\).</p>

<p><strong>Solving by substitution:</strong> From equation 2, \\(x = y + 1\\). Substitute into equation 1:</p>
$$2(y + 1) + 3y = 8$$
$$2y + 2 + 3y = 8$$
$$5y = 6$$
$$y = \\frac{6}{5}$$

<p>Therefore, \\(x = \\frac{6}{5} + 1 = \\frac{11}{5}\\).</p>

<p><strong>Solution:</strong> \\((x, y) = \\left(\\frac{11}{5}, \\frac{6}{5}\\right)\\)</p>

<p><strong>Verification:</strong>
<ul>
<li>Equation 1: \\(2 \\cdot \\frac{11}{5} + 3 \\cdot \\frac{6}{5} = \\frac{22 + 18}{5} = \\frac{40}{5} = 8\\) ✓</li>
<li>Equation 2: \\(\\frac{11}{5} - \\frac{6}{5} = \\frac{5}{5} = 1\\) ✓</li>
</ul>
</p>
</div>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>A solution to a system must satisfy <em>all</em> equations, not just one. Finding a value that works for one equation but not others is not a solution.</p>
</div>
"""
    },
    {
        "title": "Geometric Interpretation in 2D",
        "body": """
<h3>Lines in the Plane</h3>
<p>In \\(\\mathbb{R}^2\\), each linear equation \\(ax + by = c\\) represents a <strong>line</strong>. The solution to a system is the <strong>geometric intersection</strong> of all lines.</p>

<svg viewBox="0 0 400 350" style="margin: 20px 0">
  <!-- Grid -->
  <g stroke='#30363d' stroke-width="0.5">
    <line x1="0" y1="175" x2="400" y2="175" stroke='#161b22'/>
    <line x1="200" y1="0" x2="200" y2="350" stroke='#161b22'/>
  </g>

  <!-- Line 1: 2x + 3y = 8 (correctly calculated) -->
  <line x1="150" y1="8" x2="400" y2="175" stroke='#4f8ef7' stroke-width="2.5"/>

  <!-- Line 2: x - y = 1 (correctly calculated) -->
  <line x1="100" y1="325" x2="400" y2="25" stroke='#4f8ef7' stroke-width="2.5"/>

  <!-- Intersection point: x=2.2, y=1.2 -->
  <circle cx="310" cy="115" r="5" fill='#4f8ef7' stroke='currentColor' stroke-width="1"/>

  <!-- Labels -->
  <text x="10" y="25" font-size='13' fill='#4f8ef7' font-weight='bold'>2x + 3y = 8</text>
  <text x="10" y="45" font-size='13' fill='#4f8ef7' font-weight='bold'>x - y = 1</text>
  <text x="315" y="105" font-size='11' fill='currentColor' font-weight='bold'>Solution</text>

  <!-- Axis labels -->
  <text x="370" y="190" font-size='12' fill='currentColor'>x</text>
  <text x="210" y="20" font-size='12' fill='currentColor'>y</text>
</svg>

<div class="concept-box">
<h4>Three Geometric Cases (2D)</h4>
<p><strong>Case 1 (Unique Solution):</strong> Two non-parallel lines intersect at exactly one point. The system has a unique solution.</p>

<p><strong>Case 2 (Infinitely Many Solutions):</strong> Two lines are identical (the same line). Every point on the line is a solution.</p>

<p><strong>Case 3 (No Solution):</strong> Two lines are parallel but distinct. They never intersect.</p>
</div>

<div class="success-box">
<h4>Higher Dimensions (3D and Beyond)</h4>
<p>In \\(\\mathbb{R}^3\\), each linear equation \\(ax + by + cz = d\\) represents a <strong>plane</strong>. The solution is the intersection of planes. In higher dimensions, we get hyperplanes, but the geometric intuition remains the same.</p>
</div>
"""
    }
]
