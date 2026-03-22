"""
Angles & Basic Geometry - Lesson Content

Topics covered:
- Types of angles (acute, right, obtuse, reflex)
- Measuring angles with a protractor
- Angles on a line and at a point
- Properties of angles in common shapes
"""

SECTIONS = [
    {
        "title": "Understanding Angles",
        "body": """
        <h3>What is an Angle?</h3>
        <p>An angle is the <strong>amount of turn between two rays</strong> (lines) that meet at a point called the <strong>vertex</strong>.</p>

        <div class='example-box'>
            <p>Think of an angle like the opening of a door. The door frame and the door are two rays. The hinge is the vertex. The wider the opening, the larger the angle.</p>
        </div>

        <h3>Measuring Angles: Degrees</h3>
        <p>We measure angles in <strong>degrees</strong>, using the symbol °. There are 360° in a complete turn.</p>

        <div class='example-box'>
            <p>Full circle = 360°<br>
            Half turn = 180°<br>
            Quarter turn = 90°</p>
        </div>

        <h3>Types of Angles</h3>
        <p>We classify angles based on their size:</p>

        <div class='example-box'>
            <p><strong>Acute angle:</strong> Less than 90°. Examples: 30°, 45°, 60°</p>
            <p><strong>Right angle:</strong> Exactly 90°. It looks like a corner of a square. We use a small square symbol (⊥) to show it.</p>
            <p><strong>Obtuse angle:</strong> Between 90° and 180°. Examples: 120°, 135°, 150°</p>
            <p><strong>Straight angle:</strong> Exactly 180°. It's a straight line.</p>
            <p><strong>Reflex angle:</strong> Between 180° and 360°. The "outside" angle. Examples: 270°, 300°</p>
        </div>

        <h3>Remember These Key Angles</h3>
        <div class='example-box'>
            <p><strong>Right angle:</strong> 90° (like the corners of a book or window)</p>
            <p><strong>Straight angle:</strong> 180° (a straight line)</p>
            <p><strong>Full rotation:</strong> 360° (one complete turn)</p>
        </div>
        """
    },
    {
        "title": "Measuring Angles with a Protractor",
        "body": """
        <h3>What is a Protractor?</h3>
        <p>A protractor is a semicircular tool marked with degree measurements from 0° to 180°. It helps us measure angles precisely.</p>

        <h3>How to Use a Protractor</h3>
        <p><strong>Step 1: Place the baseline</strong></p>
        <div class='example-box'>
            <p>Put the straight edge of the protractor along one ray of the angle, with the center point (marked with a dot) at the vertex (corner) of the angle.</p>
        </div>

        <p><strong>Step 2: Align with the 0° mark</strong></p>
        <div class='example-box'>
            <p>Make sure the baseline aligns with the 0° marking on the protractor.</p>
        </div>

        <p><strong>Step 3: Find where the other ray crosses</strong></p>
        <div class='example-box'>
            <p>Follow the second ray of the angle until it meets the curved edge of the protractor. Read the number at that point.</p>
        </div>

        <p><strong>Step 4: Read the measurement</strong></p>
        <div class='example-box'>
            <p>Protractors have two sets of numbers. Use the one that's aligned with your first ray's 0° mark. The angle measurement is where the second ray crosses.</p>
        </div>

        <h3>Common Mistakes to Avoid</h3>
        <ul>
            <li>Forgetting to place the center point AT the vertex</li>
            <li>Not aligning the baseline properly with 0°</li>
            <li>Using the wrong scale (there are two sets of numbers!)</li>
            <li>Reading upside down</li>
        </ul>

        <h3>Practice: Estimating Before Measuring</h3>
        <p>Before measuring, guess: Is the angle acute (less than 90°)? Right (90°)? Obtuse (more than 90°)? This helps you check if your protractor reading makes sense.</p>
        """
    },
    {
        "title": "Angles on a Straight Line and at a Point",
        "body": """
        <h3>Angles on a Straight Line</h3>
        <p>All the angles on one side of a straight line always add up to <strong>180°</strong>.</p>

        <div class='example-box'>
            <p>If you have two angles on a straight line:</p>
            <p>Angle A + Angle B = 180°</p>
            <p>If Angle A = 60°, then Angle B = 180° - 60° = 120°</p>
        </div>

        <h3>Angles Around a Point</h3>
        <p>All the angles around a single point always add up to <strong>360°</strong>.</p>

        <div class='example-box'>
            <p>If you have 4 angles around a point:</p>
            <p>Angle A + Angle B + Angle C + Angle D = 360°</p>
        </div>

        <h3>Vertically Opposite Angles</h3>
        <p>When two straight lines cross, they create two pairs of opposite angles. <strong>Vertically opposite angles are always equal!</strong></p>

        <div class='example-box'>
            <p>When two lines cross, if one angle is 65°, the opposite angle is also 65°. The other two angles are both 115° (since 180° - 65° = 115°).</p>
        </div>

        <h3>Using These Rules to Find Unknown Angles</h3>
        <div class='example-box'>
            <p><strong>Problem:</strong> Two angles on a line. One is 75°. What's the other?</p>
            <p><strong>Solution:</strong> 180° - 75° = 105°</p>
            <br>
            <p><strong>Problem:</strong> Four angles around a point. Three are 80°, 90°, and 110°. What's the fourth?</p>
            <p><strong>Solution:</strong> 360° - (80° + 90° + 110°) = 360° - 280° = 80°</p>
        </div>
        """
    },
    {
        "title": "Angles in Common Shapes",
        "body": """
        <h3>Triangles</h3>
        <p><strong>The three angles in any triangle always add up to 180°.</strong></p>

        <div class='example-box'>
            <p><strong>Types of triangles by angles:</strong></p>
            <p><strong>Acute triangle:</strong> All three angles are acute (less than 90°)</p>
            <p><strong>Right triangle:</strong> One angle is 90° (a right angle)</p>
            <p><strong>Obtuse triangle:</strong> One angle is obtuse (between 90° and 180°)</p>
        </div>

        <p>If you know two angles of a triangle, you can find the third:</p>
        <div class='example-box'>
            <p><strong>Example:</strong> A triangle has angles of 60° and 70°. What's the third angle?</p>
            <p>Third angle = 180° - 60° - 70° = 50°</p>
        </div>

        <h3>Quadrilaterals (4-sided shapes)</h3>
        <p><strong>The four angles in any quadrilateral always add up to 360°.</strong></p>

        <div class='example-box'>
            <p><strong>Square:</strong> All 4 angles are 90° each</p>
            <p><strong>Rectangle:</strong> All 4 angles are 90° each</p>
            <p><strong>Rhombus:</strong> Opposite angles are equal</p>
            <p><strong>General quadrilateral:</strong> Angles can vary, but sum to 360°</p>
        </div>

        <h3>Regular Polygons</h3>
        <p>In a <strong>regular polygon</strong>, all sides are equal and all angles are equal:</p>
        <div class='example-box'>
            <p><strong>Equilateral triangle:</strong> Each angle = 180° ÷ 3 = 60°</p>
            <p><strong>Square (regular quadrilateral):</strong> Each angle = 360° ÷ 4 = 90°</p>
            <p><strong>Regular pentagon:</strong> Each angle = 540° ÷ 5 = 108°</p>
            <p><strong>Regular hexagon:</strong> Each angle = 720° ÷ 6 = 120°</p>
        </div>
        """
    },
    {
        "title": "Practical Applications and Problem-Solving",
        "body": """
        <h3>Finding Unknown Angles</h3>
        <div class='example-box'>
            <p><strong>Problem:</strong> Two angles on a straight line are (3x + 10)° and (5x + 20)°. Find x.</p>
            <p><strong>Solution:</strong> (3x + 10) + (5x + 20) = 180<br>
            8x + 30 = 180<br>
            8x = 150<br>
            x = 18.75</p>
        </div>

        <h3>Real-World Applications</h3>
        <ul>
            <li><strong>Navigation:</strong> Angles help us describe direction ("30° north of east")</li>
            <li><strong>Construction:</strong> Right angles are essential for building square corners</li>
            <li><strong>Sports:</strong> Understanding angles in ball trajectories and bounces</li>
            <li><strong>Art:</strong> Angles create perspective and composition</li>
        </ul>

        <h3>Angle Problems Involving Multiple Steps</h3>
        <div class='example-box'>
            <p><strong>Problem:</strong> A triangle has one angle of 45° and another angle that's twice the first. Find all three angles.</p>
            <p><strong>Solution:</strong><br>
            First angle = 45°<br>
            Second angle = 2 × 45° = 90°<br>
            Third angle = 180° - 45° - 90° = 45°<br>
            <strong>Answer: 45°, 90°, 45° (This is a right isosceles triangle!)</strong></p>
        </div>

        <h3>Key Facts to Remember</h3>
        <ul>
            <li>Angles on a straight line = 180°</li>
            <li>Angles around a point = 360°</li>
            <li>Angles in a triangle = 180°</li>
            <li>Angles in a quadrilateral = 360°</li>
            <li>Vertically opposite angles are equal</li>
        </ul>
        """
    }
]
