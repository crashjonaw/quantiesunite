SECTIONS = [
    {
        "title": "Cubic Functions",
        "body": """
<h3>The Cubic Function</h3>
<p>A cubic function has the form: \\(y = ax^3 + bx^2 + cx + d\\)</p>
<p>Its graph has a characteristic S-shape.</p>

<h3>Key Properties</h3>
<ul>
  <li>If \\(a > 0\\): Graph goes from bottom-left to top-right (↗↗)</li>
  <li>If \\(a < 0\\): Graph goes from top-left to bottom-right (↖↖)</li>
  <li>Cubic functions can have 1, 2, or 3 real roots</li>
  <li>Always has at least one real root (odd-degree polynomial)</li>
  <li>The graph has two turning points (one local max, one local min)</li>
</ul>

<div class="example-box">
<h4>Example 1: Analyzing \\(y = x^3 - 3x\\)</h4>
<p><strong>y-intercept:</strong> Set \\(x = 0\\) → \\(y = 0\\)</p>
<p><strong>Roots:</strong> Set \\(y = 0\\) → \\(x(x^2 - 3) = 0\\) → \\(x = 0, \\pm\\sqrt{3}\\)</p>
<p><strong>Turning points:</strong> Found using calculus (derivative = 0)</p>
<p>\\(\\frac{dy}{dx} = 3x^2 - 3 = 0\\) → \\(x = \\pm 1\\)</p>
</div>

<svg viewBox="0 0 390 290" class="worked-example">
  <!-- Axes -->
  <line x1="30" y1="145" x2="360" y2="145" stroke='#30363d' stroke-width="1" />
  <line x1="195" y1="15" x2="195" y2="275" stroke='#30363d' stroke-width="1" />
  <!-- Cubic S-curve y = x^3 - 3x -->
  <path d="M 50 260 Q 120 200, 145 145 Q 170 100, 195 145 Q 220 190, 245 145 Q 270 90, 340 30" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Origin point -->
  <circle cx="195" cy="145" r="3" fill='#79c0ff' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='12' fill='currentColor'>
    <text x="365" y="149">x</text>
    <text x="187" y="12">y</text>
    <text x="200" y="162">O</text>
    <text x="280" y="30" fill='#ffa657' font-size='11'>y = x&#xB3; &#x2212; 3x</text>
  </g>
</svg>

<h3>Sketching Tips for Cubics</h3>
<ol>
  <li>Check the sign of \\(a\\) to determine overall direction</li>
  <li>Find all real roots</li>
  <li>Find the y-intercept</li>
  <li>Identify turning points (requires calculus or using a table)</li>
  <li>Draw smooth S-curve through these points</li>
</ol>

<h3>Special Case: \\(y = x^3\\)</h3>
<p>Passes through origin, symmetric about the origin (odd function: \\(f(-x) = -f(x)\\))</p>
"""
    },
    {
        "title": "Reciprocal Functions",
        "body": """
<h3>Reciprocal Functions</h3>
<p>The simplest reciprocal function is: \\(y = \\frac{1}{x}\\)</p>
<p>Its graph has two separate branches called a <strong>hyperbola</strong>.</p>

<h3>Key Features of \\(y = \\frac{1}{x}\\)</h3>
<ul>
  <li><strong>Domain:</strong> All real numbers except \\(x = 0\\)</li>
  <li><strong>Range:</strong> All real numbers except \\(y = 0\\)</li>
  <li><strong>Asymptotes:</strong> \\(x = 0\\) (vertical) and \\(y = 0\\) (horizontal)</li>
  <li>Curve in Quadrant I (both positive) and Quadrant III (both negative)</li>
  <li>Odd function: symmetric about the origin</li>
  <li>As \\(x \\to \\infty\\), \\(y \\to 0\\); as \\(x \\to 0^+\\), \\(y \\to \\infty\\)</li>
</ul>

<svg viewBox="0 0 390 290" class="worked-example">
  <!-- Axes (solid) -->
  <line x1="30" y1="145" x2="360" y2="145" stroke='#30363d' stroke-width="1" />
  <line x1="195" y1="15" x2="195" y2="275" stroke='#30363d' stroke-width="1" />
  <!-- Hyperbola y = 1/x: Quadrant I branch -->
  <path d="M 210 55 Q 230 95, 260 120 Q 300 138, 355 142" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Hyperbola y = 1/x: Quadrant III branch -->
  <path d="M 180 235 Q 160 195, 130 170 Q 90 152, 35 148" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Origin label -->
  <circle cx="195" cy="145" r="2" fill='currentColor' />
  <!-- Asymptote labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="365" y="149">x</text>
    <text x="187" y="12">y</text>
    <text x="200" y="162">O</text>
    <text x="200" y="27" fill='currentColor' opacity='0.6' font-size='10'>x = 0 (asymptote)</text>
    <text x="280" y="138" fill='currentColor' opacity='0.6' font-size='10'>y = 0</text>
    <text x="270" y="75" fill='#58a6ff'>y = 1/x</text>
  </g>
</svg>

<div class="example-box">
<h4>Example 2: Analyzing \\(y = \\frac{1}{x-2} + 1\\)</h4>
<p><strong>Vertical asymptote:</strong> \\(x = 2\\)</p>
<p><strong>Horizontal asymptote:</strong> \\(y = 1\\)</p>
<p>The graph is shifted right 2 and up 1 from \\(y = \\frac{1}{x}\\)</p>
</div>

<h3>General Reciprocal Functions</h3>
<p>\\(y = \\frac{a}{x-h} + k\\) has:</p>
<ul>
  <li>Vertical asymptote at \\(x = h\\)</li>
  <li>Horizontal asymptote at \\(y = k\\)</li>
  <li>Branches in opposite corners of the asymptote rectangle</li>
</ul>
"""
    },
    {
        "title": "Exponential Functions",
        "body": """
<h3>Exponential Functions</h3>
<p>Exponential functions have the form: \\(y = a^x\\) where \\(a > 0\\) and \\(a \\neq 1\\)</p>
<p>Common base: \\(a = e \\approx 2.718\\) (natural exponential: \\(y = e^x\\)) or \\(a = 2\\) (\\(y = 2^x\\))</p>

<h3>Key Properties</h3>
<ul>
  <li><strong>Domain:</strong> All real numbers</li>
  <li><strong>Range:</strong> All positive numbers \\((0, \\infty)\\)</li>
  <li><strong>y-intercept:</strong> \\((0, 1)\\) always, since \\(a^0 = 1\\)</li>
  <li><strong>Horizontal asymptote:</strong> \\(y = 0\\) (the x-axis)</li>
  <li>If \\(a > 1\\): Curve increases (exponential growth)</li>
  <li>If \\(0 < a < 1\\): Curve decreases (exponential decay)</li>
</ul>

<svg viewBox="0 0 400 290" class="worked-example">
  <!-- Axes -->
  <line x1="50" y1="245" x2="370" y2="245" stroke='#30363d' stroke-width="1" />
  <line x1="170" y1="15" x2="170" y2="270" stroke='#30363d' stroke-width="1" />
  <!-- Horizontal asymptote y = 0 (dashed) -->
  <line x1="50" y1="245" x2="370" y2="245" stroke='#8b949e' stroke-width="1" stroke-dasharray="4,4" />
  <!-- Growth curve a > 1 -->
  <path d="M 50 235 Q 100 230, 140 210 Q 170 180, 200 120 Q 230 60, 260 35 Q 300 20, 360 15" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Decay curve 0 < a < 1 -->
  <path d="M 50 15 Q 80 20, 110 35 Q 140 60, 170 120 Q 200 180, 230 210 Q 270 230, 360 235" stroke='#ffa657' stroke-width="2" fill='none' />
  <!-- Intersection point (0, 1) -->
  <circle cx="170" cy="180" r="4" fill='#79c0ff' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="375" y="249">x</text>
    <text x="162" y="12">y</text>
    <text x="175" y="260">O</text>
    <text x="145" y="178" fill='#79c0ff'>(0, 1)</text>
    <text x="270" y="30" fill='#58a6ff'>a &gt; 1 (growth)</text>
    <text x="230" y="270" fill='#ffa657'>0 &lt; a &lt; 1 (decay)</text>
  </g>
</svg>

<div class="example-box">
<h4>Example 3: Growth and Decay</h4>
<p><strong>Bacteria culture:</strong> \\(N = 100 \\times 2^t\\) where \\(t\\) is time in hours</p>
<p>\\(a = 2 > 1\\) means the population doubles each hour.</p>
<p><strong>Radioactive decay:</strong> \\(M = M_0 \\times (\\frac{1}{2})^t\\)</p>
<p>\\(a = \\frac{1}{2} < 1\\) means the mass halves each time period.</p>
</div>

<h3>Solving Exponential Equations</h3>
<p>\\(2^x = 8\\) → \\(2^x = 2^3\\) → \\(x = 3\\)</p>
<p>\\(3^x = 10\\) → Take logarithm: \\(x = \\frac{\\log 10}{\\log 3}\\)</p>
"""
    },
    {
        "title": "Trigonometric Functions",
        "body": """
<h3>Sine and Cosine Functions</h3>
<p>\\(y = \\sin x\\) and \\(y = \\cos x\\) where \\(x\\) is in radians</p>

<h3>Key Properties of \\(y = \\sin x\\)</h3>
<ul>
  <li><strong>Domain:</strong> All real numbers</li>
  <li><strong>Range:</strong> \\([-1, 1]\\)</li>
  <li><strong>Period:</strong> \\(2\\pi\\) (repeats every \\(2\\pi\\) units)</li>
  <li>y-intercept: \\((0, 0)\\)</li>
  <li>Zeros at \\(x = n\\pi\\) (where \\(n\\) is any integer)</li>
  <li>Maximum value 1 at \\(x = \\frac{\\pi}{2}, \\frac{5\\pi}{2}, ...\\)</li>
  <li>Minimum value −1 at \\(x = \\frac{3\\pi}{2}, \\frac{7\\pi}{2}, ...\\)</li>
</ul>

<svg viewBox="0 0 400 270" class="worked-example">
  <!-- Axes -->
  <line x1="40" y1="135" x2="370" y2="135" stroke='#30363d' stroke-width="1" />
  <line x1="40" y1="30" x2="40" y2="240" stroke='#30363d' stroke-width="1" />
  <!-- Amplitude guides (dashed) -->
  <line x1="40" y1="55" x2="370" y2="55" stroke='#8b949e' stroke-width="0.5" stroke-dasharray="3,3" />
  <line x1="40" y1="215" x2="370" y2="215" stroke='#8b949e' stroke-width="0.5" stroke-dasharray="3,3" />
  <!-- Sine wave: 2.5 full periods -->
  <path d="M 40 135 Q 60 75, 80 55 Q 100 35, 120 55 Q 140 75, 160 135 Q 180 195, 200 215 Q 220 235, 240 215 Q 260 195, 280 135 Q 300 75, 320 55 Q 340 35, 360 55" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Tick marks on x-axis -->
  <line x1="120" y1="131" x2="120" y2="139" stroke='#30363d' stroke-width="1" />
  <line x1="200" y1="131" x2="200" y2="139" stroke='#30363d' stroke-width="1" />
  <line x1="280" y1="131" x2="280" y2="139" stroke='#30363d' stroke-width="1" />
  <line x1="360" y1="131" x2="360" y2="139" stroke='#30363d' stroke-width="1" />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='10' fill='currentColor'>
    <text x="375" y="139">x</text>
    <text x="33" y="25">y</text>
    <text x="28" y="148">O</text>
    <text x="20" y="59">1</text>
    <text x="14" y="219">&#x2212;1</text>
    <text x="108" y="152" fill='#79c0ff'>&#x3C0;/2</text>
    <text x="195" y="152" fill='#79c0ff'>&#x3C0;</text>
    <text x="264" y="152" fill='#79c0ff'>3&#x3C0;/2</text>
    <text x="350" y="152" fill='#79c0ff'>2&#x3C0;</text>
    <text x="280" y="45" fill='#58a6ff'>y = sin x</text>
  </g>
</svg>

<h3>Key Differences: \\(y = \\cos x\\)</h3>
<ul>
  <li>Same amplitude (−1 to 1) and period (\\(2\\pi\\))</li>
  <li>y-intercept: \\((0, 1)\\) instead of \\((0, 0)\\)</li>
  <li>Maximum at \\(x = 0, 2\\pi, 4\\pi, ...\\)</li>
  <li>Sine and cosine are vertical shifts of each other: \\(\\cos x = \\sin(x + \\frac{\\pi}{2})\\)</li>
</ul>

<div class="example-box">
<h4>Example 4: Trigonometric Transformations</h4>
<p>\\(y = 2\\sin(x - \\frac{\\pi}{4})\\)</p>
<p>Amplitude: 2 (twice as tall)</p>
<p>Period: \\(2\\pi\\) (unchanged)</p>
<p>Phase shift: Right by \\(\\frac{\\pi}{4}\\)</p>
</div>

<h3>Tangent Function</h3>
<p>\\(y = \\tan x = \\frac{\\sin x}{\\cos x}\\)</p>
<ul>
  <li>Period: \\(\\pi\\) (shorter than sine/cosine)</li>
  <li>Vertical asymptotes at \\(x = \\frac{\\pi}{2}, \\frac{3\\pi}{2}, ...\\)</li>
  <li>Passes through the origin</li>
</ul>
"""
    }
]
