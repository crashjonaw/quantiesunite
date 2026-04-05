"""What is a Fraction? — Introduction to parts of a whole."""

TITLE = "What is a Fraction?"

SECTIONS = [
    {
        "title": "Introduction: Breaking Things into Equal Parts",
        "body": """<p>Imagine you have <strong>ONE pizza</strong> and <strong>TWO hungry friends</strong>. You can't give each person a whole pizza, so you need to <strong>BREAK it into equal parts</strong>. That's what <strong>fractions</strong> are — parts of a whole, split equally.</p>
<p>A <strong>fraction</strong> is a piece or part of something whole. When you divide something into equal parts, each part is a fraction.</p>
<svg viewBox="0 0 400 200" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="20" y="30" font-size='16' font-weight='bold' fill='#161b22'>One whole pizza</text>
  <circle cx="100" cy="100" r="60" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <text x="75" y="105" font-size='20' fill='#8b6914'>🍕</text>

  <text x="220" y="30" font-size='16' font-weight='bold' fill='#161b22'>Cut into 2 equal parts</text>
  <circle cx="320" cy="100" r="60" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="320" y1="40" x2="320" y2="160" stroke='#d4a574' stroke-width="2"/>
  <text x="300" y="95" font-size='14' fill='#8b6914'>½</text>
  <text x="335" y="95" font-size='14' fill='#8b6914'>½</text>
</svg>
<div class="concept-box" style="background: #e8f4f8; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Key Idea:</strong> When you cut something into equal parts, each part is a fraction of the whole!
</div>"""
    },
    {
        "title": "The Two Numbers in a Fraction",
        "body": """<p>Every fraction has <strong>two numbers</strong> that tell us important information:</p>
<svg viewBox="0 0 520 280" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Numerator and denominator example -->
  <text x="50" y="40" font-size='18' font-weight='bold' fill='#161b22'>Numerator (top number)</text>
  <line x1="50" y1="50" x2="120" y2="100" stroke='#e74c3c' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="80" y="130" font-size='24' font-weight='bold' fill='#e74c3c'>1</text>
  <text x="20" y="130" font-size='48' fill='#161b22' font-weight='bold'>—</text>
  <text x="80" y="155" font-size='14' fill='#8b949e'>How many parts we have</text>

  <text x="250" y="40" font-size='18' font-weight='bold' fill='#161b22'>Denominator (bottom number)</text>
  <line x1="230" y1="50" x2="170" y2="100" stroke='#27ae60' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="150" y="130" font-size='24' font-weight='bold' fill='#27ae60'>2</text>
  <text x="180" y="155" font-size='14' fill='#8b949e'>How many equal parts the whole is cut into</text>

  <!-- Visual example -->
  <text x="50" y="220" font-size='16' font-weight='bold' fill='#161b22'>Example: ½ (one half)</text>
  <rect x="50" y="240" width="40" height="20" fill='#ffc96d' stroke='#d4a574' stroke-width="1"/>
  <rect x="95" y="240" width="40" height="20" fill='#f5f5f5' stroke='#d4a574' stroke-width="1"/>
  <text x="140" y="255" font-size='13' fill='#8b949e'>1 shaded part out of 2 equal parts</text>
</svg>
<div class="worked-example formula-box">
  <strong>Example:</strong> If you cut a chocolate bar into 4 equal pieces and eat 1 piece, you ate <strong>¼ (one quarter)</strong>.
  <ul style="margin:8px 0;padding-left:20px;">
    <li><strong>Numerator (1):</strong> You ate 1 piece</li>
    <li><strong>Denominator (4):</strong> The bar had 4 equal pieces</li>
  </ul>
</div>"""
    },
    {
        "title": "Equal Parts Are Essential",
        "body": """<p><strong>IMPORTANT:</strong> For something to be a fraction, the parts must be <strong>EQUAL</strong> in size. Unequal pieces are NOT fractions!</p>
<svg viewBox="0 0 560 220" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Equal parts (correct) -->
  <text x="30" y="30" font-size='16' font-weight='bold' fill='#27ae60'>✓ EQUAL PARTS (Correct!)</text>
  <rect x="30" y="50" width="40" height="50" fill='#a8e6a8' stroke='#27ae60' stroke-width="2"/>
  <rect x="75" y="50" width="40" height="50" fill='#a8e6a8' stroke='#27ae60' stroke-width="2"/>
  <text x="35" y="85" font-size='12' fill='#27ae60'>½</text>
  <text x="80" y="85" font-size='12' fill='#27ae60'>½</text>
  <text x="30" y="130" font-size='13' fill='#27ae60'>Same size!</text>
  <text x="30" y="150" font-size='13' fill='#27ae60'>These are fractions.</text>

  <!-- Unequal parts (wrong) -->
  <text x="280" y="30" font-size='16' font-weight='bold' fill='#e74c3c'>✗ UNEQUAL PARTS (Not fractions!)</text>
  <rect x="280" y="50" width="60" height="50" fill='#f5a9a9' stroke='#e74c3c' stroke-width="2"/>
  <rect x="345" y="50" width="20" height="50" fill='#f5a9a9' stroke='#e74c3c' stroke-width="2"/>
  <text x="305" y="85" font-size='12' fill='#e74c3c'>?</text>
  <text x="350" y="85" font-size='12' fill='#e74c3c'>?</text>
  <text x="280" y="130" font-size='13' fill='#e74c3c'>Different sizes!</text>
  <text x="280" y="150" font-size='13' fill='#e74c3c'>These are NOT fractions.</text>
</svg>
<div class="warning-box" style="background:#ffe6e6;border-left:4px solid #e74c3c;padding:12px;margin:12px 0;border-radius:4px;">
  <strong>Remember:</strong> If the parts are not equal in size, we cannot call them fractions. Equal parts are the foundation of all fractions!
</div>"""
    },
    {
        "title": "Real-World Fractions",
        "body": """<p>Fractions are everywhere in daily life! We use them for:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0;">
  <div class="concept-box formula-box">
    <strong>🍕 Food & Sharing</strong><br>
    Half a pizza, a quarter of a cake, sharing treats fairly
  </div>
  <div class="concept-box" style="background: #e8f4f8; padding: 12px; border-radius: 4px">
    <strong>⏰ Telling Time</strong><br>
    Half an hour (30 minutes), a quarter hour (15 minutes)
  </div>
  <div class="concept-box" style="background: #d4edda; padding: 12px; border-radius: 4px">
    <strong>📏 Measuring</strong><br>
    ½ cup of flour, ¼ liter of milk, ½ meter of fabric
  </div>
  <div class="concept-box" style="background:#f8d7da;border-left:4px solid #dc3545;padding:12px;border-radius:4px;">
    <strong>🎯 Sports & Games</strong><br>
    Half-time in a game, a quarter of a year (3 months)
  </div>
</div>
<p><strong>Learning fractions helps you:</strong></p>
<ul style="line-height:1.8;font-size:14px;">
  <li>Split things fairly with friends and family</li>
  <li>Follow recipes when cooking or baking</li>
  <li>Understand measurements and distances</li>
  <li>Tell time (especially on analog clocks!)</li>
  <li>Make sense of money and discounts later</li>
</ul>"""
    },
    {
        "title": "What You'll Learn",
        "body": """<p>In this module, we focus on two important fractions that you use most often in real life:</p>
<svg viewBox="0 0 500 240" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Halves -->
  <text x="50" y="40" font-size='18' font-weight='bold' fill='#161b22'>Halves: ½</text>
  <circle cx="110" cy="90" r="35" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="110" y1="55" x2="110" y2="125" stroke='#d4a574' stroke-width="2"/>
  <text x="95" y="95" font-size='16' fill='#8b6914' font-weight='bold'>½</text>
  <text x="125" y="95" font-size='16' fill='#8b6914' font-weight='bold'>½</text>
  <text x="50" y="150" font-size='14' fill='#8b949e'>Cut into 2 equal parts</text>
  <text x="50" y="170" font-size='14' fill='#8b949e'>Each part = ½</text>

  <!-- Quarters -->
  <text x="300" y="40" font-size='18' font-weight='bold' fill='#161b22'>Quarters: ¼</text>
  <rect x="280" y="55" width="60" height="60" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2"/>
  <line x1="310" y1="55" x2="310" y2="115" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="280" y1="85" x2="340" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="287" y="77" font-size='12' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="315" y="77" font-size='12' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="287" y="103" font-size='12' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="315" y="103" font-size='12' fill='#4f8ef7' font-weight='bold'>¼</text>
  <text x="280" y="150" font-size='14' fill='#8b949e'>Cut into 4 equal parts</text>
  <text x="280" y="170" font-size='14' fill='#8b949e'>Each part = ¼</text>
</svg>
<div class="success-box" style="background: #d4edda; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Ready to learn?</strong> Next, we'll explore halves in detail, then quarters, and finally how to compare them!
</div>"""
    }
]
