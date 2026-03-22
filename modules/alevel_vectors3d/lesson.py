SECTIONS = [
    {
        "title": "3D Vectors: Representation and Operations",
        "body": """
<h3>Vector Notation and Components</h3>
<p>A vector in 3D space has three components: <strong>v</strong> = (x, y, z) or <strong>v</strong> = x<strong>i</strong> + y<strong>j</strong> + z<strong>k</strong>, where <strong>i</strong>, <strong>j</strong>, <strong>k</strong> are standard basis vectors.</p>

<p>The magnitude (length) of a vector is:</p>
<p style="text-align: center; font-weight: bold;">|<strong>v</strong>| = √(x² + y² + z²)</p>

<div class="example-box">
<h4>Example 1: Vector Magnitude</h4>
<p>Find the magnitude of <strong>v</strong> = (3, -4, 12)</p>
<p><strong>Solution:</strong> |<strong>v</strong>| = √(3² + (-4)² + 12²) = √(9 + 16 + 144) = √169 = 13</p>
</div>

<h3>Vector Addition and Scalar Multiplication</h3>
<p><strong>Addition:</strong> <strong>u</strong> + <strong>v</strong> = (u₁ + v₁, u₂ + v₂, u₃ + v₃)</p>
<p><strong>Scalar multiplication:</strong> k<strong>v</strong> = (kv₁, kv₂, kv₃)</p>

<p>These operations are component-wise and commutative/associative.</p>

<h3>Unit Vectors and Normalization</h3>
<p>A <strong>unit vector</strong> has magnitude 1. To normalize a vector <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">û = <strong>v</strong>/|<strong>v</strong>|</p>

<div class="example-box">
<h4>Example 2: Normalization</h4>
<p>Normalize the vector <strong>v</strong> = (1, 2, 2)</p>
<p><strong>Solution:</strong> |<strong>v</strong>| = √(1 + 4 + 4) = √9 = 3</p>
<p>û = (1/3, 2/3, 2/3)</p>
<p><strong>Check:</strong> |û| = √(1/9 + 4/9 + 4/9) = √(9/9) = 1 ✓</p>
</div>
"""
    },
    {
        "title": "Scalar (Dot) Product: Projection and Angles",
        "body": """
<h3>Definition and Geometric Interpretation</h3>
<p>The <strong>scalar product</strong> (or dot product) of <strong>u</strong> = (u₁, u₂, u₃) and <strong>v</strong> = (v₁, v₂, v₃) is:</p>
<p style="text-align: center; font-weight: bold;"><strong>u</strong> · <strong>v</strong> = u₁v₁ + u₂v₂ + u₃v₃</p>

<p><strong>Geometric interpretation:</strong> <strong>u</strong> · <strong>v</strong> = |<strong>u</strong>| |<strong>v</strong>| cos(θ), where θ is the angle between the vectors.</p>

<p><strong>Proof:</strong> Consider the triangle formed by <strong>u</strong>, <strong>v</strong>, and <strong>u</strong> - <strong>v</strong>. By the law of cosines:
<br>|<strong>u</strong> - <strong>v</strong>|² = |<strong>u</strong>|² + |<strong>v</strong>|² - 2|<strong>u</strong>||<strong>v</strong>|cos(θ)
<br>Expanding |<strong>u</strong> - <strong>v</strong>|² = (<strong>u</strong> - <strong>v</strong>) · (<strong>u</strong> - <strong>v</strong>) = |<strong>u</strong>|² - 2<strong>u</strong> · <strong>v</strong> + |<strong>v</strong>|²
<br>Comparing: <strong>u</strong> · <strong>v</strong> = |<strong>u</strong>||<strong>v</strong>|cos(θ)
</p>

<h3>Applications: Angles and Orthogonality</h3>
<p><strong>Angle between vectors:</strong> cos(θ) = (<strong>u</strong> · <strong>v</strong>) / (|<strong>u</strong>||<strong>v</strong>|)</p>
<p><strong>Perpendicular (orthogonal):</strong> <strong>u</strong> ⊥ <strong>v</strong> if and only if <strong>u</strong> · <strong>v</strong> = 0</p>

<div class="example-box">
<h4>Example 3: Finding Angle Between Vectors</h4>
<p>Find the angle between <strong>u</strong> = (1, 2, 2) and <strong>v</strong> = (2, 1, -2)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> · <strong>v</strong> = 1(2) + 2(1) + 2(-2) = 2 + 2 - 4 = 0</p>
<p>Since <strong>u</strong> · <strong>v</strong> = 0, the vectors are perpendicular: θ = 90°</p>
</div>

<h3>Projection</h3>
<p>The <strong>scalar projection</strong> of <strong>u</strong> onto <strong>v</strong> is the component of <strong>u</strong> in the direction of <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">comp_<strong>v</strong>(<strong>u</strong>) = (<strong>u</strong> · <strong>v</strong>) / |<strong>v</strong>|</p>

<p>The <strong>vector projection</strong> is:</p>
<p style="text-align: center; font-weight: bold;">proj_<strong>v</strong>(<strong>u</strong>) = [(<strong>u</strong> · <strong>v</strong>) / |<strong>v</strong>|²] <strong>v</strong></p>

<div class="example-box">
<h4>Example 4: Vector Projection</h4>
<p>Find the projection of <strong>u</strong> = (3, 4) onto <strong>v</strong> = (1, 0)</p>
<p><strong>Solution:</strong> <strong>u</strong> · <strong>v</strong> = 3, |<strong>v</strong>|² = 1</p>
<p>proj_<strong>v</strong>(<strong>u</strong>) = (3/1)(1, 0) = (3, 0)</p>
</div>
"""
    },
    {
        "title": "Cross Product: Area and Normal Vectors",
        "body": """
<h3>Definition and Computation</h3>
<p>The <strong>cross product</strong> <strong>u</strong> × <strong>v</strong> of vectors <strong>u</strong> = (u₁, u₂, u₃) and <strong>v</strong> = (v₁, v₂, v₃) is a vector perpendicular to both:</p>

<p style="text-align: center; font-weight: bold;"><strong>u</strong> × <strong>v</strong> = (u₂v₃ - u₃v₂, u₃v₁ - u₁v₃, u₁v₂ - u₂v₁)</p>

<p>This can be computed using a determinant:</p>
<p style="text-align: center; font-weight: bold;"><strong>u</strong> × <strong>v</strong> = det|<strong>i</strong>  <strong>j</strong>  <strong>k</strong> | = <strong>i</strong>(u₂v₃ - u₃v₂) - <strong>j</strong>(u₁v₃ - u₃v₁) + <strong>k</strong>(u₁v₂ - u₂v₁)|
                     |u₁ u₂ u₃|
                     |v₁ v₂ v₃|</p>

<div class="example-box">
<h4>Example 5: Computing Cross Product</h4>
<p>Find <strong>u</strong> × <strong>v</strong> where <strong>u</strong> = (1, 2, 3) and <strong>v</strong> = (4, 5, 6)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> × <strong>v</strong> = (2·6 - 3·5, 3·4 - 1·6, 1·5 - 2·4)</p>
<p>= (12 - 15, 12 - 6, 5 - 8) = (-3, 6, -3)</p>
</div>

<h3>Geometric Interpretation</h3>
<p>The magnitude of <strong>u</strong> × <strong>v</strong> equals the area of the parallelogram spanned by <strong>u</strong> and <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">|<strong>u</strong> × <strong>v</strong>| = |<strong>u</strong>| |<strong>v</strong>| sin(θ)</p>

<p>The direction follows the <strong>right-hand rule</strong>: curl fingers from <strong>u</strong> to <strong>v</strong>, thumb points in direction of <strong>u</strong> × <strong>v</strong>.</p>

<h3>Properties of Cross Product</h3>
<ul>
<li><strong>Anticommutative:</strong> <strong>v</strong> × <strong>u</strong> = -(<strong>u</strong> × <strong>v</strong>)</li>
<li><strong>Non-associative:</strong> In general, (<strong>u</strong> × <strong>v</strong>) × <strong>w</strong> ≠ <strong>u</strong> × (<strong>v</strong> × <strong>w</strong>)</li>
<li><strong>Self-cross:</strong> <strong>u</strong> × <strong>u</strong> = <strong>0</strong></li>
<li><strong>Orthogonality:</strong> <strong>u</strong> × <strong>v</strong> is perpendicular to both <strong>u</strong> and <strong>v</strong></li>
</ul>

<h3>Triple Scalar Product (Determinant)</h3>
<p>The volume of the parallelepiped spanned by <strong>u</strong>, <strong>v</strong>, <strong>w</strong> is:</p>
<p style="text-align: center; font-weight: bold;">V = |<strong>u</strong> · (<strong>v</strong> × <strong>w</strong>)| = |det[<strong>u</strong> <strong>v</strong> <strong>w</strong>]|</p>
"""
    },
    {
        "title": "Equations of Lines and Planes in 3D",
        "body": """
<h3>Vector Equation of a Line</h3>
<p>A line passing through point A with direction vector <strong>d</strong> can be written as:</p>
<p style="text-align: center; font-weight: bold;"><strong>r</strong> = <strong>a</strong> + t<strong>d</strong>, where t ∈ ℝ</p>

<p>In component form: (x, y, z) = (a₁, a₂, a₃) + t(d₁, d₂, d₃)</p>

<p><strong>Parametric form:</strong></p>
<p>x = a₁ + td₁
<br>y = a₂ + td₂
<br>z = a₃ + td₃</p>

<p><strong>Cartesian form:</strong> (x - a₁)/d₁ = (y - a₂)/d₂ = (z - a₃)/d₃</p>

<div class="example-box">
<h4>Example 6: Line Through Two Points</h4>
<p>Find the equation of the line through P(1, 2, 3) and Q(4, 5, 6)</p>
<p><strong>Solution:</strong> Direction vector: <strong>d</strong> = Q - P = (3, 3, 3)</p>
<p>Vector equation: <strong>r</strong> = (1, 2, 3) + t(3, 3, 3)</p>
<p>Cartesian form: (x - 1)/3 = (y - 2)/3 = (z - 3)/3</p>
</div>

<h3>Vector Equation of a Plane</h3>
<p>A plane containing point A perpendicular to normal vector <strong>n</strong> = (a, b, c) satisfies:</p>
<p style="text-align: center; font-weight: bold;"><strong>n</strong> · (<strong>r</strong> - <strong>a</strong>) = 0</p>

<p><strong>Cartesian form:</strong> a(x - x₀) + b(y - y₀) + c(z - z₀) = 0
<br>Or: <strong>ax + by + cz = d</strong>, where d = ax₀ + by₀ + cz₀</p>

<div class="example-box">
<h4>Example 7: Plane Through Three Points</h4>
<p>Find the equation of the plane through P(1, 0, 0), Q(0, 2, 0), R(0, 0, 3)</p>
<p><strong>Solution:</strong></p>
<p><strong>PQ</strong> = (-1, 2, 0), <strong>PR</strong> = (-1, 0, 3)
<br>Normal: <strong>n</strong> = <strong>PQ</strong> × <strong>PR</strong> = (6, 3, 2)
<br>Plane equation: 6(x - 1) + 3(y - 0) + 2(z - 0) = 0
<br>6x + 3y + 2z = 6
</p>
</div>

<h3>Distance from Point to Plane</h3>
<p>The distance from point P(x₀, y₀, z₀) to plane ax + by + cz = d is:</p>
<p style="text-align: center; font-weight: bold;">distance = |ax₀ + by₀ + cz₀ - d| / √(a² + b² + c²)</p>

<div class="example-box">
<h4>Example 8: Point-to-Plane Distance</h4>
<p>Find the distance from P(1, 2, 3) to the plane 2x - y + 2z = 9</p>
<p><strong>Solution:</strong> distance = |2(1) - 1(2) + 2(3) - 9| / √(4 + 1 + 4)</p>
<p>= |2 - 2 + 6 - 9| / √9 = |-3| / 3 = 1</p>
</div>
"""
    },
    {
        "title": "Intersections and Distances in 3D Space",
        "body": """
<h3>Intersection of Two Lines</h3>
<p>Lines <strong>r</strong> = <strong>a₁</strong> + s<strong>d₁</strong> and <strong>r</strong> = <strong>a₂</strong> + t<strong>d₂</strong> intersect if <strong>a₁</strong> + s<strong>d₁</strong> = <strong>a₂</strong> + t<strong>d₂</strong> has a solution.</p>

<p>This gives three equations in two unknowns (s, t). The system may be:</p>
<ul>
<li><strong>Consistent and unique:</strong> Lines intersect at one point</li>
<li><strong>Consistent with infinitely many solutions:</strong> Lines are coincident (same line)</li>
<li><strong>Inconsistent:</strong> Lines are skew (don't intersect)</li>
</ul>

<div class="example-box">
<h4>Example 9: Intersection of Lines</h4>
<p>Do the lines <strong>r</strong> = (1, 2, 3) + s(1, 1, 1) and <strong>r</strong> = (2, 0, 1) + t(1, -1, 1) intersect?</p>
<p><strong>Solution:</strong> (1+s, 2+s, 3+s) = (2+t, -t, 1+t)
<br>1 + s = 2 + t ⟹ s - t = 1
<br>2 + s = -t ⟹ s + t = -2
<br>Adding: 2s = -1 ⟹ s = -1/2
<br>From s - t = 1: t = -3/2
<br>Check third equation: 3 + (-1/2) = 1 + (-3/2) = -1/2? No: 5/2 ≠ -1/2
<br>The lines do not intersect (they are skew).
</p>
</div>

<h3>Intersection of Line and Plane</h3>
<p>Substitute the parametric line equation into the plane equation ax + by + cz = d:</p>
<p>a(a₁ + td₁) + b(a₂ + td₂) + c(a₃ + td₃) = d</p>

<p><strong>Solve for t:</strong> If <strong>n</strong> · <strong>d</strong> ≠ 0, there is a unique intersection point.</p>

<p>If <strong>n</strong> · <strong>d</strong> = 0 (direction parallel to plane), the line either lies in the plane (infinitely many solutions) or is parallel but not in it (no intersection).</p>

<h3>Distance Between Two Skew Lines</h3>
<p>For skew lines <strong>r</strong> = <strong>a₁</strong> + s<strong>d₁</strong> and <strong>r</strong> = <strong>a₂</strong> + t<strong>d₂</strong>, the distance is:</p>
<p style="text-align: center; font-weight: bold;">distance = |(<strong>a₂</strong> - <strong>a₁</strong>) · (<strong>d₁</strong> × <strong>d₂</strong>)| / |<strong>d₁</strong> × <strong>d₂</strong>|</p>

<p>This is the perpendicular distance between the two lines.</p>

<div class="example-box">
<h4>Example 10: Distance Between Skew Lines</h4>
<p>Find the distance between <strong>r</strong> = (1, 0, 0) + s(0, 1, 1) and <strong>r</strong> = (0, 2, 0) + t(1, 0, 1)</p>
<p><strong>Solution:</strong></p>
<p><strong>a₂</strong> - <strong>a₁</strong> = (-1, 2, 0)
<br><strong>d₁</strong> × <strong>d₂</strong> = (0, 1, 1) × (1, 0, 1) = (1, 1, -1)
<br>|<strong>d₁</strong> × <strong>d₂</strong>| = √3
<br>(<strong>a₂</strong> - <strong>a₁</strong>) · (<strong>d₁</strong> × <strong>d₂</strong>) = (-1, 2, 0) · (1, 1, -1) = -1 + 2 + 0 = 1
<br>distance = |1| / √3 = √3/3
</p>
</div>

<h3>Angle Between Line and Plane</h3>
<p>If line has direction <strong>d</strong> and plane has normal <strong>n</strong>, the angle α between the line and plane is:</p>
<p style="text-align: center; font-weight: bold;">sin(α) = |<strong>d</strong> · <strong>n</strong>| / (|<strong>d</strong>||<strong>n</strong>|)</p>

<p>Note: This is the complement of the angle between <strong>d</strong> and <strong>n</strong>.</p>
"""
    }
]
