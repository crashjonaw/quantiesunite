"""Introduction to Inequalities — Lesson sections."""

TITLE = "Introduction to Inequalities"

SECTIONS = [
    {
        "title": "From equals to inequality symbols",
        "body": """<div class="concept-box">
<p>An <strong>equation</strong> says two things are equal. An <strong>inequality</strong> says one is greater or less than the other.</p>
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
<tr >
<th style="padding: 8px; text-align: left"><strong>Symbol</strong></th>
<th style="padding: 8px; text-align: left"><strong>Meaning</strong></th>
<th style="padding: 8px; text-align: left"><strong>Example</strong></th>
</tr>
<tr >
<td style="padding: 8px;">&gt;</td>
<td style="padding: 8px;">Greater than</td>
<td style="padding: 8px;">\\(x > 5\\)</td>
</tr>
<tr >
<td style="padding: 8px;">&lt;</td>
<td style="padding: 8px;">Less than</td>
<td style="padding: 8px;">\\(x < 3\\)</td>
</tr>
<tr >
<td style="padding: 8px;">\\(\\geq\\)</td>
<td style="padding: 8px;">Greater than or equal to</td>
<td style="padding: 8px;">\\(x \\geq 4\\)</td>
</tr>
<tr >
<td style="padding: 8px;">\\(\\leq\\)</td>
<td style="padding: 8px;">Less than or equal to</td>
<td style="padding: 8px;">\\(x \\leq 2\\)</td>
</tr>
</table>
<p><strong>Remember:</strong> The open part of the symbol points to the larger number.</p>
<div class="formula-box">
<p>\\(7 > 3\\) (7 is greater than 3) ✓</p>
<p>\\(2 < 8\\) (2 is less than 8) ✓</p>
</div>
</div>"""
    },
    {
        "title": "Solving simple inequalities",
        "body": """<div class="concept-box">
<p>Solving inequalities is like solving equations — use the balance method. But there's one important rule:</p>
<p class="warning-box formula-box">
<strong>When you multiply or divide by a negative number, flip the inequality sign!</strong>
</p>
<div class="worked-example concept-box">
<p><strong>Solve: x + 3 > 7</strong></p>
<p>Subtract 3: \\(x > 4\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: 2x ≤ 10</strong></p>
<p>Divide by 2: \\(x \\leq 5\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: -x > 3</strong></p>
<p>Multiply by -1 (flip the sign): \\(x < -3\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Solve: 2x + 1 < 9</strong></p>
<p>Subtract 1: \\(2x < 8\\)</p>
<p>Divide by 2: \\(x < 4\\)</p>
</div>
</div>"""
    },
    {
        "title": "Number lines and solution sets",
        "body": """<div class="concept-box">
<p>We show the solution to an inequality on a <strong>number line</strong>.</p>
<svg width="360" height="110" viewBox="-15 -15 390 140" style="border-radius: 4px; margin: 12px 0; display: block">
  <!-- Title -->
  <text x="180" y="15" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='13'>x &lt; 5 : open circle at 5, shade left</text>
  <!-- Main line -->
  <line x1="30" y1="55" x2="330" y2="55" stroke='currentColor' stroke-width="2"/>
  <!-- Tick marks at equal spacing (50px apart) -->
  <line x1="30" y1="48" x2="30" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="80" y1="48" x2="80" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="130" y1="48" x2="130" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="180" y1="48" x2="180" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="230" y1="48" x2="230" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="280" y1="48" x2="280" y2="62" stroke='currentColor' stroke-width="2"/>
  <line x1="330" y1="48" x2="330" y2="62" stroke='currentColor' stroke-width="2"/>
  <!-- Number labels -->
  <text x="30" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>0</text>
  <text x="80" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>1</text>
  <text x="130" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>2</text>
  <text x="180" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>3</text>
  <text x="230" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>4</text>
  <text x="280" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>5</text>
  <text x="330" y="80" text-anchor='middle' fill='currentColor' font-family='sans-serif' font-size='12'>6</text>
  <!-- Shaded region: arrow from left to open circle at 5 -->
  <line x1="30" y1="55" x2="275" y2="55" stroke='#1f6feb' stroke-width="4"/>
  <!-- Arrow at left end -->
  <polygon points="30,50 30,60 20,55" fill='#1f6feb'/>
  <!-- Open circle at 5 (not included) -->
  <circle cx="280" cy="55" r="6" fill='#0d1117' stroke='#1f6feb' stroke-width="2"/>
</svg>
<p><strong>Symbols on the number line:</strong></p>
<ul >
<li><strong>Open circle (○)</strong> for &lt; and &gt; (not including the value)</li>
<li><strong>Closed circle (●)</strong> for ≤ and ≥ (including the value)</li>
<li><strong>Arrow or line</strong> showing the direction of all solutions</li>
</ul>
<div class="worked-example concept-box">
<p><strong>Show on a number line: x ≥ 3</strong></p>
<p>Draw a closed circle at 3 and a line to the right.</p>
</div>
<div class="worked-example concept-box">
<p><strong>Show on a number line: x < 2</strong></p>
<p>Draw an open circle at 2 and a line to the left.</p>
</div>
</div>"""
    },
    {
        "title": "Real-world inequalities",
        "body": """<div class="concept-box">
<p>Inequalities describe real situations where there's a range of acceptable values.</p>
<div class="worked-example concept-box">
<p><strong>A cinema allows children under 12. Write an inequality for age.</strong></p>
<p>\\(a < 12\\) (where a is the age in years)</p>
</div>
<div class="worked-example concept-box">
<p><strong>A theme park ride requires a height of at least 1.4 m. Write an inequality.</strong></p>
<p>\\(h \\geq 1.4\\) (where h is height in metres)</p>
</div>
<div class="worked-example concept-box">
<p><strong>The cost of a ticket is no more than £25. Write an inequality.</strong></p>
<p>\\(c \\leq 25\\) (where c is cost in pounds)</p>
</div>
<p class="success-box formula-box">
<strong>Tip:</strong> Translate carefully — "at least" means ≥, "at most" means ≤, "under" means &lt;, "over" means &gt;.
</p>
</div>"""
    }
]
