TITLE = "The Cartesian Plane and Axes"

SECTIONS = [
    {
        "title": "Introduction: What is the Cartesian Plane?",
        "body": """<html><body><p><strong>A map uses two numbers — latitude and longitude — to pinpoint any location on Earth. Mathematics does the same thing: TWO numbers (x, y) can locate any point on a flat surface. This is the Cartesian coordinate system, invented by René Descartes.</strong></p>

<div class="concept-box">
<p>The <strong>Cartesian plane</strong> is a 2D grid formed by two perpendicular number lines:</p>
<ul>
<li><strong>Horizontal axis (x-axis):</strong> Runs left to right</li>
<li><strong>Vertical axis (y-axis):</strong> Runs up and down</li>
<li><strong>Origin:</strong> The point (0, 0) where the axes meet</li>
</ul>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="300" height="300">
  <!-- Grid lines -->
  <g stroke='#30363d' stroke-width="0.5">
    <line x1="-100" y1="0" x2="100" y2="0" />
    <line x1="0" y1="-100" x2="0" y2="100" />
    <line x1="-100" y1="-20" x2="100" y2="-20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-40" x2="100" y2="-40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-60" x2="100" y2="-60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-80" x2="100" y2="-80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="20" x2="100" y2="20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="40" x2="100" y2="40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="60" x2="100" y2="60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="80" x2="100" y2="80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-20" y1="-100" x2="-20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-40" y1="-100" x2="-40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-60" y1="-100" x2="-60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-80" y1="-100" x2="-80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="20" y1="-100" x2="20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="40" y1="-100" x2="40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="60" y1="-100" x2="60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="80" y1="-100" x2="80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
  </g>

  <!-- Axes -->
  <line x1="-120" y1="0" x2="120" y2="0" stroke='#8b949e' stroke-width="2"/>
  <line x1="0" y1="-120" x2="0" y2="120" stroke='#8b949e' stroke-width="2"/>

  <!-- Arrow markers -->
  <polygon points="120,0 115,-5 115,5" fill='#8b949e'/>
  <polygon points="0,-120 -5,-115 5,-115" fill='#8b949e'/>

  <!-- Axis labels -->
  <text x="110" y="-10" fill='#e6edf3' font-size='14' font-weight='bold'>x</text>
  <text x="5" y="-110" fill='#e6edf3' font-size='14' font-weight='bold'>y</text>

  <!-- Origin label -->
  <text x="-15" y="15" fill='#e6edf3' font-size='12'>O</text>

  <!-- Scale marks and numbers -->
  <text x="18" y="12" fill='#e6edf3' font-size='10'>1</text>
  <text x="38" y="12" fill='#e6edf3' font-size='10'>2</text>
  <text x="58" y="12" fill='#e6edf3' font-size='10'>3</text>
  <text x="78" y="12" fill='#e6edf3' font-size='10'>4</text>
  <text x="-22" y="-18" fill='#e6edf3' font-size='10'>1</text>
  <text x="-22" y="-38" fill='#e6edf3' font-size='10'>2</text>
  <text x="-22" y="-58" fill='#e6edf3' font-size='10'>3</text>
  <text x="-22" y="-78" fill='#e6edf3' font-size='10'>4</text>
</svg>

<p><strong>Why "Cartesian"?</strong> Named after French philosopher René Descartes, who connected algebra and geometry by using coordinates to describe locations.</p></body></html>"""
    },
    {
        "title": "The Four Quadrants",
        "body": """<html><body><p>The two axes divide the plane into four regions called <strong>quadrants</strong>. Each quadrant has its own sign pattern for x and y coordinates.</p>

<div class="concept-box">
<p><strong>Quadrant signs:</strong></p>
<ul>
<li><strong>Quadrant I:</strong> x positive, y positive (upper right)</li>
<li><strong>Quadrant II:</strong> x negative, y positive (upper left)</li>
<li><strong>Quadrant III:</strong> x negative, y negative (lower left)</li>
<li><strong>Quadrant IV:</strong> x positive, y negative (lower right)</li>
</ul>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="100%" height="350">
  <!-- Quadrant backgrounds -->
  <rect x="0" y="-120" width="120" height="120" fill='#1f6feb' opacity='0.1'/>
  <rect x="-120" y="-120" width="120" height="120" fill='#3fb950' opacity='0.1'/>
  <rect x="-120" y="0" width="120" height="120" fill='#f85149' opacity='0.1'/>
  <rect x="0" y="0" width="120" height="120" fill='#a371f7' opacity='0.1'/>

  <!-- Grid -->
  <g stroke='#30363d' stroke-width="0.5">
    <line x1="-100" y1="0" x2="100" y2="0" />
    <line x1="0" y1="-100" x2="0" y2="100" />
    <line x1="-100" y1="-20" x2="100" y2="-20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-40" x2="100" y2="-40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-60" x2="100" y2="-60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-80" x2="100" y2="-80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="20" x2="100" y2="20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="40" x2="100" y2="40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="60" x2="100" y2="60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="80" x2="100" y2="80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-20" y1="-100" x2="-20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-40" y1="-100" x2="-40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-60" y1="-100" x2="-60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-80" y1="-100" x2="-80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="20" y1="-100" x2="20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="40" y1="-100" x2="40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="60" y1="-100" x2="60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="80" y1="-100" x2="80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
  </g>

  <!-- Axes -->
  <line x1="-120" y1="0" x2="120" y2="0" stroke='#8b949e' stroke-width="2"/>
  <line x1="0" y1="-120" x2="0" y2="120" stroke='#8b949e' stroke-width="2"/>

  <!-- Quadrant labels -->
  <text x="30" y="-35" fill='#e6edf3' font-size='12' font-weight='bold'>I (+,+)</text>
  <text x="-70" y="-35" fill='#e6edf3' font-size='12' font-weight='bold'>II (-,+)</text>
  <text x="-70" y="50" fill='#e6edf3' font-size='12' font-weight='bold'>III (-,-)</text>
  <text x="30" y="50" fill='#e6edf3' font-size='12' font-weight='bold'>IV (+,-)</text>
</svg>

<div class="worked-example">
<p><strong>Example: Identify the quadrant for each point</strong></p>
<ul>
<li>(3, 2) → x is positive, y is positive → <strong>Quadrant I</strong></li>
<li>(-2, 4) → x is negative, y is positive → <strong>Quadrant II</strong></li>
<li>(-1, -3) → x is negative, y is negative → <strong>Quadrant III</strong></li>
<li>(4, -1) → x is positive, y is negative → <strong>Quadrant IV</strong></li>
</ul>
</div></body></html>"""
    },
    {
        "title": "Reading Coordinates: Ordered Pairs (x, y)",
        "body": """<html><body><p>A point's location is described by an <strong>ordered pair (x, y)</strong>, where:</p>

<div class="concept-box">
<ul>
<li><strong>x-coordinate:</strong> How far left (negative) or right (positive) from the origin</li>
<li><strong>y-coordinate:</strong> How far down (negative) or up (positive) from the origin</li>
</ul>
<p><strong>Important:</strong> Order matters! (2, 3) is different from (3, 2).</p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="100%" height="350">
  <!-- Grid -->
  <g stroke='#30363d' stroke-width="0.5">
    <line x1="-100" y1="0" x2="100" y2="0" />
    <line x1="0" y1="-100" x2="0" y2="100" />
    <line x1="-100" y1="-20" x2="100" y2="-20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-40" x2="100" y2="-40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-60" x2="100" y2="-60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-80" x2="100" y2="-80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="20" x2="100" y2="20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="40" x2="100" y2="40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="60" x2="100" y2="60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="80" x2="100" y2="80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-20" y1="-100" x2="-20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-40" y1="-100" x2="-40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-60" y1="-100" x2="-60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-80" y1="-100" x2="-80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="20" y1="-100" x2="20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="40" y1="-100" x2="40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="60" y1="-100" x2="60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="80" y1="-100" x2="80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
  </g>

  <!-- Axes -->
  <line x1="-120" y1="0" x2="120" y2="0" stroke='#8b949e' stroke-width="2"/>
  <line x1="0" y1="-120" x2="0" y2="120" stroke='#8b949e' stroke-width="2"/>

  <!-- Point (2, 3) -->
  <circle cx="40" cy="-60" r="3" fill='#58a6ff'/>
  <line x1="40" y1="0" x2="40" y2="-60" stroke='#58a6ff' stroke-dasharray="3,3" opacity='0.5'/>
  <line x1="0" y1="-60" x2="40" y2="-60" stroke='#58a6ff' stroke-dasharray="3,3" opacity='0.5'/>
  <text x="50" y="-50" fill='#58a6ff' font-weight='bold'>(2, 3)</text>

  <!-- Point (-1, 2) -->
  <circle cx="-20" cy="-40" r="3" fill='#3fb950'/>
  <line x1="-20" y1="0" x2="-20" y2="-40" stroke='#3fb950' stroke-dasharray="3,3" opacity='0.5'/>
  <line x1="0" y1="-40" x2="-20" y2="-40" stroke='#3fb950' stroke-dasharray="3,3" opacity='0.5'/>
  <text x="-50" y="-25" fill='#3fb950' font-weight='bold'>(-1, 2)</text>

  <!-- Point (3, -2) -->
  <circle cx="60" cy="40" r="3" fill='#f85149'/>
  <line x1="60" y1="0" x2="60" y2="40" stroke='#f85149' stroke-dasharray="3,3" opacity='0.5'/>
  <line x1="0" y1="40" x2="60" y2="40" stroke='#f85149' stroke-dasharray="3,3" opacity='0.5'/>
  <text x="65" y="30" fill='#f85149' font-weight='bold'>(3, -2)</text>

  <!-- Origin -->
  <circle cx="0" cy="0" r="2" fill='#e6edf3'/>
  <text x="-15" y="15" fill='#e6edf3' font-size='12'>(0, 0)</text>
</svg>

<div class="worked-example">
<p><strong>Steps to read coordinates:</strong></p>
<ol>
<li>Start at the origin (0, 0)</li>
<li>Move <strong>right</strong> (positive) or <strong>left</strong> (negative) along the x-axis</li>
<li>From there, move <strong>up</strong> (positive) or <strong>down</strong> (negative) along the y-axis</li>
<li>Mark the point and write the ordered pair (x, y)</li>
</ol>
</div></body></html>"""
    },
    {
        "title": "Special Points on the Axes",
        "body": """<html><body><p>Some important points lie directly on one of the axes. These points have special properties.</p>

<div class="concept-box">
<p><strong>Points on the axes:</strong></p>
<ul>
<li><strong>On the x-axis:</strong> All y-coordinates are 0. Form: (x, 0)</li>
<li><strong>On the y-axis:</strong> All x-coordinates are 0. Form: (0, y)</li>
<li><strong>Origin:</strong> (0, 0) — the intersection point</li>
</ul>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="100%" height="350">
  <!-- Grid -->
  <g stroke='#30363d' stroke-width="0.5">
    <line x1="-100" y1="0" x2="100" y2="0" />
    <line x1="0" y1="-100" x2="0" y2="100" />
    <line x1="-100" y1="-20" x2="100" y2="-20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-40" x2="100" y2="-40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-60" x2="100" y2="-60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="-80" x2="100" y2="-80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="20" x2="100" y2="20" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="40" x2="100" y2="40" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="60" x2="100" y2="60" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-100" y1="80" x2="100" y2="80" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-20" y1="-100" x2="-20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-40" y1="-100" x2="-40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-60" y1="-100" x2="-60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="-80" y1="-100" x2="-80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="20" y1="-100" x2="20" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="40" y1="-100" x2="40" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="60" y1="-100" x2="60" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
    <line x1="80" y1="-100" x2="80" y2="100" stroke-dasharray="2,2" opacity='0.3'/>
  </g>

  <!-- Axes -->
  <line x1="-120" y1="0" x2="120" y2="0" stroke='#8b949e' stroke-width="2"/>
  <line x1="0" y1="-120" x2="0" y2="120" stroke='#8b949e' stroke-width="2"/>

  <!-- Points on x-axis -->
  <circle cx="60" cy="0" r="3" fill='#3fb950'/>
  <text x="50" y="-10" fill='#3fb950' font-weight='bold'>(3, 0)</text>

  <circle cx="-40" cy="0" r="3" fill='#3fb950'/>
  <text x="-65" y="-10" fill='#3fb950' font-weight='bold'>(-2, 0)</text>

  <!-- Points on y-axis -->
  <circle cx="0" cy="-60" r="3" fill='#58a6ff'/>
  <text x="10" y="-55" fill='#58a6ff' font-weight='bold'>(0, 3)</text>

  <circle cx="0" cy="40" r="3" fill='#58a6ff'/>
  <text x="10" y="35" fill='#58a6ff' font-weight='bold'>(0, -2)</text>

  <!-- Origin -->
  <circle cx="0" cy="0" r="3" fill='#f85149'/>
  <text x="8" y="18" fill='#f85149' font-weight='bold'>(0, 0)</text>
</svg>

<div class="success-box">
<p><strong>Quick check:</strong> If a coordinate is 0, the point is on an axis.</p>
<ul>
<li>(5, 0) — on the x-axis (no vertical movement)</li>
<li>(0, -3) — on the y-axis (no horizontal movement)</li>
<li>(0, 0) — at the origin (both axes meet)</li>
</ul>
</div></body></html>"""
    }
]
