TITLE = "What Is a Fraction?"

SECTIONS = [
    {
        "title": "From Whole Numbers to Parts",
        "body": """<div class='concept-box'>
<p>You know whole numbers: 1, 2, 3... But what if you cut a pizza into 4 slices and eat 1? You ate <strong>PART of a whole</strong>. Fractions are the language for describing parts.</p>
<p>A <strong>fraction</strong> represents how much of something you have when it's divided into equal pieces.</p>
</div>

<h3>Real-World Examples</h3>
<ul>
<li><strong>Pizza:</strong> Cut into 8 slices, you eat 3 slices = 3/8</li>
<li><strong>Chocolate bar:</strong> 4 pieces, you have 1 piece = 1/4</li>
<li><strong>Time:</strong> 1 hour = 60 minutes, so 15 minutes = 1/4 hour</li>
<li><strong>Money:</strong> 1 dollar = 100 cents, so 50 cents = 1/2 dollar</li>
</ul>"""
    },
    {
        "title": "Numerator and Denominator: The Two Parts",
        "body": """<p>Every fraction has two parts. Let's look at \\(\\frac{3}{4}\\) (read as "three-fourths"):</p>

<svg width="310" height="130" viewBox="0 0 310 130" style="display: block; margin: 20px auto;">
  <!-- Fraction display -->
  <text x="80" y="45" font-size='32' font-family='sans-serif' text-anchor='middle' font-weight='bold' fill='currentColor'>3</text>
  <line x1="50" y1="55" x2="110" y2="55" stroke='#8b949e' stroke-width='2'/>
  <text x="80" y="90" font-size='32' font-family='sans-serif' text-anchor='middle' font-weight='bold' fill='currentColor'>4</text>

  <!-- Labels -->
  <line x1="112" y1="40" x2="140" y2="35" stroke='#58a6ff' stroke-width='1.5'/>
  <text x="145" y="40" font-size='14' font-family='sans-serif' fill='#58a6ff'>numerator (top)</text>
  <line x1="112" y1="85" x2="140" y2="90" stroke='#f97583' stroke-width='1.5'/>
  <text x="145" y="95" font-size='14' font-family='sans-serif' fill='#f97583'>denominator (bottom)</text>
</svg>

<div class='success-box'>
<p><strong>Numerator (top):</strong> How many pieces you <strong>have</strong></p>
<p><strong>Denominator (bottom):</strong> How many equal pieces the whole is divided <strong>into</strong></p>
</div>

<h3>Example: A Chocolate Bar</h3>
<svg width="280" height="110" viewBox="0 0 280 110" style="display: block; margin: 20px auto;">
  <!-- 4-piece chocolate bar -->
  <rect x="15" y="15" width="60" height="35" rx='4' fill='#e8a735' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="77" y="15" width="60" height="35" rx='4' fill='#e8a735' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="139" y="15" width="60" height="35" rx='4' fill='#e8a735' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="201" y="15" width="60" height="35" rx='4' fill='#6e4b2a' stroke='#8b949e' stroke-width='1.5'/>

  <!-- Labels -->
  <text x="140" y="72" font-size='14' font-family='sans-serif' font-weight='bold' text-anchor='middle' fill='currentColor'>3 pieces you eat (numerator)</text>
  <text x="140" y="92" font-size='13' font-family='sans-serif' text-anchor='middle' fill='currentColor'>4 pieces total (denominator)</text>
</svg>"""
    },
    {
        "title": "The Denominator Tells the Size of Each Piece",
        "body": """<p>A <strong>larger denominator</strong> means <strong>smaller pieces</strong>. A <strong>smaller denominator</strong> means <strong>bigger pieces</strong>.</p>

<h3>Compare These Fractions</h3>
<svg width="300" height="250" viewBox="0 0 300 250" style="display: block; margin: 20px auto;">
  <!-- 1/2 -->
  <text x="15" y="28" font-size='14' font-family='sans-serif' font-weight='bold' fill='currentColor'>1/2  (one-half)</text>
  <rect x="15" y="38" width="130" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="145" y="38" width="130" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1.5'/>

  <!-- 1/4 -->
  <text x="15" y="103" font-size='14' font-family='sans-serif' font-weight='bold' fill='currentColor'>1/4  (one-quarter)</text>
  <rect x="15" y="113" width="65" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="80" y="113" width="65" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="145" y="113" width="65" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1.5'/>
  <rect x="210" y="113" width="65" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1.5'/>

  <!-- 1/8 -->
  <text x="15" y="178" font-size='14' font-family='sans-serif' font-weight='bold' fill='currentColor'>1/8  (one-eighth)</text>
  <rect x="15" y="188" width="32.5" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1'/>
  <rect x="47.5" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="80" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="112.5" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="145" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="177.5" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="210" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="242.5" y="188" width="32.5" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>

  <text x="150" y="242" font-size='12' font-family='sans-serif' text-anchor='middle' fill='currentColor'>Bigger denominator = smaller pieces</text>
</svg>

<div class='warning-box'>
<p>Even though the numerator is 1 in all cases, the shaded pieces get <strong>smaller</strong> as the denominator gets <strong>larger</strong>!</p>
</div>"""
    },
    {
        "title": "Three Types of Fractions",
        "body": """<h3>Proper Fractions</h3>
<p><strong>Numerator &lt; Denominator</strong> (top number is smaller than bottom number)</p>
<p>Value: Less than 1 whole</p>
<div class='concept-box'>
<p>Examples: \\(\\frac{3}{5}\\), \\(\\frac{1}{4}\\), \\(\\frac{7}{10}\\)</p>
<p>You have some pieces, but not a complete whole.</p>
</div>

<h3>Improper Fractions</h3>
<p><strong>Numerator ≥ Denominator</strong> (top number is equal to or larger than bottom number)</p>
<p>Value: Equal to 1 or more than 1 whole</p>
<div class='concept-box'>
<p>Examples: \\(\\frac{7}{5}\\), \\(\\frac{4}{4}\\), \\(\\frac{11}{3}\\)</p>
<p>You have enough pieces to make one or more complete wholes.</p>
</div>

<h3>Mixed Numbers</h3>
<p>A <strong>whole number + a proper fraction</strong> combined.</p>
<div class='concept-box'>
<p>Examples: \\(1\\frac{2}{5}\\), \\(2\\frac{3}{4}\\), \\(3\\frac{1}{2}\\)</p>
<p>\\(1\\frac{2}{5}\\) means "1 whole and 2 fifths" = same as \\(\\frac{7}{5}\\)</p>
</div>

<h3>Converting Between Improper Fractions and Mixed Numbers</h3>
<div class='worked-example'>
<p><strong>Improper to Mixed:</strong> \\(\\frac{7}{5}\\)</p>
<p>How many 5s are in 7? One 5, with 2 left over.</p>
<p>So: \\(\\frac{7}{5}\\) = \\(1\\frac{2}{5}\\)</p>
</div>

<div class='worked-example'>
<p><strong>Mixed to Improper:</strong> \\(1\\frac{3}{4}\\)</p>
<p>Multiply: \\(1 \\times 4 = 4\\), then add the numerator: \\(4 + 3 = 7\\)</p>
<p>So: \\(1\\frac{3}{4}\\) = \\(\\frac{7}{4}\\)</p>
</div>"""
    },
    {
        "title": "Quick Check: Identifying Parts",
        "body": """<div class='concept-box'>
<p><strong>Look at this fraction: \\(\\frac{5}{8}\\)</strong></p>
<ul>
<li>Is it a proper or improper fraction? <span style="color: green;">Proper (5 &lt; 8)</span></li>
<li>What does 5 represent? <span style="color: green;">The numerator—how many pieces you have</span></li>
<li>What does 8 represent? <span style="color: green;">The denominator—how many pieces the whole is cut into</span></li>
<li>How many whole pizzas? <span style="color: green;">Less than 1 whole</span></li>
</ul>
</div>"""
    }
]
