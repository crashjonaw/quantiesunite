TITLE = "Angles and Distances Between Lines and Planes"

SECTIONS = [
    {
        "title": "Angles Between Lines",
        "body": """
<h3>Angle Between Two Lines</h3>
<p>The angle \(\theta\) between two lines with direction vectors \(\mathbf{d}_1\) and \(\mathbf{d}_2\) is given by:</p>
<p style="text-align: center; font-weight: bold;">\(\cos(\theta) = \frac{|\mathbf{d}_1 \cdot \mathbf{d}_2|}{|\mathbf{d}_1| |\mathbf{d}_2|}\)</p>

<p><strong>Note:</strong> We use the absolute value of the dot product because we want the acute angle (\(0° \leq \theta \leq 90°\)) between the lines, regardless of direction orientation.</p>

<h3>Parallel and Perpendicular Lines</h3>

<h4>Parallel:</h4>
<p>Direction vectors are scalar multiples: \(\mathbf{d}_1 = k\mathbf{d}_2\) for some \(k \neq 0\). This means \(\cos(\theta) = 1\), so \(\theta = 0°\).</p>

<h4>Perpendicular:</h4>
<p>Direction vectors are orthogonal: \(\mathbf{d}_1 \cdot \mathbf{d}_2 = 0\). This means \(\cos(\theta) = 0\), so \(\theta = 90°\).</p>

<div class="worked-example">
<h4>Example 1: Angle Between Lines</h4>
<p>Find the angle between lines with direction vectors \(\mathbf{d}_1 = (1, 2, 2)\) and \(\mathbf{d}_2 = (2, 1, -2)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{d}_1 \cdot \mathbf{d}_2 = (1)(2) + (2)(1) + (2)(-2) = 2 + 2 - 4 = 0\)</p>
<p>Since the dot product is zero, the lines are <strong>perpendicular</strong>: \(\theta =\) <strong>90°</strong></p>
</div>
"""
    },
    {
        "title": "Angle Between a Line and a Plane",
        "body": """
<h3>Definition</h3>
<p>The angle \(\alpha\) between a line and a plane is the angle between the line and its orthogonal projection onto the plane. This is the complement of the angle between the line's direction vector and the plane's normal vector.</p>

<h3>Formula</h3>
<p>If the line has direction vector \(\mathbf{d}\) and the plane has normal vector \(\mathbf{n}\):</p>
<p style="text-align: center; font-weight: bold;">\(\sin(\alpha) = \frac{|\mathbf{d} \cdot \mathbf{n}|}{|\mathbf{d}| |\mathbf{n}|}\)</p>

<p><strong>Why sine?</strong> The angle between \(\mathbf{d}\) and \(\mathbf{n}\) is complementary to \(\alpha\), so \(\sin(\alpha) = \cos(\text{angle between } \mathbf{d} \text{ and } \mathbf{n})\).</p>

<h3>Special Cases</h3>

<h4>Line parallel to plane:</h4>
<p>\(\mathbf{d} \cdot \mathbf{n} = 0\), so \(\sin(\alpha) = 0\) and \(\alpha = 0°\)</p>

<h4>Line perpendicular to plane:</h4>
<p>\(\mathbf{d}\) is parallel to \(\mathbf{n}\), so \(\sin(\alpha) = 1\) and \(\alpha = 90°\)</p>

<div class="worked-example">
<h4>Example 2: Angle Between Line and Plane</h4>
<p>Find the angle between the line \(\mathbf{r} = (1, 2, 3) + t(1, 1, 2)\) and the plane \(2x - y + z = 5\)</p>
<p><strong>Solution:</strong></p>
<p>Direction vector: \(\mathbf{d} = (1, 1, 2)\)</p>
<p>Normal vector: \(\mathbf{n} = (2, -1, 1)\)</p>
<p>\(\mathbf{d} \cdot \mathbf{n} = (1)(2) + (1)(-1) + (2)(1) = 2 - 1 + 2 = 3\)</p>
<p>\(|\mathbf{d}| = \sqrt{1 + 1 + 4} = \sqrt{6}\)</p>
<p>\(|\mathbf{n}| = \sqrt{4 + 1 + 1} = \sqrt{6}\)</p>
<p>\(\sin(\alpha) = \frac{|3|}{\sqrt{6} \cdot \sqrt{6}} = \frac{3}{6} = \frac{1}{2}\)</p>
<p>\(\alpha =\) <strong>30°</strong> or \(\pi/6\) radians</p>
</div>
"""
    },
    {
        "title": "Distance Between Skew Lines",
        "body": """
<h3>Skew Lines Definition</h3>
<p>Two lines are <strong>skew</strong> if they do not intersect and are not parallel. In 3D, this is unique to lines in three-dimensional space.</p>

<h3>Distance Formula</h3>
<p>For skew lines \(\mathbf{r} = \mathbf{a}_1 + s\mathbf{d}_1\) and \(\mathbf{r} = \mathbf{a}_2 + t\mathbf{d}_2\), the perpendicular distance is:</p>
<p style="text-align: center; font-weight: bold;">\(\text{distance} = \frac{|(\mathbf{a}_2 - \mathbf{a}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{|\mathbf{d}_1 \times \mathbf{d}_2|}\)</p>

<p>The denominator is the magnitude of the cross product, which gives a vector perpendicular to both lines. This represents the common perpendicular direction.</p>

<h3>Geometric Interpretation</h3>
<p>The shortest distance between two skew lines occurs along the unique line perpendicular to both.</p>

<div class="worked-example">
<h4>Example 3: Distance Between Skew Lines</h4>
<p>Find the distance between \(\mathbf{r} = (1, 0, 0) + s(0, 1, 1)\) and \(\mathbf{r} = (0, 2, 0) + t(1, 0, 1)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{a}_2 - \mathbf{a}_1 = (-1, 2, 0)\)</p>
<p>\(\mathbf{d}_1 = (0, 1, 1)\), \(\mathbf{d}_2 = (1, 0, 1)\)</p>
<p>\(\mathbf{d}_1 \times \mathbf{d}_2 = (1 \cdot 1 - 1 \cdot 0,\; 1 \cdot 1 - 0 \cdot 1,\; 0 \cdot 0 - 1 \cdot 1) = (1, 1, -1)\)</p>
<p>\(|\mathbf{d}_1 \times \mathbf{d}_2| = \sqrt{1 + 1 + 1} = \sqrt{3}\)</p>
<p>\((\mathbf{a}_2 - \mathbf{a}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2) = (-1, 2, 0) \cdot (1, 1, -1) = -1 + 2 + 0 = 1\)</p>
<p>Distance \(= \frac{|1|}{\sqrt{3}} =\) <strong>\(\sqrt{3}/3\)</strong> or <strong>\(1/\sqrt{3}\)</strong></p>
</div>

<div class="warning-box">
<h4>Verify the Lines are Skew</h4>
<p>Before using this formula, confirm that the lines actually are skew. Check that \(\mathbf{d}_1\) and \(\mathbf{d}_2\) are not parallel and that the lines don't intersect.</p>
</div>
"""
    },
    {
        "title": "Angle Between Two Planes",
        "body": """
<h3>Definition</h3>
<p>The angle between two planes is the angle between their normal vectors. Since normal vectors can point in either direction, we consider the acute angle (\(0° \leq \theta \leq 90°\)).</p>

<h3>Formula</h3>
<p>If two planes have normal vectors \(\mathbf{n}_1\) and \(\mathbf{n}_2\):</p>
<p style="text-align: center; font-weight: bold;">\(\cos(\theta) = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{|\mathbf{n}_1| |\mathbf{n}_2|}\)</p>

<p>The absolute value ensures we get the acute angle.</p>

<h3>Special Cases</h3>

<h4>Parallel planes:</h4>
<p>Normal vectors are scalar multiples: \(\mathbf{n}_1 = k\mathbf{n}_2\). This means \(\cos(\theta) = 1\), so \(\theta = 0°\).</p>

<h4>Perpendicular planes:</h4>
<p>Normal vectors are orthogonal: \(\mathbf{n}_1 \cdot \mathbf{n}_2 = 0\). This means \(\cos(\theta) = 0\), so \(\theta = 90°\).</p>

<div class="worked-example">
<h4>Example 4: Angle Between Planes</h4>
<p>Find the angle between the planes \(2x + y + 2z = 5\) and \(x - 2y + 2z = 3\)</p>
<p><strong>Solution:</strong></p>
<p>Normal vectors: \(\mathbf{n}_1 = (2, 1, 2)\), \(\mathbf{n}_2 = (1, -2, 2)\)</p>
<p>\(\mathbf{n}_1 \cdot \mathbf{n}_2 = (2)(1) + (1)(-2) + (2)(2) = 2 - 2 + 4 = 4\)</p>
<p>\(|\mathbf{n}_1| = \sqrt{4 + 1 + 4} = 3\)</p>
<p>\(|\mathbf{n}_2| = \sqrt{1 + 4 + 4} = 3\)</p>
<p>\(\cos(\theta) = \frac{|4|}{3 \cdot 3} = \frac{4}{9}\)</p>
<p>\(\theta = \arccos(4/9) \approx\) <strong>63.6°</strong></p>
</div>
"""
    },
    {
        "title": "Finding Common Perpendiculars and Shortest Distances",
        "body": """
<h3>Common Perpendicular to Two Skew Lines</h3>
<p>For two skew lines, there exists a unique line that is perpendicular to both. This common perpendicular is parallel to the vector \(\mathbf{d}_1 \times \mathbf{d}_2\).</p>

<p>To find the actual perpendicular line, you need to find the two closest points (one on each line) where the perpendicular intersects.</p>

<h3>Point-Line Distance</h3>
<p>The distance from point P to a line passing through point A with direction \(\mathbf{d}\) is:</p>
<p style="text-align: center; font-weight: bold;">\(\text{distance} = \frac{|(\mathbf{P} - \mathbf{A}) \times \mathbf{d}|}{|\mathbf{d}|}\)</p>

<p>This is found by constructing a parallelogram and using the cross product magnitude to find the height.</p>

<div class="worked-example">
<h4>Example 5: Distance from Point to Line</h4>
<p>Find the distance from P(3, 1, 4) to the line \(\mathbf{r} = (1, 2, 3) + t(1, 1, 1)\)</p>
<p><strong>Solution:</strong></p>
<p>\(A = (1, 2, 3)\), \(\mathbf{d} = (1, 1, 1)\)</p>
<p>\(\mathbf{P} - \mathbf{A} = (2, -1, 1)\)</p>
<p>\((\mathbf{P} - \mathbf{A}) \times \mathbf{d} = (2, -1, 1) \times (1, 1, 1)\)</p>
<p>\(= ((-1) \cdot 1 - 1 \cdot 1,\; 1 \cdot 1 - 2 \cdot 1,\; 2 \cdot 1 - (-1) \cdot 1)\)</p>
<p>\(= (-2, -1, 3)\)</p>
<p>\(|(\mathbf{P} - \mathbf{A}) \times \mathbf{d}| = \sqrt{4 + 1 + 9} = \sqrt{14}\)</p>
<p>\(|\mathbf{d}| = \sqrt{3}\)</p>
<p>Distance \(= \frac{\sqrt{14}}{\sqrt{3}} =\) <strong>\(\sqrt{42}/3\)</strong></p>
</div>

<div class="success-box">
<h4>Summary of Distance Formulas</h4>
<ul>
<li><strong>Point to plane:</strong> \(\frac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2 + b^2 + c^2}}\)</li>
<li><strong>Point to line:</strong> \(\frac{|(\mathbf{P} - \mathbf{A}) \times \mathbf{d}|}{|\mathbf{d}|}\)</li>
<li><strong>Parallel planes:</strong> \(\frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}\)</li>
<li><strong>Skew lines:</strong> \(\frac{|(\mathbf{a}_2 - \mathbf{a}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{|\mathbf{d}_1 \times \mathbf{d}_2|}\)</li>
</ul>
</div>
"""
    }
]
