TITLE = "Tenths and Hundredths"

SECTIONS = [
    {
        "title": "Understanding Tenths",
        "body": """
<h4>Dividing into 10 Equal Parts</h4>

<p>A <strong>tenth</strong> is what you get when you divide something into 10 equal parts and take 1 part.</p>

<svg viewBox="0 0 500 180" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>One Whole Divided Into 10 Tenths</text>

  <!-- Whole rectangle -->
  <rect x="20" y="40" width="460" height="60" fill='none' stroke='#4f8ef7' stroke-width="2" rx="2"/>

  <!-- 10 divisions -->
  <line x1="66" y1="40" x2="66" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="112" y1="40" x2="112" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="158" y1="40" x2="158" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="204" y1="40" x2="204" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="250" y1="40" x2="250" y2="100" stroke='#ef4444' stroke-width="2"/>
  <line x1="296" y1="40" x2="296" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="342" y1="40" x2="342" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="388" y1="40" x2="388" y2="100" stroke='#8b949e' stroke-width="1"/>
  <line x1="434" y1="40" x2="434" y2="100" stroke='#8b949e' stroke-width="1"/>

  <!-- Labels -->
  <text x="45" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.1</text>
  <text x="89" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.2</text>
  <text x="133" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.3</text>
  <text x="177" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.4</text>
  <text x="250" y="125" text-anchor='middle' fill='#ef4444' font-size='10' font-weight='bold'>0.5</text>
  <text x="319" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.6</text>
  <text x="365" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.7</text>
  <text x="411" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.8</text>
  <text x="457" y="125" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.9</text>

  <!-- Explanation -->
  <text x="250" y="160" text-anchor='middle' fill='currentColor' font-size='12'>Each part = 0.1 (one tenth = \\(\\frac{1}{10}\\))</text>
</svg>

<div class="concept-box">
  <p>\\(0.1 = \\frac{1}{10}\\) (one tenth)</p>
  <p>\\(0.5 = \\frac{5}{10}\\) (five tenths)</p>
  <p>\\(0.9 = \\frac{9}{10}\\) (nine tenths)</p>
</div>

<h4>Number Line: Tenths</h4>

<svg viewBox="0 0 550 140" style="width:100%;max-width:550px;height:auto;display:block;margin:16px auto;">
  <text x="275" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Number Line: 0 to 1 in Tenths</text>

  <!-- Main line -->
  <line x1="30" y1="60" x2="520" y2="60" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Tick marks and labels -->
  <line x1="30" y1="50" x2="30" y2="70" stroke='#4f8ef7' stroke-width="2"/>
  <text x="30" y="90" text-anchor='middle' fill='currentColor' font-size='12'>0</text>

  <line x1="79" y1="53" x2="79" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="79" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.1</text>

  <line x1="128" y1="53" x2="128" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="128" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.2</text>

  <line x1="177" y1="53" x2="177" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="177" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.3</text>

  <line x1="226" y1="53" x2="226" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="226" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.4</text>

  <line x1="275" y1="53" x2="275" y2="67" stroke='#ef4444' stroke-width="2"/>
  <text x="275" y="90" text-anchor='middle' fill='#ef4444' font-size='10' font-weight='bold'>0.5</text>

  <line x1="324" y1="53" x2="324" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="324" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.6</text>

  <line x1="373" y1="53" x2="373" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="373" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.7</text>

  <line x1="422" y1="53" x2="422" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="422" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.8</text>

  <line x1="471" y1="53" x2="471" y2="67" stroke='#8b949e' stroke-width="1.5"/>
  <text x="471" y="90" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>0.9</text>

  <line x1="520" y1="50" x2="520" y2="70" stroke='#4f8ef7' stroke-width="2"/>
  <text x="520" y="90" text-anchor='middle' fill='currentColor' font-size='12'>1</text>

  <!-- Highlight 0.5 -->
  <circle cx="275" cy="60" r="6" fill='#ef4444' opacity='0.3'/>
</svg>
        """
    },
    {
        "title": "Understanding Hundredths",
        "body": """
<h4>Dividing into 100 Equal Parts</h4>

<p>A <strong>hundredth</strong> is what you get when you divide something into 100 equal parts and take 1 part.</p>

<div class="concept-box">
  <p>\\(0.01 = \\frac{1}{100}\\) (one hundredth)</p>
  <p>\\(0.25 = \\frac{25}{100}\\) (twenty-five hundredths)</p>
  <p>\\(0.99 = \\frac{99}{100}\\) (ninety-nine hundredths)</p>
</div>

<h4>Grid Representation: 10×10 Grid = 100 Squares</h4>

<svg viewBox="0 0 500 300" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="20" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>100 Hundredths (10×10 Grid)</text>

  <!-- Grid lines -->
  <g stroke='#8b949e' stroke-width="1">
    <!-- Vertical lines -->
    <line x1="50" y1="50" x2="50" y2="250"/>
    <line x1="75" y1="50" x2="75" y2="250"/>
    <line x1="100" y1="50" x2="100" y2="250"/>
    <line x1="125" y1="50" x2="125" y2="250"/>
    <line x1="150" y1="50" x2="150" y2="250"/>
    <line x1="175" y1="50" x2="175" y2="250"/>
    <line x1="200" y1="50" x2="200" y2="250"/>
    <line x1="225" y1="50" x2="225" y2="250"/>
    <line x1="250" y1="50" x2="250" y2="250"/>
    <line x1="275" y1="50" x2="275" y2="250"/>
    <line x1="300" y1="50" x2="300" y2="250"/>
    <line x1="325" y1="50" x2="325" y2="250"/>
    <line x1="350" y1="50" x2="350" y2="250"/>
    <line x1="375" y1="50" x2="375" y2="250"/>
    <line x1="400" y1="50" x2="400" y2="250"/>
    <line x1="425" y1="50" x2="425" y2="250"/>
    <line x1="450" y1="50" x2="450" y2="250"/>
    <!-- Horizontal lines -->
    <line x1="50" y1="50" x2="450" y2="50"/>
    <line x1="50" y1="75" x2="450" y2="75"/>
    <line x1="50" y1="100" x2="450" y2="100"/>
    <line x1="50" y1="125" x2="450" y2="125"/>
    <line x1="50" y1="150" x2="450" y2="150"/>
    <line x1="50" y1="175" x2="450" y2="175"/>
    <line x1="50" y1="200" x2="450" y2="200"/>
    <line x1="50" y1="225" x2="450" y2="225"/>
    <line x1="50" y1="250" x2="450" y2="250"/>
  </g>

  <!-- Outer border -->
  <rect x="50" y="50" width="400" height="200" fill='none' stroke='#4f8ef7' stroke-width="2"/>

  <!-- Shaded area: 25 squares (0.25) -->
  <g fill='#22c55e' opacity='0.6'>
    <rect x="50" y="50" width="25" height="25"/>
    <rect x="75" y="50" width="25" height="25"/>
    <rect x="100" y="50" width="25" height="25"/>
    <rect x="125" y="50" width="25" height="25"/>
    <rect x="150" y="50" width="25" height="25"/>
    <rect x="50" y="75" width="25" height="25"/>
    <rect x="75" y="75" width="25" height="25"/>
    <rect x="100" y="75" width="25" height="25"/>
    <rect x="125" y="75" width="25" height="25"/>
    <rect x="150" y="75" width="25" height="25"/>
    <rect x="50" y="100" width="25" height="25"/>
    <rect x="75" y="100" width="25" height="25"/>
    <rect x="100" y="100" width="25" height="25"/>
    <rect x="125" y="100" width="25" height="25"/>
    <rect x="150" y="100" width="25" height="25"/>
    <rect x="50" y="125" width="25" height="25"/>
    <rect x="75" y="125" width="25" height="25"/>
    <rect x="100" y="125" width="25" height="25"/>
    <rect x="125" y="125" width="25" height="25"/>
    <rect x="150" y="125" width="25" height="25"/>
    <rect x="50" y="150" width="25" height="25"/>
    <rect x="75" y="150" width="25" height="25"/>
    <rect x="100" y="150" width="25" height="25"/>
    <rect x="125" y="150" width="25" height="25"/>
    <rect x="150" y="150" width="25" height="25"/>
  </g>

  <text x="250" y="280" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>25 squares shaded = 0.25 (twenty-five hundredths)</text>
</svg>

<div class="worked-example">
  <p><strong>Example:</strong> If you shaded 1 square out of 100, that's 0.01 (one hundredth). If you shaded 50 squares, that's 0.50 (fifty hundredths, or ½).</p>
</div>
        """
    },
    {
        "title": "Tenths and Hundredths Together",
        "body": """
<h4>Converting Between Tenths and Hundredths</h4>

<p>Since 1 tenth = 10 hundredths, we can write tenths as hundredths:</p>

<div class="concept-box">
  <p>\\(0.1 = 0.10\\) (1 tenth = 10 hundredths)</p>
  <p>\\(0.2 = 0.20\\) (2 tenths = 20 hundredths)</p>
  <p>\\(0.5 = 0.50\\) (5 tenths = 50 hundredths)</p>
  <p>\\(0.9 = 0.90\\) (9 tenths = 90 hundredths)</p>
</div>

<h4>Breaking Down a Decimal</h4>

<div class="worked-example">
  <p><strong>What does 0.37 mean?</strong></p>
  <p>\\(0.37 = 0.3 + 0.07\\)</p>
  <p>= 3 tenths + 7 hundredths</p>
  <p>= \\(\\frac{3}{10} + \\frac{7}{100}\\)</p>
  <p>= \\(\\frac{30}{100} + \\frac{7}{100}\\)</p>
  <p>= \\(\\frac{37}{100}\\)</p>
</div>

<svg viewBox="0 0 500 140" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Place Value in 0.37</text>

  <rect x="30" y="40" width="100" height="60" fill='#1e293b' stroke='#4f8ef7' stroke-width="2" rx="2"/>
  <text x="80" y="55" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='11'>Decimal</text>
  <text x="80" y="75" text-anchor='middle' fill='#4f8ef7' font-size='18' font-weight='bold'>0.37</text>

  <text x="155" y="75" text-anchor='middle' fill='currentColor' font-size='20'>=</text>

  <rect x="180" y="40" width="90" height="60" fill='#1e293b' stroke='#22c55e' stroke-width="2" rx="2"/>
  <text x="225" y="55" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>tenths</text>
  <text x="225" y="75" text-anchor='middle' fill='#22c55e' font-size='16' font-weight='bold'>3</text>

  <text x="295" y="75" text-anchor='middle' fill='currentColor' font-size='20'>+</text>

  <rect x="320" y="40" width="90" height="60" fill='#1e293b' stroke='#f59e0b' stroke-width="2" rx="2"/>
  <text x="365" y="55" text-anchor='middle' fill='currentColor' opacity='0.6' font-size='10'>hundredths</text>
  <text x="365" y="75" text-anchor='middle' fill='#f59e0b' font-size='16' font-weight='bold'>7</text>

  <text x="435" y="75" text-anchor='middle' fill='currentColor' font-size='20'>=</text>

  <text x="470" y="75" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>0.37</text>
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

<svg viewBox="0 0 500 240" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="18" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Money and Decimals</text>

  <!-- Example 1: $1.25 -->
  <rect x="20" y="35" width="460" height="50" fill='#0f172a' stroke='#4f8ef7' stroke-width="1" rx="2"/>
  <text x="35" y="55" fill='currentColor' font-size='12'><tspan font-weight='bold'>$1.25</tspan> = 1 dollar + 2 dimes + 5 cents</text>
  <text x="35" y="75" fill='currentColor' opacity='0.6' font-size='11'>= 1 + 0.20 + 0.05</text>

  <!-- Example 2: $3.42 -->
  <rect x="20" y="100" width="460" height="50" fill='#0f172a' stroke='#22c55e' stroke-width="1" rx="2"/>
  <text x="35" y="120" fill='currentColor' font-size='12'><tspan font-weight='bold'>$3.42</tspan> = 3 dollars + 4 dimes + 2 cents</text>
  <text x="35" y="140" fill='currentColor' opacity='0.6' font-size='11'>= 3 + 0.40 + 0.02</text>

  <!-- Example 3: $0.87 -->
  <rect x="20" y="165" width="460" height="50" fill='#0f172a' stroke='#f59e0b' stroke-width="1" rx="2"/>
  <text x="35" y="185" fill='currentColor' font-size='12'><tspan font-weight='bold'>$0.87</tspan> = 0 dollars + 8 dimes + 7 cents</text>
  <text x="35" y="205" fill='currentColor' opacity='0.6' font-size='11'>= 0 + 0.80 + 0.07</text>
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
