"""Shapes & Patterns — Lesson sections."""

SECTIONS = [
    {
        "title": "What are Shapes? 🎨",
        "body": """<p>A <strong>shape</strong> is something with a clear outline and size. We see shapes everywhere!</p>
<p>Shapes are like the building blocks of everything we see. When you look around, you'll notice that most things can be described using simple shapes.</p>
<div class='example-box'>
<strong>Real-world examples:</strong><br>
🔵 A ball is a <strong>circle</strong><br>
📦 A box is a <strong>square</strong><br>
🍕 A pizza slice is a <strong>triangle</strong><br>
📄 A piece of paper is a <strong>rectangle</strong>
</div>
<p>In this lesson, we'll learn about 2D shapes — shapes that are flat, like when you draw them on paper. These shapes have <strong>sides</strong> and <strong>corners</strong> (also called vertices).</p>"""
    },
    {
        "title": "Understanding Circles ⭕",
        "body": """<p>A <strong>circle</strong> is a special shape with <strong>no sides and no corners</strong>. It's completely round!</p>
<p>Every point on a circle is the same distance from the center. This is why circles look so perfectly round and smooth.</p>
<svg viewBox="0 0 200 150" style="width:100%;max-width:200px;height:auto;display:block;margin:16px auto;"
  <circle cx="100" cy="75" r="50" fill="lightblue" stroke="darkblue" stroke-width="2"/>
  <line x1="100" y1="75" x2="150" y2="75" stroke="red" stroke-width="2"/>
  <text x="115" y="70" font-size="14" fill='currentColor'>radius</text>
  <circle cx="100" cy="75" r="3" fill="red"/>
  <text x="90" y="95" font-size="14" fill='currentColor'>center</text>
</svg>
<p><strong>Why does a circle matter?</strong> Circles are everywhere — wheels, coins, the sun, clocks, pizza! Understanding circles helps us recognize these things in the real world.</p>
<div class='example-box'>
<strong>Try it yourself:</strong> Find 3 circles in your classroom or home. Examples: clock, cup opening, plate!
</div>"""
    },
    {
        "title": "Squares & Rectangles 📦",
        "body": """<p>A <strong>square</strong> is a shape with <strong>4 equal sides</strong> and <strong>4 corners</strong>. All the corners are the same — they're all right angles (90°).</p>
<p>A <strong>rectangle</strong> is similar, but its sides don't all have to be the same length. It has <strong>2 long sides and 2 short sides</strong>, and all 4 corners are still right angles.</p>
<svg viewBox="0 0 300 150" style="width:100%;max-width:300px;height:auto;display:block;margin:16px auto;"
  <text x="50" y="20" font-size="16" font-weight="bold" fill='currentColor'>Square</text>
  <rect x="20" y="40" width="80" height="80" fill="lightyellow" stroke="orange" stroke-width="2" rx='4'/>
  <circle cx="20" cy="40" r="4" fill="red"/>
  <circle cx="100" cy="40" r="4" fill="red"/>
  <circle cx="100" cy="120" r="4" fill="red"/>
  <circle cx="20" cy="120" r="4" fill="red"/>
  <text x="35" y="135" font-size="12" fill='currentColor'>4 equal sides</text>

  <text x="180" y="20" font-size="16" font-weight="bold" fill='currentColor'>Rectangle</text>
  <rect x="150" y="40" width="120" height="60" fill="lightgreen" stroke="darkgreen" stroke-width="2" rx='4'/>
  <circle cx="150" cy="40" r="4" fill="red"/>
  <circle cx="270" cy="40" r="4" fill="red"/>
  <circle cx="270" cy="100" r="4" fill="red"/>
  <circle cx="150" cy="100" r="4" fill="red"/>
  <text x="170" y="135" font-size="12" fill='currentColor'>2 long, 2 short sides</text>
</svg>
<p><strong>Real-world examples:</strong> Books, doors, windows, tiles, and screens are rectangles. A postage stamp or ice cube might be a square!</p>
<div class='example-box'>
<strong>KEY FACT:</strong> A square is a special type of rectangle where all sides are equal!
</div>"""
    },
    {
        "title": "Triangles 🔺",
        "body": """<p>A <strong>triangle</strong> is a shape with <strong>3 sides and 3 corners</strong>. It's one of the simplest shapes to draw!</p>
<p>All triangles have 3 sides and 3 corners, but they can look very different. Some triangles are tall and thin, others are wide and flat.</p>
<svg viewBox="0 0 350 150" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;"
  <text x="30" y="20" font-size="14" font-weight="bold" fill='currentColor'>Tall Triangle</text>
  <polygon points="70,120 70,30 110,120" fill="lightcoral" stroke="darkred" stroke-width="2"/>
  <circle cx="70" cy="120" r="3" fill="red"/>
  <circle cx="70" cy="30" r="3" fill="red"/>
  <circle cx="110" cy="120" r="3" fill="red"/>

  <text x="180" y="20" font-size="14" font-weight="bold" fill='currentColor'>Flat Triangle</text>
  <polygon points="160,120 220,120 190,50" fill="lightsalmon" stroke="darkorange" stroke-width="2"/>
  <circle cx="160" cy="120" r="3" fill="red"/>
  <circle cx="220" cy="120" r="3" fill="red"/>
  <circle cx="190" cy="50" r="3" fill="red"/>

  <text x="300" y="20" font-size="14" font-weight="bold" fill='currentColor'>Wide Triangle</text>
  <polygon points="280,120 340,120 310,60" fill="lightpink" stroke="deeppink" stroke-width="2"/>
  <circle cx="280" cy="120" r="3" fill="red"/>
  <circle cx="340" cy="120" r="3" fill="red"/>
  <circle cx="310" cy="60" r="3" fill="red"/>
</svg>
<p><strong>Why learn triangles?</strong> Triangles are super strong shapes. They're used in bridges, roofs of houses, and lots of structures!</p>
<div class='example-box'>
<strong>Count the corners:</strong> 1, 2, 3! <strong>Count the sides:</strong> 1, 2, 3! Always 3 of each.
</div>"""
    },
    {
        "title": "Recognizing & Creating Patterns 🎯",
        "body": """<p>A <strong>pattern</strong> is when shapes (or colors, or anything!) repeat in a way we can predict. Patterns help us see order in the world.</p>
<p>The most basic pattern is when something repeats over and over: <strong>A, B, A, B, A, B</strong> is a pattern. You can guess what comes next!</p>
<div class='example-box'>
<strong>Shape Pattern Example:</strong><br>
🔵 🟩 🔵 🟩 🔵 🟩 🔵 <strong style="color: red;">?</strong><br>
<br>
The pattern is: <strong>circle, square, circle, square...</strong><br>
The next shape should be <strong>🟩 (a square)</strong>!
</div>
<svg viewBox="0 0 350 120" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;"
  <text x="10" y="20" font-size="14" font-weight="bold" fill='currentColor'>Pattern Example with Colors:</text>
  <circle cx="40" cy="60" r="15" fill="red"/>
  <circle cx="80" cy="60" r="15" fill="yellow"/>
  <circle cx="120" cy="60" r="15" fill="red"/>
  <circle cx="160" cy="60" r="15" fill="yellow"/>
  <circle cx="200" cy="60" r="15" fill="red"/>
  <circle cx="240" cy="60" r="15" fill="yellow"/>
  <circle cx="280" cy="60" r="15" fill="lightgray" stroke="red" stroke-width="2" stroke-dasharray="5"/>
  <text x="265" y="70" font-size="16" fill='currentColor'>?</text>
  <text x="20" y="105" font-size="12" fill='currentColor'>Pattern: RED, YELLOW, RED, YELLOW...</text>
  <text x="250" y="105" font-size="12" fill='currentColor'>Next: RED</text>
</svg>
<p><strong>Patterns are powerful!</strong> When you see a pattern, you can predict what comes next without being told. This is the beginning of mathematical thinking!</p>
<div class='example-box'>
<strong>Try making your own patterns:</strong> Use shapes cut from paper or draw them. Arrange them in a pattern and ask a friend to guess what comes next!
</div>"""
    }
]
