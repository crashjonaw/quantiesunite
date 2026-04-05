TITLE = "Completing the Square"

SECTIONS = [
    {
        "title": "The Core Idea: Creating a Perfect Square",
        "body": """
<h3>Why Complete the Square?</h3>
<p>Factoring doesn't always work (try factoring $x^2 + 6x + 4$!). <strong>Completing the square</strong> is a technique that works for ANY quadratic. It transforms an unfactorable expression into a perfect square.</p>

<h3>The Geometric Intuition</h3>
<p>Think of $x^2 + 6x$ as the area of an L-shaped region:</p>
<ul style="line-height: 1.8">
  <li>$x^2$ is a square with side $x$</li>
  <li>$6x$ is an L-shaped region (two $3 \\times x$ rectangles)</li>
</ul>

<p style="margin-top: 15px"><strong>To complete the square:</strong> We add a small square ($3^2 = 9$) at the corner to finish the larger square!</p>

<p style="margin-top: 15px;">$$x^2 + 6x + 9 = (x + 3)^2$$</p>

<p style="margin-top: 15px">This works because $(x + 3)^2 = x^2 + 6x + 9$ by expansion.</p>

<h3>The Formula</h3>
<div class="formula-box">
<p >To complete the square for $x^2 + bx$:</p>
<p>$$x^2 + bx = \\left(x + \\frac{b}{2}\\right)^2 - \\left(\\frac{b}{2}\\right)^2$$</p>
</div>

<p style="margin-top: 15px; font-style: italic">Key: Take half the coefficient of $x$, square it, then add and subtract that value.</p>
"""
    },
    {
        "title": "Solving Equations by Completing the Square",
        "body": """
<h3>Step-by-Step Process</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Monic Quadratic ($a=1$)</h4>
<p><strong>Problem:</strong> Solve $x^2 + 6x + 4 = 0$</p>
<p><strong>Solution (Step by Step):</strong></p>
<p><strong>Step 1:</strong> Isolate the $x$ terms<br>
$$x^2 + 6x = -4$$</p>

<p><strong>Step 2:</strong> Complete the square. Take half of $6 \\to 3$, then square $\\to 9$<br>
$$x^2 + 6x + 9 = -4 + 9$$</p>

<p><strong>Step 3:</strong> Write the left side as a perfect square<br>
$$(x + 3)^2 = 5$$</p>

<p><strong>Step 4:</strong> Take square roots<br>
$$x + 3 = \\pm \\sqrt{5}$$</p>

<p><strong>Step 5:</strong> Solve for $x$<br>
$$x = -3 \\pm \\sqrt{5}$$</p>

<p style="margin-top: 10px"><strong>Answer:</strong> $x = -3 + \\sqrt{5} \\approx -0.76$ or $x = -3 - \\sqrt{5} \\approx -5.24$</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 2: When $a \\neq 1$</h4>
<p><strong>Problem:</strong> Solve $2x^2 + 8x - 10 = 0$</p>
<p><strong>Solution:</strong></p>
<p><strong>Step 1:</strong> Divide the entire equation by the leading coefficient ($2$)<br>
$$x^2 + 4x - 5 = 0$$</p>

<p><strong>Step 2:</strong> Isolate $x$ terms<br>
$$x^2 + 4x = 5$$</p>

<p><strong>Step 3:</strong> Complete the square. Half of $4$ is $2$, square to get $4$<br>
$$x^2 + 4x + 4 = 5 + 4$$</p>

<p><strong>Step 4:</strong> Perfect square form<br>
$$(x + 2)^2 = 9$$</p>

<p><strong>Step 5:</strong> Take square roots<br>
$$x + 2 = \\pm 3$$</p>

<p><strong>Step 6:</strong> Solve<br>
$$x = -2 + 3 = 1 \\quad \\text{or} \\quad x = -2 - 3 = -5$$</p>

<p style="margin-top: 10px"><strong>Answer:</strong> $x = 1$ or $x = -5$</p>
</div>
"""
    },
    {
        "title": "Vertex Form: From Completing the Square",
        "body": """
<h3>The Power of Completing the Square: Vertex Form</h3>
<p>When we complete the square for a quadratic function (not equation), we reveal its graph structure:</p>

<div class="formula-box">
<p ><strong>Vertex Form:</strong></p>
<p>$$f(x) = a(x - h)^2 + k$$</p>
<p style="margin-top: 10px; font-size: 0.95em">The vertex (turning point) is at the point $(h, k)$</p>
</div>

<h3>Why This Matters</h3>
<p>From vertex form, we immediately know:</p>
<ul style="line-height: 1.8;">
  <li><strong>Vertex:</strong> $(h, k)$ — the peak or valley</li>
  <li><strong>Axis of symmetry:</strong> $x = h$ — the line of mirror symmetry</li>
  <li><strong>Direction:</strong> Opens up if $a > 0$, opens down if $a < 0$</li>
  <li><strong>Shift:</strong> $h$ units right/left, $k$ units up/down from $y = ax^2$</li>
</ul>

<div class="worked-example">
<h4 class="accent-heading">Example 3: Converting to Vertex Form</h4>
<p><strong>Problem:</strong> Write $f(x) = 2x^2 - 8x + 3$ in vertex form</p>
<p><strong>Solution:</strong></p>
<p><strong>Step 1:</strong> Factor out the leading coefficient from $x$ terms<br>
$$f(x) = 2(x^2 - 4x) + 3$$</p>

<p><strong>Step 2:</strong> Complete the square inside parentheses. Half of $-4$ is $-2$, square is $4$<br>
$$f(x) = 2(x^2 - 4x + 4 - 4) + 3$$</p>

<p><strong>Step 3:</strong> Rewrite<br>
$$f(x) = 2((x - 2)^2 - 4) + 3$$</p>

<p><strong>Step 4:</strong> Distribute the $2$ and simplify<br>
$$f(x) = 2(x - 2)^2 - 8 + 3$$<br>
$$f(x) = 2(x - 2)^2 - 5$$</p>

<p style="margin-top: 10px"><strong>Vertex Form:</strong> $f(x) = 2(x - 2)^2 - 5$</p>
<p style="margin-top: 5px"><strong>Vertex:</strong> $(2, -5)$ | <strong>Axis of symmetry:</strong> $x = 2$</p>
</div>

<div class="success-box" style="background-color: rgba(76, 175, 80, 0.1); border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Key Insight:</strong> Vertex form immediately tells you the vertex, while standard form requires calculation. Both are useful!</p>
</div>
"""
    }
]
