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

<svg width="360" height="280" viewBox="0 0 360 280" class="formula-box">
  <circle cx="160" cy="130" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="160" cy="130" r="4" fill='currentColor'/>
  <circle cx="240" cy="130" r="4" fill='#f85149'/>
  <!-- Radius -->
  <line x1="160" y1="130" x2="240" y2="130" stroke='#f85149' stroke-width="2"/>
  <!-- Tangent line (visible on dark bg) -->
  <line x1="240" y1="50" x2="240" y2="220" stroke='#58a6ff' stroke-width="2.5"/>
  <!-- Right angle mark -->
  <polyline points="250,130 250,140 240,140" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <!-- Labels -->
  <text x="195" y="122" fill='#f85149' font-size='12' font-family='sans-serif' font-weight='bold'>Radius</text>
  <text x="250" y="85" fill='#58a6ff' font-size='12' font-family='sans-serif' font-weight='bold'>Tangent</text>
  <text x="145" y="125" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="248" y="155" fill='#f85149' font-size='11' font-family='sans-serif'>T</text>
  <text x="258" y="145" fill='#a371f7' font-size='12' font-family='sans-serif' font-weight='bold'>90\u00b0</text>
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

<svg width="380" height="305" viewBox="0 0 380 305" class="formula-box">
  <circle cx="160" cy="150" r="70" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="160" cy="150" r="4" fill='currentColor'/>
  <circle cx="105" cy="95" r="4" fill='#f85149'/>
  <circle cx="225" cy="100" r="4" fill='#f85149'/>
  <circle cx="290" cy="150" r="4" fill='#a371f7'/>
  <!-- Radii to tangent points -->
  <line x1="160" y1="150" x2="105" y2="95" stroke='#f85149' stroke-width="2"/>
  <line x1="160" y1="150" x2="225" y2="100" stroke='#f85149' stroke-width="2"/>
  <!-- Tangent lines (visible) -->
  <line x1="290" y1="150" x2="105" y2="95" stroke='#58a6ff' stroke-width="2"/>
  <line x1="290" y1="150" x2="225" y2="100" stroke='#58a6ff' stroke-width="2"/>
  <!-- OP dashed line -->
  <line x1="160" y1="150" x2="290" y2="150" stroke='#a371f7' stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Right angle marks -->
  <polyline points="112,105 102,108 105,95" fill='none' stroke='#a371f7' stroke-width="1"/>
  <polyline points="218,110 228,112 225,100" fill='none' stroke='#a371f7' stroke-width="1"/>
  <!-- Equal length tick marks on tangents -->
  <line x1="193" y1="118" x2="203" y2="128" stroke='#58a6ff' stroke-width="1.5"/>
  <line x1="253" y1="122" x2="263" y2="130" stroke='#58a6ff' stroke-width="1.5"/>
  <!-- Labels -->
  <text x="88" y="85" fill='#f85149' font-size='12' font-family='sans-serif'>A</text>
  <text x="230" y="90" fill='#f85149' font-size='12' font-family='sans-serif'>B</text>
  <text x="298" y="155" fill='#a371f7' font-size='12' font-family='sans-serif'>P</text>
  <text x="145" y="145" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="160" y="280" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>PA = PB (equal tangent lengths from external point)</text>
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

<svg width="400" height="290" viewBox="0 0 400 290" class="formula-box">
  <circle cx="180" cy="135" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="135" r="4" fill='currentColor'/>
  <circle cx="300" cy="135" r="4" fill='#a371f7'/>
  <!-- Secant intersection points -->
  <circle cx="100" cy="135" r="4" fill='#f85149'/>
  <circle cx="260" cy="135" r="4" fill='#f85149'/>
  <!-- Tangent point T on circle -->
  <circle cx="230" cy="72" r="4" fill='#58a6ff'/>
  <!-- Secant line through P -->
  <line x1="300" y1="135" x2="100" y2="135" stroke='#f85149' stroke-width="1.5"/>
  <!-- Tangent line from P to T -->
  <line x1="300" y1="135" x2="230" y2="72" stroke='#58a6ff' stroke-width="2"/>
  <!-- OP line -->
  <line x1="180" y1="135" x2="300" y2="135" stroke='#a371f7' stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Labels -->
  <text x="305" y="140" fill='#a371f7' font-size='12' font-family='sans-serif'>P</text>
  <text x="88" y="155" fill='#f85149' font-size='12' font-family='sans-serif'>A</text>
  <text x="258" y="155" fill='#f85149' font-size='12' font-family='sans-serif'>B</text>
  <text x="235" y="62" fill='#58a6ff' font-size='12' font-family='sans-serif'>T</text>
  <text x="165" y="128" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="275" y="95" fill='#58a6ff' font-size='11' font-family='sans-serif'>Tangent</text>
  <text x="200" y="275" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>PA \u00d7 PB = PT\u00b2 = Power(P)</text>
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

<svg width="420" height="235" viewBox="0 0 420 235" class="formula-box">
  <circle cx="100" cy="110" r="50" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="310" cy="110" r="70" fill='none' stroke='#f85149' stroke-width="2"/>
  <circle cx="100" cy="110" r="3" fill='currentColor'/>
  <circle cx="310" cy="110" r="3" fill='currentColor'/>
  <!-- Common tangent line (visible) -->
  <line x1="40" y1="65" x2="380" y2="160" stroke='#58a6ff' stroke-width="2.5"/>
  <!-- Radii to tangent points -->
  <line x1="100" y1="110" x2="82" y2="82" stroke='#79c0ff' stroke-width="1.5"/>
  <line x1="310" y1="110" x2="278" y2="60" stroke='#f85149' stroke-width="1.5"/>
  <!-- Labels -->
  <text x="85" y="130" fill='currentColor' font-size='11' font-family='sans-serif'>O\u2081</text>
  <text x="295" y="130" fill='currentColor' font-size='11' font-family='sans-serif'>O\u2082</text>
  <text x="180" y="215" fill='#58a6ff' font-size='12' font-family='sans-serif' font-weight='bold' text-anchor='middle'>Common Tangent</text>
</svg>
"""
    }
]
