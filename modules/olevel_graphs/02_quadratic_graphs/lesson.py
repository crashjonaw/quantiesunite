SECTIONS = [
    {
        "title": "The Parabola: \\(y = ax^2 + bx + c\\)",
        "body": """
<h3>Quadratic Functions</h3>
<p>A quadratic function has the form: \\(y = ax^2 + bx + c\\)</p>
<p>Its graph is a <strong>parabola</strong> — a U-shaped or upside-down U-shaped curve.</p>

<h3>Key Feature: the Coefficient \\(a\\)</h3>
<ul>
  <li>If \\(a > 0\\): parabola opens upward (∪ shape), has a <strong>minimum</strong></li>
  <li>If \\(a < 0\\): parabola opens downward (∩ shape), has a <strong>maximum</strong></li>
  <li>Larger |a| makes the parabola <strong>narrower</strong></li>
  <li>Smaller |a| makes the parabola <strong>wider</strong></li>
</ul>

<div class="example-box">
<h4>Example 1: Identifying Shape</h4>
<p>\\(y = 2x^2 + 3x - 1\\): \\(a = 2 > 0\\), so opens upward with minimum</p>
<p>\\(y = -\\frac{1}{2}x^2 + 4\\): \\(a = -\\frac{1}{2} < 0\\), so opens downward with maximum</p>
</div>

<svg viewBox="0 0 400 310" class="worked-example">
  <!-- Axes -->
  <line x1="50" y1="155" x2="360" y2="155" stroke='#30363d' stroke-width="1" />
  <line x1="200" y1="15" x2="200" y2="295" stroke='#30363d' stroke-width="1" />
  <!-- Parabola a > 0 (opens up) -->
  <path d="M 80 280 Q 140 100, 200 60 Q 260 100, 320 280" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Parabola a < 0 (opens down) -->
  <path d="M 80 30 Q 140 210, 200 250 Q 260 210, 320 30" stroke='#ffa657' stroke-width="2" fill='none' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='12' fill='currentColor'>
    <text x="365" y="159">x</text>
    <text x="192" y="12">y</text>
    <text x="330" y="265" fill='#58a6ff'>a &gt; 0</text>
    <text x="330" y="50" fill='#ffa657'>a &lt; 0</text>
  </g>
</svg>

<h3>The y-intercept</h3>
<p>Set \\(x = 0\\): \\(y = c\\)</p>
<p>The parabola always crosses the y-axis at \\((0, c)\\)</p>

<h3>The Roots (x-intercepts)</h3>
<p>Set \\(y = 0\\) and solve \\(ax^2 + bx + c = 0\\)</p>
<p>There can be 0, 1, or 2 real roots depending on the discriminant \\(\\Delta = b^2 - 4ac\\)</p>
"""
    },
    {
        "title": "Vertex, Axis of Symmetry, and Key Points",
        "body": """
<h3>The Vertex (Turning Point)</h3>
<p>The vertex is where the parabola reaches its minimum or maximum.</p>
<p>The x-coordinate of the vertex is: \\(x = -\\frac{b}{2a}\\)</p>
<p>Substitute this into the equation to find the y-coordinate.</p>

<div class="example-box">
<h4>Example 2: Finding the Vertex</h4>
<p><strong>Problem:</strong> Find the vertex of \\(y = x^2 - 4x + 3\\)</p>
<p>\\(a = 1, b = -4, c = 3\\)</p>
<p>\\(x = -\\frac{-4}{2(1)} = 2\\)</p>
<p>\\(y = 2^2 - 4(2) + 3 = 4 - 8 + 3 = -1\\)</p>
<p>Vertex: \\((2, -1)\\)</p>
</div>

<h3>Axis of Symmetry</h3>
<p>The vertical line passing through the vertex: \\(x = -\\frac{b}{2a}\\)</p>
<p>The parabola is mirror-symmetric about this line.</p>

<h3>Finding Roots from the Parabola</h3>
<p>Where the parabola crosses the x-axis.</p>
<p>For \\(y = x^2 - 4x + 3\\):</p>
<p>Set \\(y = 0\\): \\(x^2 - 4x + 3 = 0\\)</p>
<p>Factor: \\((x-1)(x-3) = 0\\)</p>
<p>Roots: \\(x = 1\\) and \\(x = 3\\)</p>

<svg viewBox="0 0 400 310" class="worked-example">
  <!-- Axes -->
  <line x1="50" y1="250" x2="360" y2="250" stroke='#30363d' stroke-width="1" />
  <line x1="50" y1="30" x2="50" y2="250" stroke='#30363d' stroke-width="1" />
  <!-- Axis of symmetry -->
  <line x1="200" y1="40" x2="200" y2="250" stroke='#8b949e' stroke-width="1" stroke-dasharray="5,5" />
  <!-- Parabola -->
  <path d="M 80 240 Q 140 80, 200 50 Q 260 80, 320 240" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Root points -->
  <circle cx="100" cy="250" r="4" fill='#79c0ff' />
  <circle cx="300" cy="250" r="4" fill='#79c0ff' />
  <!-- Vertex -->
  <circle cx="200" cy="50" r="5" fill='#ffa657' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="365" y="254">x</text>
    <text x="42" y="25">y</text>
    <text x="75" y="272" fill='#79c0ff'>root 1</text>
    <text x="278" y="272" fill='#79c0ff'>root 2</text>
    <text x="212" y="48" fill='#ffa657'>vertex</text>
    <text x="212" y="30" fill='currentColor' opacity='0.6' font-size='10'>axis of symmetry</text>
  </g>
</svg>

<h3>Standard Form & Vertex Form</h3>
<p><strong>Standard form:</strong> \\(y = ax^2 + bx + c\\)</p>
<p><strong>Vertex form:</strong> \\(y = a(x - h)^2 + k\\) where \\((h, k)\\) is the vertex</p>
<p>Vertex form shows the transformations clearly (shift right \\(h\\), up \\(k\\))</p>
"""
    },
    {
        "title": "Sketching Parabolas",
        "body": """
<h3>5-Point Method to Sketch \\(y = ax^2 + bx + c\\)</h3>
<ol>
  <li>Find and plot the y-intercept: \\((0, c)\\)</li>
  <li>Find the vertex: \\(x = -\\frac{b}{2a}\\), then find \\(y\\)</li>
  <li>Find the roots by solving \\(ax^2 + bx + c = 0\\)</li>
  <li>Use symmetry: if you know one point, the symmetric point is equidistant from the axis</li>
  <li>Draw a smooth curve through all points</li>
</ol>

<div class="example-box">
<h4>Example 3: Complete Sketch</h4>
<p><strong>Sketch \\(y = x^2 - 2x - 3\\)</strong></p>
<p><strong>Step 1:</strong> y-intercept: \\(y = -3\\) → \\((0, -3)\\)</p>
<p><strong>Step 2:</strong> Vertex: \\(x = -\\frac{-2}{2} = 1\\), \\(y = 1 - 2 - 3 = -4\\) → \\((1, -4)\\)</p>
<p><strong>Step 3:</strong> Roots: \\(x^2 - 2x - 3 = 0\\) → \\((x-3)(x+1) = 0\\) → \\(x = 3, -1\\)</p>
<p><strong>Step 4:</strong> By symmetry about \\(x = 1\\): points \\((-1, 0)\\) and \\((3, 0)\\)</p>
</div>

<svg viewBox="0 0 400 330" class="worked-example">
  <!-- Axes -->
  <line x1="60" y1="200" x2="360" y2="200" stroke='#30363d' stroke-width="1" />
  <line x1="120" y1="30" x2="120" y2="310" stroke='#30363d' stroke-width="1" />
  <!-- Parabola y = x^2 - 2x - 3 -->
  <path d="M 50 230 Q 120 310, 190 310 Q 260 310, 330 230" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- y-intercept (0, -3) -->
  <circle cx="120" cy="260" r="4" fill='#79c0ff' />
  <!-- Root at x = -1 -->
  <circle cx="90" cy="200" r="4" fill='#79c0ff' />
  <!-- Root at x = 3 -->
  <circle cx="210" cy="200" r="4" fill='#79c0ff' />
  <!-- Vertex (1, -4) -->
  <circle cx="150" cy="310" r="5" fill='#ffa657' />
  <!-- Tick marks -->
  <line x1="90" y1="196" x2="90" y2="204" stroke='#30363d' stroke-width="1" />
  <line x1="210" y1="196" x2="210" y2="204" stroke='#30363d' stroke-width="1" />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="365" y="204">x</text>
    <text x="112" y="25">y</text>
    <text x="124" y="215">O</text>
    <text x="75" y="265" fill='#79c0ff'>(0, &#x2212;3)</text>
    <text x="70" y="194" fill='#79c0ff'>&#x2212;1</text>
    <text x="215" y="194" fill='#79c0ff'>3</text>
    <text x="162" y="325" fill='#ffa657'>(1, &#x2212;4)</text>
  </g>
</svg>

<h3>Checking Your Sketch</h3>
<ul>
  <li>Does the parabola open in the right direction (check \\(a\\))?</li>
  <li>Are the roots correct (where \\(y = 0\\))?</li>
  <li>Does it pass through \\((0, c)\\)?</li>
  <li>Is the vertex clearly marked?</li>
  <li>Is the curve smooth (not pointy or angular)?</li>
</ul>
"""
    },
    {
        "title": "Solving Problems with Quadratics",
        "body": """
<h3>Finding Roots Using the Quadratic Formula</h3>
<p>For \\(ax^2 + bx + c = 0\\):</p>
<p>$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$</p>

<p>The discriminant \\(\\Delta = b^2 - 4ac\\) tells us:</p>
<ul>
  <li>If \\(\\Delta > 0\\): Two distinct real roots (parabola crosses x-axis twice)</li>
  <li>If \\(\\Delta = 0\\): One repeated root (parabola touches x-axis at vertex)</li>
  <li>If \\(\\Delta < 0\\): No real roots (parabola doesn't cross x-axis)</li>
</ul>

<div class="example-box">
<h4>Example 4: Using the Quadratic Formula</h4>
<p><strong>Solve \\(2x^2 - 5x + 2 = 0\\)</strong></p>
<p>\\(a = 2, b = -5, c = 2\\)</p>
<p>\\(\\Delta = (-5)^2 - 4(2)(2) = 25 - 16 = 9\\)</p>
<p>\\(x = \\frac{5 \\pm 3}{4}\\)</p>
<p>\\(x = 2\\) or \\(x = 0.5\\)</p>
</div>

<h3>Real-World Application: Projectile Motion</h3>
<p>A ball thrown upward follows: \\(h = -5t^2 + 20t + 2\\)</p>
<p>where \\(h\\) is height (m) and \\(t\\) is time (s)</p>
<p>Maximum height occurs at the vertex \\(t = -\\frac{20}{2(-5)} = 2\\) seconds</p>
<p>Maximum height: \\(h = -5(4) + 20(2) + 2 = 22\\) m</p>

<h3>Range of a Quadratic Function</h3>
<p>The range depends on whether it opens up or down and where the vertex is:</p>
<ul>
  <li>Opens up (\\(a > 0\\)): Range is \\([k, \\infty)\\) where \\(k\\) is the minimum y-value</li>
  <li>Opens down (\\(a < 0\\)): Range is \\((-\\infty, k]\\) where \\(k\\) is the maximum y-value</li>
</ul>

<div class="example-box">
<h4>Example 5: Finding Range</h4>
<p>\\(y = -x^2 + 4x + 1\\) with \\(a = -1 < 0\\)</p>
<p>Vertex: \\(x = -\\frac{4}{-2} = 2\\), \\(y = -4 + 8 + 1 = 5\\)</p>
<p>Range: \\((-\\infty, 5]\\)</p>
</div>
"""
    }
]
