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

<svg width="100%" height="220" viewBox="0 0 500 220" class="formula-box">
  <!-- Parallel line -->
  <line x1="100" y1="80" x2="400" y2="80" stroke='#58a6ff' stroke-width="2" stroke-dasharray="5,5"/>

  <!-- Triangle -->
  <line x1="250" y1="30" x2="150" y2="150" stroke='#56d364' stroke-width="2.5"/>
  <line x1="250" y1="30" x2="350" y2="150" stroke='#56d364' stroke-width="2.5"/>
  <line x1="150" y1="150" x2="350" y2="150" stroke='#56d364' stroke-width="2.5"/>

  <!-- Angle markers -->
  <circle cx="250" cy="30" r="3" fill='#f85149'/>
  <circle cx="150" cy="150" r="3" fill='#f85149'/>
  <circle cx="350" cy="150" r="3" fill='#f85149'/>

  <!-- Angle labels -->
  <text x="245" y="55" fill='#79c0ff' font-size='13' font-weight='bold'>A</text>
  <text x="130" y="160" fill='#79c0ff' font-size='13' font-weight='bold'>B</text>
  <text x="360" y="160" fill='#79c0ff' font-size='13' font-weight='bold'>C</text>

  <!-- Parallel line angles -->
  <text x="110" y="95" fill='#e6edf3' font-size='12' font-weight='bold'>(= B)</text>
  <text x="370" y="95" fill='#e6edf3' font-size='12' font-weight='bold'>(= C)</text>

  <text x="100" y="200" fill='#56d364' font-size='12' font-weight='bold'>A + B + C = angles on line = 180°</text>
</svg>
</div>

<h4>Finding Missing Angles: Worked Examples</h4>

<div class="warning-box">
<p><strong>Example 1: Find the missing angle if two angles are 50° and 70°</strong></p>
<div class="worked-example">
<p>50° + 70° + x = 180°</p>
<p>120° + x = 180°</p>
<p><strong>x = 60°</strong></p>
</div>
</div>

<div class="warning-box">
<p><strong>Example 2: Find all angles if they are in the ratio 2:3:4</strong></p>
<div class="worked-example">
<p>Let angles be 2k, 3k, and 4k</p>
<p>2k + 3k + 4k = 180°</p>
<p>9k = 180°</p>
<p>k = 20°</p>
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
<svg width="100%" height="240" viewBox="0 0 700 240" class="formula-box">
  <!-- Equilateral -->
  <text x="30" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Equilateral</text>
  <polygon points="80,180 50,100 110,100" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <text x="70" y="125" fill='#79c0ff' font-size='12' font-weight='bold'>60°</text>

  <!-- Isosceles -->
  <text x="160" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Isosceles</text>
  <polygon points="210,180 160,80 260,80" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <text x="195" y="140" fill='#79c0ff' font-size='12' font-weight='bold'>70°</text>
  <text x="245" y="140" fill='#79c0ff' font-size='12' font-weight='bold'>70°</text>

  <!-- Scalene -->
  <text x="310" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Scalene</text>
  <polygon points="360,180 310,90 400,120" fill='none' stroke='#f85149' stroke-width="2.5"/>
  <text x="330" y="120" fill='#ff7b72' font-size='11' font-weight='bold'>40°</text>
  <text x="370" y="100" fill='#ff7b72' font-size='11' font-weight='bold'>75°</text>

  <!-- Right-angled -->
  <text x="480" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Right-angled</text>
  <polygon points="530,180 480,100 530,100" fill='none' stroke='#a371f7' stroke-width="2.5"/>
  <rect x="530" y="100" width="12" height="12" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="495" y="145" fill='#c8b6ff' font-size='11' font-weight='bold'>90°</text>

  <!-- Acute -->
  <text x="30" y="230" fill='#e6edf3' font-size='12'>All angles < 90°</text>

  <!-- Obtuse -->
  <text x="600" y="230" fill='#e6edf3' font-size='12'>One angle > 90°</text>
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
<svg width="100%" height="240" viewBox="0 0 500 240" class="formula-box">
  <!-- Triangle -->
  <line x1="150" y1="160" x2="250" y2="50" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="250" y1="50" x2="350" y2="160" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="150" y1="160" x2="350" y2="160" stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Extended line -->
  <line x1="350" y1="160" x2="430" y2="160" stroke='#56d364' stroke-width="2.5" stroke-dasharray="5,5"/>

  <!-- Vertices -->
  <circle cx="150" cy="160" r="3" fill='#f85149'/>
  <circle cx="250" cy="50" r="3" fill='#f85149'/>
  <circle cx="350" cy="160" r="3" fill='#f85149'/>

  <!-- Angle labels -->
  <text x="160" y="145" fill='#79c0ff' font-size='13' font-weight='bold'>B</text>
  <text x="240" y="70" fill='#79c0ff' font-size='13' font-weight='bold'>A</text>
  <text x="325" y="145" fill='#79c0ff' font-size='13' font-weight='bold'>C</text>
  <text x="380" y="145" fill='#f8a5a5' font-size='13' font-weight='bold'>Ext</text>

  <!-- Angle arcs -->
  <path d="M 350 160 A 30 30 0 0 0 380 160" fill='none' stroke='#f8a5a5' stroke-width="2"/>

  <!-- Explanation -->
  <text x="50" y="200" fill='#e6edf3' font-size='12' font-weight='bold'>Exterior angle = A + B</text>
  <text x="50" y="220" fill='#e6edf3' font-size='11'>Also, Exterior angle + C = 180°</text>
  <text x="50" y="235" fill='#e6edf3' font-size='11'>(because they form a straight line)</text>
</svg>

<h4>Worked Example</h4>
<div class="warning-box">
<p><strong>A triangle has angles 50°, 70°, and 60°. Find the exterior angle at the 60° vertex.</strong></p>
<div class="worked-example">
<p><strong>Method 1: Using the theorem</strong></p>
<p>Exterior angle = 50° + 70° = 120°</p>
<p></p>
<p><strong>Method 2: Using supplementary angles</strong></p>
<p>Exterior angle + 60° = 180° (straight line)</p>
<p>Exterior angle = 180° - 60° = 120°</p>
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
<p><strong>Sum of interior angles = (n - 2) × 180°</strong></p>
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
<td>Triangle</td><td>3</td><td>(3 - 2) × 180°</td><td>180°</td>
</tr>
<tr class="formula-box">
<td>Quadrilateral</td><td>4</td><td>(4 - 2) × 180°</td><td>360°</td>
</tr>
<tr class="formula-box">
<td>Pentagon</td><td>5</td><td>(5 - 2) × 180°</td><td>540°</td>
</tr>
<tr class="formula-box">
<td>Hexagon</td><td>6</td><td>(6 - 2) × 180°</td><td>720°</td>
</tr>
<tr class="formula-box">
<td>Heptagon</td><td>7</td><td>(7 - 2) × 180°</td><td>900°</td>
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
<p>Each angle = (6 - 2) × 180° ÷ 6</p>
<p>Each angle = 4 × 180° ÷ 6 = 720° ÷ 6 = 120°</p>
<p><strong>Answer: 120°</strong></p>
</div>
</div>

<h4>Exterior Angles of Any Polygon</h4>
<div class="concept-box">
<p><strong>The sum of exterior angles of ANY polygon is ALWAYS 360°.</strong></p>
<p>This is because you turn through one complete rotation around the polygon.</p>
<p><strong>For regular polygons:</strong> Each exterior angle = 360° ÷ n</p>
</div>
"""
    }
]
