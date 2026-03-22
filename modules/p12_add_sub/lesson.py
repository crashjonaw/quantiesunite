"""Multi-digit Addition & Subtraction — Lesson sections."""

SECTIONS = [
    {
        "title": "Understanding Place Value: The Foundation 🏢",
        "body": """<p>Before we add and subtract large numbers, we need to understand <strong>place value</strong>. Every digit in a number has a different job depending on where it sits.</p>
<p>Think of place value like a building with different floors:</p>
<svg width="300" height="200" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="20" font-size="16" font-weight="bold">The number 245:</text>

  <rect x="30" y="40" width="60" height="60" fill="gold" stroke="orange" stroke-width="2"/>
  <text x="40" y="85" font-size="20" font-weight="bold">2</text>
  <text x="30" y="120" font-size="14" font-weight="bold">Hundreds</text>
  <text x="25" y="140" font-size="12">(2 × 100)</text>

  <rect x="120" y="40" width="60" height="60" fill="lightblue" stroke="blue" stroke-width="2"/>
  <text x="130" y="85" font-size="20" font-weight="bold">4</text>
  <text x="115" y="120" font-size="14" font-weight="bold">Tens</text>
  <text x="110" y="140" font-size="12">(4 × 10)</text>

  <rect x="210" y="40" width="60" height="60" fill="lightgreen" stroke="green" stroke-width="2"/>
  <text x="220" y="85" font-size="20" font-weight="bold">5</text>
  <text x="210" y="120" font-size="14" font-weight="bold">Ones</text>
  <text x="210" y="140" font-size="12">(5 × 1)</text>
</svg>
<p>So 245 = 200 + 40 + 5. Each digit is in its own "place" and has a different value!</p>
<div class='example-box'>
<strong>Another example: 623</strong><br>
6 is in the <strong>hundreds</strong> place = 600<br>
2 is in the <strong>tens</strong> place = 20<br>
3 is in the <strong>ones</strong> place = 3<br>
Total: 600 + 20 + 3 = 623
</div>
<p><strong>Why is this important?</strong> When we add and subtract, we work with each place separately. We don't mix hundreds with tens or ones!</p>"""
    },
    {
        "title": "Addition Without Carrying: The Easy Way ➕",
        "body": """<p>Let's start with addition that doesn't require carrying. We simply add each place value separately.</p>
<p><strong>Example: 123 + 214</strong></p>
<svg width="350" height="220" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Step 1: Line up the numbers by place value</text>

  <text x="50" y="60" font-size="16">123</text>
  <text x="45" y="80" font-size="16">+ 214</text>
  <line x1="30" y1="85" x2="120" y2="85" stroke="black" stroke-width="2"/>

  <text x="10" y="130" font-size="14" font-weight="bold">Step 2: Add each column (starting from the right)</text>

  <text x="50" y="165" font-size="16">Ones: 3 + 4 = 7</text>
  <text x="50" y="190" font-size="16">Tens: 2 + 1 = 3</text>
  <text x="50" y="215" font-size="16">Hundreds: 1 + 2 = 3</text>
</svg>
<div class='example-box'>
<strong>Answer: 337</strong><br>
<br>
Why did we get 337?<br>
🟡 Hundreds place: 1 + 2 = 3<br>
🔵 Tens place: 2 + 1 = 3<br>
🟢 Ones place: 3 + 4 = 7<br>
= 337
</div>
<p>The key: <strong>Always line up the place values</strong>. Ones go with ones, tens with tens, hundreds with hundreds!</p>"""
    },
    {
        "title": "Addition WITH Carrying: The Big Jump 🎯",
        "body": """<p>Sometimes when we add ones, tens, or hundreds, we get 10 or more. When that happens, we need to <strong>carry</strong> to the next place. This is why it's called "carrying"!</p>
<p><strong>Example: 27 + 15</strong></p>
<svg width="350" height="280" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Step 1: Line them up</text>
  <text x="50" y="60" font-size="16">27</text>
  <text x="45" y="80" font-size="16">+ 15</text>

  <text x="10" y="120" font-size="14" font-weight="bold">Step 2: Add the ones column (7 + 5)</text>
  <text x="50" y="155" font-size="16" style="color: red;">7 + 5 = 12</text>
  <text x="50" y="180" font-size="14">We got 12! That's 1 ten and 2 ones.</text>

  <text x="10" y="220" font-size="14" font-weight="bold">Step 3: Write the 2 in the ones place, carry the 1 to tens</text>
  <text x="50" y="255" font-size="16" style="color: blue;">Carry: 1 + 2 + 1 = 4 tens</text>
  <text x="50" y="280" font-size="16" font-weight="bold">Answer: 42</text>
</svg>
<div class='example-box'>
<strong>The Carrying Process:</strong><br>
27<br>
+15<br>
—<br>
🟢 Ones: 7 + 5 = 12 → Write 2, carry 1<br>
🔵 Tens: 1 (carry) + 2 + 1 = 4<br>
= 42
</div>
<p><strong>Why do we carry?</strong> Because 10 ones = 1 ten! When we have 10 or more ones, we bundle them into tens.</p>"""
    },
    {
        "title": "Subtraction Without Borrowing: Taking Away ➖",
        "body": """<p>Subtraction means taking away. When the digit on top is bigger than the digit below, we can subtract without borrowing.</p>
<p><strong>Example: 456 - 123</strong></p>
<svg width="350" height="220" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Step 1: Line them up by place value</text>

  <text x="50" y="60" font-size="16">456</text>
  <text x="45" y="80" font-size="16">- 123</text>
  <line x1="30" y1="85" x2="120" y2="85" stroke="black" stroke-width="2"/>

  <text x="10" y="130" font-size="14" font-weight="bold">Step 2: Subtract each column (from right to left)</text>

  <text x="50" y="165" font-size="16">Ones: 6 - 3 = 3</text>
  <text x="50" y="190" font-size="16">Tens: 5 - 2 = 3</text>
  <text x="50" y="215" font-size="16">Hundreds: 4 - 1 = 3</text>
</svg>
<div class='example-box'>
<strong>Answer: 333</strong><br>
<br>
Each digit on top is bigger than (or equal to) the digit below, so we can subtract easily!
</div>
<p><strong>Key idea:</strong> Subtraction is the opposite of addition. If you add 123 to 333, you get 456!</p>"""
    },
    {
        "title": "Subtraction WITH Borrowing: When We Need Help 🤝",
        "body": """<p>Sometimes the digit on top is SMALLER than the digit below. Then we need to <strong>borrow</strong> from the next place value. It's like asking a friend for help!</p>
<p><strong>Example: 32 - 15</strong></p>
<svg width="380" height="300" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Step 1: Look at the ones column (2 - 5)</text>
  <text x="50" y="55" font-size="16" style="color: red;">32</text>
  <text x="45" y="75" font-size="16">- 15</text>
  <text x="50" y="100" font-size="14">Can we do 2 - 5? NO! 2 is smaller than 5.</text>

  <text x="10" y="150" font-size="14" font-weight="bold">Step 2: Borrow 1 ten from the tens place</text>
  <text x="50" y="180" font-size="14">The 3 tens becomes 2 tens</text>
  <text x="50" y="205" font-size="14">The 2 ones becomes 12 ones (2 + 10 = 12)</text>

  <text x="10" y="255" font-size="14" font-weight="bold">Step 3: Now subtract!</text>
  <text x="50" y="285" font-size="16">12 - 5 = 7 (ones), then 2 - 1 = 1 (tens) → <strong>Answer: 17</strong></text>
</svg>
<div class='example-box'>
<strong>The Borrowing Process Visualized:</strong><br>
<br>
Original: 3 tens, 2 ones = 32<br>
After borrowing: 2 tens, 12 ones<br>
<br>
Now subtract:<br>
12 - 5 = 7<br>
2 - 1 = 1<br>
= 17
</div>
<p><strong>Why does borrowing work?</strong> 1 ten = 10 ones. When we borrow 1 ten, we're breaking it into 10 ones so we have enough to subtract from!</p>
<p><strong>Check your answer:</strong> If 32 - 15 = 17, then 17 + 15 should equal 32. Let's see: 17 + 15 = 32 ✓ Correct!</p>"""
    }
]
