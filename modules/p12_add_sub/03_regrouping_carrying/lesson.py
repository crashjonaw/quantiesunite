TITLE = "Regrouping: Carrying and Borrowing"

SECTIONS = [
    {
        "title": "What Happens When Ones Add Up to 10 or More?",
        "body": """<p>You know how to add: \(23 + 14 = 37\). But what if the ones add up to more than 9?</p>
<p><strong>Example: \(27 + 15\)</strong></p>
<p>If we try to add ones: \(7 + 5 = 12\). But wait! We can't write 12 in the ones place. The ones column only holds digits 0-9.</p>
<div class="concept-box">
<p><strong>Here's the magic:</strong> When we get 10 ones, we can trade them for 1 ten!</p>
<p>Remember: <strong>10 ones = 1 ten</strong></p>
</div>
<p>Think of it like having 10 one-dollar bills. You can trade them for 1 ten-dollar bill!</p>
<svg viewBox="0 0 365 85" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="130" y="20" fill='currentColor' font-size='14' text-anchor='middle'>10 ones</text>
  <circle cx="25" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="42" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="59" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="76" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="93" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="110" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="127" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="144" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="161" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>
  <circle cx="178" cy="48" r="6" fill='#22c55e' stroke='currentColor' stroke-width="1"/>

  <text x="230" y="53" fill='currentColor' font-size='18' font-weight='bold'>=</text>

  <text x="310" y="20" fill='currentColor' font-size='14' text-anchor='middle'>1 ten</text>
  <rect x="295" y="32" width="30" height="40" fill='#4f8ef7' stroke='currentColor' stroke-width="2" rx='4'/>
</svg>"""
    },
    {
        "title": "Carrying in Addition (Regrouping Ones to Tens)",
        "body": """<p>When the ones column adds up to 10 or more, we "carry" the extra ten to the tens place.</p>
<p><strong>Example: 27 + 15</strong></p>
<div class="worked-example">
<svg viewBox="0 0 520 250" style="width:100%;max-width:560px;height:auto;display:block;margin:16px auto;">
  <!-- Step 1 -->
  <text x="15" y="25" fill='currentColor' font-size='14' font-weight='bold'>Step 1: Add the ones (7 + 5)</text>
  <text x="15" y="48" fill='currentColor' font-size='13'>7 + 5 = 12</text>
  <text x="15" y="68" fill='#22c55e' font-size='13'>12 = 1 ten and 2 ones</text>
  <text x="15" y="88" fill='#f59e0b' font-size='13'>Write 2 in ones, carry 1 to tens</text>

  <!-- Column work -->
  <rect x="340" y="20" width="165" height="140" fill='none' stroke='#8b949e' stroke-width="1" rx='4'/>
  <text x="370" y="45" fill='currentColor' font-size='12' font-weight='bold'>Tens  Ones</text>
  <text x="410" y="65" fill='#ef4444' font-size='11'>1  (carry)</text>
  <text x="385" y="85" fill='currentColor' font-size='14'>2     7</text>
  <text x="370" y="108" fill='currentColor' font-size='14'>+  1     5</text>
  <line x1="360" y1="118" x2="490" y2="118" stroke='#8b949e' stroke-width="2"/>
  <text x="385" y="140" fill='currentColor' font-size='14' font-weight='bold'>4     2</text>

  <!-- Step 2 -->
  <text x="15" y="140" fill='currentColor' font-size='14' font-weight='bold'>Step 2: Add the tens (2 + 1 + 1 carry)</text>
  <text x="15" y="163" fill='#4f8ef7' font-size='13'>2 tens + 1 ten + 1 carried ten</text>
  <text x="15" y="183" fill='#4f8ef7' font-size='13'>2 + 1 + 1 = 4 tens</text>

  <!-- Result -->
  <text x="15" y="220" fill='#f59e0b' font-size='16' font-weight='bold'>Answer: 42</text>
</svg>
<p><strong>Why this works:</strong> \(27 + 15 = (20 + 7) + (10 + 5) = (20 + 10) + (7 + 5) = 30 + 12 = 42\)</p>
</div>"""
    },
    {
        "title": "Borrowing in Subtraction (Regrouping Tens to Ones)",
        "body": """<p>Sometimes in subtraction, the ones digit on top is smaller than the ones digit below. We can't do that! So we <strong>borrow</strong> 1 ten from the tens place and break it into 10 ones.</p>
<p><strong>Example: \(32 - 15\)</strong></p>
<p>Problem: We need to do \(2 - 5\) in the ones place, but \(2 < 5\).</p>
<div class="worked-example">
<svg viewBox="0 0 520 260" style="width:100%;max-width:560px;height:auto;display:block;margin:16px auto;">
  <!-- Step 1 -->
  <text x="15" y="25" fill='currentColor' font-size='14' font-weight='bold'>Step 1: Borrow 1 ten from the tens place</text>
  <text x="15" y="48" fill='#4f8ef7' font-size='13'>The 3 tens becomes 2 tens</text>
  <text x="15" y="68" fill='#22c55e' font-size='13'>The 2 ones becomes 12 ones (2 + 10)</text>

  <!-- Column work -->
  <rect x="340" y="20" width="165" height="155" fill='none' stroke='#8b949e' stroke-width="1" rx='4'/>
  <text x="370" y="45" fill='currentColor' font-size='12' font-weight='bold'>Tens  Ones</text>
  <text x="385" y="70" fill='currentColor' font-size='14'>3     2</text>
  <text x="370" y="93" fill='currentColor' font-size='14'>-  1     5</text>
  <line x1="360" y1="103" x2="490" y2="103" stroke='#8b949e' stroke-width="2"/>
  <text x="370" y="123" fill='#f59e0b' font-size='11'>after borrowing:</text>
  <text x="385" y="143" fill='currentColor' font-size='14'>2    12</text>
  <line x1="360" y1="150" x2="490" y2="150" stroke='#8b949e' stroke-width="2"/>
  <text x="385" y="168" fill='currentColor' font-size='14' font-weight='bold'>1     7</text>

  <!-- Step 2 -->
  <text x="15" y="140" fill='currentColor' font-size='14' font-weight='bold'>Step 2: Now subtract</text>
  <text x="15" y="163" fill='#22c55e' font-size='13'>Ones: 12 - 5 = 7</text>
  <text x="15" y="183" fill='#4f8ef7' font-size='13'>Tens: 2 - 1 = 1</text>

  <!-- Result -->
  <text x="15" y="225" fill='#f59e0b' font-size='16' font-weight='bold'>Answer: 17</text>
</svg>
<p><strong>Check:</strong> If \(32 - 15 = 17\), then \(17 + 15\) should equal 32. Let's check: \(17 + 15 = 32\) ✓</p>
</div>"""
    },
    {
        "title": "More Examples with Carrying and Borrowing",
        "body": """<p><strong>Carrying Example 1: 38 + 24</strong></p>
<svg viewBox="0 0 400 95" style="width:100%;max-width:430px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" fill='currentColor' font-size='13'>Ones: 8 + 4 = 12. Write 2, carry 1</text>
  <text x="15" y="48" fill='#4f8ef7' font-size='13'>Tens: 3 + 2 + 1 (carry) = 6</text>
  <text x="15" y="78" fill='#f59e0b' font-size='14' font-weight='bold'>Answer: 62</text>
</svg>
<p><strong>Borrowing Example 1: 53 - 28</strong></p>
<svg viewBox="0 0 400 95" style="width:100%;max-width:430px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" fill='currentColor' font-size='13'>Ones: 3 is less than 8, so borrow. 3 becomes 13</text>
  <text x="15" y="48" fill='#22c55e' font-size='13'>Ones: 13 - 8 = 5, Tens: 4 - 2 = 2</text>
  <text x="15" y="78" fill='#f59e0b' font-size='14' font-weight='bold'>Answer: 25</text>
</svg>"""
    },
    {
        "title": "Practice: Carrying and Borrowing",
        "body": """<p>Try these problems that need carrying or borrowing!</p>
<div class="mcq-group">
  <p><strong>What is \(27 + 15\)?</strong></p>
  <p><em>Hint: Ones: \(7 + 5 = 12\) (write 2, carry 1), Tens: \(2 + 1 + 1 = 4\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Ones: 7 + 5 = 12, write 2 and carry 1. Tens: 2 + 1 + 1 = 4. Answer: 42">42</button>
    <button class="mcq-option" data-correct="false">52</button>
    <button class="mcq-option" data-correct="false">32</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is \(32 - 15\)?</strong></p>
  <p><em>Hint: Ones: \(2 < 5\), so borrow. 2 becomes 12. Then \(12 - 5 = 7\), and \(2 - 1 = 1\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">27</button>
    <button class="mcq-option" data-correct="true" data-explanation="Borrow 1 ten: 32 becomes 2 tens 12 ones. Then: 12 - 5 = 7, 2 - 1 = 1. Answer: 17">17</button>
    <button class="mcq-option" data-correct="false">7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is \(48 + 34\)?</strong></p>
  <p><em>Hint: Ones: \(8 + 4 = 12\), carry. Tens: \(4 + 3 + 1 = 8\)</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">72</button>
    <button class="mcq-option" data-correct="true" data-explanation="Ones: 8 + 4 = 12, write 2 and carry 1. Tens: 4 + 3 + 1 = 8. Answer: 82">82</button>
    <button class="mcq-option" data-correct="false">92</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    }
]
