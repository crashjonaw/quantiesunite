TITLE = "Planes in 3D Space"

SECTIONS = [
    {
        "title": "Vector Equation of a Plane",
        "body": """
<div class="concept-box">
<h3>Normal Vector Definition</h3>
<p>A plane is uniquely determined by a point A and a vector <strong>n</strong> perpendicular to the plane (called the <strong>normal vector</strong>).</p>
</div>

<h3>Vector Equation Form</h3>
<p>The vector equation of a plane containing point A with normal vector \(\\mathbf{n}\) is:</p>
<p style="text-align: center; font-weight: bold;">\(\\mathbf{n} \\cdot (\\mathbf{r} - \\mathbf{a}) = 0\)</p>
<p>where \(\\mathbf{r} = (x, y, z)\) is any point on the plane.</p>

<p>This expresses the condition that the vector from A to any point on the plane is perpendicular to the normal.</p>

<h3>Cartesian Equation</h3>
<p>If \(\\mathbf{n} = (a, b, c)\) and \(A = (x_0, y_0, z_0)\), expanding the vector equation gives:</p>
<p style="text-align: center; font-weight: bold;">\(a(x - x_0) + b(y - y_0) + c(z - z_0) = 0\)</p>

<p>This simplifies to the standard form:</p>
<p style="text-align: center; font-weight: bold;">\(ax + by + cz = d\)</p>
<p>where \(d = ax_0 + by_0 + cz_0\)</p>

<div class="worked-example">
<h4>Example 1: Plane with Given Normal and Point</h4>
<p>Find the equation of the plane with normal \(\\mathbf{n} = (2, -3, 1)\) passing through P(1, 2, -1)</p>
<p><strong>Solution:</strong></p>
<p>\(2(x - 1) - 3(y - 2) + 1(z + 1) = 0\)</p>
<p>\(2x - 2 - 3y + 6 + z + 1 = 0\)</p>
<p>\(2x - 3y + z =\) <strong>-5</strong></p>
</div>
"""
    },
    {
        "title": "Plane Through Three Points",
        "body": """
<h3>Finding the Normal Vector</h3>
<p>Given three non-collinear points P, Q, and R on the plane, find two vectors in the plane:</p>
<p style="text-align: center; font-weight: bold;">\(\\mathbf{u} = \overrightarrow{PQ}, \quad \\mathbf{v} = \overrightarrow{PR}\)</p>

<p>The normal vector is their cross product:</p>
<p style="text-align: center; font-weight: bold;">\(\\mathbf{n} = \\mathbf{u} \\times \\mathbf{v}\)</p>

<p>This vector is perpendicular to both \(\\mathbf{u}\) and \(\\mathbf{v}\), hence perpendicular to the plane.</p>

<div class="worked-example">
<h4>Example 2: Plane Through Three Points</h4>
<p>Find the equation of the plane through P(1, 0, 0), Q(0, 2, 0), R(0, 0, 3)</p>
<p><strong>Solution:</strong></p>
<p>\(\overrightarrow{PQ} = (-1, 2, 0)\), \(\overrightarrow{PR} = (-1, 0, 3)\)</p>
<p>\(\\mathbf{n} = \overrightarrow{PQ} \\times \overrightarrow{PR}\):</p>
<p>\(= (2 \\cdot 3 - 0 \\cdot 0,\; 0 \\cdot (-1) - (-1) \\cdot 3,\; (-1) \\cdot 0 - 2 \\cdot (-1))\)</p>
<p>\(= (6, 3, 2)\)</p>
<p>Plane equation: \(6(x - 1) + 3(y - 0) + 2(z - 0) = 0\)</p>
<p>Simplifying: <strong>\(6x + 3y + 2z = 6\)</strong></p>
</div>

<h3>Verification</h3>
<p>Check that all three points satisfy the plane equation:</p>
<ul>
<li>P(1, 0, 0): \(6(1) + 3(0) + 2(0) = 6\) ✓</li>
<li>Q(0, 2, 0): \(6(0) + 3(2) + 2(0) = 6\) ✓</li>
<li>R(0, 0, 3): \(6(0) + 3(0) + 2(3) = 6\) ✓</li>
</ul>
"""
    },
    {
        "title": "Distance from Point to Plane",
        "body": """
<h3>Distance Formula</h3>
<p>The perpendicular distance from point \(P(x_0, y_0, z_0)\) to the plane \(ax + by + cz = d\) is:</p>
<p style="text-align: center; font-weight: bold;">\(\\text{distance} = \\frac{|ax_0 + by_0 + cz_0 - d|}{\\sqrt{a^2 + b^2 + c^2}}\)</p>

<p>The denominator is the magnitude of the normal vector \(\\mathbf{n} = (a, b, c)\).</p>

<h3>Geometric Interpretation</h3>
<p>The distance is the length of the perpendicular from the point to the plane. The perpendicular direction is given by the normal vector.</p>

<div class="worked-example">
<h4>Example 3: Point-to-Plane Distance</h4>
<p>Find the distance from P(1, 2, 3) to the plane \(2x - y + 2z = 9\)</p>
<p><strong>Solution:</strong></p>
<p>Distance \(= \\frac{|2(1) - 1(2) + 2(3) - 9|}{\\sqrt{2^2 + (-1)^2 + 2^2}}\)</p>
<p>\(= \\frac{|2 - 2 + 6 - 9|}{\\sqrt{9}}\)</p>
<p>\(= \\frac{|-3|}{3} =\) <strong>1</strong></p>
</div>

<div class="warning-box">
<h4>Plane Equation Format</h4>
<p>Make sure the plane equation is in standard form \(ax + by + cz = d\) before applying the distance formula. If your equation is \(a(x - x_0) + b(y - y_0) + c(z - z_0) = 0\), expand and rearrange first.</p>
</div>

<h3>Distance Between Two Parallel Planes</h3>
<p>If two planes have the same normal vector and equations \(ax + by + cz = d_1\) and \(ax + by + cz = d_2\), the distance between them is:</p>
<p style="text-align: center; font-weight: bold;">\(\\text{distance} = \\frac{|d_1 - d_2|}{\\sqrt{a^2 + b^2 + c^2}}\)</p>

<div class="worked-example">
<h4>Example 4: Distance Between Parallel Planes</h4>
<p>Find the distance between the parallel planes \(2x - y + 2z = 9\) and \(2x - y + 2z = 3\)</p>
<p><strong>Solution:</strong></p>
<p>Distance \(= \\frac{|9 - 3|}{\\sqrt{4 + 1 + 4}} = \\frac{6}{3} =\) <strong>2</strong></p>
</div>
"""
    },
    {
        "title": "Intersection of Line and Plane",
        "body": """
<h3>Intersection Procedure</h3>
<p>To find where line \(\\mathbf{r} = \\mathbf{a} + t\\mathbf{d}\) intersects plane \(ax + by + cz = d\):</p>
<ol>
<li>Substitute the parametric equations into the plane equation</li>
<li>Solve for the parameter t</li>
<li>Substitute t back into the line equation to find the intersection point</li>
</ol>

<h3>Three Cases</h3>

<h4>Case 1: Unique Intersection (Transverse)</h4>
<p>If \(\\mathbf{n} \\cdot \\mathbf{d} \\neq 0\), the line intersects the plane at exactly one point.</p>

<h4>Case 2: Line in Plane</h4>
<p>If \(\\mathbf{n} \\cdot \\mathbf{d} = 0\) and the line passes through a point on the plane, the line lies entirely in the plane (infinitely many intersections).</p>

<h4>Case 3: Parallel (No Intersection)</h4>
<p>If \(\\mathbf{n} \\cdot \\mathbf{d} = 0\) but the line doesn't pass through the plane, they are parallel (no intersection).</p>

<div class="worked-example">
<h4>Example 5: Line-Plane Intersection</h4>
<p>Find the intersection of the line \(\\mathbf{r} = (1, 0, 1) + t(1, 2, -1)\) and plane \(2x + y - z = 3\)</p>
<p><strong>Solution:</strong></p>
<p>Substitute parametric form into plane:</p>
<p>\(2(1 + t) + (0 + 2t) - (1 - t) = 3\)</p>
<p>\(2 + 2t + 2t - 1 + t = 3\)</p>
<p>\(1 + 5t = 3\)</p>
<p>\(t = 2/5\)</p>
<p>Intersection point: \(\\mathbf{r}(2/5) = (1 + 2/5,\; 0 + 4/5,\; 1 - 2/5) =\) <strong>(7/5, 4/5, 3/5)</strong></p>
</div>

<div class="success-box">
<h4>Key Insight</h4>
<p>The condition \(\\mathbf{n} \\cdot \\mathbf{d} = 0\) tells us the line is parallel to the plane (perpendicular to the normal).</p>
</div>
"""
    }
]
