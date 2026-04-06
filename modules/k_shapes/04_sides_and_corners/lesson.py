"""Sides and Corners — Understanding Shape Properties."""

TITLE = "Sides and Corners"

SECTIONS = [
    {
        "title": "What Are Sides?",
        "body": """<p>A <strong>side</strong> is one straight edge of a shape. You can trace your finger along one side.</p>
<svg viewBox="0 0 520 220" style="width:100%;max-width:520px;height:auto;display:block;margin:16px auto;">
  <!-- Circle — centered at x=87 -->
  <circle cx="87" cy="90" r="55" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3"/>
  <text x="87" y="95" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>no edges</text>
  <text x="87" y="200" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>0 sides</text>

  <!-- Triangle — centered at x=260 -->
  <polygon points="260,30 315,140 205,140" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <text x="220" y="50" font-size='12' fill='#ef4444' font-weight='bold'>side 1</text>
  <text x="300" y="100" font-size='12' fill='#ef4444' font-weight='bold'>side 2</text>
  <text x="260" y="165" text-anchor='middle' font-size='12' fill='#ef4444' font-weight='bold'>side 3</text>
  <text x="260" y="200" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>3 sides</text>

  <!-- Square — centered at x=433 -->
  <rect x="378" y="35" width="110" height="110" fill='#22c55e30' stroke='#22c55e' stroke-width="3" rx='4'/>
  <text x="433" y="25" text-anchor='middle' font-size='12' fill='#22c55e' font-weight='bold'>top</text>
  <text x="503" y="95" font-size='12' fill='#22c55e' font-weight='bold'>right</text>
  <text x="433" y="162" text-anchor='middle' font-size='12' fill='#22c55e' font-weight='bold'>bottom</text>
  <text x="363" y="95" font-size='12' fill='#22c55e' font-weight='bold' text-anchor='end'>left</text>
  <text x="433" y="200" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>4 sides</text>
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
<svg viewBox="0 0 480 210" style="width:100%;max-width:480px;height:auto;display:block;margin:16px auto;">
  <!-- Circle (no corners) — centered at x=80 -->
  <circle cx="80" cy="85" r="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3"/>
  <text x="80" y="155" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>0 corners</text>

  <!-- Triangle (3 corners) — centered at x=240 -->
  <polygon points="210,135 210,35 280,135" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="210" cy="135" r="6" fill='#ef4444'/>
  <circle cx="210" cy="35" r="6" fill='#ef4444'/>
  <circle cx="280" cy="135" r="6" fill='#ef4444'/>
  <text x="240" y="165" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>3 corners</text>

  <!-- Square (4 corners) — centered at x=400 -->
  <rect x="350" y="35" width="100" height="100" fill='#22c55e30' stroke='#22c55e' stroke-width="3" rx='4'/>
  <circle cx="350" cy="35" r="6" fill='#22c55e'/>
  <circle cx="450" cy="35" r="6" fill='#22c55e'/>
  <circle cx="450" cy="135" r="6" fill='#22c55e'/>
  <circle cx="350" cy="135" r="6" fill='#22c55e'/>
  <!-- Right angle indicators -->
  <rect x="350" y="35" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="440" y="35" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="440" y="125" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="350" y="125" width="10" height="10" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <text x="400" y="165" text-anchor='middle' font-size='12' fill='currentColor' font-weight='bold'>4 corners (right angles)</text>
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
<svg viewBox="0 0 420 300" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <!-- Right angle example -->
  <text x="210" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Right Angle (90 degrees)</text>
  <line x1="80" y1="100" x2="160" y2="100" stroke='#22c55e' stroke-width="3"/>
  <line x1="80" y1="100" x2="80" y2="45" stroke='#22c55e' stroke-width="3"/>
  <rect x="80" y="80" width="15" height="15" fill='none' stroke='#22c55e' stroke-width="2" rx='4'/>
  <text x="100" y="72" font-size='12' fill='#22c55e' font-weight='bold'>90 degrees</text>

  <!-- Shapes with right angles -->
  <text x="210" y="150" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Shapes with Right Angles:</text>

  <!-- Square — centered at x=70 -->
  <rect x="40" y="168" width="60" height="60" fill='#22c55e30' stroke='#22c55e' stroke-width="2" rx='4'/>
  <rect x="40" y="168" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="92" y="168" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="92" y="220" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <rect x="40" y="220" width="8" height="8" fill='none' stroke='#22c55e' stroke-width="1.5"/>
  <text x="70" y="248" text-anchor='middle' font-size='12' fill='currentColor' font-weight='bold'>Square</text>
  <text x="70" y="263" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(4 right angles)</text>

  <!-- Rectangle — centered at x=210 -->
  <rect x="165" y="168" width="90" height="60" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2" rx='4'/>
  <rect x="165" y="168" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="247" y="168" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="247" y="220" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="165" y="220" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="210" y="248" text-anchor='middle' font-size='12' fill='currentColor' font-weight='bold'>Rectangle</text>
  <text x="210" y="263" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(4 right angles)</text>

  <!-- Triangle — centered at x=350 -->
  <polygon points="320,228 320,168 380,228" fill='#ef444450' stroke='#ef4444' stroke-width="2"/>
  <text x="350" y="248" text-anchor='middle' font-size='12' fill='currentColor' font-weight='bold'>Triangle</text>
  <text x="350" y="263" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(usually no right angles)</text>
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
