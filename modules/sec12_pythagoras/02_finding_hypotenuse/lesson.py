TITLE = "Finding the Hypotenuse"

SECTIONS = [
    {
        "title": "The Formula: From a² + b² = c² to c = √(a² + b²)",
        "body": """<div class='concept-box'>
<p>When we know the two shorter sides (a and b) of a right-angled triangle, we can find the hypotenuse using Pythagoras' Theorem.</p>
<p>Starting with: \\(a^2 + b^2 = c^2\\)</p>
<p>We take the square root of both sides: \\(c = \\sqrt{a^2 + b^2}\\)</p>
</div>

<h3>Understanding the Process</h3>

<svg width="500" height="300" viewBox="0 0 500 300" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- 3-4-5 triangle: C=(150,250) A=(150,100) B=(350,250) -->
  <!-- a (vert)=150px, b (horiz)=200px, c (hyp)=250px — proportional to 3:4:5 -->
  <polygon points="150,250 150,100 350,250" fill='rgba(88,166,255,0.1)' stroke='currentColor' stroke-width="2"/>

  <!-- Right angle marker at C=(150,250), small 20px square -->
  <polyline points="150,230 170,230 170,250" fill='none' stroke='currentColor' stroke-width="1.5"/>

  <!-- Side labels -->
  <text x="118" y="185" font-size='18' font-weight='bold' fill='#79c0ff'>a = 3</text>
  <text x="225" y="275" font-size='18' font-weight='bold' fill='#79c0ff'>b = 4</text>
  <text x="260" y="160" font-size='18' font-weight='bold' fill='#58a6ff'>c = ?</text>

  <!-- Calculation steps on the right -->
  <text x="370" y="110" font-size='14' fill='currentColor' font-family='monospace'>c² = a² + b²</text>
  <text x="370" y="135" font-size='14' fill='currentColor' font-family='monospace'>c² = 9 + 16</text>
  <text x="370" y="160" font-size='14' fill='currentColor' font-family='monospace'>c² = 25</text>
  <text x="370" y="185" font-size='14' fill='#56d364' font-family='monospace'>c = 5 ✓</text>
</svg>

<div class='success-box'>
<p><strong>The Step-by-Step Process:</strong></p>
<ol>
<li>Write the formula: \\(c^2 = a^2 + b^2\\)</li>
<li>Substitute the known values for a and b</li>
<li>Calculate a² and b²</li>
<li>Add them together</li>
<li>Take the square root to find c</li>
</ol>
</div>
"""
    },
    {
        "title": "Example 1: Whole Number Answers (Pythagorean Triples)",
        "body": """<h3>A Triangle with Sides 3 cm and 4 cm</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with a = 3 cm, b = 4 cm</p>
<p><strong>Find:</strong> The hypotenuse c</p>

<p><strong>Solution:</strong></p>
<p>Step 1: Write the formula</p>
<p>$$c^2 = a^2 + b^2$$</p>

<p>Step 2: Substitute a = 3 and b = 4</p>
<p>$$c^2 = 3^2 + 4^2$$</p>

<p>Step 3: Calculate squares</p>
<p>$$c^2 = 9 + 16$$</p>

<p>Step 4: Add</p>
<p>$$c^2 = 25$$</p>

<p>Step 5: Take the square root</p>
<p>$$c = \\sqrt{25} = 5 \\text{ cm}$$</p>

<p><strong>Answer: The hypotenuse is 5 cm</strong></p>

<p><em>Notice: 3-4-5 is a famous Pythagorean triple - all whole numbers!</em></p>
</div>

<svg width="400" height="250" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle: 3-4-5, a=3*40=120, b=4*40=160, c=5*40=200 -->
  <polygon points="60,200 60,80 220,200" fill='rgba(88, 166, 255, 0.1)' stroke='currentColor' stroke-width="3"/>

  <!-- Right angle marker -->
  <rect x="60" y="160" width="40" height="40" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- Labels -->
  <text x="35" y="145" font-size='22' font-weight='bold' fill='#79c0ff'>3</text>
  <text x="135" y="225" font-size='22' font-weight='bold' fill='#79c0ff'>4</text>
  <text x="125" y="115" font-size='22' font-weight='bold' fill='#58a6ff'>5</text>
</svg>
"""
    },
    {
        "title": "Example 2: Decimal Answers",
        "body": """<h3>A Triangle with Sides 5 cm and 7 cm</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with a = 5 cm, b = 7 cm</p>
<p><strong>Find:</strong> The hypotenuse c (to 1 decimal place)</p>

<p><strong>Solution:</strong></p>
<p>Step 1: Write the formula</p>
<p>$$c^2 = a^2 + b^2$$</p>

<p>Step 2: Substitute a = 5 and b = 7</p>
<p>$$c^2 = 5^2 + 7^2$$</p>

<p>Step 3: Calculate squares</p>
<p>$$c^2 = 25 + 49$$</p>

<p>Step 4: Add</p>
<p>$$c^2 = 74$$</p>

<p>Step 5: Take the square root (use a calculator)</p>
<p>$$c = \\sqrt{74} \\approx 8.602...$$</p>

<p>Round to 1 decimal place:</p>
<p>$$c \\approx 8.6 \\text{ cm}$$</p>

<p><strong>Answer: The hypotenuse is approximately 8.6 cm</strong></p>
</div>

<div class='info-box'>
<p><strong>When to Round:</strong></p>
<ul>
<li>The question tells you: "to 1 decimal place", "to nearest cm", "to 2 significant figures", etc.</li>
<li>Always check what precision is asked for</li>
<li>If no instruction is given, give your answer to 2 or 3 significant figures</li>
</ul>
</div>
"""
    },
    {
        "title": "Example 3: The Famous 5-12-13 Triple",
        "body": """<h3>A Triangle with Sides 5 cm and 12 cm</h3>

<div class='example-box'>
<p><strong>Given:</strong> Right triangle with a = 5 cm, b = 12 cm</p>
<p><strong>Find:</strong> The hypotenuse c</p>

<p><strong>Solution:</strong></p>
<p>$$c^2 = 5^2 + 12^2$$</p>
<p>$$c^2 = 25 + 144$$</p>
<p>$$c^2 = 169$$</p>
<p>$$c = \\sqrt{169} = 13 \\text{ cm}$$</p>

<p><strong>Answer: The hypotenuse is 13 cm</strong></p>

<p><em>This is the famous 5-12-13 Pythagorean triple!</em></p>
</div>

<h3>Why Is This Important?</h3>

<p>The 5-12-13 triple appears over and over in mathematics problems. If you recognize it, you don't even need a calculator!</p>

<p><strong>Related triples (multiples of 5-12-13):</strong></p>
<ul>
<li>10-24-26 (multiply by 2)</li>
<li>15-36-39 (multiply by 3)</li>
<li>20-48-52 (multiply by 4)</li>
</ul>

<p><strong>Other famous triples:</strong></p>
<ul>
<li>3-4-5</li>
<li>6-8-10 (2 × the 3-4-5 triple)</li>
<li>8-15-17</li>
<li>7-24-25</li>
</ul>

<svg width="450" height="250" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle: 5-12-13, a=5*10=50, b=12*10=120, c=13*10=130 -->
  <polygon points="80,220 80,170 200,220" fill='rgba(88, 166, 255, 0.1)' stroke='currentColor' stroke-width="3"/>

  <!-- Right angle -->
  <rect x="80" y="180" width="40" height="40" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- Labels with values -->
  <text x="50" y="190" font-size='20' font-weight='bold' fill='#79c0ff'>5</text>
  <text x="130" y="245" font-size='20' font-weight='bold' fill='#79c0ff'>12</text>
  <text x="125" y="165" font-size='20' font-weight='bold' fill='#58a6ff'>13</text>
</svg>
"""
    }
]
