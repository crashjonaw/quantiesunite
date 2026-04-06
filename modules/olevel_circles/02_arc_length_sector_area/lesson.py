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

<svg width="350" height="350" viewBox="-30 0 410 348" class="formula-box">
  <circle cx="175" cy="175" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="175" r="4" fill='currentColor'/>
  <line x1="175" y1="175" x2="275" y2="175" stroke='#f85149' stroke-width="2"/>
  <line x1="175" y1="175" x2="218" y2="99" stroke='#f85149' stroke-width="2"/>
  <path d="M 275 175 A 100 100 0 0 0 218 99" fill='none' stroke='#a371f7' stroke-width="3"/>
  <text x="240" y="155" fill='#a371f7' font-size='16' font-weight='bold'>θ</text>
  <text x="260" y="130" fill='#f85149' font-size='12' font-weight='bold'>Radius</text>
  <text x="180" y="100" fill='#f85149' font-size='12' font-weight='bold'>Radius</text>
  <path d="M 200 180 A 30 30 0 0 0 195 150" fill='none' stroke='#a371f7' stroke-width="1"/>
  <text x="220" y="170" fill='#a371f7' font-size='11'>Central</text>
  <text x="225" y="185" fill='#a371f7' font-size='11'>Angle</text>
  <text x="175" y="330" fill='currentColor' font-size='13' text-anchor='middle'>The central angle determines what fraction of the circle we have</text>
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

<svg width="360" height="300" class="formula-box">
  <circle cx="180" cy="150" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <line x1="180" y1="150" x2="270" y2="150" stroke='#f85149' stroke-width="2"/>
  <line x1="180" y1="150" x2="225" y2="64" stroke='#f85149' stroke-width="2"/>
  <path d="M 270 150 A 90 90 0 0 0 225 64" fill='none' stroke='#a371f7' stroke-width="3"/>
  <text x="255" y="115" fill='#a371f7' font-size='14' font-weight='bold'>arc length</text>
  <text x="200" y="165" fill='#f85149' font-size='12'>r</text>
  <path d="M 210 155 A 25 25 0 0 0 203 125" fill='none' stroke='#a371f7' stroke-width="1"/>
  <text x="220" y="145" fill='#a371f7' font-size='11'>θ</text>
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

<svg width="400" height="280" class="formula-box">
  <circle cx="100" cy="140" r="60" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <line x1="100" y1="140" x2="160" y2="140" stroke='#f85149' stroke-width="1.5"/>
  <line x1="100" y1="140" x2="130" y2="80" stroke='#f85149' stroke-width="1.5"/>
  <path d="M 160 140 A 60 60 0 0 0 130 80" fill='#79c0ff' opacity='0.3' stroke='#79c0ff' stroke-width="2"/>
  <text x="100" y="185" fill='currentColor' font-size='12' text-anchor='middle'>60°</text>
  <text x="70" y="195" fill='#79c0ff' font-size='11'>A = πr²/6</text>

  <circle cx="280" cy="140" r="60" fill='none' stroke='#f85149' stroke-width="2"/>
  <line x1="280" y1="140" x2="340" y2="140" stroke='#f85149' stroke-width="1.5"/>
  <line x1="280" y1="140" x2="250" y2="72" stroke='#f85149' stroke-width="1.5"/>
  <path d="M 340 140 A 60 60 0 0 0 250 72" fill='#f85149' opacity='0.3' stroke='#f85149' stroke-width="2"/>
  <text x="280" y="185" fill='currentColor' font-size='12' text-anchor='middle'>120°</text>
  <text x="250" y="195" fill='#f85149' font-size='11'>A = πr²/3</text>

  <text x="200" y="250" fill='currentColor' font-size='12' text-anchor='middle'>Sector area is proportional to the central angle</text>
</svg>
"""
    },
    {
        "title": "Segment Area: The Curved Region Between Chord and Arc",
        "body": """
<h4>What is a Segment?</h4>

<p>A <strong>segment</strong> is the region between a chord and the arc above (or below) it. To find its area, we use:</p>

<p style="text-align: center; font-weight: bold; font-size: 16px;">\\(\\text{Segment Area} = \\text{Sector Area} - \\text{Triangle Area}\\)</p>

<svg width="360" height="280" class="formula-box">
  <circle cx="180" cy="140" r="80" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="180" cy="140" r="3" fill='currentColor'/>
  <line x1="180" y1="140" x2="260" y2="80" stroke='#f85149' stroke-width="2"/>
  <line x1="180" y1="140" x2="260" y2="200" stroke='#f85149' stroke-width="2"/>
  <line x1="260" y1="80" x2="260" y2="200" stroke='#a371f7' stroke-width="2"/>
  <path d="M 260 80 A 80 80 0 0 0 260 200" fill='#79c0ff' opacity='0.2' stroke='#79c0ff' stroke-width="2"/>
  <path d="M 180 140 L 260 80 L 260 200 Z" fill='#f85149' opacity='0.1' stroke='none'/>
  <text x="235" y="140" fill='#79c0ff' font-size='12' font-weight='bold'>Segment</text>
  <text x="200" y="145" fill='#f85149' font-size='11'>Sector</text>
  <text x="265" y="145" fill='#a371f7' font-size='11'>−Triangle</text>
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
