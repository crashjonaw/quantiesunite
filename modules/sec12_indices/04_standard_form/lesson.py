TITLE = "Standard Form (Scientific Notation)"

SECTIONS = [
    {
        "title": "What is Standard Form?",
        "body": """<div class='concept-box'>
<p><strong>Standard form</strong> (also called <strong>scientific notation</strong>) is a way of writing very large or very small numbers using powers of 10.</p>
<p>Standard form is written as: \\(a \\times 10^n\\)</p>
<p>Where:</p>
<ul>
<li>\\(a\\) is a number between 1 and 10 (we write \\(1 \\leq a < 10\\))</li>
<li>\\(n\\) is an integer (positive, negative, or zero)</li>
<li>\\(n\\) tells us how many places to move the decimal point</li>
</ul>
</div>

<div class='success-box'>
<h4>Why Standard Form Matters</h4>
<ul>
<li><strong>Clarity:</strong> 4,500,000,000,000 is harder to read than \\(4.5 \\times 10^{12}\\)</li>
<li><strong>Comparison:</strong> Easy to compare very large or very small numbers</li>
<li><strong>Science:</strong> Universal way to write measurements in physics, chemistry, biology</li>
<li><strong>Calculation:</strong> Makes multiplication and division of extreme values easier</li>
</ul>
</div>

<p><strong>Examples of Standard Form:</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">Normal Form</td>
  <td style="padding: 10px;">Standard Form</td>
  <td style="padding: 10px;">Size</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">5,000,000</td>
  <td style="padding: 10px; color: var(--success);">\\(5 \\times 10^6\\)</td>
  <td style="padding: 10px;">Large</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">0.00003</td>
  <td style="padding: 10px; color: var(--success);">\\(3 \\times 10^{-5}\\)</td>
  <td style="padding: 10px;">Small</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">1,000,000,000</td>
  <td style="padding: 10px; color: var(--success);">\\(1 \\times 10^9\\)</td>
  <td style="padding: 10px;">Very Large</td>
</tr>
</table>
"""
    },
    {
        "title": "Converting Large Numbers to Standard Form",
        "body": """<div class='worked-example'>
<h4>Method: Move Decimal to Get Number Between 1 and 10</h4>
<p><strong>Step 1:</strong> Place a decimal point after the first non-zero digit</p>
<p><strong>Step 2:</strong> Count how many places you moved the decimal point (left for large numbers)</p>
<p><strong>Step 3:</strong> The count becomes the positive power of 10</p>
</div>

<div class='worked-example'>
<h4>Example 1: 4,500,000</h4>
<pre>Original: 4,500,000
         Move decimal left: 4.500000
         Count: 6 places left

Result: 4.5 × 10⁶

Check: 4.5 × 10⁶ = 4.5 × 1,000,000 = 4,500,000 ✓</pre>
</div>

<div class='worked-example'>
<h4>Example 2: 85,000</h4>
<pre>Original: 85,000
         Move decimal left: 8.5
         Count: 4 places left

Result: 8.5 × 10⁴

Check: 8.5 × 10⁴ = 8.5 × 10,000 = 85,000 ✓</pre>
</div>

<div class='worked-example'>
<h4>Example 3: 302,000,000</h4>
<pre>Original: 302,000,000
         Move decimal left: 3.02
         Count: 8 places left

Result: 3.02 × 10⁸</pre>
</div>

<div class='success-box'>
<h4>Key Insight: Positive Powers = Large Numbers</h4>
<p>When converting a number larger than 1 to standard form:</p>
<ul>
<li>The power is <strong>positive</strong></li>
<li>The larger the original number, the larger the positive power</li>
<li>\\(10^1 = 10\\), \\(10^2 = 100\\), \\(10^3 = 1000\\), etc.</li>
</ul>
</div>
"""
    },
    {
        "title": "Converting Small Numbers to Standard Form",
        "body": """<div class='worked-example'>
<h4>Method: Move Decimal to Get Number Between 1 and 10</h4>
<p><strong>Step 1:</strong> Place a decimal point after the first non-zero digit</p>
<p><strong>Step 2:</strong> Count how many places you moved the decimal point (right for small numbers)</p>
<p><strong>Step 3:</strong> The count becomes the negative power of 10</p>
</div>

<div class='worked-example'>
<h4>Example 1: 0.00045</h4>
<pre>Original: 0.00045
         Move decimal right: 4.5
         Count: 4 places right

Result: 4.5 × 10⁻⁴

Check: 4.5 × 10⁻⁴ = 4.5 × 0.0001 = 0.00045 ✓</pre>
</div>

<div class='worked-example'>
<h4>Example 2: 0.000007</h4>
<pre>Original: 0.000007
         Move decimal right: 7
         Count: 6 places right

Result: 7 × 10⁻⁶</pre>
</div>

<div class='worked-example'>
<h4>Example 3: 0.0123</h4>
<pre>Original: 0.0123
         Move decimal right: 1.23
         Count: 2 places right

Result: 1.23 × 10⁻²</pre>
</div>

<div class='success-box'>
<h4>Key Insight: Negative Powers = Small Numbers</h4>
<p>When converting a number between 0 and 1 to standard form:</p>
<ul>
<li>The power is <strong>negative</strong></li>
<li>The smaller the original number, the more negative the power</li>
<li>\\(10^{-1} = 0.1\\), \\(10^{-2} = 0.01\\), \\(10^{-3} = 0.001\\), etc.</li>
</ul>
</div>
"""
    },
    {
        "title": "Converting From Standard Form Back to Normal",
        "body": """<div class='worked-example'>
<h4>Rule 1: Positive Power → Move Decimal Right</h4>
<p>\\(3.6 \\times 10^4\\)</p>
<pre>Start with: 3.6
Move decimal right 4 places: 36,000
Result: 36,000</pre>

<p>\\(1.25 \\times 10^6\\)</p>
<pre>Start with: 1.25
Move decimal right 6 places: 1,250,000
Result: 1,250,000</pre>

<p>\\(7 \\times 10^3\\)</p>
<pre>Start with: 7
Move decimal right 3 places: 7,000
Result: 7,000</pre>
</div>

<div class='worked-example'>
<h4>Rule 2: Negative Power → Move Decimal Left</h4>
<p>\\(2.5 \\times 10^{-3}\\)</p>
<pre>Start with: 2.5
Move decimal left 3 places: 0.0025
Result: 0.0025</pre>

<p>\\(8.1 \\times 10^{-5}\\)</p>
<pre>Start with: 8.1
Move decimal left 5 places: 0.000081
Result: 0.000081</pre>

<p>\\(4 \\times 10^{-2}\\)</p>
<pre>Start with: 4
Move decimal left 2 places: 0.04
Result: 0.04</pre>
</div>

<div class='success-box'>
<h4>Memory Aid</h4>
<ul>
<li><strong>Positive exponent (×10⁺):</strong> Number is BIG → move decimal RIGHT</li>
<li><strong>Negative exponent (×10⁻):</strong> Number is SMALL → move decimal LEFT</li>
<li>The exponent tells you HOW MANY places to move</li>
</ul>
</div>

<p><strong>Visual: Exponential Growth</strong></p>
<svg viewBox="0 0 400 210" style="max-width:420px;width:100%;">
  <!-- Axes -->
  <line x1="55" y1="170" x2="385" y2="170" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  <line x1="55" y1="25" x2="55" y2="170" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>

  <!-- Powers of 10 bars -->
  <rect x="70" y="158" width="35" height="12" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="87" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10¹</text>

  <rect x="120" y="140" width="35" height="30" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="137" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10²</text>

  <rect x="170" y="115" width="35" height="55" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="187" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10³</text>

  <rect x="220" y="75" width="35" height="95" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="237" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10⁴</text>

  <rect x="270" y="45" width="35" height="125" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="287" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10⁵</text>

  <rect x="320" y="30" width="35" height="140" rx="4" fill="#4169E1" opacity="0.7"/>
  <text x="337" y="188" text-anchor="middle" font-size="11" fill="currentColor" font-family="sans-serif">10⁶</text>

  <!-- Y-axis label -->
  <text x="35" y="100" text-anchor="end" font-size="12" fill="currentColor" font-family="sans-serif">Size</text>
  <!-- X-axis label -->
  <text x="220" y="205" text-anchor="middle" font-size="12" fill="currentColor" font-family="sans-serif">Power of 10</text>
</svg>
"""
    }
]
