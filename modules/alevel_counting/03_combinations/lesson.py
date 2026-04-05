TITLE = "Combinations: Unordered Selections (nCr)"

SECTIONS = [
    {
        "title": "Definition and Formula Derivation",
        "body": """
<h3>What is a Combination?</h3>
<p>A <strong>combination</strong> of $r$ objects from $n$ distinct objects is an unordered selection where order does NOT matter.</p>

<p>$$\\binom{n}{r} = {}_nC_r = \\frac{n!}{r!(n-r)!}$$</p>

<h3>Why This Formula?</h3>
<p>Each combination of $r$ objects can be arranged in $r!$ ways to form different permutations.</p>
<p>Since ${}_nP_r = r! \\times {}_nC_r$, we have:</p>
<p>$${}_nC_r = \\frac{{}_nP_r}{r!} = \\frac{n!/(n-r)!}{r!} = \\frac{n!}{r!(n-r)!}$$</p>

<div class="worked-example">
<h4>Example 1: Basic Combination</h4>
<p>Choose 3 students from 5 for a committee</p>
<p><strong>Solution:</strong> ${}_5C_3 = \\frac{5!}{3! \\times 2!} = \\frac{5 \\times 4 \\times 3!}{3! \\times 2 \\times 1} = \\frac{5 \\times 4}{2 \\times 1} = 10$</p>
</div>

<div class="concept-box">
<h4>Key Difference: Permutation vs Combination</h4>
<p><strong>Permutation:</strong> Selecting 3 people from 5 for president, VP, secretary (positions matter) $= {}_5P_3 = 60$</p>
<p><strong>Combination:</strong> Selecting 3 people from 5 for a committee (positions don't matter) $= {}_5C_3 = 10$</p>
</div>
"""
    },
    {
        "title": "Key Properties and Applications",
        "body": """
<h3>Important Properties of Combinations</h3>
<ul>
<li><strong>${}_nC_0 = 1$:</strong> One way to choose nothing</li>
<li><strong>${}_nC_n = 1$:</strong> One way to choose everything</li>
<li><strong>Symmetry: ${}_nC_r = {}_nC_{n-r}$:</strong> Choosing $r$ items is like leaving out $n-r$ items</li>
<li><strong>Pascal's Identity: $\\binom{n}{r} = \\binom{n-1}{r-1} + \\binom{n-1}{r}$</strong></li>
</ul>

<div class="worked-example">
<h4>Example 2: Symmetry Property</h4>
<p>Show that ${}_5C_2 = {}_5C_3$</p>
<p><strong>Solution:</strong> ${}_5C_2 = 10$ (choose 2) and ${}_5C_3 = 10$ (leave out 2, which is same as choosing 3). They're equal!</p>
</div>

<h3>Connection to Binomial Theorem</h3>
<p>The binomial expansion:</p>
<p>$$(x + y)^{n} = \\sum_{k=0}^{n} \\binom{n}{k} x^{n-k} y^{k}$$</p>
<p>The coefficients $\\binom{n}{k}$ count the number of ways to choose $k$ items from $n$ terms when expanding.</p>
"""
    },
    {
        "title": "Combinations with Restrictions",
        "body": """
<h3>Problems with Constraints</h3>
<p>When selecting with restrictions, break the problem into cases and apply the multiplication principle.</p>

<div class="worked-example">
<h4>Example 3: Restricted Selection</h4>
<p>Select 4 people from 6 men and 4 women such that at least 2 are women</p>
<p><strong>Solution:</strong> "At least 2 women" means 2, 3, or 4 women:</p>
<ul>
<li>2 women, 2 men: ${}_4C_2 \\times {}_6C_2 = 6 \\times 15 = 90$</li>
<li>3 women, 1 man: ${}_4C_3 \\times {}_6C_1 = 4 \\times 6 = 24$</li>
<li>4 women, 0 men: ${}_4C_4 \\times {}_6C_0 = 1 \\times 1 = 1$</li>
</ul>
<p>Total: $90 + 24 + 1 = 115$</p>
</div>

<h3>Using Complementary Counting</h3>
<p>Sometimes it's easier to count what you DON'T want and subtract from the total.</p>

<div class="worked-example">
<h4>Example 4: Complement Approach</h4>
<p>Select 4 people from 10 (6 men, 4 women) such that at least 1 woman is chosen</p>
<p><strong>Solution:</strong><br>
Total ways: ${}_{10}C_4 = 210$<br>
Ways with 0 women (all men): ${}_6C_4 = 15$<br>
Ways with at least 1 woman: $210 - 15 = 195$</p>
</div>
"""
    }
]
