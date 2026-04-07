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
<svg width="100%" height="200" viewBox="-15 -15 830 230" class="formula-box">
  <!-- Acute Angle -->
  <text x="80" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Acute (45°)</text>
  <line x1="50" y1="90" x2="150" y2="90" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="50" y1="90" x2="120" y2="40" stroke='#58a6ff' stroke-width="2.5"/>
  <path d="M 80,90 A 30,30 0 0,1 70,68" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <text x="88" y="78" fill='currentColor' font-size='11'>45°</text>

  <!-- Right Angle -->
  <text x="280" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Right (90°)</text>
  <line x1="250" y1="90" x2="350" y2="90" stroke='#56d364' stroke-width="2.5"/>
  <line x1="250" y1="90" x2="250" y2="40" stroke='#56d364' stroke-width="2.5"/>
  <polyline points="250,75 265,75 265,90" fill='none' stroke='#56d364' stroke-width="1.5"/>
  <text x="275" y="78" fill='currentColor' font-size='11'>90°</text>

  <!-- Obtuse Angle -->
  <text x="480" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Obtuse (120°)</text>
  <line x1="450" y1="90" x2="550" y2="90" stroke='#f85149' stroke-width="2.5"/>
  <line x1="450" y1="90" x2="400" y2="40" stroke='#f85149' stroke-width="2.5"/>
  <path d="M 485,90 A 35,35 0 0,1 435,60" fill='none' stroke='#ff7b72' stroke-width="2"/>
  <text x="455" y="70" fill='currentColor' font-size='11'>120°</text>

  <!-- Straight Angle -->
  <text x="680" y="25" fill='currentColor' font-size='14' font-weight='bold' text-anchor='middle'>Straight (180°)</text>
  <line x1="610" y1="90" x2="750" y2="90" stroke='#a371f7' stroke-width="2.5"/>
  <circle cx="680" cy="90" r="3" fill='#a371f7'/>
  <path d="M 710,90 A 30,30 0 0,1 650,90" fill='none' stroke='#c8b6ff' stroke-width="2"/>
  <text x="680" y="78" fill='currentColor' font-size='11' text-anchor='middle'>180°</text>
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
<svg width="100%" height="170" viewBox="-15 -15 630 200" class="formula-box">
  <!-- Base line -->
  <line x1="50" y1="90" x2="550" y2="90" stroke='#58a6ff' stroke-width="3"/>

  <!-- Rays from a common point at 300 -->
  <line x1="300" y1="90" x2="180" y2="20" stroke='#79c0ff' stroke-width="2"/>
  <line x1="300" y1="90" x2="300" y2="15" stroke='#79c0ff' stroke-width="2"/>

  <!-- Angle arcs from point 300,90 -->
  <path d="M 265,90 A 35,35 0 0,1 250,60" fill='none' stroke='#f85149' stroke-width="2"/>
  <path d="M 335,90 A 35,35 0 0,0 300,55" fill='none' stroke='#56d364' stroke-width="2"/>
  <path d="M 250,60 A 35,35 0 0,1 300,55" fill='none' stroke='#a371f7' stroke-width="2"/>

  <!-- Angle labels -->
  <text x="245" y="80" fill='currentColor' font-size='13' font-weight='bold'>60°</text>
  <text x="305" y="70" fill='currentColor' font-size='13' font-weight='bold'>50°</text>
  <text x="280" y="50" fill='currentColor' font-size='13' font-weight='bold'>70°</text>

  <!-- Point marker -->
  <circle cx="300" cy="90" r="3" fill='currentColor'/>

  <!-- Sum label -->
  <text x="300" y="145" fill='#56d364' font-size='15' font-weight='bold' text-anchor='middle'>60° + 70° + 50° = 180°</text>
</svg>

<h4>Rule 2: Angles Around a Point = 360°</h4>
<div class="success-box">
<p>When angles surround a single point, they <strong>always add to 360°</strong>. This is a complete rotation.</p>
<p><strong>Formula:</strong> \\(a + b + c + d = 360°\\)</p>
</div>

<h4>Visual: Angles Around a Point</h4>
<svg width="100%" height="230" viewBox="-15 -15 430 260" class="formula-box">
  <!-- Dashed guide circle -->
  <circle cx="200" cy="110" r="80" fill='none' stroke='#8b949e' stroke-width="1" stroke-dasharray="5,5"/>

  <!-- Rays from center -->
  <line x1="200" y1="110" x2="280" y2="50" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="200" y1="110" x2="280" y2="150" stroke='#56d364' stroke-width="2.5"/>
  <line x1="200" y1="110" x2="180" y2="190" stroke='#f85149' stroke-width="2.5"/>
  <line x1="200" y1="110" x2="120" y2="140" stroke='#a371f7' stroke-width="2.5"/>

  <!-- Angle arcs -->
  <path d="M 230,93 A 35,35 0 0,1 234,130" fill='none' stroke='#58a6ff' stroke-width="2"/>
  <path d="M 234,130 A 35,35 0 0,1 195,144" fill='none' stroke='#56d364' stroke-width="2"/>
  <path d="M 195,144 A 35,35 0 0,1 172,127" fill='none' stroke='#f85149' stroke-width="2"/>
  <path d="M 172,127 A 35,35 0 0,1 230,93" fill='none' stroke='#a371f7' stroke-width="2"/>

  <!-- Angle labels -->
  <text x="245" y="100" fill='currentColor' font-size='13' font-weight='bold'>80°</text>
  <text x="235" y="155" fill='currentColor' font-size='13' font-weight='bold'>110°</text>
  <text x="155" y="165" fill='currentColor' font-size='13' font-weight='bold'>95°</text>
  <text x="145" y="105" fill='currentColor' font-size='13' font-weight='bold'>75°</text>

  <!-- Center point -->
  <circle cx="200" cy="110" r="3.5" fill='currentColor'/>

  <!-- Sum label -->
  <text x="200" y="220" fill='#79c0ff' font-size='14' font-weight='bold' text-anchor='middle'>Sum = 360°</text>
