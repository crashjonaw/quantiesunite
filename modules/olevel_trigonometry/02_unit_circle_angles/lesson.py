TITLE = "The Unit Circle and Angle Measurement"

SECTIONS = [
    {
        "title": "Why We Need the Unit Circle: Beyond Right Triangles",
        "body": """
<h3>The Limitation of Right Triangle Trigonometry</h3>
<p>So far, we've only used trigonometry for angles between 0° and 90°. But what about angles greater than 90°? Or negative angles? Or angles representing multiple rotations?</p>

<p>The unit circle is the tool that extends trigonometry to <strong>all</strong> angles, not just acute angles in right triangles.</p>

<h3>Introducing the Unit Circle</h3>

<div class="concept-box">
<p>The <strong>unit circle</strong> is a circle with radius 1 centered at the origin (0, 0) of a coordinate system.</p>
</div>

<svg viewBox="-160 -175 345 360" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; margin:20px auto; display:block;">

  <!-- Circle -->
  <circle cx="0" cy="0" r="100" fill='none' stroke='#4f8ef7' stroke-width="1.5"/>

  <!-- Axes -->
  <line x1="-140" y1="0" x2="140" y2="0" stroke='#30363d' stroke-width="1"/>
  <line x1="0" y1="-140" x2="0" y2="140" stroke='#30363d' stroke-width="1"/>

  <!-- Axis labels -->
  <text x="148" y="5" fill='currentColor' font-size='12'>x</text>
  <text x="5" y="-145" fill='currentColor' font-size='12'>y</text>

  <!-- Radius to 30 degree point -->
  <line x1="0" y1="0" x2="86.6" y2="-50" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Dashed projections -->
  <line x1="86.6" y1="-50" x2="86.6" y2="0" stroke='#e8b04f' stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="86.6" y1="-50" x2="0" y2="-50" stroke='#e8b04f' stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Angle arc -->
  <path d="M 30 0 A 30 30 0 0 0 26 -15" fill='none' stroke='#e8b04f' stroke-width="2"/>
  <text x="36" y="-6" fill='#e8b04f' font-size='14' font-weight='bold'>θ</text>

  <!-- Point on circle -->
  <circle cx="86.6" cy="-50" r="4" fill='#4f8ef7'/>
  <text x="92" y="-58" fill='currentColor' font-size='12'>(cos θ, sin θ)</text>

  <!-- Projection labels -->
  <text x="86.6" y="18" fill='currentColor' font-size='11' text-anchor='middle'>cos θ</text>
  <text x="-30" y="-47" fill='currentColor' font-size='11' text-anchor='middle'>sin θ</text>

  <!-- Key points -->
  <circle cx="100" cy="0" r="3" fill='#4f8ef7'/>
  <text x="100" y="28" fill='currentColor' font-size='11' text-anchor='middle'>(1, 0)</text>

  <circle cx="0" cy="-100" r="3" fill='#4f8ef7'/>
  <text x="20" y="-103" fill='currentColor' font-size='11'>(0, 1)</text>

  <circle cx="-100" cy="0" r="3" fill='#4f8ef7'/>
  <text x="-100" y="28" fill='currentColor' font-size='11' text-anchor='middle'>(-1, 0)</text>

  <circle cx="0" cy="100" r="3" fill='#4f8ef7'/>
  <text x="20" y="115" fill='currentColor' font-size='11'>(0, -1)</text>

  <!-- Radius label -->
  <text x="35" y="-30" fill='#4f8ef7' font-size='12' font-weight='bold'>r = 1</text>
</svg>

<h3>The Key Insight</h3>
<p>When you rotate a radius from the positive x-axis by an angle \\(\\theta\\), the point where it hits the circle has coordinates:</p>

<div class="concept-box">
<p>If a point on the unit circle is at angle \\(\\theta\\), its coordinates are \\((\\cos(\\theta), \\sin(\\theta))\\)</p>
</div>

<p><strong>Why?</strong> Because if you drop a perpendicular from the point to the x-axis, you create a right triangle with hypotenuse 1. The x-coordinate (adjacent/1) is the cosine, and the y-coordinate (opposite/1) is the sine.</p>
"""
    },
    {
        "title": "Angle Measurement: Degrees vs Radians",
        "body": """
<h3>Two Ways to Measure Angles</h3>

<p><strong>Degrees:</strong> The familiar system where a full rotation is 360°.</p>
<p><strong>Radians:</strong> A mathematical system where a full rotation is \\(2\\pi\\) radians.</p>

<h3>Converting Between Them</h3>

<div class="concept-box">
<p>\\(360° = 2\\pi \\text{ radians}\\)</p>
<p>\\(180° = \\pi \\text{ radians}\\)</p>
<p>\\(\\text{Degrees} = \\text{Radians} \\times \\frac{180°}{\\pi}\\)</p>
<p>\\(\\text{Radians} = \\text{Degrees} \\times \\frac{\\pi}{180°}\\)</p>
</div>

<h3>Why Radians?</h3>
<p>Radians are "natural" for mathematics. The arc length on a unit circle with angle \\(\\theta\\) radians is exactly \\(\\theta\\). This simple relationship makes calculus and advanced mathematics much cleaner.</p>

<h3>Key Angles on the Unit Circle</h3>

<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr >
  <th style="padding: 10px;">Degrees</th>
  <th style="padding: 10px;">Radians</th>
  <th style="padding: 10px;">Coordinates (cos, sin)</th>
</tr>
<tr >
  <td style="padding: 10px;">0°</td>
  <td style="padding: 10px;">0</td>
  <td style="padding: 10px;">(1, 0)</td>
</tr>
<tr >
  <td style="padding: 10px;">30°</td>
  <td style="padding: 10px;">\\(\\frac{\\pi}{6}\\)</td>
  <td style="padding: 10px;">(\\(\\frac{\\sqrt{3}}{2}\\), \\(\\frac{1}{2}\\))</td>
</tr>
<tr >
  <td style="padding: 10px;">45°</td>
  <td style="padding: 10px;">\\(\\frac{\\pi}{4}\\)</td>
  <td style="padding: 10px;">(\\(\\frac{\\sqrt{2}}{2}\\), \\(\\frac{\\sqrt{2}}{2}\\))</td>
</tr>
<tr >
  <td style="padding: 10px;">60°</td>
  <td style="padding: 10px;">\\(\\frac{\\pi}{3}\\)</td>
  <td style="padding: 10px;">(\\(\\frac{1}{2}\\), \\(\\frac{\\sqrt{3}}{2}\\))</td>
</tr>
<tr >
  <td style="padding: 10px;">90°</td>
  <td style="padding: 10px;">\\(\\frac{\\pi}{2}\\)</td>
  <td style="padding: 10px;">(0, 1)</td>
</tr>
</table>

<h3>Worked Example: Radian Conversion</h3>

<div class="worked-example">
<p><strong>Convert \\(\\frac{3\\pi}{4}\\) radians to degrees:</strong></p>
<p>\\(\\frac{3\\pi}{4} \\times \\frac{180°}{\\pi} = \\frac{3 \\times 180°}{4} = \\frac{540°}{4} = 135°\\)</p>
</div>
"""
    },
    {
        "title": "Trigonometric Values for All Angles: The ASTC Rule",
        "body": """
<h3>Extending to All Quadrants</h3>
<p>The unit circle extends beyond the first quadrant. In the other quadrants, angles can be greater than 90°, and the trigonometric values can be negative.</p>

<svg viewBox="-155 -155 310 310" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:350px; margin:20px auto; display:block;">

  <!-- Circle -->
  <circle cx="0" cy="0" r="100" fill='none' stroke='#4f8ef7' stroke-width="1.5"/>

  <!-- Axes -->
  <line x1="-135" y1="0" x2="135" y2="0" stroke='#30363d' stroke-width="1"/>
  <line x1="0" y1="-135" x2="0" y2="135" stroke='#30363d' stroke-width="1"/>

  <!-- Quadrant shading (subtle) -->
  <path d="M 0 0 L 100 0 A 100 100 0 0 0 0 -100 Z" fill='#4f8ef7' opacity='0.06'/>
  <path d="M 0 0 L 0 -100 A 100 100 0 0 0 -100 0 Z" fill='#e8b04f' opacity='0.06'/>
  <path d="M 0 0 L -100 0 A 100 100 0 0 0 0 100 Z" fill='#4f8ef7' opacity='0.06'/>
  <path d="M 0 0 L 0 100 A 100 100 0 0 0 100 0 Z" fill='#e8b04f' opacity='0.06'/>

  <!-- Quadrant labels -->
  <text x="50" y="-55" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>I</text>
  <text x="50" y="-38" fill='currentColor' font-size='11' text-anchor='middle'>All +</text>

  <text x="-50" y="-55" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>II</text>
  <text x="-50" y="-38" fill='currentColor' font-size='11' text-anchor='middle'>Sin +</text>

  <text x="-50" y="45" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>III</text>
  <text x="-50" y="62" fill='currentColor' font-size='11' text-anchor='middle'>Tan +</text>

  <text x="50" y="45" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>IV</text>
  <text x="50" y="62" fill='currentColor' font-size='11' text-anchor='middle'>Cos +</text>

  <!-- Sample points on circle at 45 degrees in each quadrant -->
  <circle cx="70.7" cy="-70.7" r="4" fill='#4f8ef7'/>
  <circle cx="-70.7" cy="-70.7" r="4" fill='#e8b04f'/>
  <circle cx="-70.7" cy="70.7" r="4" fill='#4f8ef7'/>
  <circle cx="70.7" cy="70.7" r="4" fill='#e8b04f'/>

  <!-- Radii to sample points -->
  <line x1="0" y1="0" x2="70.7" y2="-70.7" stroke='#4f8ef7' stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="0" y1="0" x2="-70.7" y2="-70.7" stroke='#e8b04f' stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="0" y1="0" x2="-70.7" y2="70.7" stroke='#4f8ef7' stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="0" y1="0" x2="70.7" y2="70.7" stroke='#e8b04f' stroke-width="1" stroke-dasharray="4,3"/>
</svg>

<h3>The ASTC Rule (or "All Students Take Calculus")</h3>

<div class="concept-box">
<p><strong>Quadrant I (0° to 90°):</strong> All trig functions are positive</p>
<p><strong>Quadrant II (90° to 180°):</strong> Only sine (and cosecant) are positive</p>
<p><strong>Quadrant III (180° to 270°):</strong> Only tangent (and cotangent) are positive</p>
<p><strong>Quadrant IV (270° to 360°):</strong> Only cosine (and secant) are positive</p>
</div>

<h3>Why This Matters</h3>
<p>When you use inverse trig functions, you need to consider which quadrant your angle is in. The calculator gives you one answer, but there may be multiple correct angles.</p>

<h3>Worked Example: Finding All Solutions</h3>

<div class="worked-example">
<p><strong>Find \\(\\sin(150°)\\) using reference angles:</strong></p>

<p>150° is in Quadrant II. The reference angle is \\(180° - 150° = 30°\\)</p>

<p>In Quadrant II, sine is positive, so:</p>
<p>\\(\\sin(150°) = \\sin(30°) = \\frac{1}{2}\\)</p>

<p><strong>Find \\(\\cos(150°)\\):</strong></p>
<p>In Quadrant II, cosine is negative, so:</p>
<p>\\(\\cos(150°) = -\\cos(30°) = -\\frac{\\sqrt{3}}{2}\\)</p>
</div>

<h3>Worked Example: Solving \\(\\sin(\\theta) = 0.5\\)</h3>

<div class="worked-example">
<p>In the range [0°, 360°], find all angles where \\(\\sin(\\theta) = 0.5\\)</p>

<p><strong>Step 1:</strong> Identify the reference angle where sine equals 0.5.</p>
<p>\\(\\sin(30°) = 0.5\\), so the reference angle is 30°</p>

<p><strong>Step 2:</strong> Find where sine is positive (Quadrants I and II).</p>
<p>- Quadrant I: \\(\\theta = 30°\\)</p>
<p>- Quadrant II: \\(\\theta = 180° - 30° = 150°\\)</p>

<p><strong>Answer:</strong> \\(\\theta = 30°\\) or \\(\\theta = 150°\\)</p>
</div>
"""
    },
    {
        "title": "Applications: Modeling Periodic Phenomena",
        "body": """
<h3>Periodic Functions and Real Life</h3>
<p>Many natural phenomena repeat in cycles: seasons, tides, sound waves, and electrical signals. These are modeled using sinusoidal functions (sine and cosine functions).</p>

<h3>The General Sinusoidal Function</h3>

<div class="concept-box">
<p>\\(y = A\\sin(B(x - C)) + D\\)</p>
<p>Or equivalently: \\(y = A\\sin(Bx - C) + D\\)</p>

<p>Where:</p>
<ul>
  <li>\\(A\\) = amplitude (height of oscillation)</li>
  <li>\\(B\\) = frequency factor</li>
  <li>\\(C\\) = phase shift (horizontal shift)</li>
  <li>\\(D\\) = vertical shift (centerline)</li>
  <li>Period \\(= \\frac{2\\pi}{B}\\)</li>
</ul>
</div>

<h3>Understanding Each Parameter</h3>

<p><strong>Amplitude (\\(A\\)):</strong> The distance from the centerline to the peak. If \\(|A| = 2\\), the function oscillates 2 units above and below the centerline.</p>

<p><strong>Period (\\(T = \\frac{2\\pi}{B}\\)):</strong> How long it takes for the pattern to repeat. If the period is 12, the function repeats every 12 units.</p>

<p><strong>Vertical Shift (\\(D\\)):</strong> The centerline around which the function oscillates. If \\(D = 5\\), the centerline is at \\(y = 5\\).</p>

<h3>Worked Example: Temperature Modeling</h3>

<div class="worked-example">
<p><strong>Problem:</strong> The average monthly temperature varies from 5°C in winter to 25°C in summer. Model this with a sinusoidal function where \\(t = 0\\) represents January.</p>

<p><strong>Step 1: Find \\(D\\) (vertical shift)</strong></p>
<p>Average of max and min: \\(D = \\frac{25 + 5}{2} = 15°C\\)</p>

<p><strong>Step 2: Find \\(A\\) (amplitude)</strong></p>
<p>Half the difference: \\(A = \\frac{25 - 5}{2} = 10°C\\)</p>

<p><strong>Step 3: Find \\(B\\) (frequency)</strong></p>
<p>The pattern repeats every 12 months: Period \\(= 12 = \\frac{2\\pi}{B}\\)</p>
<p>\\(B = \\frac{2\\pi}{12} = \\frac{\\pi}{6}\\)</p>

<p><strong>Step 4: Find \\(C\\) (phase shift)</strong></p>
<p>The maximum should occur in summer (July, \\(t = 6\\)). For a sine function, max occurs when the argument equals \\(\\pi/2\\):</p>
<p>\\(\\frac{\\pi}{6}(6) - C = \\frac{\\pi}{2}\\)</p>
<p>\\(C = \\pi - \\frac{\\pi}{2} = \\frac{\\pi}{2}\\)</p>

<p><strong>Final equation:</strong></p>
<p>\\(T(t) = 15 + 10\\sin\\left(\\frac{\\pi}{6}\\left(t - 3\\right)\\right)\\)</p>

<p><strong>Verification:</strong> When \\(t = 3\\) (April), this should be near average (15°C): \\(T(3) = 15°C\\) ✓</p>
</div>
"""
    }
]
