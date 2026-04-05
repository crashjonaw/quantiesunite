TITLE = "Adding and Subtracting Decimals"

SECTIONS = [
    {
        "title": "The Golden Rule: Line Up the Decimal Points",
        "body": """
<h4>Most Important Rule for Adding/Subtracting Decimals</h4>

<div class="warning-box">
  <p><strong>⭐ The decimal points MUST be directly above each other.</strong></p>
  <p>This ensures that tenths add to tenths, hundredths add to hundredths, and ones add to ones.</p>
</div>

<h4>Example: 2.5 + 1.3</h4>

<div class="worked-example">
  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;<span class="accent-heading">2</span><span style="color: #ef4444;">.</span><span style="color: var(--success);">5</span><br>
    <span class="text-muted-note">+</span> <span class="accent-heading">1</span><span style="color: #ef4444;">.</span><span style="color: var(--success);">3</span><br>
    <span class="text-muted-note">-----</span><br>
    &nbsp;&nbsp;&nbsp;<span class="accent-heading">3</span><span style="color: #ef4444;">.</span><span style="color: var(--success);">8</span>
  </p>

  <p><strong>What we're adding:</strong></p>
  <ul>
    <li>Ones: 2 + 1 = 3</li>
    <li>Tenths: 5 + 3 = 8</li>
  </ul>

  <p><strong>Answer: 3.8</strong></p>
</div>

<svg viewBox="0 0 500 180" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='#e6edf3' font-size='14' font-weight='bold'>Why Lining Up Matters</text>

  <!-- Wrong way -->
  <rect x="20" y="35" width="200" height="50" fill='#1e293b' stroke='#ef4444' stroke-width="2" rx="2"/>
  <text x="30" y="52" fill='#ef4444' font-size='11' font-weight='bold'>❌ WRONG</text>
  <text x="30" y="72" fill='#e6edf3' font-size='13' font-family='monospace'>2.5 + 1.3 = 28</text>
  <text x="120" y="92" fill='#ef4444' font-size='10'>(5+3=8 is correct, but</text>
  <text x="120" y="105" fill='#ef4444' font-size='10'>mixing up places!)</text>

  <!-- Right way -->
  <rect x="280" y="35" width="200" height="50" fill='#1e293b' stroke='#22c55e' stroke-width="2" rx="2"/>
  <text x="290" y="52" fill='#22c55e' font-size='11' font-weight='bold'>✓ CORRECT</text>
  <text x="290" y="72" fill='#e6edf3' font-size='13' font-family='monospace'>2.5 + 1.3 = 3.8</text>
  <text x="380" y="92" fill='#22c55e' font-size='10'>(decimal points</text>
  <text x="380" y="105" fill='#22c55e' font-size='10'>lined up!)</text>
</svg>
        """
    },
    {
        "title": "Adding Decimals with Different Lengths",
        "body": """
<h4>Strategy: Add Zeros to Make Them Equal</h4>

<p>When decimals have different numbers of decimal places, add zeros to the right so they match.</p>

<div class="worked-example">
  <p><strong>Example: 3.2 + 1.45</strong></p>

  <p><strong>Step 1:</strong> Rewrite to have the same decimal places</p>
  <p style="text-align: center; font-family: monospace; font-size: 13px;">
    3.2 becomes <strong>3.20</strong>
  </p>

  <p><strong>Step 2:</strong> Line up decimal points and add</p>
  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;3.20<br>
    <span class="text-muted-note">+</span> 1.45<br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;&nbsp;4.65
  </p>

  <p><strong>What we added:</strong></p>
  <ul>
    <li>Ones: 3 + 1 = 4</li>
    <li>Tenths: 2 + 4 = 6</li>
    <li>Hundredths: 0 + 5 = 5</li>
  </ul>

  <p><strong>Answer: 4.65</strong></p>
</div>

<div class="success-box">
  <p><strong>Tip:</strong> Adding a zero doesn't change the value of a decimal! 3.2 = 3.20. This helps us line up properly.</p>
</div>

<div class="mcq-group">
  <p><strong>What is 2.3 + 1.45?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Rewrite as 2.30 + 1.45. Line up decimals: 2.30 + 1.45 = 3.75">3.75</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Rewrite 2.3 as 2.30 so you can add properly: 2.30 + 1.45 = 3.75">3.68</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. The answer should have 2 decimal places: 3.75">3.7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Subtracting Decimals",
        "body": """
<h4>Same Rule: Line Up Decimal Points</h4>

<p>Subtraction works exactly like addition. The decimal points must be directly above each other.</p>

<div class="worked-example">
  <p><strong>Example: 5.74 - 2.31</strong></p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;5.74<br>
    <span class="text-muted-note">-</span> 2.31<br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;&nbsp;3.43
  </p>

  <p><strong>What we subtracted:</strong></p>
  <ul>
    <li>Ones: 5 - 2 = 3</li>
    <li>Tenths: 7 - 3 = 4</li>
    <li>Hundredths: 4 - 1 = 3</li>
  </ul>

  <p><strong>Answer: 3.43</strong></p>
</div>

<h4>Another Example with Different Lengths</h4>

<div class="worked-example">
  <p><strong>Example: 4.5 - 2.17</strong></p>

  <p><strong>Step 1:</strong> Rewrite with same decimal places</p>
  <p style="text-align: center; font-family: monospace; font-size: 13px;">
    4.5 becomes <strong>4.50</strong>
  </p>

  <p><strong>Step 2:</strong> Line up and subtract</p>
  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;4.50<br>
    <span class="text-muted-note">-</span> 2.17<br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;&nbsp;2.33
  </p>

  <p><strong>Answer: 2.33</strong></p>
</div>
        """
    },
    {
        "title": "Subtracting When You Need to Borrow (Regroup)",
        "body": """
<h4>What Happens When You Can't Subtract?</h4>

<p>Sometimes the digit you're subtracting from is too small. Then you need to <strong>borrow</strong> (or <strong>regroup</strong) from the next place to the left.</p>

<div class="worked-example">
  <p><strong>Example: 3.2 - 1.5</strong></p>

  <p>Can you do 2 - 5 in the tenths place? <strong>No!</strong> So borrow from the ones place.</p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;3.2<span class="text-muted-note">0</span><br>
    <span class="text-muted-note">-</span> 1.5<span class="text-muted-note">0</span><br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;1.70
  </p>

  <p><strong>What we did:</strong></p>
  <ul>
    <li>Can't do 2 - 5, so borrow 1 from the 3</li>
    <li>Now it's 12 tenths - 5 tenths = 7 tenths ✓</li>
    <li>Ones: 2 - 1 = 1</li>
  </ul>

  <p><strong>Answer: 1.7 (or 1.70)</strong></p>
</div>

<h4>Another Example</h4>

<div class="worked-example">
  <p><strong>Example: 5.3 - 2.8</strong></p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;5.3 becomes 4.13 (after borrowing)<br>
    <span class="text-muted-note">-</span> 2.8<br>
    <span class="text-muted-note">-------</span><br>
    &nbsp;&nbsp;2.5
  </p>

  <p><strong>Step by step:</strong></p>
  <ol>
    <li>Can't do 3 - 8 in tenths, so borrow from ones</li>
    <li>5 ones becomes 4 ones</li>
    <li>3 tenths becomes 13 tenths (10 + 3)</li>
    <li>Now: 13 - 8 = 5 tenths ✓</li>
    <li>Ones: 4 - 2 = 2 ✓</li>
  </ol>
</div>

<div class="mcq-group">
  <p><strong>What is 4.2 - 1.7?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Can't do 2-7, so borrow: 4.2 becomes 3.12. Then 12-7=5 tenths, 3-1=2 ones. Answer: 2.5">2.5</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. You need to borrow because you can't do 2 - 7 in the tenths place.">2.6</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Regroup from the ones place and try again.">3.5</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Real-World Practice: Money",
        "body": """
<h4>Money is Perfect for Decimal Practice</h4>

<p>Money uses decimals, so adding/subtracting money is great practice!</p>

<div class="worked-example">
  <p><strong>Example 1: You have $5.75. You spend $2.30. How much is left?</strong></p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;$5.75<br>
    <span class="text-muted-note">-</span> $2.30<br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;&nbsp;$3.45
  </p>

  <p><strong>Answer: $3.45 left</strong></p>
</div>

<div class="worked-example">
  <p><strong>Example 2: Item A costs $3.25. Item B costs $4.75. Total cost?</strong></p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;&nbsp;$3.25<br>
    <span class="text-muted-note">+</span> $4.75<br>
    <span class="text-muted-note">------</span><br>
    &nbsp;&nbsp;&nbsp;$8.00
  </p>

  <p><strong>Answer: $8.00 total</strong></p>
</div>

<div class="worked-example">
  <p><strong>Example 3: You have $10.00. You buy something for $6.45. Change?</strong></p>

  <p style="text-align: center; font-family: monospace; font-size: 14px;">
    &nbsp;&nbsp;$10.00<br>
    <span class="text-muted-note">-</span> &nbsp;$6.45<br>
    <span class="text-muted-note">--------</span><br>
    &nbsp;&nbsp;&nbsp;$3.55
  </p>

  <p><strong>Answer: $3.55 change</strong></p>
</div>

<div class="mcq-group">
  <p><strong>You have $7.50. You spend $3.25. How much do you have left?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 7.50 - 3.25 = 4.25">$4.25</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Line up the decimal points and subtract carefully: 7.50 - 3.25 = 4.25">$4.35</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. You should have about $4.25 left.">$4.15</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    }
]
