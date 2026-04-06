TITLE = "Inverse Functions"

SECTIONS = [
    {
        "title": "Inverse Functions: Theory and Construction",
        "body": """
<h3>Injectivity and Inverse Existence</h3>
<p>A function \\( f: X \\to Y \\) has an inverse if and only if it is <strong>injective (one-to-one)</strong>:</p>

<div class="formula-box">
<h4>Injective Definition</h4>
<p>\\( f \\) is injective \\( \\iff \\) for all \\( x_1, x_2 \\in X \\):</p>
$$f(x_1) = f(x_2) \\implies x_1 = x_2$$
<p>Equivalently: \\( x_1 \\neq x_2 \\implies f(x_1) \\neq f(x_2) \\) (no two inputs map to the same output)</p>
</div>

<h3>Formal Definition of Inverse Function</h3>
<p>If \\( f: X \\to Y \\) is bijective (injective and surjective), then the <strong>inverse function</strong> \\( f^{-1}: Y \\to X \\) satisfies:</p>

<div class="formula-box">
<h4>Inverse Properties</h4>
$$f(f^{-1}(y)) = y \\quad \\forall y \\in Y$$
$$f^{-1}(f(x)) = x \\quad \\forall x \\in X$$
<p>Also: \\( f^{-1} \\) is itself bijective, and \\( (f^{-1})^{-1} = f \\)</p>
</div>

<h3>Theorem: Domain and Range Interchange</h3>

<div class="success-box">
<h4>Key Theorem</h4>
<p>If \\( f: A \\to B \\) is bijective with inverse \\( f^{-1}: B \\to A \\), then:</p>
$$\\text{Domain of } f^{-1} = \\text{Range of } f$$
$$\\text{Range of } f^{-1} = \\text{Domain of } f$$
</div>

<div class="example-box">
<h4>Example 1: Finding Inverse (Linear)</h4>
<p><strong>Given:</strong> \\( f(x) = 3x - 5 \\)</p>
<p><strong>Find:</strong> \\( f^{-1}(x) \\) and verify.</p>
<p><strong>Solution:</strong></p>
<p><strong>Step 1:</strong> Set \\( y = 3x - 5 \\)</p>
<p><strong>Step 2:</strong> Solve for \\( x \\):
$$y + 5 = 3x \\implies x = \\frac{y+5}{3}$$
</p>
<p><strong>Step 3:</strong> Swap variables:
$$f^{-1}(x) = \\frac{x+5}{3}$$
</p>
<p><strong>Verification:</strong></p>
$$f(f^{-1}(x)) = 3 \\cdot \\frac{x+5}{3} - 5 = x + 5 - 5 = x \\quad \\checkmark$$
$$f^{-1}(f(x)) = \\frac{3x - 5 + 5}{3} = \\frac{3x}{3} = x \\quad \\checkmark$$
</div>

<h3>Finding Inverse: Complex Functions</h3>

<div class="example-box">
<h4>Example 2: Inverse of Rational Function</h4>
<p><strong>Find inverse of:</strong> \\( f(x) = \\frac{2x+1}{x-3} \\)</p>
<p><strong>Solution:</strong></p>
<p>Set \\( y = \\frac{2x+1}{x-3} \\):
$$y(x-3) = 2x + 1$$
$$yx - 3y = 2x + 1$$
$$yx - 2x = 3y + 1$$
$$x(y - 2) = 3y + 1$$
$$x = \\frac{3y+1}{y-2}$$
</p>
<p>Therefore: \\( f^{-1}(x) = \\frac{3x+1}{x-2} \\)</p>
<p><strong>Domain of \\( f^{-1}\\):</strong> \\( \\mathbb{R} \\setminus \\{2\\} \\) (equals range of \\( f \\))</p>
</div>

<h3>Graphical Interpretation: Reflection across \\( y = x \\)</h3>
<p>The graph of \\( f^{-1} \\) is the reflection of the graph of \\( f \\) across the line \\( y = x \\).</p>

<div class="concept-box">
<h4>Geometric Principle</h4>
<p>If point \\( (a, b) \\) lies on the graph of \\( f \\), then \\( f(a) = b \\). This means \\( f^{-1}(b) = a \\), so point \\( (b, a) \\) lies on the graph of \\( f^{-1} \\).</p>
<p>The transformation \\( (x, y) \\mapsto (y, x) \\) is reflection across \\( y = x \\).</p>
</div>

<div style="margin: 20px auto; text-align: center;">
<svg width="400" height="400" viewBox="15 15 370 370">
<!-- Axes -->
<line x1="30" y1="200" x2="370" y2="200" stroke="currentColor" stroke-width="1.5" />
<line x1="200" y1="30" x2="200" y2="370" stroke="currentColor" stroke-width="1.5" />
<text x="358" y="192" font-family="serif" font-size="13" fill="currentColor">x</text>
<text x="208" y="42" font-family="serif" font-size="13" fill="currentColor">y</text>
<!-- Diagonal y = x -->
<line x1="50" y1="350" x2="350" y2="50" stroke="currentColor" stroke-width="1" stroke-dasharray="5,5" opacity="0.5" />
<text x="310" y="72" font-family="serif" font-size="12" fill="currentColor" opacity="0.6">y = x</text>
<!-- f curve (blue) -->
<path d="M 100 320 Q 150 250, 200 200 Q 250 150, 300 100" stroke="#2563eb" stroke-width="2" fill="none" />
<text x="310" y="96" font-family="serif" font-size="13" fill="#2563eb">f</text>
<!-- f inverse curve (red) -->
<path d="M 320 100 Q 250 150, 200 200 Q 150 250, 100 320" stroke="#dc2626" stroke-width="2" fill="none" />
<text x="78" y="332" font-family="serif" font-size="13" fill="#dc2626">f⁻¹</text>
<!-- Corresponding points -->
<circle cx="250" cy="150" r="4" fill="#2563eb" />
<circle cx="150" cy="250" r="4" fill="#dc2626" />
<line x1="250" y1="150" x2="150" y2="250" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.4" />
</svg>
<p style="font-size: 12px;"><em>Red curve (f⁻¹) is reflection of blue curve (f) across y = x</em></p>
</div>

<h3>Horizontal Line Test</h3>
<p>A function is injective (has an inverse) if and only if every horizontal line intersects its graph at most once.</p>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>A function like \\( f(x) = x^2 \\) on \\( \\mathbb{R} \\) is NOT injective because \\( f(-2) = f(2) = 4 \\). However, \\( f: [0, \\infty) \\to [0, \\infty) \\) defined by \\( f(x) = x^2 \\) IS bijective and has inverse \\( f^{-1}(x) = \\sqrt{x} \\).</p>
</div>
"""
    }
]
