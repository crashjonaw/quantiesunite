TITLE = "Arc Length and Sector Area: Measuring Parts of a Circle"

SECTIONS = [
    {
        "title": "Understanding Central Angle and Its Role",
        "body": """
<div class="concept-box">
<p><strong>Central Angle:</strong> An angle formed by two radii, with its vertex at the center of the circle.</p>
</div>

<p>The central angle tells us what <strong>fraction</strong> of the circle we're working with. A full circle has a central angle of 360° (or 2π radians).</p>

<h4>Central Angle in Degrees vs Radians</h4>
<ul>
<li><strong>Full circle:</strong> 360° = 2π radians</li>
<li><strong>Semicircle:</strong> 180° = π radians</li>
<li><strong>Quarter circle:</strong> 90° = π/2 radians</li>
</ul>

<svg width="380" height="340" viewBox="0 0 380 340" class="formula-box">
  <circle cx="175" cy="155" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="155" r="4" fill='currentColor'/>
  <line x1="175" y1="155" x2="275" y2="155" stroke='#f85149' stroke-width="2"/>
  <line x1="175" y1="155" x2="218" y2="79" stroke='#f85149' stroke-width="2"/>
  <path d="M 275 155 A 100 100 0 0 0 218 79" fill='none' stroke='#a371f7' stroke-width="3"/>
  <text x="253" y="135" fill='#a371f7' font-size='16' font-family='sans-serif' font-weight='bold'>\u03b8</text>
  <text x="240" y="108" fill='#f85149' font-size='11' font-family='sans-serif'>Radius</text>
  <text x="178" y="95" fill='#f85149' font-size='11' font-family='sans-serif'>Radius</text>
  <path d="M 200 160 A 30 30 0 0 0 195 130" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="210" y="148" fill='#a371f7' font-size='11' font-family='sans-serif'>Central</text>
  <text x="215" y="163" fill='#a371f7' font-size='11' font-family='sans-serif'>Angle</text>
  <text x="190" y="325" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>The central angle determines what fraction of the circle we have</text>
</svg>

<h4>Key Insight: Fractions of a Circle</h4>
<p>If the central angle is θ degrees out of 360°, then:</p>
<ul>
<li><strong>Arc length</strong> is θ/360 of the full circumference</li>
<li><strong>Sector area</strong> is θ/360 of the full area</li>
</ul>

<p style="text-align: center; margin-top: 16px;"><strong>Fraction of circle = θ/360 (when θ is in degrees)</strong></p>
"""
    },
    {
        "title": "Arc Length Formula: How Far Around?",
        "body": """
<h4>Arc Length Formula (Degrees)</h4>

<p>An arc is just a portion of the circumference. To find its length, we multiply the full circumference by the fraction of the circle it represents:</p>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(\\text{Arc length} = \\frac{\\theta}{360} \\times 2\\pi r = \\frac{\\theta \\pi r}{180}\\)</p>

<p style="margin-top: 16px;"><strong>Where:</strong></p>
<ul>
<li>θ = central angle in degrees</li>
<li>r = radius</li>
</ul>

<h4>Arc Length Formula (Radians)</h4>

<p>If the angle is in radians, the formula is even simpler:</p>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(s = r\\theta\\)</p>

<p style="margin-top: 16px;"><strong>Where:</strong></p>
<ul>
<li>s = arc length</li>
<li>r = radius</li>
<li>θ = central angle in radians</li>
</ul>

<div class="worked-example">
<h5>Example 1: Arc Length in Degrees</h5>
<p>A circle has radius 6 cm. Find the arc length of a sector with central angle 60°.</p>
<p><strong>Solution:</strong></p>
<p>Arc length \\(= \\frac{60}{360} \\times 2\\pi(6) = \\frac{1}{6} \\times 12\\pi =\\) <strong>\\(2\\pi\\) cm \\(\\approx 6.28\\) cm</strong></p>
</div>

<div class="worked-example">
<h5>Example 2: Arc Length in Radians</h5>
<p>A circle has radius 8 cm. Find the arc length when the central angle is π/4 radians.</p>
<p><strong>Solution:</strong></p>
<p>Arc length \\(= r \\times \\theta = 8 \\times \\frac{\\pi}{4} =\\) <strong>\\(2\\pi\\) cm \\(\\approx 6.28\\) cm</strong></p>
</div>

<svg width="380" height="280" viewBox="0 0 380 280" class="formula-box">
  <circle cx="170" cy="140" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="170" cy="140" r="3" fill='currentColor'/>
  <line x1="170" y1="140" x2="260" y2="140" stroke='#f85149' stroke-width="2"/>
  <line x1="170" y1="140" x2="215" y2="54" stroke='#f85149' stroke-width="2"/>
  <path d="M 260 140 A 90 90 0 0 0 215 54" fill='none' stroke='#a371f7' stroke-width="3"/>
  <text x="290" y="95" fill='#a371f7' font-size='13' font-family='sans-serif' font-weight='bold'>Arc</text>
  <text x="290" y="112" fill='#a371f7' font-size='13' font-family='sans-serif' font-weight='bold'>length</text>
  <text x="220" y="155" fill='#f85149' font-size='12' font-family='sans-serif'>r</text>
  <path d="M 200 145 A 25 25 0 0 0 193 115" fill='none' stroke='#a371f7' stroke-width="1.5"/>
  <text x="205" y="138" fill='#a371f7' font-size='12' font-family='sans-serif'>\u03b8</text>
  <text x="155" y="158" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
</svg>
"""
    },
    {
        "title": "Sector Area: The Area of a 'Pie Slice'",
        "body": """
<h4>Sector Area Formula (Degrees)</h4>

<p>A sector is like a slice of pie. Its area is a fraction of the total circle area:</p>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(\\text{Sector Area} = \\frac{\\theta}{360} \\times \\pi r^2 = \\frac{\\theta \\pi r^2}{360}\\)</p>

<p style="margin-top: 16px;"><strong>Where:</strong></p>
<ul>
<li>θ = central angle in degrees</li>
<li>r = radius</li>
</ul>

<h4>Sector Area Formula (Radians)</h4>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(A = \\frac{1}{2}r^2\\theta\\)</p>

<p style="margin-top: 16px;"><strong>Where:</strong></p>
<ul>
<li>A = sector area</li>
<li>r = radius</li>
<li>θ = central angle in radians</li>
</ul>

<div class="worked-example">
<h5>Example 3: Sector Area in Degrees</h5>
<p>A circle has radius 10 cm and central angle 45°. Find the sector area.</p>
<p><strong>Solution:</strong></p>
<p>Sector Area \\(= \\frac{45}{360} \\times \\pi(10)^2 = \\frac{1}{8} \\times 100\\pi =\\) <strong>\\(12.5\\pi\\) cm² \\(\\approx 39.3\\) cm²</strong></p>
</div>

<div class="worked-example">
<h5>Example 4: Sector Area in Radians</h5>
<p>A circle has radius 6 cm and central angle π/3 radians. Find the sector area.</p>
<p><strong>Solution:</strong></p>
<p>Sector Area \\(= \\frac{1}{2} \\times 6^2 \\times \\frac{\\pi}{3} = \\frac{1}{2} \\times 36 \\times \\frac{\\pi}{3} =\\) <strong>\\(6\\pi\\) cm² \\(\\approx 18.85\\) cm²</strong></p>
</div>

<h4>Comparing Sector Areas</h4>

<svg width="400" height="270" viewBox="0 0 400 270" class="formula-box">
  <!-- 60 degree sector -->
  <circle cx="105" cy="115" r="60" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="105" cy="115" r="3" fill='currentColor'/>
  <line x1="105" y1="115" x2="165" y2="115" stroke='#f85149' stroke-width="1.5"/>
  <line x1="105" y1="115" x2="135" y2="55" stroke='#f85149' stroke-width="1.5"/>
  <path d="M 165 115 A 60 60 0 0 0 135 55" fill='#79c0ff' opacity='0.25' stroke='#79c0ff' stroke-width="2"/>
  <text x="105" y="200" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>60\u00b0</text>
  <text x="105" y="218" fill='#79c0ff' font-size='11' font-family='sans-serif' text-anchor='middle'>A = \u03c0r\u00b2/6</text>
  <!-- 120 degree sector -->
  <circle cx="295" cy="115" r="60" fill='none' stroke='#f85149' stroke-width="2"/>
  <circle cx="295" cy="115" r="3" fill='currentColor'/>
  <line x1="295" y1="115" x2="355" y2="115" stroke='#f85149' stroke-width="1.5"/>
  <line x1="295" y1="115" x2="265" y2="47" stroke='#f85149' stroke-width="1.5"/>
  <path d="M 355 115 A 60 60 0 0 0 265 47" fill='#f85149' opacity='0.25' stroke='#f85149' stroke-width="2"/>
  <text x="295" y="200" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>120\u00b0</text>
  <text x="295" y="218" fill='#f85149' font-size='11' font-family='sans-serif' text-anchor='middle'>A = \u03c0r\u00b2/3</text>

  <text x="200" y="255" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>Sector area is proportional to the central angle</text>
</svg>
"""
    },
    {
        "title": "Segment Area: The Curved Region Between Chord and Arc",
        "body": """
<h4>What is a Segment?</h4>

<p>A <strong>segment</strong> is the region between a chord and the arc above (or below) it. To find its area, we use:</p>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(\\text{Segment Area} = \\text{Sector Area} - \\text{Triangle Area}\\)</p>

<svg width="400" height="290" viewBox="0 0 400 290" class="formula-box">
  <circle cx="170" cy="130" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="170" cy="130" r="3" fill='currentColor'/>
  <!-- Sector fill (triangle + arc region) -->
  <path d="M 170 130 L 250 70 A 80 80 0 0 1 250 190 Z" fill='#f85149' opacity='0.1' stroke='none'/>
  <!-- Segment fill (between chord and arc) -->
  <path d="M 250 70 A 80 80 0 0 1 250 190 L 250 70 Z" fill='#79c0ff' opacity='0.2' stroke='#79c0ff' stroke-width="2"/>
  <line x1="170" y1="130" x2="250" y2="70" stroke='#f85149' stroke-width="2"/>
  <line x1="170" y1="130" x2="250" y2="190" stroke='#f85149' stroke-width="2"/>
  <line x1="250" y1="70" x2="250" y2="190" stroke='#a371f7' stroke-width="2"/>
  <text x="155" y="125" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>
  <!-- Labels positioned clearly -->
  <text x="300" y="130" fill='#79c0ff' font-size='12' font-family='sans-serif' font-weight='bold'>Segment</text>
  <text x="200" y="155" fill='#f85149' font-size='11' font-family='sans-serif'>Sector</text>
  <text x="300" y="150" fill='#a371f7' font-size='11' font-family='sans-serif'>\u2212 Triangle</text>
  <text x="200" y="275" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>Segment = Sector \u2212 Triangle</text>
</svg>

<h4>Segment Area Formula (Radians)</h4>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(\\text{Segment Area} = \\frac{1}{2}r^2(\\theta - \\sin\\theta)\\)</p>

<p style="margin-top: 16px;"><strong>Where:</strong></p>
<ul>
<li>r = radius</li>
<li>θ = central angle in radians</li>
</ul>

<p><strong>Note:</strong> This formula combines the sector area \\(\\frac{1}{2}r^2\\theta\\) and subtracts the triangle area \\(\\frac{1}{2}r^2\\sin\\theta\\).</p>

<div class="worked-example">
<h5>Example 5: Segment Area</h5>
<p>A circle has radius 8 cm with central angle 2π/3 radians. Find the segment area.</p>
<p><strong>Solution:</strong></p>
<p>Segment Area \\(= \\frac{1}{2} \\times 8^2 \\times \\left(\\frac{2\\pi}{3} - \\sin\\left(\\frac{2\\pi}{3}\\right)\\right)\\)</p>
<p>\\(= \\frac{1}{2} \\times 64 \\times \\left(\\frac{2\\pi}{3} - \\frac{\\sqrt{3}}{2}\\right)\\)</p>
<p>\\(= 32\\left(\\frac{2\\pi}{3} - \\frac{\\sqrt{3}}{2}\\right)\\)</p>
<p>\\(\\approx 32(2.094 - 0.866) \\approx\\) <strong>39.3 cm²</strong></p>
</div>

<h4>When to Use Each Formula</h4>

<table style="width:100%; border-collapse:collapse; margin-top:16px;">
<tr >
<td style="padding: 8px;"><strong>Measure</strong></td>
<td style="padding: 8px;"><strong>Formula (Degrees)</strong></td>
<td style="padding: 8px;"><strong>Formula (Radians)</strong></td>
</tr>
<tr>
<td style="padding: 8px;">Arc Length</td>
<td style="padding: 8px;">\\(\\frac{\\theta \\pi r}{180}\\)</td>
<td style="padding: 8px;">\\(r\\theta\\)</td>
</tr>
<tr class="worked-example">
<td style="padding: 8px;">Sector Area</td>
<td style="padding: 8px;">\\(\\frac{\\theta \\pi r^2}{360}\\)</td>
<td style="padding: 8px;">\\(\\frac{1}{2}r^2\\theta\\)</td>
</tr>
<tr>
<td style="padding: 8px;">Segment Area</td>
<td style="padding: 8px;">\\(r^2\\left(\\frac{\\theta\\pi}{360} - \\frac{\\sin\\theta}{2}\\right)\\)</td>
<td style="padding: 8px;">\\(\\frac{1}{2}r^2(\\theta - \\sin\\theta)\\)</td>
</tr>
</table>
"""
    }
]
