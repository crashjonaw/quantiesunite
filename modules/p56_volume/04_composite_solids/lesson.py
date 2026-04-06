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
<li>Add them together: \\(V_{\\mathrm{total}} = V_1 + V_2 + V_3 + ...\\)</li>
</ol>
</div>

<svg width="100%" viewBox="0 0 400 240" class="formula-box">
  <text x="200" y="22" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>L-Shaped Composite Solid (Top View)</text>

  <!-- Vertical part of L -->
  <rect x="100" y="45" width="50" height="110" fill='#58a6ff' stroke='#79c0ff' stroke-width="2" rx='4' opacity='0.6'/>
  <text x="125" y="105" fill='currentColor' font-size='11' font-weight='bold' text-anchor='middle'>Part 1</text>

  <!-- Horizontal part of L -->
  <rect x="150" y="115" width="120" height="40" fill='#1f6feb' stroke='#79c0ff' stroke-width="2" rx='4' opacity='0.6'/>
  <text x="210" y="140" fill='currentColor' font-size='11' font-weight='bold' text-anchor='middle'>Part 2</text>

  <!-- Dimension labels -->
  <text x="88" y="100" fill='#79c0ff' font-size='10' text-anchor='end'>h</text>
  <text x="125" y="40" fill='#79c0ff' font-size='10' text-anchor='middle'>w</text>
  <text x="210" y="164" fill='#79c0ff' font-size='10' text-anchor='middle'>l</text>

  <!-- Plus sign between parts -->
  <text x="290" y="100" fill='#79c0ff' font-size='16' font-weight='bold' text-anchor='middle'>+</text>

  <!-- Separate parts on right -->
  <rect x="310" y="55" width="30" height="60" fill='#58a6ff' stroke='#79c0ff' stroke-width="1.5" rx='4' opacity='0.5'/>
  <text x="325" y="90" fill='currentColor' font-size='9' text-anchor='middle'>V1</text>
  <rect x="310" y="125" width="60" height="25" fill='#1f6feb' stroke='#79c0ff' stroke-width="1.5" rx='4' opacity='0.5'/>
  <text x="340" y="142" fill='currentColor' font-size='9' text-anchor='middle'>V2</text>

  <!-- Formula -->
  <text x="200" y="195" fill='currentColor' font-size='12' text-anchor='middle'>V_total = V_Part1 + V_Part2</text>
  <text x="200" y="215" fill='#a0aec0' font-size='11' text-anchor='middle'>Break into simpler shapes, then add volumes</text>
</svg>"""
    },
    {
        "title": "Adding Volumes: Simple Composites",
        "body": """<div class='worked-example'>
<p><strong>Example 1:</strong> An L-shaped solid is made of two cuboids:</p>
<ul>
<li>Vertical part: 2 cm \\(\\times\\) 2 cm \\(\\times\\) 5 cm</li>
<li>Horizontal part: 4 cm \\(\\times\\) 2 cm \\(\\times\\) 2 cm</li>
</ul>
<p>Find the total volume.</p>
<p>Step 1: Calculate Part 1</p>
<p>\\(V_1 = 2 \\times 2 \\times 5 = 20\\) cm³</p>
<p>Step 2: Calculate Part 2</p>
<p>\\(V_2 = 4 \\times 2 \\times 2 = 16\\) cm³</p>
<p>Step 3: Add together</p>
<p>\\(V_{\\mathrm{total}} = 20 + 16 = 36\\) cm³</p>
<p><strong>Answer: 36 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A T-shaped solid consists of:</p>
<ul>
<li>Top horizontal bar: 6 cm \\(\\times\\) 2 cm \\(\\times\\) 2 cm</li>
<li>Vertical stem: 2 cm \\(\\times\\) 2 cm \\(\\times\\) 5 cm</li>
</ul>
<p>Find the volume (assume no overlap).</p>
<p>\\(V_1 = 6 \\times 2 \\times 2 = 24\\) cm³</p>
<p>\\(V_2 = 2 \\times 2 \\times 5 = 20\\) cm³</p>
<p>\\(V_{\\mathrm{total}} = 24 + 20 = 44\\) cm³</p>
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
<p>\\(V_{\\mathrm{final}} = V_{\\mathrm{outer}} - V_{\\mathrm{hole}}\\)</p>
<p>Start with the whole shape, then subtract the part that's been removed or hollowed out.</p>
</div>

<div class='worked-example'>
<p><strong>Example 1:</strong> A cube with side 6 cm has a small cubic hole with side 2 cm drilled through it.</p>
<p>Step 1: Volume of outer cube</p>
<p>\\(V_{\\mathrm{outer}} = 6^3 = 216 \\mathrm{ cm}^3\\)</p>
<p>Step 2: Volume of hole</p>
<p>\\(V_{\\mathrm{hole}} = 2^3 = 8 \\mathrm{ cm}^3\\)</p>
<p>Step 3: Subtract</p>
<p>\\(V_{\\mathrm{final}} = 216 - 8 = 208 \\mathrm{ cm}^3\\)</p>
<p><strong>Answer: 208 cm³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A rectangular block is 10 cm \(\times\) 8 cm \(\times\) 6 cm. A smaller block 4 cm \(\times\) 3 cm \(\times\) 3 cm is removed from one corner.</p>
<p>\\(V_{\\mathrm{outer}} = 10 \\times 8 \\times 6 = 480 \\mathrm{ cm}^3\\)</p>
<p>\\(V_{\\mathrm{removed}} = 4 \\times 3 \\times 3 = 36 \\mathrm{ cm}^3\\)</p>
<p>\\(V_{\\mathrm{final}} = 480 - 36 = 444 \\mathrm{ cm}^3\\)</p>
<p><strong>Answer: 444 cm³</strong></p>
</div>

