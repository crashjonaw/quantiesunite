TITLE = "Angle Properties and Relationships"

SECTIONS = [
    {
        "title": "Understanding Angles and Their Types",
        "body": """
<div class="concept-box">
<h3>First Principle: Angles measure how far shapes turn</h3>
<p>An <strong>angle</strong> is formed when two lines meet at a point. We measure angles in <strong>degrees (°)</strong>, where a full rotation is 360°.</p>
</div>

<h4>Types of Angles</h4>
<div class="success-box">
<table style="width: 100%">
<tr style=";">
<th>Angle Type</th><th>Size</th><th>Description</th>
</tr>
<tr class="formula-box">
<td><strong>Acute</strong></td><td>0° to 90°</td><td>Sharp angle, less than a right angle</td>
</tr>
<tr class="formula-box">
<td><strong>Right</strong></td><td>Exactly 90°</td><td>Perfect corner (shown with a small square ⊏)</td>
</tr>
<tr class="formula-box">
<td><strong>Obtuse</strong></td><td>90° to 180°</td><td>Wide angle, more than a right angle</td>
</tr>
<tr class="formula-box">
<td><strong>Straight</strong></td><td>Exactly 180°</td><td>A flat line</td>
</tr>
<tr class="formula-box">
<td><strong>Reflex</strong></td><td>180° to 360°</td><td>Large angle, more than a straight line</td>
</tr>
</table>
</div>

<h4>Visual: Angle Types</h4>
<svg width="100%" height="200" viewBox="0 0 800 200" class="formula-box">
  <!-- Acute Angle -->
  <text x="40" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Acute (45°)</text>
  <line x1="50" y1="80" x2="120" y2="80" stroke='#58a6ff' stroke-width="2"/>
  <line x1="50" y1="80" x2="100" y2="130" stroke='#58a6ff' stroke-width="2"/>
  <circle cx="50" cy="80" r="25" fill='none' stroke='#79c0ff' stroke-width="1.5"/>

  <!-- Right Angle -->
  <text x="200" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Right (90°)</text>
  <line x1="210" y1="80" x2="280" y2="80" stroke='#56d364' stroke-width="2"/>
  <line x1="210" y1="80" x2="210" y2="150" stroke='#56d364' stroke-width="2"/>
  <rect x="210" y="80" width="15" height="15" fill='none' stroke='#56d364' stroke-width="1.5"/>

  <!-- Obtuse Angle -->
  <text x="380" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Obtuse (120°)</text>
  <line x1="390" y1="80" x2="480" y2="80" stroke='#f85149' stroke-width="2"/>
  <line x1="390" y1="80" x2="340" y2="130" stroke='#f85149' stroke-width="2"/>
  <circle cx="390" cy="80" r="35" fill='none' stroke='#ff7b72' stroke-width="1.5"/>

  <!-- Straight Angle -->
  <text x="580" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>Straight (180°)</text>
  <line x1="580" y1="80" x2="750" y2="80" stroke='#a371f7' stroke-width="2"/>
  <line x1="665" y1="80" x2="665" y2="100" stroke='#a371f7' stroke-width="1"/>
  <text x="630" y="125" fill='#e6edf3' font-size='12'>A flat line</text>
</svg>
"""
    },
    {
        "title": "Angles on a Straight Line and Around a Point",
        "body": """
<h4>Rule 1: Angles on a Straight Line = 180°</h4>
<div class="success-box">
<p>When angles sit on a straight line, they <strong>always add to 180°</strong>. These are called <strong>supplementary angles</strong>.</p>
<p><strong>Formula:</strong> \\(a + b + c = 180°\\)</p>
</div>

<h4>Visual: Angles on a Line</h4>
<svg width="100%" height="160" viewBox="0 0 600 160" class="formula-box">
  <line x1="50" y1="80" x2="550" y2="80" stroke='#58a6ff' stroke-width="3"/>
  <line x1="150" y1="80" x2="150" y2="30" stroke='#79c0ff' stroke-width="2"/>
  <line x1="250" y1="80" x2="250" y2="40" stroke='#79c0ff' stroke-width="2"/>
  <line x1="350" y1="80" x2="350" y2="50" stroke='#79c0ff' stroke-width="2"/>

  <text x="140" y="25" fill='#e6edf3' font-size='14' font-weight='bold'>60°</text>
  <text x="240" y="35" fill='#e6edf3' font-size='14' font-weight='bold'>70°</text>
  <text x="340" y="45" fill='#e6edf3' font-size='14' font-weight='bold'>50°</text>
  <text x="280" y="130" fill='#56d364' font-size='16' font-weight='bold'>60° + 70° + 50° = 180°</text>
</svg>

<h4>Rule 2: Angles Around a Point = 360°</h4>
<div class="success-box">
<p>When angles surround a single point, they <strong>always add to 360°</strong>. This is a complete rotation.</p>
<p><strong>Formula:</strong> \\(a + b + c + d = 360°\\)</p>
</div>

<h4>Visual: Angles Around a Point</h4>
<svg width="100%" height="200" viewBox="0 0 400 200" class="formula-box">
  <circle cx="200" cy="100" r="80" fill='none' stroke='#8b949e' stroke-width="1.5" stroke-dasharray="5,5"/>

  <line x1="200" y1="100" x2="270" y2="40" stroke='#58a6ff' stroke-width="2"/>
  <line x1="200" y1="100" x2="280" y2="120" stroke='#56d364' stroke-width="2"/>
  <line x1="200" y1="100" x2="220" y2="175" stroke='#f85149' stroke-width="2"/>
  <line x1="200" y1="100" x2="120" y2="160" stroke='#a371f7' stroke-width="2"/>

  <text x="260" y="50" fill='#e6edf3' font-size='13' font-weight='bold'>80°</text>
  <text x="285" y="115" fill='#e6edf3' font-size='13' font-weight='bold'>110°</text>
  <text x="215" y="175" fill='#e6edf3' font-size='13' font-weight='bold'>95°</text>
  <text x="110" y="155" fill='#e6edf3' font-size='13' font-weight='bold'>75°</text>

  <circle cx="200" cy="100" r="3" fill='#e6edf3'/>
  <text x="150" y="130" fill='#79c0ff' font-size='12' font-weight='bold'>Sum = 360°</text>
</svg>

<h4>Complementary Angles</h4>
<div class="success-box">
<p>Two angles that add to 90° are <strong>complementary</strong>.</p>
<p><strong>Example:</strong> 35° and 55° are complementary because 35° + 55° = 90°</p>
</div>
"""
    },
    {
        "title": "Vertically Opposite Angles",
        "body": """
<h4>Rule: Vertically Opposite Angles are Equal</h4>
<div class="concept-box">
<p>When <strong>two straight lines cross</strong>, the angles opposite each other (called <strong>vertically opposite</strong> or <strong>vertical angles</strong>) are <strong>always equal</strong>.</p>
<p><strong>Why?</strong> Both angles add to 180° with the same adjacent angle, so they must be equal to each other.</p>
</div>

<h4>Visual: Vertically Opposite Angles</h4>
<svg width="100%" height="250" viewBox="0 0 500 250" class="formula-box">
  <!-- Lines crossing -->
  <line x1="100" y1="50" x2="380" y2="200" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="380" y1="50" x2="100" y2="200" stroke='#56d364' stroke-width="2.5"/>

  <!-- Intersection point -->
  <circle cx="240" cy="125" r="4" fill='#f85149'/>

  <!-- Angle arcs -->
  <path d="M 280 125 A 25 25 0 0 0 260 100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 200 125 A 25 25 0 0 0 220 150" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 260 125 A 25 25 0 0 1 280 150" fill='none' stroke='#f8a5a5' stroke-width="2"/>
  <path d="M 220 125 A 25 25 0 0 1 200 100" fill='none' stroke='#f8a5a5' stroke-width="2"/>

  <!-- Angle labels -->
  <text x="295" y="125" fill='#79c0ff' font-size='14' font-weight='bold'>60°</text>
  <text x="195" y="160" fill='#79c0ff' font-size='14' font-weight='bold'>60°</text>
  <text x="250" y="160" fill='#f8a5a5' font-size='14' font-weight='bold'>120°</text>
  <text x="205" y="105" fill='#f8a5a5' font-size='14' font-weight='bold'>120°</text>

  <!-- Labels -->
  <text x="100" y="240" fill='#e6edf3' font-size='13'>Blue angles (opposite) = 60° each</text>
  <text x="100" y="225" fill='#e6edf3' font-size='13'>Red angles (opposite) = 120° each</text>
</svg>

<h4>Worked Example</h4>
<div class="warning-box">
<p><strong>Two lines intersect. If one angle is 50°, find all four angles.</strong></p>
<div class="worked-example">
<p><strong>Solution:</strong></p>
<ul>
<li>One angle = 50°</li>
<li>Opposite angle = 50° (vertically opposite)</li>
<li>Adjacent angle = 180° - 50° = 130° (supplementary)</li>
<li>Opposite to adjacent = 130° (vertically opposite)</li>
<li><strong>Answer: 50°, 130°, 50°, 130°</strong></li>
</ul>
</div>
</div>
"""
    },
    {
        "title": "Parallel Lines and Transversals",
        "body": """
<h4>What is a Transversal?</h4>
<div class="concept-box">
<p>A <strong>transversal</strong> is a line that crosses two or more other lines. When a transversal crosses two <strong>parallel lines</strong> (lines that never meet), special angle relationships appear.</p>
</div>

<h4>Three Key Angle Relationships</h4>

<div class="success-box">
<h5>1. Corresponding Angles are Equal</h5>
<p>Angles in the <strong>same position</strong> at each intersection are equal.</p>
<p><strong>Visual position:</strong> Both on the same side of the transversal, one above and one below the parallel lines.</p>
</div>

<div class="success-box">
<h5>2. Alternate Angles are Equal</h5>
<p>Angles on <strong>opposite sides</strong> of the transversal, between the parallel lines, are equal.</p>
<p><strong>Visual position:</strong> They form a Z-shape pattern.</p>
</div>

<div class="success-box">
<h5>3. Co-interior Angles Add to 180°</h5>
<p>Angles on the <strong>same side</strong> of the transversal, between the parallel lines, are supplementary (add to 180°).</p>
<p><strong>Visual position:</strong> They form a C-shape pattern.</p>
</div>

<h4>Visual: All Three Relationships</h4>
<svg width="100%" height="280" viewBox="0 0 700 280" class="formula-box">
  <!-- Parallel lines -->
  <line x1="50" y1="60" x2="650" y2="60" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="50" y1="180" x2="650" y2="180" stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Transversal -->
  <line x1="200" y1="10" x2="500" y2="230" stroke='#56d364' stroke-width="2.5"/>

  <!-- Angles at top intersection -->
  <text x="220" y="50" fill='#79c0ff' font-size='13' font-weight='bold'>a</text>
  <text x="220" y="85" fill='#f8a5a5' font-size='13' font-weight='bold'>b</text>

  <!-- Angles at bottom intersection -->
  <text x="350" y="170" fill='#79c0ff' font-size='13' font-weight='bold'>c</text>
  <text x="350" y="205" fill='#f8a5a5' font-size='13' font-weight='bold'>d</text>

  <!-- Annotations -->
  <text x="50" y="250" fill='#e6edf3' font-size='12'><tspan font-weight='bold'>Corresponding:</tspan> a = c</text>
  <text x="250" y="250" fill='#e6edf3' font-size='12'><tspan font-weight='bold'>Alternate:</tspan> b = c</text>
  <text x="450" y="250" fill='#e6edf3' font-size='12'><tspan font-weight='bold'>Co-interior:</tspan> b + c = 180°</text>

  <text x="50" y="270" fill='#a371f7' font-size='11'>If transversal angle = 60°, then: a = 60°, c = 60°, b = 120°, d = 120°</text>
</svg>

<h4>Worked Example</h4>
<div class="warning-box">
<p><strong>Two parallel lines are cut by a transversal. One angle is 75°. Find the corresponding angle.</strong></p>
<div class="worked-example">
<p><strong>Solution:</strong></p>
<ul>
<li>Given angle = 75°</li>
<li>Corresponding angles are equal (Rule 1)</li>
<li><strong>Answer: 75°</strong></li>
</ul>
</div>
</div>
"""
    }
]
