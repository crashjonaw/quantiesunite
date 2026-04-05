"""Sides and Corners — Understanding Shape Properties."""

TITLE = "Sides and Corners"

SECTIONS = [
    {
        "title": "What Are Sides?",
        "body": """<p>A <strong>side</strong> is one straight edge of a shape. You can trace your finger along one side.</p>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Circle -->
  <circle cx="80" cy="100" r="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3"/>
  <text x="80" y="160" text-anchor='middle' font-size='12' fill='currentColor'>0 sides</text>

  <!-- Triangle -->
  <polygon points="200,150 200,50 270,150" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <text x="200" y="40" font-size='11' fill='#ef4444' font-weight='bold'>side 1</text>
  <text x="260" y="110" font-size='11' fill='#ef4444' font-weight='bold'>side 2</text>
  <text x="230" y="165" font-size='11' fill='#ef4444' font-weight='bold'>side 3</text>
  <text x="200" y="170" text-anchor='middle' font-size='12' fill='currentColor'>3 sides</text>

  <!-- Square -->
  <rect x="340" y="50" width="100" height="100" fill='#22c55e30' stroke='#22c55e' stroke-width="3"/>
  <text x="340" y="35" font-size='11' fill='#22c55e' font-weight='bold'>top</text>
  <text x="460" y="105" font-size='11' fill='#22c55e' font-weight='bold'>right</text>
  <text x="390" y="165" font-size='11' fill='#22c55e' font-weight='bold'>bottom</text>
  <text x="320" y="105" font-size='11' fill='#22c55e' font-weight='bold'>left</text>
  <text x="390" y="170" text-anchor='middle' font-size='12' fill='currentColor'>4 sides</text>
</svg>
<p><strong>Why count sides?</strong> By counting sides, we can quickly identify what shape something is:</p>
<ul>
<li><strong>0 sides</strong> = circle</li>
<li><strong>3 sides</strong> = triangle</li>
<li><strong>4 sides</strong> = square or rectangle (or other four-sided shapes)</li>
</ul>
<div class="success-box">
<strong>Quick tip:</strong> You can count sides by counting the straight edges. Circles have no straight edges, so they have 0 sides!
</div>
"""
    },
    {
        "title": "What Are Corners?",
        "body": """<p>A <strong>corner</strong> (also called a <strong>vertex</strong>) is a point where two sides meet. You can feel corners — they're the pointy or sharp parts of a shape!</p>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Circle (no corners) -->
  <circle cx="80" cy="100" r="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3"/>
  <text x="80" y="160" text-anchor='middle' font-size='12' fill='currentColor'>0 corners</text>

  <!-- Triangle (3 corners) -->
  <polygon points="200,150 200,50 270,150" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="200" cy="150" r="6" fill='#ef4444'/>
  <circle cx="200" cy="50" r="6" fill='#ef4444'/>
  <circle cx="270" cy="150" r="6" fill='#ef4444'/>
  <text x="200" y="170" text-anchor='middle' font-size='12' fill='currentColor'>3 corners</text>

  <!-- Square (4 corners with right angle markers) -->
  <rect x="340" y="50" width="100" height="100" fill='#22c55e30' stroke='#22c55e' stroke-width="3"/>
  <circle cx="340" cy="50" r="6" fill='#22c55e'/>
  <circle cx="440" cy="50" r="6" fill='#22c55e'/>
  <circle cx="440" cy="150" r="6" fill='#22c55e'/>
  <circle cx="340" cy="150" r="6" fill='#22c55e'/>
  <!-- Right angle indicators -->
  <rect x="340" y="50" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="430" y="50" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="430" y="140" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="340" y="140" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <text x="390" y="170" text-anchor='middle' font-size='12' fill='currentColor'>4 corners (right angles)</text>
</svg>
<p><strong>Important fact:</strong> The number of sides always equals the number of corners (except for circles, which have neither)!</p>
<div class="concept-box">
<strong>Sides = Corners</strong><br>
A triangle has 3 sides and 3 corners.<br>
A square has 4 sides and 4 corners.<br>
A rectangle has 4 sides and 4 corners.<br>
A circle has 0 sides and 0 corners.
</div>
"""
    },
    {
        "title": "Right Angles and Corners",
        "body": """<p>Most shapes have <strong>corners</strong>, and many of those corners are <strong>right angles</strong>. A <strong>right angle</strong> is exactly \\(90°\\) — it's the angle you see in the corner of a book or door!</p>
<svg viewBox="0 0 500 300" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Right angle example -->
  <text x="50" y="30" font-size='14' font-weight='bold' fill='currentColor'>Right Angle (90°)</text>
  <line x1="80" y1="120" x2="150" y2="120" stroke='#22c55e' stroke-width="3"/>
  <line x1="80" y1="120" x2="80" y2="50" stroke='#22c55e' stroke-width="3"/>
  <rect x="80" y="50" width="20" height="20" fill='none' stroke='#22c55e' stroke-width="2"/>
  <text x="95" y="45" font-size='12' fill='#22c55e'>90°</text>

  <!-- Shapes with right angles -->
  <text x="50" y="170" font-size='14' font-weight='bold' fill='currentColor'>Shapes with Right Angles:</text>

  <!-- Square -->
  <rect x="40" y="190" width="60" height="60" fill='#22c55e30' stroke='#22c55e' stroke-width="2"/>
  <rect x="40" y="190" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="92" y="190" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="92" y="242" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="40" y="242" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <text x="70" y="270" text-anchor='middle' font-size='12' fill='currentColor'>Square</text>
  <text x="70" y="285" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(4 right angles)</text>

  <!-- Rectangle -->
  <rect x="150" y="190" width="90" height="60" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2"/>
  <rect x="150" y="190" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="232" y="190" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="232" y="242" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="150" y="242" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="195" y="270" text-anchor='middle' font-size='12' fill='currentColor'>Rectangle</text>
  <text x="195" y="285" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(4 right angles)</text>

  <!-- Triangle (often no right angles) -->
  <polygon points="300,250 300,190 360,250" fill='#ef444450' stroke='#ef4444' stroke-width="2"/>
  <text x="330" y="270" text-anchor='middle' font-size='12' fill='currentColor'>Triangle</text>
  <text x="330" y="285" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(usually no right angles)</text>
</svg>
<button class="reveal-btn" data-reveal="reveal4">▼ Can you find right angles?</button>
<div class="reveal-panel" id="reveal4">
Look around your room! Find 5 things with right angle corners. Hint: look at your furniture, door frames, windows, books, and boxes!
</div>
"""
    },
    {
        "title": "Summary: Counting Shapes",
        "body": """<canvas id="shapeChart3" data-chart='{"type":"bar","data":{"labels":["Circle","Triangle","Square","Rectangle"],"datasets":[{"label":"Number of Sides","data":[0,3,4,4],"backgroundColor":["#4f8ef7","#ef4444","#22c55e","#f59e0b"]},{"label":"Number of Corners","data":[0,3,4,4],"backgroundColor":["#4f8ef780","#ef444480","#22c55e80","#f59e0b80"]}]},"options":{"plugins":{"title":{"display":true,"text":"Complete Shape Summary: Sides and Corners"}}}}' height="220"></canvas>
<div class="success-box">
<strong>Remember:</strong> Every side is a straight edge, and every corner is a point where two sides meet. For shapes with straight sides, the number of sides always equals the number of corners!
</div>
"""
    }
]
