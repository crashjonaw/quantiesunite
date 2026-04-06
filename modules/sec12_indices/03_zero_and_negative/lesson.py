TITLE = "Zero and Negative Indices"

SECTIONS = [
    {
        "title": "The Zero Index",
        "body": """<div class='concept-box'>
<p><strong>Any non-zero number to the power 0 equals 1.</strong></p>
<p>$$a^0 = 1$$ (for any \\(a \\neq 0\\))</p>
</div>

<div class='worked-example'>
<h4>Why This Makes Sense</h4>
<p>Consider the division law: when we divide a number by itself using the division rule:</p>
<pre>2⁴ ÷ 2⁴ = 2⁴⁻⁴ = 2⁰</pre>
<p>But we also know:</p>
<pre>2⁴ ÷ 2⁴ = 16 ÷ 16 = 1</pre>
<p>Therefore: \\(2^0 = 1\\)</p>
<p>This works for ANY non-zero number, so we define: \\(a^0 = 1\\)</p>
</div>

<div class='success-box'>
<h4>Examples</h4>
<p>\\(5^0 = 1\\)</p>
<p>\\(x^0 = 1\\)</p>
<p>\\((100)^0 = 1\\)</p>
<p>\\((-7)^0 = 1\\)</p>
<p>\\((\\frac{3}{4})^0 = 1\\)</p>
</div>

<p><strong>Pattern Recognition:</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">Expression</td>
  <td style="padding: 10px;">Using Division Law</td>
  <td style="padding: 10px;">Result</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(3^3 \\div 3^3\\)</td>
  <td style="padding: 10px;">\\(3^{3-3} = 3^0\\)</td>
  <td style="padding: 10px; color: var(--success);">1</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(5^2 \\div 5^2\\)</td>
  <td style="padding: 10px;">\\(5^{2-2} = 5^0\\)</td>
  <td style="padding: 10px; color: var(--success);">1</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(a^n \\div a^n\\)</td>
  <td style="padding: 10px;">\\(a^{n-n} = a^0\\)</td>
  <td style="padding: 10px; color: var(--success);">1</td>
</tr>
</table>
"""
    },
    {
        "title": "Negative Indices",
        "body": """<div class='concept-box'>
<p><strong>A negative index means "take the reciprocal" or "put it in the denominator".</strong></p>
<p>$$a^{-n} = \\frac{1}{a^n}$$</p>
</div>

<div class='worked-example'>
<h4>Why This Makes Sense</h4>
<p>Again, let's use the division law with a special case:</p>
<pre>2² ÷ 2⁵ = 2²⁻⁵ = 2⁻³</pre>
<p>But we also know:</p>
<pre>2² ÷ 2⁵ = 4/32 = 1/8 = 1/2³</pre>
<p>Therefore: \\(2^{-3} = \\frac{1}{2^3} = \\frac{1}{8}\\)</p>
</div>

<div class='success-box'>
<h4>Examples</h4>
<p>\\(2^{-1} = \\frac{1}{2} = 0.5\\)</p>
<p>\\(3^{-2} = \\frac{1}{3^2} = \\frac{1}{9}\\)</p>
<p>\\(x^{-1} = \\frac{1}{x}\\)</p>
<p>\\(a^{-4} = \\frac{1}{a^4}\\)</p>
<p>\\((\\frac{3}{4})^{-1} = \\frac{4}{3}\\) (flip the fraction!)</p>
</div>

<div class='warning-box'>
<h4>Key Insight: Negative Index = Reciprocal</h4>
<p>When you see a negative index, it's telling you to:</p>
<ul>
<li>Move the term to the other side of a fraction line</li>
<li>Change the sign of the exponent to positive</li>
</ul>
<p>\\(x^{-2} = \\frac{1}{x^2}\\) OR \\(\\frac{1}{x^{-2}} = x^2\\)</p>
</div>

<p><strong>Practical Conversions:</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">Negative Index Form</td>
  <td style="padding: 10px;">Fraction Form</td>
  <td style="padding: 10px;">Decimal (if applicable)</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(2^{-3}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{1}{8}\\)</td>
  <td style="padding: 10px; color: var(--success);">0.125</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(10^{-2}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{1}{100}\\)</td>
  <td style="padding: 10px; color: var(--success);">0.01</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(5^{-1}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{1}{5}\\)</td>
  <td style="padding: 10px; color: var(--success);">0.2</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\((\\frac{2}{3})^{-1}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{3}{2}\\)</td>
  <td style="padding: 10px; color: var(--success);">1.5</td>
</tr>
</table>
"""
    },
    {
        "title": "Simplifying with Zero and Negative Indices",
        "body": """<div class='worked-example'>
<h4>Example 1: Zero Index</h4>
<p>Simplify: \\(3^0 \\times 3^5\\)</p>
<p><strong>Step 1:</strong> Evaluate \\(3^0\\)</p>
<p style="margin-left:20px;">\\(3^0 = 1\\)</p>
<p><strong>Step 2:</strong> Multiply</p>
<p style="margin-left:20px;">\\(1 \\times 3^5 = 3^5 = 243\\)</p>
</div>

<div class='worked-example'>
<h4>Example 2: Negative Index in Multiplication</h4>
<p>Simplify: \\(a^{-2} \\times a^5\\)</p>
<p><strong>Step 1:</strong> Apply multiplication law (add indices)</p>
<p style="margin-left:20px;">\\(a^{-2} \\times a^5 = a^{-2+5} = a^3\\)</p>
</div>

<div class='worked-example'>
<h4>Example 3: Negative Index in Division</h4>
<p>Simplify: \\(x^4 \\div x^9\\)</p>
<p><strong>Step 1:</strong> Apply division law (subtract indices)</p>
<p style="margin-left:20px;">\\(x^4 \\div x^9 = x^{4-9} = x^{-5}\\)</p>
<p><strong>Step 2:</strong> Convert to fraction form</p>
<p style="margin-left:20px;">\\(x^{-5} = \\frac{1}{x^5}\\)</p>
</div>

<div class='worked-example'>
<h4>Example 4: Power of a Power with Negative Index</h4>
<p>Simplify: \\((2^{-3})^2\\)</p>
<p><strong>Step 1:</strong> Apply power of power law (multiply indices)</p>
<p style="margin-left:20px;">\\((2^{-3})^2 = 2^{-3 \\times 2} = 2^{-6}\\)</p>
<p><strong>Step 2:</strong> Convert to fraction</p>
<p style="margin-left:20px;">\\(2^{-6} = \\frac{1}{2^6} = \\frac{1}{64}\\)</p>
</div>

<div class='success-box'>
<h4>All Laws Work with Negative and Zero Indices</h4>
<ul>
<li>\\(a^m \\times a^n = a^{m+n}\\) ✓ (even if m or n is negative or zero)</li>
<li>\\(a^m \\div a^n = a^{m-n}\\) ✓ (even if m or n is negative or zero)</li>
<li>\\((a^m)^n = a^{mn}\\) ✓ (even if m or n is negative or zero)</li>
</ul>
</div>
"""
    },
    {
        "title": "Converting Between Forms",
        "body": """<div class='worked-example'>
<h4>Moving Between Index Forms and Fractions</h4>
<p>Using the rule: \\(a^{-n} = \\frac{1}{a^n}\\)</p>
<p>We can move terms between numerator and denominator by flipping the sign of the exponent:</p>

<pre>2⁻³ = 1/2³            (negative index → fraction)
1/x² = x⁻²            (fraction → negative index)
a⁴/a⁷ = a⁴⁻⁷ = a⁻³    (division law)
a⁴/a⁷ = 1/a³          (simplify the fraction)</pre>
</div>

<div class='worked-example'>
<h4>Example: Expressing in Different Ways</h4>
<p>All of these mean the same thing:</p>
<ul>
<li>\\(2^{-3}\\)</li>
<li>\\(\\frac{1}{2^3}\\)</li>
<li>\\(\\frac{1}{8}\\)</li>
<li>0.125</li>
</ul>
<p>Different forms are useful in different contexts. Choose the one that makes your work clearest!</p>
</div>

<div class='success-box'>
<h4>Quick Reference Table</h4>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">If you see...</td>
  <td style="padding: 10px;">Rewrite as...</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(x^{-2}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{1}{x^2}\\)</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(\\frac{1}{a^3}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(a^{-3}\\)</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(\\frac{a^2}{b^5}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(a^2 b^{-5}\\)</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(a^{-3} b^{-2}\\)</td>
  <td style="padding: 10px; color: var(--success);">\\(\\frac{1}{a^3 b^2}\\)</td>
</tr>
</table>
</div>
"""
    }
]
