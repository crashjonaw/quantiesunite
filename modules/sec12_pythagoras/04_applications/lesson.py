TITLE = "Real-World Applications"

SECTIONS = [
    {
        "title": "Application 1: Finding Diagonals",
        "body": """<div class='concept-box'>
<p>Pythagoras' Theorem is perfect for finding diagonals in rectangles or distances across squares.</p>
</div>

<h3>The Diagonal of a Rectangle</h3>

<p>A rectangle's diagonal creates two right-angled triangles. We can use Pythagoras to find the diagonal length.</p>

<svg width="500" height="350" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Rectangle: 8m x 6m, drawn as 320 x 240 pixels (40px per unit) -->
  <rect x="80" y="80" width="320" height="240" fill='rgba(88, 166, 255, 0.1)' stroke='currentColor' stroke-width="2"/>

  <!-- Diagonal -->
  <line x1="80" y1="80" x2="400" y2="320" stroke='#58a6ff' stroke-width="3"/>

  <!-- Right angle marker -->
  <rect x="80" y="280" width="40" height="40" fill='none' stroke='currentColor' stroke-width="1"/>

  <!-- Labels -->
  <text x="220" y="70" font-size='18' font-weight='bold' fill='#79c0ff'>8 m</text>
  <text x="20" y="220" font-size='18' font-weight='bold' fill='#79c0ff'>6 m</text>
  <text x="240" y="210" font-size='18' font-weight='bold' fill='#58a6ff'>?</text>
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

<p><em>Notice: 6-8-10 is 2 × the 3-4-5 triple!</em></p>
</div>

<h3>The Diagonal of a Square</h3>

<p>For a square with side length s, the diagonal d is:</p>

<p>$$d^2 = s^2 + s^2 = 2s^2$$</p>
<p>$$d = s\\sqrt{2}$$</p>

<p>For example, a square with side 4 cm has diagonal: d = 4√2 ≈ 5.66 cm</p>
"""
    },
    {
        "title": "Application 2: Heights and Distances - The Ladder Problem",
        "body": """<h3>A Classic Real-World Problem</h3>

<p>A ladder leaning against a wall forms a right-angled triangle with the wall and ground.</p>

<svg width="450" height="400" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Ground -->
  <line x1="50" y1="300" x2="200" y2="300" stroke='currentColor' stroke-width="3"/>

  <!-- Wall -->
  <line x1="100" y1="300" x2="100" y2="100" stroke='currentColor' stroke-width="3"/>

  <!-- Ladder: 3-4-5 triangle, 3m horizontal=150px, 4m vertical=200px, 5m hypotenuse=250px -->
  <line x1="100" y1="100" x2="250" y2="300" stroke='#79c0ff' stroke-width="4"/>

  <!-- Right angle -->
  <rect x="100" y="260" width="40" height="40" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- Distance labels -->
  <text x="150" y="350" font-size='18' font-weight='bold' fill='#79c0ff'>3 m</text>
  <text x="60" y="220" font-size='18' font-weight='bold' fill='#79c0ff'>4 m</text>
  <text x="145" y="200" font-size='18' font-weight='bold' fill='#58a6ff'>5 m</text>

  <!-- Ground and wall labels -->
  <text x="105" y="80" font-size='14' fill='currentColor'>Wall</text>
  <text x="350" y="320" font-size='14' fill='currentColor'>Ground</text>
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
<p>In real life, ladders should be placed so the base is about 1/4 of the ladder's length away from the wall. For a 5 m ladder, that would be about 1.25 m away.</p>
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

<svg width="500" height="400" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- Grid -->
  <line x1="100" y1="100" x2="400" y2="100" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="100" y1="150" x2="400" y2="150" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="100" y1="200" x2="400" y2="200" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="100" y1="250" x2="400" y2="250" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="100" y1="300" x2="400" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>

  <line x1="100" y1="100" x2="100" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="150" y1="100" x2="150" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="200" y1="100" x2="200" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="250" y1="100" x2="250" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="300" y1="100" x2="300" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="350" y1="100" x2="350" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>
  <line x1="400" y1="100" x2="400" y2="300" stroke='currentColor' stroke-width="1" opacity='0.3'/>

  <!-- Town A -->
  <circle cx="100" cy="100" r="8" fill='#79c0ff'/>
  <text x="105" y="95" font-size='14' fill='currentColor'>Town A</text>

  <!-- Town B: 7 km north-south (70 px), 24 km east-west (240 px) -->
  <circle cx="340" cy="170" r="8" fill='#79c0ff'/>
  <text x="270" y="190" font-size='14' fill='currentColor'>Town B</text>

  <!-- North-South distance -->
  <line x1="80" y1="100" x2="80" y2="170" stroke='#79c0ff' stroke-width="2"/>
  <text x="40" y="140" font-size='14' fill='#79c0ff'>7 km</text>

  <!-- East-West distance -->
  <line x1="100" y1="180" x2="340" y2="180" stroke='#79c0ff' stroke-width="2"/>
  <text x="200" y="205" font-size='14' fill='#79c0ff'>24 km</text>

  <!-- Straight-line distance -->
  <line x1="100" y1="100" x2="340" y2="170" stroke='#58a6ff' stroke-width="3"/>
  <text x="210" y="125" font-size='16' font-weight='bold' fill='#58a6ff'>25 km</text>
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
<p>The base is a 3 m × 4 m rectangle. Its diagonal is:</p>
<p>$$d_{\\text{base}}^2 = 3^2 + 4^2 = 9 + 16 = 25$$</p>
<p>$$d_{\\text{base}} = 5 \\text{ m}$$</p>

<p><strong>Solution - Step 2: Use the height and base diagonal</strong></p>
<p>The base diagonal and height form a new right triangle. The space diagonal is:</p>
<p>$$d_{\\text{space}}^2 = 5^2 + 12^2 = 25 + 144 = 169$$</p>
<p>$$d_{\\text{space}} = \\sqrt{169} = 13 \\text{ m}$$</p>

<p><strong>Answer: The space diagonal is 13 m</strong></p>

<p><em>Notice: We used both the 3-4-5 triple and the 5-12-13 triple!</em></p>
</div>

<svg width="500" height="380" class="formula-box" style="display: block; margin: 20px auto;">
  <!-- 3D box representation -->
  <!-- Front face -->
  <rect x="100" y="150" width="200" height="150" fill='none' stroke='currentColor' stroke-width="2"/>

  <!-- Top face (perspective) -->
  <polygon points="100,150 140,110 340,110 300,150" fill='rgba(88, 166, 255, 0.1)' stroke='currentColor' stroke-width="2"/>

  <!-- Right face (perspective) -->
  <polygon points="300,150 340,110 340,260 300,300" fill='rgba(88, 166, 255, 0.05)' stroke='currentColor' stroke-width="2"/>

  <!-- Base diagonal -->
  <line x1="100" y1="300" x2="300" y2="150" stroke='#79c0ff' stroke-width="2" stroke-dasharray="5,5"/>

  <!-- Space diagonal -->
  <line x1="100" y1="300" x2="340" y2="110" stroke='#58a6ff' stroke-width="3"/>

  <!-- Height -->
  <line x1="300" y1="150" x2="340" y2="110" stroke='#79c0ff' stroke-width="2"/>

  <!-- Labels -->
  <text x="150" y="330" font-size='14' fill='#79c0ff'>3 m (length)</text>
  <text x="320" y="280" font-size='14' fill='#79c0ff'>4 m (width)</text>
  <text x="350" y="200" font-size='14' fill='#79c0ff'>12 m</text>
  <text x="200" y="190" font-size='14' font-weight='bold' fill='#58a6ff'>13 m (space diagonal)</text>
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
