SECTIONS = [
    {
        "title": "The Cartesian Plane and Plotting Points",
        "body": """
<p><strong>The Cartesian Coordinate System</strong> is a way of locating points on a plane using two numbers.</p>

<p><strong>The Two Axes:</strong></p>
<ul>
<li><strong>Horizontal axis (x-axis):</strong> Runs left to right</li>
<li><strong>Vertical axis (y-axis):</strong> Runs up and down</li>
<li><strong>Origin:</strong> The point (0, 0) where the axes meet</li>
</ul>

<div class='example-box'>
<p><strong>Coordinates (x, y):</strong></p>
<pre class='code-block'>
A point is located by its coordinates (x, y):
- x is the horizontal distance (left or right)
- y is the vertical distance (up or down)

Coordinates are written as (x, y), e.g., (3, 2)

Positive x: to the right of origin
Negative x: to the left of origin
Positive y: above the origin
Negative y: below the origin

Example points:
(2, 3): 2 right, 3 up
(-1, 4): 1 left, 4 up
(3, -2): 3 right, 2 down
(-2, -3): 2 left, 3 down
(0, 0): at the origin
(3, 0): on x-axis, 3 right
(0, -2): on y-axis, 2 down
</pre>
</div>

<p><strong>Four Quadrants:</strong></p>
<p>The axes divide the plane into four regions:</p>

<div class='example-box'>
<p><strong>Quadrants:</strong></p>
<pre class='code-block'>
        |
    II  |  I
   (-,+)|  (+,+)
--------|--------
   (-,-)|  (+,-)
    III |  IV
        |

Quadrant I: Both x and y positive
Quadrant II: x negative, y positive
Quadrant III: Both x and y negative
Quadrant IV: x positive, y negative

Example:
(2, 3) is in Quadrant I
(-1, 4) is in Quadrant II
(-3, -2) is in Quadrant III
(3, -1) is in Quadrant IV
</pre>
</div>

<p><strong>Distance Between Two Points:</strong></p>
<p>To find the straight-line distance between two points, we use the Distance Formula.</p>

<p><strong>Distance Formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]</strong></p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
The distance between points (x₁, y₁) and (x₂, y₂)
forms the hypotenuse of a right triangle!

Horizontal distance: |x₂ - x₁|
Vertical distance: |y₂ - y₁|

By Pythagoras' Theorem:
d² = (x₂ - x₁)² + (y₂ - y₁)²
d = √[(x₂ - x₁)² + (y₂ - y₁)²]
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Distance between (1, 2) and (4, 6)</strong></p>
<pre class='code-block'>
d = √[(4 - 1)² + (6 - 2)²]
  = √[3² + 4²]
  = √[9 + 16]
  = √25
  = 5

The distance is 5 units.
</pre>
</div>

<p><strong>Midpoint of a Line Segment:</strong></p>
<p>The midpoint is the point halfway between two points.</p>

<p><strong>Midpoint Formula: M = ((x₁ + x₂)/2, (y₁ + y₂)/2)</strong></p>

<div class='example-box'>
<p><strong>Example: Midpoint of (2, 3) and (6, 7)</strong></p>
<pre class='code-block'>
M = ((2 + 6)/2, (3 + 7)/2)
  = (8/2, 10/2)
  = (4, 5)

The midpoint is at (4, 5).

Check: (2,3) to (4,5): 2 right, 2 up
       (4,5) to (6,7): 2 right, 2 up ✓ (equal distances)
</pre>
</div>
"""
    },
    {
        "title": "Gradient (Slope) of a Line",
        "body": """
<p><strong>The Gradient</strong> (or slope) describes how steep a line is. It tells us the rate of change.</p>

<p><strong>Gradient Formula: m = rise/run = (y₂ - y₁)/(x₂ - x₁)</strong></p>

<div class='example-box'>
<p><strong>Understanding Gradient:</strong></p>
<pre class='code-block'>
Gradient = vertical change / horizontal change
         = rise / run
         = change in y / change in x

Positive gradient: Line slopes upward (left to right)
Negative gradient: Line slopes downward (left to right)
Zero gradient: Horizontal line
Undefined gradient: Vertical line
</pre>
</div>

<div class='example-box'>
<p><strong>Example 1: Positive gradient</strong></p>
<pre class='code-block'>
Find gradient of line through (1, 2) and (3, 6)

m = (6 - 2)/(3 - 1)
  = 4/2
  = 2

The gradient is 2.
This means: for every 1 unit right, go 2 units up.
(Or equivalently, for 2 units right, go 4 units up)
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Negative gradient</strong></p>
<pre class='code-block'>
Find gradient of line through (1, 5) and (4, 2)

m = (2 - 5)/(4 - 1)
  = -3/3
  = -1

The gradient is -1.
This means: for every 1 unit right, go 1 unit down.
(The line slopes downward)
</pre>
</div>

<div class='example-box'>
<p><strong>Example 3: Zero gradient</strong></p>
<pre class='code-block'>
Find gradient of line through (1, 3) and (5, 3)

m = (3 - 3)/(5 - 1)
  = 0/4
  = 0

The gradient is 0.
This is a horizontal line (y = 3 for all points)
</pre>
</div>

<p><strong>Gradient and Angles:</strong></p>
<ul>
<li><strong>Gradient = 0:</strong> Horizontal line (angle 0°)</li>
<li><strong>Gradient = 1:</strong> Line at 45° angle</li>
<li><strong>Gradient = -1:</strong> Line at 135° angle (or -45°)</li>
<li><strong>Positive gradient:</strong> Acute angle (less than 90°)</li>
<li><strong>Negative gradient:</strong> Obtuse angle (more than 90°)</li>
</ul>

<p><strong>Parallel and Perpendicular Lines:</strong></p>

<div class='example-box'>
<p><strong>Parallel Lines: Same Gradient</strong></p>
<pre class='code-block'>
Line 1 passes through (0, 1) and (2, 5): m = (5-1)/(2-0) = 2
Line 2 passes through (1, 0) and (2, 2): m = (2-0)/(2-1) = 2

Both have gradient 2, so they're parallel.
</pre>
</div>

<div class='example-box'>
<p><strong>Perpendicular Lines: Gradients are Negative Reciprocals</strong></p>
<pre class='code-block'>
If line 1 has gradient m₁, line 2 is perpendicular if:
m₂ = -1/m₁

Example:
Line 1: gradient = 2
Line 2: gradient = -1/2 (perpendicular)

Check: 2 × (-1/2) = -1 ✓

Line 1: gradient = 3/4
Line 2: gradient = -4/3 (perpendicular)

Check: (3/4) × (-4/3) = -1 ✓
</pre>
</div>
"""
    },
    {
        "title": "Equation of a Line: y = mx + c",
        "body": """
<p><strong>The equation of a straight line can be written as: y = mx + c</strong></p>

<p>where:</p>
<ul>
<li><strong>m</strong> = gradient (slope)</li>
<li><strong>c</strong> = y-intercept (where the line crosses the y-axis)</li>
</ul>

<div class='example-box'>
<p><strong>Understanding y = mx + c:</strong></p>
<pre class='code-block'>
Example: y = 2x + 3

m = 2 (gradient: for every 1 right, go 2 up)
c = 3 (y-intercept: line crosses y-axis at (0, 3))

The line passes through:
- (0, 3): put x = 0, get y = 2(0) + 3 = 3 ✓
- (1, 5): put x = 1, get y = 2(1) + 3 = 5 ✓
- (2, 7): put x = 2, get y = 2(2) + 3 = 7 ✓
- (-1, 1): put x = -1, get y = 2(-1) + 3 = 1 ✓
</pre>
</div>

<p><strong>Finding the Equation of a Line:</strong></p>

<div class='example-box'>
<p><strong>Given gradient and y-intercept:</strong></p>
<pre class='code-block'>
If gradient = 3 and y-intercept = -2:
Equation: y = 3x - 2
</pre>
</div>

<div class='example-box'>
<p><strong>Given two points:</strong></p>
<pre class='code-block'>
Find the equation through (1, 3) and (2, 5)

Step 1: Find gradient
m = (5 - 3)/(2 - 1) = 2/1 = 2

Step 2: Find c using y = mx + c
Use point (1, 3):
3 = 2(1) + c
3 = 2 + c
c = 1

Equation: y = 2x + 1

Check with point (2, 5):
y = 2(2) + 1 = 5 ✓
</pre>
</div>

<div class='example-box'>
<p><strong>Given gradient and a point:</strong></p>
<pre class='code-block'>
Find equation with gradient 3 through point (2, 7)

Step 1: We know m = 3
Step 2: Find c using y = mx + c
7 = 3(2) + c
7 = 6 + c
c = 1

Equation: y = 3x + 1

Check: At x = 2: y = 3(2) + 1 = 7 ✓
</pre>
</div>

<p><strong>Special Cases:</strong></p>

<div class='example-box'>
<p><strong>Horizontal Line (m = 0):</strong></p>
<pre class='code-block'>
y = 0 · x + c
y = c

All points on the line have the same y-coordinate.
Example: y = 5 (a horizontal line at height 5)
</pre>
</div>

<div class='example-box'>
<p><strong>Vertical Line (undefined gradient):</strong></p>
<pre class='code-block'>
Can't use y = mx + c form.
Instead: x = a (constant)

All points on the line have the same x-coordinate.
Example: x = 3 (a vertical line at x = 3)
</pre>
</div>

<p><strong>Rearranging to y = mx + c Form:</strong></p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
2x + y = 5
y = -2x + 5
(gradient = -2, y-intercept = 5)

3x - 2y = 6
-2y = -3x + 6
y = (3/2)x - 3
(gradient = 3/2, y-intercept = -3)

x + y - 4 = 0
y = -x + 4
(gradient = -1, y-intercept = 4)
</pre>
</div>
"""
    },
    {
        "title": "Using Coordinates to Solve Geometric Problems",
        "body": """
<p>Coordinate geometry allows us to solve geometry problems algebraically.</p>

<div class='example-box'>
<p><strong>Example 1: Verify a right angle</strong></p>
<pre class='code-block'>
Triangle with vertices A(0, 0), B(3, 0), C(0, 4)

Check if angle at A is 90°:

Gradient of AB = (0 - 0)/(3 - 0) = 0 (horizontal line)
Gradient of AC = (4 - 0)/(0 - 0) undefined (vertical line)

A horizontal and vertical line are perpendicular.
So angle at A = 90° ✓

Using Pythagoras to verify:
AB = 3 units
AC = 4 units
BC = √[(3-0)² + (0-4)²] = √[9 + 16] = √25 = 5

Check: 3² + 4² = 9 + 16 = 25 = 5² ✓
This is the 3-4-5 Pythagorean triple!
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Check if points are collinear</strong></p>
<pre class='code-block'>
Are points A(1, 2), B(2, 3), C(3, 4) collinear
(do they lie on the same line)?

Gradient AB = (3 - 2)/(2 - 1) = 1/1 = 1
Gradient BC = (4 - 3)/(3 - 2) = 1/1 = 1

Same gradient and share point B, so they're collinear.

Verify with equation:
Using A and B: y = 1·x + c
2 = 1(1) + c, so c = 1
Line equation: y = x + 1

Check C(3, 4): y = 3 + 1 = 4 ✓
Point C lies on the line, so all three are collinear.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 3: Find area of a triangle using coordinates</strong></p>
<pre class='code-block'>
Triangle with vertices A(0, 0), B(4, 0), C(2, 3)

Method 1: Using base and height
Base (on x-axis): from A to B = 4 units
Height: perpendicular distance from C to x-axis = 3 units
Area = (1/2) × base × height = (1/2) × 4 × 3 = 6 square units

Method 2: Using the formula
For triangle with vertices (x₁, y₁), (x₂, y₂), (x₃, y₃):
Area = (1/2)|x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|

Area = (1/2)|0(0 - 3) + 4(3 - 0) + 2(0 - 0)|
     = (1/2)|0 + 12 + 0|
     = (1/2) × 12
     = 6 square units ✓
</pre>
</div>

<div class='example-box'>
<p><strong>Example 4: Find the equation of a line from a graph</strong></p>
<pre class='code-block'>
From a graph, identify two clear points on the line:
Point 1: (1, 1)
Point 2: (3, 5)

Find gradient:
m = (5 - 1)/(3 - 1) = 4/2 = 2

Find y-intercept using point (1, 1):
1 = 2(1) + c
1 = 2 + c
c = -1

Equation: y = 2x - 1

To write in standard form:
y = 2x - 1
-2x + y = -1
2x - y = 1 or 2x - y - 1 = 0
</pre>
</div>

<p><strong>Applications of Coordinate Geometry:</strong></p>
<ul>
<li>Navigation and mapping</li>
<li>Computer graphics and game design</li>
<li>Engineering and architecture</li>
<li>Physics: plotting motion and forces</li>
<li>Economics: supply and demand curves</li>
<li>Statistics: scatter plots and trend lines</li>
</ul>
"""
    }
]
