"""Shapes in Real Life — Applying Shape Knowledge."""

TITLE = "Shapes in Real Life"

SECTIONS = [
    {
        "title": "Shapes Are Everywhere!",
        "body": """<p>Once you learn about shapes, you'll start seeing them in absolutely everything. Buildings, food, furniture, vehicles, signs — they're all made from basic shapes!</p>
<svg viewBox="0 0 540 380" style="width:100%;max-width:540px;height:auto;display:block;margin:16px auto;">
  <!-- Row 1 -->
  <!-- House — col 1, centered at x=90 -->
  <rect x="50" y="65" width="80" height="60" fill='#d4a574' stroke='#8b6f47' stroke-width="2.5"/>
  <polygon points="90,65 45,35 135,35" fill='#c84a1a' stroke='#8b4513' stroke-width="2.5"/>
  <rect x="77" y="90" width="26" height="35" fill='#5a3a1a' stroke='#8b6f47' stroke-width="1.5"/>
  <text x="90" y="145" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>House</text>
  <text x="90" y="160" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>rectangle + triangle</text>

  <!-- Clock — col 2, centered at x=270 -->
  <circle cx="270" cy="70" r="42" fill='#fef3c7' stroke='#d97706' stroke-width="2.5"/>
  <circle cx="270" cy="70" r="3" fill='#d97706'/>
  <line x1="270" y1="70" x2="270" y2="42" stroke='#d97706' stroke-width="2.5" stroke-linecap='round'/>
  <line x1="270" y1="70" x2="290" y2="78" stroke='#d97706' stroke-width="2" stroke-linecap='round'/>
  <text x="270" y="130" text-anchor='middle' font-size='11' fill='#d97706' font-weight='bold'>12</text>
  <text x="270" y="145" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Clock</text>
  <text x="270" y="160" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>circle</text>

  <!-- Pizza Slice — col 3, centered at x=450 -->
  <polygon points="450,30 420,120 480,120" fill='#fbbf24' stroke='#d97706' stroke-width="2.5"/>
  <circle cx="445" cy="75" r="4" fill='#dc2626'/>
  <circle cx="460" cy="90" r="4" fill='#dc2626'/>
  <circle cx="440" cy="100" r="4" fill='#dc2626'/>
  <text x="450" y="145" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Pizza Slice</text>
  <text x="450" y="160" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>triangle</text>

  <!-- Row 2 -->
  <!-- Book — col 1, centered at x=90 -->
  <rect x="60" y="195" width="60" height="80" rx="3" fill='#991b1b' stroke='#7f1d1d' stroke-width="2.5"/>
  <line x1="62" y1="195" x2="62" y2="275" stroke='#fca5a5' stroke-width="2"/>
  <line x1="72" y1="215" x2="110" y2="215" stroke='#fca5a5' stroke-width="1" opacity='0.5'/>
  <line x1="72" y1="225" x2="105" y2="225" stroke='#fca5a5' stroke-width="1" opacity='0.5'/>
  <line x1="72" y1="235" x2="108" y2="235" stroke='#fca5a5' stroke-width="1" opacity='0.5'/>
  <text x="90" y="295" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Book</text>
  <text x="90" y="310" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>rectangle</text>

  <!-- Window — col 2, centered at x=270 -->
  <rect x="235" y="200" width="70" height="70" fill='#bae6fd' stroke='#6b7280' stroke-width="2.5"/>
  <line x1="270" y1="200" x2="270" y2="270" stroke='#6b7280' stroke-width="2"/>
  <line x1="235" y1="235" x2="305" y2="235" stroke='#6b7280' stroke-width="2"/>
  <text x="270" y="295" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Window</text>
  <text x="270" y="310" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>square</text>

  <!-- Coin — col 3, centered at x=450 -->
  <circle cx="450" cy="235" r="35" fill='#fde68a' stroke='#d97706' stroke-width="2.5"/>
  <circle cx="450" cy="235" r="28" fill='none' stroke='#d97706' stroke-width="1.5"/>
  <text x="450" y="240" text-anchor='middle' font-size='16' fill='#92400e' font-weight='bold'>1</text>
  <text x="450" y="295" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Coin</text>
  <text x="450" y="310" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.7'>circle</text>

  <!-- Decorative divider lines between rows -->
  <line x1="30" y1="175" x2="510" y2="175" stroke='currentColor' stroke-width="0.5" opacity='0.15'/>
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
