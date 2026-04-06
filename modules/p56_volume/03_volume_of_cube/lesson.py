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

<svg width="100%" viewBox="0 0 320 200" class="formula-box">
  <text x="160" y="20" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>All sides are equal</text>

  <!-- Cube - centred in viewBox -->
  <!-- Front face -->
  <rect x="110" y="70" width="80" height="80" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <!-- Top face -->
  <polygon points="110,70 140,42 220,42 190,70" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.5'/>
  <!-- Right face -->
  <polygon points="190,70 220,42 220,122 190,150" fill='#3d444d' stroke='#58a6ff' stroke-width="2" opacity='0.7'/>
  <!-- Edges -->
  <line x1="110" y1="70" x2="140" y2="42" stroke='#58a6ff' stroke-width="2"/>
  <line x1="190" y1="70" x2="220" y2="42" stroke='#58a6ff' stroke-width="2"/>
  <line x1="190" y1="150" x2="220" y2="122" stroke='#58a6ff' stroke-width="2"/>

  <!-- Dimension labels -->
  <text x="90" y="115" fill='#79c0ff' font-size='14' font-weight='bold' text-anchor='middle'>s</text>
  <text x="150" y="165" fill='#79c0ff' font-size='14' font-weight='bold' text-anchor='middle'>s</text>
  <text x="228" y="95" fill='#79c0ff' font-size='14' font-weight='bold' text-anchor='middle'>s</text>

  <!-- Formula -->
  <text x="160" y="190" fill='currentColor' font-size='12' text-anchor='middle'>All sides = s (the side length)</text>
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
<p>\(s^3\) means "\(s \times s \times s\)" — multiply the side length by itself three times.</p>
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
<p>Cube root asks: "What number \(\times\) itself \(\times\) itself \(= V\)?"</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cube has a volume of 125 cm³. Find the side length.</p>
<p>\\(s = \\sqrt[3]{125}\\)</p>
<p>We need: \(s \times s \times s = 125\)</p>
<p>Try: \(5 \times 5 \times 5 = 25 \times 5 = 125\) ✓</p>
<p>\\(s = 5 \\text{ cm}\\)</p>
<p><strong>Answer: 5 cm</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A cube-shaped container has volume 64 cm³. What is its side length?</p>
<p>\\(s = \\sqrt[3]{64}\\)</p>
<p>We need: \(s \times s \times s = 64\)</p>
<p>Try: \(4 \times 4 \times 4 = 16 \times 4 = 64\) ✓</p>
<p>\\(s = 4 \\text{ cm}\\)</p>
<p><strong>Answer: 4 cm</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A cube has volume 1000 cm³. Find its side.</p>
<p>\\(s = \\sqrt[3]{1000}\\)</p>
<p>Try: \(10 \times 10 \times 10 = 1000\) ✓</p>
<p>\\(s = 10 \\text{ cm}\\)</p>
<p><strong>Answer: 10 cm</strong></p>
<p><strong>Remember:</strong> This cube holds exactly 1 litre of water!</p>
</div>

<table style="width:100%; border-collapse:collapse; margin-top:12px;">
<tr style="background:#3d444d;">
<th style="padding:10px; text-align:center; border:1px solid #58a6ff;">Side (cm)</th>
<th style="padding:10px; text-align:center; border:1px solid #58a6ff;">Volume (cm&#179;)</th>
<th style="padding:10px; text-align:center; border:1px solid #58a6ff;">Capacity</th>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">1</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">1</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">1 mL</td>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">2</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">8</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">8 mL</td>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">3</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">27</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">27 mL</td>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">4</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">64</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">64 mL</td>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">5</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">125</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">125 mL</td>
</tr>
<tr>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">10</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">1000</td>
<td style="padding:10px; text-align:center; border:1px solid #30363d;">1 L</td>
</tr>
</table>"""
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
<td style="padding:10px;">\(l \neq w \neq h\) (can be different)</td>
<td style="padding:10px;">\(l = w = h = s\) (all equal)</td>
</tr>
<tr >
<td style="padding:10px;"><strong>Formula</strong></td>
<td style="padding:10px;">\(V = l \times w \times h\)</td>
<td style="padding:10px;">\(V = s^3\)</td>
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
<p><strong>Cube:</strong> \(V = 5^3 = 125\) cm³</p>
<p><strong>Cuboid:</strong> \(V = 6 \times 5 \times 4 = 120\) cm³</p>
<p><strong>Answer:</strong> The cube is slightly bigger (125 > 120).</p>
</div>"""
    }
]
