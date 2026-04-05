TITLE = "Lines in 3D Space"

SECTIONS = [
    {
        "title": "Vector Equation of a Line",
        "body": """
<div class="concept-box">
<h3>Parametric Vector Form</h3>
<p>A line passing through point A with direction vector <strong>d</strong> can be written as:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{r} = \\mathbf{a} + t\\mathbf{d}, \\quad t \\in \\mathbb{R}</p>
<p>where <strong>a</strong> is the position vector of point A, and <strong>d</strong> is the direction vector. The parameter t determines position along the line.</p>
</div>

<h3>Component Form</h3>
<p>If A = (a₁, a₂, a₃) and <strong>d</strong> = (d₁, d₂, d₃), then:</p>
<p style="text-align: center; font-weight: bold;">(x, y, z) = (a_1, a_2, a_3) + t(d_1, d_2, d_3)</p>

<h3>Parametric Form (Scalar Equations)</h3>
<p>Breaking the vector equation into components:</p>
<p style="text-align: center; font-weight: bold;">x = a_1 + td_1 \\quad y = a_2 + td_2 \\quad z = a_3 + td_3</p>

<div class="worked-example">
<h4>Example 1: Line Through a Point with Given Direction</h4>
<p>Find the vector equation of the line through P(2, 3, -1) with direction vector <strong>d</strong> = (1, -2, 3)</p>
<p><strong>Solution:</strong></p>
<p><strong>r</strong> = (2, 3, -1) + t(1, -2, 3)</p>
<p><strong>Parametric form:</strong></p>
<p>x = 2 + t, y = 3 - 2t, z = -1 + 3t</p>
</div>

<h3>Cartesian Form</h3>
<p>Eliminating the parameter t from the parametric equations gives the Cartesian form:</p>
<p style="text-align: center; font-weight: bold;">\\frac{x - a_1}{d_1} = \\frac{y - a_2}{d_2} = \\frac{z - a_3}{d_3}</p>
<p>This represents the line as the intersection of two planes.</p>

<div class="warning-box">
<h4>Division by Zero</h4>
<p>If a direction component is zero (e.g., d₁ = 0), the line is parallel to a coordinate plane. In this case, write that component as a constant (e.g., x = a₁) rather than dividing by zero.</p>
</div>
"""
    },
    {
        "title": "Line Through Two Points",
        "body": """
<h3>Finding the Direction Vector</h3>
<p>To find the equation of a line through two distinct points P and Q, use the direction vector:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{d} = \\mathbf{PQ} = \\mathbf{Q} - \\mathbf{P}</p>

<div class="worked-example">
<h4>Example 2: Line Through Two Points</h4>
<p>Find the equation of the line through P(1, 2, 3) and Q(4, 5, 6)</p>
<p><strong>Solution:</strong></p>
<p>Direction vector: <strong>d</strong> = Q - P = (3, 3, 3)</p>
<p><strong>Vector equation:</strong> <strong>r</strong> = (1, 2, 3) + t(3, 3, 3)</p>
<p>Or equivalently: <strong>r</strong> = (1, 2, 3) + t(1, 1, 1) (using a scalar multiple of <strong>d</strong>)</p>
<p><strong>Cartesian form:</strong> $\\frac{x - 1}{1} = \\frac{y - 2}{1} = \\frac{z - 3}{1}$</p>
<p>Simplified: x - 1 = y - 2 = z - 3</p>
</div>

<h3>Checking if a Point Lies on a Line</h3>
<p>To determine if point R lies on the line <strong>r</strong> = <strong>a</strong> + t<strong>d</strong>:</p>
<ol>
<li>Set R = (x₀, y₀, z₀) equal to <strong>a</strong> + t<strong>d</strong></li>
<li>Solve for t in each component equation</li>
<li>If all three equations give the same value of t, the point lies on the line</li>
</ol>

<div class="worked-example">
<h4>Example 3: Testing if Point is on Line</h4>
<p>Does point (7, 8, 9) lie on the line <strong>r</strong> = (1, 2, 3) + t(1, 1, 1)?</p>
<p><strong>Solution:</strong></p>
<p>Setting (7, 8, 9) = (1, 2, 3) + t(1, 1, 1):</p>
<p>7 = 1 + t → t = 6</p>
<p>8 = 2 + t → t = 6</p>
<p>9 = 3 + t → t = 6</p>
<p>All three equations give t = 6, so <strong>yes, the point lies on the line</strong>.</p>
</div>
"""
    },
    {
        "title": "Intersection and Relationships Between Lines",
        "body": """
<h3>Types of Line Relationships in 3D</h3>
<p>Two lines in 3D can have four possible relationships:</p>

<h4>1. Intersecting Lines</h4>
<p>The lines meet at exactly one point. The system of equations has a unique solution.</p>

<h4>2. Parallel Lines</h4>
<p>The lines have the same direction vector (or scalar multiples) and do not intersect.</p>
<p>Condition: <strong>d</strong>₁ = k<strong>d</strong>₂ for some scalar k ≠ 0</p>

<h4>3. Coincident Lines</h4>
<p>The lines are actually the same line. They have the same direction and share all points.</p>

<h4>4. Skew Lines</h4>
<p>The lines do not intersect and are not parallel. They exist in different "layers" of 3D space.</p>

<h3>Finding Intersection Points</h3>
<p>For lines <strong>r</strong> = <strong>a</strong>₁ + s<strong>d</strong>₁ and <strong>r</strong> = <strong>a</strong>₂ + t<strong>d</strong>₂, set them equal:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{a}_1 + s\\mathbf{d}_1 = \\mathbf{a}_2 + t\\mathbf{d}_2</p>
<p>This gives three equations in two unknowns (s and t). If consistent with a unique solution, the lines intersect.</p>

<div class="worked-example">
<h4>Example 4: Testing for Intersection</h4>
<p>Do the lines <strong>r</strong> = (1, 2, 3) + s(1, 1, 1) and <strong>r</strong> = (2, 0, 1) + t(1, -1, 1) intersect?</p>
<p><strong>Solution:</strong></p>
<p>Setting equal: (1+s, 2+s, 3+s) = (2+t, -t, 1+t)</p>
<p>Component equations:</p>
<p>1 + s = 2 + t → s - t = 1 ... (1)</p>
<p>2 + s = -t → s + t = -2 ... (2)</p>
<p>3 + s = 1 + t → s - t = -2 ... (3)</p>
<p>From (1): s - t = 1</p>
<p>From (3): s - t = -2</p>
<p>These are contradictory, so the lines do <strong>not intersect</strong> (they are skew).</p>
</div>

<h3>Determining Line Relationships</h3>
<p><strong>Step 1:</strong> Check if direction vectors are parallel (scalar multiples)</p>
<p><strong>Step 2:</strong> If parallel, check if lines are the same or distinct</p>
<p><strong>Step 3:</strong> If not parallel, solve the system to see if they intersect or are skew</p>
"""
    }
]
