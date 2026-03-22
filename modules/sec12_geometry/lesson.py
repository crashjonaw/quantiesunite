SECTIONS = [
    {
        "title": "Angle Properties and Relationships",
        "body": """
<p><strong>Types of Angles:</strong></p>
<ul>
<li><strong>Acute angle:</strong> Less than 90°</li>
<li><strong>Right angle:</strong> Exactly 90° (shown with a small square)</li>
<li><strong>Obtuse angle:</strong> Between 90° and 180°</li>
<li><strong>Straight angle:</strong> Exactly 180° (a straight line)</li>
<li><strong>Reflex angle:</strong> Between 180° and 360°</li>
</ul>

<p><strong>Angle Relationships at a Point:</strong></p>

<div class='example-box'>
<p><strong>Angles on a Straight Line = 180°</strong></p>
<pre class='code-block'>
If angles sit on a straight line, they add to 180°:
a + b + c = 180°

Example: If one angle is 60° and another is 50°,
the third angle = 180° - 60° - 50° = 70°
</pre>
</div>

<div class='example-box'>
<p><strong>Angles Around a Point = 360°</strong></p>
<pre class='code-block'>
If angles surround a point, they add to 360°:
a + b + c + d = 360°

Example: If three angles are 100°, 80°, and 120°,
the fourth angle = 360° - 100° - 80° - 120° = 60°
</pre>
</div>

<p><strong>Vertically Opposite Angles:</strong></p>

<div class='example-box'>
<p><strong>When two lines cross, opposite angles are equal</strong></p>
<pre class='code-block'>
If two straight lines intersect:
      \  /
       \/
       /\
      /  \

The angles opposite each other (vertically opposite)
are always equal.

If one angle is 50°, the opposite angle is also 50°.
If another angle is 130°, its opposite is also 130°.
Check: 50° + 130° = 180° (angles on a line)
</pre>
</div>

<p><strong>Parallel Lines Cut by a Transversal:</strong></p>

<div class='example-box'>
<p><strong>When a line (transversal) cuts two parallel lines:</strong></p>
<pre class='code-block'>
Parallel lines: ========================
Transversal:           /
                      /

The following angle pairs are equal:
1. Corresponding angles (same position at each intersection)
   These are in matching corners

2. Alternate angles (opposite sides of transversal)
   These are on opposite sides, between the parallel lines

3. Co-interior angles (same side of transversal)
   These ADD to 180°

Example: If one corresponding angle is 60°,
the other corresponding angle is also 60°.
</pre>
</div>
"""
    },
    {
        "title": "Triangle Properties",
        "body": """
<p><strong>The Angle Sum Property of Triangles:</strong></p>

<p>One of the most important rules in geometry: <strong>The sum of all angles in any triangle is always 180°</strong></p>

<div class='example-box'>
<p><strong>Proof by Parallel Lines:</strong></p>
<pre class='code-block'>
Consider triangle ABC with angles a, b, and c.

Draw a line parallel to BC through point A.

      E ------A------ F
             /|\
            / | \
           /  |  \
          /   |   \
         B----+----C

Because EAF is parallel to BC:
- Angle EAB = angle ABC (alternate angles)
- Angle FAC = angle ACB (alternate angles)

Angles on the line EF:
angle EAB + angle BAC + angle FAC = 180°

Therefore: angle ABC + angle BAC + angle ACB = 180°
Or: a + b + c = 180°
</pre>
</div>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
If a triangle has angles 50° and 70°, find the third:
50° + 70° + x = 180°
x = 180° - 50° - 70° = 60°

If a triangle has angles x, 2x, and 3x, find each:
x + 2x + 3x = 180°
6x = 180°
x = 30°
The angles are 30°, 60°, and 90°
</pre>
</div>

<p><strong>Types of Triangles:</strong></p>
<ul>
<li><strong>Equilateral:</strong> All three sides equal, all angles 60°</li>
<li><strong>Isosceles:</strong> Two sides equal, two angles equal (base angles)</li>
<li><strong>Scalene:</strong> All sides different, all angles different</li>
<li><strong>Right-angled:</strong> One angle is 90°</li>
</ul>

<p><strong>Exterior Angle of a Triangle:</strong></p>

<div class='example-box'>
<p><strong>An exterior angle equals the sum of the two non-adjacent interior angles</strong></p>
<pre class='code-block'>
       A
      /|
     / |
    /  |
   /   |
  /    |
 B-----C----D (extending BC to D)

Angle ACD (exterior angle) = angle A + angle B

Example:
If angle A = 50° and angle B = 70°,
then exterior angle ACD = 50° + 70° = 120°

This also means angle ACB = 180° - 120° = 60°
Check: 50° + 70° + 60° = 180° ✓
</pre>
</div>
"""
    },
    {
        "title": "Polygon Angle Sums",
        "body": """
<p>For any polygon, there's a formula to find the sum of all interior angles.</p>

<p><strong>The Formula: Sum of Interior Angles = (n - 2) × 180°</strong></p>
<p>where n = number of sides</p>

<div class='example-box'>
<p><strong>Why This Works:</strong></p>
<pre class='code-block'>
Any polygon can be divided into triangles from one vertex.

Triangle (3 sides):
- Can be divided into 1 triangle
- Sum = (3 - 2) × 180° = 1 × 180° = 180°

Quadrilateral (4 sides):
- Can be divided into 2 triangles
- Sum = (4 - 2) × 180° = 2 × 180° = 360°

Pentagon (5 sides):
- Can be divided into 3 triangles
- Sum = (5 - 2) × 180° = 3 × 180° = 540°

Hexagon (6 sides):
- Can be divided into 4 triangles
- Sum = (6 - 2) × 180° = 4 × 180° = 720°

Notice: We always get (n - 2) triangles!
</pre>
</div>

<p><strong>Examples:</strong></p>

<div class='example-box'>
<p><strong>Find the missing angle in a quadrilateral:</strong></p>
<pre class='code-block'>
Sum of angles in quadrilateral = 360°

If three angles are 85°, 95°, and 100°:
85° + 95° + 100° + x = 360°
280° + x = 360°
x = 80°
</pre>
</div>

<div class='example-box'>
<p><strong>Regular Polygons:</strong></p>
<pre class='code-block'>
A regular polygon has all sides equal and all angles equal.

Each interior angle = (n - 2) × 180° / n

Regular triangle (equilateral):
Angle = (3 - 2) × 180° / 3 = 180° / 3 = 60°

Regular quadrilateral (square):
Angle = (4 - 2) × 180° / 4 = 360° / 4 = 90°

Regular pentagon:
Angle = (5 - 2) × 180° / 5 = 540° / 5 = 108°

Regular hexagon:
Angle = (6 - 2) × 180° / 6 = 720° / 6 = 120°
</pre>
</div>

<p><strong>Exterior Angles of a Polygon:</strong></p>

<p><strong>The sum of exterior angles of any polygon is always 360°</strong></p>

<div class='example-box'>
<p><strong>For Regular Polygons:</strong></p>
<pre class='code-block'>
Each exterior angle = 360° / n

Regular pentagon:
Each exterior angle = 360° / 5 = 72°

Regular hexagon:
Each exterior angle = 360° / 6 = 60°

Notice: interior angle + exterior angle = 180°
(They form a straight line)

Square: interior = 90°, exterior = 90°
Check: 90° + 90° = 180° ✓
</pre>
</div>
"""
    },
    {
        "title": "Congruence of Shapes",
        "body": """
<p><strong>Congruent</strong> shapes are exactly the same size and shape. If you cut one out, it would fit perfectly on top of the other.</p>

<p><strong>Congruence Tests for Triangles:</strong></p>
<p>Two triangles are congruent if one of these conditions is true:</p>

<p><strong>1. SSS (Side-Side-Side)</strong></p>
<p>All three sides of one triangle equal all three sides of the other.</p>

<div class='example-box'>
<pre class='code-block'>
Triangle 1: sides 3 cm, 4 cm, 5 cm
Triangle 2: sides 3 cm, 4 cm, 5 cm
These triangles are congruent (SSS)
</pre>
</div>

<p><strong>2. SAS (Side-Angle-Side)</strong></p>
<p>Two sides and the included angle (between them) are equal.</p>

<div class='example-box'>
<pre class='code-block'>
Triangle 1: side = 5 cm, angle = 60°, side = 4 cm
Triangle 2: side = 5 cm, angle = 60°, side = 4 cm
These are congruent (SAS)

The angle MUST be between the two sides.
</pre>
</div>

<p><strong>3. ASA (Angle-Side-Angle)</strong></p>
<p>Two angles and the included side are equal.</p>

<div class='example-box'>
<pre class='code-block'>
Triangle 1: angle = 50°, side = 6 cm, angle = 60°
Triangle 2: angle = 50°, side = 6 cm, angle = 60°
These are congruent (ASA)

The side MUST be between the two angles.
</pre>
</div>

<p><strong>4. RHS (Right angle-Hypotenuse-Side)</strong></p>
<p>For right-angled triangles: the hypotenuse and one other side are equal.</p>

<div class='example-box'>
<pre class='code-block'>
Right triangle 1: hypotenuse = 10 cm, one side = 6 cm
Right triangle 2: hypotenuse = 10 cm, one side = 6 cm
These are congruent (RHS)
</pre>
</div>

<p><strong>Why These Tests Work:</strong></p>
<p>If the required parts match, the triangle's shape is completely determined. You cannot draw a different triangle with the same parts.</p>
"""
    },
    {
        "title": "Similarity of Shapes",
        "body": """
<p><strong>Similar</strong> shapes have the same shape but different sizes. One is an enlargement of the other. All corresponding angles are equal, and all corresponding sides are proportional.</p>

<p><strong>Properties of Similar Shapes:</strong></p>
<ul>
<li>All corresponding angles are equal</li>
<li>All corresponding sides are in the same ratio</li>
<li>The ratio of sides is called the scale factor</li>
</ul>

<div class='example-box'>
<p><strong>Example of Similar Triangles:</strong></p>
<pre class='code-block'>
Triangle A: sides 3 cm, 4 cm, 5 cm
Triangle B: sides 6 cm, 8 cm, 10 cm

Scale factor = 6/3 = 8/4 = 10/5 = 2

Triangle B is an enlargement of Triangle A with scale factor 2.

If triangle A has an angle of 50°,
triangle B also has a 50° angle in the corresponding position.

The triangles are similar.
</pre>
</div>

<p><strong>Tests for Similar Triangles:</strong></p>

<p><strong>1. AAA (Angle-Angle-Angle) or AA (Angle-Angle)</strong></p>
<p>If two angles are equal, the triangles are similar (the third angle must then also be equal).</p>

<p><strong>2. SSS (Side-Side-Side)</strong></p>
<p>If all three sides of one triangle are proportional to all three sides of another, they're similar.</p>

<p><strong>3. SAS (Side-Angle-Side)</strong></p>
<p>If two sides are proportional and the included angle is equal, the triangles are similar.</p>

<div class='example-box'>
<p><strong>Finding Unknown Sides in Similar Triangles:</strong></p>
<pre class='code-block'>
Triangle A: sides 2 cm, 3 cm, and unknown
Triangle B: sides 4 cm, 6 cm, and 5 cm

First, check the scale factor:
4/2 = 2 and 6/3 = 2, so scale factor = 2

Unknown side in A = 5/2 = 2.5 cm

Or: Unknown in A / 5 = 2/4
    Unknown in A = 5 × 2/4 = 2.5 cm
</pre>
</div>

<p><strong>Linear Scale Factor vs Area Scale Factor:</strong></p>

<div class='example-box'>
<p><strong>If shapes are similar with linear scale factor k:</strong></p>
<pre class='code-block'>
Linear scale factor (sides): k
Area scale factor: k²

Example:
Triangle A has area 10 cm²
Triangle B is similar with linear scale factor 3

Area of Triangle B = 10 × 3² = 10 × 9 = 90 cm²

This is because area is two-dimensional!
</pre>
</div>

<p><strong>Difference Between Congruent and Similar:</strong></p>
<ul>
<li><strong>Congruent:</strong> Same size AND same shape (scale factor = 1)</li>
<li><strong>Similar:</strong> Same shape, possibly different sizes (any scale factor)</li>
<li><strong>All congruent shapes are similar, but not all similar shapes are congruent</strong></li>
</ul>
"""
    }
]
