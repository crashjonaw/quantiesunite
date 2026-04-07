"""Expanding Brackets — Lesson sections."""

TITLE = "Expanding Brackets"

SECTIONS = [
    {
        "title": "What does expanding mean?",
        "body": """<div class="concept-box">
<p><strong>Expanding brackets</strong> means multiplying out the brackets to remove them.</p>
<p>The operation <strong>inside</strong> applies to <strong>each term inside</strong> the brackets.</p>
<div class="formula-box">
<p>\\(3(x + 2) = 3 \\times x + 3 \\times 2 = 3x + 6\\)</p>
</div>
<p>Think of it as <strong>distribution</strong>: the number outside "distributes" to each term inside.</p>
</div>"""
    },
    {
        "title": "Single brackets: the distributive law",
        "body": """<div class="concept-box">
<p>When we expand \\(a(b + c)\\), we multiply \\(a\\) by <strong>both</strong> \\(b\\) and \\(c\\):</p>
<div class="formula-box">
<p>\\(a(b + c) = ab + ac\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Expand:</strong> \\(4(x + 3)\\)</p>
<p>\\(= 4 \\times x + 4 \\times 3\\)</p>
<p>\\(= 4x + 12\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Expand:</strong> \\(5(2x - 1)\\)</p>
<p>\\(= 5 \\times 2x - 5 \\times 1\\)</p>
<p>\\(= 10x - 5\\)</p>
</div>
<p class="warning-box formula-box">
<strong>Be careful with signs:</strong> \\(-3(x - 2) = -3x + 6\\) (negative times negative = positive)
</p>
</div>"""
    },
    {
        "title": "Double brackets: area models",
        "body": """<div class="concept-box">
<p>When we expand \\((a + b)(c + d)\\), we multiply <strong>each term</strong> in the first bracket by <strong>each term</strong> in the second.</p>
<div class="formula-box">
<p>\\((a + b)(c + d) = ac + ad + bc + bd\\)</p>
</div>
<p><strong>An area model helps visualize this:</strong></p>
<svg width="310" height="210" viewBox="-15 -15 340 210" style="border-radius: 4px; margin: 12px 0; display: block">
  <!-- Column headers -->
  <text x="130" y="18" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>a</text>
  <text x="230" y="18" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>b</text>
  <!-- Row headers -->
  <text x="45" y="75" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>c</text>
  <text x="45" y="145" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>d</text>
  <!-- Grid cells (equal 100x70 each) -->
  <rect x="80" y="35" width="100" height="70" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <rect x="180" y="35" width="100" height="70" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <rect x="80" y="105" width="100" height="70" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <rect x="180" y="105" width="100" height="70" rx='4' fill='none' stroke='#1f6feb' stroke-width="2"/>
  <!-- Cell contents -->
  <text x="130" y="75" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>ac</text>
  <text x="230" y="75" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>bc</text>
  <text x="130" y="145" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>ad</text>
  <text x="230" y="145" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='14'>bd</text>
</svg>
<div class="worked-example concept-box">
<p><strong>Expand:</strong> \\((x + 2)(x + 3)\\)</p>
<p>\\(= x \\cdot x + x \\cdot 3 + 2 \\cdot x + 2 \\cdot 3\\)</p>
<p>\\(= x^2 + 3x + 2x + 6\\)</p>
<p>\\(= x^2 + 5x + 6\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Expand:</strong> \\((2x - 1)(x + 4)\\)</p>
<p>\\(= 2x \\cdot x + 2x \\cdot 4 - 1 \\cdot x - 1 \\cdot 4\\)</p>
<p>\\(= 2x^2 + 8x - x - 4\\)</p>
<p>\\(= 2x^2 + 7x - 4\\)</p>
</div>
</div>"""
    },
    {
        "title": "Pattern and check",
        "body": """<div class="concept-box">
<p>After expanding, always check by substituting a simple value like \\(x = 1\\):</p>
<div class="worked-example concept-box">
<p><strong>Check:</strong> \\((x + 2)(x + 3) = x^2 + 5x + 6\\)</p>
<p>Let \\(x = 1\\):</p>
<p><strong>Left side:</strong> \\((1 + 2)(1 + 3) = 3 \\times 4 = 12\\)</p>
<p><strong>Right side:</strong> \\(1^2 + 5(1) + 6 = 1 + 5 + 6 = 12\\) ✓</p>
</div>
<p><strong>Common patterns to recognize:</strong></p>
<div class="formula-box">
<p>Difference of squares: \\((a + b)(a - b) = a^2 - b^2\\)</p>
<p>Perfect square: \\((a + b)^2 = a^2 + 2ab + b^2\\)</p>
</div>
</div>"""
    }
]
