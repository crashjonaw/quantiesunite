TITLE = "Volume of Cuboids (Rectangular Boxes)"

SECTIONS = [
    {
        "title": "The Cuboid Volume Formula",
        "body": """<div class='concept-box'>
<h3>What's a Cuboid?</h3>
<p>A <strong>cuboid</strong> (or rectangular box) has 6 rectangular faces. Think of a cereal box, a brick, or a shoebox.</p>
<p>It has three dimensions:</p>
<ul>
<li><strong>Length (l)</strong> — how long it is</li>
<li><strong>Width (w)</strong> — how wide it is</li>
<li><strong>Height (h)</strong> — how tall it is</li>
</ul>
</div>

<div class='success-box'>
<h3>The Formula</h3>
<p>\\(V = l \\times w \\times h\\)</p>
<p><strong>Volume \(= \text{Length} \times \text{Width} \times \text{Height}\)</strong></p>
</div>

<svg width="100%" viewBox="0 0 360 200" class="formula-box">
  <text x="16" y="20" fill='currentColor' font-size='13' font-weight='bold'>Cuboid with Dimensions</text>

  <!-- Front face -->
  <rect x="60" y="80" width="140" height="80" rx='4' fill='#3d444d' stroke='#58a6ff' stroke-width='2'/>

  <!-- Top face (isometric) -->
  <polygon points="60,80 110,50 250,50 200,80" fill='#1f6feb' stroke='#58a6ff' stroke-width='2' opacity='0.45'/>

  <!-- Right face (isometric) -->
  <polygon points="200,80 250,50 250,130 200,160" fill='#2d333b' stroke='#58a6ff' stroke-width='2' opacity='0.7'/>

  <!-- Back edges (dashed, hidden) -->
  <line x1="60" y1="160" x2="110" y2="130" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.35'/>
  <line x1="110" y1="50" x2="110" y2="130" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.35'/>
  <line x1="250" y1="130" x2="110" y2="130" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.35'/>

  <!-- Length label (bottom front edge) -->
  <line x1="65" y1="168" x2="195" y2="168" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="130" y="184" fill='#79c0ff' font-size='12' font-weight='bold' text-anchor='middle'>l (length)</text>

  <!-- Height label (left front edge) -->
  <line x1="50" y1="85" x2="50" y2="155" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="36" y="124" fill='#79c0ff' font-size='12' font-weight='bold' text-anchor='middle' transform='rotate(-90,36,124)'>h</text>

  <!-- Width label (top right edge) -->
  <line x1="205" y1="76" x2="245" y2="54" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="238" y="76" fill='#79c0ff' font-size='12' font-weight='bold'>w</text>

  <!-- Arrowhead markers -->
  <defs>
    <marker id='arrL' markerWidth='6' markerHeight='6' refX='0' refY='3' orient='auto'><path d='M6,0 L0,3 L6,6' fill='#79c0ff'/></marker>
    <marker id='arrR' markerWidth='6' markerHeight='6' refX='6' refY='3' orient='auto'><path d='M0,0 L6,3 L0,6' fill='#79c0ff'/></marker>
  </defs>
</svg>"""
    },
    {
        "title": "Worked Examples: Basic Calculations",
        "body": """<div class='worked-example'>
<p><strong>Example 1:</strong> Find the volume of a cuboid with length 8 cm, width 5 cm, and height 3 cm.</p>
<p>Step 1: Write the formula</p>
<p>\\(V = l \\times w \\times h\\)</p>
<p>Step 2: Substitute the values</p>
<p>\\(V = 8 \\times 5 \\times 3\\)</p>
<p>Step 3: Calculate</p>
<p>\\(V = 40 \\times 3 = 120 \\text{ cm}^3\\)</p>
<p><strong>Answer: 120 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A cuboid has length 10 m, width 4 m, and height 2.5 m. What is its volume?</p>
<p>\\(V = 10 \\times 4 \\times 2.5\\)</p>
<p>\\(V = 40 \\times 2.5 = 100 \\text{ m}^3\\)</p>
<p><strong>Answer: 100 m³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A gift box is 20 cm long, 15 cm wide, and 10 cm high. Calculate its volume.</p>
<p>\\(V = 20 \\times 15 \\times 10\\)</p>
<p>\\(V = 300 \\times 10 = 3000 \\text{ cm}^3\\)</p>
<p><strong>Answer: 3000 cm³ = 3 L</strong></p>
</div>

<svg width="100%" viewBox="0 0 360 60" class="formula-box" style="margin-top:6px;">
  <rect x="8" y="8" width="100" height="40" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="58" y="24" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 1</text>
  <text x="58" y="40" fill='#79c0ff' font-size='11' text-anchor='middle'>120 cm³</text>

  <rect x="128" y="8" width="100" height="40" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="178" y="24" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 2</text>
  <text x="178" y="40" fill='#79c0ff' font-size='11' text-anchor='middle'>100 m³</text>

  <rect x="248" y="8" width="100" height="40" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="298" y="24" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 3</text>
  <text x="298" y="40" fill='#79c0ff' font-size='11' text-anchor='middle'>3000 cm³</text>
</svg>"""
    },
    {
        "title": "Finding Missing Dimensions",
        "body": """<div class='concept-box'>
<h3>Working Backwards</h3>
<p>Sometimes we know the volume and some dimensions, but need to find a missing one. Use the formula rearranged:</p>
<p>\\(h = \\frac{V}{l \\times w}\\)</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cuboid has length 10 cm, width 4 cm, and volume 200 cm³. Find the height.</p>
<p>Step 1: Use the formula rearranged</p>
<p>\\(h = \\frac{V}{l \\times w}\\)</p>
<p>Step 2: Substitute values</p>
<p>\\(h = \\frac{200}{10 \\times 4}\\)</p>
<p>Step 3: Calculate</p>
<p>\\(h = \\frac{200}{40} = 5 \\text{ cm}\\)</p>
<p><strong>Answer: Height = 5 cm</strong></p>
<p><strong>Check:</strong> \(10 \times 4 \times 5 = 200\) ✓</p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A tank has width 3 m, height 2 m, and volume 90 m³. Find the length.</p>
<p>\\(l = \\frac{V}{w \\times h} = \\frac{90}{3 \\times 2} = \\frac{90}{6} = 15 \\text{ m}\\)</p>
<p><strong>Answer: Length = 15 m</strong></p>
</div>"""
    },
    {
        "title": "Base Area Method: A Useful Shortcut",
        "body": """<div class='concept-box'>
<h3>Think of Volume Differently</h3>
<p>Volume can be thought of as <strong>stacking layers</strong>:</p>
<p>\\(V = \\text{Base Area} \\times \\text{Height}\\)</p>
<p>Imagine a rectangular base (\(\text{length} \times \text{width}\)). Now stack it upward by the height. That's your volume!</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cuboid has a rectangular base with area 24 cm² and height 6 cm. Find the volume.</p>
<p>\\(V = \\text{Base Area} \\times \\text{Height}\\)</p>
<p>\\(V = 24 \\times 6 = 144 \\text{ cm}^3\\)</p>
<p><strong>Answer: 144 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A rectangular tank has a base of 50 m × 40 m and height 2 m.</p>
<p>Step 1: Find the base area</p>
<p>\\(\\text{Base Area} = 50 \\times 40 = 2000 \\text{ m}^2\\)</p>
<p>Step 2: Multiply by height</p>
<p>\\(V = 2000 \\times 2 = 4000 \\text{ m}^3\\)</p>
<p><strong>Answer: 4000 m³</strong></p>
</div>

<svg width="100%" viewBox="0 0 360 220" class="formula-box">
  <text x="16" y="20" fill='currentColor' font-size='13' font-weight='bold'>Stacking Layers Concept</text>

  <defs>
    <marker id='arrU' markerWidth='6' markerHeight='6' refX='3' refY='0' orient='auto'><path d='M0,6 L3,0 L6,6' fill='#79c0ff'/></marker>
    <marker id='arrD' markerWidth='6' markerHeight='6' refX='3' refY='6' orient='auto'><path d='M0,0 L3,6 L6,0' fill='#79c0ff'/></marker>
  </defs>

  <!-- Layer 1 (bottom) - base layer highlighted -->
  <polygon points="50,160 100,140 220,140 170,160" fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.55'/>
  <rect x="50" y="160" width="120" height="24" rx='2' fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.55'/>
  <polygon points="170,160 220,140 220,164 170,184" fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.4'/>

  <!-- Layer 2 -->
  <polygon points="50,134 100,114 220,114 170,134" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="50" y="134" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="170,134 220,114 220,138 170,158" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Layer 3 -->
  <polygon points="50,108 100,88 220,88 170,108" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="50" y="108" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="170,108 220,88 220,112 170,132" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Layer 4 (top) -->
  <polygon points="50,82 100,62 220,62 170,82" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="50" y="82" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="170,82 220,62 220,86 170,106" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Base Area label -->
  <text x="110" y="176" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Base Area</text>
  <text x="110" y="188" fill='#79c0ff' font-size='9' text-anchor='middle'>(l x w)</text>

  <!-- Height arrow -->
  <line x1="234" y1="66" x2="234" y2="178" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrU)' marker-end='url(#arrD)'/>
  <text x="248" y="126" fill='#79c0ff' font-size='11' font-weight='bold'>h</text>

  <!-- Formula -->
  <rect x="16" y="198" width="328" height="18" rx='4' fill='#1f6feb' opacity='0.15'/>
  <text x="180" y="211" fill='currentColor' font-size='11' text-anchor='middle'>V = Base Area x Height = (l x w) x h</text>
</svg>"""
    }
]
