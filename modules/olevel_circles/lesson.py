SECTIONS = [
    {
        "title": "Circle Equations and Basic Properties",
        "body": """
<h3>Standard Form of Circle</h3>
<p>(x - h)² + (y - k)² = r²</p>
<p>Center: (h, k), Radius: r</p>

<p>General form: x² + y² + Dx + Ey + F = 0</p>

<div class="example-box">
<h4>Example 1: Circle Equation</h4>
<p>Circle with center (3, -2) and radius 5:</p>
<p>(x - 3)² + (y + 2)² = 25</p>
<p>Expand: x² - 6x + 9 + y² + 4y + 4 = 25</p>
<p>x² + y² - 6x + 4y - 12 = 0</p>
</div>

<h3>Key Vocabulary</h3>
<ul>
  <li>Chord: Line segment joining two points on circle</li>
  <li>Diameter: Chord through center (length = 2r)</li>
  <li>Arc: Portion of circumference</li>
  <li>Sector: Region bounded by two radii and arc</li>
  <li>Segment: Region bounded by chord and arc</li>
</ul>
"""
    },
    {
        "title": "Angles and Circle Theorems",
        "body": """
<h3>Central and Inscribed Angles</h3>
<p><strong>Central angle:</strong> Vertex at center</p>
<p><strong>Inscribed angle:</strong> Vertex on circle</p>
<p><strong>Theorem:</strong> Inscribed angle = (1/2) × Central angle (same arc)</p>

<h3>Tangent Lines</h3>
<p>A tangent is perpendicular to the radius at point of contact.</p>
<p>From external point, two tangents of equal length can be drawn.</p>

<div class="example-box">
<h4>Example 2: Tangent Properties</h4>
<p>Circle center O, radius 5. Point P outside circle with OP = 13.</p>
<p>Tangent from P touches at T. Find PT.</p>
<p>By Pythagoras: PT² + 5² = 13²</p>
<p>PT² = 169 - 25 = 144, so PT = 12</p>
</div>

<h3>Angles in Same Segment</h3>
<p>Angles subtended by the same arc at the circumference are equal.</p>

<h3>Angle in Semicircle</h3>
<p>Angle subtended by diameter = 90°</p>
"""
    },
    {
        "title": "Tangent-Chord Angles and Power of a Point",
        "body": """
<h3>Angle Between Tangent and Chord</h3>
<p>Angle between tangent and chord = (1/2) × arc subtended by chord</p>

<h3>Power of a Point</h3>
<p><strong>Definition:</strong> For point P and circle with center O, radius r:</p>
<p>Power(P) = OP² - r²</p>

<p><strong>Theorem:</strong> If line through P intersects circle at A, B:</p>
<p>PA · PB = |Power(P)|</p>

<div class="example-box">
<h4>Example 3: Power of Point</h4>
<p>Circle x² + y² = 25 (center O, radius 5). Point P(8, 0).</p>
<p>Power(P) = 8² - 5² = 64 - 25 = 39</p>
<p>If line through P intersects at A, B: PA · PB = 39</p>
</div>
"""
    },
    {
        "title": "Circle Intersection and Equations",
        "body": """
<h3>Intersection of Circle and Line</h3>
<p>Substitute line equation into circle, get quadratic in one variable.</p>

<div class="example-box">
<h4>Example 4: Line-Circle Intersection</h4>
<p>Circle: x² + y² = 10</p>
<p>Line: y = x + 1</p>
<p>Substitute: x² + (x+1)² = 10</p>
<p>2x² + 2x - 9 = 0</p>
<p>Δ = 4 + 72 = 76 > 0, so two intersection points</p>
</div>

<h3>Intersection of Two Circles</h3>
<p>Subtract equations to eliminate x² and y² terms, get line equation, then substitute back.</p>

<h3>Tangency Conditions</h3>
<p>Line is tangent if discriminant = 0</p>
<p>Circles are tangent if distance between centers = r₁ + r₂ (external) or |r₁ - r₂| (internal)</p>
"""
    },
    {
        "title": "Areas and Arc Lengths",
        "body": """
<h3>Circle Measurements</h3>
<p><strong>Circumference:</strong> C = 2πr</p>
<p><strong>Area:</strong> A = πr²</p>
<p><strong>Arc length:</strong> s = rθ (θ in radians)</p>
<p><strong>Sector area:</strong> A = (1/2)r²θ</p>

<h3>Segment Area</h3>
<p>Area = (1/2)r²(θ - sin(θ))</p>

<div class="example-box">
<h4>Example 5: Sector and Segment</h4>
<p>Circle radius 8, central angle 60° = π/3 radians</p>
<p>Arc length: s = 8 × π/3 = 8π/3</p>
<p>Sector area: A = (1/2) × 64 × π/3 = 32π/3</p>
</div>
"""
    }
]
