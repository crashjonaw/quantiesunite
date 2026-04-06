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

<svg viewBox="0 0 400 250" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Protractor semicircle -->
  <path d="M 80 200 L 320 200 A 120 120 0 0 1 80 200" stroke='#8b949e' stroke-width="3" fill='none'/>
  <!-- Baseline -->
  <line x1="80" y1="200" x2="320" y2="200" stroke='#0969da' stroke-width="2"/>
  <!-- Center dot -->
  <circle cx="200" cy="200" r="3" fill='#ff6b6b'/>
  <!-- Sample angle ray -->
  <line x1="200" y1="200" x2="290" y2="100" stroke='#4f8ef7' stroke-width="2"/>
  <!-- Arc showing measurement -->
  <path d="M 260 200 A 60 60 0 0 0 241 124" stroke='#22c55e' stroke-width="2" fill='none'/>
  <!-- Labels -->
  <text x="75" y="225" fill='currentColor' font-size='12' font-weight='bold'>0°</text>
  <text x="320" y="225" fill='currentColor' font-size='12' font-weight='bold'>0°</text>
  <text x="200" y="100" fill='currentColor' font-size='12' font-weight='bold'>180°</text>
  <text x="200" y="220" fill='#ff6b6b' font-size='12' text-anchor='middle' font-weight='bold'>Center point</text>
  <text x="270" y="90" fill='#22c55e' font-size='11' font-weight='bold'>~50°</text>
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

<svg viewBox="0 0 350 280" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Protractor -->
  <path d="M 50 200 L 300 200 A 125 125 0 0 1 50 200" stroke='#8b949e' stroke-width="2" fill='none'/>
  <!-- First ray (baseline) -->
  <line x1="175" y1="200" x2="300" y2="200" stroke='#0969da' stroke-width="3"/>
  <!-- Second ray at 60 degrees -->
  <line x1="175" y1="200" x2="239" y2="92" stroke='#4f8ef7' stroke-width="3"/>
  <!-- Arc -->
  <path d="M 240 200 A 65 65 0 0 0 200 115" stroke='#22c55e' stroke-width="2" fill='none'/>
  <!-- Center point -->
  <circle cx="175" cy="200" r="3" fill='#ff6b6b'/>
  <!-- Annotations -->
  <text x="200" y="225" fill='#0969da' font-size='12' font-weight='bold'>0° mark</text>
  <text x="220" y="110" fill='#4f8ef7' font-size='12' font-weight='bold'>Second ray</text>
  <text x="215" y="85" fill='#22c55e' font-size='13' font-weight='bold'>60°</text>
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

<svg viewBox="-40 -60 400 310" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Right angle reference -->
  <g transform='translate(50, 150)'>
    <line x1="0" y1="0" x2="50" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="0" y2="-50" stroke='#4f8ef7' stroke-width="2"/>
    <rect x="0" y="-25" width="20" height="20" fill='none' stroke='#22c55e' stroke-width="1"/>
    <text x="30" y="-10" fill='currentColor' font-size='11'>Reference: 90°</text>
  </g>

  <!-- Acute angle example -->
  <g transform='translate(200, 150)'>
    <line x1="0" y1="0" x2="50" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="38" y2="-32" stroke='#0969da' stroke-width="2"/>
    <text x="25" y="-15" fill='#0969da' font-size='12'>~40°</text>
  </g>

  <!-- Obtuse angle example -->
  <g transform='translate(200, 50)'>
    <line x1="0" y1="0" x2="50" y2="0" stroke='#8b949e' stroke-width="2"/>
    <line x1="0" y1="0" x2="-32" y2="-38" stroke='#ff6b6b' stroke-width="2"/>
    <text x="0" y="-20" fill='#ff6b6b' font-size='12'>~130°</text>
  </g>

  <text x="150" y="230" fill='currentColor' font-size='12' text-anchor='middle'>Compare any angle to the 90° reference</text>
</svg>

<div class='success-box'>
  <p><strong>Your measurement is correct if:</strong> It matches your estimate (within about 5°), and it makes sense compared to your reference right angle!</p>
</div>
        """
    }
]
