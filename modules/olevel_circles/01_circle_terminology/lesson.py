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
<svg width="300" height="260" viewBox="0 0 300 260" class="formula-box">
  <circle cx="150" cy="115" r="100" fill='none' stroke='#79c0ff' stroke-width="2" rx='4'/>
  <circle cx="150" cy="115" r="3" fill='currentColor'/>
  <line x1="150" y1="115" x2="250" y2="115" stroke='#79c0ff' stroke-width="2"/>
  <circle cx="250" cy="115" r="3" fill='#79c0ff'/>
  <text x="200" y="105" fill='currentColor' font-size='14' font-family='sans-serif' font-weight='bold'>r</text>
  <text x="155" y="130" fill='currentColor' font-size='14' font-family='sans-serif' font-weight='bold'>O</text>
  <line x1="50" y1="115" x2="250" y2="115" stroke='#f85149' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="150" y="245" fill='currentColor' font-size='13' font-family='sans-serif' text-anchor='middle'>Diameter = 2r</text>
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

<svg width="350" height="280" viewBox="0 0 350 280" class="formula-box">
  <circle cx="175" cy="130" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="130" r="3" fill='currentColor'/>
  <circle cx="240" cy="85" r="4" fill='#f85149'/>
  <circle cx="110" cy="85" r="4" fill='#f85149'/>
  <path d="M 110 85 A 90 90 0 0 1 240 85" fill='none' stroke='#79c0ff' stroke-width="3"/>
  <path d="M 110 85 A 90 90 0 1 1 240 85" fill='none' stroke='#a371f7' stroke-width="2" stroke-dasharray="5,5"/>
  <line x1="110" y1="85" x2="240" y2="85" stroke='#f85149' stroke-width="2"/>
  <text x="175" y="148" fill='currentColor' font-size='13' font-family='sans-serif' text-anchor='middle'>O</text>
  <text x="80" y="72" fill='currentColor' font-size='12' font-family='sans-serif'>A</text>
  <text x="248" y="72" fill='currentColor' font-size='12' font-family='sans-serif'>B</text>
  <text x="175" y="58" fill='#79c0ff' font-size='12' font-family='sans-serif' font-weight='bold' text-anchor='middle'>Minor Arc</text>
  <text x="175" y="200" fill='#a371f7' font-size='12' font-family='sans-serif' font-weight='bold' text-anchor='middle'>Major Arc</text>
  <text x="175" y="108" fill='#f85149' font-size='12' font-family='sans-serif' text-anchor='middle'>Chord</text>
</svg>

<h4>Sector: A "Pie Slice" of the Circle</h4>
<p><strong>Sector:</strong> A region bounded by two radii and an arc. Think of it as a "slice of pie".</p>

<h4>Segment: Between a Chord and Arc</h4>
<p><strong>Segment:</strong> A region bounded by a chord and the arc it cuts off. This is the region "between" a chord and the arc above it.</p>

<svg width="370" height="295" viewBox="0 0 370 295" class="formula-box">
  <circle cx="175" cy="135" r="90" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="175" cy="135" r="3" fill='currentColor'/>
  <!-- Sector: two radii + arc fill -->
  <path d="M 175 135 L 175 45 A 90 90 0 0 1 240 185 Z" fill='#79c0ff' opacity='0.15' stroke='#79c0ff' stroke-width="2"/>
  <line x1="175" y1="135" x2="175" y2="45" stroke='#f85149' stroke-width="2"/>
  <line x1="175" y1="135" x2="240" y2="185" stroke='#f85149' stroke-width="2"/>
  <text x="210" y="130" fill='currentColor' font-size='12' font-family='sans-serif' font-weight='bold'>Sector</text>
  <text x="155" y="90" fill='#f85149' font-size='11' font-family='sans-serif'>Radius</text>
  <text x="215" y="168" fill='#f85149' font-size='11' font-family='sans-serif'>Radius</text>
  <!-- Segment: chord + arc fill -->
  <line x1="110" y1="185" x2="240" y2="185" stroke='#a371f7' stroke-width="2"/>
  <path d="M 110 185 A 90 90 0 0 1 240 185" fill='#a371f7' opacity='0.15' stroke='#a371f7' stroke-width="2"/>
  <text x="175" y="210" fill='#a371f7' font-size='12' font-family='sans-serif' font-weight='bold' text-anchor='middle'>Chord</text>
  <text x="175" y="280" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>Segment = region between chord and arc</text>
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

<svg width="460" height="300" viewBox="0 0 460 300" class="formula-box">
  <circle cx="70" cy="105" r="40" fill='none' stroke='#79c0ff' stroke-width="2"/>
  <circle cx="200" cy="105" r="60" fill='none' stroke='#f85149' stroke-width="2"/>
  <circle cx="360" cy="105" r="80" fill='none' stroke='#a371f7' stroke-width="2"/>
  <text x="70" y="175" fill='#79c0ff' font-size='13' font-family='sans-serif' text-anchor='middle' font-weight='bold'>r = 2</text>
  <text x="70" y="193" fill='#79c0ff' font-size='12' font-family='sans-serif' text-anchor='middle'>C = 4\u03c0</text>
  <text x="70" y="211" fill='#79c0ff' font-size='12' font-family='sans-serif' text-anchor='middle'>A = 4\u03c0</text>
  <text x="200" y="195" fill='#f85149' font-size='13' font-family='sans-serif' text-anchor='middle' font-weight='bold'>r = 3</text>
  <text x="200" y="213" fill='#f85149' font-size='12' font-family='sans-serif' text-anchor='middle'>C = 6\u03c0</text>
  <text x="200" y="231" fill='#f85149' font-size='12' font-family='sans-serif' text-anchor='middle'>A = 9\u03c0</text>
  <text x="360" y="215" fill='#a371f7' font-size='13' font-family='sans-serif' text-anchor='middle' font-weight='bold'>r = 4</text>
  <text x="360" y="233" fill='#a371f7' font-size='12' font-family='sans-serif' text-anchor='middle'>C = 8\u03c0</text>
  <text x="360" y="251" fill='#a371f7' font-size='12' font-family='sans-serif' text-anchor='middle'>A = 16\u03c0</text>
  <text x="230" y="285" fill='currentColor' font-size='12' font-family='sans-serif' text-anchor='middle'>Circumference grows linearly; area grows quadratically</text>
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
