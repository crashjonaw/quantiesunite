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

<svg width="380" height="310" viewBox="0 0 380 310" class="formula-box">
  <circle cx="180" cy="145" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="145" r="4" fill='currentColor'/>
  <circle cx="100" cy="85" r="4" fill='#f85149'/>
  <circle cx="260" cy="85" r="4" fill='#f85149'/>
  <circle cx="220" cy="215" r="4" fill='#a371f7'/>
  <line x1="180" y1="145" x2="100" y2="85" stroke='#f85149' stroke-width="2"/>
  <line x1="180" y1="145" x2="260" y2="85" stroke='#f85149' stroke-width="2"/>
  <path d="M 100 85 A 100 100 0 0 1 260 85" fill='none' stroke='#79c0ff' stroke-width="3"/>
  <line x1="220" y1="215" x2="100" y2="85" stroke='#a371f7' stroke-width="2"/>
  <line x1="220" y1="215" x2="260" y2="85" stroke='#a371f7' stroke-width="2"/>
  <path d="M 205 150 A 20 20 0 0 0 193 138" fill='none' stroke='#f85149' stroke-width="1.5"/>
  <text x="195" y="172" fill='#f85149' font-size='11' font-family='sans-serif' font-weight='bold'>\u2220AOB</text>
  <path d="M 215 200 A 15 15 0 0 0 225 190" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="233" y="205" fill='#a371f7' font-size='11' font-family='sans-serif' font-weight='bold'>\u2220APB</text>
  <text x="82" y="78" fill='#f85149' font-size='12' font-family='sans-serif'>A</text>
  <text x="268" y="78" fill='#f85149' font-size='12' font-family='sans-serif'>B</text>
  <text x="228" y="233" fill='#a371f7' font-size='12' font-family='sans-serif'>P</text>
  <text x="165" y="140" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="190" y="295" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>\u2220AOB = 2 \u00d7 \u2220APB (always!)</text>
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

<svg width="380" height="295" viewBox="0 0 380 295" class="formula-box">
  <circle cx="190" cy="140" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="190" cy="140" r="4" fill='currentColor'/>
  <!-- Diameter AB -->
  <line x1="90" y1="140" x2="290" y2="140" stroke='#f85149' stroke-width="2"/>
  <circle cx="90" cy="140" r="4" fill='#f85149'/>
  <circle cx="290" cy="140" r="4" fill='#f85149'/>
  <!-- Point P on circumference -->
  <circle cx="190" cy="40" r="4" fill='#a371f7'/>
  <line x1="190" y1="40" x2="90" y2="140" stroke='#a371f7' stroke-width="2"/>
  <line x1="190" y1="40" x2="290" y2="140" stroke='#a371f7' stroke-width="2"/>
  <!-- Right angle mark at P -->
  <rect x="190" y="40" width="12" height="12" fill='none' stroke='#a371f7' stroke-width="1.5" transform="rotate(45,190,40)"/>
  <text x="220" y="45" fill='#a371f7' font-size='13' font-family='sans-serif' font-weight='bold'>90\u00b0</text>
  <!-- Labels -->
  <text x="75" y="160" fill='#f85149' font-size='12' font-family='sans-serif'>A</text>
  <text x="295" y="160" fill='#f85149' font-size='12' font-family='sans-serif'>B</text>
  <text x="180" y="30" fill='#a371f7' font-size='12' font-family='sans-serif'>P</text>
  <text x="195" y="155" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="190" y="280" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>P is on the circle, AB is a diameter \u2192 \u2220APB = 90\u00b0</text>
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

