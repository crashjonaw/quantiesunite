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

<svg viewBox="0 0 460 310" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="460" height="310" fill="none" rx="4"/>

  <!-- Triangle: 3-4-5 right triangle -->
  <!-- C=(80,260) A=(80,110) B=(280,260), a=150 (vert), b=200 (horiz) -->
  <polygon points="80,260 80,110 280,260" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="2"/>

  <!-- Right angle marker at C -->
  <polyline points="80,235 105,235 105,260" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <!-- Known sides -->
  <text x="25" y="195" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">a = ?</text>
  <text x="145" y="290" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">b = 4</text>
  <text x="195" y="165" font-size="18" font-weight="bold" fill="#58a6ff" font-family="sans-serif">c = 5</text>

  <!-- Formula steps -->
  <text x="310" y="80" font-size="14" fill="currentColor" font-family="monospace">a² + b² = c²</text>
  <text x="310" y="110" font-size="14" fill="currentColor" font-family="monospace">a² + 4² = 5²</text>
  <text x="310" y="140" font-size="14" fill="currentColor" font-family="monospace">a² = 25 - 16</text>
  <text x="310" y="170" font-size="14" fill="currentColor" font-family="monospace">a² = 9</text>
  <text x="310" y="200" font-size="14" fill="#56d364" font-family="monospace">a = 3 &#x2713;</text>
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

<svg viewBox="0 0 380 280" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="380" height="280" fill="none" rx="4"/>

  <!-- Triangle: 5-12-13 right triangle, proportional: a=144 (vert), b=60 (horiz) -->
  <!-- C=(60,235) A=(60,91) B=(204,235) -->
  <polygon points="60,235 60,91 204,235" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="3"/>

  <!-- Right angle marker at C -->
  <polyline points="60,210 85,210 85,235" fill="none" stroke="currentColor" stroke-width="2"/>

  <!-- Labels -->
  <text x="22" y="172" font-size="22" font-weight="bold" fill="#79c0ff" font-family="sans-serif">12</text>
  <text x="110" y="262" font-size="22" font-weight="bold" fill="#79c0ff" font-family="sans-serif">5</text>
  <text x="145" y="145" font-size="22" font-weight="bold" fill="#58a6ff" font-family="sans-serif">13</text>
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
<p>The hypotenuse (10 cm) must be longer than any of the shorter sides (7 cm and 7.1 cm). &#x2713;</p>
<p>\(7^2 + 7.1^2 \approx 49 + 50.41 \approx 99.41 \approx 100 = 10^2\). &#x2713;</p>
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

<svg viewBox="0 0 380 270" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="380" height="270" fill="none" rx="4"/>

  <!-- Triangle: 3-4-5 right triangle, a=120 (vert), b=90 (horiz) -->
  <!-- C=(70,225) A=(70,105) B=(160,225) -->
  <polygon points="70,225 70,105 160,225" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="3"/>

  <!-- Right angle marker at C -->
  <polyline points="70,200 95,200 95,225" fill="none" stroke="currentColor" stroke-width="2"/>

  <!-- Labels -->
  <text x="32" y="175" font-size="20" font-weight="bold" fill="#79c0ff" font-family="sans-serif">4</text>
  <text x="100" y="252" font-size="20" font-weight="bold" fill="#79c0ff" font-family="sans-serif">3</text>
  <text x="130" y="148" font-size="20" font-weight="bold" fill="#58a6ff" font-family="sans-serif">5</text>
</svg>
"""
    }
]
