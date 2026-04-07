TITLE = "Bar Model Method - Visualizing Problems (Singapore Math)"

SECTIONS = [
    {
        "title": "What is the Bar Model?",
        "body": """
<div class="concept-box">
<h3>The Bar Model Explained</h3>

<p>A <strong>bar model</strong> (also called a tape diagram or strip diagram) is a visual way to represent a problem using rectangles.</p>

<p>Instead of just writing numbers, you DRAW the relationships between quantities. This helps you:</p>

<ul>
<li>See what you know (given information)</li>
<li>See what you're looking for (unknown)</li>
<li>Understand the relationships (one is bigger, combined amounts, etc.)</li>
<li>Plan your calculation</li>
</ul>

<h3>Why Use Bar Models?</h3>

<p>Bar models turn confusing word problems into visual pictures. You can SEE the math, not just read it.</p>
</div>

<div class="worked-example">
<h4>Simple Example: Part-Whole</h4>

<p><strong>Problem:</strong> "Ben has 5 apples. Amy has 8 apples. How many do they have together?"</p>

<p><strong>Bar Model:</strong></p>

<svg width="100%" height="140" viewBox="0 0 420 140" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="47" font-size='13' fill='currentColor' font-family='sans-serif'>Ben:</text>
  <rect x="60" y="25" width="110" height="40" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="115" y="50" font-size='14' fill='currentColor' text-anchor='middle' font-family='sans-serif'>5</text>

  <text x="15" y="97" font-size='13' fill='currentColor' font-family='sans-serif'>Amy:</text>
  <rect x="60" y="75" width="176" height="40" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="148" y="100" font-size='14' fill='currentColor' text-anchor='middle' font-family='sans-serif'>8</text>

  <line x1="236" y1="25" x2="236" y2="115" stroke='#30363d' stroke-width="1" stroke-dasharray="3,3"/>
  <text x="250" y="72" font-size='12' fill='#79c0ff' font-family='sans-serif'>Total: 5 + 8 = 13</text>
</svg>

<p>The bars show: Ben has 5, Amy has 8, and together they have 5 + 8 = 13.</p>
</div>

<h3>When to Use Bar Models</h3>

<ul>
<li>When comparing quantities (one is larger)</li>
<li>When combining amounts (finding totals)</li>
<li>When showing relationships (one is 3 times another)</li>
<li>When showing before and after states</li>
<li>For any problem with multiple quantities</li>
</ul>
"""
    },
    {
        "title": "Type 1: Comparison Models",
        "body": """
<div class="concept-box">
<h3>Comparing Two Quantities</h3>

<p>Use a comparison bar model when one quantity is bigger or smaller than another.</p>
</div>

<div class="worked-example">
<h4>Example 1: Simple Multiplication Comparison</h4>

<p><strong>Problem:</strong> "Ali has 3 times as many stickers as Ben. Ben has 6 stickers. How many does Ali have?"</p>

<p><strong>Bar Model:</strong></p>

<svg width="100%" height="150" viewBox="0 0 460 150" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="47" font-size='13' fill='currentColor' font-family='sans-serif'>Ben:</text>
  <rect x="60" y="25" width="70" height="35" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="95" y="48" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>6</text>

  <text x="15" y="97" font-size='13' fill='currentColor' font-family='sans-serif'>Ali:</text>
  <rect x="60" y="75" width="70" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <rect x="140" y="75" width="70" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <rect x="220" y="75" width="70" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="95" y="98" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>6</text>
  <text x="175" y="98" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>6</text>
  <text x="255" y="98" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>6</text>

  <line x1="300" y1="85" x2="315" y2="92" stroke='#30363d' stroke-width="1"/>
  <text x="320" y="97" font-size='12' fill='#79c0ff' font-family='sans-serif'>3 units = 3 x 6 = 18</text>
</svg>

<p><strong>Calculation:</strong> Ali has \(3 \times 6 = 18\) stickers</p>
</div>

<div class="worked-example">
<h4>Example 2: Comparison with Unknown Quantities</h4>

<p><strong>Problem:</strong> "Amy has 4 times as much money as Ben. Together they have 100 dollars. How much does each have?"</p>

<p><strong>Bar Model:</strong></p>

<svg width="100%" height="155" viewBox="0 0 460 155" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="47" font-size='13' fill='currentColor' font-family='sans-serif'>Ben:</text>
  <rect x="60" y="25" width="55" height="35" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="87" y="48" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>?</text>

  <text x="15" y="102" font-size='13' fill='currentColor' font-family='sans-serif'>Amy:</text>
  <rect x="60" y="80" width="55" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <rect x="125" y="80" width="55" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <rect x="190" y="80" width="55" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <rect x="255" y="80" width="55" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="87" y="103" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>?</text>
  <text x="152" y="103" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>?</text>
  <text x="217" y="103" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>?</text>
  <text x="282" y="103" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>?</text>

  <line x1="320" y1="90" x2="335" y2="95" stroke='#30363d' stroke-width="1"/>
  <text x="340" y="95" font-size='12' fill='#79c0ff' font-family='sans-serif'>5 units = 100</text>
  <text x="340" y="115" font-size='12' fill='#79c0ff' font-family='sans-serif'>1 unit = 20</text>
</svg>

<p><strong>Calculation:</strong></p>
<ul>
<li>5 units total = 100 dollars</li>
<li>1 unit = \(100 \div 5 = 20\) dollars</li>
<li>Ben has 20 dollars</li>
<li>Amy has \(4 \times 20 = 80\) dollars</li>
</ul>
</div>

<div class="success-box">
<h3>Key for Comparison Models</h3>

<ul>
<li>Make one bar for each person/object</li>
<li>If one has more, make that bar longer</li>
<li>Divide bars into equal units</li>
<li>Label what you know and what you don't know</li>
<li>Calculate the value of ONE unit first</li>
</ul>
</div>
"""
    },
    {
        "title": "Type 2: Before-After Models",
        "body": """
<div class="concept-box">
<h3>Tracking Change Over Time</h3>

<p>Use a before-after model when something CHANGES: items are transferred, bought, sold, or amounts increase/decrease.</p>
</div>

<div class="worked-example">
<h4>Example: Transfer Between Groups</h4>

<p><strong>Problem:</strong> "Container A has 60 mL of water. Container B has 40 mL. If 15 mL is poured from A to B, how much does each have?"</p>

<p><strong>Bar Model - BEFORE:</strong></p>

<svg width="100%" height="130" viewBox="0 0 320 130" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="42" font-size='13' fill='currentColor' font-family='sans-serif'>A:</text>
  <rect x="40" y="20" width="180" height="35" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="130" y="43" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>60 mL</text>

  <text x="15" y="92" font-size='13' fill='currentColor' font-family='sans-serif'>B:</text>
  <rect x="40" y="70" width="120" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="100" y="93" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>40 mL</text>
</svg>

<p><strong>Bar Model - AFTER:</strong></p>

<svg width="100%" height="130" viewBox="0 0 320 130" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="42" font-size='13' fill='currentColor' font-family='sans-serif'>A:</text>
  <rect x="40" y="20" width="135" height="35" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="107" y="43" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>45 mL</text>

  <text x="15" y="92" font-size='13' fill='currentColor' font-family='sans-serif'>B:</text>
  <rect x="40" y="70" width="165" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="122" y="93" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>55 mL</text>
</svg>

<p><strong>Solution:</strong></p>
<ul>
<li>A loses 15: \(60 - 15 = 45\) mL</li>
<li>B gains 15: \(40 + 15 = 55\) mL</li>
<li>Total unchanged: \(45 + 55 = 100\) ✓</li>
</ul>
</div>

<div class="worked-example">
<h4>Example: Finding Initial Amounts</h4>

<p><strong>Problem:</strong> "Tom and Jerry have some money. After Tom gives 12 dollars to Jerry, they both have the same amount. Tom started with 40 dollars. How much did Jerry have initially?"</p>

<p><strong>Bar Model - AFTER (Equal):</strong></p>

<svg width="100%" height="135" viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <text x="15" y="42" font-size='12' fill='currentColor' font-family='sans-serif'>Tom after:</text>
  <rect x="100" y="20" width="120" height="35" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="160" y="43" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>28</text>

  <text x="15" y="92" font-size='12' fill='currentColor' font-family='sans-serif'>Jerry after:</text>
  <rect x="100" y="70" width="120" height="35" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="160" y="93" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>28</text>
</svg>

<p><strong>Calculation:</strong></p>
<ul>
<li>After giving 12, Tom has: \(40 - 12 = 28\) dollars</li>
<li>Jerry also has 28 dollars after receiving 12</li>
<li>Jerry initially had: \(28 - 12 = 16\) dollars</li>
<li>Check: Tom 40 → gives 12 → 28. Jerry 16 → gets 12 → 28 ✓</li>
</ul>
</div>
"""
    },
    {
        "title": "Type 3: Multi-Step Problems with Models",
        "body": """
<div class="concept-box">
<h3>Complex Problems Need Multiple Parts</h3>

<p>Some problems involve several steps. Draw separate bar models for each part, or use a model that shows all relationships at once.</p>
</div>

<div class="worked-example">
<h4>Example: Three-Part Problem</h4>

<p><strong>Problem:</strong> "Red ribbons cost 3 dollars each. Blue ribbons cost 5 dollars each. Sara buys 10 items total for 38 dollars. How many of each color?"</p>

<p><strong>Strategy: Assumption Method with Model</strong></p>

<p><strong>Step 1: Assume all are the cheaper item (red)</strong></p>

<svg width="100%" height="75" viewBox="0 0 320 75" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <rect x="15" y="15" width="240" height="40" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="135" y="41" font-size='13' fill='currentColor' text-anchor='middle' font-family='sans-serif'>10 x $3 = $30</text>
</svg>

<p><strong>Step 2: Find the difference</strong></p>
<ul>
<li>Actual cost: 38 dollars</li>
<li>Assumed cost: 30 dollars</li>
<li>Extra money spent: \(38 - 30 = 8\) dollars</li>
</ul>

<p><strong>Step 3: Calculate how many blue ribbons</strong></p>
<ul>
<li>Each blue ribbon costs 2 more than red (\(5 - 3 = 2\))</li>
<li>Number of blue: \(8 \div 2 = 4\) ribbons</li>
<li>Number of red: \(10 - 4 = 6\) ribbons</li>
</ul>

<p><strong>Check:</strong></p>
<ul>
<li>6 red + 4 blue = 10 items ✓</li>
<li>\((6 \times 3) + (4 \times 5) = 18 + 20 = 38\) dollars ✓</li>
</ul>
</div>

<div class="success-box">
<h3>Steps for Multi-Step Bar Models</h3>

<ol>
<li>Identify all quantities and relationships</li>
<li>Draw separate models for each condition if needed</li>
<li>Label known values and unknowns clearly</li>
<li>Work from simpler parts to more complex</li>
<li>Calculate the value of one unit</li>
<li>Use that to find all other quantities</li>
<li>Always check against ALL conditions</li>
</ol>
</div>
"""
    }
]
