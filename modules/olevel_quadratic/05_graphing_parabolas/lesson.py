TITLE = "Graphing Quadratics: Parabolas"

SECTIONS = [
    {
        "title": "The Quadratic Function and Its Graph",
        "body": """
<h3>Definition: The Parabola</h3>
<p>A <strong>quadratic function</strong> is $f(x) = ax^2 + bx + c$ (where $a \\neq 0$). Its graph is a smooth U-shaped (or inverted U) curve called a <strong>parabola</strong>.</p>

<h3>Key Properties of Parabolas</h3>

<p style="font-size: 1.05em; margin: 15px 0"><strong>1. Opening Direction</strong></p>
<ul style="line-height: 1.8;">
  <li>If $a > 0$: Opens upward (like $\\cup$) — has a <strong>minimum</strong></li>
  <li>If $a < 0$: Opens downward (like $\\cap$) — has a <strong>maximum</strong></li>
</ul>

<p style="font-size: 1.05em; margin: 15px 0"><strong>2. How $|a|$ Affects Shape</strong></p>
<ul style="line-height: 1.8;">
  <li>Larger $|a|$ $\\to$ parabola is <strong>narrower</strong> (steeper sides)</li>
  <li>Smaller $|a|$ $\\to$ parabola is <strong>wider</strong> (gentler slope)</li>
</ul>

<p style="font-size: 1.05em; margin: 15px 0"><strong>3. The Vertex (Turning Point)</strong></p>
<p>The vertex is the point where the parabola changes from decreasing to increasing (or vice versa).</p>
<div class="formula-box">
<p>$$x_v = -\\frac{b}{2a}$$</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">Then evaluate $f(x_v)$ to find $y_v$</p>
</div>

<p style="font-size: 1.05em; margin: 15px 0"><strong>4. Axis of Symmetry</strong></p>
<p>The vertical line $x = -\\frac{b}{2a}$ divides the parabola into two mirror-image halves.</p>

<p style="font-size: 1.05em; margin: 15px 0"><strong>5. Intercepts</strong></p>
<ul style="line-height: 1.8;">
  <li><strong>y-intercept:</strong> Set $x = 0 \\to y = c$</li>
  <li><strong>x-intercepts (roots):</strong> Set $y = 0$ and solve $ax^2 + bx + c = 0$</li>
</ul>
"""
    },
    {
        "title": "Analyzing Parabolas: A Complete Example",
        "body": """
<h3>Step-by-Step Analysis</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Complete Graph Analysis</h4>
<p><strong>Problem:</strong> Analyze $f(x) = -2x^2 + 8x - 6$ completely</p>
<p><strong>Solution:</strong></p>

<p style="margin: 15px 0"><strong>Step 1: Opening Direction</strong><br>
Since $a = -2 < 0$, the parabola opens <strong>downward</strong> (has a maximum)</p>

<p style="margin: 15px 0"><strong>Step 2: Find Vertex</strong><br>
$$x_v = -\\frac{8}{2(-2)} = -\\frac{8}{-4} = 2$$</p>

<p style="margin: 10px 0;">$$f(2) = -2(2)^2 + 8(2) - 6 = -8 + 16 - 6 = 2$$</p>

<p style="margin-top: 10px"><strong>Vertex: (2, 2)</strong></p>

<p style="margin: 15px 0"><strong>Step 3: Axis of Symmetry</strong><br>
$$x = 2$$</p>

<p style="margin: 15px 0"><strong>Step 4: y-intercept</strong><br>
$f(0) = -6$, so y-intercept is $\\mathbf{(0, -6)}$</p>

<p style="margin: 15px 0"><strong>Step 5: x-intercepts (Roots)</strong><br>
Solve $-2x^2 + 8x - 6 = 0$<br>
Divide by $-2$: $x^2 - 4x + 3 = 0$<br>
Factor: $(x - 1)(x - 3) = 0$<br>
<strong>Roots: $x = 1$ and $x = 3$</strong></p>

<p style="margin-top: 10px"><strong>Summary:</strong> Parabola opens downward with vertex at $(2, 2)$, crosses x-axis at $1$ and $3$, and y-axis at $-6$.</p>
</div>

<h3>Sketch Without Plotting Every Point</h3>
<p style="margin: 15px 0">Once you know the vertex, intercepts, and direction, you can sketch the parabola accurately without calculating many points. The parabola is symmetric about $x = 2$.</p>
"""
    },
    {
        "title": "Domain, Range, and Sign Analysis",
        "body": """
<h3>Domain and Range</h3>

<p style="font-size: 1.05em; margin: 15px 0"><strong>Domain:</strong> All quadratic functions have domain $\\mathbb{R}$ (all real numbers)</p>

<p style="font-size: 1.05em; margin: 15px 0"><strong>Range:</strong> Depends on the vertex y-coordinate and opening direction</p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0">
  <tr >
    <th style="padding: 12px; text-align: left"><strong>Opening</strong></th>
    <th style="padding: 12px; text-align: left"><strong>Range</strong></th>
  </tr>
  <tr >
    <td style="padding: 12px;">Upward ($a > 0$)</td>
    <td style="padding: 12px;">$[y_v, \\infty)$ — from the minimum to infinity</td>
  </tr>
  <tr >
    <td style="padding: 12px;">Downward ($a < 0$)</td>
    <td style="padding: 12px;">$(-\\infty, y_v]$ — from negative infinity to the maximum</td>
  </tr>
</table>

<div class="worked-example">
<h4 class="accent-heading">Example 2: Finding Domain and Range</h4>
<p><strong>Problem:</strong> Find the domain and range of $f(x) = x^2 - 4x + 3$</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Domain:</strong> $\\mathbb{R}$ (all real numbers)</p>

<p style="margin: 10px 0;"><strong>Find range:</strong></p>
<p style="margin: 5px 0">$a = 1 > 0$, so opens upward. Find minimum at vertex.</p>
<p>$$x_v = -\\frac{-4}{2(1)} = 2$$</p>
<p>$$f(2) = 2^2 - 4(2) + 3 = 4 - 8 + 3 = -1$$</p>
<p ><strong>Range:</strong> $[-1, \\infty)$</p>
</div>

<h3>Sign Analysis: When is $f(x) > 0$ or $< 0$?</h3>
<p>The sign of $f(x)$ depends on the roots and opening direction:</p>

<div class="worked-example">
<h4 class="accent-heading">Example 3: Sign Analysis</h4>
<p><strong>Problem:</strong> For $f(x) = -2x^2 + 8x - 6$, determine where $f(x) > 0$, $f(x) = 0$, and $f(x) < 0$</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0">From earlier: roots are $x = 1$ and $x = 3$, and $a = -2 < 0$ (opens downward)</p>

<p style="margin: 10px 0;"><strong>$f(x) = 0$ when:</strong> $x = 1$ or $x = 3$</p>

<p style="margin: 10px 0;"><strong>$f(x) > 0$ when:</strong> $1 < x < 3$ (between the roots)</p>

<p style="margin: 10px 0;"><strong>$f(x) < 0$ when:</strong> $x < 1$ or $x > 3$ (outside the roots)</p>

<p style="margin-top: 10px; font-style: italic">This makes sense: the parabola opens downward, so it's positive only between its roots.</p>
</div>

<div class="success-box" style="background-color: rgba(76, 175, 80, 0.1); border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Pattern for sign analysis:</strong> If $a > 0$ (opens up), the parabola is positive OUTSIDE the roots and negative BETWEEN them. If $a < 0$ (opens down), it's reversed!</p>
</div>
"""
    },
    {
        "title": "Transformations: Shifts and Stretches",
        "body": """
<h3>Understanding Transformations via Vertex Form</h3>
<p>Recall: Vertex form is $f(x) = a(x - h)^2 + k$, where the vertex is $(h, k)$.</p>

<p style="margin: 15px 0"><strong>Starting Point:</strong> $f(x) = x^2$ (the basic parabola)</p>

<div class="formula-box">
<p >$f(x) = a(x - h)^2 + k$ transforms the basic parabola by:</p>
<ul style="line-height: 1.8">
  <li><strong>Horizontal shift:</strong> $h$ units right ($h > 0$) or left ($h < 0$)</li>
  <li><strong>Vertical shift:</strong> $k$ units up ($k > 0$) or down ($k < 0$)</li>
  <li><strong>Vertical stretch/compression:</strong> $|a| > 1$ stretches, $|a| < 1$ compresses</li>
  <li><strong>Reflection:</strong> $a < 0$ flips upside down</li>
</ul>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 4: Identifying Transformations</h4>
<p><strong>Problem:</strong> Describe how $f(x) = -2(x + 3)^2 + 5$ is transformed from $g(x) = x^2$</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Rewrite in standard form:</strong> $f(x) = -2(x - (-3))^2 + 5$</p>

<p style="margin: 10px 0;"><strong>Transformations:</strong></p>
<ul style="line-height: 1.8">
  <li>Shift <strong>3 units left</strong> ($h = -3$)</li>
  <li>Shift <strong>5 units up</strong> ($k = 5$)</li>
  <li><strong>Stretch vertically by factor of 2</strong> ($|a| = 2$)</li>
  <li><strong>Reflect downward</strong> ($a < 0$)</li>
</ul>

<p style="margin-top: 10px"><strong>Vertex:</strong> $(-3, 5)$</p>
</div>
"""
    }
]
