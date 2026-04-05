SECTIONS = [
    {
        "title": "Vertical Translations (Shifts)",
        "body": """
<h3>Shifting Graphs Up and Down</h3>
<p>If we have a function \\(y = f(x)\\), then:</p>
<ul>
  <li>\\(y = f(x) + k\\) shifts the graph up by \\(k\\) units (\\(k > 0\\))</li>
  <li>\\(y = f(x) - k\\) shifts the graph down by \\(k\\) units (\\(k > 0\\))</li>
</ul>

<p><strong>Rule:</strong> Adding/subtracting a constant to the whole function moves it vertically.</p>

<div class="example-box">
<h4>Example 1: Vertical Shifts</h4>
<p><strong>Original:</strong> \\(y = x^2\\)</p>
<p><strong>Shift up 3:</strong> \\(y = x^2 + 3\\)</p>
<p><strong>Shift down 2:</strong> \\(y = x^2 - 2\\)</p>
<p>The vertex moves from (0, 0) to (0, 3) or (0, −2), but the shape stays identical.</p>
</div>

<svg width="400" height="320" class="worked-example">
  <g id="grid">
    <line x1="50" y1="160" x2="350" y2="160" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#30363d' stroke-width="1" />
    <path d="M 100 160 Q 200 80, 300 160" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 100 130 Q 200 50, 300 130" stroke='#ffa657' stroke-width="2" fill='none' />
    <path d="M 100 190 Q 200 110, 300 190" stroke='#79c0ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='11' fill='#e6edf3'>
    <text x="360" y="165">x</text>
    <text x="190" y="40">y</text>
    <text x="250" y="90" fill='#58a6ff'>y = x²</text>
    <text x="250" y="60" fill='#ffa657'>y = x² + 3</text>
    <text x="250" y="125" fill='#79c0ff'>y = x² - 2</text>
  </g>
  <line x1="200" y1="160" x2="200" y2="130" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
  <line x1="200" y1="160" x2="200" y2="190" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
</svg>

<h3>Effect on Key Features</h3>
<ul>
  <li>y-intercept moves up/down</li>
  <li>Roots may shift (stay same x-values)</li>
  <li>Shape (curvature, gradient) is unchanged</li>
  <li>Maximum/minimum values shift up/down</li>
</ul>

<h3>General Pattern</h3>
<p>Vertical transformations are done <strong>outside</strong> the function: \\(y = f(x) + c\\)</p>
"""
    },
    {
        "title": "Horizontal Translations (Shifts)",
        "body": """
<h3>Shifting Graphs Left and Right</h3>
<p>If we have a function \\(y = f(x)\\), then:</p>
<ul>
  <li>\\(y = f(x - h)\\) shifts the graph right by \\(h\\) units (\\(h > 0\\))</li>
  <li>\\(y = f(x + h)\\) shifts the graph left by \\(h\\) units (\\(h > 0\\))</li>
</ul>

<p><strong>Important:</strong> The sign is opposite to the direction! \\(f(x - h)\\) shifts RIGHT.</p>

<div class="example-box">
<h4>Example 2: Horizontal Shifts</h4>
<p><strong>Original:</strong> \\(y = (x + 1)^2\\) can be rewritten as \\(y = (x - (-1))^2\\)</p>
<p>This shifts \\(y = x^2\\) LEFT by 1 unit. Vertex is at \\((-1, 0)\\).</p>
<p>\\(y = (x - 2)^2\\) shifts RIGHT by 2 units. Vertex is at \\((2, 0)\\).</p>
</div>

<svg width="400" height="320" class="worked-example">
  <g id="grid">
    <line x1="50" y1="160" x2="350" y2="160" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#30363d' stroke-width="1" />
    <path d="M 100 160 Q 200 80, 300 160" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 50 160 Q 150 80, 250 160" stroke='#ffa657' stroke-width="2" fill='none' />
    <path d="M 150 160 Q 250 80, 350 160" stroke='#79c0ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='11' fill='#e6edf3'>
    <text x="360" y="165">x</text>
    <text x="190" y="40">y</text>
    <text x="250" y="90" fill='#58a6ff'>y = x²</text>
    <text x="100" y="175" fill='#ffa657'>left 2</text>
    <text x="280" y="175" fill='#79c0ff'>right 2</text>
  </g>
  <circle cx="200" cy="160" r="2" fill='#79c0ff' />
  <circle cx="100" cy="160" r="2" fill='#ffa657' />
  <circle cx="300" cy="160" r="2" fill='#79c0ff' />
</svg>

<h3>Effect on Key Features</h3>
<ul>
  <li>Roots shift left/right by the same amount as the translation</li>
  <li>Vertex (for parabolas) shifts left/right</li>
  <li>y-intercept changes</li>
  <li>Shape is completely unchanged</li>
</ul>

<h3>General Pattern</h3>
<p>Horizontal transformations are done <strong>inside</strong> the function: \\(y = f(x - h)\\)</p>
"""
    },
    {
        "title": "Reflections and Stretches",
        "body": """
<h3>Reflections</h3>

<p><strong>Reflection about the x-axis:</strong> \\(y = -f(x)\\)</p>
<p>Flip the entire graph upside down. Every y-value becomes its opposite.</p>

<p><strong>Reflection about the y-axis:</strong> \\(y = f(-x)\\)</p>
<p>Mirror the graph left-to-right. This creates the "opposite x" input.</p>

<div class="example-box">
<h4>Example 3: Reflections</h4>
<p>Original: \\(y = \\sqrt{x}\\) (only for \\(x \\geq 0\\))</p>
<p>Reflect about y-axis: \\(y = \\sqrt{-x}\\) (only for \\(x \\leq 0\\))</p>
<p>Reflect about x-axis: \\(y = -\\sqrt{x}\\) (now below the x-axis)</p>
</div>

<h3>Vertical Stretches and Compressions</h3>
<p>\\(y = af(x)\\) where \\(a > 0\\):</p>
<ul>
  <li>If \\(a > 1\\): Graph stretches vertically (gets taller)</li>
  <li>If \\(0 < a < 1\\): Graph compresses vertically (gets shorter)</li>
</ul>

<p>All y-values are multiplied by \\(a\\).</p>

<div class="example-box">
<h4>Example 4: Vertical Stretch</h4>
<p>\\(y = 2\\sin x\\) is twice as tall as \\(y = \\sin x\\)</p>
<p>\\(y = \\frac{1}{2}x^2\\) is half as tall as \\(y = x^2\\)</p>
</div>

<h3>Horizontal Stretches and Compressions</h3>
<p>\\(y = f(bx)\\) where \\(b > 0\\):</p>
<ul>
  <li>If \\(b > 1\\): Graph compresses horizontally (gets narrower)</li>
  <li>If \\(0 < b < 1\\): Graph stretches horizontally (gets wider)</li>
</ul>

<p>This is the opposite of what you might expect! \\(b = 2\\) makes it <strong>narrower</strong>.</p>

<svg width="420" height="300" class="worked-example">
  <g id="grid">
    <line x1="50" y1="150" x2="350" y2="150" stroke='#30363d' stroke-width="1" />
    <line x1="200" y1="50" x2="200" y2="250" stroke='#30363d' stroke-width="1" />
    <path d="M 50 150 Q 150 80, 250 150 Q 350 220, 350 250" stroke='#58a6ff' stroke-width="2" fill='none' />
    <path d="M 50 150 Q 125 90, 200 150 Q 275 210, 350 250" stroke='#ffa657' stroke-width="2" fill='none' />
    <path d="M 50 150 Q 200 70, 350 150" stroke='#79c0ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='10' fill='#e6edf3'>
    <text x="360" y="155">x</text>
    <text x="190" y="40">y</text>
    <text x="280" y="80" fill='#58a6ff'>original</text>
    <text x="280" y="110" fill='#ffa657'>compress</text>
    <text x="280" y="140" fill='#79c0ff'>stretch</text>
  </g>
</svg>

<div class="example-box">
<h4>Example 5: Horizontal Compression</h4>
<p>\\(y = f(2x)\\) shrinks horizontally by factor of ½</p>
<p>\\(y = f(\\frac{1}{2}x)\\) stretches horizontally by factor of 2</p>
</div>
"""
    },
    {
        "title": "Composite Transformations",
        "body": """
<h3>Combining Multiple Transformations</h3>
<p>A general form: \\(y = af(b(x - h)) + k\\)</p>
<p>This applies transformations in a specific order:</p>
<ol>
  <li><strong>Inside first:</strong> Horizontal shift (\\(x - h\\)) and stretch (\\(b\\))</li>
  <li><strong>Then outside:</strong> Vertical stretch (\\(a\\)) and shift (\\(+k\\))</li>
</ol>

<div class="example-box">
<h4>Example 6: Complete Transformation</h4>
<p><strong>Transform \\(y = x^2\\) into \\(y = -2(x - 1)^2 + 3\\)</strong></p>
<p>Step 1: Start with \\(y = x^2\\)</p>
<p>Step 2: Shift right 1 → \\(y = (x - 1)^2\\)</p>
<p>Step 3: Stretch vertically by 2 → \\(y = 2(x - 1)^2\\)</p>
<p>Step 4: Reflect about x-axis (multiply by −1) → \\(y = -2(x - 1)^2\\)</p>
<p>Step 5: Shift up 3 → \\(y = -2(x - 1)^2 + 3\\)</p>
<p>Vertex: (1, 3) | Opens downward | Narrower than original</p>
</div>

<h3>Order of Transformations (PEMDAS-like)</h3>
<p>When reading \\(y = af(b(x - h)) + k\\):</p>
<ol>
  <li>Apply \\(b\\) (horizontal stretch/compression)</li>
  <li>Apply \\((x - h)\\) (horizontal shift)</li>
  <li>Apply \\(a\\) (vertical stretch/compression and reflection)</li>
  <li>Apply \\(k\\) (vertical shift)</li>
</ol>

<svg width="420" height="340" class="worked-example">
  <g id="grid">
    <line x1="50" y1="260" x2="350" y2="260" stroke='#30363d' stroke-width="1" />
    <line x1="50" y1="60" x2="50" y2="260" stroke='#30363d' stroke-width="1" />
  </g>
  <g id="curves">
    <path d="M 50 260 Q 150 160, 250 60 Q 350 260, 350 260" stroke='#58a6ff' stroke-width="2" fill='none' opacity='0.5' />
    <path d="M 100 260 Q 150 180, 200 140 Q 250 180, 300 260" stroke='#ffa657' stroke-width="2" fill='none' opacity='0.8' />
    <path d="M 100 100 Q 150 80, 200 100 Q 250 140, 300 200" stroke='#79c0ff' stroke-width="2" fill='none' />
  </g>
  <g id="labels" font-family='Arial' font-size='10' fill='#e6edf3'>
    <text x="360" y="265">x</text>
    <text x="40" y="60">y</text>
    <text x="45" y="275">O</text>
    <text x="280" y="150" fill='#58a6ff'>Original</text>
    <text x="260" y="190" fill='#ffa657'>Shift + Stretch</text>
    <text x="240" y="85" fill='#79c0ff'>+ Reflect</text>
  </g>
</svg>

<h3>Reading Transformations from Equations</h3>
<p>Given \\(y = -3(x + 2)^2 - 5\\):</p>
<ul>
  <li>Rewrite: \\(y = -3(x - (-2))^2 + (-5)\\)</li>
  <li>\\(h = -2\\): Shift LEFT by 2</li>
  <li>\\(a = -3\\): Reflect (negative) and stretch by 3</li>
  <li>\\(k = -5\\): Shift DOWN by 5</li>
  <li>Vertex: \\((-2, -5)\\)</li>
</ul>

<h3>Real-World Transformations</h3>
<p>A bouncing ball's height: \\(h(t) = -4.9(t - 0.5)^2 + 1.2\\)</p>
<p>Compared to \\(h = -4.9t^2\\):</p>
<ul>
  <li>Shifted right 0.5 seconds (time of maximum height)</li>
  <li>Maximum height at (0.5, 1.2)</li>
</ul>
"""
    }
]
