TITLE = "Adding Ones and Tens (Without Carrying)"

SECTIONS = [
    {
        "title": "Why Do We Need Place Value?",
        "body": """<p>You already know how to add small numbers: <strong>\(3 + 4 = 7\)</strong>. Easy! But what if someone gives you 23 apples, and then you get 14 more? Can you count them all on your fingers?</p>
<p>That's where <strong>place value</strong> saves us. Instead of counting one by one, we can organize numbers into <strong>tens</strong> and <strong>ones</strong>, and add them separately.</p>
<div class="concept-box">
<p><strong>Place Value is like organizing money in your wallet:</strong></p>
<ul>
<li>You keep 10-dollar bills separate from 1-dollar bills</li>
<li>When you have coins, you count them separately too</li>
<li>Then you add everything up</li>
</ul>
</div>"""
    },
    {
        "title": "Understanding Tens and Ones",
        "body": """<p>Every number from 0 to 100 can be split into <strong>tens</strong> and <strong>ones</strong>.</p>
<p><strong>Example: The number 34</strong></p>
<svg viewBox="0 0 415 140" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Tens rods -->
  <g>
    <rect x="15" y="15" width="15" height="70" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
    <rect x="38" y="15" width="15" height="70" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
    <rect x="61" y="15" width="15" height="70" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
    <text x="45" y="110" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>3 tens = 30</text>
  </g>
  <!-- Ones cubes -->
  <g>
    <circle cx="130" cy="50" r="8" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
    <circle cx="152" cy="50" r="8" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
    <circle cx="174" cy="50" r="8" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
    <circle cx="196" cy="50" r="8" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
    <text x="163" y="110" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>4 ones = 4</text>
  </g>
  <!-- Equals -->
  <text x="270" y="55" fill='currentColor' font-size='22' font-weight='bold'>=</text>
  <!-- Result -->
  <text x="330" y="58" fill='#f59e0b' font-size='28' font-weight='bold'>34</text>
</svg>
<p><strong>So \(34 = 30 + 4\)</strong> (or 3 tens and 4 ones)</p>
<p>Every two-digit number works the same way:</p>
<ul>
<li><strong>23</strong> = 2 tens and 3 ones = \(20 + 3\)</li>
<li><strong>45</strong> = 4 tens and 5 ones = \(40 + 5\)</li>
<li><strong>67</strong> = 6 tens and 7 ones = \(60 + 7\)</li>
<li><strong>89</strong> = 8 tens and 9 ones = \(80 + 9\)</li>
</ul>"""
    },
    {
        "title": "Adding Tens and Ones Separately",
        "body": """<p>Here's the magic: <strong>When we add two numbers, we can add the tens separately from the ones!</strong></p>
<p><strong>Example: 23 + 14</strong></p>
<div class="worked-example">
<p><strong>Method: Split each number into tens and ones, then add</strong></p>
<svg viewBox="0 0 555 175" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <!-- First number -->
  <text x="60" y="22" fill='currentColor' font-size='14' font-weight='bold'>23 = 20 + 3</text>
  <rect x="25" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
  <rect x="48" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
  <circle cx="95" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="112" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="129" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>

  <!-- Plus -->
  <text x="160" y="68" fill='currentColor' font-size='20' font-weight='bold'>+</text>

  <!-- Second number -->
  <text x="200" y="22" fill='currentColor' font-size='14' font-weight='bold'>14 = 10 + 4</text>
  <rect x="190" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
  <circle cx="235" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="252" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="269" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="286" cy="62" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>

  <!-- Equals -->
  <text x="315" y="68" fill='currentColor' font-size='20' font-weight='bold'>=</text>

  <!-- Add tens -->
  <text x="355" y="22" fill='currentColor' font-size='13'>Tens: 20 + 10 = 30</text>
  <rect x="350" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
  <rect x="373" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
  <rect x="396" y="35" width="15" height="55" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>

  <!-- Add ones -->
  <text x="355" y="115" fill='currentColor' font-size='13'>Ones: 3 + 4 = 7</text>
  <circle cx="430" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="447" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="464" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="481" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="498" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="515" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="532" cy="135" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
</svg>
<p><strong>\(30 + 7 = 37\)</strong></p>
<p style="margin-top: 20px;"><strong>Why this works:</strong> Addition is the same whether we add all at once or break it into pieces. Mathematicians call this the <strong>associative property</strong>. For kids, think of it like: it doesn't matter if you eat 3 apples then 4 apples, or 7 apples all at once—you still ate 7!</p>
</div>"""
    },
    {
        "title": "The Column Method (Adding Vertically)",
        "body": """<p>We can write addition in a column to make it clearer. This is the standard method everyone uses.</p>
<p><strong>Example: 34 + 23</strong></p>
<div class="worked-example">
<svg viewBox="0 0 360 215" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <!-- Column setup -->
  <text x="85" y="30" fill='currentColor' font-size='14' font-weight='bold'>Tens  Ones</text>

  <!-- First number -->
  <text x="100" y="62" fill='currentColor' font-size='18' font-weight='bold'>3</text>
  <text x="150" y="62" fill='currentColor' font-size='18' font-weight='bold'>4</text>

  <!-- Second number -->
  <text x="78" y="90" fill='currentColor' font-size='18'>+</text>
  <text x="100" y="90" fill='currentColor' font-size='18' font-weight='bold'>2</text>
  <text x="150" y="90" fill='currentColor' font-size='18' font-weight='bold'>3</text>

  <!-- Line -->
  <line x1="70" y1="100" x2="175" y2="100" stroke='#8b949e' stroke-width="2"/>

  <!-- Result digits -->
  <text x="100" y="128" fill='currentColor' font-size='18' font-weight='bold'>5</text>
  <text x="150" y="128" fill='currentColor' font-size='18' font-weight='bold'>7</text>

  <!-- Annotations - spaced apart, to the right -->
  <text x="195" y="85" fill='#4f8ef7' font-size='12'>Tens: 3 + 2 = 5</text>
  <text x="195" y="105" fill='#22c55e' font-size='12'>Ones: 4 + 3 = 7</text>

  <!-- Result label -->
  <text x="70" y="165" fill='#f59e0b' font-size='16' font-weight='bold'>Answer: 57</text>
</svg>
<p><strong>Steps:</strong></p>
<ol>
<li>Line up the numbers by place value (tens under tens, ones under ones)</li>
<li>Add the <strong>ones column first</strong>: \(4 + 3 = 7\)</li>
<li>Add the <strong>tens column</strong>: \(3 + 2 = 5\)</li>
<li>Write the answer: 57</li>
</ol>
</div>"""
    },
    {
        "title": "Practice: Adding Without Carrying",
        "body": """<p>Let's try some examples together. Remember: add the ones first, then the tens. No carrying needed yet!</p>
<div class="mcq-group">
  <p><strong>What is \(34 + 22\)?</strong></p>
  <p><em>Think: Ones: \(4 + 2 = 6\). Tens: \(3 + 2 = 5\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">46</button>
    <button class="mcq-option" data-correct="true" data-explanation="Ones: 4 + 2 = 6. Tens: 3 + 2 = 5. Answer: 56">56</button>
    <button class="mcq-option" data-correct="false">66</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is \(42 + 35\)?</strong></p>
  <p><em>Think: Ones: \(2 + 5 = 7\). Tens: \(4 + 3 = 7\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">67</button>
    <button class="mcq-option" data-correct="true" data-explanation="Ones: 2 + 5 = 7. Tens: 4 + 3 = 7. Answer: 77">77</button>
    <button class="mcq-option" data-correct="false">87</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is \(23 + 14\)?</strong></p>
  <p><em>Think: Ones: \(3 + 4 = 7\). Tens: \(2 + 1 = 3\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Ones: 3 + 4 = 7. Tens: 2 + 1 = 3. Answer: 37">37</button>
    <button class="mcq-option" data-correct="false">47</button>
    <button class="mcq-option" data-correct="false">27</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    }
]
