"""Comparing Fractions — Understanding which fraction is bigger."""

TITLE = "Comparing Fractions: Which is Bigger?"

SECTIONS = [
    {
        "title": "Introduction to Comparing Fractions",
        "body": """<p>Now that you know about halves and quarters, you might wonder: <strong>Which is bigger — 1/2 or 1/4?</strong></p>
<p>To compare fractions, we think about the <strong>size of the pieces</strong>. The best way to understand this is by looking at pictures!</p>
<svg viewBox="0 0 470 210" style="width:100%;max-width:470px;height:auto;display:block;margin:16px auto;">
  <!-- Half -->
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">A half (1/2):</text>
  <rect x="15" y="45" width="80" height="80" fill="#ffc96d" stroke="#d4a574" stroke-width="2" rx="4"/>
  <line x1="55" y1="45" x2="55" y2="125" stroke="#d4a574" stroke-width="2"/>
  <rect x="15" y="45" width="40" height="80" fill="#ffb347" stroke="#d4a574" stroke-width="2" rx="4"/>
  <text x="25" y="93" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="62" y="93" font-size="11" fill="currentColor" opacity="0.6">empty</text>

  <!-- Quarter -->
  <text x="170" y="25" font-size="14" font-weight="bold" fill="currentColor">A quarter (1/4):</text>
  <rect x="170" y="45" width="80" height="80" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <line x1="210" y1="45" x2="210" y2="125" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="170" y1="85" x2="250" y2="85" stroke="#4f8ef7" stroke-width="2"/>
  <rect x="170" y="45" width="40" height="40" fill="#7ab8f5" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="180" y="72" font-size="11" font-weight="bold" fill="#fff">1/4</text>
  <text x="217" y="72" font-size="11" font-weight="bold" fill="#4f8ef7">1/4</text>
  <text x="180" y="110" font-size="11" font-weight="bold" fill="#4f8ef7">1/4</text>
  <text x="217" y="110" font-size="11" font-weight="bold" fill="#4f8ef7">1/4</text>

  <!-- Comparison result -->
  <text x="310" y="80" font-size="20" font-weight="bold" fill="#27ae60">1/2 &gt; 1/4</text>
  <text x="310" y="105" font-size="13" fill="#27ae60">1/2 is BIGGER</text>
  <text x="310" y="125" font-size="13" fill="#27ae60">than 1/4</text>

  <!-- Note -->
  <text x="15" y="165" font-size="13" fill="currentColor">Look at the shaded areas: the half takes up</text>
  <text x="15" y="183" font-size="13" fill="currentColor">more space than one quarter.</text>
</svg>
<div class="concept-box formula-box">
  <strong>Key Rule:</strong> When the denominator (bottom number) is <strong>smaller</strong>, the pieces are <strong>bigger</strong>!
</div>"""
    },
    {
        "title": "Understanding the Rule: Smaller Denominator = Bigger Pieces",
        "body": """<p>Let's think about cutting a pizza. If you cut it into fewer pieces, each piece is bigger!</p>
<svg viewBox="0 0 470 240" style="width:100%;max-width:470px;height:auto;display:block;margin:16px auto;">
  <!-- Pizza cut into 2 -->
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">Pizza cut into 2 pieces (halves):</text>
  <circle cx="80" cy="100" r="45" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <line x1="80" y1="55" x2="80" y2="145" stroke="#d4a574" stroke-width="2"/>
  <text x="55" y="105" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="90" y="105" font-size="14" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="30" y="165" font-size="12" fill="currentColor" opacity="0.6">BIG pieces!</text>

  <!-- Pizza cut into 4 -->
  <text x="230" y="25" font-size="14" font-weight="bold" fill="currentColor">Pizza cut into 4 pieces (quarters):</text>
  <circle cx="320" cy="100" r="45" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <line x1="320" y1="55" x2="320" y2="145" stroke="#d4a574" stroke-width="2"/>
  <line x1="275" y1="100" x2="365" y2="100" stroke="#d4a574" stroke-width="2"/>
  <text x="298" y="88" font-size="11" font-weight="bold" fill="#8b6914">1/4</text>
  <text x="330" y="88" font-size="11" font-weight="bold" fill="#8b6914">1/4</text>
  <text x="298" y="118" font-size="11" font-weight="bold" fill="#8b6914">1/4</text>
  <text x="330" y="118" font-size="11" font-weight="bold" fill="#8b6914">1/4</text>
  <text x="270" y="165" font-size="12" fill="currentColor" opacity="0.6">SMALL pieces!</text>

  <!-- Comparison text -->
  <text x="15" y="200" font-size="14" font-weight="bold" fill="currentColor">Comparison:</text>
  <text x="15" y="225" font-size="13" fill="currentColor">Same pizza. More cuts = Smaller pieces. Fewer cuts = Bigger pieces!</text>
</svg>
<div class="worked-example formula-box">
  <strong>Why is this true?</strong>
  <ul style="margin:8px 0;padding-left:20px;font-size:13px;">
    <li>1/2 means the pizza was cut into 2 pieces — each piece is large</li>
    <li>1/4 means the pizza was cut into 4 pieces — each piece is smaller</li>
    <li>So 1/2 is always bigger than 1/4 when they're the same whole!</li>
  </ul>
</div>"""
    },
    {
        "title": "Comparing Different Fractions",
        "body": """<p>Here are some common fraction comparisons using visual shapes:</p>
<svg viewBox="0 0 430 380" style="width:100%;max-width:430px;height:auto;display:block;margin:16px auto;">
  <!-- Comparison 1: 1/2 vs 1/4 -->
  <text x="15" y="25" font-size="13" font-weight="bold" fill="currentColor">Is 1/2 bigger than 1/4?</text>

  <!-- 1/2 bar -->
  <rect x="15" y="40" width="120" height="30" fill="#ff9999" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <rect x="15" y="40" width="60" height="30" fill="#e74c3c" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <text x="30" y="62" font-size="13" font-weight="bold" fill="#fff">1/2</text>

  <!-- 1/4 bar (same total width) -->
  <rect x="15" y="80" width="120" height="30" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <rect x="15" y="80" width="30" height="30" fill="#4f8ef7" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="18" y="102" font-size="13" font-weight="bold" fill="#fff">1/4</text>

  <text x="150" y="62" font-size="14" font-weight="bold" fill="#27ae60">YES!</text>
  <text x="150" y="100" font-size="12" fill="currentColor" opacity="0.6">1/2 is bigger</text>

  <!-- Comparison 2: 3/4 vs 1/4 -->
  <text x="15" y="145" font-size="13" font-weight="bold" fill="currentColor">Is 3/4 bigger than 1/4?</text>

  <!-- 3/4 bar -->
  <rect x="15" y="160" width="120" height="30" fill="#ffe0e0" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <rect x="15" y="160" width="90" height="30" fill="#e74c3c" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <text x="35" y="182" font-size="13" font-weight="bold" fill="#fff">3/4</text>

  <!-- 1/4 bar -->
  <rect x="15" y="200" width="120" height="30" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <rect x="15" y="200" width="30" height="30" fill="#4f8ef7" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="18" y="222" font-size="13" font-weight="bold" fill="#fff">1/4</text>

  <text x="150" y="182" font-size="14" font-weight="bold" fill="#27ae60">YES!</text>
  <text x="150" y="220" font-size="12" fill="currentColor" opacity="0.6">3/4 (3 pieces) is</text>
  <text x="150" y="235" font-size="12" fill="currentColor" opacity="0.6">bigger than 1/4 (1 piece)</text>

  <!-- Comparison 3: 3/4 vs 1/2 -->
  <text x="15" y="275" font-size="13" font-weight="bold" fill="currentColor">Is 3/4 bigger than 1/2?</text>

  <!-- 3/4 bar -->
  <rect x="15" y="290" width="120" height="30" fill="#ffe0e0" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <rect x="15" y="290" width="90" height="30" fill="#e74c3c" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <text x="35" y="312" font-size="13" font-weight="bold" fill="#fff">3/4</text>

  <!-- 1/2 bar -->
  <rect x="15" y="330" width="120" height="30" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <rect x="15" y="330" width="60" height="30" fill="#4f8ef7" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="28" y="352" font-size="13" font-weight="bold" fill="#fff">1/2</text>

  <text x="150" y="312" font-size="14" font-weight="bold" fill="#27ae60">YES!</text>
  <text x="150" y="350" font-size="12" fill="currentColor" opacity="0.6">3/4 is bigger than 1/2</text>
</svg>"""
    },
    {
        "title": "The Pattern: Unit Fractions",
        "body": """<p><strong>Unit fractions</strong> are fractions with 1 on top (like 1/2, 1/4, 1/8). When comparing unit fractions, here's the pattern:</p>
<svg viewBox="0 0 430 200" style="width:100%;max-width:430px;height:auto;display:block;margin:16px auto;">
  <!-- Visual pattern -->
  <text x="15" y="25" font-size="14" font-weight="bold" fill="currentColor">Fraction size comparison:</text>

  <rect x="15" y="50" width="180" height="32" fill="#ff9999" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <text x="80" y="72" font-size="14" font-weight="bold" fill="#c0392b">1/2</text>
  <text x="210" y="72" font-size="12" fill="currentColor" opacity="0.6">BIGGEST piece</text>

  <rect x="15" y="98" width="90" height="32" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <text x="45" y="120" font-size="14" font-weight="bold" fill="#4f8ef7">1/4</text>
  <text x="210" y="120" font-size="12" fill="currentColor" opacity="0.6">smaller</text>

  <rect x="15" y="146" width="45" height="32" fill="#a8e6a8" stroke="#27ae60" stroke-width="2" rx="4"/>
  <text x="25" y="168" font-size="12" font-weight="bold" fill="#27ae60">1/8</text>
  <text x="210" y="168" font-size="12" fill="currentColor" opacity="0.6">SMALLEST piece</text>
</svg>
<div class="success-box" style="background: #d4edda; padding: 12px; margin: 12px 0; border-radius: 4px; color: #1a1a2e;">
  <strong>Pattern:</strong> 1/2 &gt; 1/4 &gt; 1/8 (bigger denominator = smaller piece)
  <p style="margin:8px 0 0 0;font-size:13px;">The larger the denominator (bottom number), the smaller each piece is!</p>
</div>"""
    },
    {
        "title": "Comparing in Real Life",
        "body": """<p>Here are real situations where comparing fractions matters:</p>
<div style="display:grid;grid-template-columns:1fr;gap:12px;margin:16px 0;">
  <div class="worked-example formula-box">
    <strong>Food portions:</strong><br>
    Would you rather have 1/2 of a pizza or 1/4 of a pizza?
    Answer: 1/2 is bigger, so you get more food!
  </div>
  <div class="worked-example formula-box">
    <strong>Waiting time:</strong><br>
    Wait 1/2 hour or 1/4 hour?
    Answer: 1/2 hour is longer (30 minutes vs 15 minutes), so 1/4 hour is the better wait!
  </div>
  <div class="worked-example formula-box">
    <strong>Game progress:</strong><br>
    You've completed 3/4 of your game or 1/2 of your game?
    Answer: 3/4 is bigger, so you've done more progress!
  </div>
  <div class="worked-example formula-box">
    <strong>Reading a book:</strong><br>
    You've read 1/2 or 1/4 of the book?
    Answer: 1/2 is bigger, so you've read more pages!
  </div>
</div>"""
    }
]
