TITLE = "Special Cases: Derangements, Stirling Numbers & Applications"

SECTIONS = [
    {
        "title": "Derangements: Complete Displacement",
        "body": """
<h3>What is a Derangement?</h3>
<p>A <strong>derangement</strong> is a permutation where no element appears in its original position. This is useful for problems like "Secret Santa" where no one draws their own name.</p>

<p><strong>Formula for derangements $D(n)$ of $n$ objects:</strong></p>
<p>$$D(n) = n! \\sum_{k=0}^{n} \\frac{(-1)^{k}}{k!}$$</p>

<p>Or equivalently: $D(n) = \\lfloor n!/e + 0.5 \\rfloor$ (round to nearest integer)</p>

<h3>Small Values</h3>
<ul>
<li>$D(1) = 0$ (one object cannot be displaced from itself)</li>
<li>$D(2) = 1$ (swap the two: only one way)</li>
<li>$D(3) = 2$</li>
<li>$D(4) = 9$</li>
<li>$D(5) = 44$</li>
</ul>

<p><strong>Asymptotic approximation:</strong> For large $n$, $D(n) \\approx \\frac{n!}{e} \\approx 0.368 \\times n!$</p>

<div class="worked-example">
<h4>Example 1: Derangement</h4>
<p>Find $D(3)$: all permutations of $\\{1, 2, 3\\}$ where no element is in its original position</p>
<p><strong>Solution:</strong> $D(3) = 3! \\times \\left[1 - \\frac{1}{1!} + \\frac{1}{2!} - \\frac{1}{3!}\\right] = 6 \\times \\left[1 - 1 + \\frac{1}{2} - \\frac{1}{6}\\right] = 6 \\times \\frac{1}{3} = 2$</p>
<p>The derangements are: $(2, 3, 1)$ and $(3, 1, 2)$</p>
</div>
"""
    },
    {
        "title": "Stirling Numbers and Partitions",
        "body": """
<h3>Stirling Numbers of the Second Kind</h3>
<p>$S(n, k)$ counts the number of ways to partition $n$ distinct objects into $k$ non-empty indistinguishable subsets.</p>

<p><strong>Recursive definition:</strong></p>
<p>$$S(n, k) = k \\cdot S(n-1, k) + S(n-1, k-1)$$</p>

<h3>Interpretation of Recurrence</h3>
<p>When adding element $n$ to a partition of the first $n-1$ elements:</p>
<ul>
<li><strong>$k \\cdot S(n-1, k)$:</strong> Element $n$ joins one of $k$ existing subsets ($k$ choices)</li>
<li><strong>$S(n-1, k-1)$:</strong> Element $n$ forms its own new subset</li>
</ul>

<div class="worked-example">
<h4>Example 2: Stirling Numbers</h4>
<p>Find $S(4, 2)$: partition $\\{1, 2, 3, 4\\}$ into 2 non-empty subsets</p>
<p><strong>Solution:</strong> The partitions are:</p>
<ul>
<li>$\\{\\{1\\}, \\{2,3,4\\}\\}$, $\\{\\{2\\}, \\{1,3,4\\}\\}$, $\\{\\{3\\}, \\{1,2,4\\}\\}$, $\\{\\{4\\}, \\{1,2,3\\}\\}$</li>
<li>$\\{\\{1,2\\}, \\{3,4\\}\\}$, $\\{\\{1,3\\}, \\{2,4\\}\\}$, $\\{\\{1,4\\}, \\{2,3\\}\\}$</li>
</ul>
<p>Total: $S(4, 2) = 7$</p>
</div>

<h3>Small Values Table</h3>
<p>$S(4, 1) = 1$, $S(4, 2) = 7$, $S(4, 3) = 6$, $S(4, 4) = 1$</p>
<p>$S(5, 1) = 1$, $S(5, 2) = 15$, $S(5, 3) = 25$, $S(5, 4) = 10$, $S(5, 5) = 1$</p>
"""
    },
    {
        "title": "Applications: Onto Functions and Surjections",
        "body": """
<h3>Onto Functions and Stirling Numbers</h3>
<p>The number of <strong>onto (surjective) functions</strong> from an $n$-element set to a $k$-element set equals:</p>
<p>$$k! \\times S(n, k)$$</p>

<h3>Why This Works</h3>
<ul>
<li>$S(n, k)$ counts unordered partitions of $n$ elements into $k$ non-empty parts</li>
<li>$k!$ accounts for assigning these $k$ parts to $k$ distinguishable target elements</li>
<li>The result: every target element receives at least one preimage (surjection)</li>
</ul>

<div class="worked-example">
<h4>Example 3: Onto Functions</h4>
<p>How many surjective functions exist from a 5-element set to a 3-element set?</p>
<p><strong>Solution:</strong></p>
<p>Number $= 3! \\times S(5, 3) = 6 \\times 25 = 150$</p>
<p>Here $S(5, 3) = 25$ (Stirling number): partition 5 elements into 3 non-empty groups, then assign to 3 target elements in $3! = 6$ ways.</p>
</div>

<h3>Inclusion-Exclusion for Onto Functions</h3>
<p>Alternative formula using inclusion-exclusion:</p>
<p>$$k! \\times S(n, k) = \\sum_{i=0}^{k-1} (-1)^{i} \\binom{k}{i} (k-i)^{n}$$</p>
"""
    }
]
