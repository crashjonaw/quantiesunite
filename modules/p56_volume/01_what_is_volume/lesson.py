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

<svg width="100%" viewBox="0 0 400 300" class="formula-box">
  <!-- Flat square (2D) -->
  <g>
    <text x="50" y="20" fill='currentColor' font-size='14' font-weight='bold'>2D: Area</text>
    <rect x="20" y="40" width="80" height="80" fill='none' stroke='#58a6ff' stroke-width="2"/>
    <text x="45" y="140" fill='currentColor' font-size='12'>4 × 4 = 16 sq units</text>
  </g>

  <!-- 3D cube -->
  <g>
    <text x="250" y="20" fill='currentColor' font-size='14' font-weight='bold'>3D: Volume</text>
    <!-- Front face -->
    <rect x="220" y="50" width="70" height="70" fill='#3d444d' stroke='#58a6ff' stroke-width="2"/>
    <!-- Top face -->
    <polygon points="220,50 245,25 315,25 290,50" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.5'/>
    <!-- Right face -->
    <polygon points="290,50 315,25 315,95 290,120" fill='#3d444d' stroke='#58a6ff' stroke-width="2" opacity='0.7'/>
    <!-- Edges -->
    <line x1="220" y1="50" x2="245" y2="25" stroke='#58a6ff' stroke-width="2"/>
    <line x1="290" y1="50" x2="315" y2="25" stroke='#58a6ff' stroke-width="2"/>
    <line x1="290" y1="120" x2="315" y2="95" stroke='#58a6ff' stroke-width="2"/>
    <text x="230" y="140" fill='currentColor' font-size='12'>4 × 4 × 4 = 64 cubic units</text>
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

<svg width="100%" viewBox="0 0 400 300" class="formula-box">
  <!-- 2×2×2 cube made of unit cubes -->
  <g>
    <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>A 2 × 2 × 2 cube has 8 unit cubes</text>

    <!-- Layer 1 (back) -->
    <rect x="60" y="80" width="40" height="40" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>
    <rect x="100" y="80" width="40" height="40" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>
    <rect x="60" y="120" width="40" height="40" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>
    <rect x="100" y="120" width="40" height="40" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>

    <!-- Layer 2 (front) - slightly offset -->
    <rect x="70" y="60" width="40" height="40" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" opacity='0.6'/>
    <rect x="110" y="60" width="40" height="40" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" opacity='0.6'/>
    <rect x="70" y="100" width="40" height="40" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" opacity='0.6'/>
    <rect x="110" y="100" width="40" height="40" fill='#58a6ff' stroke='#58a6ff' stroke-width="1.5" opacity='0.6'/>

    <text x="60" y="220" fill='currentColor' font-size='12'>Volume = 2 × 2 × 2 = 8 cubic units</text>
  </g>
</svg>

<div class='worked-example'>
<p><strong>Example:</strong> A box is 3 units long, 2 units wide, and 2 units tall. How many unit cubes fit inside?</p>
<p>We can arrange the cubes:</p>
<ul>
<li>Length: 3 cubes in a row</li>
<li>Width: 2 cubes deep</li>
<li>Height: 2 cubes tall</li>
</ul>
<p>Total: \(3 \times 2 \times 2 =\) <strong>12 cubic units</strong></p>
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
<h4>A \(1 \text{ cm} \times 1 \text{ cm} \times 1 \text{ cm}\) cube = 1 cm³</h4>
<p>This is roughly the size of a sugar cube or dice.</p>
</div>

<div class='success-box'>
<h4>A \(1 \text{ m} \times 1 \text{ m} \times 1 \text{ m}\) cube = 1 m³</h4>
<p>This is a huge cube — about the size of a small room corner.</p>
</div>

<div class='warning-box'>
<h3>The Big Conversion!</h3>
<p><strong>1 m = 100 cm</strong></p>
<p>So in 3D: <strong>\(1 \text{ m}^3 = 100 \times 100 \times 100 = 1{,}000{,}000 \text{ cm}^3\)</strong></p>
<p>One cubic metre contains <em>one million</em> cubic centimetres!</p>
</div>

<svg width="100%" viewBox="0 0 400 200" class="formula-box">
  <text x="20" y="30" fill='currentColor' font-size='13' font-weight='bold'>Size Comparison</text>

  <!-- Small cube (cm³) -->
  <g>
    <rect x="40" y="50" width="40" height="40" fill='none' stroke='#58a6ff' stroke-width="2"/>
    <text x="35" y="110" fill='currentColor' font-size='11' text-anchor='middle'>1 cm³</text>
    <text x="60" y="140" fill='#a0aec0' font-size='10' text-anchor='middle'>(sugar cube)</text>
  </g>

  <!-- Large cube (m³) -->
  <g>
    <rect x="180" y="50" width="120" height="120" fill='none' stroke='#79c0ff' stroke-width="2" stroke-dasharray="5,5"/>
    <text x="240" y="175" fill='currentColor' font-size='11' text-anchor='middle'>1 m³</text>
    <text x="240" y="195" fill='#a0aec0' font-size='10' text-anchor='middle'>(1,000,000 cm³)</text>
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
<p><strong>Example:</strong> A juice box is \(10 \text{ cm} \times 5 \text{ cm} \times 8 \text{ cm}\). What is its capacity in mL?</p>
<ul>
<li>Volume = \(10 \times 5 \times 8 = 400\) cm³</li>
<li>Since 1 cm³ = 1 mL: Capacity = <strong>400 mL</strong></li>
</ul>
</div>

<div class='worked-example'>
<p><strong>Example:</strong> A water tank holds 500 L. What is its volume in cm³?</p>
<ul>
<li>\(500 \text{ L} = 500 \times 1000 \text{ mL} = 500{,}000 \text{ mL}\)</li>
<li>Since 1 mL = 1 cm³: Volume = <strong>500,000 cm³</strong></li>
</ul>
</div>

<svg width="100%" viewBox="0 0 400 180" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>Quick Reference</text>

  <rect x="20" y="40" width="160" height="120" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx="4"/>
  <text x="30" y="60" fill='#79c0ff' font-size='12' font-weight='bold'>Volume</text>
  <text x="30" y="85" fill='currentColor' font-size='11'>1 cm³</text>
  <text x="30" y="105" fill='currentColor' font-size='11'>1 m³ = 1,000,000 cm³</text>
  <text x="30" y="125" fill='currentColor' font-size='11'>Units: cm³, m³</text>
  <text x="30" y="145" fill='currentColor' font-size='11'>Measured: 3D space</text>

  <rect x="220" y="40" width="160" height="120" fill='#3d444d' stroke='#79c0ff' stroke-width="2" rx="4"/>
  <text x="230" y="60" fill='#79c0ff' font-size='12' font-weight='bold'>Capacity</text>
  <text x="230" y="85" fill='currentColor' font-size='11'>1 mL</text>
  <text x="230" y="105" fill='currentColor' font-size='11'>1 L = 1000 mL</text>
  <text x="230" y="125" fill='currentColor' font-size='11'>Units: mL, L</text>
  <text x="230" y="145" fill='currentColor' font-size='11'>What it can hold</text>
</svg>"""
    }
]
