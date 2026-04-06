TITLE = "Equivalent Fractions"

SECTIONS = [
    {
        "title": "Same Amount, Different Pieces",
        "body": """<div class='concept-box'>
<p><strong>Equivalent fractions</strong> are different fractions that represent the same amount.</p>
<p>It's like cutting the same pizza into different numbers of slices—you still ate the same amount!</p>
</div>

<h3>A Chocolate Bar Example</h3>
<svg width="300" height="175" viewBox="0 0 300 175" style="display: block; margin: 20px auto;">
  <!-- First bar: divided into 2 pieces -->
  <text x="30" y="20" font-size='14' font-weight='bold'>1/2</text>
  <rect x="20" y="30" width="100" height="40" fill='orange' stroke='#8b949e' stroke-width="2"/>
  <rect x="120" y="30" width="100" height="40" fill='lightgray' stroke='#8b949e' stroke-width="2"/>
  <line x1="120" y1="30" x2="120" y2="70" stroke='#8b949e' stroke-width="2"/>

  <!-- Second bar: divided into 4 pieces -->
  <text x="30" y="115" font-size='14' font-weight='bold'>2/4</text>
  <rect x="20" y="125" width="50" height="40" fill='orange' stroke='#8b949e' stroke-width="1"/>
  <rect x="70" y="125" width="50" height="40" fill='orange' stroke='#8b949e' stroke-width="1"/>
  <rect x="120" y="125" width="50" height="40" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="170" y="125" width="50" height="40" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <line x1="70" y1="125" x2="70" y2="165" stroke='#8b949e' stroke-width="1"/>
  <line x1="120" y1="125" x2="120" y2="165" stroke='#8b949e' stroke-width="1"/>
  <line x1="170" y1="125" x2="170" y2="165" stroke='#8b949e' stroke-width="1"/>

  <!-- Equals sign -->
  <text x="260" y="85" font-size='24' font-weight='bold'>=</text>
</svg>

<div class='success-box'>
<p>You ate the same amount in both cases! The shaded area is identical.</p>
<p>\\(\\frac{1}{2}\\) = \\(\\frac{2}{4}\\)</p>
</div>"""
    },
    {
        "title": "How to Create Equivalent Fractions: Multiply",
        "body": """<p>To create equivalent fractions, <strong>multiply both the numerator AND denominator by the same number</strong>.</p>

<div class='worked-example'>
<p><strong>Start with:</strong> \\(\\frac{1}{2}\\)</p>
<p><strong>Multiply top and bottom by 2:</strong> \\(\\frac{1 \\times 2}{2 \\times 2} = \\frac{2}{4}\\)</p>
<p><strong>Multiply top and bottom by 3:</strong> \\(\\frac{1 \\times 3}{2 \\times 3} = \\frac{3}{6}\\)</p>
<p><strong>Multiply top and bottom by 5:</strong> \\(\\frac{1 \\times 5}{2 \\times 5} = \\frac{5}{10}\\)</p>
<p><strong>All of these are equivalent:</strong> $$\\frac{1}{2} = \\frac{2}{4} = \\frac{3}{6} = \\frac{5}{10}$$</p>
</div>

<h3>Why This Works</h3>
<div class='concept-box'>
<p>When you divide each piece into 2 smaller parts, you have twice as many parts. But you still need twice as many to equal the original amount!</p>
<p>Example: If you cut a pizza slice in half, you have 2 half-slices instead of 1 whole slice. That's \\(\\frac{2}{4}\\) instead of \\(\\frac{1}{2}\\)—same amount of pizza!</p>
</div>

<h3>Visual Example: Building Equivalent Fractions</h3>
<svg width="320" height="180" style="display: block; margin: 20px auto;">
  <!-- 1/2 -->
  <text x="20" y="25" font-size='13'>1/2 =</text>
  <rect x="60" y="10" width="100" height="30" fill='lightblue' stroke='#8b949e' stroke-width="2"/>
  <rect x="160" y="10" width="100" height="30" fill='lightgray' stroke='#8b949e' stroke-width="2"/>

  <!-- 2/4 -->
  <text x="20" y="80" font-size='13'>2/4 =</text>
  <rect x="60" y="65" width="50" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="110" y="65" width="50" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="160" y="65" width="50" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="210" y="65" width="50" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>

  <!-- 3/6 -->
  <text x="20" y="155" font-size='13'>3/6 =</text>
  <rect x="60" y="135" width="33" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="93" y="135" width="34" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="127" y="135" width="33" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="160" y="135" width="33" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="193" y="135" width="34" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="227" y="135" width="33" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
</svg>"""
    },
    {
        "title": "Simplifying Fractions: Divide to Reduce",
        "body": """<p>Sometimes fractions can be written using smaller numbers. We <strong>simplify</strong> by dividing both numerator and denominator by the same number.</p>

<div class='worked-example'>
<p><strong>Simplify:</strong> \\(\\frac{6}{8}\\)</p>
<p><strong>Both are divisible by 2:</strong> \\(\\frac{6 \\div 2}{8 \\div 2} = \\frac{3}{4}\\)</p>
<p><strong>3/4 is the simplified form</strong>—we can't simplify further because 3 and 4 share no common factors.</p>
</div>

<h3>Finding the Greatest Common Factor (GCF)</h3>
<p>To simplify completely, divide by the <strong>greatest common factor</strong>—the largest number that divides both the numerator and denominator.</p>

<div class='worked-example'>
<p><strong>Simplify:</strong> \\(\\frac{12}{18}\\)</p>
<p><strong>Factors of 12:</strong> 1, 2, 3, 4, 6, 12</p>
<p><strong>Factors of 18:</strong> 1, 2, 3, 6, 9, 18</p>
<p><strong>Common factors:</strong> 1, 2, 3, 6</p>
<p><strong>GCF = 6</strong></p>
<p>\\(\\frac{12 \\div 6}{18 \\div 6} = \\frac{2}{3}\\)</p>
</div>

<div class='success-box'>
<p>A fraction is in <strong>simplest form</strong> when the numerator and denominator have no common factors other than 1.</p>
</div>"""
    },
    {
        "title": "Practice: Generating and Simplifying",
        "body": """<h3>Generate Equivalent Fractions</h3>
<div class='worked-example'>
<p><strong>Write 3 equivalent fractions for \\(\\frac{2}{5}\\)</strong></p>
<p>Multiply by 2: \\(\\frac{2 \\times 2}{5 \\times 2} = \\frac{4}{10}\\)</p>
<p>Multiply by 3: \\(\\frac{2 \\times 3}{5 \\times 3} = \\frac{6}{15}\\)</p>
<p>Multiply by 4: \\(\\frac{2 \\times 4}{5 \\times 4} = \\frac{8}{20}\\)</p>
<p><strong>Answer:</strong> \\(\\frac{4}{10}\\), \\(\\frac{6}{15}\\), \\(\\frac{8}{20}\\)</p>
</div>

<h3>Simplify Fractions</h3>
<div class='worked-example'>
<p><strong>Simplify \\(\\frac{8}{12}\\)</strong></p>
<p>GCF of 8 and 12 = 4</p>
<p>\\(\\frac{8 \\div 4}{12 \\div 4} = \\frac{2}{3}\\)</p>
</div>"""
    }
]
