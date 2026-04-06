TITLE = "Times Tables 3 and 4: Building Blocks"

SECTIONS = [
    {
        "title": "Understanding Multiplication as Repeated Addition",
        "body": """
<h3>What is Multiplication?</h3>
<p>Multiplication is a <strong>shortcut for adding the same number over and over</strong>. You already know 2s, 5s, and 10s. Now we're building the rest! Every times table has patterns if you look carefully.</p>

<p>Let's say you have 4 baskets with 3 apples in each. Instead of counting \\(3 + 3 + 3 + 3\\), we write \\(3 \\times 4 = 12\\), which means "3 repeated 4 times".</p>

<div class="diagram-container">
  <svg width="100%" viewBox="0 0 530 150">
    <text x="265" y="25" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>4 Baskets with 3 Apples Each</text>

    <g>
      <rect x="20" y="50" width="60" height="70" rx="4" fill='none' stroke='#4169E1' stroke-width="2"/>
      <circle cx="35" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="55" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="45" cy="90" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
    </g>

    <g>
      <rect x="100" y="50" width="60" height="70" rx="4" fill='none' stroke='#22c55e' stroke-width="2"/>
      <circle cx="115" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="135" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="125" cy="90" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
    </g>

    <g>
      <rect x="180" y="50" width="60" height="70" rx="4" fill='none' stroke='#f59e0b' stroke-width="2"/>
      <circle cx="195" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="215" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="205" cy="90" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
    </g>

    <g>
      <rect x="260" y="50" width="60" height="70" rx="4" fill='none' stroke='#ef4444' stroke-width="2"/>
      <circle cx="275" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="295" cy="70" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
      <circle cx="285" cy="90" r="10" fill='#f59e0b80' stroke='#f59e0b' stroke-width="1"/>
    </g>

    <text x="400" y="90" font-size='20' font-weight='bold' fill='currentColor'>3 × 4 = 12</text>
  </svg>
  <div class="diagram-caption">Four groups of three equals twelve apples</div>
</div>

<div class="concept-box">
<h4>Key Concept: What Multiplication Means</h4>
<p>\\(3 \\times 4\\) can mean either "3 groups of 4" OR "4 groups of 3". Both give us 12. This is called the <strong>commutative property</strong> and it's a super useful shortcut!</p>
</div>
"""
    },
    {
        "title": "The 3 Times Table: Patterns and Tricks",
        "body": """
<h3>Learning the 3s</h3>
<p>The 3 times table might look random at first: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30. But there's a hidden pattern!</p>

<div class="worked-example">
<h4>The Digit Sum Pattern for 3s</h4>
<p>Here's the secret: <strong>if the digits in a number add up to 3, 6, or 9, that number is divisible by 3</strong>.</p>

<table style="margin: 20px auto; border-collapse: collapse; width: 100%; max-width: 500px;">
  <tr class="formula-box">
    <th style="border: 1px solid #333; padding: 10px;">Product</th>
    <th style="border: 1px solid #333; padding: 10px;">Digits</th>
    <th style="border: 1px solid #333; padding: 10px;">Sum</th>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">\\(3 \\times 4 = 12\\)</td>
    <td style="border: 1px solid #333; padding: 10px;">\\(1 + 2\\)</td>
    <td style="border: 1px solid #333; padding: 10px; "><strong>3</strong></td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">\\(3 \\times 8 = 24\\)</td>
    <td style="border: 1px solid #333; padding: 10px;">\\(2 + 4\\)</td>
    <td style="border: 1px solid #333; padding: 10px; "><strong>6</strong></td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">\\(3 \\times 9 = 27\\)</td>
    <td style="border: 1px solid #333; padding: 10px;">\\(2 + 7\\)</td>
    <td style="border: 1px solid #333; padding: 10px; "><strong>9</strong></td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">\\(3 \\times 6 = 18\\)</td>
    <td style="border: 1px solid #333; padding: 10px;">\\(1 + 8\\)</td>
    <td style="border: 1px solid #333; padding: 10px; "><strong>9</strong></td>
  </tr>
</table>

<p>You can use this to check your answers! If the digits don't add up to 3, 6, or 9, you know it's wrong.</p>
</div>

<h3>Visualizing the 3 Times Table</h3>
<div class="diagram-container">
  <canvas id="tables_3_chart" width="500" height="300"></canvas>
  <div class="diagram-caption">The 3 times table grows by 3 each time</div>
</div>

<script>
const ctx3 = document.getElementById('tables_3_chart');
if (ctx3) {
  new Chart(ctx3, {
    type: 'bar',
    data: {
      labels: ['3×1', '3×2', '3×3', '3×4', '3×5', '3×6', '3×7', '3×8', '3×9', '3×10'],
      datasets: [{
        label: '3 Times Table Results',
        data: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
        backgroundColor: '#4ade8055',
        borderColor: '#22c55e',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 35 }
      }
    }
  });
}
</script>
"""
    },
    {
        "title": "The 4 Times Table: Doubling Strategy",
        "body": """
<h3>Learning the 4s: The Smart Way</h3>
<p>Here's a fantastic shortcut for the 4 times table: <strong>4 is just 2 doubled</strong>!</p>

<div class="success-box">
<h4>The 4s Shortcut</h4>
<p>To find \\(4 \\times n\\), just find \\(2 \\times n\\) and double it.</p>
<ul>
  <li>\\(4 \\times 3\\): First \\(2 \\times 3 = 6\\), then double it: \\(6 + 6 = 12\\). So \\(4 \\times 3 = 12\\)</li>
  <li>\\(4 \\times 7\\): First \\(2 \\times 7 = 14\\), then double it: \\(14 + 14 = 28\\). So \\(4 \\times 7 = 28\\)</li>
</ul>
</div>

<h3>The Pattern in the 4s</h3>
<p>The 4 times table: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40</p>

<div class="concept-box">
<h4>Even Number Pattern</h4>
<p>All the answers in the 4 times table are <strong>even numbers</strong>—they all end in 2, 4, 6, 8, or 0. Every other number is divisible by 4:</p>
<p>4, 8, 12, 16, 20, 24, 28, 32, 36, 40 — notice how the last digit cycles: 4, 8, 2, 6, 0, 4, 8, 2, 6, 0</p>
</div>

<h3>Visualizing the 4 Times Table</h3>
<div class="diagram-container">
  <canvas id="tables_4_chart" width="500" height="300"></canvas>
  <div class="diagram-caption">The 4 times table: double the 2 times table</div>
</div>

<script>
const ctx4 = document.getElementById('tables_4_chart');
if (ctx4) {
  new Chart(ctx4, {
    type: 'line',
    data: {
      labels: ['4×1', '4×2', '4×3', '4×4', '4×5', '4×6', '4×7', '4×8', '4×9', '4×10'],
      datasets: [{
        label: '4 Times Table Results',
        data: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
        borderColor: '#f59e0b',
        backgroundColor: '#fef3c755',
        borderWidth: 3,
        fill: true,
        tension: 0.4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 45 }
      }
    }
  });
}
</script>

<h3>Comparing 2s, 4s, and 8s</h3>
<p>Now you can see why the strategy works:</p>
<ul>
  <li><strong>2 Times:</strong> 2, 4, 6, 8, 10, 12, 14, 16, 18, 20</li>
  <li><strong>4 Times (\\(2 \\times 2\\)):</strong> 4, 8, 12, 16, 20, 24, 28, 32, 36, 40</li>
  <li><strong>8 Times (\\(4 \\times 2\\)):</strong> 8, 16, 24, 32, 40, 48, 56, 64, 72, 80</li>
</ul>

<p>Each table is exactly double the one before it! This is why learning one table helps you with the others.</p>
"""
    },
    {
        "title": "Arrays: Seeing Multiplication as Pictures",
        "body": """
<h3>What is an Array?</h3>
<p>An <strong>array</strong> is objects arranged in rows and columns. Arrays help us see multiplication as a picture, which makes it much easier to understand.</p>

<h3>Example: The \\(3 \\times 4\\) Array</h3>
<div class="diagram-container">
  <svg width="100%" viewBox="0 0 460 225">
    <text x="230" y="25" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>3 Rows and 4 Columns</text>

    <g>
      <rect x="50" y="55" width="35" height="35" rx="4" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>
      <rect x="95" y="55" width="35" height="35" rx="4" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>
      <rect x="140" y="55" width="35" height="35" rx="4" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>
      <rect x="185" y="55" width="35" height="35" rx="4" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>

      <rect x="50" y="100" width="35" height="35" rx="4" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
      <rect x="95" y="100" width="35" height="35" rx="4" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
      <rect x="140" y="100" width="35" height="35" rx="4" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
      <rect x="185" y="100" width="35" height="35" rx="4" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>

      <rect x="50" y="145" width="35" height="35" rx="4" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
      <rect x="95" y="145" width="35" height="35" rx="4" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
      <rect x="140" y="145" width="35" height="35" rx="4" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
      <rect x="185" y="145" width="35" height="35" rx="4" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
    </g>

    <text x="280" y="115" font-size='18' font-weight='bold' fill='currentColor'>3 × 4 = 12</text>
    <text x="280" y="140" font-size='14' fill='currentColor'>(3 rows of 4)</text>
  </svg>
  <div class="diagram-caption">An array shows multiplication clearly</div>
</div>

<h3>Why Arrays Are Powerful</h3>
<p>Arrays show us three important ideas:</p>

<div class="concept-box">
<h4>Commutative Property</h4>
<p>If you rotate this array 90 degrees, you get 4 rows and 3 columns. Both equal 12! This shows us \\(3 \\times 4 = 4 \\times 3\\).</p>
</div>

<p><strong>Counting:</strong> We can count all the squares to find the product.</p>
<p><strong>Patterns:</strong> Arrays help us understand how times tables relate to each other.</p>
"""
    }
]
