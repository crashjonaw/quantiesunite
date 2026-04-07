"""Triangle and Rectangle — 2D Shapes Concept."""

TITLE = "Triangle and Rectangle"

SECTIONS = [
    {
        "title": "The Triangle — Three Sides, Three Corners",
        "body": """<p>A <strong>triangle</strong> is a shape with <strong>3 sides and 3 corners</strong>. The word 'triangle' comes from 'tri' which means <strong>three</strong>!</p>
<svg viewBox="0 0 450 230" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <!-- Tall — centered at x=75 -->
  <polygon points="60,160 60,40 115,160" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="60" cy="160" r="4" fill='#ef4444'/>
  <circle cx="60" cy="40" r="4" fill='#ef4444'/>
  <circle cx="115" cy="160" r="4" fill='#ef4444'/>
  <text x="75" y="190" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Tall</text>

  <!-- Flat — centered at x=225 -->
  <polygon points="170,160 280,160 225,50" fill='#f59e0b50' stroke='#f59e0b' stroke-width="3"/>
  <circle cx="170" cy="160" r="4" fill='#f59e0b'/>
  <circle cx="280" cy="160" r="4" fill='#f59e0b'/>
  <circle cx="225" cy="50" r="4" fill='#f59e0b'/>
  <text x="225" y="190" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Flat</text>

  <!-- Wide — centered at x=375 -->
  <polygon points="325,160 425,160 375,60" fill='#a855f750' stroke='#a855f7' stroke-width="3"/>
  <circle cx="325" cy="160" r="4" fill='#a855f7'/>
  <circle cx="425" cy="160" r="4" fill='#a855f7'/>
  <circle cx="375" cy="60" r="4" fill='#a855f7'/>
  <text x="375" y="190" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Wide</text>

  <!-- Key fact -->
  <text x="225" y="220" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Always 3 sides  •  Always 3 corners</text>
</svg>
<p><strong>Properties of triangles:</strong></p>
<ul>
<li>Always has exactly <strong>3 sides</strong> and <strong>3 corners</strong></li>
<li>Triangles can look very different — tall, flat, wide, or even upside-down</li>
<li>The angles inside a triangle always add up to \\(180°\\) (a fun fact for later!)</li>
</ul>
<div class="success-box">
<strong>Why are triangles so strong?</strong> Triangles are one of the strongest shapes in the world. They're used in bridges, roof trusses, and skyscrapers because they can't be bent or squashed easily!
</div>
"""
    },
    {
        "title": "The Rectangle — Four Sides, Two Pairs Equal",
        "body": """<p>A <strong>rectangle</strong> is a shape with <strong>4 sides and 4 right corners</strong>. But unlike a square, its sides are <strong>not all equal</strong> — it has <strong>2 long sides and 2 short sides</strong>.</p>
<svg viewBox="0 0 420 250" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <!-- Tall Rectangle — centered at x=105 -->
  <rect x="60" y="30" width="90" height="150" fill='#f59e0b30' stroke='#f59e0b' stroke-width="3" rx='4'/>
  <circle cx="60" cy="30" r="4" fill='#f59e0b'/>
  <circle cx="150" cy="30" r="4" fill='#f59e0b'/>
  <circle cx="150" cy="180" r="4" fill='#f59e0b'/>
  <circle cx="60" cy="180" r="4" fill='#f59e0b'/>
  <!-- Right angle indicators -->
  <rect x="60" y="30" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="142" y="30" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="142" y="172" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="60" y="172" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="105" y="205" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Tall</text>

  <!-- Wide Rectangle — centered at x=310 -->
  <rect x="230" y="60" width="160" height="90" fill='#f59e0b30' stroke='#f59e0b' stroke-width="3" rx='4'/>
  <circle cx="230" cy="60" r="4" fill='#f59e0b'/>
  <circle cx="390" cy="60" r="4" fill='#f59e0b'/>
  <circle cx="390" cy="150" r="4" fill='#f59e0b'/>
  <circle cx="230" cy="150" r="4" fill='#f59e0b'/>
  <!-- Right angle indicators -->
  <rect x="230" y="60" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="382" y="60" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="382" y="142" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="230" y="142" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="310" y="205" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>Wide</text>

  <!-- Key fact -->
  <text x="210" y="238" text-anchor='middle' font-size='13' fill='currentColor' font-weight='bold'>4 sides (2 long, 2 short)  •  4 right corners</text>
</svg>
<p><strong>Properties of rectangles:</strong></p>
<ul>
<li>Has <strong>4 sides and 4 corners</strong></li>
<li><strong>Opposite sides are equal in length</strong> — the top and bottom are the same, the left and right are the same</li>
<li>All 4 corners are <strong>right angles</strong> (\\(90°\\))</li>
<li>A <strong>square is a special rectangle</strong> where all 4 sides happen to be equal!</li>
</ul>
"""
    },
    {
        "title": "Comparing Triangles and Rectangles",
        "body": """<canvas id="shapeChart2" data-chart='{"type":"bar","data":{"labels":["Triangle","Rectangle"],"datasets":[{"label":"Number of Sides","data":[3,4],"backgroundColor":["#ef4444","#f59e0b"]},{"label":"Number of Corners","data":[3,4],"backgroundColor":["#ef444480","#f59e0b80"]}]},"options":{"indexAxis":"y","plugins":{"title":{"display":true,"text":"Triangle vs Rectangle Properties"}}}}' height="220"></canvas>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
<tr class="formula-box">
<th style="padding: 8px; text-align: left">Property</th>
<th style="padding: 8px; text-align: center;">Triangle</th>
<th style="padding: 8px; text-align: center;">Rectangle</th>
</tr>
<tr>
<td style="padding: 8px;">Sides</td>
<td style="padding: 8px; text-align: center;">3</td>
<td style="padding: 8px; text-align: center;">4</td>
</tr>
<tr style="background:#f9f9f9; color: #1a1a2e;">
<td style="padding: 8px;">Corners</td>
<td style="padding: 8px; text-align: center;">3</td>
<td style="padding: 8px; text-align: center;">4</td>
</tr>
<tr>
<td style="padding: 8px;">Equal sides</td>
<td style="padding: 8px; text-align: center;">Not always</td>
<td style="padding: 8px; text-align: center;">Opposite sides equal</td>
</tr>
<tr style="background:#f9f9f9; color: #1a1a2e;">
<td style="padding: 8px;">Right corners</td>
<td style="padding: 8px; text-align: center;">Not always</td>
<td style="padding: 8px; text-align: center;">Always (4 right angles)</td>
</tr>
</table>
"""
    },
    {
        "title": "Where Do We See Them?",
        "body": """<div class="worked-example">
<strong>Triangles in real life:</strong><br>
🏠 Roof peaks on houses, 🍕 pizza slices, ⛔ yield signs, 🎣 sails on boats, 🏔️ mountains
</div>
<div class="worked-example">
<strong>Rectangles in real life:</strong><br>
📚 Books and notepads, 🪟 windows, 🚪 doors, 📺 TV screens, 📱 phones, 🧱 bricks
</div>
<button class="reveal-btn" data-reveal="real3">▼ Interactive shape hunt!</button>
<div class="reveal-panel" id="real3">
Walk through your home and find:
1. One triangle (or something triangle-shaped)
2. Five rectangles

Take pictures or sketch them! Which shape did you find more of?
</div>
"""
    }
]
