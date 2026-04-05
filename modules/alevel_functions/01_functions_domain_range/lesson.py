TITLE = "Functions, Domain, and Range"

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
<tr ><td><strong>Interval</strong></td><td><strong>\\( x+2 \\)</strong></td><td><strong>\\( x-3 \\)</strong></td><td><strong>Quotient</strong></td></tr>
<tr ><td>\\( x < -2 \\)</td><td>\\( - \\)</td><td>\\( - \\)</td><td>\\( + \\)</td></tr>
<tr ><td>\\( -2 < x < 3 \\)</td><td>\\( + \\)</td><td>\\( - \\)</td><td>\\( - \\)</td></tr>
<tr ><td>\\( x > 3 \\)</td><td>\\( + \\)</td><td>\\( + \\)</td><td>\\( + \\)</td></tr>
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
<tr style="border-bottom: 2px solid #333">
<td style="padding: 10px;"><strong>Function Type</strong></td>
<td style="padding: 10px;"><strong>Domain Restriction</strong></td>
<td style="padding: 10px;"><strong>Range Finding Method</strong></td>
</tr>
<tr >
<td style="padding: 10px;">Polynomial</td>
<td style="padding: 10px;">None (\\( \\mathbb{R} \\))</td>
<td style="padding: 10px;">Calculus/Graphing</td>
</tr>
<tr >
<td style="padding: 10px;">Rational</td>
<td style="padding: 10px;">Exclude denominator zeros</td>
<td style="padding: 10px;">Algebraic or asymptote analysis</td>
</tr>
<tr >
<td style="padding: 10px;">Radical (even)</td>
<td style="padding: 10px;">Radicand \\( \\geq 0 \\)</td>
<td style="padding: 10px;">From radicand range; always \\( \\geq 0 \\)</td>
</tr>
<tr >
<td style="padding: 10px;">Logarithmic</td>
<td style="padding: 10px;">Argument \\( > 0 \\)</td>
<td style="padding: 10px;">\\( \\mathbb{R} \\) (surjective)</td>
</tr>
</table>
"""
    }
]
