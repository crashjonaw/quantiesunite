TITLE = "Comparing Fractions"

SECTIONS = [
    {
        "title": "When Denominators Are the Same",
        "body": """<p>When two fractions have the <strong>same denominator</strong>, comparing them is easy: <strong>just compare the numerators!</strong></p>

<div class='worked-example'>
<p><strong>Compare:</strong> \\(\\frac{3}{8}\\) and \\(\\frac{5}{8}\\)</p>
<p>The denominators are both 8, so we compare 3 and 5.</p>
<p>Since 5 > 3, then \\(\\frac{5}{8}\\) > \\(\\frac{3}{8}\\)</p>
</div>

<h3>Visual Comparison</h3>
<svg width="300" height="150" viewBox="0 0 300 150" style="display: block; margin: 20px auto;">
  <!-- 3/8 -->
  <text x="30" y="25" font-size='14' font-weight='bold'>3/8</text>
  <rect x="20" y="40" width="25" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="45" y="40" width="25" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="70" y="40" width="25" height="30" fill='lightblue' stroke='#8b949e' stroke-width="1"/>
  <rect x="95" y="40" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="120" y="40" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="145" y="40" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="170" y="40" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="195" y="40" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>

  <!-- 5/8 -->
  <text x="30" y="95" font-size='14' font-weight='bold'>5/8</text>
  <rect x="20" y="110" width="25" height="30" fill='lightgreen' stroke='#8b949e' stroke-width="1"/>
  <rect x="45" y="110" width="25" height="30" fill='lightgreen' stroke='#8b949e' stroke-width="1"/>
  <rect x="70" y="110" width="25" height="30" fill='lightgreen' stroke='#8b949e' stroke-width="1"/>
  <rect x="95" y="110" width="25" height="30" fill='lightgreen' stroke='#8b949e' stroke-width="1"/>
  <rect x="120" y="110" width="25" height="30" fill='lightgreen' stroke='#8b949e' stroke-width="1"/>
  <rect x="145" y="110" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="170" y="110" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
  <rect x="195" y="110" width="25" height="30" fill='lightgray' stroke='#8b949e' stroke-width="1"/>
</svg>

<div class='success-box'>
<p>\\(\\frac{5}{8}\\) (green) covers more area than \\(\\frac{3}{8}\\) (blue), so it's larger!</p>
</div>"""
    },
    {
        "title": "When Denominators Are Different: Find a Common Denominator",
        "body": """<p>When fractions have <strong>different denominators</strong>, we must convert them to equivalent fractions with the same denominator.</p>

<h3>Strategy: Use a Common Denominator</h3>
<div class='worked-example'>
<p><strong>Compare:</strong> \\(\\frac{2}{3}\\) and \\(\\frac{3}{4}\\)</p>
<p><strong>Step 1: Find a common denominator.</strong> The denominators are 3 and 4. We can use 12 (\\(3 \\times 4\\)).</p>
<p><strong>Step 2: Convert both fractions:</strong></p>
<p>\\(\\frac{2}{3} = \\frac{2 \\times 4}{3 \\times 4} = \\frac{8}{12}\\)</p>
<p>\\(\\frac{3}{4} = \\frac{3 \\times 3}{4 \\times 3} = \\frac{9}{12}\\)</p>
<p><strong>Step 3: Compare:</strong> \\(\\frac{8}{12}\\) vs \\(\\frac{9}{12}\\)</p>
<p>Since 9 > 8, then \\(\\frac{9}{12}\\) > \\(\\frac{8}{12}\\)</p>
<p><strong>Therefore:</strong> \\(\\frac{3}{4}\\) > \\(\\frac{2}{3}\\)</p>
</div>"""
    },
    {
        "title": "Using a Number Line to Compare",
        "body": """<p>Visualizing fractions on a number line makes comparison intuitive: <strong>fractions further to the right are larger.</strong></p>

<h3>Number Line: Halves, Thirds, and Quarters</h3>
<svg width="320" height="170" style="display: block; margin: 20px auto;">
  <!-- Halves line -->
  <text x="10" y="25" font-size='12' font-weight='bold'>Halves:</text>
  <line x1="80" y1="20" x2="300" y2="20" stroke='#8b949e' stroke-width="2"/>
  <circle cx="80" cy="20" r="3" fill='currentColor'/>
  <circle cx="190" cy="20" r="3" fill='currentColor'/>
  <circle cx="300" cy="20" r="3" fill='currentColor'/>
  <text x="75" y="40" font-size='11'>0</text>
  <text x="183" y="40" font-size='11'>1/2</text>
  <text x="295" y="40" font-size='11'>1</text>

  <!-- Thirds line -->
  <text x="10" y="85" font-size='12' font-weight='bold'>Thirds:</text>
  <line x1="80" y1="80" x2="300" y2="80" stroke='#8b949e' stroke-width="2"/>
  <circle cx="80" cy="80" r="3" fill='currentColor'/>
  <circle cx="153" cy="80" r="3" fill='blue'/>
  <circle cx="227" cy="80" r="3" fill='blue'/>
  <circle cx="300" cy="80" r="3" fill='currentColor'/>
  <text x="75" y="100" font-size='11'>0</text>
  <text x="148" y="100" font-size='11'>1/3</text>
  <text x="222" y="100" font-size='11'>2/3</text>
  <text x="295" y="100" font-size='11'>1</text>

  <!-- Quarters line -->
  <text x="10" y="145" font-size='12' font-weight='bold'>Quarters:</text>
  <line x1="80" y1="140" x2="300" y2="140" stroke='#8b949e' stroke-width="2"/>
  <circle cx="80" cy="140" r="3" fill='currentColor'/>
  <circle cx="135" cy="140" r="3" fill='green'/>
  <circle cx="190" cy="140" r="3" fill='green'/>
  <circle cx="245" cy="140" r="3" fill='green'/>
  <circle cx="300" cy="140" r="3" fill='currentColor'/>
  <text x="75" y="160" font-size='11'>0</text>
  <text x="130" y="160" font-size='11'>1/4</text>
  <text x="185" y="160" font-size='11'>2/4</text>
  <text x="240" y="160" font-size='11'>3/4</text>
  <text x="295" y="160" font-size='11'>1</text>
</svg>

<h3>Comparing Using a Number Line</h3>
<p>Looking at the number lines:</p>
<ul>
<li>\\(\\frac{1}{2}\\) is at the same position as \\(\\frac{2}{4}\\) (they're equivalent!)</li>
<li>\\(\\frac{1}{3}\\) is to the left of \\(\\frac{1}{2}\\), so \\(\\frac{1}{3}\\) < \\(\\frac{1}{2}\\)</li>
<li>\\(\\frac{2}{3}\\) is to the right of \\(\\frac{1}{2}\\), so \\(\\frac{2}{3}\\) > \\(\\frac{1}{2}\\)</li>
</ul>"""
    },
    {
        "title": "Cross-Multiplication: A Quick Comparison Tool",
        "body": """<p>For a quick check when denominators are different, use <strong>cross-multiplication</strong>:</p>

<div class='worked-example'>
<p><strong>Compare:</strong> \\(\\frac{3}{5}\\) and \\(\\frac{2}{4}\\)</p>
<p><strong>Cross-multiply:</strong></p>
<p>\\(3 \\times 4 = 12\\)</p>
<p>\\(2 \\times 5 = 10\\)</p>
<p><strong>Compare the results:</strong> \\(12 > 10\\)</p>
<p><strong>Therefore:</strong> \\(\\frac{3}{5}\\) > \\(\\frac{2}{4}\\)</p>
</div>

<svg width="250" height="120" style="display: block; margin: 20px auto;">
  <text x="50" y="30" font-size='16' font-weight='bold'>3/5</text>
  <text x="50" y="60" font-size='16' font-weight='bold'>2/4</text>

  <!-- Cross arrows -->
  <line x1="80" y1="25" x2="180" y2="55" stroke='red' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="130" y="35" font-size='12' fill='red'>3×4=12</text>

  <line x1="80" y1="65" x2="180" y2="35" stroke='blue' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="130" y="75" font-size='12' fill='blue'>2×5=10</text>

  <text x="190" y="30" font-size='16'>12</text>
  <text x="190" y="60" font-size='16'>10</text>
  <text x="220" y="45" font-size='18' font-weight='bold'>&gt;</text>
</svg>"""
    },
    {
        "title": "Summary: Three Ways to Compare",
        "body": """<div class='concept-box'>
<p><strong>1. Same Denominators?</strong> Just compare numerators.</p>
<p>\\(\\frac{2}{7}\\) < \\(\\frac{5}{7}\\) because 2 < 5</p>
</div>

<div class='concept-box'>
<p><strong>2. Different Denominators?</strong> Find a common denominator or use a number line.</p>
<p>\\(\\frac{2}{3}\\) vs \\(\\frac{3}{5}\\) → Convert to \\(\\frac{10}{15}\\) vs \\(\\frac{9}{15}\\) → \\(\\frac{10}{15}\\) > \\(\\frac{9}{15}\\)</p>
</div>

<div class='concept-box'>
<p><strong>3. Quick Check?</strong> Use cross-multiplication.</p>
<p>\\(\\frac{3}{5}\\) vs \\(\\frac{2}{4}\\) → \\(3 \\times 4 = 12\\) and \\(2 \\times 5 = 10\\) → \\(12 > 10\\), so \\(\\frac{3}{5}\\) > \\(\\frac{2}{4}\\)</p>
</div>"""
    }
]
