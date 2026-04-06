TITLE = "Quadrilaterals and Their Properties"

SECTIONS = [
    {
        "title": "The Quadrilateral Angle Sum",
        "body": """
<h4>First Principle: All Quadrilaterals Have 360° Total Angle</h4>
<div class="concept-box">
<p><strong>The sum of all interior angles in ANY quadrilateral is ALWAYS 360°.</strong></p>
<p>This is because a quadrilateral can be divided into 2 triangles (each with 180°).</p>
<p>\\(\\angle A + \\angle B + \\angle C + \\angle D = 360°\\)</p>
</div>

<h4>Why? Proof by Triangulation</h4>
<div class="success-box">
<p>Draw a diagonal across the quadrilateral. This divides it into 2 triangles.</p>
<p>Each triangle has angles that sum to 180°.</p>
<p>Total: \(180° + 180° = 360°\)</p>

<svg width="100%" height="200" viewBox="0 0 500 200" class="formula-box">
  <!-- Quadrilateral -->
  <polygon points="150,160 100,80 250,40 350,120" fill='none' stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Diagonal -->
  <line x1="150" y1="160" x2="250" y2="40" stroke='#56d364' stroke-width="2" stroke-dasharray="5,5"/>

  <!-- Vertices -->
  <circle cx="150" cy="160" r="3" fill='#f85149'/>
  <circle cx="100" cy="80" r="3" fill='#f85149'/>
  <circle cx="250" cy="40" r="3" fill='#f85149'/>
  <circle cx="350" cy="120" r="3" fill='#f85149'/>

  <!-- Labels -->
  <text x="140" y="175" fill='#79c0ff' font-size='12' font-weight='bold'>A</text>
  <text x="85" y="85" fill='#79c0ff' font-size='12' font-weight='bold'>B</text>
  <text x="245" y="25" fill='#79c0ff' font-size='12' font-weight='bold'>C</text>
  <text x="360" y="125" fill='#79c0ff' font-size='12' font-weight='bold'>D</text>

  <text x="50" y="130" fill='currentColor' font-size='11'>Triangle 1: A + B + part of C = 180°</text>
  <text x="50" y="150" fill='currentColor' font-size='11'>Triangle 2: part of C + D + part of A = 180°</text>
</svg>
</div>

<h4>Finding Missing Angles: Example</h4>
<div class="warning-box">
<p><strong>A quadrilateral has angles 70°, 85°, 95°, and x. Find x.</strong></p>
<div class="worked-example">
<p>\(70° + 85° + 95° + x = 360°\)</p>
<p>\(250° + x = 360°\)</p>
<p><strong>\(x = 110°\)</strong></p>
</div>
</div>
"""
    },
    {
        "title": "Special Quadrilaterals: Parallelograms",
        "body": """
<h4>Properties of a Parallelogram</h4>
<div class="concept-box">
<p>A <strong>parallelogram</strong> has opposite sides parallel and equal in length.</p>
<p><strong>Key Properties:</strong></p>
<ul >
<li>Opposite sides are equal and parallel</li>
<li>Opposite angles are equal</li>
<li>Adjacent angles are supplementary (add to 180°)</li>
<li>Diagonals bisect each other (cross at their midpoints)</li>
</ul>
</div>

<h4>Visual: Parallelogram Properties</h4>
<svg width="100%" height="240" viewBox="0 0 500 240" class="formula-box">
  <!-- Parallelogram -->
  <polygon points="100,180 150,80 350,80 300,180" fill='none' stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Diagonals -->
  <line x1="100" y1="180" x2="350" y2="80" stroke='#56d364' stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="150" y1="80" x2="300" y2="180" stroke='#56d364' stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Center point -->
  <circle cx="225" cy="130" r="3" fill='#f85149'/>

  <!-- Vertices -->
  <circle cx="100" cy="180" r="3" fill='#f85149'/>
  <circle cx="150" cy="80" r="3" fill='#f85149'/>
  <circle cx="350" cy="80" r="3" fill='#f85149'/>
  <circle cx="300" cy="180" r="3" fill='#f85149'/>

  <!-- Angle labels -->
  <text x="110" y="165" fill='#79c0ff' font-size='12' font-weight='bold'>x</text>
  <text x="155" y="95" fill='#79c0ff' font-size='12' font-weight='bold'>y</text>
  <text x="340" y="95" fill='#79c0ff' font-size='12' font-weight='bold'>x</text>
  <text x="290" y="165" fill='#79c0ff' font-size='12' font-weight='bold'>y</text>

  <!-- Side labels -->
  <text x="115" y="200" fill='#a371f7' font-size='11' font-weight='bold'>a</text>
  <text x="230" y="65" fill='#a371f7' font-size='11' font-weight='bold'>b</text>
  <text x="310" y="200" fill='#a371f7' font-size='11' font-weight='bold'>a</text>
  <text x="140" y="135" fill='#a371f7' font-size='11' font-weight='bold'>b</text>

  <!-- Properties text -->
  <text x="50" y="220" fill='currentColor' font-size='11'>Opposite angles equal: x and x, y and y</text>
  <text x="50" y="235" fill='currentColor' font-size='11'>Opposite sides equal: a and a, b and b</text>
</svg>

<h4>Special Types of Parallelograms</h4>

<div class="success-box">
<h5>Rectangle</h5>
<p>A parallelogram with <strong>all angles 90°</strong>. Opposite sides are equal. Diagonals are equal in length.</p>
</div>

<div class="success-box">
<h5>Rhombus (Diamond)</h5>
<p>A parallelogram with <strong>all sides equal</strong>. Opposite angles are equal. Diagonals bisect the angles and meet at right angles.</p>
</div>

<div class="success-box">
<h5>Square</h5>
<p>A parallelogram that is both a rectangle AND a rhombus. <strong>All sides equal, all angles 90°.</strong> Diagonals are equal and meet at right angles.</p>
</div>
"""
    },
    {
        "title": "Other Important Quadrilaterals",
        "body": """
<h4>Trapezium (Trapezoid)</h4>
<div class="concept-box">
<p>A <strong>trapezium</strong> has one pair of parallel sides (and the other pair is not parallel).</p>
<p><strong>Key Property:</strong> Co-interior angles on the same side add to 180°.</p>

<svg width="100%" height="160" viewBox="0 0 400 160" class="formula-box">
  <!-- Trapezium -->
  <polygon points="80,130 120,50 280,50 320,130" fill='none' stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Parallel sides marker -->
  <line x1="85" y1="135" x2="75" y2="135" stroke='#56d364' stroke-width="2"/>
  <line x1="125" y1="45" x2="275" y2="45" stroke='#56d364' stroke-width="2"/>
  <line x1="275" y1="45" x2="285" y2="45" stroke='#56d364' stroke-width="2"/>
  <line x1="315" y1="135" x2="325" y2="135" stroke='#56d364' stroke-width="2"/>

  <!-- Vertices -->
  <circle cx="80" cy="130" r="2" fill='#f85149'/>
  <circle cx="120" cy="50" r="2" fill='#f85149'/>
  <circle cx="280" cy="50" r="2" fill='#f85149'/>
  <circle cx="320" cy="130" r="2" fill='#f85149'/>

  <text x="85" y="130" fill='currentColor' font-size='11' font-weight='bold'>A</text>
  <text x="115" y="50" fill='currentColor' font-size='11' font-weight='bold'>B</text>
  <text x="285" y="50" fill='currentColor' font-size='11' font-weight='bold'>C</text>
  <text x="320" y="130" fill='currentColor' font-size='11' font-weight='bold'>D</text>
</svg>
</div>

<h4>Kite</h4>
<div class="success-box">
<p>A <strong>kite</strong> has two pairs of adjacent sides that are equal.</p>
<p><strong>Key Properties:</strong></p>
<ul >
<li>One diagonal is the line of symmetry</li>
<li>Diagonals meet at right angles</li>
<li>One pair of opposite angles are equal</li>
</ul>
</div>

<h4>Quadrilateral Hierarchy</h4>
<div class="warning-box">
<svg width="100%" height="310" viewBox="0 0 500 310" class="formula-box">
  <!-- Quadrilateral (top) -->
  <rect x="150" y="20" width="200" height="40" fill='#161b22' stroke='#58a6ff' stroke-width="2" rx="5"/>
  <text x="200" y="50" fill='currentColor' font-size='13' font-weight='bold'>Quadrilateral</text>

  <!-- Trapezium -->
  <rect x="30" y="100" width="120" height="40" fill='#161b22' stroke='#56d364' stroke-width="2" rx="5"/>
  <text x="40" y="130" fill='currentColor' font-size='12' font-weight='bold'>Trapezium</text>
  <line x1="150" y1="60" x2="70" y2="100" stroke='#30363d' stroke-width="1"/>

  <!-- Parallelogram -->
  <rect x="190" y="100" width="120" height="40" fill='#161b22' stroke='#56d364' stroke-width="2" rx="5"/>
  <text x="200" y="130" fill='currentColor' font-size='12' font-weight='bold'>Parallelogram</text>
  <line x1="250" y1="60" x2="250" y2="100" stroke='#30363d' stroke-width="1"/>

  <!-- Kite -->
  <rect x="350" y="100" width="120" height="40" fill='#161b22' stroke='#56d364' stroke-width="2" rx="5"/>
  <text x="365" y="130" fill='currentColor' font-size='12' font-weight='bold'>Kite</text>
  <line x1="350" y1="60" x2="400" y2="100" stroke='#30363d' stroke-width="1"/>

  <!-- Rectangle -->
  <rect x="115" y="180" width="120" height="40" fill='#161b22' stroke='#a371f7' stroke-width="2" rx="5"/>
  <text x="135" y="210" fill='currentColor' font-size='12' font-weight='bold'>Rectangle</text>
  <line x1="250" y1="100" x2="175" y2="180" stroke='#30363d' stroke-width="1"/>

  <!-- Rhombus -->
  <rect x="265" y="180" width="120" height="40" fill='#161b22' stroke='#a371f7' stroke-width="2" rx="5"/>
  <text x="285" y="210" fill='currentColor' font-size='12' font-weight='bold'>Rhombus</text>
  <line x1="250" y1="100" x2="325" y2="180" stroke='#30363d' stroke-width="1"/>

  <!-- Square -->
  <rect x="190" y="260" width="120" height="40" fill='#161b22' stroke='#f85149' stroke-width="2.5" rx="5"/>
  <text x="220" y="290" fill='currentColor' font-size='12' font-weight='bold'>Square</text>
  <line x1="175" y1="220" x2="240" y2="260" stroke='#30363d' stroke-width="1"/>
  <line x1="325" y1="220" x2="260" y2="260" stroke='#30363d' stroke-width="1"/>

  <text x="20" y="25" fill='currentColor' font-size='10' font-style="italic">Hierarchy: boxes below inherit properties from boxes above</text>
</svg>
</div>
"""
    },
    {
        "title": "Key Angle Properties in Quadrilaterals",
        "body": """
<h4>Angles in Different Quadrilaterals</h4>

<div class="success-box">
<h5>Parallelogram</h5>
<ul >
<li>Opposite angles are equal</li>
<li>Adjacent angles are supplementary: \\(\\angle A + \\angle B = 180°\\)</li>
</ul>
</div>

<div class="success-box">
<h5>Rectangle</h5>
<ul >
<li>All four angles are 90°</li>
<li>Sum = 360° (like all quadrilaterals)</li>
</ul>
</div>

<div class="success-box">
<h5>Rhombus</h5>
<ul >
<li>Opposite angles are equal</li>
<li>Adjacent angles are supplementary</li>
<li>Diagonals bisect the angles</li>
</ul>
</div>

<div class="success-box">
<h5>Trapezium</h5>
<ul >
<li>Co-interior angles on the same side of parallel sides add to 180°</li>
<li>If isosceles trapezium: base angles are equal</li>
</ul>
</div>

<h4>Worked Example: Finding Angles</h4>
<div class="warning-box">
<p><strong>A parallelogram has one angle of 65°. Find the other three angles.</strong></p>
<div class="worked-example">
<p>In a parallelogram:</p>
<ul>
<li>Opposite angle = 65° (opposite angles equal)</li>
<li>Adjacent angle = 180° - 65° = 115° (supplementary)</li>
<li>Opposite to adjacent = 115°</li>
<p><strong>Answer: 65°, 115°, 65°, 115°</strong></p>
</ul>
</div>
</div>
"""
    }
]
