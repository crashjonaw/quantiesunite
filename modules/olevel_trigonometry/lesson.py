SECTIONS = [
    {
        "title": "Trigonometric Ratios in Right Triangles",
        "body": """
<h3>Fundamental Definitions</h3>
<p>In a right triangle with angle θ (not the right angle):</p>
<p>sin(θ) = opposite/hypotenuse</p>
<p>cos(θ) = adjacent/hypotenuse</p>
<p>tan(θ) = opposite/adjacent = sin(θ)/cos(θ)</p>

<p>Reciprocals:</p>
<p>csc(θ) = 1/sin(θ), sec(θ) = 1/cos(θ), cot(θ) = 1/tan(θ)</p>

<h3>Mnemonic: SOHCAHTOA</h3>
<p>Sine = Opposite/Hypotenuse</p>
<p>Cosine = Adjacent/Hypotenuse</p>
<p>Tangent = Opposite/Adjacent</p>

<div class="example-box">
<h4>Example 1: Solving Right Triangles</h4>
<p>Right triangle with hypotenuse 10, one leg 6. Find angle opposite to this leg.</p>
<p>sin(θ) = 6/10 = 0.6, so θ = arcsin(0.6) ≈ 36.87°</p>
</div>
"""
    },
    {
        "title": "The Unit Circle and Angle Measurement",
        "body": """
<h3>Radian vs Degree Measure</h3>
<p>1 radian = 180°/π ≈ 57.3°</p>
<p>360° = 2π radians, 180° = π radians, 90° = π/2 radians</p>

<h3>The Unit Circle</h3>
<p>Circle with radius 1 centered at origin. Point at angle θ has coordinates (cos θ, sin θ).</p>

<p><strong>Key angles:</strong></p>
<p>0°: (1, 0); 30°: (√3/2, 1/2); 45°: (√2/2, √2/2); 60°: (1/2, √3/2); 90°: (0, 1)</p>

<h3>ASTC Rule</h3>
<p>Signs in each quadrant:</p>
<p>Quadrant I: All positive; II: Sin positive; III: Tan positive; IV: Cos positive</p>

<div class="example-box">
<h4>Example 2: Unit Circle Values</h4>
<p>sin(150°) = sin(180° - 30°) = sin(30°) = 1/2</p>
<p>cos(150°) = -cos(30°) = -√3/2</p>
</div>
"""
    },
    {
        "title": "Trigonometric Identities",
        "body": """
<h3>Fundamental Identities</h3>
<p><strong>Pythagorean:</strong> sin²θ + cos²θ = 1</p>
<p><strong>Quotient:</strong> tan(θ) = sin(θ)/cos(θ)</p>
<p><strong>Reciprocal:</strong> sin(θ)csc(θ) = 1</p>

<h3>Sum and Difference Formulas</h3>
<p>sin(A ± B) = sin(A)cos(B) ± cos(A)sin(B)</p>
<p>cos(A ± B) = cos(A)cos(B) ∓ sin(A)sin(B)</p>

<h3>Double Angle Formulas</h3>
<p>sin(2θ) = 2sin(θ)cos(θ)</p>
<p>cos(2θ) = cos²(θ) - sin²(θ) = 2cos²(θ) - 1 = 1 - 2sin²(θ)</p>

<div class="example-box">
<h4>Example 3: Proving Identities</h4>
<p>Prove: (1 + cos(θ))/sin(θ) = sin(θ)/(1 - cos(θ))</p>
<p>Multiply first fraction by (1 - cos(θ))/(1 - cos(θ)):</p>
<p>(1 - cos²(θ))/(sin(θ)(1 - cos(θ))) = sin²(θ)/(sin(θ)(1 - cos(θ))) = sin(θ)/(1 - cos(θ)) ✓</p>
</div>
"""
    },
    {
        "title": "Solving Trigonometric Equations",
        "body": """
<h3>General Approach</h3>
<p>Use identities to reduce to single trig function, then solve.</p>

<div class="example-box">
<h4>Example 4: Solving Trig Equations</h4>
<p>Solve sin(2θ) = sin(θ) for θ ∈ [0, 2π)</p>
<p>2sin(θ)cos(θ) = sin(θ)</p>
<p>sin(θ)(2cos(θ) - 1) = 0</p>
<p>sin(θ) = 0 or cos(θ) = 1/2</p>
<p>θ = 0, π, π/3, 5π/3</p>
</div>

<h3>General Solutions</h3>
<p>sin(θ) = a has solutions θ = arcsin(a) + 2πk or θ = π - arcsin(a) + 2πk</p>
<p>cos(θ) = a has solutions θ = ±arccos(a) + 2πk</p>
"""
    },
    {
        "title": "Applications: Modeling Periodic Phenomena",
        "body": """
<h3>Sinusoidal Functions</h3>
<p>y = A sin(Bx - C) + D</p>
<p>A = amplitude, period = 2π/B, phase shift = C/B, vertical shift = D</p>

<div class="example-box">
<h4>Example 5: Modeling Temperature</h4>
<p>Average temperature varies as T(t) = 15 + 10sin(πt/12) where t is months</p>
<p>Amplitude 10°, average 15°, period 24 months (2 years)</p>
</div>

<h3>Real-World Applications</h3>
<ul>
  <li>Sound and light waves</li>
  <li>Circular motion</li>
  <li>Alternating current</li>
  <li>Seasons and tides</li>
</ul>
"""
    }
]
