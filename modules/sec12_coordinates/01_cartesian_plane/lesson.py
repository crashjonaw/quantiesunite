TITLE = "The Cartesian Plane and Axes"

SECTIONS = [
    {
        "title": "Introduction: What is the Cartesian Plane?",
        "body": """<p><strong>A map uses two numbers -- latitude and longitude -- to pinpoint any location on Earth. Mathematics does the same thing: TWO numbers (x, y) can locate any point on a flat surface. This is the Cartesian coordinate system, invented by Rene Descartes.</strong></p>

<div class="concept-box">
<p>The <strong>Cartesian plane</strong> is a 2D grid formed by two perpendicular number lines:</p>
<ul>
<li><strong>Horizontal axis (x-axis):</strong> Runs left to right</li>
<li><strong>Vertical axis (y-axis):</strong> Runs up and down</li>
<li><strong>Origin:</strong> The point (0, 0) where the axes meet</li>
</ul>
</div>

<svg viewBox="-135 -135 270 270" class="worked-example" width="300" height="300">
  <rect x="-135" y="-135" width="270" height="270" fill='#161b22' rx='4'/>

  <!-- Grid lines -->
  <g stroke='#30363d' stroke-width='0.5' stroke-dasharray='2,2' opacity='0.4'>
    <line x1="-100" y1="-80" x2="100" y2="-80"/>
    <line x1="-100" y1="-60" x2="100" y2="-60"/>
    <line x1="-100" y1="-40" x2="100" y2="-40"/>
    <line x1="-100" y1="-20" x2="100" y2="-20"/>
    <line x1="-100" y1="20" x2="100" y2="20"/>
    <line x1="-100" y1="40" x2="100" y2="40"/>
    <line x1="-100" y1="60" x2="100" y2="60"/>
    <line x1="-100" y1="80" x2="100" y2="80"/>
    <line x1="-80" y1="-100" x2="-80" y2="100"/>
    <line x1="-60" y1="-100" x2="-60" y2="100"/>
    <line x1="-40" y1="-100" x2="-40" y2="100"/>
    <line x1="-20" y1="-100" x2="-20" y2="100"/>
    <line x1="20" y1="-100" x2="20" y2="100"/>
    <line x1="40" y1="-100" x2="40" y2="100"/>
    <line x1="60" y1="-100" x2="60" y2="100"/>
    <line x1="80" y1="-100" x2="80" y2="100"/>
  </g>

  <!-- Axes -->
  <line x1="-110" y1="0" x2="110" y2="0" stroke='#8b949e' stroke-width='2'/>
  <line x1="0" y1="-110" x2="0" y2="110" stroke='#8b949e' stroke-width='2'/>

  <!-- Arrow tips -->
  <polygon points="110,0 104,-4 104,4" fill='#8b949e'/>
  <polygon points="0,-110 -4,-104 4,-104" fill='#8b949e'/>

  <!-- Tick marks on x-axis -->
  <g stroke='#8b949e' stroke-width='1'>
    <line x1="-80" y1="-3" x2="-80" y2="3"/>
    <line x1="-60" y1="-3" x2="-60" y2="3"/>
    <line x1="-40" y1="-3" x2="-40" y2="3"/>
    <line x1="-20" y1="-3" x2="-20" y2="3"/>
    <line x1="20" y1="-3" x2="20" y2="3"/>
    <line x1="40" y1="-3" x2="40" y2="3"/>
    <line x1="60" y1="-3" x2="60" y2="3"/>
    <line x1="80" y1="-3" x2="80" y2="3"/>
  </g>

  <!-- Tick marks on y-axis -->
  <g stroke='#8b949e' stroke-width='1'>
    <line x1="-3" y1="-80" x2="3" y2="-80"/>
    <line x1="-3" y1="-60" x2="3" y2="-60"/>
    <line x1="-3" y1="-40" x2="3" y2="-40"/>
    <line x1="-3" y1="-20" x2="3" y2="-20"/>
    <line x1="-3" y1="20" x2="3" y2="20"/>
    <line x1="-3" y1="40" x2="3" y2="40"/>
    <line x1="-3" y1="60" x2="3" y2="60"/>
    <line x1="-3" y1="80" x2="3" y2="80"/>
  </g>

  <!-- X-axis numbers -->
  <text x="-82" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-4</text>
  <text x="-62" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-3</text>
  <text x="-42" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>
  <text x="-22" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="20" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="40" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="60" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="80" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>4</text>

  <!-- Y-axis numbers -->
  <text x="-10" y="-77" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>4</text>
  <text x="-10" y="-57" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="-10" y="-37" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="-10" y="-17" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="-12" y="23" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="-12" y="43" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>
  <text x="-12" y="63" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-3</text>
  <text x="-12" y="83" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-4</text>

  <!-- Axis labels -->
  <text x="118" y="-6" fill='currentColor' font-family='Arial, sans-serif' font-size='13' font-weight='bold'>x</text>
  <text x="8" y="-114" fill='currentColor' font-family='Arial, sans-serif' font-size='13' font-weight='bold'>y</text>

  <!-- Origin label -->
  <text x="-12" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='10'>O</text>
</svg>

<p><strong>Why "Cartesian"?</strong> Named after French philosopher Rene Descartes, who connected algebra and geometry by using coordinates to describe locations.</p>"""
    },
    {
        "title": "The Four Quadrants",
        "body": """<p>The two axes divide the plane into four regions called <strong>quadrants</strong>. Each quadrant has its own sign pattern for x and y coordinates.</p>

<div class="concept-box">
<p><strong>Quadrant signs:</strong></p>
<ul>
<li><strong>Quadrant I:</strong> x positive, y positive (upper right)</li>
<li><strong>Quadrant II:</strong> x negative, y positive (upper left)</li>
<li><strong>Quadrant III:</strong> x negative, y negative (lower left)</li>
<li><strong>Quadrant IV:</strong> x positive, y negative (lower right)</li>
</ul>
</div>

<svg viewBox="-135 -135 270 270" class="worked-example" width="300" height="300">
  <rect x="-135" y="-135" width="270" height="270" fill='#161b22' rx='4'/>

  <!-- Quadrant backgrounds -->
  <rect x="2" y="-108" width="106" height="106" fill='#1f6feb' opacity='0.12' rx='4'/>
  <rect x="-108" y="-108" width="106" height="106" fill='#3fb950' opacity='0.12' rx='4'/>
  <rect x="-108" y="2" width="106" height="106" fill='#f85149' opacity='0.12' rx='4'/>
  <rect x="2" y="2" width="106" height="106" fill='#a371f7' opacity='0.12' rx='4'/>

  <!-- Grid lines -->
  <g stroke='#30363d' stroke-width='0.5' stroke-dasharray='2,2' opacity='0.3'>
    <line x1="-100" y1="-80" x2="100" y2="-80"/>
    <line x1="-100" y1="-60" x2="100" y2="-60"/>
    <line x1="-100" y1="-40" x2="100" y2="-40"/>
    <line x1="-100" y1="-20" x2="100" y2="-20"/>
    <line x1="-100" y1="20" x2="100" y2="20"/>
    <line x1="-100" y1="40" x2="100" y2="40"/>
    <line x1="-100" y1="60" x2="100" y2="60"/>
    <line x1="-100" y1="80" x2="100" y2="80"/>
    <line x1="-80" y1="-100" x2="-80" y2="100"/>
    <line x1="-60" y1="-100" x2="-60" y2="100"/>
    <line x1="-40" y1="-100" x2="-40" y2="100"/>
    <line x1="-20" y1="-100" x2="-20" y2="100"/>
    <line x1="20" y1="-100" x2="20" y2="100"/>
    <line x1="40" y1="-100" x2="40" y2="100"/>
    <line x1="60" y1="-100" x2="60" y2="100"/>
    <line x1="80" y1="-100" x2="80" y2="100"/>
  </g>

  <!-- Axes -->
  <line x1="-110" y1="0" x2="110" y2="0" stroke='#8b949e' stroke-width='2'/>
  <line x1="0" y1="-110" x2="0" y2="110" stroke='#8b949e' stroke-width='2'/>

  <!-- Quadrant labels -->
  <text x="54" y="-45" fill='currentColor' font-family='Arial, sans-serif' font-size='12' font-weight='bold' text-anchor='middle'>I</text>
  <text x="54" y="-30" fill='currentColor' font-family='Arial, sans-serif' font-size='10' text-anchor='middle'>(+, +)</text>

  <text x="-54" y="-45" fill='currentColor' font-family='Arial, sans-serif' font-size='12' font-weight='bold' text-anchor='middle'>II</text>
  <text x="-54" y="-30" fill='currentColor' font-family='Arial, sans-serif' font-size='10' text-anchor='middle'>(-, +)</text>

  <text x="-54" y="45" fill='currentColor' font-family='Arial, sans-serif' font-size='12' font-weight='bold' text-anchor='middle'>III</text>
  <text x="-54" y="60" fill='currentColor' font-family='Arial, sans-serif' font-size='10' text-anchor='middle'>(-, -)</text>

  <text x="54" y="45" fill='currentColor' font-family='Arial, sans-serif' font-size='12' font-weight='bold' text-anchor='middle'>IV</text>
  <text x="54" y="60" fill='currentColor' font-family='Arial, sans-serif' font-size='10' text-anchor='middle'>(+, -)</text>
</svg>

<div class="worked-example">
<p><strong>Example: Identify the quadrant for each point</strong></p>
<ul>
<li>(3, 2) -- x is positive, y is positive -- <strong>Quadrant I</strong></li>
<li>(-2, 4) -- x is negative, y is positive -- <strong>Quadrant II</strong></li>
<li>(-1, -3) -- x is negative, y is negative -- <strong>Quadrant III</strong></li>
<li>(4, -1) -- x is positive, y is negative -- <strong>Quadrant IV</strong></li>
</ul>
</div>"""
    },
    {
        "title": "Reading Coordinates: Ordered Pairs (x, y)",
        "body": """<p>A point's location is described by an <strong>ordered pair (x, y)</strong>, where:</p>

<div class="concept-box">
<ul>
<li><strong>x-coordinate:</strong> How far left (negative) or right (positive) from the origin</li>
<li><strong>y-coordinate:</strong> How far down (negative) or up (positive) from the origin</li>
</ul>
<p><strong>Important:</strong> Order matters! (2, 3) is different from (3, 2).</p>
</div>

<svg viewBox="-135 -135 270 270" class="worked-example" width="300" height="300">
  <rect x="-135" y="-135" width="270" height="270" fill='#161b22' rx='4'/>

  <!-- Grid lines -->
  <g stroke='#30363d' stroke-width='0.5' stroke-dasharray='2,2' opacity='0.4'>
    <line x1="-100" y1="-80" x2="100" y2="-80"/>
    <line x1="-100" y1="-60" x2="100" y2="-60"/>
    <line x1="-100" y1="-40" x2="100" y2="-40"/>
    <line x1="-100" y1="-20" x2="100" y2="-20"/>
    <line x1="-100" y1="20" x2="100" y2="20"/>
    <line x1="-100" y1="40" x2="100" y2="40"/>
    <line x1="-100" y1="60" x2="100" y2="60"/>
    <line x1="-100" y1="80" x2="100" y2="80"/>
    <line x1="-80" y1="-100" x2="-80" y2="100"/>
    <line x1="-60" y1="-100" x2="-60" y2="100"/>
    <line x1="-40" y1="-100" x2="-40" y2="100"/>
    <line x1="-20" y1="-100" x2="-20" y2="100"/>
    <line x1="20" y1="-100" x2="20" y2="100"/>
    <line x1="40" y1="-100" x2="40" y2="100"/>
    <line x1="60" y1="-100" x2="60" y2="100"/>
    <line x1="80" y1="-100" x2="80" y2="100"/>
  </g>

  <!-- Axes -->
  <line x1="-110" y1="0" x2="110" y2="0" stroke='#8b949e' stroke-width='2'/>
  <line x1="0" y1="-110" x2="0" y2="110" stroke='#8b949e' stroke-width='2'/>

  <!-- Tick marks -->
  <g stroke='#8b949e' stroke-width='1'>
    <line x1="20" y1="-3" x2="20" y2="3"/>
    <line x1="40" y1="-3" x2="40" y2="3"/>
    <line x1="60" y1="-3" x2="60" y2="3"/>
    <line x1="80" y1="-3" x2="80" y2="3"/>
    <line x1="-20" y1="-3" x2="-20" y2="3"/>
    <line x1="-40" y1="-3" x2="-40" y2="3"/>
    <line x1="-60" y1="-3" x2="-60" y2="3"/>
    <line x1="-3" y1="-20" x2="3" y2="-20"/>
    <line x1="-3" y1="-40" x2="3" y2="-40"/>
    <line x1="-3" y1="-60" x2="3" y2="-60"/>
    <line x1="-3" y1="20" x2="3" y2="20"/>
    <line x1="-3" y1="40" x2="3" y2="40"/>
    <line x1="-3" y1="60" x2="3" y2="60"/>
  </g>

  <!-- Axis numbers -->
  <text x="20" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="40" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="60" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="-20" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="-40" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>
  <text x="-60" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-3</text>
  <text x="-10" y="-17" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="-10" y="-37" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="-10" y="-57" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="-12" y="23" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="-12" y="43" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>
  <text x="-12" y="63" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-3</text>

  <!-- Axis labels -->
  <text x="118" y="-6" fill='currentColor' font-family='Arial, sans-serif' font-size='13' font-weight='bold'>x</text>
  <text x="8" y="-114" fill='currentColor' font-family='Arial, sans-serif' font-size='13' font-weight='bold'>y</text>

  <!-- Point (2, 3): 2 right, 3 up -->
  <line x1="40" y1="0" x2="40" y2="-60" stroke='#58a6ff' stroke-dasharray='3,3' opacity='0.5'/>
  <line x1="0" y1="-60" x2="40" y2="-60" stroke='#58a6ff' stroke-dasharray='3,3' opacity='0.5'/>
  <circle cx="40" cy="-60" r="4" fill='#58a6ff'/>
  <text x="48" y="-64" fill='#58a6ff' font-family='Arial, sans-serif' font-size='11' font-weight='bold'>(2, 3)</text>

  <!-- Point (-1, 2): 1 left, 2 up -->
  <line x1="-20" y1="0" x2="-20" y2="-40" stroke='#3fb950' stroke-dasharray='3,3' opacity='0.5'/>
  <line x1="0" y1="-40" x2="-20" y2="-40" stroke='#3fb950' stroke-dasharray='3,3' opacity='0.5'/>
  <circle cx="-20" cy="-40" r="4" fill='#3fb950'/>
  <text x="-70" y="-44" fill='#3fb950' font-family='Arial, sans-serif' font-size='11' font-weight='bold'>(-1, 2)</text>

  <!-- Point (3, -2): 3 right, 2 down -->
  <line x1="60" y1="0" x2="60" y2="40" stroke='#f85149' stroke-dasharray='3,3' opacity='0.5'/>
  <line x1="0" y1="40" x2="60" y2="40" stroke='#f85149' stroke-dasharray='3,3' opacity='0.5'/>
  <circle cx="60" cy="40" r="4" fill='#f85149'/>
  <text x="68" y="36" fill='#f85149' font-family='Arial, sans-serif' font-size='11' font-weight='bold'>(3, -2)</text>

  <!-- Origin -->
  <circle cx="0" cy="0" r="3" fill='currentColor'/>
  <text x="-12" y="-6" fill='currentColor' font-family='Arial, sans-serif' font-size='10'>O</text>
</svg>

<div class="worked-example">
<p><strong>Steps to read coordinates:</strong></p>
<ol>
<li>Start at the origin (0, 0)</li>
<li>Move <strong>right</strong> (positive) or <strong>left</strong> (negative) along the x-axis</li>
<li>From there, move <strong>up</strong> (positive) or <strong>down</strong> (negative) along the y-axis</li>
<li>Mark the point and write the ordered pair (x, y)</li>
</ol>
</div>"""
    },
    {
        "title": "Special Points on the Axes",
        "body": """<p>Some important points lie directly on one of the axes. These points have special properties.</p>

<div class="concept-box">
<p><strong>Points on the axes:</strong></p>
<ul>
<li><strong>On the x-axis:</strong> All y-coordinates are 0. Form: (x, 0)</li>
<li><strong>On the y-axis:</strong> All x-coordinates are 0. Form: (0, y)</li>
<li><strong>Origin:</strong> (0, 0) -- the intersection point</li>
</ul>
</div>

<svg viewBox="-135 -135 270 270" class="worked-example" width="300" height="300">
  <rect x="-135" y="-135" width="270" height="270" fill='#161b22' rx='4'/>

  <!-- Grid lines -->
  <g stroke='#30363d' stroke-width='0.5' stroke-dasharray='2,2' opacity='0.4'>
    <line x1="-100" y1="-80" x2="100" y2="-80"/>
    <line x1="-100" y1="-60" x2="100" y2="-60"/>
    <line x1="-100" y1="-40" x2="100" y2="-40"/>
    <line x1="-100" y1="-20" x2="100" y2="-20"/>
    <line x1="-100" y1="20" x2="100" y2="20"/>
    <line x1="-100" y1="40" x2="100" y2="40"/>
    <line x1="-100" y1="60" x2="100" y2="60"/>
    <line x1="-100" y1="80" x2="100" y2="80"/>
    <line x1="-80" y1="-100" x2="-80" y2="100"/>
    <line x1="-60" y1="-100" x2="-60" y2="100"/>
    <line x1="-40" y1="-100" x2="-40" y2="100"/>
    <line x1="-20" y1="-100" x2="-20" y2="100"/>
    <line x1="20" y1="-100" x2="20" y2="100"/>
    <line x1="40" y1="-100" x2="40" y2="100"/>
    <line x1="60" y1="-100" x2="60" y2="100"/>
    <line x1="80" y1="-100" x2="80" y2="100"/>
  </g>

  <!-- Axes -->
  <line x1="-110" y1="0" x2="110" y2="0" stroke='#8b949e' stroke-width='2'/>
  <line x1="0" y1="-110" x2="0" y2="110" stroke='#8b949e' stroke-width='2'/>

  <!-- Tick marks -->
  <g stroke='#8b949e' stroke-width='1'>
    <line x1="20" y1="-3" x2="20" y2="3"/>
    <line x1="40" y1="-3" x2="40" y2="3"/>
    <line x1="60" y1="-3" x2="60" y2="3"/>
    <line x1="-20" y1="-3" x2="-20" y2="3"/>
    <line x1="-40" y1="-3" x2="-40" y2="3"/>
    <line x1="-60" y1="-3" x2="-60" y2="3"/>
    <line x1="-3" y1="-20" x2="3" y2="-20"/>
    <line x1="-3" y1="-40" x2="3" y2="-40"/>
    <line x1="-3" y1="-60" x2="3" y2="-60"/>
    <line x1="-3" y1="20" x2="3" y2="20"/>
    <line x1="-3" y1="40" x2="3" y2="40"/>
  </g>

  <!-- Axis numbers -->
  <text x="20" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="40" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="60" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="-20" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="-40" y="14" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>
  <text x="-10" y="-17" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>1</text>
  <text x="-10" y="-37" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>2</text>
  <text x="-10" y="-57" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>3</text>
  <text x="-12" y="23" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-1</text>
  <text x="-12" y="43" fill='currentColor' font-family='Arial, sans-serif' font-size='9' text-anchor='middle'>-2</text>

  <!-- Points on x-axis (green) -->
  <circle cx="60" cy="0" r="4" fill='#3fb950'/>
  <text x="60" y="-10" fill='#3fb950' font-family='Arial, sans-serif' font-size='10' font-weight='bold' text-anchor='middle'>(3, 0)</text>

  <circle cx="-40" cy="0" r="4" fill='#3fb950'/>
  <text x="-40" y="-10" fill='#3fb950' font-family='Arial, sans-serif' font-size='10' font-weight='bold' text-anchor='middle'>(-2, 0)</text>

  <!-- Points on y-axis (blue) -->
  <circle cx="0" cy="-60" r="4" fill='#58a6ff'/>
  <text x="14" y="-64" fill='#58a6ff' font-family='Arial, sans-serif' font-size='10' font-weight='bold'>(0, 3)</text>

  <circle cx="0" cy="40" r="4" fill='#58a6ff'/>
  <text x="14" y="36" fill='#58a6ff' font-family='Arial, sans-serif' font-size='10' font-weight='bold'>(0, -2)</text>

  <!-- Origin (red) -->
  <circle cx="0" cy="0" r="4" fill='#f85149'/>
  <text x="10" y="20" fill='#f85149' font-family='Arial, sans-serif' font-size='10' font-weight='bold'>(0, 0)</text>
</svg>

<div class="success-box">
<p><strong>Quick check:</strong> If a coordinate is 0, the point is on an axis.</p>
<ul>
<li>(5, 0) -- on the x-axis (no vertical movement)</li>
<li>(0, -3) -- on the y-axis (no horizontal movement)</li>
<li>(0, 0) -- at the origin (both axes meet)</li>
</ul>
</div>"""
    }
]
