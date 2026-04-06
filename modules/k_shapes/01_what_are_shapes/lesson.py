"""What are Shapes? — Foundational concept."""

TITLE = "What are Shapes?"

SECTIONS = [
    {
        "title": "Why Do Shapes Matter?",
        "body": """<div class="concept-box">
<p>Look around you right now. A <strong>door is a rectangle</strong>. A <strong>pizza is a circle</strong>. A <strong>yield sign is a triangle</strong>. Shapes describe the <strong>outline</strong> of objects all around us.</p>
<p>Mathematicians studied shapes so we could <strong>describe and build things precisely</strong>. When you understand shapes, you can recognize patterns, solve puzzles, and create amazing things!</p>
</div>
<p><strong>What is a shape?</strong> A shape is something with a clear outline and size. Every shape has edges (called <strong>sides</strong>) and points where edges meet (called <strong>corners</strong> or <strong>vertices</strong>).</p>
<p>In this lesson, we'll explore <strong>2D shapes</strong> — shapes that are flat, like when you draw them on paper. These shapes live in two dimensions: up-down and left-right.</p>
"""
    },
    {
        "title": "The Four Main Shapes",
        "body": """<p>There are four shapes you'll see everywhere:</p>
<svg viewBox="0 0 520 200" style="width:100%;max-width:520px;height:auto;display:block;margin:16px auto;">
  <!-- Circle — centered at x=65 -->
  <circle cx="65" cy="90" r="45" fill='#4f8ef750' stroke='#4f8ef7' stroke-width="3"/>
  <text x="65" y="175" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Circle</text>

  <!-- Square — centered at x=195 -->
  <rect x="152" y="48" width="85" height="85" fill='#22c55e50' stroke='#22c55e' stroke-width="3"/>
  <text x="195" y="175" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Square</text>

  <!-- Triangle — centered at x=325 -->
  <polygon points="325,48 375,133 275,133" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <text x="325" y="175" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Triangle</text>

  <!-- Rectangle — centered at x=455 -->
  <rect x="400" y="68" width="110" height="68" fill='#f59e0b50' stroke='#f59e0b' stroke-width="3"/>
  <text x="455" y="175" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Rectangle</text>
</svg>
"""
    },
    {
        "title": "Sides and Corners",
        "body": """<p>Every shape (except the circle!) has <strong>sides</strong> and <strong>corners</strong>.</p>
<ul>
<li><strong>Side:</strong> An edge of a shape. Like one side of a square or one side of a triangle.</li>
<li><strong>Corner (or vertex):</strong> A point where two sides meet. Like the corners of a rectangular picture frame.</li>
</ul>
<div class="success-box">
<strong>Quick Challenge:</strong> How many sides does a square have? How many corners? (Hint: they're the same number!)
</div>
<p>A circle is special — it has <strong>no sides and no corners</strong>. It's one continuous, smooth curve!</p>
"""
    },
    {
        "title": "Real-World Shapes",
        "body": """<div class="worked-example">
<strong>Look around your home:</strong>
<ul>
<li>📚 A book is a <strong>rectangle</strong></li>
<li>🕐 A clock is a <strong>circle</strong></li>
<li>🪟 A window is a <strong>square</strong> or <strong>rectangle</strong></li>
<li>🍕 A pizza slice is a <strong>triangle</strong></li>
<li>📦 A box face is a <strong>rectangle</strong> or <strong>square</strong></li>
<li>🔴 A coin is a <strong>circle</strong></li>
</ul>
</div>
<button class="reveal-btn" data-reveal="hunt1">▼ Can you find 5 shapes?</button>
<div class="reveal-panel" id="hunt1">
Try this: Look at your room and find one circle, one square, one triangle, and two rectangles. Take a picture or draw them!
</div>
"""
    }
]
