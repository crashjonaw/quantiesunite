TITLE = "Measuring Angles with a Protractor"

SECTIONS = [
    {
        "title": "What is a Protractor?",
        "body": """
<p>A <strong>protractor</strong> is a semicircular tool marked with degree measurements from \\(0°\\) to \\(180°\\). It helps us measure angles precisely using these degree markings.</p>

<div class='concept-box'>
  <p><strong>Key parts of a protractor:</strong></p>
  <ul style='list-style-type: none; padding: 0;'>
    <li>🎯 <strong>Center point (dot):</strong> Marks the vertex of the angle you're measuring</li>
    <li>📏 <strong>Baseline:</strong> The straight edge (0° line) that aligns with one ray of the angle</li>
    <li>📊 <strong>Degree marks:</strong> Numbers from 0° to 180° around the curved edge</li>
    <li>🔄 <strong>Two scales:</strong> Inner scale (going one direction) and outer scale (going the other direction)</li>
  </ul>
</div>

<div class='warning-box'>
  <p><strong>Why two scales?</strong> The two sets of numbers let you measure angles from either direction. This gives you flexibility in how you position your protractor.</p>
</div>

<svg viewBox="-15 -15 430 280" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="430" height="280" rx="4" fill="#1e2433"/>
  <!-- Protractor semicircle -->
  <path d="M 80 210 A 120 120 0 0 1 320 210" stroke='#8b949e' stroke-width="3" fill='none'/>
  <!-- Baseline -->
  <line x1="70" y1="210" x2="330" y2="210" stroke='#0969da' stroke-width="2"/>
  <!-- Center dot -->
  <circle cx="200" cy="210" r="4" fill='#ff6b6b'/>
  <!-- Sample angle ray -->
  <line x1="200" y1="210" x2="290" y2="110" stroke='#4f8ef7' stroke-width="2.5"/>
  <!-- Arc showing measurement -->
  <path d="M 260 210 A 60 60 0 0 0 246 140" stroke='#22c55e' stroke-width="2.5" fill='none'/>
  <!-- Tick marks on protractor -->
  <line x1="200" y1="90" x2="200" y2="97" stroke='#8b949e' stroke-width="1.5"/>
  <!-- Labels -->
  <text x="62" y="232" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>0°</text>
  <text x="324" y="232" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>0°</text>
  <text x="200" y="82" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold' text-anchor='middle'>90°</text>
  <text x="200" y="245" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle' font-weight='bold'>Centre point</text>
  <text x="298" y="105" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>~50°</text>
</svg>

<div class='worked-example'>
  <p><strong>Remember:</strong> A protractor measures angles up to 180°. Since a straight line = 180°, a protractor is shaped like a semicircle (half circle).</p>
</div>
        """
    },
    {
        "title": "Step-by-Step: How to Measure an Angle",
        "body": """
<div class='worked-example'>
  <p><strong>Step 1: Place the center point at the vertex</strong></p>
  <p>Align the small dot or hole in the center of your protractor with the vertex (corner point) of the angle. The vertex is where the two rays meet.</p>
</div>

<div class='worked-example'>
  <p><strong>Step 2: Align the baseline with one ray</strong></p>
  <p>Place the straight edge (baseline) of the protractor along one ray of the angle. Make sure the \\(0°\\) mark on the baseline lines up with this ray. Don't let it slip!</p>
</div>

<div class='worked-example'>
  <p><strong>Step 3: Find where the other ray crosses</strong></p>
  <p>Look at where the second ray of the angle intersects with the curved edge of the protractor. Trace along the arc of the protractor to find this crossing point.</p>
</div>

<div class='worked-example'>
  <p><strong>Step 4: Read the correct scale</strong></p>
  <p>Look at the number on the protractor where the second ray crosses. <strong>Use the same scale</strong> as the \\(0°\\) mark you aligned with in Step 2. If you aligned with the inner \\(0°\\), use the inner numbers. If you aligned with the outer \\(0°\\), use the outer numbers.</p>
</div>

<svg viewBox="-15 -15 380 310" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="380" height="310" rx="4" fill="#1e2433"/>
  <!-- Protractor -->
  <path d="M 50 220 A 125 125 0 0 1 300 220" stroke='#8b949e' stroke-width="2" fill='none'/>
  <!-- Baseline -->
  <line x1="50" y1="220" x2="300" y2="220" stroke='#8b949e' stroke-width="1.5"/>
  <!-- First ray (baseline) -->
  <line x1="175" y1="220" x2="310" y2="220" stroke='#0969da' stroke-width="3"/>
  <!-- Second ray at 60 degrees -->
  <line x1="175" y1="220" x2="240" y2="107" stroke='#4f8ef7' stroke-width="3"/>
  <!-- Arc -->
  <path d="M 240 220 A 65 65 0 0 0 208 135" stroke='#22c55e' stroke-width="2.5" fill='none'/>
  <!-- Center point -->
  <circle cx="175" cy="220" r="4" fill='#ff6b6b'/>
  <!-- Annotations -->
  <text x="250" y="245" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>0° mark</text>
  <text x="250" y="105" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>Second ray</text>
  <text x="250" y="142" fill='currentColor' font-family='system-ui, sans-serif' font-size='13' font-weight='bold'>60°</text>
</svg>

<div class='success-box'>
  <p><strong>Pro tip:</strong> Before using the protractor, <strong>estimate</strong> whether the angle is acute (less than 90°) or obtuse (more than 90°). This helps you choose the correct scale if you're unsure!</p>
</div>
        """
    },
    {
        "title": "Common Mistakes to Avoid",
        "body": """
<div class='warning-box'>
  <p><strong>Mistake 1: Forgetting to place the center point at the vertex</strong></p>
  <p>If the dot is even slightly off, your measurement will be wrong. Double-check that the center point is exactly at the corner where the two rays meet.</p>
</div>

<div class='warning-box'>
  <p><strong>Mistake 2: Not aligning the baseline properly with 0°</strong></p>
  <p>The straight edge must be perfectly aligned with one ray, and the 0° mark must line up with that ray. If it's crooked, the angle will measure incorrectly.</p>
</div>

<div class='warning-box'>
  <p><strong>Mistake 3: Using the wrong scale</strong></p>
  <p>Protractors have two sets of numbers! Once you choose which 0° to use, stick with that same scale for your reading. Don't mix inner and outer numbers.</p>
</div>

<div class='warning-box'>
  <p><strong>Mistake 4: Reading the protractor from the wrong end</strong></p>
  <p>If you measure from the wrong 0° mark, you might get \\(180° - \\text{your angle}\\) instead of the actual angle. Always check that you're using the scale that started at your baseline ray.</p>
</div>

<div class='success-box'>
  <p><strong>The Estimation Check:</strong> After measuring, ask yourself: Does this make sense? Is the angle really that size? If you measured 120° but it looks acute, something went wrong!</p>
</div>
        """
    },
    {
        "title": "Practice: Estimate First, Then Measure",
        "body": """
<p>Before pulling out your protractor, <strong>always estimate</strong> the angle size. This helps you verify your final measurement makes sense.</p>

<div class='worked-example'>
  <p><strong>Estimation steps:</strong></p>
  <ol>
    <li>Look at the angle</li>
    <li>Compare it mentally to a right angle (90°, the corner of a square)</li>
    <li>Is it smaller than a right angle? → Acute (estimate: 30°, 45°, 60°, 80°...)</li>
    <li>Is it the same as a right angle? → Right (estimate: 90°)</li>
    <li>Is it wider than a right angle but not a straight line? → Obtuse (estimate: 100°, 120°, 150°...)</li>
  </ol>
</div>

<svg viewBox="-15 -15 430 280" style="width:100%;max-width:440px;height:auto;display:block;margin:16px auto;background:#1e2433;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <rect x="-15" y="-15" width="430" height="280" rx="4" fill="#1e2433"/>
  <!-- Right angle reference -->
  <g transform='translate(70, 160)'>
    <line x1="0" y1="0" x2="60" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="0" y2="-60" stroke='#4f8ef7' stroke-width="2"/>
    <rect x="0" y="-18" width="18" height="18" fill='none' stroke='#22c55e' stroke-width="2"/>
    <circle cx="0" cy="0" r="3" fill='#ff6b6b'/>
    <text x="0" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle' font-weight='bold'>Reference: 90°</text>
  </g>

  <!-- Acute angle example -->
  <g transform='translate(210, 160)'>
    <line x1="0" y1="0" x2="60" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="46" y2="-39" stroke='#0969da' stroke-width="2.5"/>
    <path d="M 30 0 A 30 30 0 0 0 23 -19" stroke='#22c55e' stroke-width="2" fill='none'/>
    <circle cx="0" cy="0" r="3" fill='#ff6b6b'/>
    <text x="38" y="-18" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>~40°</text>
    <text x="0" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>Acute</text>
  </g>

  <!-- Obtuse angle example -->
  <g transform='translate(350, 160)'>
    <line x1="0" y1="0" x2="60" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="-39" y2="-46" stroke='#ff6b6b' stroke-width="2.5"/>
    <path d="M 30 0 A 30 30 0 0 1 -19 -23" stroke='#22c55e' stroke-width="2" fill='none'/>
    <circle cx="0" cy="0" r="3" fill='#ff6b6b'/>
    <text x="-10" y="-32" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' font-weight='bold'>~130°</text>
    <text x="0" y="25" fill='currentColor' font-family='system-ui, sans-serif' font-size='11' text-anchor='middle'>Obtuse</text>
  </g>

  <text x="200" y="230" fill='currentColor' font-family='system-ui, sans-serif' font-size='12' text-anchor='middle'>Compare any angle to the 90° reference</text>
</svg>

<div class='success-box'>
  <p><strong>Your measurement is correct if:</strong> It matches your estimate (within about 5°), and it makes sense compared to your reference right angle!</p>
</div>
        """
    }
]
