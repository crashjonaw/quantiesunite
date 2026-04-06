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
<svg width="300" height="170" viewBox="0 0 300 170" style="display: block; margin: 20px auto;">
  <!-- 3/8 -->
  <text x="15" y="28" font-size='14' font-family='sans-serif' font-weight='bold' fill='currentColor'>3/8</text>
  <rect x="50" y="15" width="28" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1'/>
  <rect x="78" y="15" width="28" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1'/>
  <rect x="106" y="15" width="28" height="28" rx='4' fill='#58a6ff' stroke='#8b949e' stroke-width='1'/>
  <rect x="134" y="15" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="162" y="15" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="190" y="15" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="218" y="15" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="246" y="15" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>

  <!-- 5/8 -->
  <text x="15" y="98" font-size='14' font-family='sans-serif' font-weight='bold' fill='currentColor'>5/8</text>
  <rect x="50" y="80" width="28" height="28" rx='4' fill='#3fb950' stroke='#8b949e' stroke-width='1'/>
  <rect x="78" y="80" width="28" height="28" rx='4' fill='#3fb950' stroke='#8b949e' stroke-width='1'/>
  <rect x="106" y="80" width="28" height="28" rx='4' fill='#3fb950' stroke='#8b949e' stroke-width='1'/>
  <rect x="134" y="80" width="28" height="28" rx='4' fill='#3fb950' stroke='#8b949e' stroke-width='1'/>
  <rect x="162" y="80" width="28" height="28" rx='4' fill='#3fb950' stroke='#8b949e' stroke-width='1'/>
  <rect x="190" y="80" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="218" y="80" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>
  <rect x="246" y="80" width="28" height="28" rx='4' fill='#3d3d3d' stroke='#8b949e' stroke-width='1'/>

  <!-- Caption -->
  <text x="155" y="140" font-size='13' font-family='sans-serif' text-anchor='middle' fill='currentColor'>5/8 covers more area than 3/8</text>
  <text x="155" y="158" font-size='13' font-family='sans-serif' text-anchor='middle' fill='currentColor'>so 5/8 &gt; 3/8</text>
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
<svg width="340" height="200" viewBox="0 0 340 200" style="display: block; margin: 20px auto;">
  <!-- Halves line -->
  <text x="15" y="30" font-size='12' font-family='sans-serif' font-weight='bold' fill='currentColor'>Halves:</text>
  <line x1="85" y1="25" x2="315" y2="25" stroke='#8b949e' stroke-width='2'/>
  <circle cx="85" cy="25" r="4" fill='currentColor'/>
  <circle cx="200" cy="25" r="4" fill='currentColor'/>
  <circle cx="315" cy="25" r="4" fill='currentColor'/>
  <text x="82" y="48" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>0</text>
  <text x="200" y="48" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1/2</text>
  <text x="315" y="48" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1</text>

  <!-- Thirds line -->
  <text x="15" y="95" font-size='12' font-family='sans-serif' font-weight='bold' fill='currentColor'>Thirds:</text>
  <line x1="85" y1="90" x2="315" y2="90" stroke='#8b949e' stroke-width='2'/>
  <circle cx="85" cy="90" r="4" fill='currentColor'/>
  <circle cx="162" cy="90" r="4" fill='#58a6ff'/>
  <circle cx="238" cy="90" r="4" fill='#58a6ff'/>
  <circle cx="315" cy="90" r="4" fill='currentColor'/>
  <text x="85" y="113" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>0</text>
  <text x="162" y="113" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1/3</text>
  <text x="238" y="113" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>2/3</text>
  <text x="315" y="113" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1</text>

  <!-- Quarters line -->
  <text x="15" y="160" font-size='12' font-family='sans-serif' font-weight='bold' fill='currentColor'>Quarters:</text>
  <line x1="85" y1="155" x2="315" y2="155" stroke='#8b949e' stroke-width='2'/>
  <circle cx="85" cy="155" r="4" fill='currentColor'/>
  <circle cx="142.5" cy="155" r="4" fill='#3fb950'/>
  <circle cx="200" cy="155" r="4" fill='#3fb950'/>
  <circle cx="257.5" cy="155" r="4" fill='#3fb950'/>
  <circle cx="315" cy="155" r="4" fill='currentColor'/>
  <text x="85" y="178" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>0</text>
  <text x="142.5" y="178" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1/4</text>
  <text x="200" y="178" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>2/4</text>
  <text x="257.5" y="178" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>3/4</text>
  <text x="315" y="178" font-size='11' font-family='sans-serif' text-anchor='middle' fill='currentColor'>1</text>
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

<svg width="290" height="130" viewBox="0 0 290 130" style="display: block; margin: 20px auto;">
  <!-- Fractions -->
  <text x="30" y="40" font-size='18' font-family='sans-serif' font-weight='bold' fill='currentColor'>3/5</text>
  <text x="30" y="95" font-size='18' font-family='sans-serif' font-weight='bold' fill='currentColor'>2/4</text>

  <!-- Cross arrows -->
  <line x1="70" y1="35" x2="160" y2="85" stroke='#f97583' stroke-width='2' stroke-dasharray='5,4'/>
  <text x="120" y="48" font-size='13' font-family='sans-serif' fill='#f97583'>3 x 4 = 12</text>

  <line x1="70" y1="90" x2="160" y2="40" stroke='#58a6ff' stroke-width='2' stroke-dasharray='5,4'/>
  <text x="120" y="108" font-size='13' font-family='sans-serif' fill='#58a6ff'>2 x 5 = 10</text>

  <!-- Results -->
  <text x="195" y="40" font-size='18' font-family='sans-serif' font-weight='bold' fill='#f97583'>12</text>
  <text x="195" y="95" font-size='18' font-family='sans-serif' font-weight='bold' fill='#58a6ff'>10</text>
  <text x="240" y="70" font-size='22' font-family='sans-serif' font-weight='bold' fill='currentColor'>12 &gt; 10</text>
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
