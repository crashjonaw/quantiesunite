TITLE = "Plotting Points on the Plane"

SECTIONS = [
    {
        "title": "Steps to Plot a Point",
        "body": """<html><body><p>Plotting a point means marking its exact location on the Cartesian plane using its coordinates (x, y).</p>

<div class="concept-box">
<p><strong>Three-step process to plot point (x, y):</strong></p>
<ol>
<li><strong>Start at origin (0, 0)</strong></li>
<li><strong>Move horizontally:</strong> Go right if x is positive, left if x is negative</li>
<li><strong>Move vertically:</strong> Go up if y is positive, down if y is negative</li>
<li><strong>Mark the point</strong> with a dot</li>
</ol>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="350">
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

  <!-- Plotting (2, 3) -->
  <circle cx="0" cy="0" r="3" fill='#e6edf3' opacity='0.7'/>
  <text x="-20" y="20" fill='#e6edf3' font-size='10'>Start (0,0)</text>

  <!-- Arrow showing horizontal movement -->
  <path d="M 5,-5 L 35,-5" stroke='#58a6ff' stroke-width="2" fill='none' marker-end="url(#arrowhead)"/>
  <text x="15" y="-10" fill='#58a6ff' font-size='10'>2 right</text>

  <!-- Intermediate point -->
  <circle cx="40" cy="0" r="2" fill='#58a6ff' opacity='0.5'/>

  <!-- Arrow showing vertical movement -->
  <path d="M 42,-5 L 42,-60" stroke='#3fb950' stroke-width="2" fill='none' marker-end="url(#arrowhead2)"/>
  <text x="50" y="-35" fill='#3fb950' font-size='10'>3 up</text>

  <!-- Final point -->
  <circle cx="40" cy="-60" r="5" fill='#f85149'/>
  <text x="50" y="-50" fill='#f85149' font-weight='bold' font-size='12'>(2, 3)</text>

  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#58a6ff' />
    </marker>
    <marker id="arrowhead2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#3fb950' />
    </marker>
  </defs>
</svg></body></html>"""
    },
    {
        "title": "Plotting Multiple Points",
        "body": """<html><body><p>When you plot several points, you can see patterns and connections between them.</p>

<div class="worked-example">
<p><strong>Example: Plot the points A(1, 2), B(3, 4), C(-2, 1), and D(2, -3)</strong></p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="350">
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

  <!-- Point A(1, 2) -->
  <circle cx="20" cy="-40" r="4" fill='#58a6ff'/>
  <text x="25" y="-32" fill='#58a6ff' font-weight='bold'>A(1, 2)</text>

  <!-- Point B(3, 4) -->
  <circle cx="60" cy="-80" r="4" fill='#3fb950'/>
  <text x="65" y="-72" fill='#3fb950' font-weight='bold'>B(3, 4)</text>

  <!-- Point C(-2, 1) -->
  <circle cx="-40" cy="-20" r="4" fill='#f85149'/>
  <text x="-60" y="-10" fill='#f85149' font-weight='bold'>C(-2, 1)</text>

  <!-- Point D(2, -3) -->
  <circle cx="40" cy="60" r="4" fill='#a371f7'/>
  <text x="45" y="72" fill='#a371f7' font-weight='bold'>D(2, -3)</text>

  <!-- Origin -->
  <circle cx="0" cy="0" r="2" fill='#e6edf3'/>
</svg>

<div class="success-box">
<p><strong>Key observations:</strong></p>
<ul>
<li>Point A (1, 2) is in Quadrant I — 1 right, 2 up</li>
<li>Point B (3, 4) is in Quadrant I — 3 right, 4 up</li>
<li>Point C (-2, 1) is in Quadrant II — 2 left, 1 up</li>
<li>Point D (2, -3) is in Quadrant IV — 2 right, 3 down</li>
</ul>
</div></body></html>"""
    },
    {
        "title": "Common Mistakes When Plotting",
        "body": """<html><body><p>Watch out for these common errors when plotting points.</p>

<div class="warning-box">
<p><strong>Mistake 1: Confusing the order (x, y)</strong></p>
<p>The point (2, 3) is NOT the same as (3, 2)!</p>
<ul>
<li>(2, 3) means: 2 right, 3 up</li>
<li>(3, 2) means: 3 right, 2 up</li>
</ul>
</div>

<div class="warning-box">
<p><strong>Mistake 2: Forgetting negative signs</strong></p>
<p>The point (-2, -3) is different from (2, 3).</p>
<ul>
<li>(-2, -3) is in Quadrant III (lower-left)</li>
<li>(2, 3) is in Quadrant I (upper-right)</li>
</ul>
</div>

<div class="warning-box">
<p><strong>Mistake 3: Not starting at the origin</strong></p>
<p>Always start your count from (0, 0), not from where the previous point was.</p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="350">
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

  <!-- Correct point (2, 3) -->
  <circle cx="40" cy="-60" r="5" fill='#3fb950'/>
  <text x="48" y="-48" fill='#3fb950' font-weight='bold'>(2, 3) ✓</text>

  <!-- Wrong point (3, 2) shown as comparison -->
  <circle cx="60" cy="-40" r="5" fill='#f85149'/>
  <text x="68" y="-28" fill='#f85149' font-weight='bold'>(3, 2)</text>

  <!-- Line showing they are different -->
  <line x1="40" y1="-60" x2="60" y2="-40" stroke='#a371f7' stroke-width="1" stroke-dasharray="3,3" opacity='0.5'/>
</svg></body></html>"""
    },
    {
        "title": "Reading Coordinates from a Graph",
        "body": """<html><body><p>You can also work backwards: given a point on a graph, determine its coordinates.</p>

<div class="worked-example">
<p><strong>To read a point's coordinates from a graph:</strong></p>
<ol>
<li>Look horizontally (trace downward) to find the x-coordinate</li>
<li>Look vertically (trace across) to find the y-coordinate</li>
<li>Write the ordered pair (x, y)</li>
</ol>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="350">
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

  <!-- Point to read -->
  <circle cx="-40" cy="40" r="5" fill='#58a6ff'/>

  <!-- Horizontal trace line -->
  <line x1="-40" y1="40" x2="-40" y2="2" stroke='#58a6ff' stroke-dasharray="3,3" opacity='0.6'/>
  <text x="-50" y="8" fill='#58a6ff' font-size='10'>x = -2</text>

  <!-- Vertical trace line -->
  <line x1="-40" y1="40" x2="2" y2="40" stroke='#3fb950' stroke-dasharray="3,3" opacity='0.6'/>
  <text x="8" y="45" fill='#3fb950' font-size='10'>y = 2</text>

  <!-- Result -->
  <text x="-65" y="-70" fill='#f85149' font-weight='bold' font-size='12'>Read: (-2, 2)</text>
</svg></body></html>"""
    }
]
