TITLE = "Arithmetic and Geometric Sequences"

SECTIONS = [
    {
        "title": "Arithmetic Sequences and Series",
        "body": """
<h3>Arithmetic Sequences (AP)</h3>

<div class="formula-box">
<h4>Definition and General Term</h4>
<p>An arithmetic sequence has constant common difference \\( d \\):</p>
$$a_{n+1} = a_n + d$$
<p>The general term is:</p>
$$a_n = a_1 + (n-1)d$$
</div>

<div class="example-box">
<h4>Example 1: AP General Term</h4>
<p><strong>Find the 20th term of:</strong> \\( 3, 7, 11, 15, \\ldots \\)</p>
<p><strong>Solution:</strong> \\( a_1 = 3 \\), \\( d = 4 \\)</p>
$$a_{20} = 3 + 19 \\cdot 4 = 79$$
</div>

<h3>Sum of an AP</h3>

<div class="formula-box">
<h4>AP Sum Formula</h4>
<p>The sum of the first \\( n \\) terms of an AP is:</p>
$$S_n = \\frac{n}{2}(a_1 + a_n) = \\frac{n}{2}[2a_1 + (n-1)d]$$
</div>

<div class="example-box">
<h4>Example 2: Sum of AP</h4>
<p><strong>Find:</strong> \\( 1 + 4 + 7 + \\ldots + 100 \\)</p>
<p>With \\( a_1 = 1 \\), \\( d = 3 \\): \\( 100 = 1 + (n-1) \\cdot 3 \\) gives \\( n = 34 \\)</p>
$$S_{34} = \\frac{34}{2}(1 + 100) = 17 \\times 101 = 1717$$
</div>
"""
    },
    {
        "title": "Geometric Sequences and Series",
        "body": """
<h3>Geometric Sequences (GP)</h3>

<div class="formula-box">
<h4>Definition and General Term</h4>
<p>A geometric sequence has constant common ratio \\( r \\):</p>
$$a_{n+1} = r \\cdot a_n$$
<p>General term:</p>
$$a_n = a_1 \\cdot r^{n-1}$$
</div>

<div class="example-box">
<h4>Example 3: GP General Term</h4>
<p><strong>Find the 10th term of:</strong> \\( 2, 6, 18, 54, \\ldots \\)</p>
<p>\\( a_1 = 2 \\), \\( r = 3 \\):</p>
$$a_{10} = 2 \\times 3^9 = 39366$$
</div>

<h3>Sum of a GP</h3>

<div class="formula-box">
<h4>Finite GP Sum</h4>
<p>For \\( r \\neq 1 \\):</p>
$$S_n = a_1 \\cdot \\frac{1 - r^n}{1 - r} = a_1 \\cdot \\frac{r^n - 1}{r - 1}$$
</div>

<div class="example-box">
<h4>Example 4: Sum of Finite GP</h4>
<p><strong>Find:</strong> \\( 1 + 2 + 4 + 8 + \\ldots + 512 \\)</p>
<p>\\( a_1 = 1 \\), \\( r = 2 \\), \\( a_n = 512 \\) gives \\( n = 10 \\)</p>
$$S_{10} = 1 \\times \\frac{2^{10} - 1}{2 - 1} = 1023$$
</div>

<h3>Infinite Geometric Series</h3>

<div class="formula-box">
<h4>Convergence of Infinite GP</h4>
<p>For geometric series \\( \\sum_{n=0}^{\\infty} a_1 r^{n-1} \\):</p>
<ul>
<li>If \\( |r| < 1 \\): series converges to \\( S = \\frac{a_1}{1-r} \\)</li>
<li>If \\( |r| \\geq 1 \\): series diverges</li>
</ul>
</div>

<div class="example-box">
<h4>Example 5: Infinite GP Sum</h4>
<p><strong>Find:</strong> \\( 1 + \\frac{1}{2} + \\frac{1}{4} + \\ldots \\)</p>
<p>\\( a_1 = 1 \\), \\( r = \\frac{1}{2} \\) (and \\( |r| < 1 \\))</p>
$$S = \\frac{1}{1 - 0.5} = 2$$
</div>
"""
    }
]
