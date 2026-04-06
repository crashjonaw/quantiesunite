TITLE = "Patterns and Tricks: Master the Tables"

SECTIONS = [
    {
        "title": "The Commutative Property: The Best Shortcut",
        "body": """
<h3>Multiplication Works Both Ways</h3>
<p>One of the most important discoveries in multiplication is the <strong>commutative property</strong>: \\(a \\times b = b \\times a\\). The order doesn't matter!</p>

<div class="success-box">
<h4>Why This Saves You Work</h4>
<p>You only need to memorize half the facts! If you know \\(3 \\times 8 = 24\\), you automatically know \\(8 \\times 3 = 24\\) too.</p>
</div>

<h3>Visual Proof</h3>
<div class="diagram-container">
  <svg width="100%" viewBox="0 0 520 230">
    <text x="260" y="22" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>3 × 4 and 4 × 3 Are the Same</text>

    <!-- 3 rows, 4 columns -->
    <g>
      <text x="95" y="46" text-anchor='middle' font-size='11' font-weight='bold' fill='#4169E1'>3 rows × 4 cols = 12</text>
      <rect x="30" y="58" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="60" y="58" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="90" y="58" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="120" y="58" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="30" y="88" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="60" y="88" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="90" y="88" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="120" y="88" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="30" y="118" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="60" y="118" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="90" y="118" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
      <rect x="120" y="118" width="25" height="25" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="3"/>
    </g>

    <!-- Arrow in the middle -->
    <line x1="175" y1="100" x2="225" y2="100" stroke='currentColor' stroke-width="2" marker-end="url(#arrowhead)"/>
    <defs><marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6Z" fill='currentColor'/></marker></defs>
    <text x="200" y="88" text-anchor='middle' font-size='11' fill='currentColor'>Rotate</text>

    <!-- 4 rows, 3 columns -->
    <g>
      <text x="375" y="46" text-anchor='middle' font-size='11' font-weight='bold' fill='#22c55e'>4 rows × 3 cols = 12</text>
      <rect x="330" y="58" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="360" y="58" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="390" y="58" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="330" y="88" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="360" y="88" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="390" y="88" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="330" y="118" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="360" y="118" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="390" y="118" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="330" y="148" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="360" y="148" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
      <rect x="390" y="148" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="3"/>
    </g>

    <text x="260" y="210" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Same array, different orientation = same answer!</text>
  </svg>
  <div class="diagram-caption">Rotating an array shows that 3 × 4 = 4 × 3</div>
</div>

<h3>What This Means for Learning</h3>
<p>If you've learned facts for tables 1-6, you already know:</p>
<ul>
  <li>\\(2 \\times 7\\)? You know \\(7 \\times 2\\) = 14</li>
  <li>\\(3 \\times 9\\)? You know \\(9 \\times 3\\) = 27</li>
  <li>\\(5 \\times 12\\)? You know \\(12 \\times 5\\) = 60</li>
</ul>

<div class="concept-box">
<h4>The Power of Commutativity</h4>
<p>You only truly need to memorize about 28 facts (1-6 times tables in full, plus 7-12 × 7-12). The commutative property gives you the rest for free!</p>
</div>
"""
    },
    {
        "title": "Perfect Squares: Special Multiplications",
        "body": """
<h3>What Are Perfect Squares?</h3>
<p>When you multiply a number by itself (like \\(3 \\times 3\\) or \\(7 \\times 7\\)), the result is called a <strong>perfect square</strong>. These are special because the array is always a perfect square shape!</p>

<div class="concept-box">
<h4>The Perfect Squares</h4>
<ul>
  <li>\\(1 \\times 1 = 1\\) (1 is a perfect square)</li>
  <li>\\(2 \\times 2 = 4\\) (4 is a perfect square)</li>
  <li>\\(3 \\times 3 = 9\\) (9 is a perfect square)</li>
  <li>\\(4 \\times 4 = 16\\) (16 is a perfect square)</li>
  <li>\\(5 \\times 5 = 25\\) (25 is a perfect square)</li>
  <li>\\(6 \\times 6 = 36\\) (36 is a perfect square)</li>
  <li>\\(7 \\times 7 = 49\\) (49 is a perfect square)</li>
  <li>\\(8 \\times 8 = 64\\) (64 is a perfect square)</li>
  <li>\\(9 \\times 9 = 81\\) (81 is a perfect square)</li>
  <li>\\(10 \\times 10 = 100\\) (100 is a perfect square)</li>
  <li>\\(11 \\times 11 = 121\\) (121 is a perfect square)</li>
  <li>\\(12 \\times 12 = 144\\) (144 is a perfect square)</li>
</ul>
</div>

<h3>Visualizing Perfect Squares</h3>
<div class="diagram-container">
  <svg width="550" height="280" viewBox="0 0 550 280">
    <text x="275" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Perfect Squares: Visual Representation</text>

    <!-- 3 × 3 -->
    <g id="square-3">
      <text x="60" y="50" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>3 × 3 = 9</text>
      <rect x="20" y="70" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="45" y="70" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="70" y="70" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="20" y="95" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="45" y="95" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="70" y="95" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="20" y="120" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="45" y="120" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
      <rect x="70" y="120" width="20" height="20" fill='#4169E180' stroke='#4169E1' stroke-width="1"/>
    </g>

    <!-- 5 × 5 -->
    <g id="square-5">
      <text x="200" y="50" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>5 × 5 = 25</text>
      <g id="five-by-five">
        <rect x="160" y="70" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="180" y="70" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="200" y="70" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="220" y="70" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="240" y="70" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>

        <rect x="160" y="90" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="180" y="90" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="200" y="90" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="220" y="90" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="240" y="90" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>

        <rect x="160" y="110" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="180" y="110" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="200" y="110" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="220" y="110" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="240" y="110" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>

        <rect x="160" y="130" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="180" y="130" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="200" y="130" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="220" y="130" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="240" y="130" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>

        <rect x="160" y="150" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="180" y="150" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="200" y="150" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="220" y="150" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
        <rect x="240" y="150" width="15" height="15" fill='#22c55e80' stroke='#22c55e' stroke-width="1"/>
      </g>
    </g>

    <!-- 7 × 7 -->
    <g id="square-7">
      <text x="380" y="50" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>7 × 7 = 49</text>
      <g id="seven-by-seven">
        <rect x="340" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="355" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="370" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="385" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="400" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="415" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
        <rect x="430" y="70" width="12" height="12" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      </g>
    </g>

    <!-- Pattern explanation -->
    <rect x="40" y="210" width="480" height="50" fill='#e8f5e980' stroke='#22c55e' stroke-width="2" rx="5"/>
    <text x="50" y="235" font-size='12' font-weight='bold' fill='currentColor'>The Pattern in Perfect Squares:</text>
    <text x="50" y="255" font-size='11' fill='currentColor'>1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144</text>
  </svg>
  <div class="diagram-caption">Perfect squares have equal rows and columns</div>
</div>

<div class="success-box">
<h4>A Special Pattern in Perfect Squares</h4>
<p>Notice the differences between consecutive perfect squares:</p>
<ul>
  <li>\\(1 \\to 4\\): difference of 3 (= 1 + 2)</li>
  <li>\\(4 \\to 9\\): difference of 5 (= 2 + 3)</li>
  <li>\\(9 \\to 16\\): difference of 7 (= 3 + 4)</li>
</ul>

<p>The difference increases by 2 each time! This is because you're adding a whole new row and column to the square.</p>
</div>
"""
    },
    {
        "title": "Doubling Strategy: The Power of 2",
        "body": """
<h3>The Doubling Chain</h3>
<p>Doubling is a superpower in multiplication. When you understand one table, you can immediately understand the next by doubling!</p>

<div class="concept-box">
<h4>The Four Doubling Chains</h4>
<ul>
  <li><strong>Chain 1:</strong> 1 → 2 (double) → 4 (double) → 8 (double) → 16...</li>
  <li><strong>Chain 2:</strong> 3 → 6 (double) → 12 (double)...</li>
  <li><strong>Chain 3:</strong> 5 → 10 (double)...</li>
  <li><strong>Chain 4:</strong> 7 → 14 (double)...</li>
</ul>
</div>

<h3>Using Doubling to Learn Faster</h3>
<div class="worked-example">
<h4>From 4 to 8</h4>
<p>If you know \\(4 \\times 7 = 28\\), then \\(8 \\times 7 = 56\\) (just double it!)</p>

<p>Why? Because 8 is just 4 doubled: \\(8 \\times 7 = (4 + 4) \\times 7 = (4 \\times 7) + (4 \\times 7) = 28 + 28 = 56\\)</p>
</div>

<h3>Visualizing the Doubling Chain</h3>
<div class="diagram-container">
  <canvas id="tables_doubling_chart" width="500" height="300"></canvas>
  <div class="diagram-caption">The doubling chain for multiplying by 3</div>
</div>

<script>
const ctxDoubling = document.getElementById('tables_doubling_chart');
if (ctxDoubling) {
  new Chart(ctxDoubling, {
    type: 'line',
    data: {
      labels: ['×1', '×2', '×3', '×4', '×5', '×6', '×7', '×8', '×9', '×10'],
      datasets: [
        {
          label: '1 times table',
          data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          borderColor: '#4169E1',
          backgroundColor: '#4169E155',
          borderWidth: 2,
          tension: 0.4
        },
        {
          label: '2 times (1 × 2)',
          data: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
          borderColor: '#22c55e',
          backgroundColor: '#22c55e55',
          borderWidth: 2,
          tension: 0.4
        },
        {
          label: '4 times (2 × 2)',
          data: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
          borderColor: '#f59e0b',
          backgroundColor: '#f59e0b55',
          borderWidth: 2,
          tension: 0.4
        },
        {
          label: '8 times (4 × 2)',
          data: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
          borderColor: '#ef4444',
          backgroundColor: '#ef444455',
          borderWidth: 2,
          tension: 0.4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 90 }
      }
    }
  });
}
</script>

<p>Look at how each line is exactly double the one before it!</p>
"""
    },
    {
        "title": "Breaking Apart Numbers: The Decomposition Strategy",
        "body": """
<h3>Breaking Multiplication into Easier Pieces</h3>
<p>If you're not sure about a fact, you can always break it apart into numbers you know better.</p>

<div class="worked-example">
<h4>Finding 8 × 6 Using 5 + 3</h4>
<p>\\(8 \\times 6 = 8 \\times (5 + 3) = (8 \\times 5) + (8 \\times 3) = 40 + 24 = 64\\)</p>

<p>Since you know 5s very well and 3s well, this becomes easy!</p>
</div>

<h3>Common Decompositions</h3>
<div class="diagram-container">
  <svg width="550" height="300" viewBox="0 0 550 300">
    <text x="275" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Breaking Apart Numbers: Common Strategies</text>

    <g id="decompositions">
      <!-- 6 = 5 + 1 -->
      <rect x="30" y="60" width="150" height="70" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="5"/>
      <text x="105" y="85" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>6 = 5 + 1</text>
      <text x="105" y="105" text-anchor='middle' font-size='11' fill='currentColor'>7 × 6 = 7×5 + 7×1</text>
      <text x="105" y="120" text-anchor='middle' font-size='11' fill='currentColor'>= 35 + 7 = 42</text>

      <!-- 7 = 5 + 2 -->
      <rect x="200" y="60" width="150" height="70" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="5"/>
      <text x="275" y="85" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>7 = 5 + 2</text>
      <text x="275" y="105" text-anchor='middle' font-size='11' fill='currentColor'>8 × 7 = 8×5 + 8×2</text>
      <text x="275" y="120" text-anchor='middle' font-size='11' fill='currentColor'>= 40 + 16 = 56</text>

      <!-- 8 = 10 - 2 -->
      <rect x="370" y="60" width="150" height="70" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2" rx="5"/>
      <text x="445" y="85" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>8 = 10 - 2</text>
      <text x="445" y="105" text-anchor='middle' font-size='11' fill='currentColor'>9 × 8 = 9×10 - 9×2</text>
      <text x="445" y="120" text-anchor='middle' font-size='11' fill='currentColor'>= 90 - 18 = 72</text>

      <!-- 12 = 10 + 2 -->
      <rect x="30" y="170" width="150" height="70" fill='#ef444480' stroke='#ef4444' stroke-width="2" rx="5"/>
      <text x="105" y="195" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>12 = 10 + 2</text>
      <text x="105" y="215" text-anchor='middle' font-size='11' fill='currentColor'>7 × 12 = 7×10 + 7×2</text>
      <text x="105" y="230" text-anchor='middle' font-size='11' fill='currentColor'>= 70 + 14 = 84</text>

      <!-- 9 = 10 - 1 -->
      <rect x="200" y="170" width="150" height="70" fill='#8b5cf680' stroke='#8b5cf6' stroke-width="2" rx="5"/>
      <text x="275" y="195" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>9 = 10 - 1</text>
      <text x="275" y="215" text-anchor='middle' font-size='11' fill='currentColor'>6 × 9 = 6×10 - 6×1</text>
      <text x="275" y="230" text-anchor='middle' font-size='11' fill='currentColor'>= 60 - 6 = 54</text>

      <!-- 11 = 10 + 1 -->
      <rect x="370" y="170" width="150" height="70" fill='#06b6d480' stroke='#06b6d4' stroke-width="2" rx="5"/>
      <text x="445" y="195" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>11 = 10 + 1</text>
      <text x="445" y="215" text-anchor='middle' font-size='11' fill='currentColor'>4 × 11 = 4×10 + 4×1</text>
      <text x="445" y="230" text-anchor='middle' font-size='11' fill='currentColor'>= 40 + 4 = 44</text>
    </g>
  </svg>
  <div class="diagram-caption">Common ways to break apart numbers</div>
</div>

<div class="concept-box">
<h4>Why This Works: The Distributive Property</h4>
<p>\\(a \\times (b + c) = (a \\times b) + (a \\times c)\\)</p>

<p>This is another property of multiplication that makes problem-solving flexible. When you don't know a fact, break it apart into facts you do know!</p>
</div>
"""
    }
]
