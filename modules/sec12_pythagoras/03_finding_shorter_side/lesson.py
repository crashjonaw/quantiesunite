TITLE = "Finding a Shorter Side"

SECTIONS = [
    {
        "title": "Rearranging the Formula",
        "body": """<div class='concept-box'>
<p>When we know the <strong>hypotenuse</strong> and <strong>one shorter side</strong>, we can find the <strong>other shorter side</strong>.</p>
<p>We rearrange Pythagoras' Theorem to solve for the missing shorter side.</p>
</div>

<h3>Starting with the Standard Formula</h3>

<p>The standard formula is: \\(a^2 + b^2 = c^2\\)</p>

<p>If we know c and b, but need to find a, we rearrange:</p>

<p>$$a^2 = c^2 - b^2$$</p>

<p>Then take the square root:</p>

<p>$$a = \\sqrt{c^2 - b^2}$$</p>

<div class='info-box'>
<p><strong>The Key Difference:</strong></p>
<ul>
<li><strong>Finding hypotenuse:</strong> \\(c = \\sqrt{a^2 + b^2}\\) (ADD the squares)</li>
<li><strong>Finding shorter side:</strong> \\(a = \\sqrt{c^2 - b^2}\\) (SUBTRACT the squares)</li>
</ul>
</div>

<svg width="500" height="300" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle: 3-4-5 right triangle, a=3*40=120, b=4*40=160, c=5*40=200 -->
  <polygon points="80,250 80,130 240,250" fill='rgba(88, 166, 255, 0.1)' stroke='#e6edf3' stroke-width="2"/>

  <!-- Right angle -->
  <rect x="80" y="210" width="40" height="40" fill='none' stroke='#e6edf3' stroke-width="1"/>

  <!-- Known sides -->
  <text x="40" y="170" font-size='20' font-weight='bold' fill='#79c0ff'>a = ?</text>
  <text x="200" y="280" font-size='20' font-weight='bold' fill='#79c0ff'>b = 4</text>
  <text x="200" y="140" font-size='20' font-weight='bold' fill='#58a6ff'>c = 5</text>

  <!-- Formula steps -->
  <text x="20" y="30" font-size='14' fill='#e6edf3' font-family='monospace'>a² + b² = c²</text>
  <text x="20" y="50" font-size='14' fill='#e6edf3' font-family='monospace'>a² + 4² = 5²</text>
  <text x="20" y="70" font-size='14' fill='#e6edf3' font-family='monospace'>a² = 5² - 4² = 25 - 16</text>
</svg>
"""
    },
    {
        "title": "Example 1: The 5-12-13 Triple",
        "body": """<h3>Finding the Missing Shorter Side</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with hypotenuse 13 cm and one leg 5 cm</p>
<p><strong>Find:</strong> The other leg</p>

<p><strong>Solution:</strong></p>
<p>Step 1: Write the rearranged formula</p>
<p>$$a^2 = c^2 - b^2$$</p>

<p>Step 2: Identify what we know</p>
<ul>
<li>c = 13 (hypotenuse)</li>
<li>b = 5 (one leg)</li>
<li>a = ? (the other leg)</li>
</ul>

<p>Step 3: Substitute the values</p>
<p>$$a^2 = 13^2 - 5^2$$</p>

<p>Step 4: Calculate the squares</p>
<p>$$a^2 = 169 - 25$$</p>

<p>Step 5: Subtract</p>
<p>$$a^2 = 144$$</p>

<p>Step 6: Take the square root</p>
<p>$$a = \\sqrt{144} = 12 \\text{ cm}$$</p>

<p><strong>Answer: The other leg is 12 cm</strong></p>

<p><em>Notice: This is the famous 5-12-13 Pythagorean triple!</em></p>
</div>

<svg width="400" height="250" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle: 5-12-13 right triangle, a=5*10=50, b=12*10=120, c=13*10=130 -->
  <polygon points="60,200 60,150 180,200" fill='rgba(88, 166, 255, 0.1)' stroke='#e6edf3' stroke-width="3"/>

  <!-- Right angle -->
  <rect x="60" y="160" width="40" height="40" fill='none' stroke='#e6edf3' stroke-width="2"/>

  <!-- Labels -->
  <text x="30" y="175" font-size='22' font-weight='bold' fill='#79c0ff'>12</text>
  <text x="115" y="225" font-size='22' font-weight='bold' fill='#79c0ff'>5</text>
  <text x="105" y="135" font-size='22' font-weight='bold' fill='#58a6ff'>13</text>
</svg>
"""
    },
    {
        "title": "Example 2: Decimal Answers",
        "body": """<h3>A Triangle with Hypotenuse 10 cm and One Leg 7 cm</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with hypotenuse 10 cm and one leg 7 cm</p>
<p><strong>Find:</strong> The other leg (to 1 decimal place)</p>

<p><strong>Solution:</strong></p>
<p>Step 1: Write the rearranged formula</p>
<p>$$a^2 = c^2 - b^2$$</p>

<p>Step 2: Substitute values</p>
<p>$$a^2 = 10^2 - 7^2$$</p>

<p>Step 3: Calculate squares</p>
<p>$$a^2 = 100 - 49$$</p>

<p>Step 4: Subtract</p>
<p>$$a^2 = 51$$</p>

<p>Step 5: Take the square root (use a calculator)</p>
<p>$$a = \\sqrt{51} \\approx 7.141...$$</p>

<p>Step 6: Round to 1 decimal place</p>
<p>$$a \\approx 7.1 \\text{ cm}$$</p>

<p><strong>Answer: The other leg is approximately 7.1 cm</strong></p>
</div>

<div class='info-box'>
<p><strong>Sanity Check:</strong></p>
<p>The hypotenuse (10 cm) must be longer than any of the shorter sides (7 cm and 7.1 cm). ✓</p>
<p>7² + 7.1² ≈ 49 + 50.41 ≈ 99.41 ≈ 100 = 10². ✓</p>
</div>
"""
    },
    {
        "title": "The 3-4-5 Triple in Reverse",
        "body": """<h3>A Triangle with Hypotenuse 5 cm and One Leg 3 cm</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with hypotenuse 5 cm and one leg 3 cm</p>
<p><strong>Find:</strong> The other leg</p>

<p><strong>Solution:</strong></p>
<p>$$a^2 = 5^2 - 3^2$$</p>
<p>$$a^2 = 25 - 9$$</p>
<p>$$a^2 = 16$$</p>
<p>$$a = \\sqrt{16} = 4 \\text{ cm}$$</p>

<p><strong>Answer: The other leg is 4 cm</strong></p>

<p><em>This is the 3-4-5 triple!</em></p>
</div>

<h3>Other Common Triples (In Reverse)</h3>

<p>You can use the 5-12-13, 8-15-17, and other triples in either direction:</p>

<div class='info-box'>
<p><strong>6-8-10 triangle:</strong></p>
<ul>
<li>If you know legs are 6 and 8, hypotenuse = 10</li>
<li>If you know hypotenuse is 10 and one leg is 6, other leg = 8</li>
<li>If you know hypotenuse is 10 and one leg is 8, other leg = 6</li>
</ul>
</div>

<p><strong>Multiples of Common Triples:</strong></p>
<ul>
<li>3-4-5 and all its multiples (6-8-10, 9-12-15, 12-16-20, etc.)</li>
<li>5-12-13 and all its multiples (10-24-26, 15-36-39, etc.)</li>
<li>8-15-17 and all its multiples (16-30-34, etc.)</li>
<li>7-24-25 and all its multiples (14-48-50, etc.)</li>
</ul>

<svg width="400" height="250" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle: 3-4-5 right triangle, a=4*30=120, b=3*30=90, c=5*30=150 -->
  <polygon points="80,200 80,80 170,200" fill='rgba(88, 166, 255, 0.1)' stroke='#e6edf3' stroke-width="3"/>

  <!-- Right angle -->
  <rect x="80" y="160" width="40" height="40" fill='none' stroke='#e6edf3' stroke-width="2"/>

  <!-- Labels -->
  <text x="45" y="150" font-size='20' font-weight='bold' fill='#79c0ff'>4</text>
  <text x="120" y="225" font-size='20' font-weight='bold' fill='#79c0ff'>3</text>
  <text x="115" y="120" font-size='20' font-weight='bold' fill='#58a6ff'>5</text>
</svg>
"""
    }
]
