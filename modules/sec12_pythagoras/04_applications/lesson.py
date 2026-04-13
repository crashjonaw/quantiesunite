TITLE = "Real-World Applications"

SECTIONS = [
    {
        "title": "Application 1: Finding Diagonals",
        "body": """<div class='concept-box'>
<p>Pythagoras' Theorem is perfect for finding diagonals in rectangles or distances across squares.</p>
</div>

<h3>The Diagonal of a Rectangle</h3>

<p>A rectangle's diagonal creates two right-angled triangles. We can use Pythagoras to find the diagonal length.</p>

<svg viewBox="0 0 470 370" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="470" height="370" fill="none" rx="4"/>

  <!-- Rectangle: 8m x 6m, drawn as 280 x 210 pixels -->
  <rect x="70" y="70" width="280" height="210" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="2" rx="4"/>

  <!-- Diagonal -->
  <line x1="70" y1="70" x2="350" y2="280" stroke="#58a6ff" stroke-width="3"/>

  <!-- Right angle marker at bottom-left corner -->
  <polyline points="70,255 95,255 95,280" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <!-- Labels -->
  <text x="190" y="55" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">8 m</text>
  <text x="20" y="185" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">6 m</text>
  <text x="225" y="195" font-size="18" font-weight="bold" fill="#58a6ff" font-family="sans-serif">d = ?</text>

  <!-- Dashed lines to show the triangle -->
  <line x1="70" y1="280" x2="350" y2="280" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5,5"/>
  <line x1="70" y1="70" x2="70" y2="280" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5,5"/>
</svg>

<div class='example-box'>
<p><strong>Example: Rectangle 8 m long and 6 m wide</strong></p>

<p><strong>Given:</strong> Rectangle with length 8 m and width 6 m</p>
<p><strong>Find:</strong> The length of the diagonal</p>

<p><strong>Solution:</strong></p>
<p>The diagonal is the hypotenuse of a right triangle with legs 8 m and 6 m.</p>

<p>$$c^2 = 8^2 + 6^2$$</p>
<p>$$c^2 = 64 + 36$$</p>
<p>$$c^2 = 100$$</p>
<p>$$c = \\sqrt{100} = 10 \\text{ m}$$</p>

<p><strong>Answer: The diagonal is 10 m</strong></p>

<p><em>Notice: 6-8-10 is 2 x the 3-4-5 triple!</em></p>
</div>

<h3>The Diagonal of a Square</h3>

<p>For a square with side length s, the diagonal d is:</p>

<p>$$d^2 = s^2 + s^2 = 2s^2$$</p>
<p>$$d = s\\sqrt{2}$$</p>

<p>For example, a square with side 4 cm has diagonal: \(d = 4\\sqrt{2} \\approx 5.66\) cm</p>
"""
    },
    {
        "title": "Application 2: Heights and Distances - The Ladder Problem",
        "body": """<h3>A Classic Real-World Problem</h3>

<p>A ladder leaning against a wall forms a right-angled triangle with the wall and ground.</p>

<svg viewBox="0 0 370 380" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="370" height="380" fill="none" rx="4"/>

  <!-- Wall (vertical line) -->
  <line x1="80" y1="60" x2="80" y2="310" stroke="currentColor" stroke-width="3"/>

  <!-- Ground (horizontal line) -->
  <line x1="50" y1="310" x2="310" y2="310" stroke="currentColor" stroke-width="3"/>

  <!-- Ladder: from top of wall to ground -->
  <!-- 3-4-5 triangle: base=150px (3m), height=200px (4m) -->
  <line x1="80" y1="110" x2="230" y2="310" stroke="#79c0ff" stroke-width="4"/>

  <!-- Right angle marker at wall-ground junction -->
  <polyline points="80,285 105,285 105,310" fill="none" stroke="currentColor" stroke-width="2"/>

  <!-- Distance labels -->
  <text x="140" y="345" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">3 m</text>
  <text x="25" y="220" font-size="18" font-weight="bold" fill="#79c0ff" font-family="sans-serif">4 m</text>
  <text x="175" y="195" font-size="18" font-weight="bold" fill="#58a6ff" font-family="sans-serif">5 m</text>

  <!-- Ground and wall labels -->
  <text x="85" y="75" font-size="14" fill="currentColor" font-family="sans-serif">Wall</text>
  <text x="255" y="305" font-size="14" fill="currentColor" font-family="sans-serif">Ground</text>

  <!-- Small circles at ladder endpoints -->
  <circle cx="80" cy="110" r="4" fill="#79c0ff"/>
  <circle cx="230" cy="310" r="4" fill="#79c0ff"/>
</svg>

<div class='example-box'>
<p><strong>Problem:</strong> A 5-metre ladder rests against a wall. The base of the ladder is 3 metres from the wall. How high up the wall does it reach?</p>

<p><strong>Solution:</strong></p>
<p>The ladder, wall, and ground form a right-angled triangle:</p>
<ul>
<li>Hypotenuse (ladder) = 5 m</li>
<li>Base (distance from wall) = 3 m</li>
<li>Height (how far up the wall) = ?</li>
</ul>

<p>Use: $$a^2 + b^2 = c^2$$</p>

<p>$$3^2 + \\text{height}^2 = 5^2$$</p>
<p>$$9 + \\text{height}^2 = 25$$</p>
<p>$$\\text{height}^2 = 25 - 9 = 16$$</p>
<p>$$\\text{height} = \\sqrt{16} = 4 \\text{ m}$$</p>

<p><strong>Answer: The ladder reaches 4 metres up the wall</strong></p>

<p><em>This is the famous 3-4-5 Pythagorean triple!</em></p>
</div>

<div class='info-box'>
<p><strong>Real-World Safety Note:</strong></p>
<p>In real life, ladders should be placed so the base is about \(\\frac{1}{4}\) of the ladder's length away from the wall. For a 5 m ladder, that would be about 1.25 m away.</p>
</div>
"""
    },
    {
        "title": "Application 3: Distances on a Map or Grid",
        "body": """<h3>Finding Straight-Line Distances Between Two Points</h3>

<p>If two places are separated by a north-south distance and an east-west distance, the straight-line distance between them forms the hypotenuse of a right triangle.</p>

<div class='example-box'>
<p><strong>Problem:</strong> Two towns are:</p>
<ul>
<li>7 km apart north-south</li>
<li>24 km apart east-west</li>
</ul>
<p>What is the straight-line distance between them?</p>

<p><strong>Solution:</strong></p>
<p>The distances form the two legs of a right triangle. The straight-line distance is the hypotenuse.</p>

<p>$$c^2 = 7^2 + 24^2$$</p>
<p>$$c^2 = 49 + 576$$</p>
<p>$$c^2 = 625$$</p>
<p>$$c = \\sqrt{625} = 25 \\text{ km}$$</p>

<p><strong>Answer: The straight-line distance is 25 km</strong></p>

<p><em>Notice: 7-24-25 is a famous Pythagorean triple!</em></p>
</div>

<svg viewBox="0 0 430 370" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="430" height="370" fill="none" rx="4"/>

  <!-- Grid lines -->
  <line x1="60" y1="60" x2="380" y2="60" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="60" y1="110" x2="380" y2="110" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="60" y1="160" x2="380" y2="160" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="60" y1="210" x2="380" y2="210" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="60" y1="260" x2="380" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>

  <line x1="60" y1="60" x2="60" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="140" y1="60" x2="140" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="220" y1="60" x2="220" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="300" y1="60" x2="300" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>
  <line x1="380" y1="60" x2="380" y2="260" stroke="currentColor" stroke-width="1" opacity="0.2"/>

  <!-- Town A at top-left -->
  <circle cx="80" cy="80" r="8" fill="#79c0ff"/>
  <text x="95" y="75" font-size="14" fill="currentColor" font-family="sans-serif">Town A</text>

  <!-- Town B: 7 km south (70px), 24 km east (240px) -->
  <circle cx="320" cy="150" r="8" fill="#79c0ff"/>
  <text x="330" y="145" font-size="14" fill="currentColor" font-family="sans-serif">Town B</text>

  <!-- North-South distance (vertical) -->
  <line x1="55" y1="80" x2="55" y2="150" stroke="#79c0ff" stroke-width="2"/>
  <text x="15" y="122" font-size="14" fill="#79c0ff" font-family="sans-serif">7 km</text>

  <!-- East-West distance (horizontal) -->
  <line x1="80" y1="165" x2="320" y2="165" stroke="#79c0ff" stroke-width="2"/>
  <text x="175" y="190" font-size="14" fill="#79c0ff" font-family="sans-serif">24 km</text>

  <!-- Straight-line distance (hypotenuse) -->
  <line x1="80" y1="80" x2="320" y2="150" stroke="#58a6ff" stroke-width="3"/>
  <text x="175" y="95" font-size="16" font-weight="bold" fill="#58a6ff" font-family="sans-serif">25 km</text>

  <!-- Right angle marker at the corner -->
  <polyline points="80,140 95,140 95,155" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <!-- Compass indicator -->
  <text x="390" y="80" font-size="12" fill="currentColor" font-family="sans-serif">N</text>
  <text x="390" y="250" font-size="12" fill="currentColor" font-family="sans-serif">S</text>
  <line x1="396" y1="85" x2="396" y2="240" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <polygon points="396,85 391,95 401,95" fill="currentColor" opacity="0.4"/>
</svg>
"""
    },
    {
        "title": "Application 4: 3D Problems - Space Diagonals",
        "body": """<h3>Finding Distances Inside 3D Shapes</h3>

<p>Pythagoras' Theorem isn't just for 2D! We can use it to find distances through 3D objects like boxes (cuboids).</p>

<div class='example-box'>
<p><strong>Problem:</strong> A rectangular box (cuboid) has dimensions:</p>
<ul>
<li>Length = 3 m</li>
<li>Width = 4 m</li>
<li>Height = 12 m</li>
</ul>
<p>Find the space diagonal (the distance from one corner to the diagonally opposite corner through the interior).</p>

<p><strong>Solution - Step 1: Find the diagonal of the base</strong></p>
<p>The base is a 3 m x 4 m rectangle. Its diagonal is:</p>
<p>$$d_{\\text{base}}^2 = 3^2 + 4^2 = 9 + 16 = 25$$</p>
<p>$$d_{\\text{base}} = 5 \\text{ m}$$</p>

<p><strong>Solution - Step 2: Use the height and base diagonal</strong></p>
<p>The base diagonal and height form a new right triangle. The space diagonal is:</p>
<p>$$d_{\\text{space}}^2 = 5^2 + 12^2 = 25 + 144 = 169$$</p>
<p>$$d_{\\text{space}} = \\sqrt{169} = 13 \\text{ m}$$</p>

<p><strong>Answer: The space diagonal is 13 m</strong></p>

<p><em>Notice: We used both the 3-4-5 triple and the 5-12-13 triple!</em></p>
</div>

<svg viewBox="0 0 460 380" class="formula-box" style="display: block; margin: 20px auto;">
  <rect x="0" y="0" width="460" height="380" fill="none" rx="4"/>

  <!-- 3D box representation using isometric-like projection -->
  <!-- Front face: bottom-left at (80,280), 200px wide, 160px tall -->
  <rect x="80" y="120" width="200" height="160" fill="none" stroke="currentColor" stroke-width="2"/>

  <!-- Top face (perspective) -->
  <polygon points="80,120 130,75 330,75 280,120" fill="rgba(88,166,255,0.1)" stroke="currentColor" stroke-width="2"/>

  <!-- Right face (perspective) -->
  <polygon points="280,120 330,75 330,235 280,280" fill="rgba(88,166,255,0.05)" stroke="currentColor" stroke-width="2"/>

  <!-- Base diagonal (dashed) -->
  <line x1="80" y1="280" x2="280" y2="120" stroke="#79c0ff" stroke-width="2" stroke-dasharray="6,4"/>

  <!-- Space diagonal (bold, from front-bottom-left to back-top-right) -->
  <line x1="80" y1="280" x2="330" y2="75" stroke="#58a6ff" stroke-width="3"/>

  <!-- Height line -->
  <line x1="280" y1="280" x2="330" y2="235" stroke="#79c0ff" stroke-width="2"/>

  <!-- Dimension labels -->
  <text x="140" y="310" font-size="14" fill="#79c0ff" font-family="sans-serif">3 m (length)</text>
  <text x="295" y="270" font-size="14" fill="#79c0ff" font-family="sans-serif">4 m</text>
  <text x="345" y="165" font-size="14" fill="#79c0ff" font-family="sans-serif">12 m</text>
  <text x="180" y="165" font-size="15" font-weight="bold" fill="#58a6ff" font-family="sans-serif">13 m</text>
  <text x="170" y="185" font-size="12" fill="#58a6ff" font-family="sans-serif">(space diagonal)</text>

  <!-- Small dot at endpoints of space diagonal -->
  <circle cx="80" cy="280" r="4" fill="#58a6ff"/>
  <circle cx="330" cy="75" r="4" fill="#58a6ff"/>
</svg>

<div class='info-box'>
<p><strong>General Formula for Space Diagonal:</strong></p>
<p>For a box with dimensions length (l), width (w), and height (h):</p>
<p>$$d = \\sqrt{l^2 + w^2 + h^2}$$</p>
<p>This is like Pythagoras' Theorem extended to 3D!</p>
</div>
"""
    }
]