<svg width="100%" viewBox="0 0 400 250" class="formula-box">
  <text x="200" y="22" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>Cube with Hole Removed</text>

  <!-- Outer cube - 3D isometric view -->
  <!-- Front face -->
  <rect x="90" y="70" width="100" height="100" fill='#3d444d' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <!-- Top face -->
  <polygon points="90,70 120,44 220,44 190,70" fill='#58a6ff' stroke='#58a6ff' stroke-width="2" opacity='0.4'/>
  <!-- Right face -->
  <polygon points="190,70 220,44 220,144 190,170" fill='#3d444d' stroke='#58a6ff' stroke-width="2" opacity='0.6'/>

  <!-- Hole through front face -->
  <rect x="120" y="100" width="40" height="40" fill='#161b22' stroke='#ff6b6b' stroke-width="2" rx='2'/>
  <!-- Hole depth lines -->
  <line x1="160" y1="100" x2="175" y2="86" stroke='#ff6b6b' stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="160" y1="140" x2="175" y2="126" stroke='#ff6b6b' stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Labels -->
  <text x="140" y="125" fill='#ff6b6b' font-size='10' font-weight='bold' text-anchor='middle'>Hole</text>
  <text x="78" y="125" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='end'>6 cm</text>
  <text x="140" y="185" fill='#79c0ff' font-size='11' font-weight='bold' text-anchor='middle'>6 cm</text>
  <text x="132" y="95" fill='#ff6b6b' font-size='9' text-anchor='middle'>2 cm</text>

  <!-- Minus sign and separate shapes -->
  <text x="250" y="115" fill='currentColor' font-size='18' font-weight='bold' text-anchor='middle'>=</text>

  <!-- Small outer cube -->
  <rect x="275" y="75" width="45" height="45" fill='#3d444d' stroke='#58a6ff' stroke-width="1.5" rx='4'/>
  <text x="297" y="103" fill='currentColor' font-size='9' text-anchor='middle'>216</text>

  <text x="335" y="100" fill='currentColor' font-size='16' font-weight='bold' text-anchor='middle'>-</text>

  <!-- Small hole cube -->
  <rect x="350" y="85" width="25" height="25" fill='#161b22' stroke='#ff6b6b' stroke-width="1.5" rx='2'/>
  <text x="362" y="103" fill='#ff6b6b' font-size='9' text-anchor='middle'>8</text>

  <!-- Formula -->
  <text x="200" y="215" fill='currentColor' font-size='12' text-anchor='middle'>V = V_outer - V_hole = 216 - 8 = 208 cm³</text>
  <text x="200" y="237" fill='#a0aec0' font-size='11' text-anchor='middle'>Remove the unwanted part from the total</text>
</svg>"""
    },
    {
        "title": "Real-World Applications & Word Problems",
        "body": """<div class='worked-example'>
<p><strong>Example 1:</strong> A swimming pool has an unusual shape. It can be thought of as two cuboids joined:</p>
<ul>
<li>Shallow end: 20 m \(\times\) 10 m \(\times\) 1 m</li>
<li>Deep end: 10 m \(\times\) 10 m \(\times\) 2 m</li>
</ul>
<p>How much water is needed to fill it completely?</p>
<p>\\(V_1 = 20 \\times 10 \\times 1 = 200 \\mathrm{ m}^3\\)</p>
<p>\\(V_2 = 10 \\times 10 \\times 2 = 200 \\mathrm{ m}^3\\)</p>
<p>\\(V_{\\mathrm{total}} = 200 + 200 = 400 \\mathrm{ m}^3 = 400,000 \\mathrm{ L}\\)</p>
<p><strong>Answer: 400,000 litres of water</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 2:</strong> A shipping container is L-shaped. Calculate its internal volume:</p>
<ul>
<li>Vertical section: 3 m \(\times\) 2 m \(\times\) 4 m</li>
<li>Horizontal section: 5 m \(\times\) 2 m \(\times\) 2 m</li>
</ul>
<p>\\(V_1 = 3 \\times 2 \\times 4 = 24 \\mathrm{ m}^3\\)</p>
<p>\\(V_2 = 5 \\times 2 \\times 2 = 20 \\mathrm{ m}^3\\)</p>
<p>\\(V_{\\mathrm{total}} = 24 + 20 = 44 \\mathrm{ m}^3\\)</p>
<p><strong>Answer: 44 m³</strong></p>
</div>

<div class='worked-example'>
<p><strong>Example 3:</strong> A storage box has outer dimensions 30 cm \(\times\) 25 cm \(\times\) 20 cm with walls 2 cm thick. Find the internal volume (where items can be stored).</p>
<p>Internal dimensions: \((30 - 2 \times 2) \times (25 - 2 \times 2) \times (20 - 2) = 26 \times 21 \times 18\) cm</p>
<p>\\(V_{\\mathrm{internal}} = 26 \\times 21 \\times 18 = 9828 \\mathrm{ cm}^3\\)</p>
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