<svg width="400" height="330" viewBox="0 0 400 330" class="formula-box">
  <circle cx="195" cy="155" r="110" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="195" cy="155" r="4" fill='currentColor'/>
  <circle cx="105" cy="85" r="5" fill='#f85149'/>
  <circle cx="285" cy="85" r="5" fill='#f85149'/>
  <circle cx="305" cy="185" r="5" fill='#a371f7'/>
  <circle cx="85" cy="225" r="5" fill='#a371f7'/>
  <!-- Quadrilateral sides -->
  <line x1="105" y1="85" x2="285" y2="85" stroke='#79c0ff' stroke-width="1.5"/>
  <line x1="285" y1="85" x2="305" y2="185" stroke='#79c0ff' stroke-width="1.5"/>
  <line x1="305" y1="185" x2="85" y2="225" stroke='#79c0ff' stroke-width="1.5"/>
  <line x1="85" y1="225" x2="105" y2="85" stroke='#79c0ff' stroke-width="1.5"/>
  <!-- Labels -->
  <text x="88" y="75" fill='#f85149' font-size='13' font-family='sans-serif' font-weight='bold'>A</text>
  <text x="292" y="75" fill='#f85149' font-size='13' font-family='sans-serif' font-weight='bold'>B</text>
  <text x="315" y="192" fill='#a371f7' font-size='13' font-family='sans-serif' font-weight='bold'>C</text>
  <text x="65" y="240" fill='#a371f7' font-size='13' font-family='sans-serif' font-weight='bold'>D</text>
  <text x="200" y="150" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <!-- Angle arcs -->
  <path d="M 120 95 A 20 20 0 0 0 115 110" fill='none' stroke='#f85149' stroke-width="1.5"/>
  <text x="125" y="118" fill='#f85149' font-size='11' font-family='sans-serif'>\u2220A</text>
  <path d="M 295 200 A 20 20 0 0 0 288 185" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="275" y="210" fill='#a371f7' font-size='11' font-family='sans-serif'>\u2220C</text>
  <text x="200" y="315" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>\u2220A + \u2220C = 180\u00b0 (opposite angles in cyclic quadrilateral)</text>
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

<svg width="400" height="335" viewBox="0 0 400 335" class="formula-box">
  <circle cx="200" cy="160" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="200" cy="160" r="4" fill='currentColor'/>
  <circle cx="200" cy="60" r="4" fill='#f85149'/>
  <circle cx="280" cy="210" r="4" fill='#f85149'/>
  <circle cx="140" cy="230" r="4" fill='#a371f7'/>
  <!-- Tangent line (visible color) -->
  <line x1="120" y1="20" x2="280" y2="60" stroke='#58a6ff' stroke-width="2" stroke-dasharray="6,3"/>
  <!-- Chord AB -->
  <line x1="200" y1="60" x2="280" y2="210" stroke='#f85149' stroke-width="2"/>
  <!-- Line AC -->
  <line x1="200" y1="60" x2="140" y2="230" stroke='#a371f7' stroke-width="2"/>
  <!-- Tangent-chord angle arc -->
  <path d="M 175 55 A 25 25 0 0 0 205 80" fill='none' stroke='#58a6ff' stroke-width="1.5"/>
  <text x="155" y="90" fill='#58a6ff' font-size='10' font-family='sans-serif'>Tangent-</text>
  <text x="155" y="103" fill='#58a6ff' font-size='10' font-family='sans-serif'>Chord \u2220</text>
  <!-- Alternate segment angle arc -->
  <path d="M 150 215 A 18 18 0 0 0 155 235" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="105" y="260" fill='#a371f7' font-size='11' font-family='sans-serif' font-weight='bold'>\u2220ACB</text>
  <!-- Point labels -->
  <text x="190" y="48" fill='#f85149' font-size='12' font-family='sans-serif'>A</text>
  <text x="288" y="218" fill='#f85149' font-size='12' font-family='sans-serif'>B</text>
  <text x="120" y="240" fill='#a371f7' font-size='12' font-family='sans-serif'>C</text>
  <text x="205" y="155" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <text x="290" y="48" fill='#58a6ff' font-size='11' font-family='sans-serif'>Tangent</text>
  <text x="200" y="320" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>Tangent-chord angle at A = inscribed \u2220ACB in alternate segment</text>
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
