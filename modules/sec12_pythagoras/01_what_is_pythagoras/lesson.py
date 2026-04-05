TITLE = "What Is Pythagoras' Theorem?"

SECTIONS = [
    {
        "title": "Right-Angled Triangles",
        "body": """<div class='concept-box'>
<p>A <strong>right-angled triangle</strong> is a triangle with one angle exactly equal to <strong>90 degrees</strong>. This is the corner you see in a perfect square or rectangle.</p>
<p>The right angle is often marked with a small square in the corner.</p>
</div>

<h3>The Three Sides of a Right Triangle</h3>

<svg width="400" height="300" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Triangle -->
  <polygon points="50,250 50,50 350,250" fill='none' stroke='currentColor' stroke-width="3"/>

  <!-- Right angle marker -->
  <rect x="50" y="200" width="50" height="50" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- Labels -->
  <text x="25" y="160" font-size='18' font-weight='bold' fill='currentColor'>a</text>
  <text x="200" y="280" font-size='18' font-weight='bold' fill='currentColor'>b</text>
  <text x="210" y="140" font-size='18' font-weight='bold' fill='#58a6ff'>c (hypotenuse)</text>

  <!-- Vertex labels -->
  <text x="30" y="50" font-size='16' fill='currentColor'>A</text>
  <text x="30" y="270" font-size='16' fill='currentColor'>C (right angle)</text>
  <text x="350" y="270" font-size='16' fill='currentColor'>B</text>
</svg>

<div class='info-box'>
<p><strong>The three sides:</strong></p>
<ul>
<li><strong>Side a:</strong> One of the shorter sides (a "leg")</li>
<li><strong>Side b:</strong> The other shorter side (a "leg")</li>
<li><strong>Side c:</strong> The longest side, always opposite the right angle - called the <strong>hypotenuse</strong></li>
</ul>
</div>

<p>The <strong>hypotenuse is ALWAYS the longest side</strong> in a right-angled triangle. Always!</p>
"""
    },
    {
        "title": "The Pythagorean Theorem Statement",
        "body": """<div class='success-box'>
<h3>Pythagoras' Theorem</h3>
<p>In a right-angled triangle: \\(a^2 + b^2 = c^2\\)</p>
<p>Where a and b are the two shorter sides, and c is the hypotenuse.</p>
</div>

<p>This means: <strong>The square of the hypotenuse equals the sum of the squares of the other two sides.</strong></p>

<h3>What Does This Actually Mean?</h3>

<p>Imagine you built three <strong>actual squares</strong> - one on each side of the triangle:</p>

<svg width="500" height="420" viewBox="0 0 500 420" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- 3-4-5 right triangle scaled: a=90 (vert), b=120 (horiz), c=150 (hyp) -->
  <!-- Triangle vertices: C=(170,230) A=(170,140) B=(290,230) -->
  <polygon points="170,230 170,140 290,230" fill='rgba(88,166,255,0.1)' stroke='currentColor' stroke-width="2"/>

  <!-- Right angle marker at C -->
  <polyline points="170,215 185,215 185,230" fill='none' stroke='currentColor' stroke-width="1.5"/>

  <!-- Square on side a (vertical, left of triangle): 90×90 -->
  <rect x="80" y="140" width="90" height="90" fill='rgba(121,192,255,0.12)' stroke='#79c0ff' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="125" y="192" font-size='16' font-weight='bold' fill='#79c0ff' text-anchor='middle'>a² = 9</text>

  <!-- Square on side b (horizontal, below triangle): 120×120 -->
  <rect x="170" y="230" width="120" height="120" fill='rgba(121,192,255,0.12)' stroke='#79c0ff' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="230" y="298" font-size='16' font-weight='bold' fill='#79c0ff' text-anchor='middle'>b² = 16</text>

  <!-- Square on side c (hypotenuse): 150×150 rotated along hypotenuse -->
  <!-- Hyp from A=(170,140) to B=(290,230), direction=(120,90), perp=(-90,120)/150*150=(-90,120) -->
  <!-- Corners: A=(170,140), A+perp=(80,260), B+perp=(200,350), B=(290,230) -->
  <!-- But this overlaps b² square. Place on the outside (upper-right): perp=(90,-120) -->
  <!-- Corners: A=(170,140), B=(290,230), B+perp=(380,110), A+perp=(260,20) -->
  <polygon points="170,140 290,230 380,110 260,20" fill='rgba(88,166,255,0.12)' stroke='#58a6ff' stroke-width="2"/>
  <text x="275" y="130" font-size='18' font-weight='bold' fill='#58a6ff' text-anchor='middle'>c² = 25</text>

  <!-- Side labels -->
  <text x="148" y="192" font-size='14' font-weight='bold' fill='currentColor'>a=3</text>
  <text x="218" y="225" font-size='14' font-weight='bold' fill='currentColor'>b=4</text>
  <text x="240" y="172" font-size='14' font-weight='bold' fill='#58a6ff'>c=5</text>

  <!-- Equation at bottom -->
  <text x="250" y="395" font-size='16' font-weight='bold' fill='#56d364' text-anchor='middle'>9 + 16 = 25  ✓</text>
</svg>

<p><strong>The magic:</strong> If you take the area of the square on side a (a²) and add it to the area of the square on side b (b²), you get exactly the area of the square on the hypotenuse (c²)!</p>

<p>In other words: The two smaller squares fit perfectly into the larger square.</p>
"""
    },
    {
        "title": "Why Is It True? The Area Proof",
        "body": """<h3>A Proof by Rearranging Areas</h3>

<p>Imagine a large square with side length (a + b). We can calculate its area in two ways:</p>

<svg width="450" height="450" viewBox="0 0 450 450" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Classic proof: large (a+b)² square with 4 congruent right triangles, inner tilted c² square -->
  <!-- Using a=100, b=200 so a+b=300. Triangle legs a=100, b=200. c²=a²+b²=50000, c≈224 -->
  <!-- Outer square from (60,40) to (360,340), side=300 -->
  <rect x="60" y="40" width="300" height="300" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- 4 congruent right triangles (legs a=100, b=200) arranged inside -->
  <!-- T1: top-left, hyp goes from (160,40) to (60,240) -->
  <polygon points="60,40 160,40 60,240" fill='#79c0ff' opacity='0.25' stroke='#79c0ff' stroke-width="1"/>
  <!-- T2: top-right, hyp goes from (160,40) to (360,140) -->
  <polygon points="160,40 360,40 360,140" fill='#79c0ff' opacity='0.25' stroke='#79c0ff' stroke-width="1"/>
  <!-- T3: bottom-right, hyp goes from (360,140) to (260,340) -->
  <polygon points="360,140 360,340 260,340" fill='#79c0ff' opacity='0.25' stroke='#79c0ff' stroke-width="1"/>
  <!-- T4: bottom-left, hyp goes from (260,340) to (60,240) -->
  <polygon points="260,340 60,340 60,240" fill='#79c0ff' opacity='0.25' stroke='#79c0ff' stroke-width="1"/>

  <!-- Inner tilted c² square: vertices at (160,40) (360,140) (260,340) (60,240) -->
  <polygon points="160,40 360,140 260,340 60,240" fill='#58a6ff' opacity='0.12' stroke='#58a6ff' stroke-width="2"/>
  <text x="210" y="200" font-size='22' font-weight='bold' fill='#58a6ff' text-anchor='middle'>c²</text>

  <!-- Dimension labels -->
  <text x="100" y="30" font-size='14' fill='#79c0ff' text-anchor='middle'>a</text>
  <text x="255" y="30" font-size='14' fill='#79c0ff' text-anchor='middle'>b</text>
  <text x="45" y="140" font-size='14' fill='#79c0ff' text-anchor='middle'>b</text>
  <text x="45" y="295" font-size='14' fill='#79c0ff' text-anchor='middle'>a</text>

  <!-- Triangle labels -->
  <text x="90" y="110" font-size='12' fill='currentColor'>½ab</text>
  <text x="305" y="80" font-size='12' fill='currentColor'>½ab</text>
  <text x="325" y="290" font-size='12' fill='currentColor'>½ab</text>
  <text x="110" y="315" font-size='12' fill='currentColor'>½ab</text>

  <!-- Overall label -->
  <text x="210" y="380" font-size='15' font-weight='bold' fill='#56d364' text-anchor='middle'>(a+b)² = 4·(½ab) + c²</text>
  <text x="210" y="405" font-size='14' fill='#56d364' text-anchor='middle'>∴ a² + b² = c²</text>
</svg>

<div class='info-box'>
<p><strong>Method 1:</strong> Direct calculation</p>
<p>Area of large square = (a + b)² = a² + 2ab + b²</p>

<p><strong>Method 2:</strong> Count the pieces inside</p>
<p>The large square contains:</p>
<ul>
<li>4 right triangles (each with area ab/2)</li>
<li>1 square in the middle (area = c²)</li>
</ul>
<p>Total = 4(ab/2) + c² = 2ab + c²</p>

<p><strong>Both methods must give the same answer:</strong></p>
<p>a² + 2ab + b² = 2ab + c²</p>
<p>Remove 2ab from both sides:</p>
<p>a² + b² = c²  ✓</p>
</div>

<p>This proves that Pythagoras' Theorem is always true!</p>
"""
    },
    {
        "title": "The Converse: Checking for Right Angles",
        "body": """<div class='success-box'>
<p><strong>The Converse of Pythagoras' Theorem:</strong></p>
<p>If three sides of a triangle satisfy a² + b² = c² (where c is the longest side), then the triangle IS right-angled.</p>
</div>

<p>This is incredibly useful! We can check if an angle is a right angle just by checking the side lengths.</p>

<h3>Example: Is This Triangle Right-Angled?</h3>

<p><strong>Triangle with sides: 5 cm, 12 cm, 13 cm</strong></p>

<div class='example-box'>
<p>Check: Does 5² + 12² = 13²?</p>
<p>5² + 12² = 25 + 144 = 169</p>
<p>13² = 169</p>
<p><strong>YES! They match, so this IS a right-angled triangle!</strong></p>
</div>

<h3>Counter-Example: What If They Don't Match?</h3>

<p><strong>Triangle with sides: 3 cm, 4 cm, 6 cm</strong></p>

<div class='example-box'>
<p>Check: Does 3² + 4² = 6²?</p>
<p>3² + 4² = 9 + 16 = 25</p>
<p>6² = 36</p>
<p><strong>NO! 25 ≠ 36, so this is NOT a right-angled triangle.</strong></p>
</div>

<div class='info-box'>
<p><strong>Three Possibilities:</strong></p>
<ul>
<li>If a² + b² = c²: The triangle is <strong>RIGHT-ANGLED</strong></li>
<li>If a² + b² < c²: The triangle is <strong>OBTUSE-ANGLED</strong> (one angle > 90°)</li>
<li>If a² + b² > c²: The triangle is <strong>ACUTE-ANGLED</strong> (all angles < 90°)</li>
</ul>
</div>
"""
    }
]
