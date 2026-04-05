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

<svg viewBox="0 0 500 220" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Comparing on a Number Line</text>

  <!-- Line 1: 0.7 vs 0.4 -->
  <line x1="30" y1="50" x2="470" y2="50" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="30" y1="40" x2="30" y2="60" stroke='#4f8ef7' stroke-width="2"/>
  <circle cx="210" cy="50" r="5" fill='#22c55e'/>
  <text x="210" y="75" text-anchor='middle' fill='#22c55e' font-size='11'>0.4</text>
  <circle cx="350" cy="50" r="5" fill='#ef4444'/>
  <text x="350" y="75" text-anchor='middle' fill='#ef4444' font-size='11'>0.7</text>
  <line x1="470" y1="40" x2="470" y2="60" stroke='#4f8ef7' stroke-width="2"/>
  <text x="250" y="110" text-anchor='middle' fill='currentColor' font-size='11'>0.7 is to the RIGHT, so 0.7 > 0.4</text>

  <!-- Line 2: 0.34 vs 0.38 -->
  <line x1="30" y1="140" x2="470" y2="140" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="30" y1="130" x2="30" y2="150" stroke='#4f8ef7' stroke-width="2"/>
  <circle cx="250" cy="140" r="5" fill='#22c55e'/>
  <text x="250" y="165" text-anchor='middle' fill='#22c55e' font-size='11'>0.34</text>
  <circle cx="300" cy="140" r="5" fill='#ef4444'/>
  <text x="300" y="165" text-anchor='middle' fill='#ef4444' font-size='11'>0.38</text>
  <line x1="470" y1="130" x2="470" y2="150" stroke='#4f8ef7' stroke-width="2"/>
  <text x="250" y="200" text-anchor='middle' fill='currentColor' font-size='11'>0.38 is to the RIGHT, so 0.38 > 0.34</text>
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
  <p><strong>❌ WRONG:</strong> "0.09 looks bigger than 0.1 because 09 has two digits."</p>
  <p><strong>✓ CORRECT:</strong> Compare tenths: 0.1 has 1 tenth, 0.09 has 0 tenths. So 0.1 > 0.09.</p>
</div>

<h4>Why This Happens</h4>

<p>With whole numbers, 09 < 1, so our brain wants to think that 0.09 < 0.1. But decimals are different!</p>

<svg viewBox="0 0 500 280" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Visual Comparison: 0.1 vs 0.09</text>

  <!-- Grid for 0.1 -->
  <text x="120" y="50" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>0.1 (one tenth)</text>
  <rect x="40" y="70" width="160" height="160" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <rect x="40" y="70" width="160" height="160" fill='#4f8ef7' opacity='0.3'/>
  <text x="120" y="210" text-anchor='middle' fill='#4f8ef7' font-size='11'>10 out of 100 squares</text>

  <!-- Grid for 0.09 -->
  <text x="380" y="50" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>0.09 (nine hundredths)</text>
  <rect x="300" y="70" width="160" height="160" fill='none' stroke='#f59e0b' stroke-width="2"/>
  <g fill='#f59e0b' opacity='0.3'>
    <rect x="300" y="70" width="32" height="32"/>
    <rect x="332" y="70" width="32" height="32"/>
    <rect x="364" y="70" width="32" height="32"/>
    <rect x="396" y="70" width="32" height="32"/>
    <rect x="428" y="70" width="32" height="32"/>
    <rect x="300" y="102" width="32" height="32"/>
    <rect x="332" y="102" width="32" height="32"/>
    <rect x="364" y="102" width="32" height="32"/>
    <rect x="396" y="102" width="32" height="32"/>
  </g>
  <text x="380" y="210" text-anchor='middle' fill='#f59e0b' font-size='11'>9 out of 100 squares</text>

  <text x="250" y="250" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>0.1 has MORE shaded, so 0.1 > 0.09</text>
</svg>

<h4>The Rule: Add Zeros to Compare</h4>

<p>A helpful strategy is to add zeros so both decimals have the same number of decimal places:</p>

<div class="worked-example">
  <p><strong>Compare 0.1 and 0.09:</strong></p>
  <p>Rewrite as: 0.10 and 0.09</p>
  <p>Now compare: 0.10 > 0.09 ✓</p>
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
    <li>0.060 → only 0 tenths ✗</li>
    <li>0.600 → 6 tenths ✓</li>
    <li>0.606 → 6 tenths ✓</li>
    <li>0.660 → 6 tenths ✓</li>
  </ul>

  <p><strong>Step 3:</strong> For the ones starting with 6, look at hundredths</p>
  <ul>
    <li>0.600 → 0 hundredths (comes first)</li>
    <li>0.606 → 0 hundredths (but 6 thousandths > 0)</li>
    <li>0.660 → 6 hundredths (comes last)</li>
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

<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Number Line: Ordering Example</text>

  <line x1="30" y1="60" x2="470" y2="60" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="30" y1="50" x2="30" y2="70" stroke='#4f8ef7' stroke-width="2"/>
  <text x="30" y="90" text-anchor='middle' fill='currentColor' font-size='11'>0.4</text>

  <circle cx="120" cy="60" r="4" fill='#22c55e'/>
  <text x="120" y="90" text-anchor='middle' fill='#22c55e' font-size='11'>0.45</text>

  <circle cx="180" cy="60" r="4" fill='#4f8ef7'/>
  <text x="180" y="90" text-anchor='middle' fill='#4f8ef7' font-size='11'>0.5</text>

  <circle cx="280" cy="60" r="4" fill='#f59e0b'/>
  <text x="280" y="90" text-anchor='middle' fill='#f59e0b' font-size='11'>0.54</text>

  <line x1="470" y1="50" x2="470" y2="70" stroke='#4f8ef7' stroke-width="2"/>
  <text x="470" y="90" text-anchor='middle' fill='currentColor' font-size='11'>0.6</text>

  <text x="250" y="140" text-anchor='middle' fill='currentColor' font-size='11'>Left to right = smallest to largest</text>
  <text x="250" y="160" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.4 → 0.45 → 0.5 → 0.54</text>
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

<svg viewBox="0 0 500 120" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Using Comparison Symbols</text>

  <text x="100" y="50" text-anchor='end' fill='currentColor' font-size='14'>0.3</text>
  <text x="130" y="50" text-anchor='middle' fill='#22c55e' font-size='20' font-weight='bold'>&lt;</text>
  <text x="160" y="50" text-anchor='start' fill='currentColor' font-size='14'>0.7</text>
  <text x="250" y="55" fill='currentColor' opacity='0.6' font-size='10'>(symbol points to 0.3, the smaller number)</text>

  <text x="100" y="90" text-anchor='end' fill='currentColor' font-size='14'>0.9</text>
  <text x="130" y="90" text-anchor='middle' fill='#ef4444' font-size='20' font-weight='bold'>&gt;</text>
  <text x="160" y="90" text-anchor='start' fill='currentColor' font-size='14'>0.5</text>
  <text x="250" y="95" fill='currentColor' opacity='0.6' font-size='10'>(symbol points to 0.5, the smaller number)</text>
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
