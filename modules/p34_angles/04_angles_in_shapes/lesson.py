TITLE = "Angles in Shapes"

SECTIONS = [
    {
        "title": "Angles in Triangles - The 180° Rule",
        "body": """
<p><strong>Every triangle, no matter its shape, has a special property: all three interior angles always add up to exactly 180°.</strong></p>

<div class='concept-box'>
  <p>If a triangle has angles A, B, and C:</p>
  <p style='text-align: center; font-weight: bold;'>$$A + B + C = 180°$$</p>
  <p><strong>This is true for ALL triangles!</strong></p>
</div>

<svg viewBox="-15 -15 430 260" style="width:100%;max-width:440px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="430" height="260" rx="4" fill="#1e2433"/>
  <!-- Title -->
  <text x="200" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='13' text-anchor='middle' font-weight='bold'>All angles in a triangle = 180°</text>

  <!-- Equilateral triangle (all angles 60°) -->
  <g transform='translate(100, 140)'>
    <polygon points="0,-70 61,35 -61,35" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <!-- Angle arcs -->
    <path d="M -8,-50 A 20 20 0 0 1 8,-50" stroke='#22c55e' stroke-width="2" fill='none'/>
    <path d="M -42,32 A 20 20 0 0 1 -38,18" stroke='#22c55e' stroke-width="2" fill='none'/>
    <path d="M 38,18 A 20 20 0 0 1 42,32" stroke='#22c55e' stroke-width="2" fill='none'/>
    <text x="0" y="-42" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>60°</text>
    <text x="-52" y="18" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>60°</text>
    <text x="52" y="18" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>60°</text>
    <text x="0" y="70" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>Equilateral</text>
  </g>

  <!-- Right triangle (angles 90°, 45°, 45°) -->
  <g transform='translate(300, 140)'>
    <polygon points="-40,35 40,35 -40,-35" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <!-- Right angle symbol -->
    <rect x="-40" y="17" width="18" height="18" fill='none' stroke='#22c55e' stroke-width="2"/>
    <!-- Angle arcs -->
    <path d="M -28,-28 A 18 18 0 0 1 -40,-17" stroke='#22c55e' stroke-width="2" fill='none'/>
    <path d="M 22,35 A 18 18 0 0 0 -28,-28" stroke='#22c55e' stroke-width="0" fill='none'/>
    <text x="-58" y="5" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>45°</text>
    <text x="18" y="28" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>45°</text>
    <text x="-20" y="22" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>90°</text>
    <text x="0" y="70" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>Right Triangle</text>
  </g>
</svg>

<div class='worked-example'>
  <p><strong>Example:</strong> A triangle has angles of 60° and 70°. What is the third angle?</p>
  <p>Third angle = \\(180° - 60° - 70° = \\)<strong>50°</strong></p>
</div>

<div class='success-box'>
  <p><strong>Key fact:</strong> This rule works because any triangle can be shown to be part of a straight line (180°) when you extend its sides. This is a fundamental property of Euclidean geometry!</p>
</div>
        """
    },
    {
        "title": "Types of Triangles by Their Angles",
        "body": """
<p>We can classify triangles based on the types of angles they contain:</p>

<div class='concept-box'>
  <p><strong>Acute Triangle:</strong> All three angles are acute (each less than 90°)</p>
  <p><strong>Right Triangle:</strong> One angle is exactly 90° (a right angle)</p>
  <p><strong>Obtuse Triangle:</strong> One angle is obtuse (between 90° and 180°)</p>
</div>

<svg viewBox="-15 -15 480 240" style="width:100%;max-width:480px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="480" height="240" rx="4" fill="#1e2433"/>

  <!-- Acute triangle - center at x=75 -->
  <g transform='translate(75, 110)'>
    <polygon points="0,-55 50,40 -50,40" fill='none' stroke='#22c55e' stroke-width="2"/>
    <path d="M -6,-38 A 18 18 0 0 1 6,-38" stroke='#22c55e' stroke-width="2" fill='none'/>
    <text x="0" y="-42" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>60°</text>
    <text x="42" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>65°</text>
    <text x="-42" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>55°</text>
    <text x="0" y="75" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>Acute</text>
  </g>

  <!-- Right triangle - center at x=225 (evenly spaced) -->
  <g transform='translate(225, 110)'>
    <polygon points="-40,40 40,40 -40,-30" fill='none' stroke='#0969da' stroke-width="2"/>
    <rect x="-40" y="22" width="18" height="18" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="-22" y="15" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>90°</text>
    <text x="25" y="32" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>45°</text>
    <text x="-52" y="-10" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>45°</text>
    <text x="0" y="75" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>Right</text>
  </g>

  <!-- Obtuse triangle - center at x=375 (evenly spaced) -->
  <g transform='translate(375, 110)'>
    <polygon points="0,-35 45,40 -55,40" fill='none' stroke='#ff6b6b' stroke-width="2"/>
    <text x="0" y="-12" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>120°</text>
    <text x="32" y="28" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>35°</text>
    <text x="-45" y="28" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>25°</text>
    <text x="0" y="75" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>Obtuse</text>
  </g>
</svg>

<div class='worked-example'>
  <p><strong>Quick check:</strong> Can a triangle have two right angles? No! If it had two 90° angles, the third would need to be \\(180° - 90° - 90° = 0°\\), which is impossible. Every triangle has at most one right angle!</p>

</div>
        """
    },
    {
        "title": "Angles in Quadrilaterals - The 360° Rule",
        "body": """
<p><strong>Every quadrilateral (4-sided shape) has interior angles that always add up to exactly 360°.</strong></p>

<div class='concept-box'>
  <p>If a quadrilateral has angles A, B, C, and D:</p>
  <p style='text-align: center; font-weight: bold;'>$$A + B + C + D = 360°$$</p>
  <p><strong>This is true for all quadrilaterals — squares, rectangles, trapezoids, parallelograms, and any other 4-sided shape!</strong></p>
</div>

<svg viewBox="-15 -15 430 240" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="430" height="240" rx="4" fill="#1e2433"/>
  <!-- Title -->
  <text x="200" y="22" fill='currentColor' font-family='system-ui, sans-serif' font-size='13' text-anchor='middle' font-weight='bold'>All angles in a quadrilateral = 360°</text>

  <!-- Square (all 90°) - centered at x=100 -->
  <g transform='translate(65, 75)'>
    <rect x="0" y="0" width="70" height="70" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <!-- Right angle symbols -->
    <rect x="0" y="0" width="12" height="12" fill='none' stroke='#22c55e' stroke-width="1.5"/>
    <rect x="58" y="0" width="12" height="12" fill='none' stroke='#22c55e' stroke-width="1.5"/>
    <rect x="58" y="58" width="12" height="12" fill='none' stroke='#22c55e' stroke-width="1.5"/>
    <rect x="0" y="58" width="12" height="12" fill='none' stroke='#22c55e' stroke-width="1.5"/>
    <text x="35" y="42" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>90°</text>
    <text x="35" y="105" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Square</text>
  </g>

  <!-- Trapezoid - centered at x=300 -->
  <g transform='translate(265, 75)'>
    <polygon points="0,70 80,70 65,0 15,0" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="22" y="22" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>110°</text>
    <text x="48" y="22" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>70°</text>
    <text x="58" y="62" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>100°</text>
    <text x="10" y="62" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' font-weight='bold'>80°</text>
    <text x="40" y="105" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Trapezoid</text>
  </g>
</svg>

<div class='worked-example'>
  <p><strong>Example:</strong> A quadrilateral has angles of 75°, 85°, and 100°. What is the fourth angle?</p>
  <p>Fourth angle = \\(360° - 75° - 85° - 100° = \\)<strong>100°</strong></p>
</div>

<div class='success-box'>
  <p><strong>Why 360°?</strong> A quadrilateral can be divided into two triangles. Each triangle has angles summing to 180°, so 180° + 180° = 360° for the whole quadrilateral!</p>
</div>
        """
    },
    {
        "title": "Special Quadrilaterals and Regular Polygons",
        "body": """
<p>Some quadrilaterals have special properties because of their angles:</p>

<div class='worked-example'>
  <p><strong>Square:</strong> All 4 angles are 90°</p>
  <p>Each angle = \\(360° \\div 4 = 90°\\)</p>
</div>

<div class='worked-example'>
  <p><strong>Rectangle:</strong> All 4 angles are 90°</p>
  <p>Each angle = \\(360° \\div 4 = 90°\\)</p>
</div>

<div class='worked-example'>
  <p><strong>Rhombus:</strong> Opposite angles are equal (but not necessarily 90°)</p>
  <p>If one angle is 70°, the opposite is also 70°. The other two angles are each \\(180° - 70° = 110°\\)</p>
</div>

<hr style="margin: 20px 0; border: 1px solid #d0d7de;">

<p><strong>Regular Polygons</strong> are shapes where all sides are equal and all angles are equal. Here are some common ones:</p>

<div class='concept-box'>
  <p><strong>Regular triangle (Equilateral):</strong> Each angle = \\(180° \\div 3 = \\)<strong>60°</strong></p>
  <p><strong>Regular quadrilateral (Square):</strong> Each angle = \\(360° \\div 4 = \\)<strong>90°</strong></p>
  <p><strong>Regular pentagon:</strong> Total angles = 540°, so each angle = \\(540° \\div 5 = \\)<strong>108°</strong></p>
  <p><strong>Regular hexagon:</strong> Total angles = 720°, so each angle = \\(720° \\div 6 = \\)<strong>120°</strong></p>
</div>

<svg viewBox="-15 -15 480 240" style="width:100%;max-width:480px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="480" height="240" rx="4" fill="#1e2433"/>

  <!-- Equilateral triangle - center at x=75 -->
  <g transform='translate(75, 105)'>
    <polygon points="0,-50 45,30 -45,30" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <text x="0" y="-32" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>60°</text>
    <text x="0" y="68" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Triangle: 60°</text>
  </g>

  <!-- Regular pentagon - center at x=225 (evenly spaced) -->
  <g transform='translate(225, 105)'>
    <polygon points="0,-45 43,-14 26,37 -26,37 -43,-14" fill='none' stroke='#ff6b6b' stroke-width="2"/>
    <text x="0" y="-28" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>108°</text>
    <text x="0" y="68" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Pentagon: 108°</text>
  </g>

  <!-- Regular hexagon - center at x=375 (evenly spaced) -->
  <g transform='translate(375, 105)'>
    <polygon points="0,-45 39,-22 39,22 0,45 -39,22 -39,-22" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="0" y="-28" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>120°</text>
    <text x="0" y="68" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Hexagon: 120°</text>
  </g>
</svg>

<div class='success-box'>
  <p><strong>Pattern:</strong> As a regular polygon gets more sides, each interior angle gets larger and the shape gets closer to a circle (which has no angles!).</p>
</div>
        """
    }
]
