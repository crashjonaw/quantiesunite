"""Simple Fractions (1/2, 1/4, 3/4) — Lesson sections."""

SECTIONS = [
    {
        "title": "What is a Fraction? Parts of a Whole",
        "body": """<p>A <strong>fraction</strong> is a piece or part of something whole. When you divide something into equal parts, each part is a fraction.</p>
<p>Think of a pizza cut into slices, or a chocolate bar broken into pieces — each piece is a fraction of the whole!</p>
<svg viewBox="0 0 400 195" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">Examples of fractions:</text>

  <!-- Half pizza -->
  <circle cx="80" cy="105" r="50" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <line x1="80" y1="55" x2="80" y2="155" stroke="#d4a574" stroke-width="2"/>
  <path d="M 80 55 A 50 50 0 0 0 80 155 Z" fill="#ffb347" stroke="none"/>
  <text x="58" y="110" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="45" y="180" font-size="11" fill="currentColor">half a pizza</text>

  <!-- Quarter square -->
  <rect x="175" y="55" width="80" height="80" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <line x1="175" y1="95" x2="255" y2="95" stroke="#8b6914" stroke-width="2"/>
  <line x1="215" y1="55" x2="215" y2="135" stroke="#8b6914" stroke-width="2"/>
  <rect x="175" y="55" width="40" height="40" fill="#c9a86c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <text x="200" y="110" font-size="14" font-weight="bold" fill="#5d4b0f">1/4</text>
  <text x="175" y="180" font-size="11" fill="currentColor">quarter of a square</text>

  <!-- Three quarters circle -->
  <circle cx="340" cy="105" r="40" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="340" y1="65" x2="340" y2="145" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="300" y1="105" x2="380" y2="105" stroke="#4f8ef7" stroke-width="2"/>
  <path d="M 340 65 A 40 40 0 1 0 300 105 L 340 105 Z" fill="#7ab8f5" opacity="0.6" stroke="none"/>
  <text x="325" y="110" font-size="14" font-weight="bold" fill="#2c5282">3/4</text>
  <text x="305" y="180" font-size="11" fill="currentColor">three quarters</text>
</svg>
<div class='example-box'>
<strong>Key idea:</strong> A fraction has two parts:<br>
— The <strong>top number</strong> (numerator): How many pieces we're talking about<br>
— The <strong>bottom number</strong> (denominator): How many equal pieces the whole is cut into
</div>
<p><strong>Why are fractions important?</strong> We use fractions every day — cutting food, sharing items, telling time, and measuring!</p>"""
    },
    {
        "title": "Understanding Halves (1/2)",
        "body": """<p>A <strong>half</strong> is when you cut something into 2 equal pieces. Each piece is 1/2 of the whole.</p>
<p>The bottom number is 2 (two equal pieces) and the top number is 1 (we're talking about one of those pieces).</p>
<svg viewBox="0 0 400 270" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">A whole divided into halves:</text>

  <!-- Whole rectangle -->
  <rect x="15" y="45" width="100" height="70" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="40" y="88" font-size="16" font-weight="bold" fill="#8b6914">Whole</text>

  <!-- Arrow -->
  <text x="130" y="88" font-size="18" fill="currentColor" opacity="0.6">Cut it</text>

  <!-- Two halves side by side -->
  <rect x="195" y="45" width="48" height="70" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="207" y="88" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>

  <rect x="253" y="45" width="48" height="70" fill="#f5e6c8" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="265" y="88" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>

  <!-- Explanation text -->
  <text x="15" y="145" font-size="13" fill="currentColor">Each piece is <tspan font-weight="bold">1/2</tspan></text>
  <text x="15" y="165" font-size="13" fill="currentColor">Two halves = one whole</text>

  <!-- Combining halves -->
  <text x="15" y="200" font-size="14" font-weight="bold" fill="currentColor">Put them back together:</text>
  <rect x="15" y="215" width="48" height="40" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="27" y="240" font-size="12" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="73" y="240" font-size="20" font-weight="bold" fill="currentColor" opacity="0.6">+</text>
  <rect x="95" y="215" width="48" height="40" fill="#f5e6c8" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="107" y="240" font-size="12" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="155" y="240" font-size="20" font-weight="bold" fill="currentColor" opacity="0.6">=</text>
  <rect x="180" y="215" width="100" height="40" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="200" y="242" font-size="14" font-weight="bold" fill="#8b6914">1 Whole</text>
</svg>
<div class='example-box'>
<strong>Real-world halves:</strong><br>
Half a pizza, half an apple, half a cake, half an hour = 30 minutes
</div>
<p><strong>Important fact:</strong> If you have 1/2 of something and get another 1/2 of the same thing, you have the whole thing!<br>1/2 + 1/2 = 1 whole</p>"""
    },
    {
        "title": "Understanding Quarters (1/4 and 3/4)",
        "body": """<p>A <strong>quarter</strong> is when you cut something into 4 equal pieces. Each piece is 1/4 of the whole.</p>
<p>Three quarters (3/4) means you have 3 of those 4 pieces.</p>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">A whole divided into quarters:</text>

  <!-- Whole square with quarter lines -->
  <rect x="15" y="45" width="80" height="80" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <line x1="55" y1="45" x2="55" y2="125" stroke="#8b6914" stroke-width="2"/>
  <line x1="15" y1="85" x2="95" y2="85" stroke="#8b6914" stroke-width="2"/>
  <text x="30" y="95" font-size="13" font-weight="bold" fill="#5d4b0f">Whole</text>

  <!-- Four separate quarter pieces -->
  <text x="15" y="155" font-size="13" font-weight="bold" fill="currentColor">Four quarters:</text>

  <rect x="15" y="168" width="38" height="38" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <text x="25" y="192" font-size="11" font-weight="bold" fill="#5d4b0f">1/4</text>

  <rect x="63" y="168" width="38" height="38" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <text x="73" y="192" font-size="11" font-weight="bold" fill="#5d4b0f">1/4</text>

  <rect x="111" y="168" width="38" height="38" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <text x="121" y="192" font-size="11" font-weight="bold" fill="#5d4b0f">1/4</text>

  <rect x="159" y="168" width="38" height="38" fill="#d2b48c" stroke="#8b6914" stroke-width="2" rx="4"/>
  <text x="169" y="192" font-size="11" font-weight="bold" fill="#5d4b0f">1/4</text>

  <text x="210" y="192" font-size="13" fill="currentColor">All 4 quarters = 1 whole</text>

  <!-- Three quarters (3/4) shown with shading -->
  <text x="15" y="235" font-size="13" font-weight="bold" fill="currentColor">Three quarters (3/4):</text>

  <rect x="140" y="45" width="80" height="80" fill="#a8e6a8" stroke="#27ae60" stroke-width="2" rx="4"/>
  <line x1="180" y1="45" x2="180" y2="125" stroke="#27ae60" stroke-width="2"/>
  <line x1="140" y1="85" x2="220" y2="85" stroke="#27ae60" stroke-width="2"/>
  <!-- Shade 3 of the 4 quarters -->
  <rect x="140" y="45" width="40" height="40" fill="#66cc66" stroke="#27ae60" stroke-width="2" rx="4"/>
  <rect x="180" y="45" width="40" height="40" fill="#66cc66" stroke="#27ae60" stroke-width="2" rx="4"/>
  <rect x="140" y="85" width="40" height="40" fill="#66cc66" stroke="#27ae60" stroke-width="2" rx="4"/>
  <text x="155" y="72" font-size="12" font-weight="bold" fill="#fff">3/4</text>
  <text x="195" y="72" font-size="10" fill="#fff">filled</text>
  <text x="195" y="112" font-size="10" fill="#27ae60">1/4</text>
  <text x="152" y="255" font-size="13" font-weight="bold" fill="#27ae60">3/4 shaded</text>
</svg>
<div class='example-box'>
<strong>Important relationships:</strong><br>
1/4 + 1/4 + 1/4 + 1/4 = 1 whole<br>
1/4 + 1/4 + 1/4 = 3/4<br>
1/4 + 3/4 = 1 whole (a quarter plus three quarters = the whole!)
</div>
<p><strong>Real-world quarters:</strong><br>A quarter of an hour = 15 minutes<br>A quarter of the year = 3 months<br>A quarter portion at a restaurant</p>"""
    },
    {
        "title": "Comparing Fractions: Which is Bigger?",
        "body": """<p>Now that we understand halves and quarters, we can <strong>compare</strong> them to see which is bigger!</p>
<p>Visual comparison is the best way to understand this at first.</p>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">Comparing halves to quarters:</text>

  <!-- Half square -->
  <rect x="15" y="45" width="80" height="80" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <line x1="55" y1="45" x2="55" y2="125" stroke="#d4a574" stroke-width="2"/>
  <rect x="15" y="45" width="40" height="80" fill="#ffb347" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="25" y="93" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="15" y="150" font-size="12" fill="currentColor">Takes up more space!</text>

  <!-- Quarter square -->
  <rect x="140" y="45" width="80" height="80" fill="#a8e6a8" stroke="#27ae60" stroke-width="2" rx="4"/>
  <line x1="180" y1="45" x2="180" y2="125" stroke="#27ae60" stroke-width="2"/>
  <line x1="140" y1="85" x2="220" y2="85" stroke="#27ae60" stroke-width="2"/>
  <rect x="140" y="45" width="40" height="40" fill="#66cc66" stroke="#27ae60" stroke-width="2" rx="4"/>
  <text x="150" y="72" font-size="12" font-weight="bold" fill="#fff">1/4</text>
  <text x="140" y="150" font-size="12" fill="currentColor">Smaller piece</text>

  <!-- Comparison result -->
  <text x="260" y="85" font-size="20" font-weight="bold" fill="#27ae60">1/2 &gt; 1/4</text>

  <!-- Rules -->
  <text x="15" y="190" font-size="13" font-weight="bold" fill="currentColor">Rule: Same whole size</text>
  <text x="15" y="215" font-size="13" fill="currentColor">1/2 is BIGGER than 1/4</text>
  <text x="15" y="240" font-size="13" fill="currentColor">1/2 = 2/4 (two quarters)</text>
  <text x="15" y="265" font-size="13" fill="currentColor">3/4 is BIGGER than 1/4</text>
</svg>
<div class='example-box'>
<strong>Key insight:</strong> When the bottom number (denominator) is SMALLER, the pieces are BIGGER!<br>
<br>
Think about it: If you cut a pizza into 2 pieces, each piece is bigger than if you cut it into 4 pieces!
</div>
<p><strong>Comparing unit fractions:</strong> Unit fractions have a 1 on top (like 1/2, 1/4, 1/3).<br>1/2 &gt; 1/4 &gt; 1/8 (because fewer pieces = bigger pieces!)</p>"""
    },
    {
        "title": "Fractions in Daily Life",
        "body": """<p>Fractions aren't just math — we use them constantly in real life!</p>
<svg viewBox="0 0 400 310" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">Real-world fraction examples:</text>

  <rect x="15" y="45" width="370" height="50" fill="#fff8e1" stroke="#d4a574" stroke-width="1" rx="4"/>
  <text x="25" y="75" font-size="13" fill="currentColor">Pizza: "I ate 1/2 of the pizza" or "Can I have 1/4?"</text>

  <rect x="15" y="110" width="370" height="50" fill="#e3f2fd" stroke="#4f8ef7" stroke-width="1" rx="4"/>
  <text x="25" y="133" font-size="13" fill="currentColor">Time: "Half an hour" (1/2 hour) = 30 minutes,</text>
  <text x="25" y="150" font-size="13" fill="currentColor">"A quarter hour" = 15 minutes</text>

  <rect x="15" y="175" width="370" height="50" fill="#e8f5e9" stroke="#27ae60" stroke-width="1" rx="4"/>
  <text x="25" y="205" font-size="13" fill="currentColor">Measurements: 1/4 cup of sugar, 1/2 liter of milk</text>

  <rect x="15" y="240" width="370" height="50" fill="#fce4ec" stroke="#e74c3c" stroke-width="1" rx="4"/>
  <text x="25" y="263" font-size="13" fill="currentColor">Sharing: "There's enough for 3/4 of the class"</text>
  <text x="25" y="280" font-size="13" fill="currentColor">or sharing treats equally</text>
</svg>
<div class='example-box'>
<strong>Why learn fractions?</strong><br>
- Cooking and baking (recipes use fractions!)<br>
- Sharing fairly with friends and family<br>
- Telling time (quarter past, half past)<br>
- Measuring distances and amounts<br>
- Understanding discounts and sales
</div>
<p><strong>Practice tip:</strong> Point out fractions whenever you see them in real life. Understanding that 1/2 cup is HALF of a 1-cup measure makes fractions make sense!</p>"""
    }
]
