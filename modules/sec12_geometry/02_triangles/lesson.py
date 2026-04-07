TITLE = "Triangle Properties and Angle Sum"

SECTIONS = [
    {
        "title": "The Triangle Angle Sum Rule",
        "body": """
<h4>First Principle: Every Triangle Has the Same Total Angle</h4>
<div class="concept-box">
<p><strong>The sum of all angles in ANY triangle is ALWAYS 180°.</strong></p>
<p>This is one of the most important rules in geometry. It works for every triangle, no matter the shape or size.</p>
<p>\\(\\angle A + \\angle B + \\angle C = 180°\\)</p>
</div>

<h4>Why Is This True? Proof Using Parallel Lines</h4>
<div class="success-box">
<p>Draw a line parallel to the base of a triangle through the top vertex. Using alternate angles and angles on a line, we can prove the sum is 180°.</p>

<svg width="100%" height="230" viewBox="-15 -15 530 260" class="formula-box">
  <!-- Parallel line through top vertex -->
  <line x1="80" y1="50" x2="420" y2="50" stroke='#58a6ff' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="85" y="42" fill='#58a6ff' font-size='10'>E</text>
  <text x="405" y="42" fill='#58a6ff' font-size='10'>F</text>

  <!-- Triangle -->
  <polygon points="250,50 130,170 370,170" fill='none' stroke='#56d364' stroke-width="2.5"/>

  <!-- Vertex dots -->
  <circle cx="250" cy="50" r="3" fill='currentColor'/>
  <circle cx="130" cy="170" r="3" fill='currentColor'/>
  <circle cx="370" cy="170" r="3" fill='currentColor'/>

  <!-- Angle arcs at A -->
  <path d="M 220,50 A 30,30 0 0,0 232,72" fill='none' stroke='#f85149' stroke-width="2"/>
  <path d="M 268,72 A 30,30 0 0,0 280,50" fill='none' stroke='#a371f7' stroke-width="2"/>
  <path d="M 232,72 A 30,30 0 0,0 268,72" fill='none' stroke='#79c0ff' stroke-width="2"/>

  <!-- Angle arcs at B -->
  <path d="M 160,170 A 30,30 0 0,0 145,148" fill='none' stroke='#f85149' stroke-width="2"/>

  <!-- Angle arcs at C -->
  <path d="M 355,148 A 30,30 0 0,0 340,170" fill='none' stroke='#a371f7' stroke-width="2"/>

  <!-- Labels -->
  <text x="250" y="90" fill='#79c0ff' font-size='13' font-weight='bold' text-anchor='middle'>A</text>
  <text x="110" y="180" fill='#f85149' font-size='13' font-weight='bold'>B</text>
  <text x="380" y="180" fill='#a371f7' font-size='13' font-weight='bold'>C</text>

  <!-- Alternate angle labels on parallel line -->
  <text x="185" y="48" fill='#f85149' font-size='11' font-weight='bold'>(= B)</text>
  <text x="290" y="48" fill='#a371f7' font-size='11' font-weight='bold'>(= C)</text>

  <!-- Conclusion -->
  <text x="250" y="215" fill='#56d364' font-size='13' font-weight='bold' text-anchor='middle'>B + A + C = angles on a line = 180°</text>
</svg>
</div>

<h4>Finding Missing Angles: Worked Examples</h4>

<div class="warning-box">
<p><strong>Example 1: Find the missing angle if two angles are 50° and 70°</strong></p>
<div class="worked-example">
<p>\(50° + 70° + x = 180°\)</p>
<p>\(120° + x = 180°\)</p>
<p><strong>\(x = 60°\)</strong></p>
</div>
</div>

<div class="warning-box">
<p><strong>Example 2: Find all angles if they are in the ratio 2:3:4</strong></p>
<div class="worked-example">
<p>Let angles be \(2k, 3k,\) and \(4k\)</p>
<p>\(2k + 3k + 4k = 180°\)</p>
<p>\(9k = 180°\)</p>
<p>\(k = 20°\)</p>
<p><strong>Angles are: 40°, 60°, 80°</strong></p>
</div>
</div>
"""
    },
    {
        "title": "Types of Triangles",
        "body": """
<h4>Triangles are Classified by Sides and Angles</h4>

<div class="success-box">
<h5>Classification by Sides</h5>
<table style="width: 100%">
<tr style=";">
<th>Type</th><th>Description</th><th>Angles</th>
</tr>
<tr class="formula-box">
<td><strong>Equilateral</strong></td><td>All three sides equal</td><td>All angles = 60°</td>
</tr>
<tr class="formula-box">
<td><strong>Isosceles</strong></td><td>Two sides equal</td><td>Two angles equal (base angles)</td>
</tr>
<tr class="formula-box">
<td><strong>Scalene</strong></td><td>All sides different</td><td>All angles different</td>
</tr>
</table>
</div>

<div class="success-box">
<h5>Classification by Angles</h5>
<table style="width: 100%">
<tr style=";">
<th>Type</th><th>Description</th><th>Key Feature</th>
</tr>
<tr class="formula-box">
<td><strong>Acute</strong></td><td>All angles less than 90°</td><td>Sharp-looking triangle</td>
</tr>
<tr class="formula-box">
<td><strong>Right-angled</strong></td><td>One angle = 90°</td><td>One perfect corner</td>
</tr>
<tr class="formula-box">
<td><strong>Obtuse</strong></td><td>One angle > 90°</td><td>One wide angle</td>
</tr>
</table>
</div>

<h4>Visual: Triangle Types</h4>
<svg width="100%" height="240" viewBox="-15 -15 730 270" class="formula-box">
  <!-- Equilateral -->
  <text x="80" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Equilateral</text>
  <polygon points="80,50 30,135 130,135" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <path d="M 60,135 A 20,20 0 0,1 47,118" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <path d="M 113,118 A 20,20 0 0,1 100,135" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <path d="M 92,63 A 20,20 0 0,1 68,63" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <text x="80" y="120" fill='currentColor' font-size='11' font-weight='bold' text-anchor='middle'>60°</text>
  <text x="80" y="155" fill='currentColor' font-size='11' text-anchor='middle'>All sides equal</text>

  <!-- Isosceles -->
  <text x="260" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Isosceles</text>
  <polygon points="260,50 195,135 325,135" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <path d="M 225,135 A 20,20 0 0,1 212,118" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <path d="M 308,118 A 20,20 0 0,1 295,135" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <!-- Tick marks for equal sides -->
  <line x1="223" y1="88" x2="233" y2="96" stroke='#56d364' stroke-width="1.5"/>
  <line x1="287" y1="96" x2="297" y2="88" stroke='#56d364' stroke-width="1.5"/>
  <text x="210" y="118" fill='currentColor' font-size='11' font-weight='bold'>70°</text>
  <text x="292" y="118" fill='currentColor' font-size='11' font-weight='bold'>70°</text>
  <text x="260" y="155" fill='currentColor' font-size='11' text-anchor='middle'>Two sides equal</text>

  <!-- Scalene -->
  <text x="440" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Scalene</text>
  <polygon points="420,50 390,135 500,135" fill='none' stroke='#f85149' stroke-width="2.5"/>
  <path d="M 420,135 A 20,20 0 0,1 407,118" fill='none' stroke='#ff7b72' stroke-width="1.5"/>
  <path d="M 483,118 A 20,20 0 0,1 470,135" fill='none' stroke='#ff7b72' stroke-width="1.5"/>
  <text x="400" y="120" fill='currentColor' font-size='10' font-weight='bold'>50°</text>
  <text x="468" y="120" fill='currentColor' font-size='10' font-weight='bold'>65°</text>
  <text x="440" y="155" fill='currentColor' font-size='11' text-anchor='middle'>All sides different</text>

  <!-- Right-angled -->
  <text x="620" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Right-angled</text>
  <polygon points="590,50 590,135 680,135" fill='none' stroke='#a371f7' stroke-width="2.5"/>
  <polyline points="590,120 605,120 605,135" fill='none' stroke='#c8b6ff' stroke-width="1.5"/>
  <text x="600" y="115" fill='currentColor' font-size='10' font-weight='bold'>90°</text>
  <text x="620" y="155" fill='currentColor' font-size='11' text-anchor='middle'>One angle = 90°</text>
</svg>
"""
    },
    {
        "title": "Exterior Angles of a Triangle",
        "body": """
<h4>What is an Exterior Angle?</h4>
<div class="concept-box">
<p>An <strong>exterior angle</strong> is formed when you extend one side of a triangle beyond a vertex.</p>
<p><strong>Exterior Angle Theorem:</strong> An exterior angle equals the sum of the two non-adjacent interior angles.</p>
<p>\\(\\text{Exterior angle} = \\text{Opposite angle 1} + \\text{Opposite angle 2}\\)</p>
</div>

<h4>Visual: Exterior Angle</h4>
<svg width="100%" height="250" viewBox="-15 -15 510 280" class="formula-box">
  <!-- Triangle -->
  <polygon points="120,170 250,40 360,170" fill='none' stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Extended line (BC extended to D) -->
  <line x1="360" y1="170" x2="460" y2="170" stroke='#56d364' stroke-width="2.5" stroke-dasharray="5,5"/>

  <!-- Vertex dots -->
  <circle cx="120" cy="170" r="3" fill='currentColor'/>
  <circle cx="250" cy="40" r="3" fill='currentColor'/>
  <circle cx="360" cy="170" r="3" fill='currentColor'/>

  <!-- Interior angle arcs -->
  <path d="M 150,170 A 30,30 0 0,1 137,148" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 267,58 A 30,30 0 0,1 233,58" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 343,148 A 30,30 0 0,1 330,170" fill='none' stroke='#79c0ff' stroke-width="2"/>

  <!-- Exterior angle arc -->
  <path d="M 390,170 A 30,30 0 0,0 377,148" fill='none' stroke='#f8a5a5' stroke-width="2.5"/>

  <!-- Labels -->
  <text x="155" y="158" fill='currentColor' font-size='13' font-weight='bold'>B</text>
  <text x="250" y="78" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>A</text>
  <text x="315" y="158" fill='currentColor' font-size='13' font-weight='bold'>C</text>
  <text x="395" y="158" fill='#f8a5a5' font-size='13' font-weight='bold'>Ext</text>
  <text x="465" y="174" fill='currentColor' font-size='11'>D</text>

  <!-- Explanation -->
  <text x="50" y="210" fill='currentColor' font-size='13' font-weight='bold'>Exterior angle = A + B</text>
  <text x="50" y="230" fill='currentColor' font-size='12'>Also: Exterior angle + C = 180° (straight line)</text>
</svg>

<h4>Worked Example</h4>
<div class="warning-box">
<p><strong>A triangle has angles 50°, 70°, and 60°. Find the exterior angle at the 60° vertex.</strong></p>
<div class="worked-example">
<p><strong>Method 1: Using the theorem</strong></p>
<p>Exterior angle = \(50° + 70° = 120°\)</p>
<p></p>
<p><strong>Method 2: Using supplementary angles</strong></p>
<p>Exterior angle \(+ 60° = 180°\) (straight line)</p>
<p>Exterior angle = \(180° - 60° = 120°\)</p>
<p><strong>Both methods give 120°</strong></p>
</div>
</div>
"""
    },
    {
        "title": "Polygon Angle Sums",
        "body": """
<h4>The General Formula for Any Polygon</h4>
<div class="concept-box">
<p><strong>Sum of interior angles = \((n - 2) \times 180°\)</strong></p>
<p>where <strong>n</strong> = number of sides</p>
<p>This works because any polygon can be divided into triangles from one vertex.</p>
</div>

<h4>Examples for Common Polygons</h4>
<div class="success-box">
<table style="width: 100%">
<tr style=";">
<th>Polygon</th><th>Sides (n)</th><th>Angle Sum Formula</th><th>Total</th>
</tr>
<tr class="formula-box">
<td>Triangle</td><td>3</td><td>\((3 - 2) \times 180°\)</td><td>180°</td>
</tr>
<tr class="formula-box">
<td>Quadrilateral</td><td>4</td><td>\((4 - 2) \times 180°\)</td><td>360°</td>
</tr>
<tr class="formula-box">
<td>Pentagon</td><td>5</td><td>\((5 - 2) \times 180°\)</td><td>540°</td>
</tr>
<tr class="formula-box">
<td>Hexagon</td><td>6</td><td>\((6 - 2) \times 180°\)</td><td>720°</td>
</tr>
<tr class="formula-box">
<td>Heptagon</td><td>7</td><td>\((7 - 2) \times 180°\)</td><td>900°</td>
</tr>
</table>
</div>

<h4>Regular Polygons: All Sides and Angles Equal</h4>
<div class="success-box">
<p><strong>Each interior angle in a regular polygon:</strong></p>
<p>\\(\\text{Each angle} = \\frac{(n-2) \\times 180°}{n}\\)</p>
</div>

<div class="warning-box">
<p><strong>Example: Find each interior angle in a regular hexagon</strong></p>
<div class="worked-example">
<p>n = 6</p>
<p>Each angle = \((6 - 2) \times 180° \div 6\)</p>
<p>Each angle = \(4 \times 180° \div 6 = 720° \div 6 = 120°\)</p>
<p><strong>Answer: 120°</strong></p>
</div>
</div>

<h4>Exterior Angles of Any Polygon</h4>
<div class="concept-box">
<p><strong>The sum of exterior angles of ANY polygon is ALWAYS 360°.</strong></p>
<p>This is because you turn through one complete rotation around the polygon.</p>
<p><strong>For regular polygons:</strong> Each exterior angle = \(360° \div n\)</p>
</div>
"""
    }
]
