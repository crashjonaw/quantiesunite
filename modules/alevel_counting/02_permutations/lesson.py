TITLE = "Permutations: Ordered Selections (nPr)"

SECTIONS = [
    {
        "title": "Definition and Formula",
        "body": """
<h3>What is a Permutation?</h3>
<p>A <strong>permutation</strong> of r objects from n distinct objects is an ordered arrangement where order matters and no element repeats.</p>

<p style="text-align: center; font-weight: bold;">\(P(n, r) = nPr = \\frac{n!}{(n-r)!}\)</p>

<h3>Derivation</h3>
<p>Choose the first position (n choices), second (n-1 choices), ..., r-th position (n-r+1 choices).</p>
<p style="text-align: center;">Total: \(n \\times (n-1) \\times \\cdots \\times (n-r+1) = \\frac{n!}{(n-r)!}\)</p>

<div class="worked-example">
<h4>Example 1: Simple Permutation</h4>
<p>How many ways can 3 people be selected from 5 and arranged in a line?</p>
<p><strong>Solution:</strong> \({}_{5}P_3 = \\frac{5!}{(5-3)!} = \\frac{5!}{2!} = \\frac{5 \\times 4 \\times 3 \\times 2 \\times 1}{2 \\times 1} = \\frac{120}{2} = 60\)</p>
</div>

<div class="worked-example">
<h4>Example 2: All Objects</h4>
<p>Arrange all 5 people in a line.</p>
<p><strong>Solution:</strong> \({}_{5}P_5 = 5! = 120\)</p>
</div>
"""
    },
    {
        "title": "Permutations with Constraints",
        "body": """
<h3>Restrictions and Adjacency</h3>
<p>When objects have constraints (must be adjacent, must be separated, etc.), treat connected objects as single units or use complementary counting.</p>

<div class="worked-example">
<h4>Example 3: Adjacency Constraint</h4>
<p>Arrange 5 distinct books on a shelf with book A at one end.</p>
<p><strong>Solution:</strong> Place A at an end (2 choices). Arrange remaining 4 books (\(4! = 24\) ways).</p>
<p>Total: \(2 \\times 24 = 48\)</p>
</div>

<h3>Separation Constraints</h3>
<p>When two objects must NOT be adjacent, use: Total arrangements - (arrangements where they ARE adjacent).</p>

<div class="worked-example">
<h4>Example 4: Separation</h4>
<p>Arrange A, B, C, D, E such that A and B are not adjacent.</p>
<p><strong>Solution:</strong> Total arrangements: \(5! = 120\)<br>
Arrangements with A and B adjacent: treat AB as unit, arrange 4 units: \(4! = 24\), then AB can swap: \(\\times 2 = 48\)<br>
Arrangements with A and B separated: \(120 - 48 = 72\)</p>
</div>
"""
    },
    {
        "title": "Special Cases: Circular and Repeated Elements",
        "body": """
<h3>Circular Permutations</h3>
<p>When arranging n objects in a circle (where rotations are identical), there are <strong>(n-1)! ways</strong>.</p>
<p><strong>Reason:</strong> Fix one object's position to eliminate rotational symmetry, then arrange the remaining n-1.</p>

<div class="worked-example">
<h4>Example 5: Round Table Seating</h4>
<p>Seat 5 people at a round table</p>
<p><strong>Solution:</strong> \((5-1)! = 4! = 24\) arrangements</p>
</div>

<h3>Permutations with Repetition</h3>
<p>When arranging n objects where some are identical:</p>
<p style="text-align: center; font-weight: bold;">\(\\frac{n!}{n_1! \\times n_2! \\times \\cdots \\times n_k!}\)</p>
<p>where \(n_1, n_2, \ldots, n_k\) are the frequencies of each distinct object.</p>

<div class="worked-example">
<h4>Example 6: Letters with Repetition</h4>
<p>Arrange the letters in MISSISSIPPI</p>
<p><strong>Solution:</strong> M(1), I(4), S(4), P(2). Total: 11 letters<br>
Arrangements \(= \\frac{11!}{1! \\times 4! \\times 4! \\times 2!} = \\frac{39916800}{576} = 34650\)</p>
</div>
"""
    }
]
