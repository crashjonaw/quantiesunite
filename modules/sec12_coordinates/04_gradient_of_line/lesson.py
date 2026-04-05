TITLE = "Gradient (Slope) of a Line"

SECTIONS = [
    {
        "title": "What is Gradient?",
        "body": """<html><body><p>The <strong>gradient</strong> (also called <strong>slope</strong>) describes how steep a line is and the direction it goes.</p>

<div class="concept-box">
<p><strong>Gradient Formula:</strong></p>
<p style="text-align: center; font-size: 16px;">\\(m = \\frac{\\text{rise}}{\\text{run}} = \\frac{y_2 - y_1}{x_2 - x_1}\\)</p>
<p>where:</p>
<ul>
<li><strong>Rise:</strong> The vertical change (how much y changes)</li>
<li><strong>Run:</strong> The horizontal change (how much x changes)</li>
<li><strong>m:</strong> The gradient (the letter m is standard notation)</li>
</ul>
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

  <!-- Line with positive slope -->
  <line x1="0" y1="20" x2="100" y2="-80" stroke='#58a6ff' stroke-width="3"/>

  <!-- Two points on line -->
  <circle cx="20" cy="0" r="4" fill='#58a6ff'/>
  <circle cx="60" cy="-40" r="4" fill='#58a6ff'/>

  <!-- Rise indicator (vertical) -->
  <line x1="60" y1="0" x2="60" y2="-40" stroke='#3fb950' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="68" y="-20" fill='#3fb950' font-weight='bold' font-size='12'>rise = 2</text>

  <!-- Run indicator (horizontal) -->
  <line x1="20" y1="0" x2="60" y2="0" stroke='#f85149' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="38" y="15" fill='#f85149' font-weight='bold' font-size='12'>run = 2</text>

  <!-- Gradient label -->
  <text x="5" y="-95" fill='#a371f7' font-weight='bold' font-size='12'>m = rise/run = 2/2 = 1</text>
</svg></body></html>"""
    },
    {
        "title": "Types of Gradient",
        "body": """<html><body><p>Different lines have different gradients. Let's explore the main types.</p>

<div class="worked-example">
<p><strong>Positive Gradient (m > 0):</strong> The line slopes upward from left to right.</p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="300" height="250">
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
  <line x1="-100" y1="80" x2="100" y2="-80" stroke='#58a6ff' stroke-width="3"/>
  <text x="30" y="-90" fill='#58a6ff' font-weight='bold'>m = 2 (positive)</text>
</svg>

<div class="worked-example">
<p><strong>Negative Gradient (m < 0):</strong> The line slopes downward from left to right.</p>
</div>

<svg viewBox="-150 -170 300 320" class="worked-example" width="300" height="250">
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
  <line x1="-100" y1="-80" x2="100" y2="80" stroke='#f85149' stroke-width="3"/>
  <text x="30" y="-90" fill='#f85149' font-weight='bold'>m = -1 (negative)</text>
</svg>

<div class="worked-example">
<p><strong>Zero Gradient (m = 0):</strong> The line is horizontal. No vertical change.</p>
</div>

<svg viewBox="-150 -170 300 320" class="worked-example" width="300" height="250">
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
  <line x1="-100" y1="-40" x2="100" y2="-40" stroke='#3fb950' stroke-width="3"/>
  <text x="30" y="-55" fill='#3fb950' font-weight='bold'>m = 0 (horizontal)</text>
</svg>

<div class="worked-example">
<p><strong>Undefined Gradient:</strong> The line is vertical. Infinite steepness (division by zero).</p>
</div>

<svg viewBox="-150 -170 300 320" class="worked-example" width="300" height="250">
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
  <line x1="40" y1="-100" x2="40" y2="100" stroke='#a371f7' stroke-width="3"/>
  <text x="50" y="-90" fill='#a371f7' font-weight='bold'>m = undefined</text>
  <text x="50" y="-70" fill='#a371f7' font-weight='bold'>(vertical)</text>
</svg></body></html>"""
    },
    {
        "title": "Calculating Gradient from Two Points",
        "body": """<html><body><p>To find the gradient of a line through two known points, use the formula.</p>

<div class="worked-example">
<p><strong>Example 1: Find the gradient of the line through (1, 2) and (3, 6)</strong></p>
<ol>
<li>Identify the points: \\((x_1, y_1) = (1, 2)\\) and \\((x_2, y_2) = (3, 6)\\)</li>
<li>Apply the formula: \\(m = \\frac{6 - 2}{3 - 1} = \\frac{4}{2} = 2\\)</li>
<li>Answer: The gradient is <strong>2</strong></li>
<li>Interpretation: For every 1 unit right, go 2 units up</li>
</ol>
</div>

<div class="worked-example">
<p><strong>Example 2: Find the gradient of the line through (1, 5) and (4, 2)</strong></p>
<ol>
<li>Identify the points: \\((x_1, y_1) = (1, 5)\\) and \\((x_2, y_2) = (4, 2)\\)</li>
<li>Apply the formula: \\(m = \\frac{2 - 5}{4 - 1} = \\frac{-3}{3} = -1\\)</li>
<li>Answer: The gradient is <strong>-1</strong></li>
<li>Interpretation: For every 1 unit right, go 1 unit down</li>
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

  <!-- Line through (1,2) and (3,6) -->
  <line x1="20" y1="-40" x2="60" y2="-120" stroke='#58a6ff' stroke-width="3"/>

  <!-- Points -->
  <circle cx="20" cy="-40" r="4" fill='#58a6ff'/>
  <circle cx="60" cy="-120" r="4" fill='#58a6ff'/>

  <!-- Rise and run -->
  <line x1="20" y1="-40" x2="60" y2="-40" stroke='#f85149' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="38" y="-48" fill='#f85149' font-weight='bold'>run = 2</text>

  <line x1="60" y1="-40" x2="60" y2="-120" stroke='#3fb950' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="68" y="-80" fill='#3fb950' font-weight='bold'>rise = 4</text>

  <text x="5" y="-135" fill='#a371f7' font-weight='bold'>m = 4/2 = 2</text>
</svg></body></html>"""
    },
    {
        "title": "Parallel and Perpendicular Lines",
        "body": """<html><body><p>The gradient tells us whether lines are parallel or perpendicular.</p>

<div class="concept-box">
<p><strong>Parallel Lines:</strong> Same gradient (\\(m_1 = m_2\\))</p>
<p>Parallel lines never meet and have the same steepness.</p>
</div>

<div class="worked-example">
<p><strong>Example:</strong> Line A passes through (0, 1) and (2, 5): \\(m_A = \\frac{5-1}{2-0} = 2\\)</p>
<p>Line B passes through (1, 0) and (2, 2): \\(m_B = \\frac{2-0}{2-1} = 2\\)</p>
<p>Since both have gradient 2, <strong>lines A and B are parallel</strong>.</p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="300">
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

  <!-- Parallel lines -->
  <line x1="-100" y1="80" x2="100" y2="-20" stroke='#58a6ff' stroke-width="3"/>
  <line x1="-100" y1="40" x2="100" y2="-60" stroke='#3fb950' stroke-width="3"/>
  <text x="60" y="-25" fill='#58a6ff' font-weight='bold'>m = 2</text>
  <text x="60" y="-65" fill='#3fb950' font-weight='bold'>m = 2</text>
  <text x="-90" y="110" fill='#a371f7' font-weight='bold' font-size='12'>Parallel (never meet)</text>
</svg>

<div class="concept-box">
<p><strong>Perpendicular Lines:</strong> Gradients are negative reciprocals (\\(m_1 \\times m_2 = -1\\))</p>
<p>Perpendicular lines meet at 90° angles.</p>
</div>

<div class="worked-example">
<p><strong>Example:</strong> Line A has gradient \\(m_A = 2\\)</p>
<p>Line B is perpendicular to A, so: \\(m_B = -\\frac{1}{2}\\)</p>
<p>Check: \\(2 \\times (-\\frac{1}{2}) = -1\\) ✓</p>
</div>

<svg viewBox="-150 -150 300 300" class="worked-example" width="350" height="300">
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

  <!-- Perpendicular lines -->
  <line x1="-100" y1="100" x2="100" y2="-100" stroke='#58a6ff' stroke-width="3"/>
  <line x1="-100" y1="-50" x2="100" y2="100" stroke='#f85149' stroke-width="3"/>
  <text x="50" y="-90" fill='#58a6ff' font-weight='bold'>m = 2</text>
  <text x="50" y="90" fill='#f85149' font-weight='bold'>m = -1/2</text>
  <text x="-90" y="110" fill='#a371f7' font-weight='bold' font-size='12'>Perpendicular (meet at 90°)</text>
</svg></body></html>"""
    }
]
