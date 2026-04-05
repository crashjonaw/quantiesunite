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

<svg viewBox="-60 -70 470 350" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Equilateral triangle (all angles 60°) -->
  <g transform='translate(80, 150)'>
    <polygon points="0,-60 52,30 -52,30" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <text x="0" y="-20" fill='#0969da' font-size='13' text-anchor='middle' font-weight='bold'>60°</text>
    <text x="40" y="20" fill='#0969da' font-size='13' font-weight='bold'>60°</text>
    <text x="-40" y="20" fill='#0969da' font-size='13' font-weight='bold'>60°</text>
    <text x="0" y="65" fill='#24292f' font-size='11' text-anchor='middle'>Equilateral</text>
  </g>

  <!-- Right triangle (angles 90°, 45°, 45°) -->
  <g transform='translate(240, 150)'>
    <polygon points="0,0 50,0 0,-50" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <rect x="0" y="-20" width="15" height="15" fill='none' stroke='#22c55e' stroke-width="1"/>
    <text x="15" y="-10" fill='#22c55e' font-size='12' font-weight='bold'>90°</text>
    <text x="25" y="5" fill='#0969da' font-size='13' font-weight='bold'>45°</text>
    <text x="0" y="-20" fill='#0969da' font-size='13' font-weight='bold'>45°</text>
    <text x="20" y="65" fill='#24292f' font-size='11' text-anchor='middle'>Right Triangle</text>
  </g>

  <text x="175" y="30" fill='#24292f' font-size='13' text-anchor='middle' font-weight='bold'>All angles = 180°</text>
</svg>

<div class='worked-example'>
  <p><strong>Example:</strong> A triangle has angles of 60° and 70°. What is the third angle?</p>
  <p>Third angle = 180° - 60° - 70° = <strong>50°</strong></p>
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

<svg viewBox="0 0 400 200" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Acute triangle -->
  <g transform='translate(50, 100)'>
    <polygon points="0,-50 45,35 -45,35" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="0" y="-15" fill='#22c55e' font-size='12' text-anchor='middle'>60°</text>
    <text x="30" y="15" fill='#22c55e' font-size='12'>65°</text>
    <text x="-30" y="15" fill='#22c55e' font-size='12'>55°</text>
    <text x="0" y="70" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Acute</text>
  </g>

  <!-- Right triangle -->
  <g transform='translate(190, 100)'>
    <polygon points="0,0 50,0 0,-50" fill='none' stroke='#0969da' stroke-width="2"/>
    <rect x="0" y="-20" width="15" height="15" fill='none' stroke='#0969da' stroke-width="1"/>
    <text x="15" y="-5" fill='#0969da' font-size='12'>90°</text>
    <text x="25" y="5" fill='#0969da' font-size='12'>45°</text>
    <text x="-10" y="-15" fill='#0969da' font-size='12'>45°</text>
    <text x="20" y="70" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Right</text>
  </g>

  <!-- Obtuse triangle -->
  <g transform='translate(330, 100)'>
    <polygon points="0,-30 40,35 -50,35" fill='none' stroke='#ff6b6b' stroke-width="2"/>
    <text x="0" y="-5" fill='#ff6b6b' font-size='12' text-anchor='middle'>120°</text>
    <text x="25" y="15" fill='#ff6b6b' font-size='12'>35°</text>
    <text x="-35" y="15" fill='#ff6b6b' font-size='12'>25°</text>
    <text x="10" y="70" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Obtuse</text>
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

<svg viewBox="0 0 400 220" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Square (all 90°) -->
  <g transform='translate(60, 80)'>
    <rect x="0" y="0" width="60" height="60" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <text x="10" y="20" fill='#0969da' font-size='12'>90°</text>
    <text x="50" y="20" fill='#0969da' font-size='12'>90°</text>
    <text x="50" y="55" fill='#0969da' font-size='12'>90°</text>
    <text x="10" y="55" fill='#0969da' font-size='12'>90°</text>
    <text x="30" y="90" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Square</text>
  </g>

  <!-- Trapezoid -->
  <g transform='translate(220, 80)'>
    <polygon points="0,60 70,60 55,0 15,0" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="10" y="25" fill='#22c55e' font-size='12'>110°</text>
    <text x="55" y="25" fill='#22c55e' font-size='12'>70°</text>
    <text x="55" y="55" fill='#22c55e' font-size='12'>100°</text>
    <text x="10" y="55" fill='#22c55e' font-size='12'>80°</text>
    <text x="35" y="90" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Trapezoid</text>
  </g>

  <text x="200" y="20" fill='#24292f' font-size='13' text-anchor='middle' font-weight='bold'>All angles sum to 360°</text>
</svg>

<div class='worked-example'>
  <p><strong>Example:</strong> A quadrilateral has angles of 75°, 85°, and 100°. What is the fourth angle?</p>
  <p>Fourth angle = 360° - 75° - 85° - 100° = <strong>100°</strong></p>
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
  <p>Each angle = 360° ÷ 4 = 90°</p>
</div>

<div class='worked-example'>
  <p><strong>Rectangle:</strong> All 4 angles are 90°</p>
  <p>Each angle = 360° ÷ 4 = 90°</p>
</div>

<div class='worked-example'>
  <p><strong>Rhombus:</strong> Opposite angles are equal (but not necessarily 90°)</p>
  <p>If one angle is 70°, the opposite is also 70°. The other two angles are each \\(180° - 70° = 110°\\)</p>
</div>

<hr style="margin: 20px 0; border: 1px solid #d0d7de;">

<p><strong>Regular Polygons</strong> are shapes where all sides are equal and all angles are equal. Here are some common ones:</p>

<div class='concept-box'>
  <p><strong>Regular triangle (Equilateral):</strong> Each angle = 180° ÷ 3 = <strong>60°</strong></p>
  <p><strong>Regular quadrilateral (Square):</strong> Each angle = 360° ÷ 4 = <strong>90°</strong></p>
  <p><strong>Regular pentagon:</strong> Total angles = 540°, so each angle = 540° ÷ 5 = <strong>108°</strong></p>
  <p><strong>Regular hexagon:</strong> Total angles = 720°, so each angle = 720° ÷ 6 = <strong>120°</strong></p>
</div>

<svg viewBox="0 0 350 220" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Equilateral triangle -->
  <g transform='translate(50, 120)'>
    <polygon points="0,-50 45,30 -45,30" fill='none' stroke='#4f8ef7' stroke-width="2"/>
    <text x="0" y="70" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Triangle: 60°</text>
  </g>

  <!-- Regular hexagon -->
  <g transform='translate(170, 110)'>
    <polygon points="30,-40 50,-20 50,20 30,40 -30,40 -50,20 -50,-20 -30,-40" fill='none' stroke='#22c55e' stroke-width="2"/>
    <text x="0" y="75" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Hexagon: 120°</text>
  </g>

  <!-- Regular pentagon -->
  <g transform='translate(290, 120)'>
    <polygon points="0,-45 43,-14 26,37 -26,37 -43,-14" fill='none' stroke='#ff6b6b' stroke-width="2"/>
    <text x="0" y="70" fill='#24292f' font-size='11' text-anchor='middle' font-weight='bold'>Pentagon: 108°</text>
  </g>
</svg>

<div class='success-box'>
  <p><strong>Pattern:</strong> As a regular polygon gets more sides, each interior angle gets larger and the shape gets closer to a circle (which has no angles!).</p>
</div>
        """
    }
]
