TITLE = "Comparing and Ordering Decimals"

SECTIONS = [
    {
        "title": "Comparing Decimals: The Strategy",
        "body": """
<h4>Step 1: Look at the Tenths Place First</h4>

<p>Just like comparing whole numbers, we compare decimals from left to right. Start with the tenths place.</p>

<div class="worked-example">
  <p><strong>Compare 0.7 and 0.4:</strong></p>
  <p>Look at tenths: 7 > 4</p>
  <p>So <strong>0.7 > 0.4</strong> (0.7 is bigger)</p>
</div>

<div class="worked-example">
  <p><strong>Compare 0.5 and 0.9:</strong></p>
  <p>Look at tenths: 5 < 9</p>
  <p>So <strong>0.5 < 0.9</strong> (0.5 is smaller)</p>
</div>

<h4>Step 2: If Tenths Are the Same, Look at Hundredths</h4>

<div class="worked-example">
  <p><strong>Compare 0.34 and 0.38:</strong></p>
  <p>Look at tenths: 3 = 3 (same, so look next)</p>
  <p>Look at hundredths: 4 < 8</p>
  <p>So <strong>0.34 < 0.38</strong></p>
</div>

<svg viewBox="0 0 500 230" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="470" height="200" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="250" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Comparing on a Number Line</text>

  <!-- Line 1: 0 to 1, showing 0.4 and 0.7 -->
  <line x1="40" y1="68" x2="460" y2="68" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="40" y1="58" x2="40" y2="78" stroke="#4f8ef7" stroke-width="2"/>
  <text x="40" y="95" text-anchor="middle" fill="currentColor" font-size="10" font-family="system-ui, sans-serif">0</text>
  <line x1="460" y1="58" x2="460" y2="78" stroke="#4f8ef7" stroke-width="2"/>
  <text x="460" y="95" text-anchor="middle" fill="currentColor" font-size="10" font-family="system-ui, sans-serif">1</text>

  <circle cx="208" cy="68" r="5" fill="#22c55e"/>
  <text x="208" y="95" text-anchor="middle" fill="#22c55e" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.4</text>

  <circle cx="334" cy="68" r="5" fill="#ef4444"/>
  <text x="334" y="95" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.7</text>

  <text x="250" y="115" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">0.7 is to the RIGHT, so 0.7 > 0.4</text>

  <!-- Line 2: 0.3 to 0.4, showing 0.34 and 0.38 -->
  <line x1="40" y1="145" x2="460" y2="145" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="40" y1="135" x2="40" y2="155" stroke="#4f8ef7" stroke-width="2"/>
  <text x="40" y="172" text-anchor="middle" fill="currentColor" font-size="10" font-family="system-ui, sans-serif">0.3</text>
  <line x1="460" y1="135" x2="460" y2="155" stroke="#4f8ef7" stroke-width="2"/>
  <text x="460" y="172" text-anchor="middle" fill="currentColor" font-size="10" font-family="system-ui, sans-serif">0.4</text>

  <circle cx="208" cy="145" r="5" fill="#22c55e"/>
  <text x="208" y="172" text-anchor="middle" fill="#22c55e" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.34</text>

  <circle cx="376" cy="145" r="5" fill="#ef4444"/>
  <text x="376" y="172" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.38</text>

  <text x="250" y="200" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">0.38 is to the RIGHT, so 0.38 > 0.34</text>
</svg>

<div class="mcq-group">
  <p><strong>Which is bigger: 0.6 or 0.42?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Compare tenths: 6 > 4, so 0.6 > 0.42. (We don't need to look at hundredths.)">0.6</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Compare tenths first: 6 > 4, so 0.6 is bigger. The fact that 42 is written doesn't matter.">0.42</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "The Common Mistake: Counting Digits",
        "body": """
<h4>WRONG: Thinking 0.1 < 0.09 Because 1 < 09</h4>

<p>This is a very common mistake! Don't count how many digits there are. Compare place values instead.</p>

<div class="warning-box">
  <p><strong>WRONG:</strong> "0.09 looks bigger than 0.1 because 09 has two digits."</p>
  <p><strong>CORRECT:</strong> Compare tenths: 0.1 has 1 tenth, 0.09 has 0 tenths. So 0.1 > 0.09.</p>
</div>

<h4>Why This Happens</h4>

<p>With whole numbers, 09 < 1, so our brain wants to think that 0.09 < 0.1. But decimals are different!</p>

<svg viewBox="0 0 500 280" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="470" height="250" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="250" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Visual Comparison: 0.1 vs 0.09</text>

  <!-- Grid for 0.1: 10x10, 10 squares shaded (first column) -->
  <text x="120" y="58" text-anchor="middle" fill="#4f8ef7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">0.1 (one tenth)</text>

  <!-- 10x10 grid outline -->
  <rect x="45" y="68" width="150" height="150" fill="none" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <!-- Shaded: first column = 10 squares -->
  <g fill="#4f8ef7" opacity="0.35">
    <rect x="45" y="68" width="15" height="15"/>
    <rect x="45" y="83" width="15" height="15"/>
    <rect x="45" y="98" width="15" height="15"/>
    <rect x="45" y="113" width="15" height="15"/>
    <rect x="45" y="128" width="15" height="15"/>
    <rect x="45" y="143" width="15" height="15"/>
    <rect x="45" y="158" width="15" height="15"/>
    <rect x="45" y="173" width="15" height="15"/>
    <rect x="45" y="188" width="15" height="15"/>
    <rect x="45" y="203" width="15" height="15"/>
  </g>
  <!-- Grid lines -->
  <g stroke="#8b949e" stroke-width="0.4">
    <line x1="60" y1="68" x2="60" y2="218"/>
    <line x1="75" y1="68" x2="75" y2="218"/>
    <line x1="90" y1="68" x2="90" y2="218"/>
    <line x1="105" y1="68" x2="105" y2="218"/>
    <line x1="120" y1="68" x2="120" y2="218"/>
    <line x1="135" y1="68" x2="135" y2="218"/>
    <line x1="150" y1="68" x2="150" y2="218"/>
    <line x1="165" y1="68" x2="165" y2="218"/>
    <line x1="180" y1="68" x2="180" y2="218"/>
    <line x1="45" y1="83" x2="195" y2="83"/>
    <line x1="45" y1="98" x2="195" y2="98"/>
    <line x1="45" y1="113" x2="195" y2="113"/>
    <line x1="45" y1="128" x2="195" y2="128"/>
    <line x1="45" y1="143" x2="195" y2="143"/>
    <line x1="45" y1="158" x2="195" y2="158"/>
    <line x1="45" y1="173" x2="195" y2="173"/>
    <line x1="45" y1="188" x2="195" y2="188"/>
    <line x1="45" y1="203" x2="195" y2="203"/>
  </g>
  <text x="120" y="237" text-anchor="middle" fill="#4f8ef7" font-size="10" font-family="system-ui, sans-serif">10 out of 100 squares</text>

  <!-- Grid for 0.09: 10x10, 9 squares shaded -->
  <text x="380" y="58" text-anchor="middle" fill="#f59e0b" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">0.09 (nine hundredths)</text>

  <rect x="305" y="68" width="150" height="150" fill="none" stroke="#f59e0b" stroke-width="2" rx="4"/>
  <!-- Shaded: 9 squares (first column minus last) -->
  <g fill="#f59e0b" opacity="0.35">
    <rect x="305" y="68" width="15" height="15"/>
    <rect x="305" y="83" width="15" height="15"/>
    <rect x="305" y="98" width="15" height="15"/>
    <rect x="305" y="113" width="15" height="15"/>
    <rect x="305" y="128" width="15" height="15"/>
    <rect x="305" y="143" width="15" height="15"/>
    <rect x="305" y="158" width="15" height="15"/>
    <rect x="305" y="173" width="15" height="15"/>
    <rect x="305" y="188" width="15" height="15"/>
  </g>
  <!-- Grid lines -->
  <g stroke="#8b949e" stroke-width="0.4">
    <line x1="320" y1="68" x2="320" y2="218"/>
    <line x1="335" y1="68" x2="335" y2="218"/>
    <line x1="350" y1="68" x2="350" y2="218"/>
    <line x1="365" y1="68" x2="365" y2="218"/>
    <line x1="380" y1="68" x2="380" y2="218"/>
    <line x1="395" y1="68" x2="395" y2="218"/>
    <line x1="410" y1="68" x2="410" y2="218"/>
    <line x1="425" y1="68" x2="425" y2="218"/>
    <line x1="440" y1="68" x2="440" y2="218"/>
    <line x1="305" y1="83" x2="455" y2="83"/>
    <line x1="305" y1="98" x2="455" y2="98"/>
    <line x1="305" y1="113" x2="455" y2="113"/>
    <line x1="305" y1="128" x2="455" y2="128"/>
    <line x1="305" y1="143" x2="455" y2="143"/>
    <line x1="305" y1="158" x2="455" y2="158"/>
    <line x1="305" y1="173" x2="455" y2="173"/>
    <line x1="305" y1="188" x2="455" y2="188"/>
    <line x1="305" y1="203" x2="455" y2="203"/>
  </g>
  <text x="380" y="237" text-anchor="middle" fill="#f59e0b" font-size="10" font-family="system-ui, sans-serif">9 out of 100 squares</text>

  <text x="250" y="258" text-anchor="middle" fill="#22c55e" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">0.1 has MORE shaded, so 0.1 > 0.09</text>
</svg>

<h4>The Rule: Add Zeros to Compare</h4>

<p>A helpful strategy is to add zeros so both decimals have the same number of decimal places:</p>

<div class="worked-example">
  <p><strong>Compare 0.1 and 0.09:</strong></p>
  <p>Rewrite as: 0.10 and 0.09</p>
  <p>Now compare: 0.10 > 0.09</p>
</div>

<div class="mcq-group">
  <p><strong>Which is bigger: 0.5 or 0.05?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 0.5 = 0.50, which is 50 hundredths. 0.05 is only 5 hundredths. So 0.5 > 0.05.">0.5</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Rewrite as 0.50 vs 0.05. Now it's clear: 50 > 5, so 0.5 > 0.05.">0.05</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Ordering Multiple Decimals",
        "body": """
<h4>Strategy: Rewrite with Same Decimal Places</h4>

<p>When you need to put multiple decimals in order, first write them all with the same number of decimal places. Then compare!</p>

<div class="worked-example">
  <p><strong>Order from smallest to largest: 0.6, 0.06, 0.66, 0.606</strong></p>

  <p><strong>Step 1:</strong> Rewrite with same decimal places (3 places)</p>
  <p>0.600, 0.060, 0.660, 0.606</p>

  <p><strong>Step 2:</strong> Compare digit by digit</p>
  <ul>
    <li>0.060 has only 0 tenths (smallest)</li>
    <li>0.600, 0.606, 0.660 all have 6 tenths</li>
  </ul>

  <p><strong>Step 3:</strong> For the ones starting with 6, look at hundredths</p>
  <ul>
    <li>0.600 has 0 hundredths (comes first)</li>
    <li>0.606 has 0 hundredths (but 6 thousandths)</li>
    <li>0.660 has 6 hundredths (comes last)</li>
  </ul>

  <p><strong>Answer: 0.06, 0.6, 0.606, 0.66</strong></p>
</div>

<h4>Another Example</h4>

<div class="worked-example">
  <p><strong>Order from smallest to largest: 0.45, 0.54, 0.4, 0.5</strong></p>

  <p><strong>Step 1:</strong> Rewrite with same decimal places</p>
  <p>0.45, 0.54, 0.40, 0.50</p>

  <p><strong>Step 2:</strong> Compare</p>
  <p>0.40 < 0.45 < 0.50 < 0.54</p>

  <p><strong>Answer: 0.4, 0.45, 0.5, 0.54</strong></p>
</div>

<svg viewBox="0 0 500 175" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="470" height="145" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="250" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Number Line: Ordering Example</text>

  <!-- Number line from 0.4 to 0.6 -->
  <line x1="40" y1="70" x2="460" y2="70" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Endpoints -->
  <line x1="40" y1="60" x2="40" y2="80" stroke="#4f8ef7" stroke-width="2"/>
  <text x="40" y="98" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">0.4</text>

  <line x1="460" y1="60" x2="460" y2="80" stroke="#4f8ef7" stroke-width="2"/>
  <text x="460" y="98" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">0.6</text>

  <!-- 0.45 at 1/4 of the way -->
  <circle cx="145" cy="70" r="5" fill="#22c55e"/>
  <text x="145" y="98" text-anchor="middle" fill="#22c55e" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.45</text>

  <!-- 0.5 at midpoint -->
  <circle cx="250" cy="70" r="5" fill="#4f8ef7"/>
  <text x="250" y="98" text-anchor="middle" fill="#4f8ef7" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.5</text>

  <!-- 0.54 at about 2/3 -->
  <circle cx="334" cy="70" r="5" fill="#f59e0b"/>
  <text x="334" y="98" text-anchor="middle" fill="#f59e0b" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">0.54</text>

  <text x="250" y="128" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">Left to right = smallest to largest</text>
  <text x="250" y="148" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.4  -->  0.45  -->  0.5  -->  0.54</text>
</svg>
        """
    },
    {
        "title": "Using Symbols: <, >, =",
        "body": """
<h4>Comparison Symbols</h4>

<div class="concept-box">
  <p><strong>&lt;</strong> means "less than" (the small end points to the smaller number)</p>
  <p><strong>&gt;</strong> means "greater than" (the wide end opens to the bigger number)</p>
  <p><strong>=</strong> means "equal to"</p>
</div>

<h4>Remember: The Symbol Points to the Smaller Number</h4>

<svg viewBox="0 0 420 130" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="390" height="100" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="210" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Using Comparison Symbols</text>

  <!-- Row 1 -->
  <text x="80" y="68" text-anchor="middle" fill="currentColor" font-size="16" font-family="system-ui, sans-serif">0.3</text>
  <text x="120" y="68" text-anchor="middle" fill="#22c55e" font-size="22" font-weight="bold" font-family="system-ui, sans-serif">&lt;</text>
  <text x="160" y="68" text-anchor="middle" fill="currentColor" font-size="16" font-family="system-ui, sans-serif">0.7</text>
  <text x="300" y="68" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">(points to 0.3, the smaller)</text>

  <!-- Row 2 -->
  <text x="80" y="100" text-anchor="middle" fill="currentColor" font-size="16" font-family="system-ui, sans-serif">0.9</text>
  <text x="120" y="100" text-anchor="middle" fill="#ef4444" font-size="22" font-weight="bold" font-family="system-ui, sans-serif">&gt;</text>
  <text x="160" y="100" text-anchor="middle" fill="currentColor" font-size="16" font-family="system-ui, sans-serif">0.5</text>
  <text x="300" y="100" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">(points to 0.5, the smaller)</text>
</svg>

<div class="mcq-group">
  <p><strong>Which symbol is correct? 0.32 ___ 0.31</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Both have 3 tenths. Compare hundredths: 2 > 1. So 0.32 > 0.31">></button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 32 hundredths is more than 31 hundredths, so the > symbol is correct."><</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 0.32 is not equal to 0.31.">= </button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Practice: Mixed Comparisons",
        "body": """
<h4>Test Your Skills</h4>

<div class="mcq-group">
  <p><strong>Order from smallest to largest: 0.7, 0.07, 0.77</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 0.07 = 7 hundredths, 0.7 = 70 hundredths, 0.77 = 77 hundredths. So 0.07 < 0.7 < 0.77">0.07, 0.7, 0.77</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. Check your place values again: 0.07 has fewer tenths than the others.">0.7, 0.77, 0.07</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 0.07 should be first because it's the smallest.">0.77, 0.7, 0.07</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>Which is biggest: 0.62, 0.26, 0.206?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Compare tenths: 0.62 has 6 tenths (more than 0.26 which has 2 tenths). So 0.62 is biggest.">0.62</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 0.62 has more tenths than 0.26.">0.26</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. 0.206 has only 2 tenths, while 0.62 has 6 tenths.">0.206</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    }
]
