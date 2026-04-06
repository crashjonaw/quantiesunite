TITLE = "Pictograms and Bar Charts"
SECTIONS = [
    {
        "title": "What Are Pictograms?",
        "body": """<h3>Understanding Pictograms (Picture Graphs)</h3>
<p>A pictogram uses <strong>symbols or pictures to represent data</strong>. Each symbol or picture represents a certain amount.</p>

<div class="concept-box">
<p>Instead of writing numbers, we use pictures! This makes data easy to see at a glance.</p>
</div>

<h3>Simple Pictogram Example</h3>

<div class="worked-example">
<p><strong>Example: Books Read by Students</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Student</td>
    <td style="text-align: center; font-weight: bold;">Books Read (📚 = 1 book)</td>
    <td style="text-align: center; font-weight: bold;">Total</td>
  </tr>
  <tr>
    <td>Ali</td>
    <td>📚 📚 📚</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Bella</td>
    <td>📚 📚 📚 📚</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Chen</td>
    <td>📚 📚</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Diana</td>
    <td>📚 📚 📚 📚 📚</td>
    <td>5</td>
  </tr>
</table>

<p>It's easy to see that Diana read the most books!</p>
</div>

<h3>Reading the Legend</h3>
<p>The <strong>legend</strong> tells you what each symbol means.</p>

<div class="worked-example">
<p><strong>Example with different values:</strong></p>
<p><strong>Legend: 🎾 = 10 tennis balls</strong></p>
<p>Store A has: 🎾 🎾 = 20 balls<br>
Store B has: 🎾 🎾 🎾 = 30 balls</p>
<p>Store C has: 🎾 (half) = 5 balls</p>
<p>You need to read the legend to understand the value!</p>
</div>

<h3>How to Read a Pictogram</h3>
<ol>
  <li><strong>Read the legend</strong> to see what each symbol means</li>
  <li><strong>Count the symbols</strong> in each row</li>
  <li><strong>Multiply</strong> the number of symbols by the value each symbol represents</li>
</ol>

<div class="success-box">
<p><strong>Formula:</strong> \\(\\text{Total} = \\text{Number of symbols} \\times \\text{Value per symbol}\\)</p>
</div>

<div class="worked-example">
<p><strong>Question: How many tennis balls does Store B have?</strong><br>
Count the symbols: 3 symbols<br>
Value per symbol: 10 balls<br>
Total: \\(3 \\times 10 = 30\\) balls</p>
</div>
"""
    },
    {
        "title": "Creating Pictograms",
        "body": """<h3>Steps to Create a Pictogram</h3>

<ol>
  <li><strong>Collect and organize your data</strong> (like we learned in Concept 1)</li>
  <li><strong>Choose a symbol</strong> that represents your data (🍎 for apples, ⚽ for goals, etc.)</li>
  <li><strong>Decide what each symbol means</strong> (1 symbol = 1 apple, OR 1 symbol = 5 apples)</li>
  <li><strong>Draw the symbols</strong> in neat rows for each category</li>
  <li><strong>Write the legend</strong> clearly so others understand the symbol</li>
  <li><strong>Add a title</strong> so people know what the graph shows</li>
</ol>

<h3>Choosing Your Symbol</h3>

<div class="worked-example">
<p><strong>Example: Favourite Fruit Survey</strong></p>
<p><strong>Data collected:</strong> Apples: 8, Bananas: 12, Oranges: 5, Grapes: 7</p>
<p><strong>Symbol chosen:</strong> 🍎 (apple symbol)</p>
<p><strong>Legend:</strong> 🍎 = 1 piece of fruit</p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Fruit</td>
    <td style="text-align: center; font-weight: bold;">Pictogram (🍎 = 1)</td>
    <td style="text-align: center; font-weight: bold;">Total</td>
  </tr>
  <tr>
    <td>Apple</td>
    <td>🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Banana</td>
    <td>🍌 🍌 🍌 🍌 🍌 🍌 🍌 🍌 🍌 🍌 🍌 🍌</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Orange</td>
    <td>🍊 🍊 🍊 🍊 🍊</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Grape</td>
    <td>🍇 🍇 🍇 🍇 🍇 🍇 🍇</td>
    <td>7</td>
  </tr>
</table>

<p><strong>What can we see?</strong> Bananas are most popular (12)!</p>
</div>

<h3>When to Use Pictograms</h3>
<div class="concept-box">
<p>Pictograms are great for:</p>
<ul>
  <li>Young learners (pictures are easy to understand)</li>
  <li>Data with small whole numbers</li>
  <li>Making comparisons visually and quickly</li>
  <li>Making data fun and interesting!</li>
</ul>
</div>
"""
    },
    {
        "title": "What Are Bar Charts?",
        "body": """<h3>Understanding Bar Charts (Bar Graphs)</h3>
<p>A bar chart uses <strong>rectangular bars</strong> to show and compare amounts. The height or length of each bar represents the value.</p>

<h3>Parts of a Bar Chart</h3>

<svg viewBox="-15 -15 440 330" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:440px;">
  <!-- Background -->
  <rect x="-15" y="-15" width="440" height="330" rx="4" fill="#1e1e2e"/>

  <!-- Title -->
  <text x="215" y="22" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="currentColor">Favourite Sport</text>

  <!-- Y-axis -->
  <line x1="70" y1="45" x2="70" y2="250" stroke="#8b949e" stroke-width="2"/>
  <text x="20" y="152" font-family="sans-serif" font-size="12" text-anchor="middle" transform="rotate(-90,20,152)" fill="currentColor">Number of Students</text>

  <!-- X-axis -->
  <line x1="70" y1="250" x2="395" y2="250" stroke="#8b949e" stroke-width="2"/>
  <text x="232" y="295" font-family="sans-serif" font-size="12" text-anchor="middle" fill="currentColor">Sport</text>

  <!-- Y-axis labels and grid lines -->
  <text x="60" y="254" font-family="sans-serif" font-size="11" text-anchor="end" fill="currentColor">0</text>

  <line x1="70" y1="210" x2="395" y2="210" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="60" y="214" font-family="sans-serif" font-size="11" text-anchor="end" fill="currentColor">5</text>

  <line x1="70" y1="170" x2="395" y2="170" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="60" y="174" font-family="sans-serif" font-size="11" text-anchor="end" fill="currentColor">10</text>

  <line x1="70" y1="130" x2="395" y2="130" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="60" y="134" font-family="sans-serif" font-size="11" text-anchor="end" fill="currentColor">15</text>

  <line x1="70" y1="90" x2="395" y2="90" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="60" y="94" font-family="sans-serif" font-size="11" text-anchor="end" fill="currentColor">20</text>

  <!-- Bars: equal spacing. 5 bars, each 45px wide, 20px gap. Start at x=85 -->
  <!-- Football: 10 students. height = 10*8 = 80. y = 250-80 = 170 -->
  <rect x="85" y="170" width="45" height="80" rx="4" fill="#ef4444"/>
  <!-- Tennis: 15 students. height = 120. y = 250-120 = 130 -->
  <rect x="150" y="130" width="45" height="120" rx="4" fill="#f59e0b"/>
  <!-- Swimming: 8 students. height = 64. y = 250-64 = 186 -->
  <rect x="215" y="186" width="45" height="64" rx="4" fill="#f97316"/>
  <!-- Running: 12 students. height = 96. y = 250-96 = 154 -->
  <rect x="280" y="154" width="45" height="96" rx="4" fill="#a855f7"/>
  <!-- Badminton: 7 students. height = 56. y = 250-56 = 194 -->
  <rect x="345" y="194" width="45" height="56" rx="4" fill="#22c55e"/>

  <!-- X-axis labels (centered under each bar) -->
  <text x="107" y="270" font-family="sans-serif" font-size="11" text-anchor="middle" fill="currentColor">Football</text>
  <text x="172" y="270" font-family="sans-serif" font-size="11" text-anchor="middle" fill="currentColor">Tennis</text>
  <text x="237" y="270" font-family="sans-serif" font-size="11" text-anchor="middle" fill="currentColor">Swimming</text>
  <text x="302" y="270" font-family="sans-serif" font-size="11" text-anchor="middle" fill="currentColor">Running</text>
  <text x="367" y="270" font-family="sans-serif" font-size="11" text-anchor="middle" fill="currentColor">Badminton</text>

  <!-- Value labels on bars -->
  <text x="107" y="165" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="currentColor">10</text>
  <text x="172" y="125" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="currentColor">15</text>
  <text x="237" y="181" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="currentColor">8</text>
  <text x="302" y="149" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="currentColor">12</text>
  <text x="367" y="189" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="currentColor">7</text>
</svg>

<h3>Reading a Bar Chart</h3>

<div class="worked-example">
<p><strong>Steps to read a bar chart:</strong></p>
<ol>
  <li><strong>Read the title</strong> to understand what the chart shows</li>
  <li><strong>Check the scales</strong> on both axes (the lines with numbers)</li>
  <li><strong>Find the bar</strong> you're interested in</li>
  <li><strong>Read the value</strong> by seeing where the top of the bar aligns with the number scale</li>
</ol>

<p><strong>Example question: How many students chose tennis as their favourite sport?</strong></p>
<ol>
  <li>Find the "Tennis" bar</li>
  <li>Trace from the top of the bar to the left</li>
  <li>Read the number: 15 students</li>
</ol>
</div>

<h3>Comparing Data with Bar Charts</h3>

<div class="success-box">
<p>Bar charts make comparison easy! You can instantly see:</p>
<ul>
  <li><strong>Which is most:</strong> Look for the tallest bar</li>
  <li><strong>Which is least:</strong> Look for the shortest bar</li>
  <li><strong>Differences:</strong> Compare heights of two bars</li>
</ul>
</div>

<div class="worked-example">
<p><strong>From the sports chart above:</strong></p>
<ul>
  <li>Most popular sport? Tennis (15 students) ← tallest bar</li>
  <li>Least popular? Badminton (7 students) ← shortest bar</li>
  <li>How many more chose tennis than badminton? \\(15 - 7 = 8\\) more students</li>
</ul>
</div>
"""
    },
    {
        "title": "Vertical vs Horizontal Bar Charts",
        "body": """<h3>Two Styles of Bar Charts</h3>

<h4>Vertical Bar Charts (Most Common)</h4>
<p>Vertical bars stand up. Categories are on the horizontal axis (bottom), numbers are on the vertical axis (side).</p>

<div class="worked-example">
<p><strong>Vertical Bar Chart Example: Favourite Colour</strong></p>

<canvas id="data_colours1" data-chart='{"type":"bar","data":{"labels":["Red","Blue","Green","Yellow"],"datasets":[{"label":"Number of Students","data":[7,10,8,5],"backgroundColor":["#ef4444","#3b82f6","#22c55e","#eab308"]}]},"options":{"plugins":{"title":{"display":true,"text":"Favourite Colour Survey"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Students"}}}}}' height="300"></canvas>

<p><strong>Easy to read:</strong> Blue bar is tallest, so blue is the most popular colour.</p>
</div>

<h4>Horizontal Bar Charts</h4>
<p>Horizontal bars lie flat. Categories are on the vertical axis (side), numbers are on the horizontal axis (bottom).</p>

<div class="worked-example">
<p><strong>Horizontal Bar Chart Example: Same Data</strong></p>

<svg viewBox="-15 -15 440 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:440px;">
  <!-- Background -->
  <rect x="-15" y="-15" width="440" height="260" rx="4" fill="#1e1e2e"/>

  <!-- Title -->
  <text x="220" y="20" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="currentColor">Favourite Colour Survey (Horizontal)</text>

  <!-- Y-axis -->
  <line x1="80" y1="40" x2="80" y2="200" stroke="#8b949e" stroke-width="2"/>
  <!-- X-axis -->
  <line x1="80" y1="200" x2="380" y2="200" stroke="#8b949e" stroke-width="2"/>

  <!-- Labels on Y-axis (equal spacing: 40px apart, at 70, 110, 150, 190) -->
  <text x="70" y="74" font-family="sans-serif" font-size="12" text-anchor="end" fill="currentColor">Red</text>
  <text x="70" y="114" font-family="sans-serif" font-size="12" text-anchor="end" fill="currentColor">Blue</text>
  <text x="70" y="154" font-family="sans-serif" font-size="12" text-anchor="end" fill="currentColor">Green</text>
  <text x="70" y="194" font-family="sans-serif" font-size="12" text-anchor="end" fill="currentColor">Yellow</text>

  <!-- Numbers on X-axis: scale 0-15, each unit = 20px -->
  <text x="80" y="218" font-family="sans-serif" font-size="10" text-anchor="middle" fill="currentColor">0</text>
  <text x="180" y="218" font-family="sans-serif" font-size="10" text-anchor="middle" fill="currentColor">5</text>
  <text x="280" y="218" font-family="sans-serif" font-size="10" text-anchor="middle" fill="currentColor">10</text>
  <text x="380" y="218" font-family="sans-serif" font-size="10" text-anchor="middle" fill="currentColor">15</text>

  <!-- Grid lines -->
  <line x1="180" y1="40" x2="180" y2="200" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="280" y1="40" x2="280" y2="200" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="380" y1="40" x2="380" y2="200" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>

  <!-- Bars: equal spacing, 22px tall, centered in 40px rows -->
  <!-- Red: 7. width = 7*20 = 140 -->
  <rect x="80" y="59" width="140" height="22" rx="4" fill="#ef4444"/>
  <!-- Blue: 10. width = 10*20 = 200 -->
  <rect x="80" y="99" width="200" height="22" rx="4" fill="#3b82f6"/>
  <!-- Green: 8. width = 8*20 = 160 -->
  <rect x="80" y="139" width="160" height="22" rx="4" fill="#22c55e"/>
  <!-- Yellow: 5. width = 5*20 = 100 -->
  <rect x="80" y="179" width="100" height="22" rx="4" fill="#eab308"/>

  <!-- Values after bars -->
  <text x="228" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="currentColor">7</text>
  <text x="288" y="115" font-family="sans-serif" font-size="11" font-weight="bold" fill="currentColor">10</text>
  <text x="248" y="155" font-family="sans-serif" font-size="11" font-weight="bold" fill="currentColor">8</text>
  <text x="188" y="195" font-family="sans-serif" font-size="11" font-weight="bold" fill="currentColor">5</text>
</svg>

<p><strong>Same data, different view!</strong> Blue is still the tallest (most popular).</p>
</div>

<h3>When to Use Each Style</h3>

<div class="concept-box">
<ul>
  <li><strong>Vertical bars:</strong> Best for most situations. Easy to compare heights.</li>
  <li><strong>Horizontal bars:</strong> Good when category names are long (so they fit on the side).</li>
</ul>
</div>
"""
    },
    {
        "title": "Creating Bar Charts",
        "body": """<h3>Steps to Create a Bar Chart</h3>

<ol>
  <li><strong>Collect and organize your data</strong></li>
  <li><strong>Choose a scale</strong> (like 0, 5, 10, 15... or 0, 10, 20, 30...)</li>
  <li><strong>Draw the axes</strong> (horizontal and vertical lines)</li>
  <li><strong>Label the axes</strong> (what does each axis show?)</li>
  <li><strong>Draw the bars</strong> accurately (use a ruler!)</li>
  <li><strong>Add a title</strong></li>
</ol>

<h3>Choosing a Good Scale</h3>

<p>The scale is the sequence of numbers on a graph's axis. Choosing the right scale is important!</p>

<div class="worked-example">
<p><strong>Example: Ice Cream Sales Data</strong></p>
<p>Vanilla: 45, Chocolate: 52, Strawberry: 38</p>

<p><strong>Bad scale (too small):</strong> Going 0, 1, 2, 3... 60</p>
<p>The bars would be huge and hard to draw!</p>

<p><strong>Good scale:</strong> Going 0, 10, 20, 30, 40, 50, 60</p>
<p>The bars fit nicely on the page and are easy to read.</p>
</div>

<h3>Why Scale Matters</h3>

<p>The same data can look very different with different scales!</p>

<div class="worked-example">
<p><strong>Sales data:</strong> January: 100, February: 110, March: 120</p>

<p><strong>Scale 0-200:</strong> The differences look small (bars are similar height)</p>
<p><strong>Scale 95-125:</strong> The differences look HUGE (bars look very different)</p>

<p><strong>The data is the same, but the visual impression is different!</strong> Always check the scale!</p>
</div>

<h3>Real-World Bar Chart Example</h3>

<div class="worked-example">
<p><strong>Class Favourite Fruit Survey Results</strong></p>

<canvas id="data_fruit1" data-chart='{"type":"bar","data":{"labels":["Apples","Bananas","Oranges","Grapes"],"datasets":[{"label":"Favourite Fruit","data":[8,12,5,7],"backgroundColor":["#ef4444","#fbbf24","#f97316","#a855f7"]}]},"options":{"plugins":{"title":{"display":true,"text":"Class Favourite Fruit Survey"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Students"}}}}}' height="300"></canvas>

<p><strong>What we can see:</strong></p>
<ul>
  <li>Bananas are most popular (12 students)</li>
  <li>Oranges are least popular (5 students)</li>
  <li>Total students surveyed: \\(8 + 12 + 5 + 7 = 32\\)</li>
</ul>
</div>
"""
    }
]
