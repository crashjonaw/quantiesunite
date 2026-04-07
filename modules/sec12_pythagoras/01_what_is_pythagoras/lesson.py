TITLE = "What Is Pythagoras' Theorem?"

SECTIONS = [
    {
        "title": "Right-Angled Triangles",
        "body": """<div class='concept-box'>
<p>A <strong>right-angled triangle</strong> is a triangle with one angle exactly equal to <strong>90 degrees</strong>. This is the corner you see in a perfect square or rectangle.</p>
<p>The right angle is often marked with a small square in the corner.</p>
</div>

<h3>The Three Sides of a Right Triangle</h3>

<svg viewBox="0 0 430 310" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="430" height="310" fill="none" rx="4"/>

  <!-- Triangle: C=(65,255) A=(65,55) B=(365,255) -->
  <polygon points="65,255 65,55 365,255" fill="none" stroke="currentColor" stroke-width="3"/>

  <!-- Right angle marker at C using polyline -->
  <polyline points="65,225 95,225 95,255" fill="none" stroke="currentColor" stroke-width="2"/>

  <!-- Side labels -->
  <text x="35" y="165" font-size="18" font-weight="bold" fill="currentColor" font-family="sans-serif">a</text>
  <text x="210" y="285" font-size="18" font-weight="bold" fill="currentColor" font-family="sans-serif">b</text>
  <text x="230" y="135" font-size="18" font-weight="bold" fill="#58a6ff" font-family="sans-serif">c (hypotenuse)</text>

  <!-- Vertex labels -->
  <text x="50" y="42" font-size="16" fill="currentColor" font-family="sans-serif">A</text>
  <text x="50" y="298" font-size="14" fill="currentColor" font-family="sans-serif">C (right angle)</text>
  <text x="370" y="272" font-size="16" fill="currentColor" font-family="sans-serif">B</text>
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

<svg viewBox="0 0 500 420" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="500" height="420" fill="none" rx="4"/>

  <!-- 3-4-5 right triangle scaled: a=90 (vert), b=120 (horiz), c=150 (hyp) -->
  <!-- Triangle vertices: C=(170,230) A=(170,140) B=(290,230) -->
  <polygon points="170,230 170,140 290,230" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="2"/>

  <!-- Right angle marker at C -->
  <polyline points="170,215 185,215 185,230" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <!-- Square on side a (vertical, left of triangle): 90x90 -->
  <rect x="80" y="140" width="90" height="90" fill="rgba(121,192,255,0.12)" stroke="#79c0ff" stroke-width="2" stroke-dasharray="5,5" rx="4"/>
  <text x="125" y="192" font-size="16" font-weight="bold" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">a² = 9</text>

  <!-- Square on side b (horizontal, below triangle): 120x120 -->
  <rect x="170" y="230" width="120" height="120" fill="rgba(121,192,255,0.12)" stroke="#79c0ff" stroke-width="2" stroke-dasharray="5,5" rx="4"/>
  <text x="230" y="298" font-size="16" font-weight="bold" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">b² = 16</text>

  <!-- Square on side c (hypotenuse): rotated along hypotenuse -->
  <!-- Corners: A=(170,140), B=(290,230), B+perp=(380,110), A+perp=(260,20) -->
  <polygon points="170,140 290,230 380,110 260,20" fill="rgba(88,166,255,0.12)" stroke="#58a6ff" stroke-width="2"/>
  <text x="275" y="130" font-size="18" font-weight="bold" fill="#58a6ff" text-anchor="middle" font-family="sans-serif">c² = 25</text>

  <!-- Side labels -->
  <text x="148" y="192" font-size="14" font-weight="bold" fill="currentColor" font-family="sans-serif">a=3</text>
  <text x="218" y="225" font-size="14" font-weight="bold" fill="currentColor" font-family="sans-serif">b=4</text>
  <text x="240" y="172" font-size="14" font-weight="bold" fill="#58a6ff" font-family="sans-serif">c=5</text>

  <!-- Equation at bottom -->
  <text x="250" y="395" font-size="16" font-weight="bold" fill="#56d364" text-anchor="middle" font-family="sans-serif">9 + 16 = 25  &#x2713;</text>
</svg>

<p><strong>The magic:</strong> If you take the area of the square on side a (a²) and add it to the area of the square on side b (b²), you get exactly the area of the square on the hypotenuse (c²)!</p>

<p>In other words: The two smaller squares fit perfectly into the larger square.</p>
"""
    },
    {
        "title": "Why Is It True? The Area Proof",
        "body": """<h3>A Proof by Rearranging Areas</h3>

<p>Imagine a large square with side length (a + b). We can calculate its area in two ways:</p>

<svg viewBox="0 0 450 435" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="450" height="435" fill="none" rx="4"/>

  <!-- Classic proof: large (a+b)² square with 4 congruent right triangles, inner tilted c² square -->
  <!-- Using a=100, b=200 so a+b=300. Triangle legs a=100, b=200. -->
  <!-- Outer square from (60,40) to (360,340), side=300 -->
  <rect x="60" y="40" width="300" height="300" fill="none" stroke="currentColor" stroke-width="2" rx="4"/>

  <!-- 4 congruent right triangles (legs a=100, b=200) arranged inside -->
  <!-- T1: top-left -->
  <polygon points="60,40 160,40 60,240" fill="#79c0ff" opacity="0.25" stroke="#79c0ff" stroke-width="1"/>
  <!-- T2: top-right -->
  <polygon points="160,40 360,40 360,140" fill="#79c0ff" opacity="0.25" stroke="#79c0ff" stroke-width="1"/>
  <!-- T3: bottom-right -->
  <polygon points="360,140 360,340 260,340" fill="#79c0ff" opacity="0.25" stroke="#79c0ff" stroke-width="1"/>
  <!-- T4: bottom-left -->
  <polygon points="260,340 60,340 60,240" fill="#79c0ff" opacity="0.25" stroke="#79c0ff" stroke-width="1"/>

  <!-- Inner tilted c² square: vertices at (160,40) (360,140) (260,340) (60,240) -->
  <polygon points="160,40 360,140 260,340 60,240" fill="#58a6ff" opacity="0.12" stroke="#58a6ff" stroke-width="2"/>
  <text x="210" y="200" font-size="22" font-weight="bold" fill="#58a6ff" text-anchor="middle" font-family="sans-serif">c²</text>

  <!-- Dimension labels -->
  <text x="100" y="30" font-size="14" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">a</text>
  <text x="255" y="30" font-size="14" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">b</text>
  <text x="45" y="140" font-size="14" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">b</text>
  <text x="45" y="295" font-size="14" fill="#79c0ff" text-anchor="middle" font-family="sans-serif">a</text>

  <!-- Triangle labels -->
  <text x="95" y="115" font-size="12" fill="currentColor" font-family="sans-serif">&#xBD;ab</text>
  <text x="305" y="80" font-size="12" fill="currentColor" font-family="sans-serif">&#xBD;ab</text>
  <text x="325" y="290" font-size="12" fill="currentColor" font-family="sans-serif">&#xBD;ab</text>
  <text x="115" y="315" font-size="12" fill="currentColor" font-family="sans-serif">&#xBD;ab</text>

  <!-- Overall label -->
  <text x="225" y="380" font-size="15" font-weight="bold" fill="#56d364" text-anchor="middle" font-family="sans-serif">(a+b)² = 4&#xB7;(&#xBD;ab) + c²</text>
  <text x="225" y="410" font-size="14" fill="#56d364" text-anchor="middle" font-family="sans-serif">&#x2234; a² + b² = c²</text>
</svg>

<div class='info-box'>
<p><strong>Method 1:</strong> Direct calculation</p>
<p>Area of large square = \((a + b)^2 = a^2 + 2ab + b^2\)</p>

<p><strong>Method 2:</strong> Count the pieces inside</p>
<p>The large square contains:</p>
<ul>
<li>4 right triangles (each with area \(ab/2\))</li>
<li>1 square in the middle (area = \(c^2\))</li>
</ul>
<p>Total = \(4(ab/2) + c^2 = 2ab + c^2\)</p>

<p><strong>Both methods must give the same answer:</strong></p>
<p>\(a^2 + 2ab + b^2 = 2ab + c^2\)</p>
<p>Remove \(2ab\) from both sides:</p>
<p>\(a^2 + b^2 = c^2\) &#x2713;</p>
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
<p>Check: Does \(5^2 + 12^2 = 13^2\)?</p>
<p>\(5^2 + 12^2 = 25 + 144 = 169\)</p>
<p>\(13^2 = 169\)</p>
<p><strong>YES! They match, so this IS a right-angled triangle!</strong></p>
</div>

<h3>Counter-Example: What If They Don't Match?</h3>

<p><strong>Triangle with sides: 3 cm, 4 cm, 6 cm</strong></p>

<div class='example-box'>
<p>Check: Does \(3^2 + 4^2 = 6^2\)?</p>
<p>\(3^2 + 4^2 = 9 + 16 = 25\)</p>
<p>\(6^2 = 36\)</p>
<p><strong>NO! \(25 \neq 36\), so this is NOT a right-angled triangle.</strong></p>
</div>

<div class='info-box'>
<p><strong>Three Possibilities:</strong></p>
<ul>
<li>If \(a^2 + b^2 = c^2\): The triangle is <strong>RIGHT-ANGLED</strong></li>
<li>If \(a^2 + b^2 < c^2\): The triangle is <strong>OBTUSE-ANGLED</strong> (one angle > 90°)</li>
<li>If \(a^2 + b^2 > c^2\): The triangle is <strong>ACUTE-ANGLED</strong> (all angles < 90°)</li>
</ul>
</div>
"""
    }
]
