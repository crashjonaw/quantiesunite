"""Shapes in Real Life — Applying Shape Knowledge."""

TITLE = "Shapes in Real Life"

SECTIONS = [
    {
        "title": "Shapes Are Everywhere!",
        "body": """<p>Once you learn about shapes, you'll start seeing them in absolutely everything. Buildings, food, furniture, vehicles, signs — they're all made from basic shapes!</p>
<svg viewBox="0 0 500 310" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- House -->
  <text x="30" y="30" font-size='12' font-weight='bold' fill='#e6edf3'>🏠 House</text>
  <rect x="20" y="60" width="70" height="60" fill='#d4a574' stroke='#8b6f47' stroke-width="2"/>
  <polygon points="55,60 20,40 90,40" fill='#c84a1a' stroke='#8b4513' stroke-width="2"/>
  <text x="55" y="90" text-anchor='middle' font-size='9' fill='#e6edf3'>rectangle</text>
  <text x="55" y="110" text-anchor='middle' font-size='9' fill='#e6edf3'>+ triangle</text>

  <!-- Clock -->
  <text x="150" y="30" font-size='12' font-weight='bold' fill='#e6edf3'>🕐 Clock</text>
  <circle cx="190" cy="85" r="30" fill='#f4a460' stroke='#8b949e' stroke-width="2"/>
  <text x="190" y="100" text-anchor='middle' font-size='9' fill='#e6edf3'>circle</text>

  <!-- Pizza -->
  <text x="270" y="30" font-size='12' font-weight='bold' fill='#e6edf3'>🍕 Pizza Slice</text>
  <polygon points="340,90 320,60 360,60" fill='#daa520' stroke='#c41e3a' stroke-width="2"/>
  <text x="340" y="105" text-anchor='middle' font-size='9' fill='#e6edf3'>triangle</text>

  <!-- Book -->
  <text x="30" y="160" font-size='12' font-weight='bold' fill='#e6edf3'>📚 Book</text>
  <rect x="20" y="190" width="50" height="70" fill='#8b0000' stroke='#8b949e' stroke-width="2"/>
  <text x="45" y="235" text-anchor='middle' font-size='9' fill='#fff'>rectangle</text>

  <!-- Window -->
  <text x="150" y="160" font-size='12' font-weight='bold' fill='#e6edf3'>🪟 Window</text>
  <rect x="140" y="190" width="50" height="50" fill='#87ceeb' stroke='#8b949e' stroke-width="2"/>
  <line x1="165" y1="190" x2="165" y2="240" stroke='#8b949e' stroke-width="1"/>
  <line x1="140" y1="215" x2="190" y2="215" stroke='#8b949e' stroke-width="1"/>
  <text x="165" y="250" text-anchor='middle' font-size='9' fill='#e6edf3'>square</text>

  <!-- Door -->
  <text x="270" y="160" font-size='12' font-weight='bold' fill='#e6edf3'>🚪 Door</text>
  <rect x="260" y="190" width="40" height="70" fill='#8b4513' stroke='#8b949e' stroke-width="2"/>
  <circle cx="298" cy="225" r="3" fill='#ffd700'/>
  <text x="280" y="275" text-anchor='middle' font-size='9' fill='#e6edf3'>rectangle</text>

  <!-- Coin -->
  <text x="30" y="300" font-size='12' font-weight='bold' fill='#e6edf3'>🪙 Coin</text>

  <!-- Yield sign -->
  <text x="150" y="300" font-size='12' font-weight='bold' fill='#e6edf3'>⛔ Yield Sign</text>

  <!-- Soccer ball -->
  <text x="270" y="300" font-size='12' font-weight='bold' fill='#e6edf3'>⚽ Ball</text>
</svg>
<p>Every object is made from basic shapes. When you understand shapes, you can:</p>
<ul>
<li>Recognize things more quickly</li>
<li>Understand how buildings and objects are designed</li>
<li>Solve puzzles and play shape games</li>
<li>Draw and create things yourself!</li>
</ul>
"""
    },
    {
        "title": "Why Different Shapes for Different Things?",
        "body": """<p>Different shapes are used for different things because they have different properties and strengths.</p>
<div class="worked-example">
<strong>Triangles are super strong!</strong> That's why:
<ul>
<li>Bridge trusses use triangles</li>
<li>Tent frames are triangular</li>
<li>Roof frames use triangles</li>
</ul>
Triangles don't bend or collapse easily!
</div>
<div class="worked-example">
<strong>Circles roll!</strong> That's why:
<ul>
<li>Wheels are circles</li>
<li>Balls are circles (spheres in 3D)</li>
<li>Coins are circles</li>
</ul>
You can't roll a square wheel!
</div>
<div class="worked-example">
<strong>Rectangles fit together!</strong> That's why:
<ul>
<li>Bricks are rectangular</li>
<li>Books are rectangular</li>
<li>Windows and doors are rectangular</li>
</ul>
Rectangles pack efficiently with no wasted space!
</div>
"""
    },
    {
        "title": "Interactive Shape Finder",
        "body": """<div class="concept-box">
<strong>Challenge 1: Room Shapes</strong><br>
Look at your bedroom. Can you find and count:
<ul>
<li>How many circles? (clocks, lights, plates)</li>
<li>How many triangles? (tent corners, roof peaks)</li>
<li>How many squares? (tiles, cushions, picture frames)</li>
<li>How many rectangles? (books, windows, doors, beds, tables)</li>
</ul>
Which shape do you find most often? <strong>Rectangles!</strong> Because they fit together and use space efficiently.
</div>

<button class="reveal-btn" data-reveal="real2">▼ Challenge 2: Food Shapes</button>
<div class="reveal-panel" id="real2">
Look in your kitchen. What shapes can you find?
<ul>
<li>🍕 Pizza slice = <strong>triangle</strong></li>
<li>🥪 Sandwich = <strong>triangle</strong> (if cut diagonally!) or <strong>rectangle</strong></li>
<li>🍪 Cookie = <strong>circle</strong> or <strong>square</strong></li>
<li>🍎 Apple = <strong>circle</strong> (sphere in 3D)</li>
<li>📦 Cereal box = <strong>rectangle</strong></li>
</ul>
</div>

<button class="reveal-btn" data-reveal="real3">▼ Challenge 3: Design a Playground</button>
<div class="reveal-panel" id="real3">
If you were to design a playground, which shapes would you use?
<ul>
<li>Swings: Use <strong>circles</strong> and <strong>rectangles</strong> for the frame</li>
<li>Slide: Has a <strong>triangular</strong> frame and <strong>rectangular</strong> slide surface</li>
<li>Sandbox: Usually a <strong>square</strong> or <strong>rectangle</strong></li>
<li>Merry-go-round: Uses a <strong>circle</strong></li>
</ul>
</div>
"""
    },
    {
        "title": "Shapes Around the World",
        "body": """<p><strong>Different cultures use shapes differently:</strong></p>
<div class="success-box">
<strong>Egyptian Pyramids:</strong> Built with triangular faces because triangles are strong and stable.<br><br>
<strong>Japanese Gardens:</strong> Often include circular stepping stones and rectangular pools because these shapes create balance and beauty.<br><br>
<strong>Islamic Patterns:</strong> Use geometric shapes (circles, squares, triangles) in repeating patterns called tessellations.<br><br>
<strong>Modern Architecture:</strong> Uses circles, squares, and rectangles to create functional, beautiful buildings.
</div>

<button class="reveal-btn" data-reveal="real4">▼ Fun fact: Honeycombs</button>
<div class="reveal-panel" id="real4">
Did you know bees build honeycombs with <strong>hexagons</strong> (6-sided shapes)? This is because hexagons are the strongest shape and use the least amount of wax. Nature discovered the perfect shape!
</div>

<button class="reveal-btn" data-reveal="real5">▼ Can shapes tell stories?</button>
<div class="reveal-panel" id="real5">
Yes! Artists and designers use shapes to communicate:
<ul>
<li>🔺 A triangle pointing up feels <strong>strong</strong> and <strong>stable</strong></li>
<li>⬜ A square feels <strong>balanced</strong> and <strong>calm</strong></li>
<li>⭕ A circle feels <strong>friendly</strong> and <strong>complete</strong></li>
<li>▬ A horizontal line feels <strong>peaceful</strong> and <strong>calm</strong></li>
<li>|  A vertical line feels <strong>strong</strong> and <strong>tall</strong></li>
</ul>
</div>
"""
    }
]
