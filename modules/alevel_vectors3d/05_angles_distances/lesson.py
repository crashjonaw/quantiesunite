TITLE = "Angles and Distances Between Lines and Planes"

SECTIONS = [
    {
        "title": "Angles Between Lines",
        "body": """
<h3>Angle Between Two Lines</h3>
<p>The angle θ between two lines with direction vectors <strong>d</strong>₁ and <strong>d</strong>₂ is given by:</p>
<p style="text-align: center; font-weight: bold;">\\cos(\\theta) = \\frac{|\\mathbf{d}_1 \\cdot \\mathbf{d}_2|}{|\\mathbf{d}_1| |\\mathbf{d}_2|}</p>

<p><strong>Note:</strong> We use the absolute value of the dot product because we want the acute angle (0° ≤ θ ≤ 90°) between the lines, regardless of direction orientation.</p>

<h3>Parallel and Perpendicular Lines</h3>

<h4>Parallel:</h4>
<p>Direction vectors are scalar multiples: <strong>d</strong>₁ = k<strong>d</strong>₂ for some k ≠ 0. This means cos(θ) = 1, so θ = 0°.</p>

<h4>Perpendicular:</h4>
<p>Direction vectors are orthogonal: <strong>d</strong>₁ · <strong>d</strong>₂ = 0. This means cos(θ) = 0, so θ = 90°.</p>

<div class="worked-example">
<h4>Example 1: Angle Between Lines</h4>
<p>Find the angle between lines with direction vectors <strong>d</strong>₁ = (1, 2, 2) and <strong>d</strong>₂ = (2, 1, -2)</p>
<p><strong>Solution:</strong></p>
<p><strong>d</strong>₁ · <strong>d</strong>₂ = (1)(2) + (2)(1) + (2)(-2) = 2 + 2 - 4 = 0</p>
<p>Since the dot product is zero, the lines are <strong>perpendicular</strong>: θ = <strong>90°</strong></p>
</div>
"""
    },
    {
        "title": "Angle Between a Line and a Plane",
        "body": """
<h3>Definition</h3>
<p>The angle α between a line and a plane is the angle between the line and its orthogonal projection onto the plane. This is the complement of the angle between the line's direction vector and the plane's normal vector.</p>

<h3>Formula</h3>
<p>If the line has direction vector <strong>d</strong> and the plane has normal vector <strong>n</strong>:</p>
<p style="text-align: center; font-weight: bold;">\\sin(\\alpha) = \\frac{|\\mathbf{d} \\cdot \\mathbf{n}|}{|\\mathbf{d}| |\\mathbf{n}|}</p>

<p><strong>Why sine?</strong> The angle between <strong>d</strong> and <strong>n</strong> is complementary to α, so sin(α) = cos(angle between <strong>d</strong> and <strong>n</strong>).</p>

<h3>Special Cases</h3>

<h4>Line parallel to plane:</h4>
<p><strong>d</strong> · <strong>n</strong> = 0, so sin(α) = 0 and α = 0°</p>

<h4>Line perpendicular to plane:</h4>
<p><strong>d</strong> is parallel to <strong>n</strong>, so sin(α) = 1 and α = 90°</p>

<div class="worked-example">
<h4>Example 2: Angle Between Line and Plane</h4>
<p>Find the angle between the line <strong>r</strong> = (1, 2, 3) + t(1, 1, 2) and the plane 2x - y + z = 5</p>
<p><strong>Solution:</strong></p>
<p>Direction vector: <strong>d</strong> = (1, 1, 2)</p>
<p>Normal vector: <strong>n</strong> = (2, -1, 1)</p>
<p><strong>d</strong> · <strong>n</strong> = (1)(2) + (1)(-1) + (2)(1) = 2 - 1 + 2 = 3</p>
<p>|<strong>d</strong>| = √(1 + 1 + 4) = √6</p>
<p>|<strong>n</strong>| = √(4 + 1 + 1) = √6</p>
<p>sin(α) = |3| / (√6 · √6) = 3/6 = 1/2</p>
<p>α = <strong>30°</strong> or π/6 radians</p>
</div>
"""
    },
    {
        "title": "Distance Between Skew Lines",
        "body": """
<h3>Skew Lines Definition</h3>
<p>Two lines are <strong>skew</strong> if they do not intersect and are not parallel. In 3D, this is unique to lines in three-dimensional space.</p>

<h3>Distance Formula</h3>
<p>For skew lines <strong>r</strong> = <strong>a</strong>₁ + s<strong>d</strong>₁ and <strong>r</strong> = <strong>a</strong>₂ + t<strong>d</strong>₂, the perpendicular distance is:</p>
<p style="text-align: center; font-weight: bold;">\\text{distance} = \\frac{|(\\mathbf{a}_2 - \\mathbf{a}_1) \\cdot (\\mathbf{d}_1 \\times \\mathbf{d}_2)|}{|\\mathbf{d}_1 \\times \\mathbf{d}_2|}</p>

<p>The denominator is the magnitude of the cross product, which gives a vector perpendicular to both lines. This represents the common perpendicular direction.</p>

<h3>Geometric Interpretation</h3>
<p>The shortest distance between two skew lines occurs along the unique line perpendicular to both.</p>

<div class="worked-example">
<h4>Example 3: Distance Between Skew Lines</h4>
<p>Find the distance between <strong>r</strong> = (1, 0, 0) + s(0, 1, 1) and <strong>r</strong> = (0, 2, 0) + t(1, 0, 1)</p>
<p><strong>Solution:</strong></p>
<p><strong>a</strong>₂ - <strong>a</strong>₁ = (-1, 2, 0)</p>
<p><strong>d</strong>₁ = (0, 1, 1), <strong>d</strong>₂ = (1, 0, 1)</p>
<p><strong>d</strong>₁ × <strong>d</strong>₂ = (1·1 - 1·0, 1·1 - 0·1, 0·0 - 1·1) = (1, 1, -1)</p>
<p>|<strong>d</strong>₁ × <strong>d</strong>₂| = √(1 + 1 + 1) = √3</p>
<p>(<strong>a</strong>₂ - <strong>a</strong>₁) · (<strong>d</strong>₁ × <strong>d</strong>₂) = (-1, 2, 0) · (1, 1, -1) = -1 + 2 + 0 = 1</p>
<p>Distance = |1| / √3 = <strong>√3/3</strong> or <strong>1/√3</strong></p>
</div>

<div class="warning-box">
<h4>Verify the Lines are Skew</h4>
<p>Before using this formula, confirm that the lines actually are skew. Check that <strong>d</strong>₁ and <strong>d</strong>₂ are not parallel and that the lines don't intersect.</p>
</div>
"""
    },
    {
        "title": "Angle Between Two Planes",
        "body": """
<h3>Definition</h3>
<p>The angle between two planes is the angle between their normal vectors. Since normal vectors can point in either direction, we consider the acute angle (0° ≤ θ ≤ 90°).</p>

<h3>Formula</h3>
<p>If two planes have normal vectors <strong>n</strong>₁ and <strong>n</strong>₂:</p>
<p style="text-align: center; font-weight: bold;">\\cos(\\theta) = \\frac{|\\mathbf{n}_1 \\cdot \\mathbf{n}_2|}{|\\mathbf{n}_1| |\\mathbf{n}_2|}</p>

<p>The absolute value ensures we get the acute angle.</p>

<h3>Special Cases</h3>

<h4>Parallel planes:</h4>
<p>Normal vectors are scalar multiples: <strong>n</strong>₁ = k<strong>n</strong>₂. This means cos(θ) = 1, so θ = 0°.</p>

<h4>Perpendicular planes:</h4>
<p>Normal vectors are orthogonal: <strong>n</strong>₁ · <strong>n</strong>₂ = 0. This means cos(θ) = 0, so θ = 90°.</p>

<div class="worked-example">
<h4>Example 4: Angle Between Planes</h4>
<p>Find the angle between the planes 2x + y + 2z = 5 and x - 2y + 2z = 3</p>
<p><strong>Solution:</strong></p>
<p>Normal vectors: <strong>n</strong>₁ = (2, 1, 2), <strong>n</strong>₂ = (1, -2, 2)</p>
<p><strong>n</strong>₁ · <strong>n</strong>₂ = (2)(1) + (1)(-2) + (2)(2) = 2 - 2 + 4 = 4</p>
<p>|<strong>n</strong>₁| = √(4 + 1 + 4) = 3</p>
<p>|<strong>n</strong>₂| = √(1 + 4 + 4) = 3</p>
<p>cos(θ) = |4| / (3 · 3) = 4/9</p>
<p>θ = arccos(4/9) ≈ <strong>63.6°</strong></p>
</div>
"""
    },
    {
        "title": "Finding Common Perpendiculars and Shortest Distances",
        "body": """
<h3>Common Perpendicular to Two Skew Lines</h3>
<p>For two skew lines, there exists a unique line that is perpendicular to both. This common perpendicular is parallel to the vector <strong>d</strong>₁ × <strong>d</strong>₂.</p>

<p>To find the actual perpendicular line, you need to find the two closest points (one on each line) where the perpendicular intersects.</p>

<h3>Point-Line Distance</h3>
<p>The distance from point P to a line passing through point A with direction <strong>d</strong> is:</p>
<p style="text-align: center; font-weight: bold;">\\text{distance} = \\frac{|(\\mathbf{P} - \\mathbf{A}) \\times \\mathbf{d}|}{|\\mathbf{d}|}</p>

<p>This is found by constructing a parallelogram and using the cross product magnitude to find the height.</p>

<div class="worked-example">
<h4>Example 5: Distance from Point to Line</h4>
<p>Find the distance from P(3, 1, 4) to the line <strong>r</strong> = (1, 2, 3) + t(1, 1, 1)</p>
<p><strong>Solution:</strong></p>
<p>A = (1, 2, 3), <strong>d</strong> = (1, 1, 1)</p>
<p><strong>P</strong> - <strong>A</strong> = (2, -1, 1)</p>
<p>(<strong>P</strong> - <strong>A</strong>) × <strong>d</strong> = (2, -1, 1) × (1, 1, 1)</p>
<p>= ((-1)·1 - 1·1, 1·1 - 2·1, 2·1 - (-1)·1)</p>
<p>= (-2, -1, 3)</p>
<p>|(<strong>P</strong> - <strong>A</strong>) × <strong>d</strong>| = √(4 + 1 + 9) = √14</p>
<p>|<strong>d</strong>| = √3</p>
<p>Distance = √14 / √3 = <strong>√42/3</strong></p>
</div>

<div class="success-box">
<h4>Summary of Distance Formulas</h4>
<ul>
<li><strong>Point to plane:</strong> |ax₀ + by₀ + cz₀ - d| / √(a² + b² + c²)</li>
<li><strong>Point to line:</strong> |(<strong>P</strong> - <strong>A</strong>) × <strong>d</strong>| / |<strong>d</strong>|</li>
<li><strong>Parallel planes:</strong> |d₁ - d₂| / √(a² + b² + c²)</li>
<li><strong>Skew lines:</strong> |(<strong>a</strong>₂ - <strong>a</strong>₁) · (<strong>d</strong>₁ × <strong>d</strong>₂)| / |<strong>d</strong>₁ × <strong>d</strong>₂|</li>
</ul>
</div>
"""
    }
]
