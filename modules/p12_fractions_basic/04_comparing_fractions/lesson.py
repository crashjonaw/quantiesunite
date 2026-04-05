"""Comparing Fractions — Understanding which fraction is bigger."""

TITLE = "Comparing Fractions: Which is Bigger?"

SECTIONS = [
    {
        "title": "Introduction to Comparing Fractions",
        "body": """<p>Now that you know about halves and quarters, you might wonder: <strong>Which is bigger — ½ or ¼?</strong></p>
<p>To compare fractions, we think about the <strong>size of the pieces</strong. The best way to understand this is by looking at pictures!</p>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Half -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#161b22'>A half (½):</text>
  <rect x="20" y="50" width="80" height="80" fill='#ffc96d' stroke='#d4a574' stroke-width="2" rx="4"/>
  <line x1="60" y1="50" x2="60" y2="130" stroke='#d4a574' stroke-width="2"/>
  <text x="35" y="97" font-size='14' fill='#8b6914' font-weight='bold'>½</text>
  <text x="70" y="97" font-size='12' fill='#ccc'>empty</text>

  <!-- Quarter -->
  <text x="180" y="30" font-size='14' font-weight='bold' fill='#161b22'>A quarter (¼):</text>
  <rect x="170" y="50" width="80" height="80" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <line x1="210" y1="50" x2="210" y2="130" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="170" y1="90" x2="250" y2="90" stroke='#4f8ef7' stroke-width="2"/>
  <text x="185" y="73" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="217" y="73" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="185" y="109" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="217" y="109" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>

  <!-- Comparison arrows -->
  <text x="350" y="97" font-size='28' fill='#27ae60' font-weight='bold'>✓</text>
  <text x="320" y="120" font-size='12' fill='#27ae60'>½ is BIGGER</text>
  <text x="320" y="135" font-size='12' fill='#27ae60'>than ¼</text>
</svg>
<div class="concept-box formula-box">
  <strong>Key Rule:</strong> When the denominator (bottom number) is <strong>smaller</strong>, the pieces are <strong>bigger</strong>!
</div>"""
    },
    {
        "title": "Understanding the Rule: Smaller Denominator = Bigger Pieces",
        "body": """<p>Let's think about cutting a pizza. If you cut it into fewer pieces, each piece is bigger!</p>
<svg viewBox="0 0 500 240" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Pizza cut into 2 -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#161b22'>Pizza cut into 2 pieces (halves):</text>
  <circle cx="80" cy="100" r="40" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="80" y1="60" x2="80" y2="140" stroke='#d4a574' stroke-width="2"/>
  <text x="60" y="105" font-size='14' fill='#8b6914' font-weight='bold'>½</text>
  <text x="95" y="105" font-size='14' fill='#8b6914' font-weight='bold'>½</text>
  <text x="30" y="160" font-size='12' fill='#8b949e'>BIG pieces!</text>

  <!-- Pizza cut into 4 -->
  <text x="250" y="30" font-size='14' font-weight='bold' fill='#161b22'>Pizza cut into 4 pieces (quarters):</text>
  <circle cx="320" cy="100" r="40" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="320" y1="60" x2="320" y2="140" stroke='#d4a574' stroke-width="2"/>
  <line x1="280" y1="100" x2="360" y2="100" stroke='#d4a574' stroke-width="2"/>
  <text x="305" y="88" font-size='11' fill='#8b6914' font-weight='bold'>¼</text>
  <text x="335" y="88" font-size='11' fill='#8b6914' font-weight='bold'>¼</text>
  <text x="305" y="118" font-size='11' fill='#8b6914' font-weight='bold'>¼</text>
  <text x="335" y="118" font-size='11' fill='#8b6914' font-weight='bold'>¼</text>
  <text x="260" y="160" font-size='12' fill='#8b949e'>SMALL pieces!</text>

  <!-- Comparison -->
  <text x="30" y="200" font-size='14' font-weight='bold' fill='#161b22'>Comparison:</text>
  <text x="30" y="225" font-size='13' fill='#8b949e'>Same pizza. More cuts = Smaller pieces. Fewer cuts = Bigger pieces!</text>
</svg>
<div class="worked-example formula-box">
  <strong>Why is this true?</strong>
  <ul style="margin:8px 0;padding-left:20px;font-size:13px;">
    <li>½ means the pizza was cut into 2 pieces — each piece is large</li>
    <li>¼ means the pizza was cut into 4 pieces — each piece is smaller</li>
    <li>So ½ is always bigger than ¼ when they're the same whole!</li>
  </ul>
</div>"""
    },
    {
        "title": "Comparing Different Fractions",
        "body": """<p>Here are some common fraction comparisons using visual shapes:</p>
<svg viewBox="0 0 500 380" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Comparison 1: 1/2 vs 1/4 -->
  <text x="20" y="30" font-size='13' font-weight='bold' fill='#161b22'>Is ½ bigger than ¼?</text>
  <rect x="20" y="50" width="60" height="50" fill='#ff9999' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <line x1="50" y1="50" x2="50" y2="100" stroke='#e74c3c' stroke-width="2"/>
  <text x="32" y="80" font-size='13' fill='#c0392b' font-weight='bold'>½</text>

  <text x="100" y="80" font-size='18' fill='#8b949e' font-weight='bold'>&gt;</text>

  <rect x="140" y="50" width="60" height="50" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <line x1="170" y1="50" x2="170" y2="100" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="140" y1="75" x2="200" y2="75" stroke='#4f8ef7' stroke-width="2"/>
  <text x="152" y="65" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="65" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="152" y="93" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="93" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>

  <text x="220" y="80" font-size='14' fill='#27ae60' font-weight='bold'>✓ YES!</text>
  <text x="220" y="105" font-size='12' fill='#8b949e'>½ is bigger</text>

  <!-- Comparison 2: 3/4 vs 1/4 -->
  <text x="20" y="150" font-size='13' font-weight='bold' fill='#161b22'>Is ¾ bigger than ¼?</text>
  <rect x="20" y="170" width="60" height="50" fill='#ff9999' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <line x1="35" y1="170" x2="35" y2="220" stroke='#e74c3c' stroke-width="2"/>
  <line x1="20" y1="195" x2="80" y2="195" stroke='#e74c3c' stroke-width="2"/>
  <text x="26" y="182" font-size='10' fill='#c0392b' font-weight='bold'>¼</text>
  <text x="44" y="182" font-size='10' fill='#c0392b' font-weight='bold'>¼</text>
  <text x="26" y="210" font-size='10' fill='#c0392b' font-weight='bold'>¼</text>
  <text x="44" y="210" font-size='10' fill='#c0392b' font-weight='bold'>¼</text>

  <text x="100" y="195" font-size='18' fill='#8b949e' font-weight='bold'>&gt;</text>

  <rect x="140" y="170" width="60" height="50" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <line x1="170" y1="170" x2="170" y2="220" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="140" y1="195" x2="200" y2="195" stroke='#4f8ef7' stroke-width="2"/>
  <text x="152" y="185" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="185" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="152" y="213" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="213" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>

  <text x="220" y="195" font-size='14' fill='#27ae60' font-weight='bold'>✓ YES!</text>
  <text x="220" y="220" font-size='12' fill='#8b949e'>¾ (3 pieces)</text>
  <text x="220" y="235" font-size='12' fill='#8b949e'>is bigger than ¼ (1 piece)</text>

  <!-- Comparison 3: 3/4 vs 1/2 -->
  <text x="20" y="280" font-size='13' font-weight='bold' fill='#161b22'>Is ¾ bigger than ½?</text>
  <rect x="20" y="300" width="60" height="50" fill='#ff9999' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <line x1="50" y1="300" x2="50" y2="350" stroke='#e74c3c' stroke-width="2"/>
  <line x1="20" y1="325" x2="80" y2="325" stroke='#e74c3c' stroke-width="2"/>
  <text x="28" y="318" font-size='11' fill='#c0392b' font-weight='bold'>½</text>
  <text x="55" y="318" font-size='11' fill='#c0392b' font-weight='bold'>½</text>
  <text x="28" y="346" font-size='11' fill='#c0392b' font-weight='bold'>½</text>
  <text x="55" y="346" font-size='11' fill='#c0392b' font-weight='bold'>½</text>

  <text x="100" y="325" font-size='18' fill='#8b949e' font-weight='bold'>&lt;</text>

  <rect x="140" y="300" width="60" height="50" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <line x1="170" y1="300" x2="170" y2="350" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="140" y1="325" x2="200" y2="325" stroke='#4f8ef7' stroke-width="2"/>
  <text x="152" y="315" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="315" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="152" y="343" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="175" y="343" font-size='11' fill='#4f8ef7' font-weight='bold'>¼</text>

  <text x="220" y="325" font-size='14' fill='#27ae60' font-weight='bold'>✓ YES!</text>
  <text x="220" y="350" font-size='12' fill='#8b949e'>¾ is bigger than ½</text>
</svg>"""
    },
    {
        "title": "The Pattern: Unit Fractions",
        "body": """<p><strong>Unit fractions</strong> are fractions with 1 on top (like ½, ¼, ⅛). When comparing unit fractions, here's the pattern:</p>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Visual pattern -->
  <text x="20" y="30" font-size='14' font-weight='bold' fill='#161b22'>Fraction size comparison:</text>

  <rect x="20" y="50" width="150" height="30" fill='#ff9999' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <text x="100" y="72" font-size='14' fill='#c0392b' font-weight='bold'>½</text>
  <text x="180" y="72" font-size='12' fill='#8b949e'>BIGGEST piece</text>

  <rect x="20" y="100" width="100" height="30" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <text x="70" y="122" font-size='14' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="180" y="122" font-size='12' fill='#8b949e'>smaller</text>

  <rect x="20" y="150" width="60" height="30" fill='#a8e6a8' stroke='#27ae60' stroke-width="2" rx="3"/>
  <text x="50" y="172" font-size='12' fill='#27ae60' font-weight='bold'>⅛</text>
  <text x="180" y="172" font-size='12' fill='#8b949e'>SMALLEST piece</text>
</svg>
<div class="success-box" style="background: #d4edda; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Pattern:</strong> \\(\\frac{1}{2}\\) > \\(\\frac{1}{4}\\) > \\(\\frac{1}{8}\\) (bigger denominator = smaller piece)
  <p style="margin:8px 0 0 0;font-size:13px;">The larger the denominator (bottom number), the smaller each piece is!</p>
</div>"""
    },
    {
        "title": "Comparing in Real Life",
        "body": """<p>Here are real situations where comparing fractions matters:</p>
<div style="display:grid;grid-template-columns:1fr;gap:12px;margin:16px 0;">
  <div class="worked-example formula-box">
    <strong>🍕 Food portions:</strong><br>
    Would you rather have ½ of a pizza or ¼ of a pizza?
    Answer: ½ is bigger, so you get more food!
  </div>
  <div class="worked-example formula-box">
    <strong>⏰ Waiting time:</strong><br>
    Wait ½ hour or ¼ hour?
    Answer: ½ hour is longer (30 minutes vs 15 minutes), so ¼ hour is the better wait!
  </div>
  <div class="worked-example formula-box">
    <strong>🎮 Game progress:</strong><br>
    You've completed ¾ of your game or ½ of your game?
    Answer: ¾ is bigger, so you've done more progress!
  </div>
  <div class="worked-example formula-box">
    <strong>📖 Reading a book:</strong><br>
    You've read ½ or ¼ of the book?
    Answer: ½ is bigger, so you've read more pages!
  </div>
</div>"""
    }
]
