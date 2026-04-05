TITLE = "Factoring Quadratics"

SECTIONS = [
    {
        "title": "Why Factoring Works: The Zero-Product Property",
        "body": """
<h3>The Fundamental Principle</h3>
<p>At the heart of factoring is a simple but powerful truth:</p>
<div class="formula-box">
<p><strong>If AB = 0, then A = 0 or B = 0</strong></p>
</div>

<p>This is the <strong>zero-product property</strong>. It means if two things multiply to give zero, at least one of them must be zero.</p>

<h3>Applying It to Quadratics</h3>
<p>If we can write ax² + bx + c as a(x - α)(x - β), then:</p>
<p>$$a(x - \\alpha)(x - \\beta) = 0$$</p>
<p>Since a ≠ 0, we must have (x - α) = 0 or (x - β) = 0, giving us:</p>
<div class="formula-box">
<p>$$x = \\alpha \\quad \\text{or} \\quad x = \\beta$$</p>
</div>

<p style="font-size: 1.05em; margin-top: 15px">The question becomes: <strong>How do we find α and β?</strong></p>
"""
    },
    {
        "title": "Method 1: Trial and Error (Simple Cases)",
        "body": """
<h3>The Key Insight</h3>
<p>For x² + bx + c, we need two numbers that:</p>
<ul style="line-height: 1.8;">
  <li><strong>Multiply to c</strong></li>
  <li><strong>Add to b</strong></li>
</ul>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Simple Factoring</h4>
<p><strong>Problem:</strong> Factor and solve x² + 5x + 6 = 0</p>
<p><strong>Solution:</strong></p>
<p style="margin: 5px 0">We need two numbers that:</p>
<ul style="margin: 5px 0">
  <li>Multiply to 6</li>
  <li>Add to 5</li>
</ul>
<p style="margin: 10px 0;">The pairs that multiply to 6 are: (1,6), (2,3), (-1,-6), (-2,-3)</p>
<p style="margin: 10px 0;">Which pair adds to 5? <strong>2 and 3!</strong> (since 2 + 3 = 5)</p>
<p>$$x^2 + 5x + 6 = (x + 2)(x + 3) = 0$$</p>
<p style="margin: 10px 0;"><strong>Therefore:</strong> x = -2 or x = -3</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 2: With Negative Numbers</h4>
<p><strong>Problem:</strong> Factor and solve x² - 5x + 6 = 0</p>
<p><strong>Solution:</strong></p>
<p style="margin: 5px 0">We need two numbers that multiply to 6 and add to -5.</p>
<p style="margin: 10px 0;"><strong>Answer: -2 and -3</strong> (since (-2)(-3) = 6 and -2 + (-3) = -5)</p>
<p>$$x^2 - 5x + 6 = (x - 2)(x - 3) = 0$$</p>
<p style="margin: 10px 0;"><strong>Therefore:</strong> x = 2 or x = 3</p>
</div>
"""
    },
    {
        "title": "Method 2: AC Method (When a ≠ 1)",
        "body": """
<h3>The Problem with ax² + bx + c when a ≠ 1</h3>
<p>When the coefficient of x² is not 1, trial and error becomes harder. We use the <strong>AC method</strong>:</p>

<p style="font-size: 1.05em; line-height: 1.8"><strong>Step 1:</strong> Calculate AC = a × c<br>
<strong>Step 2:</strong> Find two numbers that multiply to AC and add to b<br>
<strong>Step 3:</strong> Rewrite bx as a sum using these two numbers<br>
<strong>Step 4:</strong> Factor by grouping</p>

<div class="worked-example">
<h4 class="accent-heading">Example 3: AC Method in Action</h4>
<p><strong>Problem:</strong> Solve 2x² + 5x + 3 = 0</p>
<p><strong>Solution:</strong></p>
<p><strong>Step 1:</strong> AC = 2 × 3 = 6 (and b = 5)</p>
<p><strong>Step 2:</strong> Find two numbers that multiply to 6 and add to 5: <strong>2 and 3</strong></p>
<p><strong>Step 3:</strong> Rewrite: 2x² + 5x + 3 = 2x² + 2x + 3x + 3</p>
<p><strong>Step 4:</strong> Factor by grouping:</p>
<p>$$\\begin{align}
2x^2 + 2x + 3x + 3 &= 2x(x + 1) + 3(x + 1) \\\\
&= (2x + 3)(x + 1) = 0
\\end{align}$$</p>
<p style="margin: 10px 0;"><strong>Therefore:</strong> x = -3/2 or x = -1</p>
</div>

<div class="success-box" style="background-color: rgba(76, 175, 80, 0.1); border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Why this works:</strong> Grouping reveals the common factor (x + 1), which is the hidden structure in the original quadratic.</p>
</div>
"""
    },
    {
        "title": "Special Cases: Perfect Squares and Differences",
        "body": """
<h3>Perfect Square Trinomials</h3>
<p>Some quadratics are perfect squares and factor immediately:</p>
<div class="formula-box">
<p>$$x^2 + 2px + p^2 = (x + p)^2$$</p>
<p>$$x^2 - 2px + p^2 = (x - p)^2$$</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 4: Perfect Square</h4>
<p><strong>Problem:</strong> Solve x² - 8x + 16 = 0</p>
<p><strong>Solution:</strong></p>
<p>Notice: 16 = 4², and -8 = 2(-4)</p>
<p>$$x^2 - 8x + 16 = (x - 4)^2 = 0$$</p>
<p style="margin: 10px 0;"><strong>Therefore:</strong> x = 4 (repeated root)</p>
</div>

<h3>Difference of Squares</h3>
<div class="formula-box">
<p>$$x^2 - p^2 = (x - p)(x + p)$$</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 5: Difference of Squares</h4>
<p><strong>Problem:</strong> Solve x² - 9 = 0</p>
<p><strong>Solution:</strong></p>
<p>$$x^2 - 9 = (x - 3)(x + 3) = 0$$</p>
<p style="margin: 10px 0;"><strong>Therefore:</strong> x = 3 or x = -3</p>
</div>

<div class="warning-box" style="background-color: rgba(255, 165, 0, 0.1); border-left: 4px solid #ff9800; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Key Insight:</strong> Always check if your quadratic is a perfect square or difference of squares first—these are fastest to factor!</p>
</div>
"""
    }
]
