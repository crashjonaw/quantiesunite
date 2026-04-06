TITLE = "Problem-Solving Strategies: Combining Counting Techniques"

SECTIONS = [
    {
        "title": "Adjacency and Separation Constraints",
        "body": """
<h3>Common Restriction Types</h3>

<h4>1. Adjacency Constraints: Items Must Be Together</h4>
<p><strong>Strategy:</strong> Treat required adjacent items as a single unit, arrange all units, then account for internal arrangements.</p>

<div class="worked-example">
<h4>Example 1: Adjacency</h4>
<p>Arrange 5 people in a row with persons A and B sitting together</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Treat A and B as a single unit: 4 units to arrange</li>
<li>Arrange 4 units: \(4! = 24\) ways</li>
<li>Within the unit, A and B can swap: \(2! = 2\) ways</li>
<li>Total: \(24 \times 2 = 48\)</li>
</ul>
</div>

<h4>2. Separation Constraints: Items Must NOT Be Together</h4>
<p><strong>Strategy:</strong> Use complementary counting: Total arrangements minus arrangements where they ARE together.</p>

<div class="worked-example">
<h4>Example 2: Separation</h4>
<p>Arrange A, B, C, D, E in a row such that A and B are not adjacent</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Total arrangements: \(5! = 120\)</li>
<li>Arrangements with A and B adjacent: treat AB as unit, \(4! \times 2 = 24 \times 2 = 48\)</li>
<li>Arrangements with A and B separated: \(120 - 48 = 72\)</li>
</ul>
</div>

<h4>3. Alternating Arrangements</h4>
<p><strong>Strategy:</strong> Fix one type's positions, then arrange the other type in remaining positions.</p>

<div class="worked-example">
<h4>Example 3: Alternating</h4>
<p>Arrange 3 men and 2 women in a line with alternating genders (M-W-M-W-M pattern)</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Pattern is fixed: M-W-M-W-M</li>
<li>Arrange 3 men in 3 positions: \(3! = 6\)</li>
<li>Arrange 2 women in 2 positions: \(2! = 2\)</li>
<li>Total: \(6 \times 2 = 12\)</li>
</ul>
</div>
"""
    },
    {
        "title": "Divisibility and Modular Constraints",
        "body": """
<h3>Conditional Selection Based on Properties</h3>

<p><strong>Strategy:</strong> Identify which elements satisfy the constraint, then apply counting principles.</p>

<div class="worked-example">
<h4>Example 4: Divisibility Constraint</h4>
<p>Form 3-digit numbers from {1, 2, 3, 4, 5} with distinct digits that are divisible by 2</p>
<p><strong>Solution:</strong></p>
<ul>
<li>For divisibility by 2, the last digit must be even: 2 or 4 (2 choices)</li>
<li>First digit can be any of remaining 4 elements: 4 choices</li>
<li>Second digit can be any of remaining 3 elements: 3 choices</li>
<li>Total: \(4 \times 3 \times 2 = 24\)</li>
</ul>
</div>

<h3>Multi-Constraint Problems</h3>

<div class="worked-example">
<h4>Example 5: Multiple Constraints</h4>
<p>From {1, 2, 3, 4, 5, 6, 7}, count integers from 100-999 where digits are distinct, the first digit is odd, and the last digit is even</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Last digit (even): choose from {2, 4, 6} → 3 choices</li>
<li>First digit (odd, not used): choose from {1, 3, 5, 7} → 4 choices</li>
<li>Middle digit: choose from remaining 5 digits → 5 choices</li>
<li>Total: \(3 \times 4 \times 5 = 60\)</li>
</ul>
</div>
"""
    },
    {
        "title": "Casework and Combinatorial Arguments",
        "body": """
<h3>Breaking into Cases</h3>

<p>When a problem has multiple scenarios, partition into mutually exclusive cases and sum the counts.</p>

<div class="worked-example">
<h4>Example 6: Casework with Repeated Elements</h4>
<p>How many 4-letter "words" can be formed from MISSISSIPPI, using each letter at most as many times as it appears?</p>
<p><strong>Context:</strong> M(1), I(4), S(4), P(2)</p>
<p><strong>Solution outline:</strong> Choose 4 letters respecting frequencies, then count arrangements.</p>
<ul>
<li>Case M1I3: arrangements \(= 4!/3! = 4\)</li>
<li>Case M1I2S1: arrangements \(= 4!/(2! \times 1! \times 1!) = 12\)</li>
<li>Case M1I2P1: arrangements \(= 4!/2! = 12\)</li>
<li>... (continue for all valid letter compositions)</li>
<li>Sum all cases</li>
</ul>
</div>

<h3>Using Inclusion-Exclusion in Complex Problems</h3>

<div class="worked-example">
<h4>Example 7: Three-Set Inclusion-Exclusion</h4>
<p>Count integers 1-100 divisible by 2, 3, or 5</p>
<p><strong>Solution:</strong></p>
<ul>
<li>Divisible by 2: 50</li>
<li>Divisible by 3: 33</li>
<li>Divisible by 5: 20</li>
<li>Divisible by \(2 \cap 3\) (i.e., 6): 16</li>
<li>Divisible by \(2 \cap 5\) (i.e., 10): 10</li>
<li>Divisible by \(3 \cap 5\) (i.e., 15): 6</li>
<li>Divisible by \(2 \cap 3 \cap 5\) (i.e., 30): 3</li>
</ul>
<p>By inclusion-exclusion: \(50 + 33 + 20 - 16 - 10 - 6 + 3 = 74\)</p>
</div>

<h3>Verification Strategies</h3>
<ul>
<li><strong>Check dimensions:</strong> Does the formula have correct units/structure?</li>
<li><strong>Test edge cases:</strong> What if n=0 or k=1?</li>
<li><strong>Verify complementary counting:</strong> Does (count of A) + (count of not-A) = total?</li>
<li><strong>Use small examples:</strong> Work through with n=3, 4 to verify your approach</li>
</ul>
"""
    }
]
