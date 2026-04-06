TITLE = "Times Tables 9, 11, and 12: The Special Three"

SECTIONS = [
    {
        "title": "The 9 Times Table: The Magical Pattern",
        "body": """
<h3>Learning the 9s: The Digit Sum Trick</h3>
<p>The 9 times table has a hidden pattern: <strong>the digits in every answer always add up to 9</strong>. This is one of the most magical patterns in all of multiplication!</p>

<div class="worked-example">
<h4>The 9-Pattern Magic</h4>
<table style="margin: 20px auto; border-collapse: collapse; width: 100%; max-width: 500px; color: currentColor;">
  <tr>
    <th style="border: 1px solid #8b949e; padding: 10px; background: transparent; color: currentColor;">Multiplication</th>
    <th style="border: 1px solid #8b949e; padding: 10px; background: transparent; color: currentColor;">Product</th>
    <th style="border: 1px solid #8b949e; padding: 10px; background: transparent; color: currentColor;">Digits</th>
    <th style="border: 1px solid #8b949e; padding: 10px; background: transparent; color: currentColor;">Sum = 9</th>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 1\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 2\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">18</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(1 + 8\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 3\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">27</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(2 + 7\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 4\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">36</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(3 + 6\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 5\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">45</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(4 + 5\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(9 \\times 6\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">54</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">\\(5 + 4\\)</td>
    <td style="border: 1px solid #8b949e; padding: 10px;">9</td>
  </tr>
</table>

<p>Every single answer's digits add up to 9! You can use this to check if your answer is right.</p>
</div>

<h3>The Finger Trick for 9s</h3>
<p>Here's a fun way to remember the 9 times table using your fingers:</p>

<div class="success-box">
<h4>The 9-Finger Trick</h4>
<p>To find \\(9 \\times 3\\) using your fingers:</p>
<ol>
  <li>Hold up all 10 fingers</li>
  <li>Put down the 3rd finger from the left</li>
  <li>Count the fingers to the left (2) — that's the first digit</li>
  <li>Count the fingers to the right (7) — that's the second digit</li>
  <li>Answer: 27! (And \\(2 + 7 = 9\\) ✓)</li>
</ol>

<p>Try it for \\(9 \\times 7\\): Put down the 7th finger, you get 6 fingers left and 3 fingers right = 63 (and \\(6 + 3 = 9\\) ✓)</p>
</div>

<h3>Visualizing the 9 Times Table</h3>
<div class="diagram-container">
  <canvas id="tables_9_chart" width="500" height="300"></canvas>
  <div class="diagram-caption">The 9 times table grows by 9 each time</div>
</div>

<script>
const ctx9 = document.getElementById('tables_9_chart');
if (ctx9) {
  new Chart(ctx9, {
    type: 'line',
    data: {
      labels: ['9×1', '9×2', '9×3', '9×4', '9×5', '9×6', '9×7', '9×8', '9×9', '9×10'],
      datasets: [{
        label: '9 Times Table Results',
        data: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],
        borderColor: '#ef4444',
        backgroundColor: '#fee2e255',
        borderWidth: 3,
        fill: true,
        tension: 0.4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 100 }
      }
    }
  });
}
</script>
"""
    },
    {
        "title": "The 11 Times Table: The Double-Digit Shortcut",
        "body": """
<h3>Learning the 11s: The Easiest Shortcut!</h3>
<p>The 11 times table is beautiful because for single-digit numbers, the answer is that digit doubled:</p>

<div class="concept-box">
<h4>The 11 Times Table Shortcut for Single Digits</h4>
<p>\\(11 \\times 3 = 33\\) (the digit 3 appears twice!)</p>
<p>\\(11 \\times 7 = 77\\) (the digit 7 appears twice!)</p>
<p>\\(11 \\times 9 = 99\\) (the digit 9 appears twice!)</p>

<p>For any single digit \\(d\\), \\(11 \\times d = dd\\) (the digit repeated)</p>
</div>

<h3>The Full 11 Times Table</h3>
<p>11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132</p>

<div class="worked-example">
<h4>For Two-Digit Answers</h4>
<p>When you get to \\(11 \\times 10\\), things change slightly:</p>
<ul>
  <li>\\(11 \\times 10 = 110\\)</li>
  <li>\\(11 \\times 11 = 121\\)</li>
  <li>\\(11 \\times 12 = 132\\)</li>
</ul>

<p>You can still see a pattern: the middle digit is the tens place, the ones and hundreds are based on what you're multiplying by.</p>
</div>

<h3>Pattern Visualization</h3>
<div class="diagram-container">
  <svg width="500" height="250" viewBox="0 0 500 250">
    <text x="250" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>The 11 Times Table Pattern</text>

    <g id="pattern">
      <text x="50" y="70" font-size='12' font-weight='bold' fill='currentColor'>11 × 1 = 11</text>
      <rect x="50" y="75" width="30" height="30" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>
      <rect x="85" y="75" width="30" height="30" fill='#4169E180' stroke='#4169E1' stroke-width="2"/>

      <text x="50" y="135" font-size='12' font-weight='bold' fill='currentColor'>11 × 5 = 55</text>
      <g id="five-boxes">
        <rect x="50" y="140" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
        <rect x="80" y="140" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
        <rect x="110" y="140" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
        <rect x="140" y="140" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
        <rect x="170" y="140" width="25" height="25" fill='#22c55e80' stroke='#22c55e' stroke-width="2"/>
        <rect x="50" y="170" width="25" height="25" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
        <rect x="80" y="170" width="25" height="25" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
        <rect x="110" y="170" width="25" height="25" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
        <rect x="140" y="170" width="25" height="25" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
        <rect x="170" y="170" width="25" height="25" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2"/>
      </g>

      <text x="280" y="100" font-size='13' font-weight='bold' fill='currentColor'>All answers have</text>
      <text x="280" y="120" font-size='13' font-weight='bold' fill='currentColor'>the same digit</text>
      <text x="280" y="140" font-size='13' font-weight='bold' fill='currentColor'>repeated!</text>

      <text x="280" y="190" font-size='12' fill='currentColor'>11 × 2 = 22</text>
      <text x="280" y="210" font-size='12' fill='currentColor'>11 × 8 = 88</text>
      <text x="280" y="230" font-size='12' fill='currentColor'>11 × 3 = 33</text>
    </g>
  </svg>
  <div class="diagram-caption">Single digits repeat in the 11 times table</div>
</div>

<div class="success-box">
<h4>Remember: 11 Is Special!</h4>
<p>The 11 times table for single digits (1-9) is the easiest: just double the digit. This shortcut alone will make these facts stick in your memory!</p>
</div>
"""
    },
    {
        "title": "The 12 Times Table: Connecting to 10s",
        "body": """
<h3>Learning the 12s: Using What You Know</h3>
<p>The 12 times table: 12, 24, 36, 48, 60, 72, 84, 96, 108, 120</p>

<p>You can break 12 into 10 + 2, which are numbers you know very well!</p>

<div class="worked-example">
<h4>Finding 12 × 7 Using 10 + 2</h4>
<p>\\(12 \\times 7 = (10 + 2) \\times 7 = (10 \\times 7) + (2 \\times 7) = 70 + 14 = 84\\)</p>

<p>Since you know the 10 times table (just add a zero!) and the 2 times table, you can build the 12 times table!</p>
</div>

<h3>Breaking Down the 12 Times Table</h3>
<div class="diagram-container">
  <svg width="550" height="200" viewBox="0 0 550 200">
    <text x="275" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>12 = 10 + 2: Build 12s from Facts You Know</text>

    <g id="breakdown">
      <!-- 10 times part -->
      <rect x="30" y="60" width="120" height="80" fill='#4169E180' stroke='#4169E1' stroke-width="2" rx="5"/>
      <text x="90" y="90" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>10 Times</text>
      <text x="90" y="110" text-anchor='middle' font-size='12' fill='currentColor'>10 × 7 = 70</text>
      <text x="90" y="130" text-anchor='middle' font-size='12' fill='currentColor'>(add a zero!)</text>

      <text x="160" y="105" font-size='20' font-weight='bold' fill='currentColor'>+</text>

      <!-- 2 times part -->
      <rect x="190" y="60" width="120" height="80" fill='#22c55e80' stroke='#22c55e' stroke-width="2" rx="5"/>
      <text x="250" y="90" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>2 Times</text>
      <text x="250" y="110" text-anchor='middle' font-size='12' fill='currentColor'>2 × 7 = 14</text>
      <text x="250" y="130" text-anchor='middle' font-size='12' fill='currentColor'>(easy!)</text>

      <text x="330" y="105" font-size='20' font-weight='bold' fill='currentColor'>=</text>

      <!-- Answer -->
      <rect x="360" y="60" width="140" height="80" fill='#f59e0b80' stroke='#f59e0b' stroke-width="2" rx="5"/>
      <text x="430" y="90" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>12 Times</text>
      <text x="430" y="110" text-anchor='middle' font-size='12' fill='currentColor'>12 × 7 = 84</text>
      <text x="430" y="130" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>70 + 14</text>
    </g>
  </svg>
  <div class="diagram-caption">Use 10 + 2 to build the 12 times table</div>
</div>

<h3>All 12s Are Even</h3>
<p>Since 12 is even (and 2 is even, and 10 is even), every answer is even: 12, 24, 36, 48, 60, 72, 84, 96, 108, 120</p>

<div class="concept-box">
<h4>The Dozen Connection</h4>
<p>Did you know that 12 items make a "dozen"? (Like a dozen eggs = 12 eggs.) So the 12 times table answers show how many items you have when counting by dozens!</p>
</div>
"""
    },
    {
        "title": "Putting It All Together: The Big Picture",
        "body": """
<h3>The Complete Times Table Family</h3>
<p>Now you've learned about 9, 11, and 12. Together with 3 and 4, 6, 7, and 8, you've learned strategies for every times table from 1 to 12!</p>

<div class="diagram-container">
  <svg width="600" height="300" viewBox="0 0 600 300">
    <text x="300" y="25" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>All Times Tables 1-12: Quick Reference</text>

    <g id="tables-overview">
      <!-- Row 1 -->
      <text x="30" y="60" font-size='11' font-weight='bold' fill='currentColor'>1: Identity</text>
      <text x="30" y="75" font-size='10' fill='currentColor'>1, 2, 3, 4, 5...</text>

      <text x="120" y="60" font-size='11' font-weight='bold' fill='currentColor'>2: Doubling</text>
      <text x="120" y="75" font-size='10' fill='currentColor'>2, 4, 6, 8, 10...</text>

      <text x="210" y="60" font-size='11' font-weight='bold' fill='currentColor'>3: Digit Sum</text>
      <text x="210" y="75" font-size='10' fill='currentColor'>3, 6, 9, 12, 15...</text>

      <text x="300" y="60" font-size='11' font-weight='bold' fill='currentColor'>4: Double 2s</text>
      <text x="300" y="75" font-size='10' fill='currentColor'>4, 8, 12, 16, 20...</text>

      <text x="390" y="60" font-size='11' font-weight='bold' fill='currentColor'>5: 0 or 5</text>
      <text x="390" y="75" font-size='10' fill='currentColor'>5, 10, 15, 20, 25...</text>

      <text x="480" y="60" font-size='11' font-weight='bold' fill='currentColor'>10: Add Zero</text>
      <text x="480" y="75" font-size='10' fill='currentColor'>10, 20, 30, 40, 50...</text>

      <!-- Row 2 -->
      <text x="30" y="130" font-size='11' font-weight='bold' fill='currentColor'>6: Double 3s</text>
      <text x="30" y="145" font-size='10' fill='currentColor'>6, 12, 18, 24, 30...</text>

      <text x="120" y="130" font-size='11' font-weight='bold' fill='currentColor'>7: Build Up</text>
      <text x="120" y="145" font-size='10' fill='currentColor'>7, 14, 21, 28, 35...</text>

      <text x="210" y="130" font-size='11' font-weight='bold' fill='currentColor'>8: Double 4s</text>
      <text x="210" y="145" font-size='10' fill='currentColor'>8, 16, 24, 32, 40...</text>

      <text x="300" y="130" font-size='11' font-weight='bold' fill='currentColor'>9: Digits = 9</text>
      <text x="300" y="145" font-size='10' fill='currentColor'>9, 18, 27, 36, 45...</text>

      <text x="390" y="130" font-size='11' font-weight='bold' fill='currentColor'>11: Repeat</text>
      <text x="390" y="145" font-size='10' fill='currentColor'>11, 22, 33, 44, 55...</text>

      <text x="480" y="130" font-size='11' font-weight='bold' fill='currentColor'>12: 10 + 2</text>
      <text x="480" y="145" font-size='10' fill='currentColor'>12, 24, 36, 48, 60...</text>

      <!-- Strategies box -->
      <rect x="30" y="190" width="540" height="100" fill='none' stroke='#8b949e' stroke-width="2" rx="5"/>
      <text x="40" y="210" font-size='12' font-weight='bold' fill='currentColor'>Key Strategies to Remember:</text>

      <text x="50" y="235" font-size='11' fill='currentColor'>• Use doubling: 2 → 4 → 8, and 3 → 6 (6 is 3 doubled)</text>
      <text x="50" y="255" font-size='11' fill='currentColor'>• Use breaking apart: 12 = 10 + 2, 7 = 5 + 2</text>
      <text x="50" y="275" font-size='11' fill='currentColor'>• Use digit patterns: 9s sum to 9, 11s repeat single digits</text>
    </g>
  </svg>
  <div class="diagram-caption">All twelve times tables with their special shortcuts</div>
</div>

<div class="success-box">
<h4>You've Done It!</h4>
<p>You now know every times table from 1 to 12! By understanding the patterns and connections, you have tools to figure out any fact you forget. Keep practicing, and soon these facts will be automatic!</p>
</div>
"""
    }
]
