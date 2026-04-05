"""Understanding Halves — Learning about one-half (½)."""

TITLE = "Understanding Halves (½)"

SECTIONS = [
    {
        "title": "What is a Half?",
        "body": """<p>A <strong>half</strong> (written as \\(\\frac{1}{2}\\)) is when you cut something into <strong>2 equal pieces</strong>. Each piece is called <strong>one half</strong> or <strong>½</strong>.</p>
<p>Think of it like this: If you have a whole item and you cut it into 2 pieces that are exactly the same size, each piece is a half.</p>
<svg viewBox="0 0 450 180" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <!-- Whole item -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#161b22'>One Whole:</text>
  <rect x="20" y="50" width="100" height="80" fill='#ffc96d' stroke='#d4a574' stroke-width="2" rx="4"/>
  <text x="65" y="100" font-size='16' fill='#8b6914' font-weight='bold'>Whole</text>

  <!-- Arrow -->
  <text x="150" y="100" font-size='20' fill='#8b949e'>→</text>

  <!-- Two halves -->
  <text x="200" y="30" font-size='14' font-weight='bold' fill='#161b22'>Cut into 2 equal pieces:</text>
  <rect x="190" y="50" width="45" height="80" fill='#ffc96d' stroke='#d4a574' stroke-width="2" rx="4"/>
  <text x="210" y="100" font-size='14' fill='#8b6914' font-weight='bold'>½</text>

  <rect x="245" y="50" width="45" height="80" fill='#f5f0e6' stroke='#d4a574' stroke-width="2" rx="4"/>
  <text x="260" y="100" font-size='14' fill='#8b6914' font-weight='bold'>½</text>

  <!-- Labels -->
  <text x="190" y="150" font-size='12' fill='#8b949e'>Same size</text>
  <line x1="210" y1="140" x2="215" y2="135" stroke='#555' stroke-width="1"/>
  <line x1="267" y1="140" x2="262" y2="135" stroke='#555' stroke-width="1"/>
</svg>
<div class="concept-box" style="background: #e8f4f8; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Key fact:</strong> \\(\\frac{1}{2}\\) + \\(\\frac{1}{2}\\) = 1 whole. Two halves always equal one whole!
</div>"""
    },
    {
        "title": "Visual Examples of Halves",
        "body": """<p>Here are some real ways we see halves in everyday life:</p>
<svg viewBox="0 0 500 280" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Circle (pizza) -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#161b22'>A pizza cut in half:</text>
  <circle cx="80" cy="90" r="35" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="80" y1="55" x2="80" y2="125" stroke='#d4a574' stroke-width="2"/>
  <text x="65" y="95" font-size='14' fill='#8b6914' font-weight='bold'>½</text>
  <text x="90" y="95" font-size='14' fill='#8b6914' font-weight='bold'>½</text>

  <!-- Rectangle (chocolate bar) -->
  <text x="200" y="30" font-size='14' font-weight='bold' fill='#161b22'>Chocolate bar split in half:</text>
  <rect x="200" y="55" width="80" height="35" fill='#8b6914' stroke='#5d4b0f' stroke-width="2" rx="2"/>
  <line x1="240" y1="55" x2="240" y2="90" stroke='#5d4b0f' stroke-width="2"/>
  <text x="215" y="80" font-size='12' fill='#ffd699' font-weight='bold'>½</text>
  <text x="250" y="80" font-size='12' fill='#ffd699' font-weight='bold'>½</text>

  <!-- Apple cut in half -->
  <text x="350" y="30" font-size='14' font-weight='bold' fill='#161b22'>Apple cut in half:</text>
  <circle cx="400" cy="90" r="30" fill='#e74c3c' stroke='#c0392b' stroke-width="2"/>
  <line x1="400" y1="60" x2="400" y2="120" stroke='#c0392b' stroke-width="2"/>
  <text x="385" y="92" font-size='12' fill='#fff' font-weight='bold'>½</text>
  <text x="405" y="92" font-size='12' fill='#fff' font-weight='bold'>½</text>

  <!-- Paper folding -->
  <text x="30" y="150" font-size='14' font-weight='bold' fill='#161b22'>Paper folded in half:</text>
  <rect x="20" y="170" width="70" height="50" fill='#e8f4f8' stroke='#4f8ef7' stroke-width="2" rx="2"/>
  <line x1="20" y1="195" x2="90" y2="195" stroke='#4f8ef7' stroke-width="2" stroke-dasharray="3,3"/>
  <text x="30" y="210" font-size='12' fill='#4f8ef7' font-weight='bold'>½</text>
  <text x="60" y="210" font-size='12' fill='#4f8ef7' font-weight='bold'>½</text>

  <!-- Clock -->
  <text x="200" y="150" font-size='14' font-weight='bold' fill='#161b22'>Half an hour:</text>
  <circle cx="245" cy="195" r="25" fill='none' stroke='#8b949e' stroke-width="2"/>
  <line x1="245" y1="170" x2="245" y2="145" stroke='#8b949e' stroke-width="2"/>
  <line x1="245" y1="170" x2="260" y2="185" stroke='#8b949e' stroke-width="2"/>
  <text x="235" y="215" font-size='12' fill='#8b949e'>30 minutes</text>

  <!-- Money -->
  <text x="350" y="150" font-size='14' font-weight='bold' fill='#161b22'>Half the money:</text>
  <rect x="330" y="175" width="35" height="20" fill='#90ee90' stroke='#27ae60' stroke-width="1" rx="2"/>
  <text x="340" y="188" font-size='11' fill='#27ae60' font-weight='bold'>£5</text>
  <text x="330" y="210" font-size='12' fill='#8b949e'>If you had £10</text>
  <text x="330" y="225" font-size='12' fill='#8b949e'>and split it in half</text>
</svg>"""
    },
    {
        "title": "The Parts of a Half",
        "body": """<p>In the fraction \\(\\frac{1}{2}\\):</p>
<div style="margin: 16px 0; padding: 16px; border-left: 4px solid #ffc107; border-radius: 4px">
  <p style="margin:0 0 10px 0;"><strong style="font-size:16px;">1</strong> (the top number) = We have <strong>1 piece</strong></p>
  <p style="margin:0 0 10px 0;"><strong style="font-size:20px;">―</strong></p>
  <p style="margin:0;"><strong style="font-size:16px;">2</strong> (the bottom number) = The whole was cut into <strong>2 equal pieces</strong></p>
</div>
<svg viewBox="0 0 450 220" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <!-- Example 1 -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#161b22'>Example: Half a pizza (one of two pieces)</text>
  <circle cx="100" cy="100" r="40" fill='#ffc96d' stroke='#d4a574' stroke-width="2"/>
  <line x1="100" y1="60" x2="100" y2="140" stroke='#d4a574' stroke-width="2"/>
  <path d="M 100 60 A 40 40 0 0 0 100 140" fill='#ff9999' opacity='0.6' stroke='none'/>
  <text x="85" y="105" font-size='12' fill='#8b6914' font-weight='bold'>You have this ½</text>

  <!-- Fraction notation -->
  <text x="190" y="100" font-size='40' fill='#161b22' font-weight='bold'>½</text>
  <text x="240" y="80" font-size='12' fill='#8b949e'>(one shaded piece out of two)</text>

  <!-- Example 2 -->
  <text x="30" y="180" font-size='14' font-weight='bold' fill='#161b22'>Example: Half of a chocolate bar</text>
  <rect x="30" y="195" width="50" height="15" fill='#8b6914' stroke='#5d4b0f' stroke-width="1" rx="1"/>
  <rect x="85" y="195" width="50" height="15" fill='#d4a574' stroke='#5d4b0f' stroke-width="1" rx="1"/>
  <text x="35" y="207" font-size='11' fill='#ffd699' font-weight='bold'>½</text>
  <text x="195" y="205" font-size='12' fill='#8b949e'>(the dark piece)</text>
</svg>
<div class="worked-example formula-box">
  <strong>Real-world scenario:</strong> You and your friend share a sandwich. Your friend gets one half, you get one half. You both got \\(\\frac{1}{2}\\) of the sandwich!
</div>"""
    },
    {
        "title": "Combining Halves to Make a Whole",
        "body": """<p>An important pattern: if you put two halves together, you get back the whole thing!</p>
<svg viewBox="0 0 450 200" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <!-- First half -->
  <rect x="30" y="40" width="50" height="70" fill='#ff9999' stroke='#e74c3c' stroke-width="2" rx="4"/>
  <text x="45" y="85" font-size='14' fill='#c0392b' font-weight='bold'>½</text>

  <!-- Plus sign -->
  <text x="95" y="85" font-size='32' fill='#8b949e' font-weight='bold'>+</text>

  <!-- Second half -->
  <rect x="130" y="40" width="50" height="70" fill='#99ccff' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="145" y="85" font-size='14' fill='#2c3e50' font-weight='bold'>½</text>

  <!-- Equals -->
  <text x="200" y="85" font-size='32' fill='#8b949e' font-weight='bold'>=</text>

  <!-- Whole -->
  <rect x="240" y="40" width="100" height="70" fill='#b3d9ff' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="280" y="85" font-size='20' fill='#2c3e50' font-weight='bold'>1 WHOLE</text>
</svg>
<div class="success-box" style="background: #d4edda; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>The equation:</strong> \\(\\frac{1}{2}\\) + \\(\\frac{1}{2}\\) = 1 whole
  <p style="margin:8px 0 0 0;font-size:13px;">This means if you have half of something and get another half, you have the complete thing!</p>
</div>"""
    },
    {
        "title": "Practice: Identifying Halves",
        "body": """<p>Can you spot which items show halves? Remember: the two pieces must be <strong>equal in size</strong>.</p>
<svg viewBox="0 0 500 290" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Correct halves -->
  <text x="30" y="30" font-size='14' font-weight='bold' fill='#27ae60'>✓ This shows halves:</text>
  <rect x="30" y="50" width="40" height="60" fill='#a8e6a8' stroke='#27ae60' stroke-width="2" rx="3"/>
  <rect x="75" y="50" width="40" height="60" fill='#a8e6a8' stroke='#27ae60' stroke-width="2" rx="3"/>
  <text x="40" y="87" font-size='13' fill='#27ae60' font-weight='bold'>½</text>
  <text x="80" y="87" font-size='13' fill='#27ae60' font-weight='bold'>½</text>
  <text x="30" y="135" font-size='12' fill='#27ae60'>Equal pieces!</text>

  <!-- Correct halves circle -->
  <text x="280" y="30" font-size='14' font-weight='bold' fill='#27ae60'>✓ This shows halves:</text>
  <circle cx="330" cy="85" r="30" fill='#a8e6a8' stroke='#27ae60' stroke-width="2"/>
  <line x1="330" y1="55" x2="330" y2="115" stroke='#27ae60' stroke-width="2"/>
  <text x="315" y="88" font-size='13' fill='#27ae60' font-weight='bold'>½</text>
  <text x="340" y="88" font-size='13' fill='#27ae60' font-weight='bold'>½</text>
  <text x="280" y="135" font-size='12' fill='#27ae60'>Equal halves!</text>

  <!-- Wrong halves -->
  <text x="30" y="170" font-size='14' font-weight='bold' fill='#e74c3c'>✗ This does NOT show halves:</text>
  <rect x="30" y="190" width="60" height="50" fill='#f5a9a9' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <rect x="95" y="190" width="20" height="50" fill='#f5a9a9' stroke='#e74c3c' stroke-width="2" rx="3"/>
  <text x="45" y="220" font-size='12' fill='#e74c3c' font-weight='bold'>?</text>
  <text x="100" y="220" font-size='12' fill='#e74c3c' font-weight='bold'>?</text>
  <text x="30" y="260" font-size='12' fill='#e74c3c'>Pieces are different sizes!</text>

  <!-- Wrong halves -->
  <text x="280" y="170" font-size='14' font-weight='bold' fill='#e74c3c'>✗ This does NOT show halves:</text>
  <circle cx="330" cy="240" r="30" fill='#f5a9a9' stroke='#e74c3c' stroke-width="2"/>
  <line x1="310" y1="245" x2="350" y2="235" stroke='#e74c3c' stroke-width="2"/>
  <text x="310" y="250" font-size='12' fill='#e74c3c' font-weight='bold'>?</text>
  <text x="335" y="230" font-size='12' fill='#e74c3c' font-weight='bold'>?</text>
  <text x="280" y="280" font-size='12' fill='#e74c3c'>Not divided equally!</text>
</svg>"""
    }
]
