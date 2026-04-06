TITLE = "Decimals and Fractions"

SECTIONS = [
    {
        "title": "Converting Decimals to Fractions",
        "body": """
<h4>The Simple Rule</h4>

<p>The number of decimal places tells you the denominator:</p>

<div class="concept-box">
  <p><strong>1 decimal place</strong> --> denominator is <strong>10</strong></p>
  <p><strong>2 decimal places</strong> --> denominator is <strong>100</strong></p>
  <p><strong>3 decimal places</strong> --> denominator is <strong>1000</strong></p>
</div>

<h4>Examples</h4>

<div class="worked-example">
  <p><strong>Convert 0.3 to a fraction:</strong></p>
  <ul>
    <li>One decimal place --> denominator 10</li>
    <li>Numerator is 3</li>
    <li>Answer: 3/10</li>
  </ul>
</div>

<div class="worked-example">
  <p><strong>Convert 0.25 to a fraction:</strong></p>
  <ul>
    <li>Two decimal places --> denominator 100</li>
    <li>Numerator is 25</li>
    <li>Answer: 25/100</li>
    <li>Simplified: 1/4 (divide top and bottom by 25)</li>
  </ul>
</div>

<div class="worked-example">
  <p><strong>Convert 0.456 to a fraction:</strong></p>
  <ul>
    <li>Three decimal places --> denominator 1000</li>
    <li>Numerator is 456</li>
    <li>Answer: 456/1000</li>
  </ul>
</div>

<svg viewBox="0 0 420 280" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="390" height="250" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="210" y="40" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Decimal to Fraction Examples</text>

  <!-- Column headers -->
  <text x="100" y="68" text-anchor="middle" fill="#4f8ef7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Decimal</text>
  <text x="210" y="68" text-anchor="middle" fill="#f59e0b" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Fraction</text>
  <text x="330" y="68" text-anchor="middle" fill="#22c55e" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Simplified</text>

  <line x1="35" y1="78" x2="385" y2="78" stroke="#334155" stroke-width="1"/>

  <!-- Row 1 -->
  <text x="100" y="100" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.5</text>
  <text x="210" y="100" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">5/10</text>
  <text x="330" y="100" text-anchor="middle" fill="#22c55e" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">1/2</text>

  <!-- Row 2 -->
  <text x="100" y="130" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.25</text>
  <text x="210" y="130" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">25/100</text>
  <text x="330" y="130" text-anchor="middle" fill="#22c55e" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">1/4</text>

  <!-- Row 3 -->
  <text x="100" y="160" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.75</text>
  <text x="210" y="160" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">75/100</text>
  <text x="330" y="160" text-anchor="middle" fill="#22c55e" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">3/4</text>

  <!-- Row 4 -->
  <text x="100" y="190" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.1</text>
  <text x="210" y="190" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">1/10</text>
  <text x="330" y="190" text-anchor="middle" fill="currentColor" opacity="0.5" font-size="11" font-family="system-ui, sans-serif">already simple</text>

  <!-- Row 5 -->
  <text x="100" y="220" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.01</text>
  <text x="210" y="220" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">1/100</text>
  <text x="330" y="220" text-anchor="middle" fill="currentColor" opacity="0.5" font-size="11" font-family="system-ui, sans-serif">already simple</text>

  <!-- Row 6 -->
  <text x="100" y="250" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.001</text>
  <text x="210" y="250" text-anchor="middle" fill="currentColor" font-size="13" font-family="system-ui, sans-serif">1/1000</text>
  <text x="330" y="250" text-anchor="middle" fill="currentColor" opacity="0.5" font-size="11" font-family="system-ui, sans-serif">already simple</text>
</svg>

<div class="mcq-group">
  <p><strong>Convert 0.7 to a fraction.</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! One decimal place means denominator 10. So 0.7 = 7/10.">7/10</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. One decimal place means the denominator is 10, not 100. That would be 0.07.">7/100</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. The denominator depends on decimal places, not the value of the digit.">7/7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Converting Fractions to Decimals",
        "body": """
<h4>The Method: Divide</h4>

<p>To convert a fraction to a decimal, divide the numerator by the denominator.</p>

<div class="concept-box">
  <p>numerator / denominator = decimal</p>
</div>

<h4>Examples</h4>

<div class="worked-example">
  <p><strong>Convert 1/4 to a decimal:</strong></p>
  <ul>
    <li>Divide: 1 / 4 = 0.25</li>
    <li>Answer: 1/4 = 0.25</li>
  </ul>
</div>

<div class="worked-example">
  <p><strong>Convert 3/5 to a decimal:</strong></p>
  <ul>
    <li>Divide: 3 / 5 = 0.6</li>
    <li>Answer: 3/5 = 0.6</li>
  </ul>
</div>

<div class="worked-example">
  <p><strong>Convert 7/8 to a decimal:</strong></p>
  <ul>
    <li>Divide: 7 / 8 = 0.875</li>
    <li>Answer: 7/8 = 0.875</li>
  </ul>
</div>

<div class="success-box">
  <p><strong>Tip:</strong> If the denominator is 10 or 100, you can use our place value shortcut instead of dividing. For example, 35/100 = 0.35 (just read the digits).</p>
</div>

<div class="mcq-group">
  <p><strong>Convert 1/2 to a decimal.</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 1 / 2 = 0.5. Or: 1/2 = 5/10 = 0.5">0.5</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 1 / 2 = 0.5, not 0.2.">0.2</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 1/2 is smaller than 1, so the decimal should be less than 1.">1.2</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Common Decimal-Fraction Pairs to Know",
        "body": """
<h4>These Are Super Useful!</h4>

<p>Memorize these common conversions. You'll see them over and over:</p>

<svg viewBox="0 0 420 400" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="390" height="370" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="210" y="40" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Common Decimal-Fraction Pairs</text>

  <!-- Halves -->
  <text x="40" y="70" fill="#4f8ef7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Halves:</text>
  <text x="60" y="90" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">1/2 = 0.5</text>

  <line x1="35" y1="102" x2="385" y2="102" stroke="#334155" stroke-width="0.5"/>

  <!-- Quarters -->
  <text x="40" y="122" fill="#22c55e" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Quarters:</text>
  <text x="60" y="142" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">1/4 = 0.25</text>
  <text x="230" y="142" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">2/4 = 0.5</text>
  <text x="60" y="162" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">3/4 = 0.75</text>

  <line x1="35" y1="174" x2="385" y2="174" stroke="#334155" stroke-width="0.5"/>

  <!-- Fifths -->
  <text x="40" y="194" fill="#f59e0b" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Fifths:</text>
  <text x="60" y="214" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">1/5 = 0.2</text>
  <text x="230" y="214" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">2/5 = 0.4</text>
  <text x="60" y="234" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">3/5 = 0.6</text>
  <text x="230" y="234" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">4/5 = 0.8</text>

  <line x1="35" y1="246" x2="385" y2="246" stroke="#334155" stroke-width="0.5"/>

  <!-- Tenths -->
  <text x="40" y="266" fill="#ec4899" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Tenths:</text>
  <text x="60" y="286" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">1/10 = 0.1</text>
  <text x="230" y="286" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">3/10 = 0.3</text>
  <text x="60" y="306" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">5/10 = 0.5</text>
  <text x="230" y="306" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">9/10 = 0.9</text>

  <line x1="35" y1="318" x2="385" y2="318" stroke="#334155" stroke-width="0.5"/>

  <!-- Eighths -->
  <text x="40" y="338" fill="#8b5cf6" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">Eighths:</text>
  <text x="60" y="358" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">1/8 = 0.125</text>
  <text x="230" y="358" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">3/8 = 0.375</text>
  <text x="60" y="378" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">5/8 = 0.625</text>
  <text x="230" y="378" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">7/8 = 0.875</text>
</svg>

<div class="success-box">
  <p><strong>Memory Trick:</strong> Notice that halves, quarters, and fifths all equal 0.something with 1 or 2 decimal places. Memorize the main ones and you'll recognize the patterns!</p>
</div>
        """
    },
    {
        "title": "Choosing: Fraction or Decimal?",
        "body": """
<h4>When Do We Use Each?</h4>

<p>Both fractions and decimals are useful. Here's when you might use each:</p>

<div class="concept-box">
  <p><strong>Use Decimals When:</strong></p>
  <ul>
    <li>You're dealing with money ($2.50)</li>
    <li>You're measuring length (1.5 metres)</li>
    <li>You're doing calculations (easier to add 2.3 + 1.7)</li>
    <li>The number comes from scientific instruments</li>
  </ul>

  <p><strong>Use Fractions When:</strong></p>
  <ul>
    <li>You're describing parts of something (half, quarter, third)</li>
    <li>The exact mathematical relationship matters (1/3 is more precise than 0.333...)</li>
    <li>You're comparing sizes (which is bigger: 2/3 or 3/4?)</li>
  </ul>
</div>

<h4>Equivalence: Same Value, Different Forms</h4>

<p>The important thing to remember: a fraction and decimal can be the same value, just written differently.</p>

<svg viewBox="0 0 420 165" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="390" height="135" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="210" y="40" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Three Ways to Write the Same Amount</text>

  <!-- Three boxes side by side -->
  <rect x="35" y="58" width="110" height="50" fill="#0f172a" stroke="#4f8ef7" stroke-width="1.5" rx="4"/>
  <text x="90" y="76" text-anchor="middle" fill="#4f8ef7" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Fraction</text>
  <text x="90" y="98" text-anchor="middle" fill="currentColor" font-size="16" font-weight="bold" font-family="system-ui, sans-serif">1/2</text>

  <rect x="160" y="58" width="110" height="50" fill="#0f172a" stroke="#22c55e" stroke-width="1.5" rx="4"/>
  <text x="215" y="76" text-anchor="middle" fill="#22c55e" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Decimal</text>
  <text x="215" y="98" text-anchor="middle" fill="currentColor" font-size="16" font-weight="bold" font-family="system-ui, sans-serif">0.5</text>

  <rect x="285" y="58" width="110" height="50" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="340" y="76" text-anchor="middle" fill="#f59e0b" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Percent</text>
  <text x="340" y="98" text-anchor="middle" fill="currentColor" font-size="16" font-weight="bold" font-family="system-ui, sans-serif">50%</text>

  <text x="210" y="135" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="11" font-style="italic" font-family="system-ui, sans-serif">All three represent the same amount!</text>
</svg>

<div class="mcq-group">
  <p><strong>Which would you most likely use for measuring the height of a person?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Measurements typically use decimals, like 1.75 metres or 5.83 feet.">Decimal (like 1.75 m)</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not typically. We could write it as a fraction, but decimals are more standard for measurements.">Fraction (like 1 and 3/4 m)</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Practice: Converting Both Ways",
        "body": """
<h4>Test Your Conversion Skills</h4>

<div class="mcq-group">
  <p><strong>Convert 0.6 to a fraction.</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! One decimal place means denominator 10. 0.6 = 6/10 = 3/5 (simplified).">6/10 or 3/5</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. One decimal place means denominator 10, not 100.">60/100</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. The decimal 0.6 means 6 in the tenths place.">6/6</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>Convert 3/4 to a decimal.</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 3 / 4 = 0.75.">0.75</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Divide: 3 / 4 = 0.75.">0.34</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 3/4 is less than 1, so the decimal should be less than 1.">1.75</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>Which is bigger: 0.3 or 1/4?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 1/4 = 0.25, and 0.3 > 0.25.">0.3</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Convert 1/4 to a decimal: 1/4 = 0.25. Now compare: 0.3 > 0.25.">1/4</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>A recipe calls for 0.75 cups of flour. How do you write this as a fraction?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 0.75 = 75/100 = 3/4 (simplified).">3/4 cups</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Two decimal places means denominator 100: 0.75 = 75/100 = 3/4.">7/5 cups</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 0.75 is not equal to 3/5. Remember: 3/5 = 0.6.">3/5 cups</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    }
]
