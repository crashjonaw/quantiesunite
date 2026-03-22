SECTIONS = [
    {
        "title": "What are Indices (Exponents)?",
        "body": """
<p><strong>Indices</strong> (or <strong>exponents</strong>) are a shorthand way of writing repeated multiplication.</p>

<p>When we write 2³, we mean: 2 × 2 × 2 = 8</p>

<p><strong>The Parts of an Index:</strong></p>
<ul>
<li><strong>Base:</strong> The number being multiplied (in 2³, the base is 2)</li>
<li><strong>Index (or exponent):</strong> The small number showing how many times to multiply (in 2³, the index is 3)</li>
</ul>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
3⁴ = 3 × 3 × 3 × 3 = 81
(the base 3 is multiplied by itself 4 times)

5² = 5 × 5 = 25
(read as "5 squared")

2⁵ = 2 × 2 × 2 × 2 × 2 = 32
(read as "2 to the power of 5")

10³ = 10 × 10 × 10 = 1000
</pre>
</div>

<p><strong>Why Indices Are Useful:</strong></p>
<ul>
<li>They make large calculations easier to write: instead of 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2, we write 2⁸</li>
<li>They help us understand patterns in numbers</li>
<li>They're essential in science (for very large and very small numbers)</li>
</ul>

<p><strong>Special Index Values:</strong></p>
<ul>
<li>Any number to the power 1 equals itself: 5¹ = 5</li>
<li>Any number to the power 0 equals 1: 5⁰ = 1 (we'll see why this makes sense soon)</li>
</ul>
"""
    },
    {
        "title": "Laws of Indices: Multiply and Divide",
        "body": """
<p>There are rules (laws) for working with indices that make calculations much easier.</p>

<p><strong>Law 1: Multiplying Powers (Same Base)</strong></p>
<p>When multiplying numbers with the same base, add the indices.</p>
<p><strong>aᵐ × aⁿ = aᵐ⁺ⁿ</strong></p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
2³ × 2² = (2 × 2 × 2) × (2 × 2)
        = 2 × 2 × 2 × 2 × 2
        = 2⁵

So we add the indices: 3 + 2 = 5

More examples:
x⁴ × x³ = x⁷
10² × 10⁵ = 10⁷
a² × a² × a³ = a⁷
</pre>
</div>

<p><strong>Law 2: Dividing Powers (Same Base)</strong></p>
<p>When dividing numbers with the same base, subtract the indices.</p>
<p><strong>aᵐ ÷ aⁿ = aᵐ⁻ⁿ</strong> (or written as aᵐ/aⁿ = aᵐ⁻ⁿ)</p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
2⁵ ÷ 2² = (2 × 2 × 2 × 2 × 2) ÷ (2 × 2)
        = (2 × 2 × 2 × 2 × 2)/(2 × 2)

The two 2's cancel out, leaving:
        = 2 × 2 × 2
        = 2³

So we subtract the indices: 5 - 2 = 3

More examples:
x⁷ ÷ x⁴ = x³
10⁸ ÷ 10³ = 10⁵
a⁶/a² = a⁴
</pre>
</div>

<div class='example-box'>
<p><strong>Combined Examples:</strong></p>
<pre class='code-block'>
Simplify: (2⁴ × 2³) ÷ 2⁵
= 2⁷ ÷ 2⁵
= 2²
= 4

Simplify: (3² × 3⁴) / 3³
= 3⁶ / 3³
= 3³
= 27

Simplify: a⁵ × b³ × a² ÷ b
= a⁷ × b²
(combine like bases: a's together, b's together)
</pre>
</div>
"""
    },
    {
        "title": "Law of Indices: Power of a Power",
        "body": """
<p><strong>Law 3: Power of a Power</strong></p>
<p>When raising a power to a power, multiply the indices.</p>
<p><strong>(aᵐ)ⁿ = aᵐ⁽ⁿ⁾ = aᵐⁿ</strong></p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
(2³)² = 2³ × 2³
      = 2³⁺³
      = 2⁶
      = 64

Or thinking about it differently:
(2³)² means "2³, multiplied by itself"
= (2 × 2 × 2) × (2 × 2 × 2)
= 2 × 2 × 2 × 2 × 2 × 2
= 2⁶

We multiply indices: 3 × 2 = 6
</pre>
</div>

<p><strong>Law 4: Power of a Product</strong></p>
<p>When raising a product to a power, apply the power to each factor.</p>
<p><strong>(ab)ⁿ = aⁿbⁿ</strong></p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
(2 × 3)² = 2² × 3²
         = 4 × 9
         = 36

Or: (2 × 3)² = 6² = 36 ✓

(xy)³ = x³y³

(2a)⁴ = 2⁴a⁴ = 16a⁴
</pre>
</div>

<p><strong>Law 5: Power of a Quotient</strong></p>
<p>When raising a quotient to a power, apply the power to both numerator and denominator.</p>
<p><strong>(a/b)ⁿ = aⁿ/bⁿ</strong></p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
(2/3)² = 2²/3² = 4/9

(x/y)³ = x³/y³

(a/5)² = a²/25
</pre>
</div>

<div class='example-box'>
<p><strong>Combining Multiple Laws:</strong></p>
<pre class='code-block'>
Simplify: (2a³)⁴
= 2⁴ × (a³)⁴
= 16 × a¹²
= 16a¹²

Simplify: (x²y)³
= (x²)³ × y³
= x⁶ × y³
= x⁶y³

Simplify: (a²/b³)²
= a⁴/b⁶
</pre>
</div>
"""
    },
    {
        "title": "Negative and Zero Indices",
        "body": """
<p><strong>Zero Index: Any Number to the Power 0</strong></p>
<p><strong>a⁰ = 1</strong> (for any non-zero number a)</p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
Consider: 2⁴ ÷ 2⁴
Using the division law: 2⁴⁻⁴ = 2⁰

But we also know:
2⁴ ÷ 2⁴ = 16 ÷ 16 = 1

So 2⁰ must equal 1

More examples:
5⁰ = 1
x⁰ = 1
(100)⁰ = 1
</pre>
</div>

<p><strong>Negative Indices: Reciprocals</strong></p>
<p>A negative index means "take the reciprocal" or "put it in the denominator".</p>
<p><strong>a⁻ⁿ = 1/aⁿ</strong></p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
Consider: 2² ÷ 2⁵
Using the division law: 2²⁻⁵ = 2⁻³

But we also know:
2² ÷ 2⁵ = 4/32 = 1/8 = 1/2³

So 2⁻³ = 1/2³

More examples:
2⁻¹ = 1/2
3⁻² = 1/9
x⁻¹ = 1/x
a⁻⁴ = 1/a⁴
</pre>
</div>

<div class='example-box'>
<p><strong>Converting Between Forms:</strong></p>
<pre class='code-block'>
2⁻³ = 1/2³ = 1/8

x⁻² = 1/x²

(3/4)⁻¹ = 1/(3/4) = 4/3

a⁻ⁿ can be written as: 1/aⁿ or as a power with positive index

2⁴/2⁷ = 2⁴⁻⁷ = 2⁻³ = 1/8
</pre>
</div>

<p><strong>Simplifying with Negative and Zero Indices:</strong></p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
Simplify: 3⁰ × 3⁵
= 1 × 3⁵
= 3⁵
= 243

Simplify: a⁻² × a⁵
= a⁻²⁺⁵
= a³

Simplify: x⁴/x⁹
= x⁴⁻⁹
= x⁻⁵
= 1/x⁵

Simplify: (2⁻³)²
= 2⁻³ˣ²
= 2⁻⁶
= 1/64
</pre>
</div>
"""
    },
    {
        "title": "Standard Form (Scientific Notation)",
        "body": """
<p><strong>Standard Form</strong> is a way of writing very large or very small numbers using powers of 10. It's also called <strong>scientific notation</strong>.</p>

<p>Standard form is written as: <strong>a × 10ⁿ</strong> where:</p>
<ul>
<li>a is a number between 1 and 10 (1 ≤ a < 10)</li>
<li>n is an integer (positive, negative, or zero)</li>
<li>n tells us how many places to move the decimal point</li>
</ul>

<p><strong>Converting Large Numbers to Standard Form:</strong></p>

<div class='example-box'>
<p><strong>Example 1: 4,500,000</strong></p>
<pre class='code-block'>
Move the decimal point to create a number between 1 and 10:
4,500,000 = 4.500000...

Count how many places we moved the decimal (left):
4,500,000 → 4.5 (moved 6 places left)

So: 4,500,000 = 4.5 × 10⁶

The positive 6 tells us the original number is large.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: 85,000</strong></p>
<pre class='code-block'>
85,000 = 8.5 × 10⁴
(moved decimal 4 places left)

Example 3: 302,000,000
302,000,000 = 3.02 × 10⁸
(moved decimal 8 places left)

Example 4: 6
6 = 6 × 10⁰
(decimal didn't move)
</pre>
</div>

<p><strong>Converting Small Numbers to Standard Form:</strong></p>

<div class='example-box'>
<p><strong>Example 1: 0.00045</strong></p>
<pre class='code-block'>
Move the decimal point to create a number between 1 and 10:
0.00045 → 4.5 (moved 4 places right)

When we move right, we use a negative power:
0.00045 = 4.5 × 10⁻⁴

The negative 4 tells us the original number is small.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: 0.000007</strong></p>
<pre class='code-block'>
0.000007 = 7 × 10⁻⁶
(moved decimal 6 places right)

Example 3: 0.0123
0.0123 = 1.23 × 10⁻²
(moved decimal 2 places right)

Example 4: 0.5
0.5 = 5 × 10⁻¹
(moved decimal 1 place right)
</pre>
</div>

<p><strong>Converting From Standard Form Back to Normal:</strong></p>

<div class='example-box'>
<p><strong>Positive Power: Move Decimal Right</strong></p>
<pre class='code-block'>
3.6 × 10⁴ = 36,000
(move decimal 4 places right)

1.25 × 10⁶ = 1,250,000
(move decimal 6 places right)

7 × 10³ = 7,000
(move decimal 3 places right)
</pre>
</div>

<div class='example-box'>
<p><strong>Negative Power: Move Decimal Left</strong></p>
<pre class='code-block'>
2.5 × 10⁻³ = 0.0025
(move decimal 3 places left)

8.1 × 10⁻⁵ = 0.000081
(move decimal 5 places left)

4 × 10⁻² = 0.04
(move decimal 2 places left)
</pre>
</div>

<p><strong>Operations with Standard Form:</strong></p>

<div class='example-box'>
<p><strong>Multiplication:</strong></p>
<pre class='code-block'>
(2 × 10⁵) × (3 × 10³)
= (2 × 3) × (10⁵ × 10³)
= 6 × 10⁸

(1.5 × 10⁻²) × (4 × 10⁴)
= (1.5 × 4) × (10⁻² × 10⁴)
= 6 × 10²
= 6 × 100
= 600
</pre>
</div>

<div class='example-box'>
<p><strong>Division:</strong></p>
<pre class='code-block'>
(8 × 10⁶) ÷ (2 × 10³)
= (8 ÷ 2) × (10⁶ ÷ 10³)
= 4 × 10³
= 4,000

(6 × 10⁻⁴) ÷ (3 × 10⁻⁶)
= (6 ÷ 3) × (10⁻⁴ ÷ 10⁻⁶)
= 2 × 10⁻⁴⁻⁽⁻⁶⁾
= 2 × 10⁻⁴⁺⁶
= 2 × 10²
= 200
</pre>
</div>

<p><strong>Why Standard Form Is Useful:</strong></p>
<ul>
<li>Makes very large and very small numbers easier to write and compare</li>
<li>Used in science for distances (light-years), atomic sizes, bacteria counts</li>
<li>Makes calculations easier when working with extreme values</li>
<li>Universal system understood across science and engineering</li>
</ul>
"""
    }
]
