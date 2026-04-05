TITLE = "Tangent Properties: Lines That Touch Circles"

SECTIONS = [
    {
        "title": "What is a Tangent? A Line That Touches Once",
        "body": """
<div class="concept-box">
<p><strong>Tangent to a Circle:</strong> A straight line that touches the circle at exactly ONE point, called the point of tangency.</p>
</div>

<p>Unlike a chord (which crosses through the circle) or a secant (which intersects at two points), a tangent just "kisses" the circle.</p>

<h4>The Key Property: Tangent is Perpendicular to Radius</h4>

<p><strong>Fundamental Theorem:</strong> A tangent to a circle is perpendicular to the radius at the point of tangency.</p>

<p style="text-align: center; font-weight: bold;">\\(\\text{Tangent} \\perp \\text{Radius at point of tangency}\\)</p>

<p>This is THE most important fact about tangents. Everything else follows from this.</p>

<svg width="360" height="300" class="formula-box">
  <circle cx="180" cy="150" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="150" r="4" fill='#e6edf3'/>
  <circle cx="260" cy="150" r="4" fill='#f85149'/>
  <line x1="180" y1="150" x2="260" y2="150" stroke='#f85149' stroke-width="2"/>
  <line x1="260" y1="70" x2="260" y2="230" stroke='#30363d' stroke-width="2.5"/>
  <path d="M 270 155 L 275 155 L 275 150 L 270 150" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="200" y="165" fill='#f85149' font-size='12' font-weight='bold'>Radius</text>
  <text x="265" y="100" fill='#30363d' font-size='12' font-weight='bold'>Tangent</text>
  <text x="165" y="140" fill='#e6edf3' font-size='10'>O</text>
  <text x="265" y="135" fill='#f85149' font-size='10'>T</text>
  <text x="270" y="168" fill='#a371f7' font-size='11' font-weight='bold'>90°</text>
</svg>

<h4>Why Is This True?</h4>

<p>Imagine the radius as a "spoke" from the center to the edge. A tangent can't cross through the circle (it only touches once), so it must be perpendicular to this spoke. If it weren't perpendicular, it would either miss the circle or intersect it at two points.</p>

<div class="worked-example">
<h5>Example 1: Finding a Tangent Point</h5>
<p>A circle has center O and radius 5 cm. A line is tangent to the circle at point T. If you know the tangent line makes a certain angle with the horizontal, how do you find the direction of the radius OT?</p>
<p><strong>Solution:</strong></p>
<p>The radius OT is perpendicular to the tangent line. If the tangent makes angle θ with the horizontal, then OT makes angle (θ + 90°) with the horizontal.</p>
</div>
"""
    },
    {
        "title": "Two Tangents from an External Point",
        "body": """
<div class="concept-box">
<p><strong>Theorem:</strong> From any external point, exactly TWO tangents can be drawn to a circle, and these tangents have EQUAL LENGTH.</p>
</div>

<h4>The Setup</h4>

<p>Imagine a point P outside a circle with center O. Draw the two tangent lines from P to the circle, touching at points A and B. Then:</p>

<ul>
<li>PA = PB (the tangents are equal)</li>
<li>∠OPA = ∠OPB (the tangents make equal angles with OP)</li>
<li>∠OAP = ∠OBP = 90° (tangents perpendicular to radii)</li>
</ul>

<svg width="380" height="320" class="formula-box">
  <circle cx="180" cy="160" r="70" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="160" r="4" fill='#e6edf3'/>
  <circle cx="120" cy="90" r="4" fill='#f85149'/>
  <circle cx="240" cy="90" r="4" fill='#f85149'/>
  <circle cx="280" cy="180" r="4" fill='#a371f7'/>
  <line x1="180" y1="160" x2="120" y2="90" stroke='#f85149' stroke-width="2"/>
  <line x1="180" y1="160" x2="240" y2="90" stroke='#f85149' stroke-width="2"/>
  <line x1="280" y1="180" x2="120" y2="90" stroke='#30363d' stroke-width="2.5"/>
  <line x1="280" y1="180" x2="240" y2="90" stroke='#30363d' stroke-width="2.5"/>
  <line x1="180" y1="160" x2="280" y2="180" stroke='#a371f7' stroke-width="1.5" stroke-dasharray="3,3"/>
  <path d="M 135 110 L 140 105 L 145 115 L 140 110" fill='none' stroke='#f85149' stroke-width="1"/>
  <path d="M 255 110 L 250 105 L 260 105 L 255 110" fill='none' stroke='#f85149' stroke-width="1"/>
  <text x="115" y="80" fill='#f85149' font-size='11'>A</text>
  <text x="245" y="80" fill='#f85149' font-size='11'>B</text>
  <text x="285" y="195" fill='#a371f7' font-size='11'>P</text>
  <text x="165" y="150" fill='#e6edf3' font-size='10'>O</text>
  <text x="200" y="120" fill='#30363d' font-size='10'>PA = PB</text>
  <text x="235" y="165" fill='#30363d' font-size='10'>PA = PB</text>
</svg>

<h4>Why Are the Tangents Equal?</h4>

<p>Consider triangles OAP and OBP:</p>
<ul>
<li>OA = OB (both radii)</li>
<li>∠OAP = ∠OBP = 90° (tangent perpendicular to radius)</li>
<li>OP is common to both triangles</li>
</ul>

<p>By the Pythagorean theorem in both right triangles:</p>
<p style="text-align: center; font-weight: bold;">\\(PA^2 = OP^2 - OA^2 = OP^2 - r^2\\)</p>
<p style="text-align: center; font-weight: bold;">\\(PB^2 = OP^2 - OB^2 = OP^2 - r^2\\)</p>

<p>So PA = PB!</p>

<div class="worked-example">
<h5>Example 2: Finding Tangent Length</h5>
<p>A circle has center O and radius 5 cm. Point P is outside, with OP = 13 cm. Find the length of a tangent from P to the circle.</p>
<p><strong>Solution:</strong></p>
<p>Let T be the point of tangency. Triangle OTP is right-angled at T.</p>
<p>By Pythagoras: PT² + OT² = OP²</p>
<p>PT² + 5² = 13²</p>
<p>PT² = 169 - 25 = 144</p>
<p>PT = <strong>12 cm</strong></p>
</div>
"""
    },
    {
        "title": "Power of a Point: A Unified View of Circle Properties",
        "body": """
<div class="concept-box">
<p><strong>Power of a Point (P with respect to circle with center O, radius r):</strong></p>
<p style="text-align: center; font-weight: bold;">\\(\\text{Power}(P) = OP^2 - r^2\\)</p>
</div>

<p>The power of a point is a measure that unifies many circle properties. It's constant along all lines through P.</p>

<h4>Three Cases</h4>

<h5>Case 1: P Outside the Circle (Power > 0)</h5>

<p>If a line through P intersects the circle at points A and B (with A closer to P), then:</p>

<p style="text-align: center; font-weight: bold;">\\(PA \\times PB = \\text{Power}(P)\\)</p>

<p>Special case: If the line is tangent (touches at one point T), then:</p>

<p style="text-align: center; font-weight: bold;">\\(PT^2 = \\text{Power}(P)\\)</p>

<h5>Case 2: P Inside the Circle (Power < 0)</h5>

<p>If a line through P intersects the circle at A and B (P between them), then:</p>

<p style="text-align: center; font-weight: bold;">\\(PA \\times PB = |\\text{Power}(P)| = r^2 - OP^2\\)</p>

<h5>Case 3: P On the Circle (Power = 0)</h5>

<p>If P is on the circle, then OP² = r², so Power = 0. Any line through P either passes through P (giving PA = 0) or intersects at another point.</p>

<svg width="380" height="300" class="formula-box">
  <circle cx="180" cy="150" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="150" r="4" fill='#e6edf3'/>
  <circle cx="280" cy="150" r="4" fill='#a371f7'/>
  <circle cx="100" cy="150" r="4" fill='#f85149'/>
  <circle cx="200" cy="80" r="4" fill='#f85149'/>
  <line x1="280" y1="150" x2="100" y2="150" stroke='#30363d' stroke-width="1.5"/>
  <line x1="280" y1="150" x2="200" y2="80" stroke='#30363d' stroke-width="1.5"/>
  <line x1="180" y1="150" x2="280" y2="150" stroke='#a371f7' stroke-width="2"/>
  <text x="280" y="165" fill='#a371f7' font-size='11'>P</text>
  <text x="100" y="165" fill='#f85149' font-size='11'>A</text>
  <text x="205" y="70" fill='#f85149' font-size='11'>B</text>
  <text x="165" y="140" fill='#e6edf3' font-size='10'>O</text>
  <text x="235" y="155" fill='#a371f7' font-size='10' font-weight='bold'>Tangent</text>
  <text x="190" y="280" fill='#e6edf3' font-size='12' text-anchor='middle'>PA × PB = PT² = Power(P)</text>
</svg>

<div class="worked-example">
<h5>Example 3: Using Power of a Point</h5>
<p>A circle has center O and radius 6 cm. Point P is outside with OP = 10 cm.</p>
<p>A line through P intersects the circle at A (closer to P) and B (farther from P).</p>
<p>If PA = 2 cm, find PB.</p>
<p><strong>Solution:</strong></p>
<p>Power(P) = OP² - r² = 10² - 6² = 100 - 36 = 64</p>
<p>PA × PB = 64</p>
<p>2 × PB = 64</p>
<p>PB = <strong>32 cm</strong></p>
</div>
"""
    },
    {
        "title": "Summary: Tangent and Power Applications",
        "body": """
<h4>Key Facts About Tangents</h4>

<table style="width:100%; border-collapse:collapse; margin-bottom:16px;">
<tr >
<td style="padding: 8px;"><strong>Property</strong></td>
<td style="padding: 8px;"><strong>Statement</strong></td>
</tr>
<tr>
<td style="padding: 8px;">Tangent ⊥ Radius</td>
<td style="padding: 8px;">At point of tangency T: OT ⊥ tangent line</td>
</tr>
<tr class="worked-example">
<td style="padding: 8px;">Two Tangents Equal</td>
<td style="padding: 8px;">From external point P: PA = PB (both tangents)</td>
</tr>
<tr>
<td style="padding: 8px;">Tangent Length</td>
<td style="padding: 8px;">PT² = OP² - r² = Power(P)</td>
</tr>
<tr class="worked-example">
<td style="padding: 8px;">Power of Point</td>
<td style="padding: 8px;">PA × PB = OP² - r² (for any secant through P)</td>
</tr>
</table>

<h4>Problem-Solving Strategy</h4>

<p><strong>When you see a tangent:</strong></p>
<ol>
<li>Draw the radius to the point of tangency</li>
<li>Mark the 90° angle between tangent and radius</li>
<li>Look for right triangles you can solve with Pythagoras</li>
<li>Use the power of a point if multiple lines are involved</li>
</ol>

<h4>Practice Scenario</h4>

<p>Two circles with centers O₁ and O₂, radii r₁ and r₂. A line is tangent to both circles. This is called a <strong>common tangent</strong>. The distances from each center to the tangent line are exactly equal to their respective radii.</p>

<svg width="420" height="240" class="formula-box">
  <circle cx="100" cy="120" r="50" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="300" cy="120" r="70" fill='none' stroke='#f85149' stroke-width="2"/>
  <circle cx="100" cy="120" r="3" fill='#e6edf3'/>
  <circle cx="300" cy="120" r="3" fill='#e6edf3'/>
  <line x1="50" y1="80" x2="370" y2="170" stroke='#30363d' stroke-width="2.5"/>
  <line x1="100" y1="120" x2="85" y2="95" stroke='#79c0ff' stroke-width="1.5"/>
  <line x1="300" y1="120" x2="265" y2="65" stroke='#f85149' stroke-width="1.5"/>
  <text x="95" y="115" fill='#e6edf3' font-size='10'>O₁</text>
  <text x="295" y="115" fill='#e6edf3' font-size='10'>O₂</text>
  <text x="180" y="180" fill='#30363d' font-size='11' font-weight='bold'>Common Tangent</text>
</svg>
"""
    }
]
