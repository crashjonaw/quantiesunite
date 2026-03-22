SECTIONS = [
    {
        "title": "Functions: Definition and Notation",
        "body": """
<h3>Axiomatic Definition of a Function</h3>
<p>A <strong>function</strong> f: A → B is a relation where each element in set A (domain) maps to exactly one element in set B (codomain).</p>
<p>Notation: f(x) = y, read as "f of x equals y"</p>

<p><strong>Key properties:</strong></p>
<ul>
  <li>Every input has exactly one output (vertical line test)</li>
  <li>Domain: Set of all valid inputs</li>
  <li>Range: Set of all actual outputs (⊆ codomain)</li>
  <li>Image: f(x) denotes the output for input x</li>
</ul>

<h3>Domain Restrictions</h3>
<div class="example-box">
<h4>Example 1: Finding Domain</h4>
<p>f(x) = 1/(x-2): Domain is ℝ \\ {2} (all reals except 2)</p>
<p>g(x) = √(x-3): Domain is [3, ∞) (x ≥ 3)</p>
</div>

<h3>Function Families</h3>
<ul>
  <li><strong>Linear:</strong> f(x) = mx + b (straight line)</li>
  <li><strong>Quadratic:</strong> f(x) = ax² + bx + c (parabola)</li>
  <li><strong>Polynomial:</strong> f(x) = aₙxⁿ + ... + a₀</li>
  <li><strong>Rational:</strong> f(x) = p(x)/q(x)</li>
  <li><strong>Exponential:</strong> f(x) = aˣ</li>
  <li><strong>Logarithmic:</strong> f(x) = logₐ(x)</li>
</ul>
"""
    },
    {
        "title": "Linear Functions and Straight Lines",
        "body": """
<h3>The Linear Function</h3>
<p>A linear function has form f(x) = mx + b where m is the slope and b is the y-intercept.</p>

<h3>Slope Calculation</h3>
<p>The slope m measures the rate of change:</p>
<p>$$m = \\frac{\\Delta y}{\\Delta x} = \\frac{y_2 - y_1}{x_2 - x_1}$$</p>

<div class="example-box">
<h4>Example 2: Finding Slope</h4>
<p>Line through (1, 3) and (4, 9): m = (9-3)/(4-1) = 6/3 = 2</p>
</div>

<h3>Forms of Linear Equations</h3>
<ul>
  <li><strong>Slope-intercept:</strong> y = mx + b</li>
  <li><strong>Point-slope:</strong> y - y₁ = m(x - x₁)</li>
  <li><strong>General form:</strong> Ax + By + C = 0</li>
</ul>

<h3>Parallel and Perpendicular Lines</h3>
<ul>
  <li>Parallel lines: m₁ = m₂</li>
  <li>Perpendicular lines: m₁ · m₂ = -1</li>
</ul>
"""
    },
    {
        "title": "Transformations of Functions",
        "body": """
<h3>Fundamental Transformations</h3>
<p>If y = f(x), then:</p>
<ul>
  <li>y = f(x) + k: Vertical shift up by k units</li>
  <li>y = f(x - h): Horizontal shift right by h units</li>
  <li>y = af(x): Vertical stretch by factor a (compress if 0 < a < 1)</li>
  <li>y = f(bx): Horizontal compression by factor 1/b</li>
  <li>y = -f(x): Reflection about x-axis</li>
  <li>y = f(-x): Reflection about y-axis</li>
</ul>

<div class="example-box">
<h4>Example 3: Composite Transformation</h4>
<p>Transform f(x) = x²: y = -2(x-3)² + 1</p>
<p>Shift right 3, stretch vertically by 2, reflect about x-axis, shift up 1</p>
</div>
"""
    },
    {
        "title": "Polynomial Functions: Behavior and Zeros",
        "body": """
<h3>Polynomial Characteristics</h3>
<p>A polynomial of degree n has the form:</p>
<p>$$f(x) = a_n x^n + a_{n-1}x^{n-1} + ... + a_1 x + a_0$$</p>

<h3>End Behavior</h3>
<p>For large |x|, the leading term aₙxⁿ dominates:</p>
<ul>
  <li>If n is even and aₙ > 0: Both ends go to +∞</li>
  <li>If n is even and aₙ < 0: Both ends go to -∞</li>
  <li>If n is odd and aₙ > 0: Left to -∞, right to +∞</li>
  <li>If n is odd and aₙ < 0: Left to +∞, right to -∞</li>
</ul>

<h3>Zeros and Multiplicity</h3>
<p>If (x - a)ᵐ is a factor, x = a is a zero of multiplicity m:</p>
<ul>
  <li>Odd multiplicity: Graph crosses x-axis</li>
  <li>Even multiplicity: Graph touches x-axis and bounces</li>
</ul>
"""
    },
    {
        "title": "Rational Functions and Asymptotes",
        "body": """
<h3>Definition and Domain</h3>
<p>A rational function is f(x) = p(x)/q(x) where p and q are polynomials.</p>
<p>Domain: All x except where q(x) = 0</p>

<h3>Asymptotes</h3>
<p><strong>Vertical asymptotes:</strong> x = a where q(a) = 0 (and p(a) ≠ 0)</p>
<p><strong>Horizontal asymptotes:</strong> Determined by degrees of p and q:
<ul>
  <li>deg(p) < deg(q): y = 0</li>
  <li>deg(p) = deg(q): y = (leading coeff of p)/(leading coeff of q)</li>
  <li>deg(p) > deg(q): No horizontal asymptote (oblique exists)</li>
</ul>
</p>

<div class="example-box">
<h4>Example 4: Analyzing Rational Functions</h4>
<p>f(x) = (2x²+1)/(x²-4)</p>
<p>Vertical asymptotes at x = ±2</p>
<p>Horizontal asymptote: y = 2/1 = 2</p>
</div>
"""
    },
    {
        "title": "Composition and Inverse Functions",
        "body": """
<h3>Function Composition</h3>
<p>(f ∘ g)(x) = f(g(x)): Apply g first, then apply f to the result</p>

<div class="example-box">
<h4>Example 5: Composition</h4>
<p>f(x) = 2x + 1, g(x) = x²</p>
<p>(f ∘ g)(x) = f(g(x)) = f(x²) = 2x² + 1</p>
<p>(g ∘ f)(x) = g(f(x)) = g(2x+1) = (2x+1)² = 4x² + 4x + 1</p>
</div>

<h3>Inverse Functions</h3>
<p>If f: A → B is bijective, f⁻¹: B → A satisfies:</p>
<p>(f ∘ f⁻¹)(y) = y and (f⁻¹ ∘ f)(x) = x</p>

<p>To find f⁻¹: Set y = f(x), solve for x in terms of y, swap x and y</p>

<div class="example-box">
<h4>Example 6: Inverse Function</h4>
<p>f(x) = (x+3)/2</p>
<p>y = (x+3)/2 → 2y = x + 3 → x = 2y - 3</p>
<p>f⁻¹(x) = 2x - 3</p>
</div>
"""
    },
    {
        "title": "Piecewise Functions and Step Functions",
        "body": """
<h3>Piecewise Defined Functions</h3>
<p>A function with different rules on different intervals:</p>
<p>$$f(x) = \\begin{cases} x^2 & \\text{if } x < 0 \\\\ x & \\text{if } 0 \\le x < 2 \\\\ 4 & \\text{if } x \\ge 2 \\end{cases}$$</p>

<h3>Absolute Value as Piecewise</h3>
<p>$$|x| = \\begin{cases} -x & \\text{if } x < 0 \\\\ x & \\text{if } x \\ge 0 \\end{cases}$$</p>

<h3>Floor and Ceiling Functions</h3>
<p>⌊x⌋ = greatest integer ≤ x (floor)</p>
<p>⌈x⌉ = least integer ≥ x (ceiling)</p>

<div class="example-box">
<h4>Example 7: Evaluating Piecewise</h4>
<p>Find f(-2), f(1), f(3) using function above</p>
<p>f(-2) = (-2)² = 4</p>
<p>f(1) = 1</p>
<p>f(3) = 4</p>
</div>
"""
    }
]
