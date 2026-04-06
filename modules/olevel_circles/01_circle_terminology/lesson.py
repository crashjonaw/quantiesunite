TITLE = "Circle Terminology: Vocabulary and Key Definitions"

SECTIONS = [
    {
        "title": "What is a Circle? The Fundamental Definition",
        "body": """
<div class="concept-box">
<p><strong>Circle Definition:</strong> A circle is the set of ALL points at the same distance (called the <strong>radius</strong>) from a fixed point called the <strong>center</strong>.</p>
</div>

<p>This simple definition creates a shape with incredibly deep and beautiful properties. Once you understand what a circle truly is, all the other circle vocabulary follows naturally.</p>

<h4>The Most Important Parts</h4>
<ul>
<li><strong>Center (O):</strong> The fixed point from which all points on the circle are equidistant</li>
<li><strong>Radius (r):</strong> The distance from center to any point on the circle. All radii are equal</li>
<li><strong>Diameter (d):</strong> A chord that passes through the center. Length = 2r</li>
</ul>

<h4>Visualizing Radius and Diameter</h4>
<svg width="300" height="300" class="formula-box">
  <circle cx="150" cy="150" r="100" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="150" cy="150" r="3" fill='currentColor'/>
  <line x1="150" y1="150" x2="250" y2="150" stroke='#79c0ff' stroke-width="2"/>
  <circle cx="250" cy="150" r="3" fill='#79c0ff'/>
  <text x="200" y="140" fill='currentColor' font-size='14' font-weight='bold'>r</text>
  <text x="155" y="165" fill='currentColor' font-size='14' font-weight='bold'>O</text>
  <line x1="50" y1="150" x2="250" y2="150" stroke='#f85149' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="140" y="180" fill='currentColor' font-size='14'>Diameter = 2r</text>
</svg>

<p><strong>Circumference Formula:</strong></p>
<p>The perimeter (distance around) a circle is called the <strong>circumference</strong>:</p>
<p style="text-align: center; font-weight: bold;">\\(C = 2\\pi r\\) or \\(C = \\pi d\\)</p>

<div class="worked-example">
<h5>Example 1: Circle with Radius 5 cm</h5>
<ul>
<li>Radius: r = 5 cm</li>
<li>Diameter: d = 2 × 5 = 10 cm</li>
<li>Circumference: \\(C = 2\\pi(5) = 10\\pi \\approx 31.4\\) cm</li>
</ul>
</div>
"""
    },
    {
        "title": "Chords, Arcs, and Segments: Pieces of the Circle",
        "body": """
<h4>Chord: A Line Segment Inside the Circle</h4>
<p><strong>Chord:</strong> A straight line segment joining any two points on the circle.</p>

<ul>
<li>The <strong>diameter</strong> is the longest possible chord (it passes through the center)</li>
<li>All other chords are shorter than the diameter</li>
<li>Chords of equal length are equidistant from the center</li>
</ul>

<h4>Arc: A Curved Piece of the Circle</h4>
<p><strong>Arc:</strong> A portion of the circumference. When you specify a chord, you also define two arcs (major and minor).</p>

<ul>
<li><strong>Minor arc:</strong> The shorter arc between two points</li>
<li><strong>Major arc:</strong> The longer arc between the same two points</li>
<li><strong>Semicircle:</strong> An arc that is exactly half the circumference (180°)</li>
</ul>

<svg width="350" height="280" class="formula-box">
  <circle cx="175" cy="140" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="140" r="3" fill='currentColor'/>
  <circle cx="240" cy="95" r="4" fill='#f85149'/>
  <circle cx="110" cy="95" r="4" fill='#f85149'/>
  <path d="M 110 95 A 90 90 0 0 1 240 95" fill='none' stroke='#79c0ff' stroke-width="3"/>
  <path d="M 110 95 A 90 90 0 1 1 240 95" fill='none' stroke='#a371f7' stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="110" y1="95" x2="240" y2="95" stroke='#f85149' stroke-width="2"/>
  <text x="175" y="160" fill='currentColor' font-size='13' text-anchor='middle'>O</text>
  <text x="85" y="80" fill='currentColor' font-size='12'>Point A</text>
  <text x="245" y="80" fill='currentColor' font-size='12'>Point B</text>
  <text x="150" y="110" fill='#79c0ff' font-size='13' font-weight='bold'>Minor Arc</text>
  <text x="160" y="200" fill='#a371f7' font-size='13' font-weight='bold'>Major Arc</text>
  <text x="175" y="130" fill='#f85149' font-size='13'>Chord</text>
</svg>

<h4>Sector: A "Pie Slice" of the Circle</h4>
<p><strong>Sector:</strong> A region bounded by two radii and an arc. Think of it as a "slice of pie".</p>

<h4>Segment: Between a Chord and Arc</h4>
<p><strong>Segment:</strong> A region bounded by a chord and the arc it cuts off. This is the region "between" a chord and the arc above it.</p>

<svg width="370" height="280" viewBox="0 0 370 280" class="formula-box">
  <circle cx="175" cy="140" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="140" r="3" fill='currentColor'/>
  <path d="M 175 50 L 240 190 L 110 190 Z" fill='#79c0ff' opacity='0.2' stroke='#79c0ff' stroke-width="2"/>
  <line x1="175" y1="140" x2="175" y2="50" stroke='#f85149' stroke-width="2"/>
  <line x1="175" y1="140" x2="240" y2="190" stroke='#f85149' stroke-width="2"/>
  <text x="200" y="150" fill='currentColor' font-size='12' font-weight='bold'>Sector</text>
  <text x="185" y="105" fill='#f85149' font-size='11'>Radius</text>
  <text x="210" y="175" fill='#f85149' font-size='11'>Radius</text>
  <line x1="110" y1="190" x2="240" y2="190" stroke='#a371f7' stroke-width="2"/>
  <text x="175" y="220" fill='#a371f7' font-size='12' font-weight='bold'>Chord</text>
  <path d="M 110 190 A 90 90 0 0 1 240 190" fill='#a371f7' opacity='0.1' stroke='#a371f7' stroke-width="2"/>
  <text x="175" y="270" fill='#a371f7' font-size='11' font-weight='bold'>Segment = Between chord and arc</text>
</svg>
"""
    },
    {
        "title": "Circumference and Area Formulas",
        "body": """
<h4>Circumference: The Perimeter of a Circle</h4>

<p>We already know: \\(C = 2\\pi r\\)</p>

<p>Why? Because circumference is proportional to radius, and the constant of proportionality is 2π (which comes from the definition of π itself).</p>

<div class="worked-example">
<h5>Example: Finding Circumference</h5>
<p>A circle has radius 7 cm.</p>
<p><strong>Circumference:</strong> \\(C = 2\\pi(7) = 14\\pi \\approx 43.98\\) cm</p>
</div>

<h4>Area: The Space Inside a Circle</h4>

<p><strong>Area Formula:</strong></p>
<p style="text-align: center; font-weight: bold;">\\(A = \\pi r^2\\)</p>

<p>This is one of the most important formulas in mathematics. The area grows with the <strong>square</strong> of the radius, which means doubling the radius gives 4× the area!</p>

<div class="worked-example">
<h5>Example: Finding Area</h5>
<p>A circle has radius 7 cm.</p>
<p><strong>Area:</strong> \\(A = \\pi(7)^2 = 49\\pi \\approx 153.94\\) cm²</p>
</div>

<h4>Comparing Circles: Area and Circumference Relationship</h4>

<svg width="400" height="300" viewBox="-50 0 500 298" class="formula-box">
  <circle cx="80" cy="120" r="40" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="200" cy="120" r="60" fill='none' stroke='#f85149' stroke-width="2"/>
  <circle cx="320" cy="120" r="80" fill='none' stroke='#a371f7' stroke-width="2"/>
  <text x="80" y="200" fill='#79c0ff' font-size='13' text-anchor='middle' font-weight='bold'>r=2</text>
  <text x="80" y="220" fill='#79c0ff' font-size='12' text-anchor='middle'>C=4π</text>
  <text x="80" y="238" fill='#79c0ff' font-size='12' text-anchor='middle'>A=4π</text>
  <text x="200" y="200" fill='#f85149' font-size='13' text-anchor='middle' font-weight='bold'>r=3</text>
  <text x="200" y="220" fill='#f85149' font-size='12' text-anchor='middle'>C=6π</text>
  <text x="200" y="238" fill='#f85149' font-size='12' text-anchor='middle'>A=9π</text>
  <text x="320" y="200" fill='#a371f7' font-size='13' text-anchor='middle' font-weight='bold'>r=4</text>
  <text x="320" y="220" fill='#a371f7' font-size='12' text-anchor='middle'>C=8π</text>
  <text x="320" y="238" fill='#a371f7' font-size='12' text-anchor='middle'>A=16π</text>
  <text x="200" y="280" fill='currentColor' font-size='13' text-anchor='middle'>As radius increases, circumference grows linearly, but area grows quadratically!</text>
</svg>
"""
    },
    {
        "title": "Practice Problems: Testing Your Understanding",
        "body": """
<h4>Problem 1: Identifying Parts of a Circle</h4>
<p>For a circle with center O and radius 6 cm, identify each measurement:</p>
<ul>
<li>What is the diameter?</li>
<li>What is the circumference?</li>
<li>What is the area?</li>
</ul>

<div class="success-box" style="display:none;" id="sol1">
<strong>Solutions:</strong>
<ul>
<li>Diameter: \\(d = 2r = 2(6) =\\) <strong>12 cm</strong></li>
<li>Circumference: \\(C = 2\\pi r = 2\\pi(6) =\\) <strong>\\(12\\pi \\approx 37.7\\) cm</strong></li>
<li>Area: \\(A = \\pi r^2 = \\pi(6)^2 =\\) <strong>\\(36\\pi \\approx 113.1\\) cm²</strong></li>
</ul>
</div>

<button onclick="document.getElementById('sol1').style.display='block'" style="padding: 8px 16px;  border: none; border-radius: 4px; cursor: pointer">Show Solution</button>

<h4 style="margin-top:24px;">Problem 2: Chord and Arc</h4>
<p>A chord is drawn in a circle, creating a minor arc and a major arc. If the minor arc is 120°, what is the major arc?</p>

<div class="success-box" style="display:none;" id="sol2">
<strong>Solution:</strong>
<p>The two arcs must sum to 360° (the full circle).</p>
<p>Major arc = 360° − 120° = <strong>240°</strong></p>
</div>

<button onclick="document.getElementById('sol2').style.display='block'" style="padding: 8px 16px;  border: none; border-radius: 4px; cursor: pointer">Show Solution</button>

<h4 style="margin-top:24px;">Problem 3: Finding Radius from Circumference</h4>
<p>A circle has circumference 31.4 cm. What is its radius? (Use π ≈ 3.14)</p>

<div class="success-box" style="display:none;" id="sol3">
<strong>Solution:</strong>
<p>\\(C = 2\\pi r\\), so: \\(31.4 = 2(3.14)r\\)</p>
<p>\\(31.4 = 6.28r\\)</p>
<p>\\(r = 31.4 \\div 6.28 =\\) <strong>5 cm</strong></p>
</div>

<button onclick="document.getElementById('sol3').style.display='block'" style="padding: 8px 16px;  border: none; border-radius: 4px; cursor: pointer">Show Solution</button>
"""
    }
]
