TITLE = "Circle Theorems: Angles, Chords, and Cyclic Properties"

SECTIONS = [
    {
        "title": "Angle at the Center vs Angle at the Circumference",
        "body": """
<div class="concept-box">
<p><strong>Circle Theorem 1:</strong> The angle subtended by an arc at the center is TWICE the angle subtended by the same arc at any point on the circumference.</p>
</div>

<p>This is one of the most powerful theorems in circle geometry. If you understand this, you understand a huge amount about circles.</p>

<h4>What Does This Mean?</h4>

<p>Imagine an arc AB on a circle with center O. Now pick any point P on the circumference (on the major arc). The angle ∠AOB at the center is always exactly TWICE the angle ∠APB at the circumference:</p>

<p style="text-align: center; font-weight: bold;">\\(\\angle AOB = 2 \\times \\angle APB\\)</p>

<svg width="360" height="320" class="formula-box">
  <circle cx="180" cy="160" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="160" r="4" fill='#e6edf3'/>
  <circle cx="100" cy="100" r="4" fill='#f85149'/>
  <circle cx="260" cy="100" r="4" fill='#f85149'/>
  <circle cx="220" cy="230" r="4" fill='#a371f7'/>
  <line x1="180" y1="160" x2="100" y2="100" stroke='#f85149' stroke-width="2"/>
  <line x1="180" y1="160" x2="260" y2="100" stroke='#f85149' stroke-width="2"/>
  <path d="M 100 100 A 100 100 0 0 1 260 100" fill='none' stroke='#79c0ff' stroke-width="3"/>
  <line x1="220" y1="230" x2="100" y2="100" stroke='#a371f7' stroke-width="2"/>
  <line x1="220" y1="230" x2="260" y2="100" stroke='#a371f7' stroke-width="2"/>
  <path d="M 205 165 A 20 20 0 0 0 193 153" fill='none' stroke='#f85149' stroke-width="1.5"/>
  <text x="195" y="178" fill='#f85149' font-size='12' font-weight='bold'>∠AOB</text>
  <path d="M 215 215 A 15 15 0 0 0 225 205" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="225" y="220" fill='#a371f7' font-size='11' font-weight='bold'>∠APB</text>
  <text x="85" y="85" fill='#f85149' font-size='11'>A</text>
  <text x="265" y="85" fill='#f85149' font-size='11'>B</text>
  <text x="225" y="245" fill='#a371f7' font-size='11'>P</text>
  <text x="165" y="150" fill='#e6edf3' font-size='11'>O</text>
  <text x="180" y="295" fill='#e6edf3' font-size='12' text-anchor='middle'>∠AOB = 2 × ∠APB (always!)</text>
</svg>

<h4>Key Observation</h4>

<p>No matter where you place P on the circumference (on the major arc), the angle ∠APB stays the same! This is because all such angles subtend the same arc.</p>

<div class="worked-example">
<h5>Example 1: Center vs Circumference Angle</h5>
<p>In a circle with center O, the angle ∠AOB = 80°. Point P is on the circumference. Find ∠APB.</p>
<p><strong>Solution:</strong></p>
<p>∠APB = (1/2) × ∠AOB = (1/2) × 80° = <strong>40°</strong></p>
</div>

<div class="warning-box">
<p><strong>Important:</strong> Point P must be on the circumference on the opposite side of the arc from the center angle. If P is on the minor arc AB, it would be inside the angle at the center.</p>
</div>
"""
    },
    {
        "title": "Angle in a Semicircle: The 90° Theorem",
        "body": """
<div class="concept-box">
<p><strong>Circle Theorem 2:</strong> An angle inscribed in a semicircle is a RIGHT ANGLE (90°).</p>
</div>

<p>This is a special case of the angle at center vs circumference theorem. When the arc is a semicircle, the central angle is 180°, so the inscribed angle is 180°/2 = 90°.</p>

<h4>Why Does This Work?</h4>

<p>The central angle for a semicircle is 180° (a straight line through the center). By the angle at center theorem, any angle subtended by this arc at the circumference is:</p>

<p style="text-align: center; font-weight: bold;">\\(\\angle = \\frac{1}{2} \\times 180° = 90°\\)</p>

<svg width="380" height="300" class="formula-box">
  <circle cx="190" cy="150" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="190" cy="150" r="4" fill='#e6edf3'/>
  <line x1="90" y1="150" x2="290" y2="150" stroke='#f85149' stroke-width="2"/>
  <circle cx="90" cy="150" r="4" fill='#f85149'/>
  <circle cx="290" cy="150" r="4" fill='#f85149'/>
  <circle cx="190" cy="50" r="4" fill='#a371f7'/>
  <line x1="190" y1="50" x2="90" y2="150" stroke='#a371f7' stroke-width="2"/>
  <line x1="190" y1="50" x2="290" y2="150" stroke='#a371f7' stroke-width="2"/>
  <path d="M 190 150 A 100 100 0 0 1 90 150" fill='none' stroke='#79c0ff' stroke-width="3"/>
  <text x="80" y="170" fill='#f85149' font-size='11'>A</text>
  <text x="295" y="170" fill='#f85149' font-size='11'>B</text>
  <text x="185" y="35" fill='#a371f7' font-size='11'>P</text>
  <text x="180" y="160" fill='#e6edf3' font-size='10'>O</text>
  <path d="M 200 80 A 20 20 0 0 0 225 95" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="230" y="85" fill='#a371f7' font-size='12' font-weight='bold'>90°</text>
  <text x="190" y="290" fill='#e6edf3' font-size='12' text-anchor='middle'>P is on the circle, AB is a diameter → ∠APB = 90°</text>
</svg>

<h4>Practical Application</h4>

<p>This theorem is incredibly useful for:</p>
<ul>
<li>Finding right angles in geometric figures</li>
<li>Proving that triangles are right-angled</li>
<li>Construction problems (if you want a right angle, use a diameter)</li>
</ul>

<div class="worked-example">
<h5>Example 2: Right Angle in Semicircle</h5>
<p>A circle has diameter AB = 10 cm. Point P is on the circle. Find angle ∠APB.</p>
<p><strong>Solution:</strong></p>
<p>Since AB is a diameter and P is on the circle:</p>
<p>∠APB = <strong>90°</strong> (angle in a semicircle is always 90°)</p>
</div>
"""
    },
    {
        "title": "Angles in the Same Segment and Cyclic Quadrilaterals",
        "body": """
<div class="concept-box">
<p><strong>Circle Theorem 3:</strong> Angles subtended by the same arc at the circumference are EQUAL.</p>
</div>

<p>This follows directly from the angle at center theorem. Since any two angles at the circumference subtending the same arc are each half the center angle, they must be equal to each other.</p>

<h4>Cyclic Quadrilateral: A Quadrilateral Inside a Circle</h4>

<p>A <strong>cyclic quadrilateral</strong> is a quadrilateral whose four vertices all lie on a circle.</p>

<p><strong>Key Property:</strong> Opposite angles in a cyclic quadrilateral are SUPPLEMENTARY (they add up to 180°).</p>

<p style="text-align: center; font-weight: bold;">\\(\\angle A + \\angle C = 180°\\)</p>
<p style="text-align: center; font-weight: bold;">\\(\\angle B + \\angle D = 180°\\)</p>

<svg width="380" height="340" class="formula-box">
  <circle cx="190" cy="170" r="110" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="190" cy="170" r="4" fill='#e6edf3'/>
  <circle cx="100" cy="100" r="5" fill='#f85149'/>
  <circle cx="280" cy="100" r="5" fill='#f85149'/>
  <circle cx="300" cy="200" r="5" fill='#a371f7'/>
  <circle cx="80" cy="240" r="5" fill='#a371f7'/>
  <line x1="100" y1="100" x2="280" y2="100" stroke='#30363d' stroke-width="1.5"/>
  <line x1="280" y1="100" x2="300" y2="200" stroke='#30363d' stroke-width="1.5"/>
  <line x1="300" y1="200" x2="80" y2="240" stroke='#30363d' stroke-width="1.5"/>
  <line x1="80" y1="240" x2="100" y2="100" stroke='#30363d' stroke-width="1.5"/>
  <text x="85" y="90" fill='#f85149' font-size='12' font-weight='bold'>A</text>
  <text x="285" y="90" fill='#f85149' font-size='12' font-weight='bold'>B</text>
  <text x="310" y="205" fill='#a371f7' font-size='12' font-weight='bold'>C</text>
  <text x="65" y="250" fill='#a371f7' font-size='12' font-weight='bold'>D</text>
  <text x="185" y="160" fill='#e6edf3' font-size='10'>O</text>
  <path d="M 115 110 A 20 20 0 0 0 125 125" fill='none' stroke='#f85149' stroke-width="1.5"/>
  <text x="115" y="130" fill='#f85149' font-size='10'>∠A</text>
  <path d="M 290 120 A 20 20 0 0 0 280 130" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="300" y="145" fill='#a371f7' font-size='10'>∠C</text>
  <text x="190" y="320" fill='#e6edf3' font-size='12' text-anchor='middle'>∠A + ∠C = 180° (opposite angles in cyclic quadrilateral)</text>
</svg>

<h4>Why Is This True?</h4>

<p>Consider opposite angles A and C. Together, they subtend arcs that form the complete circle (360°). By the angle at center theorem:</p>
<ul>
<li>Angle A = (1/2) × (arc BCD)</li>
<li>Angle C = (1/2) × (arc DAB)</li>
<li>Arc BCD + Arc DAB = 360°</li>
<li>So A + C = (1/2) × 360° = 180°</li>
</ul>

<div class="worked-example">
<h5>Example 3: Cyclic Quadrilateral</h5>
<p>ABCD is a cyclic quadrilateral. If ∠A = 75°, find ∠C.</p>
<p><strong>Solution:</strong></p>
<p>Since A and C are opposite angles:</p>
<p>∠A + ∠C = 180°</p>
<p>75° + ∠C = 180°</p>
<p>∠C = <strong>105°</strong></p>
</div>
"""
    },
    {
        "title": "The Alternate Segment Theorem (Tangent-Chord Angle)",
        "body": """
<div class="concept-box">
<p><strong>Circle Theorem 4 (Alternate Segment):</strong> The angle between a tangent and a chord equals the angle in the alternate segment.</p>
</div>

<p>This theorem connects tangent lines with inscribed angles in a beautiful way.</p>

<h4>What Does This Mean?</h4>

<p>A tangent touches the circle at exactly one point. When a chord emanates from that point, the angle between the tangent and the chord equals any inscribed angle in the "alternate segment" (the region on the opposite side of the chord).</p>

<svg width="400" height="340" viewBox="0 0 400 340" class="formula-box">
  <circle cx="200" cy="170" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="200" cy="170" r="4" fill='#e6edf3'/>
  <circle cx="200" cy="70" r="4" fill='#f85149'/>
  <circle cx="280" cy="220" r="4" fill='#f85149'/>
  <circle cx="140" cy="240" r="4" fill='#a371f7'/>
  <line x1="200" y1="70" x2="120" y2="10" stroke='#30363d' stroke-width="2"/>
  <line x1="200" y1="70" x2="280" y2="220" stroke='#f85149' stroke-width="2"/>
  <line x1="200" y1="70" x2="140" y2="240" stroke='#a371f7' stroke-width="2"/>
  <path d="M 180 80 A 25 25 0 0 0 210 90" fill='none' stroke='#30363d' stroke-width="1.5"/>
  <text x="175" y="110" fill='#30363d' font-size='10'>Tangent-</text>
  <text x="175" y="125" fill='#30363d' font-size='10'>Chord</text>
  <path d="M 200 180 A 30 30 0 0 0 225 200" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="235" y="200" fill='#a371f7' font-size='10' font-weight='bold'>∠ACB</text>
  <text x="195" y="55" fill='#f85149' font-size='11'>A (tangent point)</text>
  <text x="285" y="225" fill='#f85149' font-size='11'>B</text>
  <text x="130" y="250" fill='#a371f7' font-size='11'>C</text>
  <text x="185" y="160" fill='#e6edf3' font-size='10'>O</text>
  <text x="200" y="320" fill='#e6edf3' font-size='12' text-anchor='middle'>Angle between tangent and chord AB equals inscribed angle ∠ACB</text>
</svg>

<h4>Why Is This Useful?</h4>

<p>This theorem helps you:</p>
<ul>
<li>Find angles involving tangents</li>
<li>Prove that lines are tangent to circles</li>
<li>Solve complex angle-chasing problems</li>
</ul>

<div class="worked-example">
<h5>Example 4: Alternate Segment Theorem</h5>
<p>A line is tangent to a circle at point A. A chord AB is drawn. The angle between the tangent and chord AB is 35°. Find the inscribed angle ∠ACB in the alternate segment.</p>
<p><strong>Solution:</strong></p>
<p>By the alternate segment theorem:</p>
<p>∠ACB = <strong>35°</strong> (equals the tangent-chord angle)</p>
</div>
"""
    }
]
