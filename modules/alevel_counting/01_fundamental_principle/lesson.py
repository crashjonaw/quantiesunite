TITLE = "Fundamental Counting Principle: Multiplication & Addition Rules"

SECTIONS = [
    {
        "title": "Multiplication Principle",
        "body": """
<h3>Multiplication Principle</h3>
<p>If a task has m ways and a second independent task has n ways, then both tasks together can be done in \(m \\times n\) ways.</p>

<p><strong>General form:</strong> If we have k independent tasks with \(n_1, n_2, \ldots, n_k\) ways respectively, the total number of ways is:</p>
<p style="text-align: center; font-weight: bold;">\(n_1 \\times n_2 \\times \\cdots \\times n_k\)</p>

<div class="concept-box">
<h4>Example 1: Multiplication Principle</h4>
<p>A restaurant offers 5 appetizers, 8 main courses, and 3 desserts. How many complete meals can be ordered?</p>
<p><strong>Solution:</strong> \(5 \\times 8 \\times 3 = 120\) different meals</p>
</div>

<h3>Key Insight</h3>
<p>The multiplication principle applies when tasks are <strong>independent</strong>—the number of ways to complete one task doesn't affect the number of ways to complete another.</p>
"""
    },
    {
        "title": "Addition Principle and Inclusion-Exclusion",
        "body": """
<h3>Addition Principle</h3>
<p>If task A can be done in m mutually exclusive ways and task B in n mutually exclusive ways, then either A or B can be done in \(m + n\) ways (provided A and B don't overlap).</p>

<p><strong>Inclusion-Exclusion Principle:</strong> If sets overlap:</p>
<p style="text-align: center; font-weight: bold;">\(|A \cup B| = |A| + |B| - |A \cap B|\)</p>

<div class="worked-example">
<h4>Example 2: Addition Principle</h4>
<p>How many integers from 1 to 100 are divisible by 3 or 5?</p>
<p><strong>Solution:</strong></p>
<p>Divisible by 3: \(\lfloor 100/3 \rfloor = 33\)<br>
Divisible by 5: \(\lfloor 100/5 \rfloor = 20\)<br>
Divisible by both 15: \(\lfloor 100/15 \rfloor = 6\)<br>
By inclusion-exclusion: \(33 + 20 - 6 = 47\)</p>
</div>

<h3>Three-Set Inclusion-Exclusion</h3>
<p style="text-align: center; font-weight: bold;">\(|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|\)</p>
"""
    },
    {
        "title": "Arrangements Without Repetition",
        "body": """
<h3>Counting Linear Arrangements</h3>
<p>If we arrange n distinct objects where order matters and no repetition is allowed, there are \(n! = n(n-1)(n-2) \\cdots 1\) arrangements.</p>

<p><strong>General principle:</strong> Arrange r objects from n total: there are \(n(n-1)(n-2) \\cdots (n-r+1) = \\frac{n!}{(n-r)!}\) ways (this is the permutation formula \(nPr\)).</p>

<div class="worked-example">
<h4>Example 3: Counting Arrangements</h4>
<p>In how many ways can we arrange the letters A, B, C, D?</p>
<p><strong>Solution:</strong> \(4! = 4 \\times 3 \\times 2 \\times 1 = 24\) ways</p>
</div>

<div class="worked-example">
<h4>Example 4: Partial Arrangements</h4>
<p>How many 3-letter arrangements can be made from {A, B, C, D, E}?</p>
<p><strong>Solution:</strong> First position: 5 choices, second: 4 choices, third: 3 choices. Total: \(5 \\times 4 \\times 3 = 60\)</p>
</div>
"""
    }
]
