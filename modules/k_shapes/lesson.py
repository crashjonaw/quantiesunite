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
<svg viewBox="0 0 230 170" style="width:100%;max-width:230px;height:auto;display:block;margin:16px auto;">
  <circle cx="115" cy="85" r="50" fill="#4f8ef730" stroke="#4f8ef7" stroke-width="3"/>
  <line x1="115" y1="85" x2="165" y2="85" stroke="#ef4444" stroke-width="2"/>
  <text x="130" y="78" font-size="13" fill='currentColor' font-weight='bold'>radius</text>
  <circle cx="115" cy="85" r="4" fill="#ef4444"/>
  <text x="115" y="155" text-anchor="middle" font-size="13" fill='currentColor' font-weight='bold'>center</text>
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
<svg viewBox="0 0 360 165" style="width:100%;max-width:360px;height:auto;display:block;margin:16px auto;">
  <!-- Square — centered at x=90 -->
  <text x="90" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill='currentColor'>Square</text>
  <rect x="45" y="35" width="90" height="90" fill="#22c55e30" stroke="#22c55e" stroke-width="3" rx='4'/>
  <circle cx="45" cy="35" r="4" fill="#ef4444"/>
  <circle cx="135" cy="35" r="4" fill="#ef4444"/>
  <circle cx="135" cy="125" r="4" fill="#ef4444"/>
  <circle cx="45" cy="125" r="4" fill="#ef4444"/>
  <text x="90" y="150" text-anchor="middle" font-size="12" fill='currentColor' font-weight='bold'>4 equal sides</text>

  <!-- Rectangle — centered at x=270 -->
  <text x="270" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill='currentColor'>Rectangle</text>
  <rect x="210" y="50" width="120" height="65" fill="#f59e0b30" stroke="#f59e0b" stroke-width="3" rx='4'/>
  <circle cx="210" cy="50" r="4" fill="#ef4444"/>
  <circle cx="330" cy="50" r="4" fill="#ef4444"/>
  <circle cx="330" cy="115" r="4" fill="#ef4444"/>
  <circle cx="210" cy="115" r="4" fill="#ef4444"/>
  <text x="270" y="150" text-anchor="middle" font-size="12" fill='currentColor' font-weight='bold'>2 long, 2 short sides</text>
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
<svg viewBox="0 0 420 155" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <!-- Tall — centered at x=70 -->
  <text x="70" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill='currentColor'>Tall</text>
  <polygon points="55,125 55,35 100,125" fill="#ef444450" stroke="#ef4444" stroke-width="3"/>
  <circle cx="55" cy="125" r="4" fill="#ef4444"/>
  <circle cx="55" cy="35" r="4" fill="#ef4444"/>
  <circle cx="100" cy="125" r="4" fill="#ef4444"/>

  <!-- Flat — centered at x=210 -->
  <text x="210" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill='currentColor'>Flat</text>
  <polygon points="170,125 250,125 210,55" fill="#f59e0b50" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="170" cy="125" r="4" fill="#f59e0b"/>
  <circle cx="250" cy="125" r="4" fill="#f59e0b"/>
  <circle cx="210" cy="55" r="4" fill="#f59e0b"/>

  <!-- Wide — centered at x=350 -->
  <text x="350" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill='currentColor'>Wide</text>
  <polygon points="310,125 390,125 350,55" fill="#a855f750" stroke="#a855f7" stroke-width="3"/>
  <circle cx="310" cy="125" r="4" fill="#a855f7"/>
  <circle cx="390" cy="125" r="4" fill="#a855f7"/>
  <circle cx="350" cy="55" r="4" fill="#a855f7"/>

  <text x="210" y="148" text-anchor="middle" font-size="12" fill='currentColor' font-weight='bold'>All triangles have 3 sides and 3 corners</text>
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
<svg viewBox="0 0 370 130" style="width:100%;max-width:370px;height:auto;display:block;margin:16px auto;">
  <text x="185" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill='currentColor'>Pattern Example with Colors:</text>
  <!-- 7 circles evenly spaced: centers at 40, 85, 130, 175, 220, 265, 310 -->
  <circle cx="40" cy="62" r="18" fill="#ef4444"/>
  <circle cx="85" cy="62" r="18" fill="#facc15"/>
  <circle cx="130" cy="62" r="18" fill="#ef4444"/>
  <circle cx="175" cy="62" r="18" fill="#facc15"/>
  <circle cx="220" cy="62" r="18" fill="#ef4444"/>
  <circle cx="265" cy="62" r="18" fill="#facc15"/>
  <circle cx="310" cy="62" r="18" fill="#e5e7eb" stroke="#ef4444" stroke-width="2" stroke-dasharray="5"/>
  <text x="310" y="68" text-anchor="middle" font-size="16" font-weight="bold" fill='currentColor'>?</text>
  <text x="130" y="108" text-anchor="middle" font-size="12" fill='currentColor'>RED, YELLOW, RED, YELLOW...</text>
  <text x="310" y="108" text-anchor="middle" font-size="12" fill='currentColor' font-weight="bold">Next: RED</text>
</svg>
<p><strong>Patterns are powerful!</strong> When you see a pattern, you can predict what comes next without being told. This is the beginning of mathematical thinking!</p>
<div class='example-box'>
<strong>Try making your own patterns:</strong> Use shapes cut from paper or draw them. Arrange them in a pattern and ask a friend to guess what comes next!
</div>"""
    }
]
