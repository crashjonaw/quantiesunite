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
<p><strong>Volume = Length × Width × Height</strong></p>
</div>

<svg width="100%" viewBox="0 0 400 300" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>Cuboid with Dimensions</text>

  <!-- Front face -->
  <rect x="100" y="100" width="100" height="60" fill='#3d444d' stroke='#58a6ff' stroke-width="2"/>

  <!-- Top face (isometric) -->
  <polygon points="100,100 130,75 230,75 200,100" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.5'/>

  <!-- Right face -->
  <polygon points="200,100 230,75 230,135 200,160" fill='#3d444d' stroke='#58a6ff' stroke-width="2" opacity='0.7'/>

  <!-- Edges -->
  <line x1="100" y1="100" x2="130" y2="75" stroke='#58a6ff' stroke-width="2"/>
  <line x1="200" y1="100" x2="230" y2="75" stroke='#58a6ff' stroke-width="2"/>
  <line x1="200" y1="160" x2="230" y2="135" stroke='#58a6ff' stroke-width="2"/>

  <!-- Dimension labels -->
  <text x="85" y="135" fill='#79c0ff' font-size='12' font-weight='bold'>h</text>
  <text x="140" y="190" fill='#79c0ff' font-size='12' font-weight='bold'>l</text>
  <text x="220" y="120" fill='#79c0ff' font-size='12' font-weight='bold'>w</text>

  <!-- Formula -->
  <text x="20" y="260" fill='currentColor' font-size='12'>V = l × w × h</text>
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

<canvas id="vol_cuboid_example" style="max-width:100%; margin-top:15px;"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('vol_cuboid_example'), {
  type: 'bar',
  data: {
    labels: ['Example 1\n(8×5×3)', 'Example 2\n(10×4×2.5)', 'Example 3\n(20×15×10)'],
    datasets: [{
      label: 'Volume (cm³ or m³)',
      data: [120, 100, 3000],
      backgroundColor: ['#58a6ff', '#79c0ff', '#1f6feb'],
      borderColor: '#30363d',
      borderWidth: 2
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
<p><strong>Check:</strong> 10 × 4 × 5 = 200 ✓</p>
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
<p>Imagine a rectangular base (length × width). Now stack it upward by the height. That's your volume!</p>
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

<svg width="100%" viewBox="0 0 400 280" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>Stacking Layers Concept</text>

  <!-- Base -->
  <rect x="50" y="180" width="100" height="70" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.6'/>
  <text x="100" y="235" fill='currentColor' font-size='11' text-anchor='middle' font-weight='bold'>Base Area</text>

  <!-- One layer up -->
  <rect x="60" y="150" width="100" height="20" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>

  <!-- Two layers up -->
  <rect x="70" y="120" width="100" height="20" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>

  <!-- Three layers up -->
  <rect x="80" y="90" width="100" height="20" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5"/>

  <!-- Height arrow and label -->
  <line x1="200" y1="90" x2="200" y2="180" stroke='#79c0ff' stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="215" y="140" fill='#79c0ff' font-size='11' font-weight='bold'>Height</text>

  <text x="20" y="260" fill='currentColor' font-size='12'>V = Base Area × Height = Stacking layers</text>
</svg>"""
    }
]
