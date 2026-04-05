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

<svg width="400" height="300" viewBox="0 0 400 300">
  <!-- Title -->
  <text x="200" y="25" font-size='18' font-weight='bold' text-anchor='middle'>Parts of a Bar Chart</text>

  <!-- Y-axis (vertical) -->
  <line x1="50" y1="50" x2="50" y2="250" stroke='#8b949e' stroke-width="2"/>
  <text x="15" y="155" font-size='12' text-anchor='middle' transform='rotate(-90, 15, 155)'>Number of Students</text>

  <!-- X-axis (horizontal) -->
  <line x1="50" y1="250" x2="380" y2="250" stroke='#8b949e' stroke-width="2"/>
  <text x="215" y="280" font-size='12' text-anchor='middle'>Favourite Sport</text>

  <!-- Y-axis labels -->
  <text x="40" y="255" font-size='10' text-anchor='end'>0</text>
  <text x="40" y="205" font-size='10' text-anchor='end'>5</text>
  <text x="40" y="155" font-size='10' text-anchor='end'>10</text>
  <text x="40" y="105" font-size='10' text-anchor='end'>15</text>

  <!-- Grid lines -->
  <line x1="50" y1="200" x2="380" y2="200" stroke='#30363d' stroke-width="1" stroke-dasharray="5,5"/>
  <line x1="50" y1="150" x2="380" y2="150" stroke='#30363d' stroke-width="1" stroke-dasharray="5,5"/>
  <line x1="50" y1="100" x2="380" y2="100" stroke='#30363d' stroke-width="1" stroke-dasharray="5,5"/>

  <!-- Bars -->
  <rect x="70" y="150" width="40" height="100" fill='#ef4444'/>
  <rect x="130" y="100" width="40" height="150" fill='#f59e0b'/>
  <rect x="190" y="170" width="40" height="80" fill='#f97316'/>
  <rect x="250" y="130" width="40" height="120" fill='#a855f7'/>
  <rect x="310" y="180" width="40" height="70" fill='#22c55e'/>

  <!-- X-axis labels -->
  <text x="90" y="270" font-size='11' text-anchor='middle'>Football</text>
  <text x="150" y="270" font-size='11' text-anchor='middle'>Tennis</text>
  <text x="210" y="270" font-size='11' text-anchor='middle'>Swimming</text>
  <text x="270" y="270" font-size='11' text-anchor='middle'>Running</text>
  <text x="330" y="270" font-size='11' text-anchor='middle'>Badminton</text>

  <!-- Legend for parts -->
  <circle cx="60" cy="30" r="4" fill='#ef4444'/>
  <text x="70" y="35" font-size='11'>Bars show amounts</text>
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

<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 420px;">
  <!-- Title -->
  <text x="210" y="20" font-size='14' font-weight='bold' text-anchor='middle' fill='currentColor'>Favourite Colour Survey (Horizontal)</text>

  <!-- Y-axis -->
  <line x1="80" y1="40" x2="80" y2="200" stroke='#8b949e' stroke-width="2"/>
  <!-- X-axis -->
  <line x1="80" y1="200" x2="380" y2="200" stroke='#8b949e' stroke-width="2"/>

  <!-- Labels on Y-axis -->
  <text x="70" y="75" font-size='12' text-anchor='end' fill='currentColor'>Red</text>
  <text x="70" y="110" font-size='12' text-anchor='end' fill='currentColor'>Blue</text>
  <text x="70" y="145" font-size='12' text-anchor='end' fill='currentColor'>Green</text>
  <text x="70" y="180" font-size='12' text-anchor='end' fill='currentColor'>Yellow</text>

  <!-- Numbers on X-axis -->
  <text x="80" y="215" font-size='10' fill='currentColor'>0</text>
  <text x="150" y="215" font-size='10' fill='currentColor'>5</text>
  <text x="220" y="215" font-size='10' fill='currentColor'>10</text>
  <text x="290" y="215" font-size='10' fill='currentColor'>15</text>

  <!-- Bars -->
  <rect x="80" y="65" width="140" height="18" fill='#ef4444' rx="2"/>
  <rect x="80" y="100" width="200" height="18" fill='#3b82f6' rx="2"/>
  <rect x="80" y="135" width="160" height="18" fill='#22c55e' rx="2"/>
  <rect x="80" y="170" width="100" height="18" fill='#eab308' rx="2"/>

  <!-- Values after bars -->
  <text x="225" y="79" font-size='11' font-weight='bold' fill='currentColor'>7</text>
  <text x="285" y="114" font-size='11' font-weight='bold' fill='currentColor'>10</text>
  <text x="245" y="149" font-size='11' font-weight='bold' fill='currentColor'>8</text>
  <text x="185" y="184" font-size='11' font-weight='bold' fill='currentColor'>5</text>
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
