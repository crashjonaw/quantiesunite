SECTIONS = [
    {
        "title": "Fundamental Counting Principles: Building Blocks",
        "body": """
<h3>Multiplication Principle</h3>
<p>If a task has m ways and a second independent task has n ways, then both tasks together can be done in m × n ways.</p>

<p><strong>General form:</strong> If we have k independent tasks with n₁, n₂, ..., n_k ways respectively, the total number of ways is:</p>
<p style="text-align: center; font-weight: bold;">n₁ × n₂ × ... × n_k</p>

<div class="example-box">
<h4>Example 1: Multiplication Principle</h4>
<p>A restaurant offers 5 appetizers, 8 main courses, and 3 desserts. How many complete meals can be ordered?</p>
<p><strong>Solution:</strong> 5 × 8 × 3 = 120 different meals</p>
</div>

<h3>Addition Principle</h3>
<p>If task A can be done in m mutually exclusive ways and task B in n mutually exclusive ways, then either A or B can be done in m + n ways (provided A and B don't overlap).</p>

<p><strong>Inclusion-Exclusion Principle:</strong> If sets overlap:</p>
<p style="text-align: center; font-weight: bold;">|A ∪ B| = |A| + |B| - |A ∩ B|</p>

<div class="example-box">
<h4>Example 2: Addition Principle</h4>
<p>How many integers from 1 to 100 are divisible by 3 or 5?</p>
<p><strong>Solution:</strong> Divisible by 3: ⌊100/3⌋ = 33
<br>Divisible by 5: ⌊100/5⌋ = 20
<br>Divisible by 15: ⌊100/15⌋ = 6
<br>By inclusion-exclusion: 33 + 20 - 6 = 47
</p>
</div>

<h3>Arrangements Without Repetition</h3>
<p>If we arrange n distinct objects where order matters and no repetition is allowed, there are n! = n(n-1)(n-2)...1 arrangements.</p>

<p><strong>Restriction example:</strong> Arrange r objects from n total: there are n(n-1)(n-2)...(n-r+1) = n!/(n-r)! ways (this is nPr).</p>
"""
    },
    {
        "title": "Permutations: Ordered Selections (nPr)",
        "body": """
<h3>Definition and Formula</h3>
<p>A <strong>permutation</strong> of r objects from n distinct objects is an ordered arrangement.</p>

<p style="text-align: center; font-weight: bold;">P(n, r) = nPr = n!/(n-r)!</p>

<p><strong>Derivation:</strong> Choose the first position (n choices), second (n-1 choices), ..., r-th position (n-r+1 choices).</p>
<p>Total: n × (n-1) × ... × (n-r+1) = n!/(n-r)!</p>

<div class="example-box">
<h4>Example 3: Simple Permutation</h4>
<p>How many ways can 3 people be selected from 5 and arranged in a line?</p>
<p><strong>Solution:</strong> 5P3 = 5!/(5-3)! = 5!/2! = (5 × 4 × 3 × 2 × 1)/(2 × 1) = 60</p>
</div>

<h3>Permutations with Restrictions</h3>

<div class="example-box">
<h4>Example 4: Permutation with Constraints</h4>
<p>Arrange 5 distinct books on a shelf with book A at one end.</p>
<p><strong>Solution:</strong> Place A at an end (2 choices). Arrange remaining 4 books (4! = 24 ways).</p>
<p>Total: 2 × 24 = 48</p>
</div>

<h3>Circular Permutations</h3>
<p>Arranging n objects in a circle: (n-1)! ways (fix one position to account for rotational symmetry).</p>

<div class="example-box">
<h4>Example 5: Circular Arrangement</h4>
<p>Seat 5 people at a round table</p>
<p><strong>Solution:</strong> (5-1)! = 4! = 24 arrangements</p>
</div>

<h3>Permutations with Repetition</h3>
<p>Arrange n objects where some are identical: n!/(n₁! × n₂! × ... × n_k!)</p>

<p>where n₁, n₂, ..., n_k are the frequencies of each distinct object.</p>

<div class="example-box">
<h4>Example 6: Repetition</h4>
<p>Arrange the letters in the word MISSISSIPPI</p>
<p><strong>Solution:</strong> M appears 1 time, I appears 4 times, S appears 4 times, P appears 2 times</p>
<p>Total arrangements: 11!/(1! × 4! × 4! × 2!) = 39916800/576 = 34650</p>
</div>
"""
    },
    {
        "title": "Combinations: Unordered Selections (nCr)",
        "body": """
<h3>Definition and Formula Derivation</h3>
<p>A <strong>combination</strong> of r objects from n distinct objects is an unordered selection.</p>

<p style="text-align: center; font-weight: bold;">C(n, r) = nCr = n!/(r!(n-r)!)</p>

<p><strong>Derivation:</strong> Each combination of r objects can be arranged in r! ways to form permutations.</p>
<p>Since nPr = r! × nCr, we have nCr = nPr/r! = [n!/(n-r)!]/r! = n!/(r!(n-r)!)</p>

<div class="example-box">
<h4>Example 7: Basic Combination</h4>
<p>Choose 3 students from 5 for a committee</p>
<p><strong>Solution:</strong> 5C3 = 5!/(3! × 2!) = (5 × 4 × 3!)/(3! × 2 × 1) = 20/2 = 10</p>
</div>

<h3>Key Properties of Combinations</h3>
<ul>
<li>nC0 = nCn = 1</li>
<li>nCr = nC(n-r) (symmetry: choosing r is like leaving out n-r)</li>
<li>Pascal's identity: nCr = (n-1)C(r-1) + (n-1)Cr</li>
</ul>

<h3>Problems with Restrictions</h3>

<div class="example-box">
<h4>Example 8: Restricted Combination</h4>
<p>Select 4 people from 6 men and 4 women such that at least 2 are women</p>
<p><strong>Solution:</strong> At least 2 women means 2, 3, or 4 women.</p>
<p>2 women, 2 men: 4C2 × 6C2 = 6 × 15 = 90
<br>3 women, 1 man: 4C3 × 6C1 = 4 × 6 = 24
<br>4 women: 4C4 = 1
<br>Total: 90 + 24 + 1 = 115
</p>
</div>

<h3>Binomial Theorem Connection</h3>
<p>The binomial expansion (x + y)^n = Σ(k=0 to n) nCk · x^(n-k) · y^k</p>

<p>The coefficients nCk count the number of ways to choose k items from n (when expanding, choose which k of n terms contribute y).</p>
"""
    },
    {
        "title": "Arrangements and Selections with Restrictions",
        "body": """
<h3>Common Restriction Types</h3>

<p><strong>1. Adjacency constraints:</strong> Certain items must be together</p>

<div class="example-box">
<h4>Example 9: Adjacency</h4>
<p>Arrange 5 people in a row with A and B sitting together</p>
<p><strong>Solution:</strong> Treat A and B as a single unit. Arrange 4 units: 4! = 24 ways. Within the unit, A and B can swap: 2 ways. Total: 24 × 2 = 48</p>
</div>

<p><strong>2. Separation constraints:</strong> Certain items must not be together</p>

<div class="example-box">
<h4>Example 10: Separation</h4>
<p>Arrange A, B, C, D, E such that A and B are not adjacent</p>
<p><strong>Solution:</strong> Total arrangements: 5! = 120
<br>Arrangements with A and B adjacent: 4! × 2 = 48 (treat AB as unit)
<br>Arrangements with A and B separated: 120 - 48 = 72
</p>
</div>

<p><strong>3. Alternating arrangements:</strong> Objects alternate by type</p>

<div class="example-box">
<h4>Example 11: Alternating</h4>
<p>Arrange 3 men and 2 women in a line with alternating genders (man-woman-man-...)</p>
<p><strong>Solution:</strong> Pattern: M-W-M-W-M
<br>Arrange men: 3! = 6
<br>Arrange women in 2 positions: 2! = 2
<br>Total: 6 × 2 = 12
</p>
</div>

<h3>Divisibility and Modular Constraints</h3>
<p>When items must satisfy modular or divisibility conditions, list valid items explicitly and apply counting principles.</p>

<div class="example-box">
<h4>Example 12: Modular Constraint</h4>
<p>Form 3-digit numbers from {1, 2, 3, 4, 5} with distinct digits that are divisible by 2</p>
<p><strong>Solution:</strong> Last digit must be even: 2 or 4 (2 choices)
<br>First digit: 4 remaining choices
<br>Second digit: 3 remaining choices
<br>Total: 4 × 3 × 2 = 24
</p>
</div>
"""
    },
    {
        "title": "Advanced Counting: Derangements and Stirling Numbers",
        "body": """
<h3>Derangements: Complete Displacement</h3>
<p>A <strong>derangement</strong> is a permutation where no element appears in its original position.</p>

<p>Number of derangements D(n) of n objects:</p>
<p style="text-align: center; font-weight: bold;">D(n) = n! × Σ(k=0 to n) (-1)^k / k!</p>

<p>For small n:</p>
<ul>
<li>D(1) = 0</li>
<li>D(2) = 1</li>
<li>D(3) = 2</li>
<li>D(4) = 9</li>
<li>D(5) = 44</li>
</ul>

<p><strong>Approximation:</strong> For large n, D(n) ≈ n!/e ≈ 0.368 × n!</p>

<div class="example-box">
<h4>Example 13: Derangement</h4>
<p>Find D(3) for objects 1, 2, 3 in original positions</p>
<p><strong>Solution:</strong> D(3) = 3! × [1 - 1/1! + 1/2! - 1/3!] = 6 × [1 - 1 + 1/2 - 1/6] = 6 × 1/3 = 2
<br>The derangements are: (2, 3, 1) and (3, 1, 2)
</p>
</div>

<h3>Stirling Numbers of the Second Kind</h3>
<p><strong>S(n, k)</strong> counts the number of ways to partition n distinct objects into k non-empty indistinguishable subsets.</p>

<p><strong>Recursion:</strong> S(n, k) = k·S(n-1, k) + S(n-1, k-1)</p>

<p><strong>Interpretation:</strong> Either element n joins one of k existing subsets [k·S(n-1, k)] or forms its own subset [S(n-1, k-1)].</p>

<div class="example-box">
<h4>Example 14: Stirling Numbers</h4>
<p>Find S(4, 2): partition {1, 2, 3, 4} into 2 non-empty subsets</p>
<p><strong>Solution:</strong> Partitions: {{1}, {2,3,4}}, {{2}, {1,3,4}}, {{3}, {1,2,4}}, {{4}, {1,2,3}}, {{1,2}, {3,4}}, {{1,3}, {2,4}}, {{1,4}, {2,3}}
<br>Total: S(4, 2) = 7
</p>
</div>

<h3>Applications: Onto Functions and Surjections</h3>
<p>The number of onto functions from an n-element set to a k-element set is:</p>
<p style="text-align: center; font-weight: bold;">k! × S(n, k)</p>

<p>This counts ordered partitions (where the k subsets are distinguishable).</p>
"""
    }
]
