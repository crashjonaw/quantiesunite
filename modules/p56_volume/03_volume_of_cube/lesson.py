TITLE = "Volume of Cubes (Special Cuboids)"

SECTIONS = [
    {
        "title": "What's a Cube?",
        "body": """<div class='concept-box'>
<h3>A Cube is a Special Cuboid</h3>
<p>A <strong>cube</strong> is a cuboid where <strong>all three dimensions are equal</strong>:</p>
<p>\\(l = w = h = s\\)</p>
<p>Where <strong>s</strong> is the side length.</p>
<p>Think of: a dice, a sugar cube, or a Rubik's cube.</p>
</div>

<svg width="100%" viewBox="0 0 400 300" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>All sides are equal</text>

  <!-- Cube with all sides labeled -->
  <!-- Front face -->
  <rect x="100" y="100" width="80" height="80" fill='#3d444d' stroke='#58a6ff' stroke-width="2"/>

  <!-- Top face -->
  <polygon points="100,100 130,70 210,70 180,100" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.5'/>

  <!-- Right face -->
  <polygon points="180,100 210,70 210,150 180,180" fill='#3d444d' stroke='#58a6ff' stroke-width="2" opacity='0.7'/>

  <!-- Edges -->
  <line x1="100" y1="100" x2="130" y2="70" stroke='#58a6ff' stroke-width="2"/>
  <line x1="180" y1="100" x2="210" y2="70" stroke='#58a6ff' stroke-width="2"/>
  <line x1="180" y1="180" x2="210" y2="150" stroke='#58a6ff' stroke-width="2"/>

  <!-- All dimensions labeled as 's' -->
  <text x="80" y="145" fill='#79c0ff' font-size='14' font-weight='bold'>s</text>
  <text x="130" y="190" fill='#79c0ff' font-size='14' font-weight='bold'>s</text>
  <text x="215" y="125" fill='#79c0ff' font-size='14' font-weight='bold'>s</text>

  <!-- Formula -->
  <text x="20" y="260" fill='currentColor' font-size='12'>All sides = s (the side length)</text>
</svg>"""
    },
    {
        "title": "The Cube Volume Formula",
        "body": """<div class='success-box'>
<h3>Formula for Cube Volume</h3>
<p>Since a cube is just a cuboid with \\(l = w = h = s\\):</p>
<p>\\(V = s \\times s \\times s = s^3\\)</p>
<p><strong>Volume = side³</strong></p>
</div>

<div class='concept-box'>
<h3>Understanding s³ (side cubed)</h3>
<p>s³ means "s × s × s" — multiply the side length by itself three times.</p>
<p>This is why we call it <em>cubic</em> units!</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cube has side length 4 cm. Find its volume.</p>
<p>\\(V = s^3 = 4^3 = 4 \\times 4 \\times 4\\)</p>
<p>\\(V = 16 \\times 4 = 64 \\text{ cm}^3\\)</p>
<p><strong>Answer: 64 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A cube-shaped box has side 10 cm. What is its volume?</p>
<p>\\(V = 10^3 = 10 \\times 10 \\times 10 = 1000 \\text{ cm}^3 = 1 \\text{ L}\\)</p>
<p><strong>Answer: 1000 cm³ (or 1 L)</strong></p>
<p>This is exactly 1 litre! A 10 cm cube holds 1 litre of liquid.</p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A cube-shaped room has side 3 m. Find the volume of air inside.</p>
<p>\\(V = 3^3 = 27 \\text{ m}^3\\)</p>
<p><strong>Answer: 27 m³</strong></p>
</div>

<canvas id="vol_cube_progression" style="max-width:100%; margin-top:15px;"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('vol_cube_progression'), {
  type: 'line',
  data: {
    labels: ['Side = 1', 'Side = 2', 'Side = 3', 'Side = 4', 'Side = 5'],
    datasets: [{
      label: 'Volume (cubic units)',
      data: [1, 8, 27, 64, 125],
      borderColor: '#58a6ff',
      backgroundColor: 'rgba(88, 166, 255, 0.1)',
      borderWidth: 3,
      fill: true,
      tension: 0.4,
      pointRadius: 5,
      pointBackgroundColor: '#79c0ff'
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { labels: { color: '#e6edf3' } }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { color: '#e6edf3' },
        grid: { color: '#30363d' }
      },
      x: {
        ticks: { color: '#e6edf3' },
        grid: { color: '#30363d' }
      }
    }
  }
});
</script>"""
    },
    {
        "title": "Finding the Side Length from Volume",
        "body": """<div class='concept-box'>
<h3>Working Backwards: Cube Root</h3>
<p>Sometimes you know the volume but need to find the side length. Use the <strong>cube root</strong>:</p>
<p>\\(s = \\sqrt[3]{V}\\)</p>
<p>Cube root asks: "What number × itself × itself = V?"</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cube has a volume of 125 cm³. Find the side length.</p>
<p>\\(s = \\sqrt[3]{125}\\)</p>
<p>We need: s × s × s = 125</p>
<p>Try: 5 × 5 × 5 = 25 × 5 = 125 ✓</p>
<p>\\(s = 5 \\text{ cm}\\)</p>
<p><strong>Answer: 5 cm</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A cube-shaped container has volume 64 cm³. What is its side length?</p>
<p>\\(s = \\sqrt[3]{64}\\)</p>
<p>We need: s × s × s = 64</p>
<p>Try: 4 × 4 × 4 = 16 × 4 = 64 ✓</p>
<p>\\(s = 4 \\text{ cm}\\)</p>
<p><strong>Answer: 4 cm</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A cube has volume 1000 cm³. Find its side.</p>
<p>\\(s = \\sqrt[3]{1000}\\)</p>
<p>Try: 10 × 10 × 10 = 1000 ✓</p>
<p>\\(s = 10 \\text{ cm}\\)</p>
<p><strong>Answer: 10 cm</strong></p>
<p><strong>Remember:</strong> This cube holds exactly 1 litre of water!</p>
</div>

<svg width="100%" viewBox="0 0 400 250" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>Perfect Cubes (Common Values)</text>

  <g>
    <rect x="20" y="45" width="85" height="180" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx="4"/>
    <text x="62" y="65" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>Side</text>
    <text x="62" y="90" fill='currentColor' font-size='10' text-anchor='middle'>1</text>
    <text x="62" y="115" fill='currentColor' font-size='10' text-anchor='middle'>2</text>
    <text x="62" y="140" fill='currentColor' font-size='10' text-anchor='middle'>3</text>
    <text x="62" y="165" fill='currentColor' font-size='10' text-anchor='middle'>4</text>
    <text x="62" y="190" fill='currentColor' font-size='10' text-anchor='middle'>5</text>
    <text x="62" y="215" fill='currentColor' font-size='10' text-anchor='middle'>10</text>
  </g>

  <g>
    <rect x="135" y="45" width="85" height="180" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx="4"/>
    <text x="177" y="65" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>Volume</text>
    <text x="177" y="90" fill='currentColor' font-size='10' text-anchor='middle'>1</text>
    <text x="177" y="115" fill='currentColor' font-size='10' text-anchor='middle'>8</text>
    <text x="177" y="140" fill='currentColor' font-size='10' text-anchor='middle'>27</text>
    <text x="177" y="165" fill='currentColor' font-size='10' text-anchor='middle'>64</text>
    <text x="177" y="190" fill='currentColor' font-size='10' text-anchor='middle'>125</text>
    <text x="177" y="215" fill='currentColor' font-size='10' text-anchor='middle'>1000</text>
  </g>

  <g>
    <rect x="250" y="45" width="110" height="180" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx="4"/>
    <text x="305" y="65" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>Capacity</text>
    <text x="305" y="90" fill='currentColor' font-size='10' text-anchor='middle'>1 mL</text>
    <text x="305" y="115" fill='currentColor' font-size='10' text-anchor='middle'>8 mL</text>
    <text x="305" y="140" fill='currentColor' font-size='10' text-anchor='middle'>27 mL</text>
    <text x="305" y="165" fill='currentColor' font-size='10' text-anchor='middle'>64 mL</text>
    <text x="305" y="190" fill='currentColor' font-size='10' text-anchor='middle'>125 mL</text>
    <text x="305" y="215" fill='currentColor' font-size='10' text-anchor='middle'>1 L</text>
  </g>
</svg>"""
    },
    {
        "title": "Cubes vs. Cuboids: Quick Comparison",
        "body": """<div class='success-box'>
<h3>Key Differences</h3>
<table style="width: 100%; border-collapse: collapse">
<tr style="background: #3d444d">
<th style="padding:10px; text-align:left;">Property</th>
<th style="padding:10px; text-align:left;">Cuboid</th>
<th style="padding:10px; text-align:left;">Cube</th>
</tr>
<tr >
<td style="padding:10px;"><strong>Shape</strong></td>
<td style="padding:10px;">6 rectangular faces</td>
<td style="padding:10px;">6 square faces</td>
</tr>
<tr style="">
<td style="padding:10px;"><strong>Dimensions</strong></td>
<td style="padding:10px;">l ≠ w ≠ h (can be different)</td>
<td style="padding:10px;">l = w = h = s (all equal)</td>
</tr>
<tr >
<td style="padding:10px;"><strong>Formula</strong></td>
<td style="padding:10px;">V = l × w × h</td>
<td style="padding:10px;">V = s³</td>
</tr>
<tr style="">
<td style="padding:10px;"><strong>Examples</strong></td>
<td style="padding:10px;">Cereal box, brick, shoe box</td>
<td style="padding:10px;">Dice, sugar cube, ice cube</td>
</tr>
</table>
</div>

<div class='worked-example'>
<p><strong>Quick Comparison:</strong> Which is bigger — a cube with side 5 cm, or a cuboid with dimensions 6 × 5 × 4 cm?</p>
<p><strong>Cube:</strong> V = 5³ = 125 cm³</p>
<p><strong>Cuboid:</strong> V = 6 × 5 × 4 = 120 cm³</p>
<p><strong>Answer:</strong> The cube is slightly bigger (125 > 120).</p>
</div>"""
    }
]
