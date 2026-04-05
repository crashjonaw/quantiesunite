"""Triangle and Rectangle — 2D Shapes Concept."""

TITLE = "Triangle and Rectangle"

SECTIONS = [
    {
        "title": "The Triangle — Three Sides, Three Corners",
        "body": """<p>A <strong>triangle</strong> is a shape with <strong>3 sides and 3 corners</strong>. The word 'triangle' comes from 'tri' which means <strong>three</strong>!</p>
<svg viewBox="0 0 500 300" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Tall triangle -->
  <polygon points="80,220 80,60 150,220" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="80" cy="220" r="4" fill='#ef4444'/>
  <circle cx="80" cy="60" r="4" fill='#ef4444'/>
  <circle cx="150" cy="220" r="4" fill='#ef4444'/>
  <text x="80" y="250" text-anchor='middle' font-size='12' fill='#e6edf3'>Tall</text>

  <!-- Flat triangle -->
  <polygon points="220,220 340,220 280,80" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="220" cy="220" r="4" fill='#ef4444'/>
  <circle cx="340" cy="220" r="4" fill='#ef4444'/>
  <circle cx="280" cy="80" r="4" fill='#ef4444'/>
  <text x="280" y="250" text-anchor='middle' font-size='12' fill='#e6edf3'>Flat</text>

  <!-- Wide triangle -->
  <polygon points="370,220 470,220 420,90" fill='#ef444450' stroke='#ef4444' stroke-width="3"/>
  <circle cx="370" cy="220" r="4" fill='#ef4444'/>
  <circle cx="470" cy="220" r="4" fill='#ef4444'/>
  <circle cx="420" cy="90" r="4" fill='#ef4444'/>
  <text x="420" y="250" text-anchor='middle' font-size='12' fill='#e6edf3'>Wide</text>

  <!-- Key fact -->
  <text x="250" y="290" text-anchor='middle' font-size='13' fill='#e6edf3' font-weight='bold'>Always 3 sides  •  Always 3 corners</text>
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
<svg viewBox="0 0 500 300" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Rectangle 1 (vertical orientation) -->
  <rect x="50" y="80" width="80" height="140" fill='#f59e0b30' stroke='#f59e0b' stroke-width="3"/>
  <circle cx="50" cy="80" r="4" fill='#f59e0b'/>
  <circle cx="130" cy="80" r="4" fill='#f59e0b'/>
  <circle cx="130" cy="220" r="4" fill='#f59e0b'/>
  <circle cx="50" cy="220" r="4" fill='#f59e0b'/>
  <!-- Right angle indicators -->
  <rect x="50" y="80" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="122" y="80" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="122" y="212" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="50" y="212" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="90" y="250" text-anchor='middle' font-size='12' fill='#e6edf3'>Tall</text>

  <!-- Rectangle 2 (horizontal orientation) -->
  <rect x="200" y="120" width="140" height="80" fill='#f59e0b30' stroke='#f59e0b' stroke-width="3"/>
  <circle cx="200" cy="120" r="4" fill='#f59e0b'/>
  <circle cx="340" cy="120" r="4" fill='#f59e0b'/>
  <circle cx="340" cy="200" r="4" fill='#f59e0b'/>
  <circle cx="200" cy="200" r="4" fill='#f59e0b'/>
  <!-- Right angle indicators -->
  <rect x="200" y="120" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="332" y="120" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="332" y="192" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <rect x="200" y="192" width="8" height="8" fill='none' stroke='#f59e0b' stroke-width="1.5"/>
  <text x="270" y="250" text-anchor='middle' font-size='12' fill='#e6edf3'>Wide</text>

  <!-- Key fact -->
  <text x="250" y="290" text-anchor='middle' font-size='13' fill='#e6edf3' font-weight='bold'>4 sides (2 long, 2 short)  •  4 right corners</text>
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
<tr style="background:#f9f9f9;">
<td style="padding: 8px;">Corners</td>
<td style="padding: 8px; text-align: center;">3</td>
<td style="padding: 8px; text-align: center;">4</td>
</tr>
<tr>
<td style="padding: 8px;">Equal sides</td>
<td style="padding: 8px; text-align: center;">Not always</td>
<td style="padding: 8px; text-align: center;">Opposite sides equal</td>
</tr>
<tr style="background:#f9f9f9;">
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
