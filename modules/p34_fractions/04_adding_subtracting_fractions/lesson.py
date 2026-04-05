TITLE = "Adding and Subtracting Fractions"

SECTIONS = [
    {
        "title": "Same Denominators: Just Add or Subtract the Numerators",
        "body": """<p>When fractions have the <strong>same denominator</strong>, adding or subtracting is simple:</p>

<div class='concept-box'>
<p><strong>Add or subtract the numerators. Keep the denominator the same.</strong></p>
<p>$$\\frac{a}{c} + \\frac{b}{c} = \\frac{a + b}{c}$$</p>
<p>$$\\frac{a}{c} - \\frac{b}{c} = \\frac{a - b}{c}$$</p>
</div>

<h3>Why This Works</h3>
<p>You're combining pieces of the same size! It's like adding apples to apples.</p>

<svg width="300" height="140" style="display: block; margin: 20px auto;">
  <!-- First fraction: 2/5 -->
  <text x="20" y="30" font-size='14' font-weight='bold'>2/5 +</text>
  <rect x="80" y="10" width="30" height="30" fill='orange' stroke='#8b949e' stroke-width="1"/>
  <rect x="110" y="10" width="30" height="30" fill='orange' stroke='#8b949e' stroke-width="1"/>
  <rect x="140" y="10" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="170" y="10" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="200" y="10" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>

  <!-- Second fraction: 1/5 -->
  <text x="20" y="90" font-size='14' font-weight='bold'>1/5 =</text>
  <rect x="80" y="70" width="30" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="110" y="70" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="140" y="70" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="170" y="70" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="200" y="70" width="30" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>

  <!-- Answer -->
  <text x="260" y="55" font-size='18' font-weight='bold'>3/5</text>
</svg>

<div class='worked-example'>
<p><strong>Example 1: Add</strong> \\(\\frac{2}{7}\\) + \\(\\frac{3}{7}\\)</p>
<p>Same denominator, so add numerators: (2 + 3) / 7 = 5/7</p>
</div>

<div class='worked-example'>
<p><strong>Example 2: Subtract</strong> \\(\\frac{5}{8}\\) - \\(\\frac{2}{8}\\)</p>
<p>Same denominator, so subtract numerators: (5 - 2) / 8 = 3/8</p>
</div>"""
    },
    {
        "title": "Different Denominators: Find a Common Denominator First",
        "body": """<p>When fractions have <strong>different denominators</strong>, you must convert them to equivalent fractions with a common denominator first.</p>

<h3>The Challenge</h3>
<p>You can't add thirds and quarters directly—they're different-sized pieces!</p>
<p>\\(\\frac{1}{3}\\) + \\(\\frac{1}{4}\\) ≠ \\(\\frac{2}{7}\\) (This is WRONG!)</p>

<h3>The Solution: Common Denominator</h3>
<div class='worked-example'>
<p><strong>Add:</strong> \\(\\frac{1}{3}\\) + \\(\\frac{1}{4}\\)</p>
<p><strong>Step 1: Find a common denominator.</strong> The denominators are 3 and 4. A common multiple is 12.</p>
<p><strong>Step 2: Convert to equivalent fractions:</strong></p>
<p>\\(\\frac{1}{3}\\) = \\(\\frac{1 × 4}{3 × 4}\\) = \\(\\frac{4}{12}\\)</p>
<p>\\(\\frac{1}{4}\\) = \\(\\frac{1 × 3}{4 × 3}\\) = \\(\\frac{3}{12}\\)</p>
<p><strong>Step 3: Add:</strong> \\(\\frac{4}{12}\\) + \\(\\frac{3}{12}\\) = \\(\\frac{7}{12}\\)</p>
</div>

<h3>Step-by-Step Example: Subtraction with Different Denominators</h3>
<div class='worked-example'>
<p><strong>Subtract:</strong> \\(\\frac{2}{3}\\) - \\(\\frac{1}{4}\\)</p>
<p><strong>Step 1: Find common denominator.</strong> Multiples of 3: 3, 6, 9, 12... Multiples of 4: 4, 8, 12...</p>
<p>Common denominator = 12</p>
<p><strong>Step 2: Convert:</strong></p>
<p>\\(\\frac{2}{3}\\) = \\(\\frac{2 × 4}{3 × 4}\\) = \\(\\frac{8}{12}\\)</p>
<p>\\(\\frac{1}{4}\\) = \\(\\frac{1 × 3}{4 × 3}\\) = \\(\\frac{3}{12}\\)</p>
<p><strong>Step 3: Subtract:</strong> \\(\\frac{8}{12}\\) - \\(\\frac{3}{12}\\) = \\(\\frac{5}{12}\\)</p>
</div>"""
    },
    {
        "title": "Using the Least Common Multiple (LCM)",
        "body": """<p>The <strong>Least Common Multiple (LCM)</strong> is the smallest common denominator. Using the LCM keeps your numbers small and makes simplifying easier.</p>

<h3>Finding the LCM</h3>
<div class='worked-example'>
<p><strong>Find the LCM of 4 and 6:</strong></p>
<p>Multiples of 4: 4, 8, 12, 16, 20, 24...</p>
<p>Multiples of 6: 6, 12, 18, 24...</p>
<p><strong>Common multiples:</strong> 12, 24...</p>
<p><strong>LCM = 12</strong> (the smallest)</p>
</div>

<h3>Using LCM to Add</h3>
<div class='worked-example'>
<p><strong>Add:</strong> \\(\\frac{1}{4}\\) + \\(\\frac{1}{6}\\)</p>
<p><strong>Step 1: LCM of 4 and 6 is 12.</strong></p>
<p><strong>Step 2: Convert:</strong></p>
<p>\\(\\frac{1}{4}\\) = \\(\\frac{1 × 3}{4 × 3}\\) = \\(\\frac{3}{12}\\)</p>
<p>\\(\\frac{1}{6}\\) = \\(\\frac{1 × 2}{6 × 2}\\) = \\(\\frac{2}{12}\\)</p>
<p><strong>Step 3: Add:</strong> \\(\\frac{3}{12}\\) + \\(\\frac{2}{12}\\) = \\(\\frac{5}{12}\\)</p>
</div>"""
    },
    {
        "title": "Always Simplify Your Answer",
        "body": """<p>After adding or subtracting, <strong>check if your answer can be simplified</strong> (reduced to lowest terms).</p>

<div class='worked-example'>
<p><strong>Add:</strong> \\(\\frac{1}{2}\\) + \\(\\frac{1}{4}\\)</p>
<p><strong>Step 1: Common denominator = 4</strong></p>
<p>\\(\\frac{1}{2}\\) = \\(\\frac{2}{4}\\)</p>
<p><strong>Step 2: Add:</strong> \\(\\frac{2}{4}\\) + \\(\\frac{1}{4}\\) = \\(\\frac{3}{4}\\)</p>
<p><strong>Step 3: Simplify:</strong> \\(\\frac{3}{4}\\) is already simplified (GCF of 3 and 4 is 1)</p>
</div>

<div class='worked-example'>
<p><strong>Add:</strong> \\(\\frac{1}{3}\\) + \\(\\frac{1}{6}\\)</p>
<p><strong>Step 1: LCM = 6</strong></p>
<p>\\(\\frac{1}{3}\\) = \\(\\frac{2}{6}\\)</p>
<p><strong>Step 2: Add:</strong> \\(\\frac{2}{6}\\) + \\(\\frac{1}{6}\\) = \\(\\frac{3}{6}\\)</p>
<p><strong>Step 3: Simplify:</strong> \\(\\frac{3}{6}\\) = \\(\\frac{1}{2}\\) (divide top and bottom by 3)</p>
</div>

<div class='success-box'>
<p>Always check: Can the numerator and denominator be divided by the same number?</p>
</div>"""
    },
    {
        "title": "Fractions with Whole Numbers and Mixed Numbers",
        "body": """<h3>Adding a Fraction to a Whole Number</h3>
<div class='worked-example'>
<p><strong>Add:</strong> 2 + \\(\\frac{3}{4}\\)</p>
<p>Result: \\(2\\frac{3}{4}\\)</p>
</div>

<h3>Adding Mixed Numbers</h3>
<div class='worked-example'>
<p><strong>Add:</strong> \\(1\\frac{2}{5}\\) + \\(2\\frac{1}{5}\\)</p>
<p><strong>Step 1: Add whole numbers:</strong> 1 + 2 = 3</p>
<p><strong>Step 2: Add fractions:</strong> \\(\\frac{2}{5}\\) + \\(\\frac{1}{5}\\) = \\(\\frac{3}{5}\\)</p>
<p><strong>Step 3: Combine:</strong> \\(3\\frac{3}{5}\\)</p>
</div>

<div class='worked-example'>
<p><strong>Add:</strong> \\(1\\frac{3}{4}\\) + \\(2\\frac{1}{3}\\)</p>
<p><strong>Step 1: Add whole numbers:</strong> 1 + 2 = 3</p>
<p><strong>Step 2: Add fractions (different denominators):</strong></p>
<p>\\(\\frac{3}{4}\\) + \\(\\frac{1}{3}\\)</p>
<p>LCM of 4 and 3 = 12</p>
<p>\\(\\frac{3}{4}\\) = \\(\\frac{9}{12}\\), \\(\\frac{1}{3}\\) = \\(\\frac{4}{12}\\)</p>
<p>\\(\\frac{9}{12}\\) + \\(\\frac{4}{12}\\) = \\(\\frac{13}{12}\\) = \\(1\\frac{1}{12}\\)</p>
<p><strong>Step 3: Combine:</strong> 3 + \\(1\\frac{1}{12}\\) = \\(4\\frac{1}{12}\\)</p>
</div>"""
    }
]
