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

<svg width="100%" viewBox="0 0 380 210" class="formula-box">
  <defs>
    <marker id='arrL' markerWidth='6' markerHeight='6' refX='0' refY='3' orient='auto'><path d='M6,0 L0,3 L6,6' fill='#79c0ff'/></marker>
    <marker id='arrR' markerWidth='6' markerHeight='6' refX='6' refY='3' orient='auto'><path d='M0,0 L6,3 L0,6' fill='#79c0ff'/></marker>
  </defs>

  <text x="190" y="20" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Cuboid with Dimensions</text>

  <!-- Front face -->
  <rect x="70" y="75" width="140" height="80" rx='4' fill='#3d444d' stroke='#58a6ff' stroke-width='2'/>

  <!-- Top face (isometric) -->
  <polygon points="70,75 120,45 260,45 210,75" fill='#1f6feb' stroke='#58a6ff' stroke-width='2' opacity='0.45'/>

  <!-- Right face (isometric) -->
  <polygon points="210,75 260,45 260,125 210,155" fill='#2d333b' stroke='#58a6ff' stroke-width='2' opacity='0.65'/>

  <!-- Back edges (dashed, hidden) -->
  <line x1="70" y1="155" x2="120" y2="125" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.3'/>
  <line x1="120" y1="45" x2="120" y2="125" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.3'/>
  <line x1="260" y1="125" x2="120" y2="125" stroke='#58a6ff' stroke-width='1' stroke-dasharray='5,4' opacity='0.3'/>

  <!-- Length label (bottom front edge) -->
  <line x1="75" y1="165" x2="205" y2="165" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="140" y="182" fill='#79c0ff' font-size='12' font-weight='bold' text-anchor='middle'>l (length)</text>

  <!-- Height label (left front edge) -->
  <line x1="55" y1="80" x2="55" y2="150" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="40" y="120" fill='#79c0ff' font-size='12' font-weight='bold' text-anchor='middle' transform='rotate(-90,40,120)'>h</text>

  <!-- Width label (top right edge) -->
  <line x1="218" y1="72" x2="255" y2="50" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrL)' marker-end='url(#arrR)'/>
  <text x="248" y="72" fill='#79c0ff' font-size='12' font-weight='bold'>w</text>
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

<svg width="100%" viewBox="0 0 380 65" class="formula-box" style="margin-top:6px;">
  <rect x="15" y="10" width="105" height="42" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="67" y="27" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 1</text>
  <text x="67" y="43" fill='#79c0ff' font-size='11' text-anchor='middle'>120 cm³</text>

  <rect x="138" y="10" width="105" height="42" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="190" y="27" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 2</text>
  <text x="190" y="43" fill='#79c0ff' font-size='11' text-anchor='middle'>100 m³</text>

  <rect x="261" y="10" width="105" height="42" rx='4' fill='#58a6ff' opacity='0.25' stroke='#58a6ff' stroke-width='1.5'/>
  <text x="313" y="27" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Ex 3</text>
  <text x="313" y="43" fill='#79c0ff' font-size='11' text-anchor='middle'>3000 cm³</text>
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

<svg width="100%" viewBox="0 0 380 235" class="formula-box">
  <defs>
    <marker id='arrU' markerWidth='6' markerHeight='6' refX='3' refY='0' orient='auto'><path d='M0,6 L3,0 L6,6' fill='#79c0ff'/></marker>
    <marker id='arrD' markerWidth='6' markerHeight='6' refX='3' refY='6' orient='auto'><path d='M0,0 L3,6 L6,0' fill='#79c0ff'/></marker>
  </defs>

  <text x="190" y="20" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Stacking Layers Concept</text>

  <!-- Layer 1 (bottom) - base layer highlighted -->
  <polygon points="60,170 110,148 230,148 180,170" fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.55'/>
  <rect x="60" y="170" width="120" height="24" rx='2' fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.55'/>
  <polygon points="180,170 230,148 230,172 180,194" fill='#1f6feb' stroke='#58a6ff' stroke-width='1.5' opacity='0.4'/>

  <!-- Layer 2 -->
  <polygon points="60,144 110,122 230,122 180,144" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="60" y="144" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="180,144 230,122 230,146 180,168" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Layer 3 -->
  <polygon points="60,118 110,96 230,96 180,118" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="60" y="118" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="180,118 230,96 230,120 180,142" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Layer 4 (top) -->
  <polygon points="60,92 110,70 230,70 180,92" fill='#3d444d' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>
  <rect x="60" y="92" width="120" height="24" rx='2' fill='#3d444d' stroke='#58a6ff' stroke-width='1.5'/>
  <polygon points="180,92 230,70 230,94 180,116" fill='#2d333b' stroke='#58a6ff' stroke-width='1.5' opacity='0.7'/>

  <!-- Base Area label -->
  <text x="120" y="186" fill='currentColor' font-size='10' text-anchor='middle' font-weight='bold'>Base Area</text>
  <text x="120" y="198" fill='#79c0ff' font-size='9' text-anchor='middle'>(l × w)</text>

  <!-- Height arrow -->
  <line x1="248" y1="74" x2="248" y2="190" stroke='#79c0ff' stroke-width='1.5' marker-start='url(#arrU)' marker-end='url(#arrD)'/>
  <text x="262" y="136" fill='#79c0ff' font-size='11' font-weight='bold'>h</text>

  <!-- Formula -->
  <rect x="20" y="210" width="340" height="18" rx='4' fill='#1f6feb' opacity='0.15'/>
  <text x="190" y="223" fill='currentColor' font-size='11' text-anchor='middle'>V = Base Area × Height = (l × w) × h</text>
</svg>"""
    }
]
