TITLE = "Advanced Topics: Asymptotes, Piecewise, and Modulus Functions"

SECTIONS = [
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
<h4>Example 1: Vertical Asymptotes vs. Removable Discontinuity</h4>
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
<tr >
<td style="padding: 10px;"><strong>Case</strong></td>
<td style="padding: 10px;"><strong>Horizontal Asymptote</strong></td>
</tr>
<tr >
<td style="padding: 10px;">\\( n < m \\)</td>
<td style="padding: 10px;">\\( y = 0 \\)</td>
</tr>
<tr >
<td style="padding: 10px;">\\( n = m \\)</td>
<td style="padding: 10px;">\\( y = \\frac{a_n}{b_m} \\)</td>
</tr>
<tr >
<td style="padding: 10px;">\\( n > m \\)</td>
<td style="padding: 10px;">None (oblique possible)</td>
</tr>
</table>
</div>

<h3>Proof: Horizontal Asymptote (\\( n = m \\))</h3>
<p>For \\( f(x) = \\frac{a_n x^n + a_{n-1}x^{n-1} + \\ldots}{b_n x^n + b_{n-1}x^{n-1} + \\ldots} \\):</p>
$$\\lim_{x \\to \\infty} f(x) = \\lim_{x \\to \\infty} \\frac{a_n x^n(1 + a_{n-1}/(a_n x) + \\ldots)}{b_n x^n(1 + b_{n-1}/(b_n x) + \\ldots)} = \\frac{a_n}{b_n}$$

<div class="example-box">
<h4>Example 2: Horizontal Asymptote Analysis</h4>
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
<h4>Example 3: Oblique Asymptote Derivation</h4>
<p><strong>Find oblique asymptote of:</strong> \\( f(x) = \\frac{2x^2 + 3x - 1}{x - 1} \\)</p>
<p><strong>Solution (Polynomial Long Division):</strong></p>
<div style="margin: 10px; padding: 10px; border-left: 3px solid #2563eb">
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
<h4>Example 4: Complete Curve Sketch</h4>
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
<h4>Example 5: Checking Continuity at Transition</h4>
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
<h4>Example 6: Absolute Value Equation</h4>
<p><strong>Solve:</strong> \\( |2x - 3| = 5 \\)</p>
<p><strong>Solution:</strong> The equation \\( |A| = B \\) (where \\( B > 0 \\)) has solutions \\( A = B \\) or \\( A = -B \\).</p>
<p>Case 1: \\( 2x - 3 = 5 \\Rightarrow x = 4 \\)</p>
<p>Case 2: \\( 2x - 3 = -5 \\Rightarrow x = -1 \\)</p>
<p><strong>Answer:</strong> \\( x = -1 \\text{ or } x = 4 \\)</p>
</div>

<div class="example-box">
<h4>Example 7: Absolute Value Inequality</h4>
<p><strong>Solve:</strong> \\( |x - 2| < 3 \\)</p>
<p><strong>Solution:</strong> \\( |A| < B \\) is equivalent to \\( -B < A < B \\).</p>
$$-3 < x - 2 < 3$$
$$-1 < x < 5$$
<p><strong>Answer:</strong> \\( x \\in (-1, 5) \\)</p>
</div>

<h3>Graphing Piecewise and Absolute Value Functions</h3>

<div class="example-box">
<h4>Example 8: Graph Transformation via Absolute Value</h4>
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
<h4>Example 9: Composition with Absolute Value</h4>
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
<h4>Example 10: Modulus Function Reflection</h4>
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
<h4>Example 11: Absolute Value of Linear Function</h4>
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
<h4>Example 12: Equation with Two Absolute Values</h4>
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
<h4>Example 13: Distance and Absolute Value Inequality</h4>
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
