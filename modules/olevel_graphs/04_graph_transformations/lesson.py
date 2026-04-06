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

<svg viewBox="0 0 400 300" class="worked-example">
  <!-- Axes -->
  <line x1="30" y1="160" x2="370" y2="160" stroke='#30363d' stroke-width="1" />
  <line x1="200" y1="15" x2="200" y2="280" stroke='#30363d' stroke-width="1" />
  <!-- y = x^2 (original) -->
  <path d="M 100 260 Q 150 190, 200 160 Q 250 190, 300 260" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- y = x^2 + 3 (shifted up) -->
  <path d="M 100 230 Q 150 160, 200 130 Q 250 160, 300 230" stroke='#ffa657' stroke-width="2" fill='none' />
  <!-- y = x^2 - 2 (shifted down) -->
  <path d="M 100 280 Q 150 210, 200 185 Q 250 210, 300 280" stroke='#79c0ff' stroke-width="2" fill='none' />
  <!-- Shift arrows -->
  <line x1="200" y1="160" x2="200" y2="132" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
  <line x1="200" y1="160" x2="200" y2="183" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" />
  <!-- Vertex dots -->
  <circle cx="200" cy="160" r="3" fill='#58a6ff' />
  <circle cx="200" cy="130" r="3" fill='#ffa657' />
  <circle cx="200" cy="185" r="3" fill='#79c0ff' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="375" y="164">x</text>
    <text x="192" y="12">y</text>
    <text x="310" y="250" fill='#58a6ff'>y = x&#xB2;</text>
    <text x="310" y="220" fill='#ffa657'>y = x&#xB2; + 3</text>
    <text x="310" y="275" fill='#79c0ff'>y = x&#xB2; &#x2212; 2</text>
  </g>
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

<svg viewBox="0 0 400 300" class="worked-example">
  <!-- Axes -->
  <line x1="15" y1="160" x2="385" y2="160" stroke='#30363d' stroke-width="1" />
  <line x1="200" y1="15" x2="200" y2="280" stroke='#30363d' stroke-width="1" />
  <!-- y = x^2 (original, center) -->
  <path d="M 100 260 Q 150 190, 200 160 Q 250 190, 300 260" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- y = (x+2)^2 (shifted left) -->
  <path d="M 50 260 Q 100 190, 150 160 Q 200 190, 250 260" stroke='#ffa657' stroke-width="2" fill='none' />
  <!-- y = (x-2)^2 (shifted right) -->
  <path d="M 150 260 Q 200 190, 250 160 Q 300 190, 350 260" stroke='#79c0ff' stroke-width="2" fill='none' />
  <!-- Vertex dots -->
  <circle cx="200" cy="160" r="3" fill='#58a6ff' />
  <circle cx="150" cy="160" r="3" fill='#ffa657' />
  <circle cx="250" cy="160" r="3" fill='#79c0ff' />
  <!-- Shift arrows -->
  <line x1="198" y1="163" x2="153" y2="163" stroke='#ffa657' stroke-width="1" stroke-dasharray="3,3" />
  <line x1="202" y1="163" x2="247" y2="163" stroke='#79c0ff' stroke-width="1" stroke-dasharray="3,3" />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="375" y="155">x</text>
    <text x="192" y="12">y</text>
    <text x="302" y="250" fill='#58a6ff'>y = x&#xB2;</text>
    <text x="60" y="250" fill='#ffa657'>left 2</text>
    <text x="310" y="272" fill='#79c0ff'>right 2</text>
  </g>
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

<svg viewBox="0 0 400 290" class="worked-example">
  <!-- Axes -->
  <line x1="30" y1="145" x2="370" y2="145" stroke='#30363d' stroke-width="1" />
  <line x1="200" y1="15" x2="200" y2="275" stroke='#30363d' stroke-width="1" />
  <!-- Original sine wave -->
  <path d="M 50 145 Q 100 55, 200 145 Q 300 235, 350 145" stroke='#58a6ff' stroke-width="2" fill='none' />
  <!-- Compressed f(2x) - narrower -->
  <path d="M 50 145 Q 75 55, 125 145 Q 175 235, 200 145" stroke='#ffa657' stroke-width="2" fill='none' />
  <!-- Stretched f(0.5x) - wider -->
  <path d="M 50 145 Q 150 55, 350 145" stroke='#79c0ff' stroke-width="2" fill='none' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="375" y="149">x</text>
    <text x="192" y="12">y</text>
    <text x="300" y="80" fill='#58a6ff'>f(x)</text>
    <text x="130" y="80" fill='#ffa657'>f(2x)</text>
    <text x="300" y="110" fill='#79c0ff'>f(&#xBD;x)</text>
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

<svg viewBox="0 0 400 310" class="worked-example">
  <!-- Axes -->
  <line x1="30" y1="200" x2="370" y2="200" stroke='#30363d' stroke-width="1" />
  <line x1="70" y1="15" x2="70" y2="295" stroke='#30363d' stroke-width="1" />
  <!-- Original y = x^2 (faded) -->
  <path d="M 30 280 Q 50 230, 70 200 Q 90 230, 110 280" stroke='#58a6ff' stroke-width="2" fill='none' opacity='0.4' />
  <!-- Shifted + stretched y = 2(x-1)^2 -->
  <path d="M 70 280 Q 100 230, 130 200 Q 160 230, 190 280" stroke='#ffa657' stroke-width="2" fill='none' opacity='0.7' />
  <!-- Reflected y = -2(x-1)^2 + 3 -->
  <path d="M 70 80 Q 100 130, 130 155 Q 160 130, 190 80" stroke='#79c0ff' stroke-width="2" fill='none' />
  <!-- Key points -->
  <circle cx="70" cy="200" r="3" fill='#58a6ff' />
  <circle cx="130" cy="200" r="3" fill='#ffa657' />
  <circle cx="130" cy="155" r="4" fill='#79c0ff' />
  <!-- Labels -->
  <g font-family='Arial, sans-serif' font-size='11' fill='currentColor'>
    <text x="375" y="204">x</text>
    <text x="62" y="12">y</text>
    <text x="75" y="215">O</text>
    <text x="115" y="280" fill='#58a6ff'>y = x&#xB2;</text>
    <text x="195" y="270" fill='#ffa657'>Shift + Stretch</text>
    <text x="195" y="100" fill='#79c0ff'>+ Reflect + Shift up</text>
    <text x="138" y="150" fill='#79c0ff'>(1, 3)</text>
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
