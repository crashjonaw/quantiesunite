"""Linear Equations — Lesson sections."""

TITLE = "Linear Equations"

SECTIONS = [
    {
        "title": "The balance method: keeping equations equal",
        "body": """<div class="concept-box">
<p>An equation is like a <strong>balance scale</strong>. Both sides must stay equal.</p>
<p>The golden rule: <strong>Whatever you do to one side, do to the other.</strong></p>
<svg width="320" height="170" viewBox="-15 -15 350 200" style="border-radius: 4px; margin: 12px 0; display: block">
  <!-- Fulcrum triangle -->
  <polygon points="160,155 145,175 175,175" fill='none' stroke='currentColor' stroke-width="2"/>
  <!-- Balance beam -->
  <line x1="30" y1="155" x2="290" y2="155" stroke='currentColor' stroke-width="2"/>
  <!-- Left pan -->
  <rect x="40" y="110" width="80" height="40" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <text x="80" y="136" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>2x + 5</text>
  <!-- Right pan -->
  <rect x="200" y="110" width="80" height="40" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <text x="240" y="136" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>13</text>
  <!-- Equals sign -->
  <text x="160" y="100" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='16'>=</text>
  <!-- Label -->
  <text x="160" y="30" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='13'>Both sides must stay equal</text>
</svg>
<div class="worked-example concept-box">
<p><strong>Solve: 2x + 5 = 13</strong></p>
<p>Subtract 5 from both sides: \\(2x + 5 - 5 = 13 - 5\\)</p>
<p>\\(2x = 8\\)</p>
<p>Divide both sides by 2: \\(\\frac{2x}{2} = \\frac{8}{2}\\)</p>
<p>\\(x = 4\\)</p>
<p><strong>Check:</strong> \\(2(4) + 5 = 8 + 5 = 13\\) ✓</p>
</div>
</div>"""
    },
    {
        "title": "One-step and two-step equations",
        "body": """<div class="concept-box">
<p><strong>One-step equations:</strong> Add, subtract, multiply, or divide once.</p>
<div class="worked-example concept-box">
<p><strong>Solve: x + 7 = 10</strong></p>
<p>Subtract 7: \\(x = 10 - 7 = 3\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: 3x = 12</strong></p>
<p>Divide by 3: \\(x = \\frac{12}{3} = 4\\)</p>
</div>
<p><strong>Two-step equations:</strong> Perform two operations.</p>
<div class="worked-example concept-box">
<p><strong>Solve: 3x - 4 = 11</strong></p>
<p>Add 4 to both sides: \\(3x = 15\\)</p>
<p>Divide by 3: \\(x = 5\\)</p>
<p><strong>Check:</strong> \\(3(5) - 4 = 15 - 4 = 11\\) ✓</p>
</div>
<p class="warning-box formula-box">
<strong>Order matters:</strong> Undo addition/subtraction first, then multiplication/division (reverse BIDMAS).
</p>
</div>"""
    },
    {
        "title": "Multi-step equations with variables on both sides",
        "body": """<div class="concept-box">
<p>When \\(x\\) appears on both sides, collect the variable terms on one side first.</p>
<div class="worked-example concept-box">
<p><strong>Solve: 2x + 3 = x + 7</strong></p>
<p>Subtract \\(x\\) from both sides: \\(x + 3 = 7\\)</p>
<p>Subtract 3: \\(x = 4\\)</p>
<p><strong>Check:</strong> Left: \\(2(4) + 3 = 11\\). Right: \\(4 + 7 = 11\\) ✓</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: 5x - 2 = 3x + 8</strong></p>
<p>Subtract \\(3x\\): \\(2x - 2 = 8\\)</p>
<p>Add 2: \\(2x = 10\\)</p>
<p>Divide by 2: \\(x = 5\\)</p>
<p><strong>Check:</strong> Left: \\(5(5) - 2 = 23\\). Right: \\(3(5) + 8 = 23\\) ✓</p>
</div>
</div>"""
    },
    {
        "title": "Equations with brackets and fractions",
        "body": """<div class="concept-box">
<p>Expand brackets first, then solve using the balance method.</p>
<div class="worked-example concept-box">
<p><strong>Solve: 3(x + 2) = 21</strong></p>
<p>Expand: \\(3x + 6 = 21\\)</p>
<p>Subtract 6: \\(3x = 15\\)</p>
<p>Divide by 3: \\(x = 5\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: \\(\\frac{x}{2} + 3 = 7\\)</strong></p>
<p>Subtract 3: \\(\\frac{x}{2} = 4\\)</p>
<p>Multiply by 2: \\(x = 8\\)</p>
</div>
<p><strong>Solving with fractions:</strong> Multiply all terms by the denominator to clear fractions.</p>
<div class="worked-example concept-box">
<p><strong>Solve: \\(\\frac{x}{3} + 2 = 5\\)</strong></p>
<p>Multiply all terms by 3: \\(x + 6 = 15\\)</p>
<p>Subtract 6: \\(x = 9\\)</p>
</div>
</div>"""
    }
]
