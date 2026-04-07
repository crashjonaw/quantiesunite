"""What is a Fraction? — Introduction to parts of a whole."""

TITLE = "What is a Fraction?"

SECTIONS = [
    {
        "title": "Introduction: Breaking Things into Equal Parts",
        "body": """<p>Imagine you have <strong>ONE pizza</strong> and <strong>TWO hungry friends</strong>. You can't give each person a whole pizza, so you need to <strong>BREAK it into equal parts</strong>. That's what <strong>fractions</strong> are — parts of a whole, split equally.</p>
<p>A <strong>fraction</strong> is a piece or part of something whole. When you divide something into equal parts, each part is a fraction.</p>
<svg viewBox="0 0 430 215" style="width:100%;max-width:430px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size="16" font-weight="bold" fill="currentColor">One whole pizza</text>
  <circle cx="100" cy="120" r="60" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <text x="85" y="125" font-size="16" font-weight="bold" fill="#8b6914">1</text>

  <!-- Arrow -->
  <text x="180" y="125" font-size="24" fill="currentColor" opacity="0.6">--&gt;</text>

  <text x="235" y="30" font-size="16" font-weight="bold" fill="currentColor">Cut into 2 equal parts</text>
  <circle cx="330" cy="120" r="60" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <line x1="330" y1="60" x2="330" y2="180" stroke="#d4a574" stroke-width="2"/>
  <path d="M 330 60 A 60 60 0 0 0 330 180 Z" fill="#ffb347" opacity="0.5" stroke="none"/>
  <text x="300" y="125" font-size="16" font-weight="bold" fill="#8b6914">1/2</text>
  <text x="340" y="125" font-size="16" font-weight="bold" fill="#8b6914">1/2</text>
</svg>
<div class="concept-box" style="background: #e8f4f8; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Key Idea:</strong> When you cut something into equal parts, each part is a fraction of the whole!
</div>"""
    },
    {
        "title": "The Two Numbers in a Fraction",
        "body": """<p>Every fraction has <strong>two numbers</strong> that tell us important information:</p>
<svg viewBox="0 0 440 210" style="width:100%;max-width:440px;height:auto;display:block;margin:16px auto;">
  <text x="220" y="24" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">The Parts of a Fraction</text>

  <!-- Numerator label with arrow -->
  <text x="30" y="68" font-size="13" font-weight="bold" fill="#e74c3c">Numerator</text>
  <text x="30" y="84" font-size="11" fill="#e74c3c">(top number)</text>
  <line x1="115" y1="75" x2="140" y2="75" stroke="#e74c3c" stroke-width="1.5" marker-end="none"/>
  <polygon points="138,71 148,75 138,79" fill="#e74c3c"/>

  <!-- Large fraction in center -->
  <text x="170" y="80" font-size="42" font-weight="bold" fill="#e74c3c" text-anchor="middle">1</text>
  <line x1="148" y1="90" x2="192" y2="90" stroke="currentColor" stroke-width="3"/>
  <text x="170" y="128" font-size="42" font-weight="bold" fill="#27ae60" text-anchor="middle">2</text>

  <!-- Denominator label with arrow -->
  <text x="30" y="118" font-size="13" font-weight="bold" fill="#27ae60">Denominator</text>
  <text x="30" y="134" font-size="11" fill="#27ae60">(bottom number)</text>
  <line x1="115" y1="125" x2="140" y2="125" stroke="#27ae60" stroke-width="1.5"/>
  <polygon points="138,121 148,125 138,129" fill="#27ae60"/>

  <!-- Explanations on right side -->
  <text x="220" y="75" font-size="13" fill="currentColor">= How many parts we HAVE</text>
  <text x="220" y="125" font-size="13" fill="currentColor">= Total equal parts in the whole</text>

  <!-- Visual example bar -->
  <text x="220" y="170" font-size="13" font-weight="bold" fill="currentColor">Example: 1/2 means</text>
  <rect x="220" y="180" width="45" height="18" fill="#ffc96d" stroke="#b45309" stroke-width="1.5" rx="4"/>
  <rect x="270" y="180" width="45" height="18" fill="#f5f0e6" stroke="#b45309" stroke-width="1.5" rx="4"/>
  <text x="242" y="194" text-anchor="middle" font-size="10" fill="#000">1</text>
  <text x="292" y="194" text-anchor="middle" font-size="10" fill="#888">2</text>
  <text x="340" y="194" font-size="11" fill="currentColor">1 of 2 parts</text>
</svg>
<div class="worked-example formula-box">
  <strong>Example:</strong> If you cut a chocolate bar into 4 equal pieces and eat 1 piece, you ate <strong>1/4 (one quarter)</strong>.
  <ul style="margin:8px 0;padding-left:20px;">
    <li><strong>Numerator (1):</strong> You ate 1 piece</li>
    <li><strong>Denominator (4):</strong> The bar had 4 equal pieces</li>
  </ul>
</div>"""
    },
    {
        "title": "Equal Parts Are Essential",
        "body": """<p><strong>IMPORTANT:</strong> For something to be a fraction, the parts must be <strong>EQUAL</strong> in size. Unequal pieces are NOT fractions!</p>
<svg viewBox="0 0 500 175" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <!-- Equal parts (correct) -->
  <text x="15" y="25" font-size="14" font-weight="bold" fill="#27ae60">EQUAL PARTS (Correct!)</text>
  <rect x="15" y="45" width="50" height="55" fill="#a8e6a8" stroke="#27ae60" stroke-width="2" rx="4"/>
  <rect x="75" y="45" width="50" height="55" fill="#a8e6a8" stroke="#27ae60" stroke-width="2" rx="4"/>
  <text x="30" y="80" font-size="13" font-weight="bold" fill="#27ae60">1/2</text>
  <text x="90" y="80" font-size="13" font-weight="bold" fill="#27ae60">1/2</text>
  <text x="15" y="125" font-size="13" fill="#27ae60">Same size!</text>
  <text x="15" y="145" font-size="13" fill="#27ae60">These are fractions.</text>

  <!-- Unequal parts (wrong) -->
  <text x="265" y="25" font-size="14" font-weight="bold" fill="#e74c3c">UNEQUAL PARTS (Not fractions!)</text>
  <rect x="265" y="45" width="70" height="55" fill="#f5a9a9" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <rect x="345" y="45" width="25" height="55" fill="#f5a9a9" stroke="#e74c3c" stroke-width="2" rx="4"/>
  <text x="295" y="80" font-size="13" font-weight="bold" fill="#e74c3c">?</text>
  <text x="352" y="80" font-size="13" font-weight="bold" fill="#e74c3c">?</text>
  <text x="265" y="125" font-size="13" fill="#e74c3c">Different sizes!</text>
  <text x="265" y="145" font-size="13" fill="#e74c3c">These are NOT fractions.</text>
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
    <strong>Food and Sharing</strong><br>
    Half a pizza, a quarter of a cake, sharing treats fairly
  </div>
  <div class="concept-box" style="background: #e8f4f8; padding: 12px; border-radius: 4px">
    <strong>Telling Time</strong><br>
    Half an hour (30 minutes), a quarter hour (15 minutes)
  </div>
  <div class="concept-box" style="background: #d4edda; padding: 12px; border-radius: 4px">
    <strong>Measuring</strong><br>
    1/2 cup of flour, 1/4 liter of milk, 1/2 meter of fabric
  </div>
  <div class="concept-box" style="background:#f8d7da;border-left:4px solid #dc3545;padding:12px;border-radius:4px;">
    <strong>Sports and Games</strong><br>
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
<svg viewBox="0 0 470 200" style="width:100%;max-width:470px;height:auto;display:block;margin:16px auto;">
  <!-- Halves -->
  <text x="15" y="30" font-size="16" font-weight="bold" fill="currentColor">Halves: 1/2</text>
  <circle cx="90" cy="95" r="40" fill="#ffc96d" stroke="#d4a574" stroke-width="2"/>
  <line x1="90" y1="55" x2="90" y2="135" stroke="#d4a574" stroke-width="2"/>
  <path d="M 90 55 A 40 40 0 0 0 90 135 Z" fill="#ffb347" opacity="0.5" stroke="none"/>
  <text x="65" y="100" font-size="14" fill="#8b6914" font-weight="bold">1/2</text>
  <text x="100" y="100" font-size="14" fill="#8b6914" font-weight="bold">1/2</text>
  <text x="30" y="160" font-size="13" fill="currentColor" opacity="0.6">Cut into 2 equal parts</text>
  <text x="30" y="178" font-size="13" fill="currentColor" opacity="0.6">Each part = 1/2</text>

  <!-- Quarters -->
  <text x="260" y="30" font-size="16" font-weight="bold" fill="currentColor">Quarters: 1/4</text>
  <rect x="260" y="55" width="70" height="70" fill="#b3d9ff" stroke="#4f8ef7" stroke-width="2" rx="4"/>
  <line x1="295" y1="55" x2="295" y2="125" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="260" y1="90" x2="330" y2="90" stroke="#4f8ef7" stroke-width="2"/>
  <text x="270" y="80" font-size="12" fill="#4f8ef7" font-weight="bold">1/4</text>
  <text x="305" y="80" font-size="12" fill="#4f8ef7" font-weight="bold">1/4</text>
  <text x="270" y="112" font-size="12" fill="#4f8ef7" font-weight="bold">1/4</text>
  <text x="305" y="112" font-size="12" fill="#4f8ef7" font-weight="bold">1/4</text>
  <text x="260" y="160" font-size="13" fill="currentColor" opacity="0.6">Cut into 4 equal parts</text>
  <text x="260" y="178" font-size="13" fill="currentColor" opacity="0.6">Each part = 1/4</text>
</svg>
<div class="success-box" style="background: #d4edda; padding: 12px; margin: 12px 0; border-radius: 4px">
  <strong>Ready to learn?</strong> Next, we'll explore halves in detail, then quarters, and finally how to compare them!
</div>"""
    }
]
