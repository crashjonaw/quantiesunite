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

<svg width="400" height="300" class="worked-example">
  <g id="grid">
    <line x1="50" y1="150" x2="350" y2="150" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#30363d' stroke-width="1" />
    <path d="M 50 250 Q 150 100, 200 150 Q 250 200, 350 50" stroke='#58a6ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='12' fill='#e6edf3'>
    <text x="360" y="155">x</text>
    <text x="190" y="40">y</text>
    <text x="200" y="270" fill='#ffa657'>S-shape</text>
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

<svg width="400" height="300" class="worked-example">
  <g id="grid">
    <line x1="50" y1="150" x2="350" y2="150" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
    <line x1="50" y1="150" x2="350" y2="150" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
    <path d="M 230 50 Q 280 90, 340 140" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 170 150 Q 120 110, 60 60" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 170 150 Q 120 190, 60 240" stroke='#ffa657' stroke-width="2" fill='none' />
    <path d="M 230 150 Q 280 210, 340 260" stroke='#ffa657' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='11' fill='#e6edf3'>
    <text x="360" y="155">x</text>
    <text x="190" y="40">y</text>
    <text x="200" y="270">O</text>
    <text x="210" y="35" fill='#8b949e'>x = 0</text>
    <text x="280" y="150" fill='#8b949e'>y = 0</text>
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

<svg width="400" height="300" class="worked-example">
  <g id="grid">
    <line x1="50" y1="250" x2="350" y2="250" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="50" x2="50" y2="250" stroke='#30363d' stroke-width="1" />
    <path d="M 50 240 Q 100 220, 150 180 Q 200 100, 250 50 Q 300 40, 350 35" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 50 50 Q 100 70, 150 110 Q 200 170, 250 220 Q 300 240, 350 245" stroke='#ffa657' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='11' fill='#e6edf3'>
    <text x="360" y="255">x</text>
    <text x="40" y="40">y</text>
    <text x="300" y="30" fill='#58a6ff'>a > 1 (growth)</text>
    <text x="280" y="255" fill='#ffa657'>0 < a < 1 (decay)</text>
    <text x="45" y="265">O</text>
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

<svg width="400" height="280" class="worked-example">
  <g id="grid">
    <line x1="50" y1="140" x2="350" y2="140" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="50" x2="50" y2="230" stroke='#30363d' stroke-width="1" />
    <path d="M 50 140 Q 80 80, 110 140 Q 140 200, 170 140 Q 200 80, 230 140 Q 260 200, 290 140 Q 320 80, 350 140" stroke='#58a6ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='10' fill='#e6edf3'>
    <text x="360" y="145">x</text>
    <text x="40" y="50">y</text>
    <text x="45" y="155">O</text>
    <text x="110" y="35" fill='#79c0ff'>π/2</text>
    <text x="170" y="250" fill='#79c0ff'>π</text>
    <text x="230" y="35" fill='#79c0ff'>3π/2</text>
    <text x="290" y="250" fill='#79c0ff'>2π</text>
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
