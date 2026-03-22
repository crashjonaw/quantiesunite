SECTIONS = [
    {
        "title": "Domain and Range: First Principles",
        "body": """
<h3>Fundamental Definition</h3>
<p>A <strong>function</strong> is a relation <span class="formula">\\( f: X \\to Y \\)</span> where each element of the domain <span class="formula">\\( X \\)</span> maps to exactly one element in the codomain <span class="formula">\\( Y \\)</span>. The <strong>domain</strong> is the set of all permissible inputs; the <strong>range</strong> (or image) is the set of values actually attained.</p>

<div class="formula-box">
<h4>Formal Definition</h4>
<p>For <span class="formula">\\( f: X \\to Y \\)</span>:</p>
<ul>
<li><strong>Domain:</strong> <span class="formula">\\( D_f = X \\)</span></li>
<li><strong>Range:</strong> <span class="formula">\\( R_f = \\{ y \\in Y : \\exists x \\in X, f(x) = y \\} \\)</span></li>
</ul>
</div>

<h3>Finding Domain: Exclusion Rules</h3>
<p>The natural domain of a real function is \\(\\mathbb{R}\\) except where the function becomes undefined:</p>

<ol>
<li><strong>Rational functions:</strong> Exclude zeros of denominator
$$\\frac{p(x)}{q(x)} \\text{ undefined when } q(x) = 0$$</li>
<li><strong>Even roots:</strong> Radicand must be non-negative
$$\\sqrt[2n]{f(x)} \\text{ requires } f(x) \\geq 0$$</li>
<li><strong>Logarithms:</strong> Argument must be strictly positive
$$\\log f(x) \\text{ requires } f(x) > 0$$</li>
<li><strong>Inverse trig:</strong> Argument restricted to specific intervals
$$\\arcsin(f(x)) \\text{ requires } -1 \\leq f(x) \\leq 1$$</li>
</ol>

<div class="example-box">
<h4>Example 1: Domain of Composite Restriction</h4>
<p><strong>Find domain of:</strong> \\( f(x) = \\sqrt{\\frac{x+2}{x-3}} \\)</p>
<p><strong>Solution:</strong></p>
<ol>
<li>Denominator: \\( x \\neq 3 \\)</li>
<li>Radicand non-negative: \\( \\frac{x+2}{x-3} \\geq 0 \\)</li>
</ol>
<p>Sign analysis of \\( \\frac{x+2}{x-3} \\):</p>
<table style="margin: 10px auto; border-collapse: collapse;">
<tr style="border-bottom: 1px solid #ccc;"><td><strong>Interval</strong></td><td><strong>\\( x+2 \\)</strong></td><td><strong>\\( x-3 \\)</strong></td><td><strong>Quotient</strong></td></tr>
<tr style="border-bottom: 1px solid #ccc;"><td>\\( x < -2 \\)</td><td>\\( - \\)</td><td>\\( - \\)</td><td>\\( + \\)</td></tr>
<tr style="border-bottom: 1px solid #ccc;"><td>\\( -2 < x < 3 \\)</td><td>\\( + \\)</td><td>\\( - \\)</td><td>\\( - \\)</td></tr>
<tr style="border-bottom: 1px solid #ccc;"><td>\\( x > 3 \\)</td><td>\\( + \\)</td><td>\\( + \\)</td><td>\\( + \\)</td></tr>
</table>
<p><strong>Answer:</strong> \\( D_f = (-\\infty, -2] \\cup (3, \\infty) \\)</p>
</div>

<h3>Finding Range: Algebraic Approach</h3>
<p><strong>Method:</strong> Set \\( y = f(x) \\) and solve for \\( x \\) in terms of \\( y \\). Determine which \\( y \\)-values admit real solutions for \\( x \\) in the domain.</p>

<div class="example-box">
<h4>Example 2: Range via Algebraic Manipulation</h4>
<p><strong>Find range of:</strong> \\( f(x) = \\frac{2x-1}{x+1}, \\quad x \\in \\mathbb{R} \\setminus \\{-1\\} \\)</p>
<p><strong>Solution:</strong></p>
<p>Set \\( y = \\frac{2x-1}{x+1} \\):</p>
$$y(x+1) = 2x - 1$$
$$yx + y = 2x - 1$$
$$yx - 2x = -1 - y$$
$$x(y - 2) = -1 - y$$
$$x = \\frac{-1-y}{y-2} = \\frac{y+1}{2-y}$$
<p>This is defined for all \\( y \\neq 2 \\).</p>
<p><strong>Answer:</strong> \\( R_f = \\mathbb{R} \\setminus \\{2\\} \\) or \\( (-\\infty, 2) \\cup (2, \\infty) \\)</p>
</div>

<h3>Finding Range: Calculus Approach</h3>
<p>For continuous functions on a domain, find critical points using derivatives to locate extrema:</p>
<ol>
<li>Solve \\( f'(x) = 0 \\) for critical points</li>
<li>Evaluate \\( f \\) at critical points and boundary points</li>
<li>Consider limits as \\( x \\to \\pm\\infty \\)</li>
<li>Range = union of all extremal values and limiting behaviour</li>
</ol>

<div class="example-box">
<h4>Example 3: Range via Calculus</h4>
<p><strong>Find range of:</strong> \\( f(x) = x^2 - 4x + 3 \\) on \\( \\mathbb{R} \\)</p>
<p><strong>Solution:</strong></p>
<p>Complete the square: \\( f(x) = (x-2)^2 - 1 \\)</p>
<p>Minimum occurs at \\( x = 2 \\): \\( f(2) = -1 \\)</p>
<p>As \\( x \\to \\pm\\infty \\): \\( f(x) \\to \\infty \\)</p>
<p><strong>Answer:</strong> \\( R_f = [-1, \\infty) \\)</p>
</div>

<h3>Restricted Domains and Ranges</h3>
<p>When a function is defined on a restricted domain, its range is determined by the function's behaviour on that restriction only.</p>

<div class="concept-box">
<h4>Key Principle</h4>
<p>If \\( f: A \\to B \\) where \\( A \\subsetneq \\mathbb{R} \\), then:
$$R_f = f(A) = \\{ f(x) : x \\in A \\}$$
depends critically on the domain restriction.</p>
</div>

<div class="example-box">
<h4>Example 4: Restricted Domain Impact</h4>
<p>Consider \\( f(x) = x^2 \\):</p>
<ul>
<li>On \\( \\mathbb{R} \\): range is \\( [0, \\infty) \\)</li>
<li>On \\( [1, 3] \\): range is \\( [1, 9] \\)</li>
<li>On \\( [-2, 0] \\): range is \\( [0, 4] \\)</li>
</ul>
</div>

<h3>Summary: Domain and Range Checklist</h3>
<table style="margin: 15px auto; border-collapse: collapse; width: 90%;">
<tr style="background-color: #f0f0f0; border-bottom: 2px solid #333;">
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Function Type</strong></td>
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Domain Restriction</strong></td>
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Range Finding Method</strong></td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">Polynomial</td>
<td style="padding: 10px; border: 1px solid #ccc;">None (\\( \\mathbb{R} \\))</td>
<td style="padding: 10px; border: 1px solid #ccc;">Calculus/Graphing</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">Rational</td>
<td style="padding: 10px; border: 1px solid #ccc;">Exclude denominator zeros</td>
<td style="padding: 10px; border: 1px solid #ccc;">Algebraic or asymptote analysis</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">Radical (even)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Radicand \\( \\geq 0 \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">From radicand range; always \\( \\geq 0 \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">Logarithmic</td>
<td style="padding: 10px; border: 1px solid #ccc;">Argument \\( > 0 \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">\\( \\mathbb{R} \\) (surjective)</td>
</tr>
</table>
"""
    },
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
<h4>Example 5: Finding Inverse (Linear)</h4>
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
<h4>Example 6: Inverse of Rational Function</h4>
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
<svg width="400" height="400" viewBox="0 0 400 400" style="border: 1px solid #ccc; background: #fafafa;">
<defs>
<style>
.axis { stroke: #000; stroke-width: 1; }
.gridline { stroke: #e0e0e0; stroke-width: 0.5; }
.curve { stroke: #2563eb; stroke-width: 2; fill: none; }
.inverse { stroke: #dc2626; stroke-width: 2; fill: none; }
.diag { stroke: #666; stroke-width: 1.5; stroke-dasharray: 5,5; }
.label { font-family: serif; font-size: 12px; }
</style>
</defs>
<g class="gridline">
<line x1="50" y1="200" x2="350" y2="200" />
<line x1="200" y1="50" x2="200" y2="350" />
</g>
<g class="axis">
<line x1="30" y1="200" x2="370" y2="200" stroke-width="2" />
<line x1="200" y1="30" x2="200" y2="370" stroke-width="2" />
<text x="360" y="195" class="label">x</text>
<text x="205" y="30" class="label">y</text>
</g>
<g class="diag">
<line x1="50" y1="350" x2="350" y2="50" />
<text x="320" y="80" class="label" fill="#666">y = x</text>
</g>
<g class="curve">
<path d="M 100 320 Q 150 250, 200 200 Q 250 150, 300 100" />
<text x="310" y="100" class="label" fill="#2563eb">f</text>
</g>
<g class="inverse">
<path d="M 320 100 Q 250 150, 200 200 Q 150 250, 100 320" />
<text x="110" y="320" class="label" fill="#dc2626">f⁻¹</text>
</g>
<circle cx="250" cy="150" r="3" fill="#2563eb" />
<circle cx="150" cy="250" r="3" fill="#dc2626" />
<line x1="250" y1="150" x2="150" y2="250" stroke="#999" stroke-width="1" stroke-dasharray="3,3" />
</svg>
<p style="font-size: 12px; color: #666;"><em>Red curve (f⁻¹) is reflection of blue curve (f) across y = x</em></p>
</div>

<h3>Horizontal Line Test</h3>
<p>A function is injective (has an inverse) if and only if every horizontal line intersects its graph at most once.</p>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>A function like \\( f(x) = x^2 \\) on \\( \\mathbb{R} \\) is NOT injective because \\( f(-2) = f(2) = 4 \\). However, \\( f: [0, \\infty) \\to [0, \\infty) \\) defined by \\( f(x) = x^2 \\) IS bijective and has inverse \\( f^{-1}(x) = \\sqrt{x} \\).</p>
</div>
"""
    },
    {
        "title": "Composite Functions: Properties and Calculus",
        "body": """
<h3>Definition of Function Composition</h3>
<p>Given functions \\( f: Y \\to Z \\) and \\( g: X \\to Y \\), their <strong>composition</strong> is:</p>

<div class="formula-box">
<h4>Composition Formula</h4>
$$(f \\circ g)(x) = f(g(x))$$
<p><strong>Domain:</strong> \\( D_{f \\circ g} = \\{ x \\in D_g : g(x) \\in D_f \\} \\)</p>
<p>Apply \\( g \\) first, then \\( f \\) to the result.</p>
</div>

<h3>Composition is Non-Commutative</h3>

<div class="example-box">
<h4>Example 7: Order Matters</h4>
<p><strong>Let:</strong> \\( f(x) = x^2 + 1 \\) and \\( g(x) = 2x - 3 \\)</p>
<p><strong>Compute:</strong> \\( (f \\circ g)(x) \\) and \\( (g \\circ f)(x) \\)</p>
<p><strong>Solution:</strong></p>
<p>\\( (f \\circ g)(x) = f(g(x)) = f(2x-3) = (2x-3)^2 + 1 = 4x^2 - 12x + 9 + 1 = 4x^2 - 12x + 10 \\)</p>
<p>\\( (g \\circ f)(x) = g(f(x)) = g(x^2+1) = 2(x^2+1) - 3 = 2x^2 + 2 - 3 = 2x^2 - 1 \\)</p>
<p>Clearly \\( f \\circ g \\neq g \\circ f \\). Composition <strong>is not commutative</strong>.</p>
</div>

<h3>Associativity of Composition</h3>

<div class="success-box">
<h4>Theorem: Associativity</h4>
<p>For functions \\( f \\), \\( g \\), \\( h \\):</p>
$$(f \\circ g) \\circ h = f \\circ (g \\circ h)$$
<p><strong>Proof:</strong> Both sides evaluate to \\( f(g(h(x))) \\).</p>
</div>

<h3>Inverse of Composition</h3>

<div class="success-box">
<h4>Theorem: Inverse Composition Rule</h4>
<p>If \\( f \\) and \\( g \\) are bijective, then:</p>
$$(f \\circ g)^{-1} = g^{-1} \\circ f^{-1}$$
<p><strong>Proof:</strong> We verify:
$$(g^{-1} \\circ f^{-1}) \\circ (f \\circ g) = g^{-1} \\circ (f^{-1} \\circ f) \\circ g = g^{-1} \\circ \\text{id}_Y \\circ g = g^{-1} \\circ g = \\text{id}_X$$
</p>
</div>

<div class="example-box">
<h4>Example 8: Inverse of Composite</h4>
<p><strong>Given:</strong> \\( f(x) = 2x + 1 \\) and \\( g(x) = x - 3 \\)</p>
<p><strong>Find:</strong> \\( (f \\circ g)^{-1}(x) \\)</p>
<p><strong>Method 1 (Direct):</strong></p>
<p>\\( (f \\circ g)(x) = f(g(x)) = f(x-3) = 2(x-3) + 1 = 2x - 5 \\)</p>
<p>Set \\( y = 2x - 5 \\): \\( x = \\frac{y+5}{2} \\), so \\( (f \\circ g)^{-1}(x) = \\frac{x+5}{2} \\)</p>
<p><strong>Method 2 (Using Rule):</strong></p>
<p>\\( f^{-1}(x) = \\frac{x-1}{2} \\) and \\( g^{-1}(x) = x + 3 \\)</p>
<p>\\( (f \\circ g)^{-1} = g^{-1} \\circ f^{-1}(x) = g^{-1}\\left(\\frac{x-1}{2}\\right) = \\frac{x-1}{2} + 3 = \\frac{x-1+6}{2} = \\frac{x+5}{2} \\)</p>
</div>

<h3>Differentiation of Composite Functions: Chain Rule</h3>

<div class="success-box">
<h4>Theorem: Chain Rule</h4>
<p>If \\( u = g(x) \\) is differentiable at \\( x \\), and \\( y = f(u) \\) is differentiable at \\( u = g(x) \\), then:</p>
$$\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)$$
<p>Or in Leibniz notation:</p>
$$\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$$
</div>

<h3>Proof of Chain Rule</h3>
<p>Let \\( f \\circ g \\) be defined near \\( x \\). Let \\( h = f \\circ g \\). Consider:</p>
$$\\frac{d}{dx}[f(g(x))] = \\lim_{\\Delta x \\to 0} \\frac{f(g(x + \\Delta x)) - f(g(x))}{\\Delta x}$$
<p>Let \\( u = g(x) \\) and \\( \\Delta u = g(x + \\Delta x) - g(x) \\). As \\( \\Delta x \\to 0 \\), \\( \\Delta u \\to 0 \\) (by continuity of \\( g \\)).</p>
$$= \\lim_{\\Delta x \\to 0} \\frac{f(u + \\Delta u) - f(u)}{\\Delta u} \\cdot \\frac{\\Delta u}{\\Delta x}$$
$$= \\lim_{\\Delta u \\to 0} \\frac{f(u + \\Delta u) - f(u)}{\\Delta u} \\cdot \\lim_{\\Delta x \\to 0} \\frac{g(x + \\Delta x) - g(x)}{\\Delta x}$$
$$= f'(u) \\cdot g'(x) = f'(g(x)) \\cdot g'(x)$$

<div class="example-box">
<h4>Example 9: Chain Rule Application</h4>
<p><strong>Differentiate:</strong> \\( y = \\sin(x^3) \\)</p>
<p><strong>Solution:</strong> Let \\( u = x^3 \\), so \\( y = \\sin(u) \\)</p>
$$\\frac{dy}{du} = \\cos(u), \\quad \\frac{du}{dx} = 3x^2$$
$$\\frac{dy}{dx} = \\cos(x^3) \\cdot 3x^2 = 3x^2 \\cos(x^3)$$
</div>
"""
    },
    {
        "title": "Graphical Transformations: Theory and Systematic Analysis",
        "body": """
<h3>Fundamental Transformation Classes</h3>
<p>Given the graph of \\( y = f(x) \\), we can systematically generate new functions via transformations. Each transformation affects the graph in a precise, predictable way.</p>

<h3>Vertical Transformations (Affect \\( y \\)-coordinates)</h3>

<div class="formula-box">
<h4>Vertical Shift</h4>
<p>\\( y = f(x) + k \\) shifts the graph vertically:</p>
<ul>
<li>\\( k > 0 \\): shift UP by \\( k \\) units</li>
<li>\\( k < 0 \\): shift DOWN by \\( |k| \\) units</li>
</ul>
<p><strong>Effect on range:</strong> \\( R_{f+k} = R_f + k = \\{ y + k : y \\in R_f \\} \\)</p>
</div>

<div class="formula-box">
<h4>Vertical Scaling and Reflection</h4>
<p>\\( y = a \\cdot f(x) \\) stretches or compresses vertically:</p>
<ul>
<li>\\( |a| > 1 \\): stretch vertically by factor \\( |a| \\)</li>
<li>\\( 0 < |a| < 1 \\): compress vertically by factor \\( 1/|a| \\)</li>
<li>\\( a < 0 \\): also reflects across \\( x \\)-axis</li>
</ul>
</div>

<h3>Horizontal Transformations (Affect \\( x \\)-coordinates)</h3>

<div class="formula-box">
<h4>Horizontal Shift</h4>
<p>\\( y = f(x - h) \\) shifts the graph horizontally:</p>
<ul>
<li>\\( h > 0 \\): shift RIGHT by \\( h \\) units</li>
<li>\\( h < 0 \\): shift LEFT by \\( |h| \\) units</li>
</ul>
<p><strong>Key insight:</strong> \\( f(x - h) \\) means "the value at \\( x \\) is what \\( f \\) had at \\( x - h \\)", so the graph shifts right.</p>
</div>

<div class="formula-box">
<h4>Horizontal Scaling and Reflection</h4>
<p>\\( y = f(bx) \\) compresses or stretches horizontally:</p>
<ul>
<li>\\( |b| > 1 \\): compress horizontally by factor \\( 1/|b| \\)</li>
<li>\\( 0 < |b| < 1 \\): stretch horizontally by factor \\( 1/|b| \\)</li>
<li>\\( b < 0 \\): also reflects across \\( y \\)-axis</li>
</ul>
</div>

<h3>General Transformation Composition</h3>

<div class="formula-box">
<h4>Standard Form</h4>
$$y = a \\cdot f\\left(b(x - h)\\right) + k$$
<p><strong>Order of operations:</strong></p>
<ol>
<li>Apply \\( f \\) to \\( bx \\) (horizontal scaling \\( b \\))</li>
<li>Apply \\( f(b(\\cdot)) \\) to \\( (x - h) \\) (horizontal shift \\( h \\))</li>
<li>Multiply by \\( a \\) (vertical scaling \\( a \\))</li>
<li>Add \\( k \\) (vertical shift \\( k \\))</li>
</ol>
</div>

<div class="example-box">
<h4>Example 10: Complex Transformation Sequence</h4>
<p><strong>Describe transformations from \\( y = \\sqrt{x} \\) to \\( y = -2\\sqrt{3(x-1)} + 4 \\)</strong></p>
<p><strong>Rewrite in standard form:</strong> \\( y = -2\\sqrt{3}\\sqrt{x-1} + 4 \\)</p>
<p><strong>Transformations (reading inside-out):</strong></p>
<ol>
<li>Shift RIGHT by 1: \\( \\sqrt{x-1} \\)</li>
<li>Compress horizontally by \\( 1/\\sqrt{3} \\approx 0.577 \\): \\( \\sqrt{3(x-1)} \\)</li>
<li>Stretch vertically by 2: \\( 2\\sqrt{3(x-1)} \\)</li>
<li>Reflect across \\( x \\)-axis: \\( -2\\sqrt{3(x-1)} \\)</li>
<li>Shift UP by 4: \\( -2\\sqrt{3(x-1)} + 4 \\)</li>
</ol>
</div>

<h3>Reflections</h3>

<div class="formula-box">
<h4>Three Types of Reflection</h4>
<ul>
<li><strong>Across \\( x \\)-axis:</strong> \\( y = -f(x) \\)</li>
<li><strong>Across \\( y \\)-axis:</strong> \\( y = f(-x) \\)</li>
<li><strong>Across \\( y = x \\):</strong> \\( y = f^{-1}(x) \\)</li>
</ul>
</div>

<div class="example-box">
<h4>Example 11: Reflection Mechanics</h4>
<p><strong>Graph of \\( f(x) = |x| \\):</strong></p>
<ul>
<li>Reflect across \\( x \\)-axis: \\( y = -|x| \\)</li>
<li>Reflect across \\( y \\)-axis: \\( y = |-x| = |x| \\) (even function, unchanged)</li>
<li>Reflect across \\( y = x \\): \\( y = |x|^{-1} \\) is not a function (fails horizontal line test)</li>
</ul>
</div>

<h3>Effect of Transformations on Key Features</h3>

<table style="margin: 15px auto; border-collapse: collapse; width: 95%;">
<tr style="background-color: #f0f0f0; border-bottom: 2px solid #333;">
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Transformation</strong></td>
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Domain</strong></td>
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Range</strong></td>
<td style="padding: 10px; border: 1px solid #ccc;"><strong>Asymptotes</strong></td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">\\( f(x) + k \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Unchanged</td>
<td style="padding: 10px; border: 1px solid #ccc;">Shift by \\( k \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Horiz. unch.; vert. shift \\( k \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">\\( a \\cdot f(x) \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Unchanged</td>
<td style="padding: 10px; border: 1px solid #ccc;">Scale by \\( |a| \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Vert. unch.; vert. asymptotes scale \\( |a| \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">\\( f(x-h) \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Shift by \\( h \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Unchanged</td>
<td style="padding: 10px; border: 1px solid #ccc;">Shift by \\( h \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px; border: 1px solid #ccc;">\\( f(bx) \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Scale by \\( 1/|b| \\)</td>
<td style="padding: 10px; border: 1px solid #ccc;">Unchanged</td>
<td style="padding: 10px; border: 1px solid #ccc;">Vert. unch.; scale \\( x \\) by \\( 1/|b| \\)</td>
</tr>
</table>
"""
    },
    {
        "title": "Asymptotes and Advanced Curve Sketching",
        "body": """
<h3>Classification of Asymptotes</h3>
<p>An <strong>asymptote</strong> is a line that a curve approaches arbitrarily closely as one variable increases or decreases without bound. Formally:</p>

<div class="formula-box">
<h4>Asymptote Definition</h4>
<p>A line \\( L \\) is an asymptote to the curve \\( y = f(x) \\) if:</p>
$$\\lim_{x \\to a^+} \\text{(distance from curve to } L) = 0$$
<p>or similarly as \\( x \\to \\pm\\infty \\).</p>
</div>

<h3>Vertical Asymptotes: Poles of Rational Functions</h3>

<div class="formula-box">
<h4>Vertical Asymptote Test</h4>
<p>For rational \\( f(x) = \\frac{p(x)}{q(x)} \\):</p>
<p>\\( x = a \\) is a vertical asymptote if:</p>
<ul>
<li>\\( q(a) = 0 \\) AND</li>
<li>\\( p(a) \\neq 0 \\) (simple pole, not cancellable zero)</li>
</ul>
</div>

<div class="example-box">
<h4>Example 12: Vertical Asymptotes vs. Removable Discontinuity</h4>
<p><strong>Analyze:</strong> \\( f(x) = \\frac{(x-2)(x+1)}{(x-2)(x-3)} \\)</p>
<p><strong>Solution:</strong></p>
<p>At \\( x = 2 \\): Both numerator and denominator have factor \\( (x-2) \\). Cancel:</p>
$$f(x) = \\frac{x+1}{x-3} \\text{ for } x \\neq 2$$
<p>So \\( x = 2 \\) is a <strong>removable discontinuity (hole)</strong>, not an asymptote.</p>
<p>At \\( x = 3 \\): Denominator zero, numerator \\( \\neq 0 \\). This IS a vertical asymptote.</p>
</div>

<h3>Horizontal Asymptotes: Long-Run Behaviour</h3>

<div class="success-box">
<h4>Theorem: Horizontal Asymptotes for Rational Functions</h4>
<p>For \\( f(x) = \\frac{a_n x^n + \\ldots + a_0}{b_m x^m + \\ldots + b_0} \\):</p>
<table style="margin: 10px auto; border-collapse: collapse;">
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px;"><strong>Case</strong></td>
<td style="padding: 10px;"><strong>Horizontal Asymptote</strong></td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px;">\\( n < m \\)</td>
<td style="padding: 10px;">\\( y = 0 \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px;">\\( n = m \\)</td>
<td style="padding: 10px;">\\( y = \\frac{a_n}{b_m} \\)</td>
</tr>
<tr style="border-bottom: 1px solid #ccc;">
<td style="padding: 10px;">\\( n > m \\)</td>
<td style="padding: 10px;">None (oblique possible)</td>
</tr>
</table>
</div>

<h3>Proof: Horizontal Asymptote (\\( n = m \\))</h3>
<p>For \\( f(x) = \\frac{a_n x^n + a_{n-1}x^{n-1} + \\ldots}{b_n x^n + b_{n-1}x^{n-1} + \\ldots} \\):</p>
$$\\lim_{x \\to \\infty} f(x) = \\lim_{x \\to \\infty} \\frac{a_n x^n(1 + a_{n-1}/(a_n x) + \\ldots)}{b_n x^n(1 + b_{n-1}/(b_n x) + \\ldots)} = \\frac{a_n}{b_n}$$

<div class="example-box">
<h4>Example 13: Horizontal Asymptote Analysis</h4>
<p><strong>Find horizontal asymptotes of:</strong></p>
<ol>
<li>\\( f(x) = \\frac{2x^2 - 3x + 1}{x^2 + x - 5} \\): \\( n = m = 2 \\), so \\( y = \\frac{2}{1} = 2 \\)</li>
<li>\\( g(x) = \\frac{3x + 1}{x^3 - 2x} \\): \\( n = 1 < m = 3 \\), so \\( y = 0 \\)</li>
<li>\\( h(x) = \\frac{x^3 - 1}{2x + 1} \\): \\( n = 3 > m = 1 \\), no horizontal asymptote</li>
</ol>
</div>

<h3>Oblique (Slant) Asymptotes</h3>

<div class="formula-box">
<h4>Oblique Asymptote Condition</h4>
<p>When \\( n = m + 1 \\) (numerator degree exceeds denominator by 1), perform polynomial long division:</p>
$$f(x) = (ax + b) + \\frac{r(x)}{q(x)}$$
<p>where \\( \\deg(r) < \\deg(q) \\). As \\( x \\to \\infty \\), \\( \\frac{r(x)}{q(x)} \\to 0 \\), so \\( y = ax + b \\) is the oblique asymptote.</p>
</div>

<div class="example-box">
<h4>Example 14: Oblique Asymptote Derivation</h4>
<p><strong>Find oblique asymptote of:</strong> \\( f(x) = \\frac{2x^2 + 3x - 1}{x - 1} \\)</p>
<p><strong>Solution (Polynomial Long Division):</strong></p>
<div style="margin: 10px; padding: 10px; background: #f5f5f5; border-left: 3px solid #2563eb;">
<pre>
         2x + 5
        ________
x - 1 | 2x² + 3x - 1
        2x² - 2x
        _________
              5x - 1
              5x - 5
              ______
                   4
</pre>
</div>
<p>Therefore: \\( f(x) = 2x + 5 + \\frac{4}{x-1} \\)</p>
<p>As \\( x \\to \\infty \\): \\( \\frac{4}{x-1} \\to 0 \\)</p>
<p><strong>Oblique asymptote:</strong> \\( y = 2x + 5 \\)</p>
</div>

<h3>Systematic Curve Sketching Protocol</h3>

<div class="steps-container">
<h4>7-Step Curve Sketching Procedure</h4>
<ol>
<li><strong>Domain & Continuity:</strong> Identify excluded points; note vertical asymptotes.</li>
<li><strong>Horizontal/Oblique Asymptotes:</strong> Analyze \\( \\lim_{x \\to \\pm\\infty} f(x) \\)</li>
<li><strong>Intercepts:</strong> Find \\( y \\)-intercept (\\( x = 0 \\)) and \\( x \\)-intercepts (\\( f(x) = 0 \\))</li>
<li><strong>First Derivative \\( f'(x) \\):</strong> Find critical points; determine monotonicity</li>
<li><strong>Local Extrema:</strong> Classify critical points as maxima, minima, or saddle points</li>
<li><strong>Second Derivative \\( f''(x) \\):</strong> Find inflection points; determine concavity</li>
<li><strong>Sketch:</strong> Plot key features; draw smooth curve respecting all asymptotic behaviour</li>
</ol>
</div>

<div class="example-box">
<h4>Example 15: Complete Curve Sketch</h4>
<p><strong>Sketch:</strong> \\( f(x) = \\frac{x}{(x-1)^2} \\)</p>

<p><strong>Step 1 - Domain:</strong> All \\( x \\neq 1 \\). Vertical asymptote at \\( x = 1 \\).</p>

<p><strong>Step 2 - Horizontal Asymptote:</strong> \\( \\lim_{x \\to \\infty} \\frac{x}{(x-1)^2} = \\lim_{x \\to \\infty} \\frac{x}{x^2 - 2x + 1} = 0 \\). Horizontal asymptote: \\( y = 0 \\).</p>

<p><strong>Step 3 - Intercepts:</strong></p>
<ul>
<li>\\( y \\)-intercept: \\( f(0) = 0 \\) → point \\( (0, 0) \\)</li>
<li>\\( x \\)-intercept: \\( f(x) = 0 \\Rightarrow x = 0 \\) → same point</li>
</ul>

<p><strong>Step 4 - First Derivative:</strong></p>
$$f'(x) = \\frac{(x-1)^2 - x \\cdot 2(x-1)}{(x-1)^4} = \\frac{(x-1) - 2x}{(x-1)^3} = \\frac{1 - x}{(x-1)^3} = \\frac{-(x-1)}{(x-1)^3} = \\frac{-1}{(x-1)^2}$$
<p>\\( f'(x) < 0 \\) everywhere defined, so \\( f \\) is strictly decreasing on \\( (-\\infty, 1) \\) and \\( (1, \\infty) \\).</p>

<p><strong>Step 5 - Extrema:</strong> No critical points (\\( f'(x) \\neq 0 \\) anywhere).</p>

<p><strong>Step 6 - Second Derivative:</strong></p>
$$f''(x) = \\frac{d}{dx}\\left[\\frac{-1}{(x-1)^2}\\right] = \\frac{2}{(x-1)^3}$$
<ul>
<li>\\( f''(x) > 0 \\) for \\( x > 1 \\) → concave up on \\( (1, \\infty) \\)</li>
<li>\\( f''(x) < 0 \\) for \\( x < 1 \\) → concave down on \\( (-\\infty, 1) \\)</li>
</ul>

<p><strong>Step 7 - Sketch Summary:</strong></p>
<ul>
<li>Curve passes through origin</li>
<li>Concave down and decreasing on \\( (-\\infty, 1) \\), approaching asymptotes \\( y = 0 \\) and \\( x = 1 \\)</li>
<li>Concave up and decreasing on \\( (1, \\infty) \\), approaching asymptotes \\( y = 0 \\) and \\( x = 1 \\)</li>
</ul>
</div>
"""
    },
    {
        "title": "Piecewise Functions and Absolute Value",
        "body": """
<h3>Piecewise Function Definition</h3>
<p>A <strong>piecewise function</strong> is defined by different formulas on different parts of its domain:</p>

<div class="formula-box">
<h4>General Form</h4>
$$f(x) = \\begin{cases}
f_1(x) & \\text{if } x \\in D_1 \\\\
f_2(x) & \\text{if } x \\in D_2 \\\\
\\vdots & \\vdots \\\\
f_n(x) & \\text{if } x \\in D_n
\\end{cases}$$
<p>where \\( D_1, D_2, \\ldots, D_n \\) partition the domain.</p>
</div>

<h3>Continuity at Transition Points</h3>

<div class="success-box">
<h4>Continuity Condition</h4>
<p>At a transition point \\( x = a \\), \\( f \\) is continuous if:</p>
$$\\lim_{x \\to a^-} f(x) = \\lim_{x \\to a^+} f(x) = f(a)$$
</div>

<div class="example-box">
<h4>Example 16: Checking Continuity at Transition</h4>
<p><strong>Determine continuity of:</strong></p>
$$f(x) = \\begin{cases}
x^2 & \\text{if } x < 2 \\\\
3x - 2 & \\text{if } x \\geq 2
\\end{cases}$$
<p><strong>at \\( x = 2 \\)</strong></p>

<p>\\( \\lim_{x \\to 2^-} f(x) = \\lim_{x \\to 2^-} x^2 = 4 \\)</p>
<p>\\( \\lim_{x \\to 2^+} f(x) = \\lim_{x \\to 2^+} (3x - 2) = 6 - 2 = 4 \\)</p>
<p>\\( f(2) = 3(2) - 2 = 4 \\)</p>
<p><strong>Conclusion:</strong> All three values equal 4, so \\( f \\) is <strong>continuous at \\( x = 2 \\)</strong>.</p>
</div>

<h3>The Absolute Value Function</h3>
<p>The absolute value function is the prototypical piecewise function:</p>

<div class="formula-box">
<h4>Definition</h4>
$$|x| = \\begin{cases}
-x & \\text{if } x < 0 \\\\
x & \\text{if } x \\geq 0
\\end{cases}$$
<p><strong>Key properties:</strong></p>
<ul>
<li>\\( |x| \\geq 0 \\) for all \\( x \\) (range: \\( [0, \\infty) \\))</li>
<li>\\( |x| = |{-x}| \\) (even function)</li>
<li>\\( |xy| = |x||y| \\) (multiplicative)</li>
<li>\\( |x + y| \\leq |x| + |y| \\) (triangle inequality)</li>
</ul>
</div>

<h3>Solving Absolute Value Equations and Inequalities</h3>

<div class="example-box">
<h4>Example 17: Absolute Value Equation</h4>
<p><strong>Solve:</strong> \\( |2x - 3| = 5 \\)</p>
<p><strong>Solution:</strong> The equation \\( |A| = B \\) (where \\( B > 0 \\)) has solutions \\( A = B \\) or \\( A = -B \\).</p>
<p>Case 1: \\( 2x - 3 = 5 \\Rightarrow x = 4 \\)</p>
<p>Case 2: \\( 2x - 3 = -5 \\Rightarrow x = -1 \\)</p>
<p><strong>Answer:</strong> \\( x = -1 \\text{ or } x = 4 \\)</p>
</div>

<div class="example-box">
<h4>Example 18: Absolute Value Inequality</h4>
<p><strong>Solve:</strong> \\( |x - 2| < 3 \\)</p>
<p><strong>Solution:</strong> \\( |A| < B \\) is equivalent to \\( -B < A < B \\).</p>
$$-3 < x - 2 < 3$$
$$-1 < x < 5$$
<p><strong>Answer:</strong> \\( x \\in (-1, 5) \\)</p>
</div>

<h3>Graphing Piecewise and Absolute Value Functions</h3>

<div class="example-box">
<h4>Example 19: Graph Transformation via Absolute Value</h4>
<p><strong>Sketch:</strong> \\( y = |x^2 - 4| \\)</p>
<p><strong>Solution:</strong></p>
<p>First understand \\( g(x) = x^2 - 4 \\):</p>
<ul>
<li>Parabola with vertex \\( (0, -4) \\)</li>
<li>Zeros at \\( x = \\pm 2 \\)</li>
<li>\\( g(x) < 0 \\) for \\( x \\in (-2, 2) \\)</li>
<li>\\( g(x) > 0 \\) for \\( |x| > 2 \\)</li>
</ul>
<p>Taking absolute value:</p>
$$y = |x^2 - 4| = \\begin{cases}
x^2 - 4 & \\text{if } |x| \\geq 2 \\\\
4 - x^2 & \\text{if } |x| < 2
\\end{cases}$$
<p>The parabola below the \\( x \\)-axis (for \\( |x| < 2 \\)) is reflected above it.</p>
<ul>
<li>Vertex of \\( y = |x^2 - 4| \\) is at \\( (0, 4) \\)</li>
<li>Touches \\( x \\)-axis at \\( (\\pm 2, 0) \\)</li>
<li>Range: \\( [0, \\infty) \\)</li>
</ul>
</div>

<h3>Composite Piecewise Functions</h3>

<div class="example-box">
<h4>Example 20: Composition with Absolute Value</h4>
<p><strong>Given:</strong> \\( f(x) = |x| \\) and \\( g(x) = x^2 - 1 \\)</p>
<p><strong>Find:</strong> \\( (f \\circ g)(x) = f(g(x)) = |x^2 - 1| \\)</p>
<p><strong>Solution:</strong></p>
$$f(g(x)) = |x^2 - 1| = \\begin{cases}
x^2 - 1 & \\text{if } x^2 \\geq 1 \\text{ (i.e., } |x| \\geq 1) \\\\
1 - x^2 & \\text{if } x^2 < 1 \\text{ (i.e., } |x| < 1)
\\end{cases}$$
</div>
"""
    },
    {
        "title": "Modulus Function: Behaviour and Applications",
        "body": """
<h3>Modulus Function Extended: Non-Negative Output</h3>
<p>The modulus function \\( |x| \\) extracts "magnitude" or "size" without regard to sign. Generalizing to functions:</p>

<div class="formula-box">
<h4>Modulus of a Function</h4>
$$y = |f(x)| = \\begin{cases}
f(x) & \\text{if } f(x) \\geq 0 \\\\
-f(x) & \\text{if } f(x) < 0
\\end{cases}$$
<p><strong>Range:</strong> \\( [0, \\infty) \\) (always non-negative)</p>
</div>

<h3>Geometric Interpretation: Reflection Above \\( x \\)-Axis</h3>
<p>The graph of \\( y = |f(x)| \\) is obtained from \\( y = f(x) \\) by reflecting any portions below the \\( x \\)-axis upward.</p>

<div class="example-box">
<h4>Example 21: Modulus Function Reflection</h4>
<p><strong>Graph \\( y = |\\sin(x)| \\)</strong></p>
<p><strong>Description:</strong></p>
<ul>
<li>Where \\( \\sin(x) \\geq 0 \\) (i.e., \\( x \\in [0, \\pi] \\) in each period): \\( y = \\sin(x) \\)</li>
<li>Where \\( \\sin(x) < 0 \\) (i.e., \\( x \\in (\\pi, 2\\pi) \\) in each period): \\( y = -\\sin(x) \\)</li>
<li>Net effect: Oscillates between \\( 0 \\) and \\( 1 \\), touching the \\( x \\)-axis at \\( x = n\\pi \\)</li>
<li>Period: \\( \\pi \\) (halved from \\( 2\\pi \\))</li>
<li>Range: \\( [0, 1] \\)</li>
</ul>
</div>

<h3>Analysis of \\( y = |ax + b| \\): Absolute Value Lines</h3>

<div class="example-box">
<h4>Example 22: Absolute Value of Linear Function</h4>
<p><strong>Sketch \\( y = |2x - 4| \\)</strong></p>
<p><strong>Solution:</strong></p>
<p>The line \\( y = 2x - 4 \\) has \\( x \\)-intercept at \\( x = 2 \\).</p>
$$y = |2x - 4| = \\begin{cases}
2x - 4 & \\text{if } x \\geq 2 \\\\
4 - 2x & \\text{if } x < 2
\\end{cases}$$
<p><strong>Key features:</strong></p>
<ul>
<li>V-shaped graph with vertex (corner) at \\( (2, 0) \\)</li>
<li>Left branch (\\( x < 2 \\)): slope \\( -2 \\)</li>
<li>Right branch (\\( x > 2 \\)): slope \\( +2 \\)</li>
<li>Range: \\( [0, \\infty) \\)</li>
</ul>
</div>

<h3>Solving \\( |f(x)| = |g(x)| \\)</h3>

<div class="success-box">
<h4>Theorem: Absolute Value Equality</h4>
$$|f(x)| = |g(x)| \\iff f(x) = g(x) \\text{ or } f(x) = -g(x)$$
</div>

<div class="example-box">
<h4>Example 23: Equation with Two Absolute Values</h4>
<p><strong>Solve:</strong> \\( |x - 1| = |2x + 3| \\)</p>
<p><strong>Solution:</strong></p>
<p><strong>Case 1:</strong> \\( x - 1 = 2x + 3 \\Rightarrow -x = 4 \\Rightarrow x = -4 \\)</p>
<p>Check: \\( |{-4} - 1| = 5 \\) and \\( |2({-4}) + 3| = |{-5}| = 5 \\) ✓</p>
<p><strong>Case 2:</strong> \\( x - 1 = -(2x + 3) \\Rightarrow x - 1 = -2x - 3 \\Rightarrow 3x = -2 \\Rightarrow x = -\\frac{2}{3} \\)</p>
<p>Check: \\( |{-\\frac{2}{3}} - 1| = \\frac{5}{3} \\) and \\( |2({-\\frac{2}{3}}) + 3| = |\\frac{5}{3}| = \\frac{5}{3} \\) ✓</p>
<p><strong>Answer:</strong> \\( x = -4 \\) or \\( x = -\\frac{2}{3} \\)</p>
</div>

<h3>Distances and Absolute Value</h3>

<div class="concept-box">
<h4>Distance Formula</h4>
<p>The distance between \\( a \\) and \\( b \\) on the real line is:</p>
$$d(a, b) = |a - b| = |b - a|$$
</div>

<div class="example-box">
<h4>Example 24: Distance and Absolute Value Inequality</h4>
<p><strong>Describe:</strong> All \\( x \\) within distance 3 of 5</p>
<p><strong>Solution:</strong></p>
$$|x - 5| \\leq 3$$
$$-3 \\leq x - 5 \\leq 3$$
$$2 \\leq x \\leq 8$$
<p><strong>Answer:</strong> \\( x \\in [2, 8] \\)</p>
</div>
"""
    }
]
