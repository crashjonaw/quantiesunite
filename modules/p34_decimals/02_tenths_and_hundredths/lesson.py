TITLE = "Tenths and Hundredths"

SECTIONS = [
    {
        "title": "Understanding Tenths",
        "body": """
<h4>Dividing into 10 Equal Parts</h4>

<p>A <strong>tenth</strong> is what you get when you divide something into 10 equal parts and take 1 part.</p>

<svg viewBox="0 0 520 175" style="width:100%;max-width:520px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="490" height="145" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="260" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">One Whole Divided Into 10 Tenths</text>

  <!-- Whole rectangle -->
  <rect x="35" y="55" width="450" height="50" fill="none" stroke="#4f8ef7" stroke-width="2" rx="4"/>

  <!-- 10 divisions: each cell is 45px wide -->
  <line x1="80" y1="55" x2="80" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="125" y1="55" x2="125" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="170" y1="55" x2="170" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="215" y1="55" x2="215" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="260" y1="55" x2="260" y2="105" stroke="#ef4444" stroke-width="2"/>
  <line x1="305" y1="55" x2="305" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="350" y1="55" x2="350" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="395" y1="55" x2="395" y2="105" stroke="#8b949e" stroke-width="1"/>
  <line x1="440" y1="55" x2="440" y2="105" stroke="#8b949e" stroke-width="1"/>

  <!-- Labels below each cell -->
  <text x="57" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.1</text>
  <text x="102" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.2</text>
  <text x="147" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.3</text>
  <text x="192" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.4</text>
  <text x="237" y="125" text-anchor="middle" fill="#ef4444" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">0.5</text>
  <text x="282" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.6</text>
  <text x="327" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.7</text>
  <text x="372" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.8</text>
  <text x="417" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">0.9</text>
  <text x="462" y="125" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">1.0</text>

  <!-- Explanation -->
  <text x="260" y="150" text-anchor="middle" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">Each part = 0.1 (one tenth = 1/10)</text>
</svg>

<div class="concept-box">
  <p>0.1 = 1/10 (one tenth)</p>
  <p>0.5 = 5/10 (five tenths)</p>
  <p>0.9 = 9/10 (nine tenths)</p>
</div>

<h4>Number Line: Tenths</h4>

<svg viewBox="0 0 520 120" style="width:100%;max-width:520px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="490" height="90" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="260" y="35" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Number Line: 0 to 1 in Tenths</text>

  <!-- Main line -->
  <line x1="40" y1="60" x2="490" y2="60" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Tick marks and labels: spacing = 45px each -->
  <line x1="40" y1="52" x2="40" y2="68" stroke="#4f8ef7" stroke-width="2"/>
  <text x="40" y="84" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">0</text>

  <line x1="85" y1="54" x2="85" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="85" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.1</text>

  <line x1="130" y1="54" x2="130" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="130" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.2</text>

  <line x1="175" y1="54" x2="175" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="175" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.3</text>

  <line x1="220" y1="54" x2="220" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="220" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.4</text>

  <line x1="265" y1="54" x2="265" y2="66" stroke="#ef4444" stroke-width="2"/>
  <text x="265" y="84" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="bold" font-family="system-ui, sans-serif">0.5</text>
  <circle cx="265" cy="60" r="5" fill="#ef4444" opacity="0.3"/>

  <line x1="310" y1="54" x2="310" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="310" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.6</text>

  <line x1="355" y1="54" x2="355" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="355" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.7</text>

  <line x1="400" y1="54" x2="400" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="400" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.8</text>

  <line x1="445" y1="54" x2="445" y2="66" stroke="#8b949e" stroke-width="1.5"/>
  <text x="445" y="84" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="9" font-family="system-ui, sans-serif">0.9</text>

  <line x1="490" y1="52" x2="490" y2="68" stroke="#4f8ef7" stroke-width="2"/>
  <text x="490" y="84" text-anchor="middle" fill="currentColor" font-size="11" font-family="system-ui, sans-serif">1</text>
</svg>
        """
    },
    {
        "title": "Understanding Hundredths",
        "body": """
<h4>Dividing into 100 Equal Parts</h4>

<p>A <strong>hundredth</strong> is what you get when you divide something into 100 equal parts and take 1 part.</p>

<div class="concept-box">
  <p>0.01 = 1/100 (one hundredth)</p>
  <p>0.25 = 25/100 (twenty-five hundredths)</p>
  <p>0.99 = 99/100 (ninety-nine hundredths)</p>
</div>

<h4>Grid Representation: 10 x 10 Grid = 100 Squares</h4>

<svg viewBox="0 0 340 310" style="width:100%;max-width:340px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="310" height="280" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="170" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">100 Hundredths (10 x 10 Grid)</text>

  <!-- Shaded area: 25 squares (0.25) - first 2.5 columns -->
  <g fill="#22c55e" opacity="0.5">
    <!-- Column 1 (rows 1-10) -->
    <rect x="45" y="52" width="24" height="24"/>
    <rect x="45" y="76" width="24" height="24"/>
    <rect x="45" y="100" width="24" height="24"/>
    <rect x="45" y="124" width="24" height="24"/>
    <rect x="45" y="148" width="24" height="24"/>
    <rect x="45" y="172" width="24" height="24"/>
    <rect x="45" y="196" width="24" height="24"/>
    <rect x="45" y="220" width="24" height="24"/>
    <rect x="45" y="244" width="24" height="24"/>
    <rect x="45" y="268" width="24" height="24"/>
    <!-- Column 2 (rows 1-10) -->
    <rect x="69" y="52" width="24" height="24"/>
    <rect x="69" y="76" width="24" height="24"/>
    <rect x="69" y="100" width="24" height="24"/>
    <rect x="69" y="124" width="24" height="24"/>
    <rect x="69" y="148" width="24" height="24"/>
    <rect x="69" y="172" width="24" height="24"/>
    <rect x="69" y="196" width="24" height="24"/>
    <rect x="69" y="220" width="24" height="24"/>
    <rect x="69" y="244" width="24" height="24"/>
    <rect x="69" y="268" width="24" height="24"/>
    <!-- Column 3 (rows 1-5 only = 5 more squares, total 25) -->
    <rect x="93" y="52" width="24" height="24"/>
    <rect x="93" y="76" width="24" height="24"/>
    <rect x="93" y="100" width="24" height="24"/>
    <rect x="93" y="124" width="24" height="24"/>
    <rect x="93" y="148" width="24" height="24"/>
  </g>

  <!-- Grid lines: 10 columns x 10 rows, each cell 24px -->
  <g stroke="#8b949e" stroke-width="0.5">
    <!-- Vertical lines -->
    <line x1="69" y1="52" x2="69" y2="292"/>
    <line x1="93" y1="52" x2="93" y2="292"/>
    <line x1="117" y1="52" x2="117" y2="292"/>
    <line x1="141" y1="52" x2="141" y2="292"/>
    <line x1="165" y1="52" x2="165" y2="292"/>
    <line x1="189" y1="52" x2="189" y2="292"/>
    <line x1="213" y1="52" x2="213" y2="292"/>
    <line x1="237" y1="52" x2="237" y2="292"/>
    <line x1="261" y1="52" x2="261" y2="292"/>
    <!-- Horizontal lines -->
    <line x1="45" y1="76" x2="285" y2="76"/>
    <line x1="45" y1="100" x2="285" y2="100"/>
    <line x1="45" y1="124" x2="285" y2="124"/>
    <line x1="45" y1="148" x2="285" y2="148"/>
    <line x1="45" y1="172" x2="285" y2="172"/>
    <line x1="45" y1="196" x2="285" y2="196"/>
    <line x1="45" y1="220" x2="285" y2="220"/>
    <line x1="45" y1="244" x2="285" y2="244"/>
    <line x1="45" y1="268" x2="285" y2="268"/>
  </g>

  <!-- Outer border -->
  <rect x="45" y="52" width="240" height="240" fill="none" stroke="#4f8ef7" stroke-width="2" rx="4"/>
</svg>

<p style="text-align:center;"><strong style="color:#22c55e;">25 squares shaded = 0.25 (twenty-five hundredths)</strong></p>

<div class="worked-example">
  <p><strong>Example:</strong> If you shaded 1 square out of 100, that's 0.01 (one hundredth). If you shaded 50 squares, that's 0.50 (fifty hundredths, or 1/2).</p>
</div>
        """
    },
    {
        "title": "Tenths and Hundredths Together",
        "body": """
<h4>Converting Between Tenths and Hundredths</h4>

<p>Since 1 tenth = 10 hundredths, we can write tenths as hundredths:</p>

<div class="concept-box">
  <p>0.1 = 0.10 (1 tenth = 10 hundredths)</p>
  <p>0.2 = 0.20 (2 tenths = 20 hundredths)</p>
  <p>0.5 = 0.50 (5 tenths = 50 hundredths)</p>
  <p>0.9 = 0.90 (9 tenths = 90 hundredths)</p>
</div>

<h4>Breaking Down a Decimal</h4>

<div class="worked-example">
  <p><strong>What does 0.37 mean?</strong></p>
  <p>0.37 = 0.3 + 0.07</p>
  <p>= 3 tenths + 7 hundredths</p>
  <p>= 30/100 + 7/100</p>
  <p>= 37/100</p>
</div>

<svg viewBox="0 0 500 140" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="470" height="110" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="250" y="38" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Place Value in 0.37</text>

  <!-- Decimal box -->
  <rect x="35" y="52" width="90" height="55" fill="#0f172a" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="80" y="70" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">Decimal</text>
  <text x="80" y="92" text-anchor="middle" fill="#4f8ef7" font-size="18" font-weight="bold" font-family="system-ui, sans-serif">0.37</text>

  <text x="145" y="84" text-anchor="middle" fill="currentColor" font-size="20" font-family="system-ui, sans-serif">=</text>

  <!-- Tenths box -->
  <rect x="165" y="52" width="90" height="55" fill="#0f172a" stroke="#22c55e" stroke-width="2" rx="4"/>
  <text x="210" y="70" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">tenths</text>
  <text x="210" y="92" text-anchor="middle" fill="#22c55e" font-size="18" font-weight="bold" font-family="system-ui, sans-serif">3</text>

  <text x="275" y="84" text-anchor="middle" fill="currentColor" font-size="20" font-family="system-ui, sans-serif">+</text>

  <!-- Hundredths box -->
  <rect x="295" y="52" width="90" height="55" fill="#0f172a" stroke="#f59e0b" stroke-width="2" rx="4"/>
  <text x="340" y="70" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="10" font-family="system-ui, sans-serif">hundredths</text>
  <text x="340" y="92" text-anchor="middle" fill="#f59e0b" font-size="18" font-weight="bold" font-family="system-ui, sans-serif">7</text>

  <text x="405" y="84" text-anchor="middle" fill="currentColor" font-size="20" font-family="system-ui, sans-serif">=</text>

  <text x="450" y="84" text-anchor="middle" fill="currentColor" font-size="16" font-weight="bold" font-family="system-ui, sans-serif">0.37</text>
</svg>

<div class="mcq-group">
  <p><strong>What do the digits in 0.45 represent?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 4 tenths + 5 hundredths = 45 hundredths total">4 tenths and 5 hundredths</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. The first digit after the decimal (4) is tenths, the second digit (5) is hundredths.">4 hundredths and 5 tenths</button>
    <button class="mcq-option" data-correct="false" data-explanation="No. 45 is the numerator, not what the digits represent in place value.">Just the number 45</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    },
    {
        "title": "Real-World Examples: Money",
        "body": """
<h4>Money Uses Hundredths!</h4>

<p>Money is one of the best examples of hundredths because 1 dollar = 100 cents.</p>

<svg viewBox="0 0 460 230" style="width:100%;max-width:460px;height:auto;display:block;margin:16px auto;">
  <rect x="15" y="15" width="430" height="200" fill="#1e293b" stroke="#334155" stroke-width="1" rx="4"/>
  <text x="230" y="40" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold" font-family="system-ui, sans-serif">Money and Decimals</text>

  <!-- Example 1: $1.25 -->
  <rect x="35" y="55" width="390" height="45" fill="#0f172a" stroke="#4f8ef7" stroke-width="1" rx="4"/>
  <text x="50" y="74" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">$1.25</text>
  <text x="110" y="74" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">= 1 dollar + 2 dimes + 5 cents</text>
  <text x="50" y="92" fill="currentColor" opacity="0.6" font-size="11" font-family="system-ui, sans-serif">= 1 + 0.20 + 0.05</text>

  <!-- Example 2: $3.42 -->
  <rect x="35" y="110" width="390" height="45" fill="#0f172a" stroke="#22c55e" stroke-width="1" rx="4"/>
  <text x="50" y="129" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">$3.42</text>
  <text x="110" y="129" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">= 3 dollars + 4 dimes + 2 cents</text>
  <text x="50" y="147" fill="currentColor" opacity="0.6" font-size="11" font-family="system-ui, sans-serif">= 3 + 0.40 + 0.02</text>

  <!-- Example 3: $0.87 -->
  <rect x="35" y="165" width="390" height="45" fill="#0f172a" stroke="#f59e0b" stroke-width="1" rx="4"/>
  <text x="50" y="184" fill="currentColor" font-size="13" font-weight="bold" font-family="system-ui, sans-serif">$0.87</text>
  <text x="110" y="184" fill="currentColor" font-size="12" font-family="system-ui, sans-serif">= 0 dollars + 8 dimes + 7 cents</text>
  <text x="50" y="202" fill="currentColor" opacity="0.6" font-size="11" font-family="system-ui, sans-serif">= 0 + 0.80 + 0.07</text>
</svg>

<div class="success-box">
  <p><strong>Remember:</strong> When you see $2.50, the first digit after the decimal (5) is <strong>dimes</strong> (tenths of a dollar), and the second digit (0) is <strong>cents</strong> (hundredths of a dollar).</p>
</div>

<div class="mcq-group">
  <p><strong>What is 45 cents as a decimal?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 45 cents = 45 hundredths of a dollar = $0.45">$0.45</button>
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. $0.45 is 45 hundredths, not 4.5 hundredths.">$4.5</button>
    <button class="mcq-option" data-correct="false" data-explanation="No. That would be 45 cents written as a whole number, not as part of a dollar.">45</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
        """
    }
]
