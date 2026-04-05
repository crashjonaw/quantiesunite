TITLE = "Composite Functions"

SECTIONS = [
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
<h4>Example 1: Order Matters</h4>
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
<h4>Example 2: Inverse of Composite</h4>
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
<h4>Example 3: Chain Rule Application</h4>
<p><strong>Differentiate:</strong> \\( y = \\sin(x^3) \\)</p>
<p><strong>Solution:</strong> Let \\( u = x^3 \\), so \\( y = \\sin(u) \\)</p>
$$\\frac{dy}{du} = \\cos(u), \\quad \\frac{du}{dx} = 3x^2$$
$$\\frac{dy}{dx} = \\cos(x^3) \\cdot 3x^2 = 3x^2 \\cos(x^3)$$
</div>
"""
    }
]
