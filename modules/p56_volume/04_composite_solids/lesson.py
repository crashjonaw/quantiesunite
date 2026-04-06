TITLE = "Volume of Composite Solids"

SECTIONS = [
    {
        "title": "What Are Composite Solids?",
        "body": """<div class='concept-box'>
<h3>Breaking Down Complex Shapes</h3>
<p>A <strong>composite solid</strong> is a 3D shape made by <strong>combining two or more simple solids</strong> (cubes or cuboids).</p>
<p>Examples:</p>
<ul>
<li>An L-shaped box (two cuboids joined)</li>
<li>A T-shaped solid (three cuboids)</li>
<li>A plus-sign shape (multiple cuboids)</li>
</ul>
</div>

<div class='success-box'>
<h3>The Strategy</h3>
<p><strong>To find the volume of a composite solid:</strong></p>
<ol>
<li>Break it into simpler shapes (cuboids)</li>
<li>Find the volume of each part</li>
<li>Add them together: \\(V_{\\text{total}} = V_1 + V_2 + V_3 + ...\\)</li>
</ol>
</div>

<svg width="100%" viewBox="0 0 400 280" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>L-Shaped Composite Solid (Top View)</text>

  <!-- Vertical part of L -->
  <rect x="60" y="80" width="40" height="100" fill='#58a6ff' stroke='#79c0ff' stroke-width="2" opacity='0.6'/>
  <text x="80" y="140" fill='currentColor' font-size='11' font-weight='bold' text-anchor='middle'>Part 1</text>

  <!-- Horizontal part of L -->
  <rect x="100" y="160" width="100" height="40" fill='#1f6feb' stroke='#79c0ff' stroke-width="2" opacity='0.6'/>
  <text x="150" y="185" fill='currentColor' font-size='11' font-weight='bold' text-anchor='middle'>Part 2</text>

  <!-- Show them separately below -->
  <text x="20" y="250" fill='currentColor' font-size='12'>V_total = V_Part1 + V_Part2</text>
</svg>"""
    },
    {
        "title": "Adding Volumes: Simple Composites",
        "body": """<div class='worked-example'>
<p><strong>Example 1:</strong> An L-shaped solid is made of two cuboids:</p>
<ul>
<li>Vertical part: \(2 \text{ cm} \times 2 \text{ cm} \times 5 \text{ cm}\)</li>
<li>Horizontal part: \(4 \text{ cm} \times 2 \text{ cm} \times 2 \text{ cm}\)</li>
</ul>
<p>Find the total volume.</p>
<p>Step 1: Calculate Part 1</p>
<p>\\(V_1 = 2 \\times 2 \\times 5 = 20 \\text{ cm}^3\\)</p>
<p>Step 2: Calculate Part 2</p>
<p>\\(V_2 = 4 \\times 2 \\times 2 = 16 \\text{ cm}^3\\)</p>
<p>Step 3: Add together</p>
<p>\\(V_{\\text{total}} = 20 + 16 = 36 \\text{ cm}^3\\)</p>
<p><strong>Answer: 36 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A T-shaped solid consists of:</p>
<ul>
<li>Top horizontal bar: \(6 \text{ cm} \times 2 \text{ cm} \times 2 \text{ cm}\)</li>
<li>Vertical stem: \(2 \text{ cm} \times 2 \text{ cm} \times 5 \text{ cm}\)</li>
</ul>
<p>Find the volume (assume no overlap).</p>
<p>\\(V_1 = 6 \\times 2 \\times 2 = 24 \\text{ cm}^3\\)</p>
<p>\\(V_2 = 2 \\times 2 \\times 5 = 20 \\text{ cm}^3\\)</p>
<p>\\(V_{\\text{total}} = 24 + 20 = 44 \\text{ cm}^3\\)</p>
<p><strong>Answer: 44 cm³</strong></p>
</div>

<canvas id="vol_composite_add" style="max-width:100%; margin-top:15px;"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('vol_composite_add'), {
  type: 'bar',
  data: {
    labels: ['Part 1', 'Part 2', 'Total'],
    datasets: [{
      label: 'Volume (cm³)',
      data: [20, 16, 36],
      backgroundColor: ['#58a6ff', '#1f6feb', '#79c0ff'],
      borderColor: '#30363d',
      borderWidth: 2
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true,
    plugins: {
      legend: { labels: { color: '#e6edf3' } }
    },
    scales: {
      x: {
        beginAtZero: true,
        ticks: { color: '#e6edf3' },
        grid: { color: '#30363d' }
      },
      y: {
        ticks: { color: '#e6edf3' },
        grid: { color: '#30363d' }
      }
    }
  }
});
</script>"""
    },
    {
        "title": "Subtracting Volumes: Shapes with Holes",
        "body": """<div class='concept-box'>
<h3>When a Shape Has a Hole</h3>
<p>For shapes with holes or hollowed sections, we use <strong>subtraction</strong>:</p>
<p>\\(V_{\\text{final}} = V_{\\text{outer}} - V_{\\text{hole}}\\)</p>
<p>Start with the whole shape, then subtract the part that's been removed or hollowed out.</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cube with side 6 cm has a small cubic hole with side 2 cm drilled through it.</p>
<p>Step 1: Volume of outer cube</p>
<p>\\(V_{\\text{outer}} = 6^3 = 216 \\text{ cm}^3\\)</p>
<p>Step 2: Volume of hole</p>
<p>\\(V_{\\text{hole}} = 2^3 = 8 \\text{ cm}^3\\)</p>
<p>Step 3: Subtract</p>
<p>\\(V_{\\text{final}} = 216 - 8 = 208 \\text{ cm}^3\\)</p>
<p><strong>Answer: 208 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A rectangular block is \(10 \text{ cm} \times 8 \text{ cm} \times 6 \text{ cm}\). A smaller block \(4 \text{ cm} \times 3 \text{ cm} \times 3 \text{ cm}\) is removed from one corner.</p>
<p>\\(V_{\\text{outer}} = 10 \\times 8 \\times 6 = 480 \\text{ cm}^3\\)</p>
<p>\\(V_{\\text{removed}} = 4 \\times 3 \\times 3 = 36 \\text{ cm}^3\\)</p>
<p>\\(V_{\\text{final}} = 480 - 36 = 444 \\text{ cm}^3\\)</p>
<p><strong>Answer: 444 cm³</strong></p>
</div>

<svg width="100%" viewBox="0 0 400 280" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='13' font-weight='bold'>Cube with Hole Removed</text>

  <!-- Outer cube (hollow) -->
  <g>
    <!-- Front face -->
    <rect x="70" y="80" width="100" height="100" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
    <!-- Inner hole -->
    <rect x="95" y="105" width="50" height="50" fill='#161b22' stroke='#ff6b6b' stroke-width="2"/>
    <text x="145" y="135" fill='#ff6b6b' font-size='11' text-anchor='middle' font-weight='bold'>Hole</text>
  </g>

  <!-- Formula below -->
  <text x="20" y="230" fill='currentColor' font-size='12'>V = V_outer - V_hole = 216 - 8 = 208 cm³</text>

  <text x="20" y="255" fill='#a0aec0' font-size='11'>Remove the unwanted part from the total</text>
</svg>"""
    },
    {
        "title": "Real-World Applications & Word Problems",
        "body": """<div class='worked-example'>
<p><strong>Example 1:</strong> A swimming pool has an unusual shape. It can be thought of as two cuboids joined:</p>
<ul>
<li>Shallow end: \(20 \text{ m} \times 10 \text{ m} \times 1 \text{ m}\)</li>
<li>Deep end: \(10 \text{ m} \times 10 \text{ m} \times 2 \text{ m}\)</li>
</ul>
<p>How much water is needed to fill it completely?</p>
<p>\\(V_1 = 20 \\times 10 \\times 1 = 200 \\text{ m}^3\\)</p>
<p>\\(V_2 = 10 \\times 10 \\times 2 = 200 \\text{ m}^3\\)</p>
<p>\\(V_{\\text{total}} = 200 + 200 = 400 \\text{ m}^3 = 400,000 \\text{ L}\\)</p>
<p><strong>Answer: 400,000 litres of water</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A shipping container is L-shaped. Calculate its internal volume:</p>
<ul>
<li>Vertical section: \(3 \text{ m} \times 2 \text{ m} \times 4 \text{ m}\)</li>
<li>Horizontal section: \(5 \text{ m} \times 2 \text{ m} \times 2 \text{ m}\)</li>
</ul>
<p>\\(V_1 = 3 \\times 2 \\times 4 = 24 \\text{ m}^3\\)</p>
<p>\\(V_2 = 5 \\times 2 \\times 2 = 20 \\text{ m}^3\\)</p>
<p>\\(V_{\\text{total}} = 24 + 20 = 44 \\text{ m}^3\\)</p>
<p><strong>Answer: 44 m³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A storage box has outer dimensions \(30 \text{ cm} \times 25 \text{ cm} \times 20 \text{ cm}\) with walls 2 cm thick. Find the internal volume (where items can be stored).</p>
<p>Internal dimensions: \((30 - 2 \times 2) \times (25 - 2 \times 2) \times (20 - 2) = 26 \times 21 \times 18\) cm</p>
<p>\\(V_{\\text{internal}} = 26 \\times 21 \\times 18 = 9828 \\text{ cm}^3\\)</p>
<p><strong>Answer: 9828 cm³ ≈ 9.8 L</strong></p>
</div>

<div class='success-box'>
<h3>Checking Your Work</h3>
<p>When solving composite solid problems:</p>
<ul>
<li>Always identify all the separate shapes first</li>
<li>Measure or identify all dimensions clearly</li>
<li>Calculate each part's volume separately</li>
<li>Add (if joining) or subtract (if removing) carefully</li>
<li>Check: Does the answer make sense? Is it reasonable?</li>
</ul>
</div>"""
    }
]
