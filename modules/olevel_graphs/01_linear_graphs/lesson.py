SECTIONS = [
    {
        "title": "Gradient and y-intercept",
        "body": """
<h3>The Linear Equation</h3>
<p>A straight line follows the equation: \\(y = mx + c\\) where:</p>
<ul>
  <li>\\(m\\) is the <strong>gradient</strong> (slope) — how steep the line is</li>
  <li>\\(c\\) is the <strong>y-intercept</strong> — where the line crosses the y-axis</li>
</ul>

<h3>Understanding Gradient</h3>
<p>Gradient measures rise over run:</p>
<p>$$m = \\frac{\\text{rise}}{\\text{run}} = \\frac{y_2 - y_1}{x_2 - x_1}$$</p>
<p>A positive gradient slopes upward (↗), negative slopes downward (↘), zero is horizontal, undefined is vertical.</p>

<div class="example-box">
<h4>Example 1: Finding Gradient</h4>
<p>Find the gradient of the line through (1, 2) and (4, 8).</p>
<p>$$m = \\frac{8-2}{4-1} = \\frac{6}{3} = 2$$</p>
<p>For every 1 unit right, the line goes up 2 units.</p>
</div>

<svg width="400" height="300" class="worked-example">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='currentColor' opacity='0.6' />
    </marker>
  </defs>
  <g id="grid">
    <line x1="50" y1="250" x2="350" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="50" x2="50" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="250" x2="350" y2="50" stroke='#58a6ff' stroke-width="2" />
  </g>
  <g id="labels" font-family='Arial' font-size='12' fill='currentColor'>
    <text x="360" y="255">x</text>
    <text x="40" y="40">y</text>
    <text x="45" y="265">O</text>
    <text x="200" y="175" fill='#ffa657'>m = 2</text>
    <text x="200" y="30" fill='#ffa657'>c = 0</text>
  </g>
  <circle cx="50" cy="250" r="3" fill='#79c0ff' />
  <circle cx="150" cy="150" r="3" fill='#79c0ff' />
  <circle cx="250" cy="50" r="3" fill='#79c0ff' />
</svg>

<h3>Reading from a Graph</h3>
<p>To find the equation:</p>
<ol>
  <li>Find where the line crosses the y-axis (read \\(c\\))</li>
  <li>Pick any two clear points and calculate \\(m = \\frac{\\Delta y}{\\Delta x}\\)</li>
  <li>Write \\(y = mx + c\\)</li>
</ol>
"""
    },
    {
        "title": "Equation of a Line",
        "body": """
<h3>Three Forms of Linear Equations</h3>

<p><strong>Slope-intercept form:</strong> \\(y = mx + c\\)</p>
<p>Use when you know the gradient and y-intercept.</p>

<p><strong>Point-slope form:</strong> \\(y - y_1 = m(x - x_1)\\)</p>
<p>Use when you know the gradient and one point.</p>

<p><strong>General form:</strong> \\(Ax + By + C = 0\\)</p>
<p>Use when working with parallel/perpendicular lines algebraically.</p>

<div class="example-box">
<h4>Example 2: Finding Line Equations</h4>
<p><strong>Problem:</strong> Find the equation of the line through (2, 5) with gradient 3.</p>
<p>Using point-slope: \\(y - 5 = 3(x - 2)\\)</p>
<p>\\(y - 5 = 3x - 6\\)</p>
<p>\\(y = 3x - 1\\)</p>
</div>

<div class="example-box">
<h4>Example 3: Converting Forms</h4>
<p>Convert \\(2x - 3y + 6 = 0\\) to slope-intercept form.</p>
<p>\\(3y = 2x + 6\\)</p>
<p>\\(y = \\frac{2}{3}x + 2\\)</p>
<p>So \\(m = \\frac{2}{3}\\) and \\(c = 2\\)</p>
</div>

<h3>Key Points</h3>
<ul>
  <li>To find x-intercept, set \\(y = 0\\) and solve for \\(x\\)</li>
  <li>To find y-intercept, set \\(x = 0\\) and solve for \\(y\\)</li>
  <li>Intercepts are useful for sketching quickly</li>
</ul>
"""
    },
    {
        "title": "Parallel and Perpendicular Lines",
        "body": """
<h3>Parallel Lines</h3>
<p>Two lines are parallel if they have the <strong>same gradient</strong>.</p>
<p>If \\(y = m_1x + c_1\\) is parallel to \\(y = m_2x + c_2\\), then \\(m_1 = m_2\\)</p>

<div class="example-box">
<h4>Example 4: Parallel Lines</h4>
<p><strong>Problem:</strong> Write the equation of a line parallel to \\(y = 3x + 2\\) passing through (1, 4).</p>
<p>Parallel line has gradient 3.</p>
<p>Using \\(y - 4 = 3(x - 1)\\)</p>
<p>\\(y = 3x + 1\\)</p>
</div>

<h3>Perpendicular Lines</h3>
<p>Two lines are perpendicular if their gradients multiply to give <strong>−1</strong>:</p>
<p>If \\(m_1 \\times m_2 = -1\\), then \\(m_2 = -\\frac{1}{m_1}\\)</p>

<svg width="400" height="320" class="worked-example">
  <g id="grid">
    <line x1="50" y1="250" x2="350" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="50" x2="50" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="100" y1="250" x2="300" y2="100" stroke='#58a6ff' stroke-width="2" />
    <line x1="150" y1="250" x2="300" y2="50" stroke='#ffa657' stroke-width="2" />
  </g>
  <g id="labels" font-family='Arial' font-size='12' fill='currentColor'>
    <text x="360" y="255">x</text>
    <text x="40" y="40">y</text>
    <text x="200" y="30" fill='#58a6ff'>m₁ = 2</text>
    <text x="200" y="65" fill='#ffa657'>m₂ = -½</text>
    <text x="220" y="160" fill='#79c0ff' font-size='14'>90°</text>
  </g>
</svg>

<div class="example-box">
<h4>Example 5: Perpendicular Lines</h4>
<p><strong>Problem:</strong> Find a line perpendicular to \\(y = 2x + 3\\) through (0, 1).</p>
<p>Perpendicular gradient: \\(m = -\\frac{1}{2}\\)</p>
<p>\\(y = -\\frac{1}{2}x + 1\\)</p>
<p>Check: \\(2 \\times (-\\frac{1}{2}) = -1\\) ✓</p>
</div>

<h3>Quick Method</h3>
<ul>
  <li>Parallel: Copy the gradient</li>
  <li>Perpendicular: Flip and negate the gradient (reciprocal with opposite sign)</li>
</ul>
"""
    },
    {
        "title": "Sketching Linear Graphs",
        "body": """
<h3>Method to Sketch \\(y = mx + c\\)</h3>
<ol>
  <li>Plot the y-intercept \\((0, c)\\)</li>
  <li>Use gradient \\(m\\) to find another point: go right 1 unit, up \\(m\\) units</li>
  <li>Draw a straight line through both points, extending both ways with arrows</li>
</ol>

<div class="example-box">
<h4>Example 6: Sketching \\(y = -2x + 4\\)</h4>
<p>Step 1: y-intercept is (0, 4)</p>
<p>Step 2: Gradient is −2, so go right 1, down 2 → point (1, 2)</p>
<p>Step 3: Draw line through (0, 4) and (1, 2)</p>
<p>Step 4: Find x-intercept: set \\(y = 0\\): \\(0 = -2x + 4 → x = 2\\)</p>
</div>

<svg width="400" height="300" class="worked-example">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='currentColor' opacity='0.6' />
    </marker>
  </defs>
  <g id="grid">
    <line x1="50" y1="50" x2="350" y2="250" stroke='#58a6ff' stroke-width="2" marker-end="url(#arrow)" />
    <line x1="50" y1="250" x2="350" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="50" x2="50" y2="250" stroke='#30363d' stroke-width="1" />
  </g>
  <circle cx="50" cy="50" r="4" fill='#79c0ff' />
  <circle cx="200" cy="150" r="4" fill='#79c0ff' />
  <g id="labels" font-family='Arial' font-size='12' fill='currentColor'>
    <text x="360" y="255">x</text>
    <text x="40" y="40">y</text>
    <text x="45" y="265">O</text>
    <text x="30" y="50">4</text>
    <text x="200" y="265">2</text>
    <text x="60" y="45" fill='#ffa657'>(0, 4)</text>
    <text x="210" y="140" fill='#ffa657'>(1, 2)</text>
  </g>
</svg>

<h3>From Graph to Equation</h3>
<p>Reverse the process:</p>
<ol>
  <li>Read the y-intercept from the graph → this is \\(c\\)</li>
  <li>Identify two clear grid points and calculate \\(m = \\frac{\\Delta y}{\\Delta x}\\)</li>
  <li>Write \\(y = mx + c\\)</li>
</ol>

<h3>Real-World Example</h3>
<p>A taxi charges £2 per mile plus £5 base fare: \\(\\text{Cost} = 2d + 5\\) (where \\(d\\) is distance).</p>
<p>The y-intercept is 5 (base fare), gradient is 2 (cost per mile).</p>
"""
    }
]
