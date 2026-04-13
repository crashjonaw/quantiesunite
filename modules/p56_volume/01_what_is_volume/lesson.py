TITLE = "What is Volume?"

SECTIONS = [
    {
        "title": "Volume: From Flat to 3D",
        "body": """<div class='concept-box'>
<h3>The Big Idea</h3>
<p><strong>Area</strong> measures how much <em>flat space</em> a shape covers. <strong>Volume</strong> measures how much <em>3D space</em> a solid fills.</p>
<p>Think of it this way:</p>
<ul>
<li>A square on paper has area (2D)</li>
<li>A cube in space has volume (3D)</li>
</ul>
</div>

<p><strong>Volume tells us: "How much can fit inside?"</strong></p>

<p>Imagine filling a box with water, sand, or air. The amount of space inside the box is its volume.</p>

<svg width="100%" viewBox="0 0 420 165" class="formula-box">
  <!-- Flat square (2D) -->
  <g>
    <rect x="30" y="15" width="80" height="80" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
    <text x="70" y="55" fill='currentColor' font-size='12' text-anchor='middle'>4</text>
    <text x="15" y="60" fill='#79c0ff' font-size='10' text-anchor='middle'>4</text>
    <text x="70" y="112" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>2D: Area</text>
    <text x="70" y="130" fill='currentColor' font-size='11' text-anchor='middle'>4 × 4 = 16 sq units</text>
  </g>

  <!-- Arrow -->
  <text x="175" y="60" fill='#a0aec0' font-size='28' text-anchor='middle'>→</text>

  <!-- 3D cube -->
  <g>
    <!-- Front face -->
    <rect x="250" y="30" width="80" height="80" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx='4'/>
    <!-- Top face -->
    <polygon points="250,30 280,5 360,5 330,30" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.45'/>
    <!-- Right face -->
    <polygon points="330,30 360,5 360,85 330,110" fill='#2d333b' stroke='#58a6ff' stroke-width="2" opacity='0.65'/>
    <!-- Hidden back edges (dashed) -->
    <line x1="250" y1="110" x2="280" y2="85" stroke='#58a6ff' stroke-width="1" stroke-dasharray="4,3" opacity='0.3'/>
    <line x1="280" y1="5" x2="280" y2="85" stroke='#58a6ff' stroke-width="1" stroke-dasharray="4,3" opacity='0.3'/>
    <line x1="360" y1="85" x2="280" y2="85" stroke='#58a6ff' stroke-width="1" stroke-dasharray="4,3" opacity='0.3'/>
    <text x="290" y="122" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>3D: Volume</text>
    <text x="290" y="140" fill='currentColor' font-size='11' text-anchor='middle'>4 × 4 × 4 = 64 cubic units</text>
  </g>
</svg>"""
    },
    {
        "title": "Cubic Units: Counting Blocks",
        "body": """<div class='concept-box'>
<h3>How We Measure Volume</h3>
<p>Volume is measured in <strong>cubic units</strong>. Imagine a solid made of tiny unit cubes stacked together.</p>
<p><strong>The volume IS the number of unit cubes that fit inside.</strong></p>
</div>

<svg width="100%" viewBox="0 0 420 210" class="formula-box">
  <text x="210" y="20" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Counting unit cubes in a 2 × 2 × 2 cube</text>

  <!-- Layer 1 label -->
  <text x="90" y="48" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>Bottom layer</text>
  <!-- Layer 1: 2x2 grid -->
  <rect x="40" y="58" width="44" height="44" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx='4'/>
  <rect x="92" y="58" width="44" height="44" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx='4'/>
  <rect x="40" y="110" width="44" height="44" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx='4'/>
  <rect x="92" y="110" width="44" height="44" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx='4'/>
  <!-- Numbers in cubes -->
  <text x="62" y="86" fill='currentColor' font-size='13' text-anchor='middle'>1</text>
  <text x="114" y="86" fill='currentColor' font-size='13' text-anchor='middle'>2</text>
  <text x="62" y="138" fill='currentColor' font-size='13' text-anchor='middle'>3</text>
  <text x="114" y="138" fill='currentColor' font-size='13' text-anchor='middle'>4</text>
  <text x="90" y="170" fill='#a0aec0' font-size='10' text-anchor='middle'>4 cubes</text>

  <!-- Plus sign -->
  <text x="185" y="112" fill='#a0aec0' font-size='22' text-anchor='middle'>+</text>

  <!-- Layer 2 label -->
  <text x="300" y="48" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>Top layer</text>
  <!-- Layer 2: 2x2 grid -->
  <rect x="250" y="58" width="44" height="44" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" rx='4' opacity='0.4'/>
  <rect x="302" y="58" width="44" height="44" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" rx='4' opacity='0.4'/>
  <rect x="250" y="110" width="44" height="44" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" rx='4' opacity='0.4'/>
  <rect x="302" y="110" width="44" height="44" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" rx='4' opacity='0.4'/>
  <!-- Numbers in cubes -->
  <text x="272" y="86" fill='currentColor' font-size='13' text-anchor='middle'>5</text>
  <text x="324" y="86" fill='currentColor' font-size='13' text-anchor='middle'>6</text>
  <text x="272" y="138" fill='currentColor' font-size='13' text-anchor='middle'>7</text>
  <text x="324" y="138" fill='currentColor' font-size='13' text-anchor='middle'>8</text>
  <text x="300" y="170" fill='#a0aec0' font-size='10' text-anchor='middle'>4 cubes</text>

  <!-- Result -->
  <text x="210" y="198" fill='currentColor' font-size='12' font-weight='bold' text-anchor='middle'>Volume = 2 × 2 × 2 = 8 cubic units</text>
</svg>

<div class='worked-example'>
<p><strong>Example:</strong> A box is 3 units long, 2 units wide, and 2 units tall. How many unit cubes fit inside?</p>
<p>We can arrange the cubes:</p>
<ul>
<li>Length: 3 cubes in a row</li>
<li>Width: 2 cubes deep</li>
<li>Height: 2 cubes tall</li>
</ul>
<p>Total: \(3 \\times 2 \\times 2 =\) <strong>12 cubic units</strong></p>
</div>"""
    },
    {
        "title": "Units of Volume: cm³ and m³",
        "body": """<div class='concept-box'>
<h3>Real-World Cubic Units</h3>
<p>We don't use generic "units" — we use standard measurements:</p>
<ul>
<li><strong>cm³</strong> (cubic centimetres) — for small objects like boxes, books</li>
<li><strong>m³</strong> (cubic metres) — for large spaces like rooms, swimming pools</li>
</ul>
</div>

<div class='success-box'>
<h4>A \(1 \\text{ cm} \\times 1 \\text{ cm} \\times 1 \\text{ cm}\) cube = 1 cm³</h4>
<p>This is roughly the size of a sugar cube or dice.</p>
</div>

<div class='success-box'>
<h4>A \(1 \\text{ m} \\times 1 \\text{ m} \\times 1 \\text{ m}\) cube = 1 m³</h4>
<p>This is a huge cube — about the size of a small room corner.</p>
</div>

<div class='warning-box'>
<h3>The Big Conversion!</h3>
<p><strong>1 m = 100 cm</strong></p>
<p>So in 3D: <strong>\(1 \\text{ m}^3 = 100 \\times 100 \\times 100 = 1{,}000{,}000 \\text{ cm}^3\)</strong></p>
<p>One cubic metre contains <em>one million</em> cubic centimetres!</p>
</div>

<svg width="100%" viewBox="0 0 420 220" class="formula-box">
  <text x="210" y="22" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Size Comparison</text>

  <!-- Small cube (cm³) - 3D isometric -->
  <g>
    <rect x="35" y="55" width="40" height="40" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx='4'/>
    <polygon points="35,55 50,42 90,42 75,55" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" opacity='0.45'/>
    <polygon points="75,55 90,42 90,82 75,95" fill='#2d333b' stroke='#58a6ff' stroke-width="1.5" opacity='0.6'/>
    <text x="55" y="120" fill='currentColor' font-size='11' text-anchor='middle'>1 cm³</text>
    <text x="55" y="136" fill='#a0aec0' font-size='10' text-anchor='middle'>(sugar cube)</text>
  </g>

  <!-- Large cube (m³) - 3D isometric -->
  <g>
    <rect x="185" y="45" width="130" height="130" fill='#3d444d' stroke='#79c0ff' stroke-width="2" stroke-dasharray="5,5" rx='4'/>
    <polygon points="185,45 220,18 350,18 315,45" fill='#79c0ff' stroke='#79c0ff' stroke-width="1.5" stroke-dasharray="5,5" opacity='0.3'/>
    <polygon points="315,45 350,18 350,148 315,175" fill='#2d333b' stroke='#79c0ff' stroke-width="1.5" stroke-dasharray="5,5" opacity='0.4'/>
    <text x="250" y="195" fill='currentColor' font-size='11' text-anchor='middle'>1 m³</text>
    <text x="250" y="211" fill='#a0aec0' font-size='10' text-anchor='middle'>(1,000,000 cm³)</text>
  </g>
</svg>"""
    },
    {
        "title": "Volume vs. Capacity: Holding Things",
        "body": """<div class='concept-box'>
<h3>What's the Difference?</h3>
<ul>
<li><strong>Volume:</strong> The 3D space inside a solid (in cm³ or m³)</li>
<li><strong>Capacity:</strong> How much liquid or material a container can <em>hold</em> (in mL or L)</li>
</ul>
<p>They're closely linked: A container's volume tells us its capacity!</p>
</div>

<div class='success-box'>
<h4>The Key Connection</h4>
<p><strong>1 mL = 1 cm³</strong> (exactly!)</p>
<p><strong>1 L = 1000 mL = 1000 cm³</strong></p>
<p><strong>1 m³ = 1000 L</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example:</strong> A juice box is \(10 \\text{ cm} \\times 5 \\text{ cm} \\times 8 \\text{ cm}\). What is its capacity in mL?</p>
<ul>
<li>Volume = \(10 \\times 5 \\times 8 = 400\) cm³</li>
<li>Since 1 cm³ = 1 mL: Capacity = <strong>400 mL</strong></li>
</ul>
</div>

<div class='worked-example'>
<p><strong>Example:</strong> A water tank holds 500 L. What is its volume in cm³?</p>
<ul>
<li>\(500 \\text{ L} = 500 \\times 1000 \\text{ mL} = 500{,}000 \\text{ mL}\)</li>
<li>Since 1 mL = 1 cm³: Volume = <strong>500,000 cm³</strong></li>
</ul>
</div>

<svg width="100%" viewBox="0 0 420 190" class="formula-box">
  <text x="210" y="25" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Quick Reference</text>

  <rect x="20" y="45" width="175" height="125" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx="4"/>
  <text x="35" y="68" fill='#79c0ff' font-size='12' font-weight='bold'>Volume</text>
  <text x="35" y="90" fill='currentColor' font-size='11'>1 cm³</text>
  <text x="35" y="110" fill='currentColor' font-size='11'>1 m³ = 1,000,000 cm³</text>
  <text x="35" y="130" fill='currentColor' font-size='11'>Units: cm³, m³</text>
  <text x="35" y="150" fill='currentColor' font-size='11'>Measured: 3D space</text>

  <rect x="225" y="45" width="175" height="125" fill='#3d444d' stroke='#79c0ff' stroke-width="2" rx="4"/>
  <text x="240" y="68" fill='#79c0ff' font-size='12' font-weight='bold'>Capacity</text>
  <text x="240" y="90" fill='currentColor' font-size='11'>1 mL</text>
  <text x="240" y="110" fill='currentColor' font-size='11'>1 L = 1000 mL</text>
  <text x="240" y="130" fill='currentColor' font-size='11'>Units: mL, L</text>
  <text x="240" y="150" fill='currentColor' font-size='11'>What it can hold</text>
</svg>"""
    }
]
