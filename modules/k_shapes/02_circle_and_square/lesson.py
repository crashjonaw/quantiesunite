"""Circle and Square — 2D Shapes Concept."""

TITLE = "Circle and Square"

SECTIONS = [
    {
        "title": "The Perfect Circle",
        "body": """<p>A <strong>circle</strong> is the most perfectly balanced shape. Every point on the edge is <strong>exactly the same distance</strong> from the center.</p>
<svg viewBox="0 0 400 300" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <!-- Circle -->
  <circle cx="200" cy="150" r="80" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3"/>
  <!-- Center point -->
  <circle cx="200" cy="150" r="5" fill='#ef4444'/>
  <!-- Radius lines -->
  <line x1="200" y1="150" x2="280" y2="150" stroke='#ef4444' stroke-width="2"/>
  <line x1="200" y1="150" x2="165" y2="210" stroke='#ef4444' stroke-width="2"/>
  <line x1="200" y1="150" x2="140" y2="100" stroke='#ef4444' stroke-width="2"/>
  <!-- Labels -->
  <text x="240" y="145" font-size='14' font-weight='bold' fill='currentColor'>radius</text>
  <text x="190" y="140" font-size='14' font-weight='bold' fill='currentColor'>center</text>
  <!-- Key facts -->
  <text x="200" y="280" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>0 sides  •  0 corners  •  1 curved edge</text>
</svg>
<p><strong>Special properties of circles:</strong></p>
<ul>
<li>Every circle has exactly <strong>0 sides</strong> and <strong>0 corners</strong></li>
<li>The distance from center to edge is called the <strong>radius</strong></li>
<li>Circles are <strong>symmetrical in all directions</strong> — you can turn them and they look the same!</li>
</ul>
<div class="success-box">
<strong>Fun fact:</strong> A circle has <strong>infinite symmetry</strong> — you can flip it, rotate it, and it always looks the same. No other shape can do this!
</div>
"""
    },
    {
        "title": "The Square",
        "body": """<p>A <strong>square</strong> is one of the most common shapes. It has <strong>4 equal sides</strong> and <strong>4 right corners</strong> (90° angles).</p>
<svg viewBox="0 0 400 300" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <!-- Square -->
  <rect x="100" y="80" width="120" height="120" fill='#22c55e30' stroke='#22c55e' stroke-width="3"/>
  <!-- Corner indicators -->
  <circle cx="100" cy="80" r="5" fill='#ef4444'/>
  <circle cx="220" cy="80" r="5" fill='#ef4444'/>
  <circle cx="220" cy="200" r="5" fill='#ef4444'/>
  <circle cx="100" cy="200" r="5" fill='#ef4444'/>
  <!-- Right angle indicators -->
  <rect x="100" y="80" width="10" height="10" fill='none' stroke='#ef4444' stroke-width="1.5"/>
  <rect x="210" y="80" width="10" height="10" fill='none' stroke='#ef4444' stroke-width="1.5"/>
  <rect x="210" y="190" width="10" height="10" fill='none' stroke='#ef4444' stroke-width="1.5"/>
  <rect x="100" y="190" width="10" height="10" fill='none' stroke='#ef4444' stroke-width="1.5"/>
  <!-- Side labels -->
  <text x="160" y="60" text-anchor='middle' font-size='12' fill='currentColor'>side</text>
  <text x="240" y="140" text-anchor='middle' font-size='12' fill='currentColor'>side</text>
  <text x="160" y="230" text-anchor='middle' font-size='12' fill='currentColor'>side</text>
  <text x="60" y="140" text-anchor='middle' font-size='12' fill='currentColor'>side</text>
  <!-- Key facts -->
  <text x="200" y="260" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>4 EQUAL sides  •  4 right corners</text>
</svg>
<p><strong>What makes a square special:</strong></p>
<ul>
<li>All 4 sides are <strong>exactly the same length</strong></li>
<li>All 4 corners are <strong>right angles</strong> (\\(90°\\))</li>
<li>A square is perfectly <strong>symmetrical</strong> — it has 4 lines of symmetry</li>
</ul>
<div class="success-box">
<strong>A square is a special rectangle!</strong> A rectangle is any shape with 4 sides and 4 right corners. A square is a rectangle where all sides are equal.
</div>
"""
    },
    {
        "title": "Comparing Circles and Squares",
        "body": """<canvas id="shapeChart1" data-chart='{"type":"bar","data":{"labels":["Circle","Square"],"datasets":[{"label":"Number of Sides","data":[0,4],"backgroundColor":["#4f8ef7","#22c55e"]},{"label":"Number of Corners","data":[0,4],"backgroundColor":["#4f8ef780","#22c55e80"]}]},"options":{"indexAxis":"y","plugins":{"title":{"display":true,"text":"Circle vs Square Properties"}}}}' height="220"></canvas>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
<tr class="formula-box">
<th style="padding: 8px; text-align: left">Property</th>
<th style="padding: 8px; text-align: center;">Circle</th>
<th style="padding: 8px; text-align: center;">Square</th>
</tr>
<tr>
<td style="padding: 8px;">Sides</td>
<td style="padding: 8px; text-align: center;">0</td>
<td style="padding: 8px; text-align: center;">4</td>
</tr>
<tr style="background:#f9f9f9;">
<td style="padding: 8px;">Corners</td>
<td style="padding: 8px; text-align: center;">0</td>
<td style="padding: 8px; text-align: center;">4</td>
</tr>
<tr>
<td style="padding: 8px;">Shape</td>
<td style="padding: 8px; text-align: center;">Curved</td>
<td style="padding: 8px; text-align: center;">Straight edges</td>
</tr>
<tr style="background:#f9f9f9;">
<td style="padding: 8px;">Equal sides</td>
<td style="padding: 8px; text-align: center;">N/A</td>
<td style="padding: 8px; text-align: center;">Yes</td>
</tr>
</table>
"""
    },
    {
        "title": "Where Do We See Them?",
        "body": """<div class="worked-example">
<strong>Circles in real life:</strong><br>
🕐 Clocks, 🍕 pizzas, 🪙 coins, 🌙 the moon, 💿 CDs, 🍂 wheels
</div>
<div class="worked-example">
<strong>Squares in real life:</strong><br>
🎮 Game boards, 📋 tiles on walls, ⬜ ice cubes, 🎯 targets, 📦 small boxes
</div>
<button class="reveal-btn" data-reveal="real1">▼ Interactive: Find circles and squares!</button>
<div class="reveal-panel" id="real1">
Look at a map of your house. Find 3 circles (like round tables, plates, or lights) and 3 squares or square-shaped things (like picture frames, windows, or cushions). Can you draw them?
</div>
"""
    }
]
