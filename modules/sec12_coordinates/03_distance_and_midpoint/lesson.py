TITLE = "Distance Formula and Midpoint"

SECTIONS = [
    {
        "title": "Distance Between Two Points: The Distance Formula",
        "body": """<html><body><p>To find the straight-line distance between any two points on the plane, we use a formula based on Pythagoras' Theorem.</p>

<div class="concept-box">
<p><strong>Distance Formula:</strong></p>
<p style="text-align: center; font-size: 16px;">\\(d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\\)</p>
<p>where:</p>
<ul>
<li>\\((x_1, y_1)\\) and \\((x_2, y_2)\\) are the two points</li>
<li>\\(d\\) is the distance between them</li>
</ul>
</div>

<p><strong>Why does this work?</strong> The distance between two points forms the hypotenuse of a right triangle!</p>

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

  <!-- Point 1 -->
  <circle cx="20" cy="-40" r="4" fill='#58a6ff'/>
  <text x="25" y="-30" fill='#58a6ff' font-weight='bold'>(1, 2)</text>

  <!-- Point 2 -->
  <circle cx="80" cy="40" r="4" fill='#3fb950'/>
  <text x="85" y="50" fill='#3fb950' font-weight='bold'>(4, -2)</text>

  <!-- Hypotenuse (distance) -->
  <line x1="20" y1="-40" x2="80" y2="40" stroke='#f85149' stroke-width="3"/>
  <text x="50" y="5" fill='#f85149' font-weight='bold'>d = 5√2</text>

  <!-- Right triangle - horizontal leg -->
  <line x1="20" y1="-40" x2="80" y2="-40" stroke='#a371f7' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="50" y="-45" fill='#a371f7' font-size='11'>3 units</text>

  <!-- Right triangle - vertical leg -->
  <line x1="80" y1="-40" x2="80" y2="40" stroke='#a371f7' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="90" y="5" fill='#a371f7' font-size='11'>4 units</text>

  <!-- Right angle marker -->
  <rect x="75" y="-45" width="5" height="5" fill='none' stroke='#a371f7'/>
</svg></body></html>"""
    },
    {
        "title": "Using the Distance Formula: Step by Step",
        "body": """<html><body><p>Let's calculate the distance between two points using the formula.</p>

<div class="worked-example">
<p><strong>Example 1: Find the distance between (1, 2) and (4, 6)</strong></p>
<ol>
<li>Identify the coordinates: \\((x_1, y_1) = (1, 2)\\) and \\((x_2, y_2) = (4, 6)\\)</li>
<li>Substitute into the formula: \\(d = \\sqrt{(4-1)^2 + (6-2)^2}\\)</li>
<li>Simplify: \\(d = \\sqrt{3^2 + 4^2}\\)</li>
<li>Calculate: \\(d = \\sqrt{9 + 16} = \\sqrt{25} = 5\\)</li>
<li>Answer: The distance is <strong>5 units</strong></li>
</ol>
</div>

<div class="worked-example">
<p><strong>Example 2: Find the distance between (-1, 2) and (2, 6)</strong></p>
<ol>
<li>Identify the coordinates: \\((x_1, y_1) = (-1, 2)\\) and \\((x_2, y_2) = (2, 6)\\)</li>
<li>Substitute: \\(d = \\sqrt{(2-(-1))^2 + (6-2)^2}\\)</li>
<li>Simplify: \\(d = \\sqrt{3^2 + 4^2}\\)</li>
<li>Calculate: \\(d = \\sqrt{9 + 16} = \\sqrt{25} = 5\\)</li>
<li>Answer: The distance is <strong>5 units</strong></li>
</ol>
</div>

<div class="success-box">
<p><strong>The 3-4-5 Pythagorean Triple:</strong> Notice that 3, 4, and 5 form a Pythagorean triple (\(3^2 + 4^2 = 5^2\)). This is the most common example in coordinate geometry!</p>
</div></body></html>"""
    },
    {
        "title": "The Midpoint Formula",
        "body": """<html><body><p>The midpoint of a line segment is the point located exactly halfway between the two endpoints.</p>

<div class="concept-box">
<p><strong>Midpoint Formula:</strong></p>
<p style="text-align: center; font-size: 16px;">\\(M = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)\\)</p>
<p>In other words: Average the x-coordinates and average the y-coordinates.</p>
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

  <!-- Endpoints -->
  <circle cx="40" cy="-60" r="4" fill='#58a6ff'/>
  <text x="48" y="-50" fill='#58a6ff' font-weight='bold'>(2, 3)</text>

  <circle cx="120" cy="-20" r="4" fill='#58a6ff'/>
  <text x="90" y="-25" fill='#58a6ff' font-weight='bold'>(6, 1)</text>

  <!-- Line segment -->
  <line x1="40" y1="-60" x2="120" y2="-20" stroke='#58a6ff' stroke-width="2"/>

  <!-- Midpoint -->
  <circle cx="80" cy="-40" r="5" fill='#f85149'/>
  <text x="88" y="-45" fill='#f85149' font-weight='bold'>M(4, 2)</text>

  <!-- Verification lines -->
  <line x1="40" y1="-60" x2="80" y2="-40" stroke='#3fb950' stroke-dasharray="3,3" opacity='0.6'/>
  <line x1="80" y1="-40" x2="120" y2="-20" stroke='#3fb950' stroke-dasharray="3,3" opacity='0.6'/>
  <text x="50" y="-55" fill='#3fb950' font-size='10'>equal</text>
  <text x="100" y="-25" fill='#3fb950' font-size='10'>equal</text>
</svg></body></html>"""
    },
    {
        "title": "Using the Midpoint Formula: Examples",
        "body": """<html><body><p>Let's find midpoints using the formula and verify that the midpoint is equidistant from both endpoints.</p>

<div class="worked-example">
<p><strong>Example 1: Find the midpoint between (2, 4) and (6, 8)</strong></p>
<ol>
<li>Apply the formula: \\(M = \\left( \\frac{2+6}{2}, \\frac{4+8}{2} \\right)\\)</li>
<li>Calculate: \\(M = \\left( \\frac{8}{2}, \\frac{12}{2} \\right)\\)</li>
<li>Answer: \\(M = (4, 6)\\)</li>
<li>Verification: Distance from (2,4) to (4,6) = \\(\\sqrt{(4-2)^2 + (6-4)^2} = \\sqrt{8} = 2\\sqrt{2}\\)</li>
<li>Distance from (4,6) to (6,8) = \\(\\sqrt{(6-4)^2 + (8-6)^2} = \\sqrt{8} = 2\\sqrt{2}\\) ✓</li>
</ol>
</div>

<div class="worked-example">
<p><strong>Example 2: Find the midpoint between (-3, 2) and (5, -4)</strong></p>
<ol>
<li>Apply the formula: \\(M = \\left( \\frac{-3+5}{2}, \\frac{2+(-4)}{2} \\right)\\)</li>
<li>Calculate: \\(M = \\left( \\frac{2}{2}, \\frac{-2}{2} \\right)\\)</li>
<li>Answer: \\(M = (1, -1)\\)</li>
</ol>
</div>

<div class="concept-box">
<p><strong>Key insight:</strong> The midpoint divides the line segment into two equal parts. If you know the midpoint and one endpoint, you can find the other endpoint!</p>
</div></body></html>"""
    }
]
