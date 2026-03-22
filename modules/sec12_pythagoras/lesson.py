SECTIONS = [
    {
        "title": "Pythagoras' Theorem - Statement and Proof",
        "body": """
<p><strong>Pythagoras' Theorem</strong> is one of the most important theorems in mathematics. It relates the sides of a right-angled triangle.</p>

<p><strong>The Theorem: a² + b² = c²</strong></p>
<p>In a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) equals the sum of the squares of the other two sides.</p>

<div class='example-box'>
<p><strong>Naming the sides:</strong></p>
<pre class='code-block'>
        A
        |\
        | \
      b |  \ c (hypotenuse)
        |   \
        |____\
        C  a  B

The right angle is at C (shown with a square).
Sides a and b are called "legs" or "shorter sides".
Side c is called the "hypotenuse" (always opposite the right angle).

Pythagoras' Theorem: a² + b² = c²
</pre>
</div>

<p><strong>Proof by Area (Rearrangement Proof):</strong></p>

<div class='example-box'>
<p><strong>Visual Proof:</strong></p>
<pre class='code-block'>
Consider a right-angled triangle with legs a and b,
and hypotenuse c.

Create a large square with side length (a + b).

METHOD 1: Calculate the area directly
Area = (a + b)² = a² + 2ab + b²

METHOD 2: Count the contents
The large square contains:
- 4 copies of the right triangle (each with area ab/2)
- 1 square with side c (area = c²)

Total area = 4(ab/2) + c² = 2ab + c²

Since both methods give the same area:
a² + 2ab + b² = 2ab + c²

Subtract 2ab from both sides:
a² + b² = c²

Therefore, Pythagoras' Theorem is proven!
</pre>
</div>

<p><strong>Why Pythagoras' Theorem Is Important:</strong></p>
<ul>
<li>It applies to ANY right-angled triangle</li>
<li>It lets us find unknown side lengths</li>
<li>It helps us check if an angle is a right angle</li>
<li>It's used in construction, navigation, and engineering</li>
</ul>
"""
    },
    {
        "title": "Finding Unknown Sides",
        "body": """
<p>We can use Pythagoras' Theorem to find any unknown side of a right-angled triangle if we know the other two sides.</p>

<p><strong>Finding the Hypotenuse (the longest side):</strong></p>

<div class='example-box'>
<p><strong>Example: Find c</strong></p>
<pre class='code-block'>
A right triangle has legs 3 cm and 4 cm.
Find the hypotenuse.

Using a² + b² = c²:
3² + 4² = c²
9 + 16 = c²
25 = c²
c = √25 = 5 cm

The hypotenuse is 5 cm.
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Find c with decimal answer</strong></p>
<pre class='code-block'>
A right triangle has legs 5 cm and 7 cm.
Find the hypotenuse (to 1 decimal place).

Using a² + b² = c²:
5² + 7² = c²
25 + 49 = c²
74 = c²
c = √74
c ≈ 8.6 cm
</pre>
</div>

<p><strong>Finding One of the Shorter Sides (a leg):</strong></p>

<p>If we know the hypotenuse and one leg, we can find the other leg.</p>
<p>Rearranging: a² = c² - b²</p>

<div class='example-box'>
<p><strong>Example: Find a missing leg</strong></p>
<pre class='code-block'>
A right triangle has hypotenuse 13 cm and one leg 5 cm.
Find the other leg.

Using a² + b² = c²:
a² + 5² = 13²
a² + 25 = 169
a² = 169 - 25
a² = 144
a = √144 = 12 cm

The missing leg is 12 cm.

This is actually the famous 5-12-13 Pythagorean triple!
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Finding a leg with decimal answer</strong></p>
<pre class='code-block'>
A right triangle has hypotenuse 10 cm and one leg 7 cm.
Find the other leg (to 1 decimal place).

Using a² + b² = c²:
7² + b² = 10²
49 + b² = 100
b² = 100 - 49
b² = 51
b = √51
b ≈ 7.1 cm
</pre>
</div>

<p><strong>Step-by-Step Process:</strong></p>
<ol>
<li>Identify which sides are given and which is unknown</li>
<li>Write the formula a² + b² = c² (c is always the hypotenuse)</li>
<li>Substitute the known values</li>
<li>Solve for the unknown (using square roots)</li>
<li>Check your answer makes sense (hypotenuse is always the longest side)</li>
</ol>
"""
    },
    {
        "title": "The Converse and Checking for Right Angles",
        "body": """
<p><strong>The Converse of Pythagoras' Theorem:</strong></p>
<p>If a² + b² = c² for a triangle, then the triangle MUST be right-angled.</p>

<p>This means we can use Pythagoras' Theorem backwards to check if a triangle is right-angled!</p>

<div class='example-box'>
<p><strong>Example 1: Check if a triangle is right-angled</strong></p>
<pre class='code-block'>
A triangle has sides 5 cm, 12 cm, and 13 cm.
Is it right-angled?

Check using the converse of Pythagoras:
The longest side (13) should be the hypotenuse.

5² + 12² = 25 + 144 = 169
13² = 169

Since 5² + 12² = 13², the triangle IS right-angled!
The right angle is opposite the side of length 13 cm.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: A triangle that's NOT right-angled</strong></p>
<pre class='code-block'>
A triangle has sides 3 cm, 4 cm, and 6 cm.
Is it right-angled?

Check: Does 3² + 4² = 6²?
9 + 16 = 25
36 = 36?
25 ≠ 36

The sides don't satisfy Pythagoras' Theorem,
so this triangle is NOT right-angled.

Note: Since 3² + 4² < 6², this is an obtuse triangle
(has one angle larger than 90°).
</pre>
</div>

<p><strong>Three Possibilities:</strong></p>
<ul>
<li>If a² + b² = c²: The triangle is RIGHT-angled</li>
<li>If a² + b² < c²: The triangle is OBTUSE-angled (one angle > 90°)</li>
<li>If a² + b² > c²: The triangle is ACUTE-angled (all angles < 90°)</li>
</ul>

<div class='example-box'>
<p><strong>Distinguishing Triangle Types:</strong></p>
<pre class='code-block'>
Triangle 1: sides 5, 6, 7
Longest side is 7.
5² + 6² = 25 + 36 = 61
7² = 49
61 > 49, so 5² + 6² > 7²
This is ACUTE-angled (all angles are less than 90°)

Triangle 2: sides 3, 7, 8
Longest side is 8.
3² + 7² = 9 + 49 = 58
8² = 64
58 < 64, so 3² + 7² < 8²
This is OBTUSE-angled (one angle is more than 90°)
</pre>
</div>
"""
    },
    {
        "title": "Pythagorean Triples",
        "body": """
<p><strong>A Pythagorean Triple</strong> is a set of three positive whole numbers (integers) that satisfy Pythagoras' Theorem.</p>

<p>These are special because they give whole number answers (no square roots needed).</p>

<p><strong>Common Pythagorean Triples:</strong></p>

<div class='example-box'>
<p><strong>The Most Famous Triples:</strong></p>
<pre class='code-block'>
3-4-5 triple: 3² + 4² = 5²
              9 + 16 = 25 ✓

5-12-13 triple: 5² + 12² = 13²
                25 + 144 = 169 ✓

8-15-17 triple: 8² + 15² = 17²
                64 + 225 = 289 ✓

7-24-25 triple: 7² + 24² = 25²
                49 + 576 = 625 ✓

20-21-29 triple: 20² + 21² = 29²
                 400 + 441 = 841 ✓
</pre>
</div>

<p><strong>Multiples of Pythagorean Triples:</strong></p>
<p>If (a, b, c) is a Pythagorean triple, then (ka, kb, kc) is also a triple for any positive whole number k.</p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
Base triple: 3-4-5

Multiples:
× 2: 6-8-10 (since 6² + 8² = 36 + 64 = 100 = 10²)
× 3: 9-12-15 (since 9² + 12² = 81 + 144 = 225 = 15²)
× 4: 12-16-20
× 5: 15-20-25

Base triple: 5-12-13

Multiples:
× 2: 10-24-26
× 3: 15-36-39
</pre>
</div>

<p><strong>How to Recognize a Pythagorean Triple Problem:</strong></p>
<ul>
<li>The sides are given as whole numbers</li>
<li>The answer comes out as a whole number</li>
<li>No calculator needed - check by mental arithmetic</li>
</ul>

<div class='example-box'>
<p><strong>Example: Using a Pythagorean Triple</strong></p>
<pre class='code-block'>
A right triangle has legs 6 cm and 8 cm.
Find the hypotenuse.

Recognize: This is 2 × the 3-4-5 triple!
Sides: 2×3 = 6, 2×4 = 8, so hypotenuse = 2×5 = 10 cm

Check: 6² + 8² = 36 + 64 = 100 = 10² ✓
</pre>
</div>
"""
    },
    {
        "title": "Applications of Pythagoras' Theorem",
        "body": """
<p>Pythagoras' Theorem is not just for pure mathematics - it has many real-world applications.</p>

<p><strong>Application 1: Distances and Diagonals</strong></p>

<div class='example-box'>
<p><strong>Example: Finding the diagonal of a rectangle</strong></p>
<pre class='code-block'>
A rectangle is 8 metres long and 6 metres wide.
What is the length of the diagonal?

The diagonal splits the rectangle into two
right-angled triangles.

Using Pythagoras:
diagonal² = 8² + 6²
diagonal² = 64 + 36
diagonal² = 100
diagonal = 10 metres
</pre>
</div>

<p><strong>Application 2: Heights and Distances in Real Life</strong></p>

<div class='example-box'>
<p><strong>Example: A ladder against a wall</strong></p>
<pre class='code-block'>
A ladder is 5 metres long.
It rests against a wall, with the base 3 metres
from the wall.
How high up the wall does it reach?

This forms a right triangle:
- Hypotenuse (ladder) = 5 m
- One leg (distance from wall) = 3 m
- Other leg (height) = ?

Using Pythagoras:
3² + height² = 5²
9 + height² = 25
height² = 16
height = 4 metres

The ladder reaches 4 metres up the wall.
</pre>
</div>

<p><strong>Application 3: Distance Between Two Points</strong></p>

<div class='example_box'>
<p><strong>Example: Distance on a map or grid</strong></p>
<pre class='code-block'>
Two towns are:
- 7 km north-south apart
- 24 km east-west apart
What is the straight-line distance?

This forms a right triangle where:
- One leg = 7 km
- Other leg = 24 km
- Hypotenuse = straight-line distance

Using Pythagoras:
distance² = 7² + 24²
distance² = 49 + 576
distance² = 625
distance = 25 km

(Notice: 7-24-25 is a Pythagorean triple!)
</pre>
</div>

<p><strong>Application 4: 3D Problems (Extension)</strong></p>

<div class='example-box'>
<p><strong>Example: Space diagonal in a cuboid</strong></p>
<pre class='code-block'>
A box has dimensions:
Length = 3 m, Width = 4 m, Height = 12 m

Find the space diagonal (from one corner to
the opposite corner through the interior).

First, find the diagonal of the base:
base diagonal² = 3² + 4² = 9 + 16 = 25
base diagonal = 5 m

Then use Pythagoras with the height:
space diagonal² = 5² + 12² = 25 + 144 = 169
space diagonal = 13 m

(Another 5-12-13 triple!)
</pre>
</div>

<p><strong>Steps for Real-World Problems:</strong></p>
<ol>
<li>Draw a diagram</li>
<li>Identify the right angle</li>
<li>Label the sides you know</li>
<li>Apply Pythagoras' Theorem</li>
<li>Check your answer is reasonable</li>
</ol>
"""
    }
]
