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

<svg width="300" height="120" style="display: block; margin: 20px auto;">
  <!-- Fraction display -->
  <text x="100" y="40" font-size='32' text-anchor='middle' font-weight='bold'>3</text>
  <line x1="60" y1="50" x2="140" y2="50" stroke='#8b949e' stroke-width="2"/>
  <text x="100" y="80" font-size='32' text-anchor='middle' font-weight='bold'>4</text>

  <!-- Labels -->
  <text x="160" y="40" font-size='14' fill='blue'>numerator</text>
  <text x="160" y="80" font-size='14' fill='red'>denominator</text>
  <line x1="140" y1="35" x2="160" y2="40" stroke='blue' stroke-width="1"/>
  <line x1="140" y1="80" x2="160" y2="80" stroke='red' stroke-width="1"/>
</svg>

<div class='success-box'>
<p><strong>Numerator (top):</strong> How many pieces you <strong>have</strong></p>
<p><strong>Denominator (bottom):</strong> How many equal pieces the whole is divided <strong>into</strong></p>
</div>

<h3>Example: A Chocolate Bar</h3>
<svg width="250" height="95" style="display: block; margin: 20px auto;">
  <!-- Whole bar -->
  <rect x="20" y="20" width="200" height="30" fill='brown' stroke='#8b949e' stroke-width="2"/>
  <!-- Divide into 4 pieces -->
  <line x1="70" y1="20" x2="70" y2="50" stroke='#8b949e' stroke-width="1"/>
  <line x1="120" y1="20" x2="120" y2="50" stroke='#8b949e' stroke-width="1"/>
  <line x1="170" y1="20" x2="170" y2="50" stroke='#8b949e' stroke-width="1"/>
  <!-- Highlight 3 pieces -->
  <rect x="20" y="20" width="50" height="30" fill='orange' opacity='0.5' stroke='none'/>
  <rect x="70" y="20" width="50" height="30" fill='orange' opacity='0.5' stroke='none'/>
  <rect x="120" y="20" width="50" height="30" fill='orange' opacity='0.5' stroke='none'/>
  <text x="125" y="70" font-size='16' font-weight='bold' text-anchor='middle'>3 pieces you eat (numerator)</text>
  <text x="125" y="85" font-size='14' text-anchor='middle'>4 pieces total (denominator)</text>
</svg>"""
    },
    {
        "title": "The Denominator Tells the Size of Each Piece",
        "body": """<p>A <strong>larger denominator</strong> means <strong>smaller pieces</strong>. A <strong>smaller denominator</strong> means <strong>bigger pieces</strong>.</p>

<h3>Compare These Fractions</h3>
<svg width="280" height="220" viewBox="0 0 280 220" style="display: block; margin: 20px auto;">
  <!-- 1/2 -->
  <text x="20" y="25" font-size='16' font-weight='bold'>1/2 (one-half, big piece)</text>
  <rect x="30" y="40" width="100" height="20" fill='lightblue' stroke='#8b949e' stroke-width="2"/>
  <rect x="130" y="40" width="100" height="20" fill='lightgray' stroke='#8b949e' stroke-width="2"/>

  <!-- 1/4 -->
  <text x="20" y="100" font-size='16' font-weight='bold'>1/4 (one-quarter, smaller)</text>
  <rect x="30" y="115" width="50" height="20" fill='lightblue' stroke='#8b949e' stroke-width="2"/>
  <rect x="80" y="115" width="50" height="20" fill='lightgray' stroke='#8b949e' stroke-width="2"/>
  <rect x="130" y="115" width="50" height="20" fill='lightgray' stroke='#8b949e' stroke-width="2"/>
  <rect x="180" y="115" width="50" height="20" fill='lightgray' stroke='#8b949e' stroke-width="2"/>

  <!-- 1/8 -->
  <text x="20" y="175" font-size='16' font-weight='bold'>1/8 (one-eighth, smallest)</text>
  <rect x="30" y="190" width="25" height="20" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="55" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="80" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="105" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="130" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="155" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="180" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="205" y="190" width="25" height="20" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
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