</svg>

<h4>Complementary Angles</h4>
<div class="success-box">
<p>Two angles that add to 90° are <strong>complementary</strong>.</p>
<p><strong>Example:</strong> 35° and 55° are complementary because \(35° + 55° = 90°\)</p>
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
<svg width="100%" height="260" viewBox="-15 -15 530 290" class="formula-box">
  <!-- Two crossing lines -->
  <line x1="80" y1="40" x2="420" y2="210" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="420" y1="40" x2="80" y2="210" stroke='#56d364' stroke-width="2.5"/>

  <!-- Intersection point -->
  <circle cx="250" cy="125" r="4" fill='currentColor'/>

  <!-- Angle arcs - blue pair (vertically opposite) -->
  <path d="M 285,108 A 40,40 0 0,1 268,90" fill='none' stroke='#79c0ff' stroke-width="2.5"/>
  <path d="M 215,142 A 40,40 0 0,1 232,160" fill='none' stroke='#79c0ff' stroke-width="2.5"/>

  <!-- Angle arcs - red pair (vertically opposite) -->
  <path d="M 268,90 A 40,40 0 0,1 215,108" fill='none' stroke='#f8a5a5' stroke-width="2.5"/>
  <path d="M 232,160 A 40,40 0 0,1 285,142" fill='none' stroke='#f8a5a5' stroke-width="2.5"/>

  <!-- Angle labels -->
  <text x="295" y="98" fill='#79c0ff' font-size='14' font-weight='bold'>60°</text>
  <text x="175" y="168" fill='#79c0ff' font-size='14' font-weight='bold'>60°</text>
  <text x="175" y="98" fill='#f8a5a5' font-size='14' font-weight='bold'>120°</text>
  <text x="290" y="168" fill='#f8a5a5' font-size='14' font-weight='bold'>120°</text>

  <!-- Legend -->
  <text x="100" y="240" fill='currentColor' font-size='13'>Blue angles (opposite) = 60° each</text>
  <text x="100" y="258" fill='currentColor' font-size='13'>Red angles (opposite) = 120° each</text>
</svg>

<h4>Worked Example</h4>
<div class="warning-box">
<p><strong>Two lines intersect. If one angle is 50°, find all four angles.</strong></p>
<div class="worked-example">
<p><strong>Solution:</strong></p>
<ul>
<li>One angle = 50°</li>
<li>Opposite angle = 50° (vertically opposite)</li>
<li>Adjacent angle = \(180° - 50° = 130°\) (supplementary)</li>
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
<svg width="100%" height="300" viewBox="-15 -15 730 330" class="formula-box">
  <!-- Parallel lines -->
  <line x1="50" y1="70" x2="650" y2="70" stroke='#58a6ff' stroke-width="2.5"/>
  <line x1="50" y1="190" x2="650" y2="190" stroke='#58a6ff' stroke-width="2.5"/>

  <!-- Parallel arrows -->
  <text x="20" y="74" fill='#58a6ff' font-size='14' font-weight='bold'>//</text>
  <text x="20" y="194" fill='#58a6ff' font-size='14' font-weight='bold'>//</text>

  <!-- Transversal -->
  <line x1="230" y1="15" x2="470" y2="245" stroke='#56d364' stroke-width="2.5"/>

  <!-- Intersection points -->
  <circle cx="295" cy="70" r="3" fill='currentColor'/>
  <circle cx="405" cy="190" r="3" fill='currentColor'/>

  <!-- Angle arcs at top intersection -->
  <path d="M 325,70 A 30,30 0 0,0 310,46" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 265,70 A 30,30 0 0,0 280,94" fill='none' stroke='#f8a5a5' stroke-width="2"/>

  <!-- Angle arcs at bottom intersection -->
  <path d="M 435,190 A 30,30 0 0,0 420,166" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 375,190 A 30,30 0 0,0 390,214" fill='none' stroke='#f8a5a5' stroke-width="2"/>

  <!-- Angle labels -->
  <text x="330" y="55" fill='#79c0ff' font-size='14' font-weight='bold'>a</text>
  <text x="255" y="100" fill='#f8a5a5' font-size='14' font-weight='bold'>b</text>
  <text x="440" y="175" fill='#79c0ff' font-size='14' font-weight='bold'>c</text>
  <text x="365" y="220" fill='#f8a5a5' font-size='14' font-weight='bold'>d</text>

  <!-- Annotations -->
  <text x="50" y="268" fill='currentColor' font-size='13' font-weight='bold'>Corresponding: a = c</text>
  <text x="270" y="268" fill='currentColor' font-size='13' font-weight='bold'>Alternate: b = c</text>
  <text x="490" y="268" fill='currentColor' font-size='13' font-weight='bold'>Co-interior: b + c = 180°</text>

  <text x="350" y="295" fill='#a371f7' font-size='12' text-anchor='middle'>If a = 60°, then c = 60°, b = 120°, d = 120°</text>
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
