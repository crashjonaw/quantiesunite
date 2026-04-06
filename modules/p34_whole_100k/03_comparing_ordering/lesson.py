TITLE = "Comparing and Ordering Numbers to 100,000"
SECTIONS = [
    {
        "title": "Comparison Symbols and Strategy",
        "body": """
<h3>Which Number is Bigger?</h3>
<p>Now that we can read large numbers, we need to compare them. We use special symbols:</p>

<div class="formula-box" style="text-align: center; margin: 20px auto; padding: 15px; background: #f0f9ff">
  <p style="font-size: 16px; margin: 5px;">\\( < \\) means "is less than"</p>
  <p style="font-size: 16px; margin: 5px;">\\( > \\) means "is greater than"</p>
  <p style="font-size: 16px; margin: 5px;">\\( = \\) means "is equal to"</p>
</div>

<h3>The Key Strategy: Look Left to Right</h3>
<p>To compare two numbers, always start with the <strong>leftmost (highest) place value</strong>. The first digit that is different tells us which number is larger.</p>

<div class="concept-box">
<h4>Comparison Rule</h4>
<p><strong>Step 1:</strong> Compare the ten thousands place first. Whoever has the bigger digit there wins!</p>
<p><strong>Step 2:</strong> If the ten thousands digits are the same, look at the thousands place.</p>
<p><strong>Step 3:</strong> Keep moving right until you find a difference.</p>
</div>

<h3>A Visual Number Line</h3>
<p>Numbers get bigger as we move right on a number line:</p>

<div class="diagram-container">
  <svg width="660" height="80" viewBox="0 0 660 80">
    <line x1="20" y1="40" x2="630" y2="40" stroke='#8b949e' stroke-width="2"/>
    <circle cx="20" cy="40" r="4" fill='#ef4444'/>
    <text x="20" y="65" text-anchor='middle' font-size='12' fill='currentColor'>10,000</text>
    <circle cx="150" cy="40" r="4" fill='#cccccc'/>
    <text x="150" y="65" text-anchor='middle' font-size='12' fill='currentColor'>35,000</text>
    <circle cx="300" cy="40" r="4" fill='#cccccc'/>
    <text x="300" y="65" text-anchor='middle' font-size='12' fill='currentColor'>60,000</text>
    <circle cx="450" cy="40" r="4" fill='#cccccc'/>
    <text x="450" y="65" text-anchor='middle' font-size='12' fill='currentColor'>85,000</text>
    <circle cx="630" cy="40" r="4" fill='#22c55e'/>
    <text x="630" y="65" text-anchor='middle' font-size='12' fill='currentColor'>100,000</text>
    <text x="325" y="25" text-anchor='middle' font-size='12' fill='currentColor'>Smaller                            Larger</text>
  </svg>
</div>
"""
    },
    {
        "title": "Comparing Two Numbers",
        "body": """
<h3>Step-by-Step Comparison</h3>
<p>Let's compare two numbers using our strategy.</p>

<div class="example-box">
<h4>Example 1: Compare 45,230 and 42,890</h4>

<p><strong>Step 1: Compare the ten thousands place</strong></p>
<p>45,230 has <strong>4</strong> in the ten thousands place</p>
<p>42,890 has <strong>4</strong> in the ten thousands place</p>
<p>They're the same (4 = 4), so we continue...</p>

<p><strong>Step 2: Compare the thousands place</strong></p>
<p>45,230 has <strong>5</strong> in the thousands place</p>
<p>42,890 has <strong>2</strong> in the thousands place</p>
<p>Since 5 > 2, we found our answer!</p>

<p style="font-size: 16px; margin-top: 15px; text-align: center;"><strong>\\(45{,}230 > 42{,}890\\)</strong></p>
</div>

<div class="example-box">
<h4>Example 2: Compare 78,450 and 87,450</h4>

<p><strong>Step 1: Compare the ten thousands place</strong></p>
<p>78,450 has <strong>7</strong> in the ten thousands place</p>
<p>87,450 has <strong>8</strong> in the ten thousands place</p>
<p>Since 7 < 8, we're done!</p>

<p style="font-size: 16px; margin-top: 15px; text-align: center;"><strong>\\(78{,}450 < 87{,}450\\)</strong></p>
</div>

<h3>A Shortcut: Count the Digits First</h3>
<p>If two numbers have different numbers of digits, the one with more digits is always larger:</p>

<div class="success-box">
<p><strong>\\(4{,}999 < 50{,}000\\)</strong> (because 4,999 has 4 digits and 50,000 has 5 digits)</p>
<p>We don't even need to look closely—5 digits beats 4 digits every time!</p>
</div>
"""
    },
    {
        "title": "Ordering Multiple Numbers",
        "body": """
<h3>From Least to Greatest</h3>
<p>When we have several numbers, we need to arrange them in order. We compare them using our place value strategy.</p>

<div class="example-box">
<h4>Example: Order These Numbers from Least to Greatest</h4>
<p><strong>Numbers:</strong> 23,456 | 2,345 | 32,456 | 23,465 | 32,450</p>

<p><strong>Step 1: Count digits</strong></p>
<ul>
  <li>2,345 has 4 digits (this is the smallest!)</li>
  <li>The others have 5 digits</li>
</ul>

<p><strong>Step 2: Among the 5-digit numbers, look at ten thousands place</strong></p>
<ul>
  <li>23,456 and 23,465 start with 23...</li>
  <li>32,456 and 32,450 start with 32...</li>
  <li>The 23,000s are smaller, so they come first</li>
</ul>

<p><strong>Step 3: Compare within the 23,000s</strong></p>
<ul>
  <li>23,456 and 23,465 have the same ten thousands and thousands</li>
  <li>Look at hundreds: both have 4</li>
  <li>Look at tens: 23,456 has 5, and 23,465 has 6</li>
  <li>Since 5 < 6, the order is 23,456 then 23,465</li>
</ul>

<p><strong>Step 4: Compare within the 32,000s</strong></p>
<ul>
  <li>32,456 has 5 in the hundreds place</li>
  <li>32,450 has 5 in the hundreds place</li>
  <li>Look at tens: 32,450 has 5, and 32,456 has 5</li>
  <li>Look at ones: 32,450 has 0, and 32,456 has 6</li>
  <li>Since 0 < 6, the order is 32,450 then 32,456</li>
</ul>

<p style="font-size: 16px; margin-top: 15px; text-align: center;"><strong>Final Answer:</strong></p>
<p style="text-align: center; font-size: 15px;"><strong>\\(2{,}345 < 23{,}456 < 23{,}465 < 32{,}450 < 32{,}456\\)</strong></p>
</div>

<h3>From Greatest to Least</h3>
<p>To order from greatest to least, just reverse the order above!</p>

<p style="text-align: center; font-size: 15px;"><strong>\\(32{,}456 > 32{,}450 > 23{,}465 > 23{,}456 > 2{,}345\\)</strong></p>
"""
    },
    {
        "title": "Practical Ordering: Real-World Comparisons",
        "body": """
<h3>Using Comparison in Real Life</h3>
<p>We compare numbers all the time in real situations.</p>

<h3>Example 1: City Populations</h3>
<p>Three nearby cities have these populations:</p>
<ul>
  <li>Smallville: 8,500 people</li>
  <li>Midtown: 24,300 people</li>
  <li>Largecity: 47,200 people</li>
</ul>

<p>Order from smallest to largest:</p>
<p style="text-align: center; font-size: 14px;"><strong>\\(8{,}500 < 24{,}300 < 47{,}200\\)</strong></p>

<h3>Example 2: Attendance at Events</h3>
<p>A week of games had these attendance numbers:</p>
<ul>
  <li>Monday: 15,600 fans</li>
  <li>Tuesday: 12,400 fans</li>
  <li>Wednesday: 18,900 fans</li>
</ul>

<p>Which day had the most fans?</p>
<p style="text-align: center; font-size: 14px;"><strong>Wednesday (18,900)</strong></p>

<div class="success-box">
<h4>Key Takeaway</h4>
<p>Comparing and ordering help us understand which quantity is bigger, smaller, or in between. This is a skill we use every day!</p>
</div>
"""
    }
]
