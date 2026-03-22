SECTIONS = [
    {
        "title": "What are Simultaneous Equations?",
        "body": """
<p>A <strong>simultaneous equation</strong> is a pair (or more) of equations that must be solved at the same time. This means we need to find values for the unknown variables that make ALL equations true at once.</p>

<p>For example, consider these two equations:</p>
<div class='example-box'>
<p><strong>Example:</strong> 2x + y = 5 and x + y = 3</p>
<p>We need to find values of x and y that satisfy BOTH equations. If we try x = 1, y = 2:</p>
<ul>
<li>First equation: 2(1) + 2 = 4 ✗ (should be 5)</li>
<li>Second equation: 1 + 2 = 3 ✓</li>
</ul>
<p>This doesn't work because x = 1, y = 2 doesn't satisfy the first equation.</p>
<p>If we try x = 2, y = 1:</p>
<ul>
<li>First equation: 2(2) + 1 = 5 ✓</li>
<li>Second equation: 2 + 1 = 3 ✓</li>
</ul>
<p>This works! So the solution is x = 2, y = 1.</p>
</div>

<p>Why do we use simultaneous equations? In real life, many problems involve multiple conditions that must be satisfied at the same time. For instance, a business might want to find the price and quantity of items that satisfy both their cost constraints AND their profit targets.</p>

<p><strong>Key Points:</strong></p>
<ul>
<li>We have two (or more) equations with two (or more) unknowns</li>
<li>Each equation represents one condition</li>
<li>The solution must satisfy ALL equations simultaneously</li>
<li>Graphically, the solution is where the lines intersect</li>
</ul>
"""
    },
    {
        "title": "The Elimination Method",
        "body": """
<p>The <strong>elimination method</strong> works by eliminating one variable so we can solve for the other. The key idea is to make the coefficients of one variable the same (or opposite) in both equations, then add or subtract the equations.</p>

<p><strong>Step-by-Step Process:</strong></p>
<ol>
<li>Write both equations clearly</li>
<li>Look for a variable that can be easily eliminated</li>
<li>Multiply one or both equations if needed to make the coefficients of that variable equal (or opposite)</li>
<li>Add or subtract the equations to eliminate that variable</li>
<li>Solve the resulting single-variable equation</li>
<li>Substitute back into one of the original equations to find the other variable</li>
<li>Check your answer in both original equations</li>
</ol>

<div class='example-box'>
<p><strong>Example 1: Eliminate y easily</strong></p>
<pre class='code-block'>
Equation 1: 2x + y = 7
Equation 2: x - y = 2

Notice that the y coefficients are +1 and -1.
Adding these equations eliminates y:

(2x + y) + (x - y) = 7 + 2
2x + x + y - y = 9
3x = 9
x = 3

Now substitute x = 3 into Equation 2:
3 - y = 2
y = 1

Check in Equation 1: 2(3) + 1 = 7 ✓
Check in Equation 2: 3 - 1 = 2 ✓
Solution: x = 3, y = 1
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Multiply equations first</strong></p>
<pre class='code-block'>
Equation 1: 3x + 2y = 11
Equation 2: 2x + y = 7

The y coefficients are 2 and 1. We can:
- Multiply Equation 2 by 2 to make y coefficients equal

Original:     3x + 2y = 11
Multiply Eq 2: 2(2x + y) = 2(7)
               4x + 2y = 14

Now subtract to eliminate y:
(3x + 2y) - (4x + 2y) = 11 - 14
3x - 4x + 2y - 2y = -3
-x = -3
x = 3

Substitute into Equation 2:
2(3) + y = 7
6 + y = 7
y = 1

Check in Equation 1: 3(3) + 2(1) = 11 ✓
Solution: x = 3, y = 1
</pre>
</div>

<p><strong>Why Elimination Works:</strong></p>
<p>When we add or subtract equations, we're using the property that if A = B and C = D, then A + C = B + D. This keeps the equations balanced while eliminating one variable.</p>
"""
    },
    {
        "title": "The Substitution Method",
        "body": """
<p>The <strong>substitution method</strong> works by solving one equation for one variable, then substituting (replacing) that expression into the other equation.</p>

<p><strong>Step-by-Step Process:</strong></p>
<ol>
<li>Choose an equation and solve for one variable (pick the easiest one!)</li>
<li>Write this as an expression (e.g., y = ...)</li>
<li>Substitute this expression into the other equation</li>
<li>Solve the resulting single-variable equation</li>
<li>Substitute back to find the other variable</li>
<li>Check your answer in both original equations</li>
</ol>

<div class='example-box'>
<p><strong>Example 1: Simple substitution</strong></p>
<pre class='code-block'>
Equation 1: y = 2x + 1
Equation 2: x + y = 4

y is already isolated in Equation 1, so substitute
into Equation 2:
x + (2x + 1) = 4
x + 2x + 1 = 4
3x + 1 = 4
3x = 3
x = 1

Substitute back into Equation 1:
y = 2(1) + 1 = 3

Check in Equation 2: 1 + 3 = 4 ✓
Solution: x = 1, y = 3
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Rearrange first</strong></p>
<pre class='code-block'>
Equation 1: 2x + y = 5
Equation 2: x - y = 1

Solve Equation 1 for y:
y = 5 - 2x

Substitute into Equation 2:
x - (5 - 2x) = 1
x - 5 + 2x = 1
3x - 5 = 1
3x = 6
x = 2

Substitute back:
y = 5 - 2(2) = 5 - 4 = 1

Check in Equation 1: 2(2) + 1 = 5 ✓
Check in Equation 2: 2 - 1 = 1 ✓
Solution: x = 2, y = 1
</pre>
</div>

<p><strong>When to Use Substitution:</strong></p>
<ul>
<li>When one equation is already solved for one variable (like y = 2x)</li>
<li>When one variable has a coefficient of 1 or -1 (easier to isolate)</li>
<li>When the coefficients don't have convenient factors for elimination</li>
</ul>

<p><strong>Why Substitution Works:</strong></p>
<p>If y = expression, then wherever y appears, we can replace it with that expression. This is valid because both sides of the equation are equal.</p>
"""
    },
    {
        "title": "Graphical Interpretation",
        "body": """
<p>Each linear equation in two variables represents a straight line on a graph. When we have two equations, we have two lines. The solution to the simultaneous equations is the point where the two lines intersect.</p>

<p><strong>Understanding the Graph:</strong></p>
<ul>
<li>Each equation can be written as y = mx + c (gradient-intercept form)</li>
<li>The solution (x, y) is the coordinate where both lines meet</li>
<li>At this point, both equations are satisfied</li>
</ul>

<div class='example-box'>
<p><strong>Example: Graphical solution</strong></p>
<pre class='code-block'>
Equation 1: y = 2x - 1
Equation 2: y = -x + 2

Let's find where they intersect using algebra:
2x - 1 = -x + 2
3x = 3
x = 1
y = 2(1) - 1 = 1

At x = 1, both equations give y = 1.
The intersection point is (1, 1).

Check:
Equation 1: y = 2(1) - 1 = 1 ✓
Equation 2: y = -(1) + 2 = 1 ✓
</pre>
</div>

<p><strong>Three Possible Outcomes:</strong></p>
<ul>
<li><strong>One intersection point:</strong> The lines cross at one point. There is ONE unique solution.</li>
<li><strong>No intersection (parallel lines):</strong> The lines never meet. The equations have the SAME gradient but different intercepts. NO solution exists.</li>
<li><strong>Infinitely many intersections (same line):</strong> The lines are identical (one equation is a multiple of the other). INFINITELY MANY solutions exist.</li>
</ul>

<div class='example-box'>
<p><strong>Parallel lines (no solution):</strong></p>
<pre class='code-block'>
Equation 1: y = 2x + 1
Equation 2: y = 2x - 3

Both have gradient 2, so they're parallel.
They never meet, so there's no solution.

Using algebra:
2x + 1 = 2x - 3
1 = -3 (impossible!)
</pre>
</div>

<div class='example-box'>
<p><strong>Same line (infinite solutions):</strong></p>
<pre class='code-block'>
Equation 1: 2x + y = 4
Equation 2: 4x + 2y = 8

Equation 2 is just Equation 1 multiplied by 2.
These represent the same line.

Using algebra:
Multiply Equation 1 by 2:
4x + 2y = 8
4x + 2y = 8 (same as Equation 2)
0 = 0 (always true!)

Every point on the line is a solution.
</pre>
</div>

<p><strong>Key Insight:</strong></p>
<p>Graphing helps us visualize whether a solution exists and approximately where it is. Algebra gives us the exact answer.</p>
"""
    },
    {
        "title": "Word Problems with Simultaneous Equations",
        "body": """
<p>Real-world problems often require us to set up simultaneous equations. The key is translating words into mathematical equations.</p>

<p><strong>Steps for Solving Word Problems:</strong></p>
<ol>
<li>Read the problem carefully</li>
<li>Identify what unknowns you need to find (assign variables like x, y)</li>
<li>Write an equation for each piece of information given</li>
<li>Solve the simultaneous equations</li>
<li>Check that your answer makes sense in the context</li>
<li>Write your answer as a sentence</li>
</ol>

<div class='example-box'>
<p><strong>Example 1: Age problem</strong></p>
<p>Alice is twice as old as Bob. Together they are 30 years old. How old is each person?</p>
<pre class='code-block'>
Let a = Alice's age, b = Bob's age

From the problem:
"Alice is twice as old as Bob" → a = 2b
"Together they are 30" → a + b = 30

Substitute a = 2b into the second equation:
2b + b = 30
3b = 30
b = 10

So a = 2(10) = 20

Check: Alice is 20, Bob is 10.
Is Alice twice Bob's age? 20 = 2(10) ✓
Together: 20 + 10 = 30 ✓

Answer: Alice is 20 years old, Bob is 10 years old.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Cost problem</strong></p>
<p>At a café, 2 coffees and 3 muffins cost $15.
1 coffee and 4 muffins cost $13.
Find the price of a coffee and a muffin.</p>
<pre class='code-block'>
Let c = price of coffee, m = price of muffin

From the problem:
"2 coffees and 3 muffins cost $15" → 2c + 3m = 15
"1 coffee and 4 muffins cost $13" → c + 4m = 13

From the second equation:
c = 13 - 4m

Substitute into the first:
2(13 - 4m) + 3m = 15
26 - 8m + 3m = 15
26 - 5m = 15
-5m = -11
m = 2.2

So c = 13 - 4(2.2) = 13 - 8.8 = 4.2

Check:
2(4.2) + 3(2.2) = 8.4 + 6.6 = 15 ✓
4.2 + 4(2.2) = 4.2 + 8.8 = 13 ✓

Answer: A coffee costs $4.20, a muffin costs $2.20.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 3: Speed/distance problem</strong></p>
<p>Two hikers start from opposite ends of a 20 km trail
and walk towards each other. They meet after 2 hours.
One hiker walks 1 km/hour faster than the other.
Find their speeds.</p>
<pre class='code-block'>
Let s₁ = speed of slower hiker, s₂ = speed of faster hiker

When they meet after 2 hours:
Distance covered by hiker 1: 2s₁
Distance covered by hiker 2: 2s₂
Total distance: 2s₁ + 2s₂ = 20

From the problem:
"One walks 1 km/h faster" → s₂ = s₁ + 1

Substitute:
2s₁ + 2(s₁ + 1) = 20
2s₁ + 2s₁ + 2 = 20
4s₁ = 18
s₁ = 4.5 km/h

So s₂ = 4.5 + 1 = 5.5 km/h

Check:
Distance: 2(4.5) + 2(5.5) = 9 + 11 = 20 ✓
Speed difference: 5.5 - 4.5 = 1 ✓

Answer: The slower hiker walks 4.5 km/h,
the faster hiker walks 5.5 km/h.
</pre>
</div>

<p><strong>Common Problem Types:</strong></p>
<ul>
<li><strong>Age problems:</strong> Use relationships between ages</li>
<li><strong>Cost/money problems:</strong> Set up equations from total costs</li>
<li><strong>Speed/distance problems:</strong> Use distance = speed × time</li>
<li><strong>Mixture problems:</strong> Combine items with different properties</li>
<li><strong>Geometry problems:</strong> Use length, area, perimeter relationships</li>
</ul>
"""
    }
]
