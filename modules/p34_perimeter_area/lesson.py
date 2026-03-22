"""
Perimeter & Area - Lesson Content

Topics covered:
- Perimeter of polygons
- Area of rectangles and squares
- Composite shapes
- Relationship between perimeter and area
"""

SECTIONS = [
    {
        "title": "Understanding Perimeter",
        "body": """
        <h3>What is Perimeter?</h3>
        <p>Perimeter is the <strong>distance around the edge of a shape</strong>. Imagine walking around the outside of a field—the total distance you walk is the perimeter.</p>

        <div class='example-box'>
            <p>A square garden with sides of 4 metres:</p>
            <p>Perimeter = 4 + 4 + 4 + 4 = <strong>16 metres</strong></p>
            <p>You walk 16 metres to go all the way around the garden.</p>
        </div>

        <h3>Calculating Perimeter: The Basic Method</h3>
        <p>To find the perimeter of any polygon, simply <strong>add all the side lengths</strong>:</p>
        <div class='example-box'>
            <p><strong>A triangle with sides 3, 4, and 5 metres:</strong><br>
            Perimeter = 3 + 4 + 5 = <strong>12 metres</strong></p>
            <p><strong>A pentagon with sides 2, 2, 3, 2, 3 metres:</strong><br>
            Perimeter = 2 + 2 + 3 + 2 + 3 = <strong>12 metres</strong></p>
        </div>

        <h3>Perimeter Formulas for Regular Shapes</h3>
        <p>For shapes where all sides are equal, we can use a formula:</p>
        <div class='example-box'>
            <p><strong>Square:</strong> Perimeter = 4 × side<br>
            If side = 5, then P = 4 × 5 = 20</p>
            <p><strong>Equilateral triangle:</strong> Perimeter = 3 × side<br>
            If side = 6, then P = 3 × 6 = 18</p>
        </div>

        <h3>Perimeter of a Rectangle</h3>
        <p>A rectangle has opposite sides that are equal. We can use a special formula:</p>
        <div class='example-box'>
            <p><strong>Formula:</strong> Perimeter = 2 × (length + width) or P = 2L + 2W</p>
            <p><strong>Example:</strong> A rectangle with length 8 and width 5</p>
            <p>P = 2 × (8 + 5) = 2 × 13 = <strong>26</strong></p>
            <p>Or: P = (8 + 8) + (5 + 5) = 16 + 10 = <strong>26</strong></p>
        </div>
        """
    },
    {
        "title": "Understanding Area",
        "body": """
        <h3>What is Area?</h3>
        <p>Area is the <strong>amount of space inside a shape</strong>. It measures how much flat surface the shape covers.</p>

        <div class='example-box'>
            <p>Picture a floor covered with square tiles. The number of tiles is the area!</p>
        </div>

        <h3>Measuring Area: Square Units</h3>
        <p>Area is always measured in square units (like square metres, m², or square centimetres, cm²):</p>
        <div class='example-box'>
            <p>A rectangle 4 metres long and 3 metres wide:</p>
            <p style="text-align: center;">
            ☐☐☐<br>
            ☐☐☐<br>
            ☐☐☐<br>
            ☐☐☐</p>
            <p>We can count: 12 square units, so Area = <strong>12 m²</strong></p>
        </div>

        <h3>Formula for Area of a Rectangle</h3>
        <p>Instead of counting every square, we can use a formula:</p>
        <div class='example-box'>
            <p><strong>Area = length × width</strong> or <strong>A = L × W</strong></p>
            <p><strong>Example:</strong> 8 metres × 5 metres = <strong>40 m²</strong></p>
        </div>

        <h3>Area of a Square</h3>
        <p>A square is a special rectangle where all sides are equal:</p>
        <div class='example-box'>
            <p><strong>Formula:</strong> Area = side × side or A = s²</p>
            <p><strong>Example:</strong> A square with side 6 cm<br>
            Area = 6 × 6 = <strong>36 cm²</strong></p>
        </div>

        <h3>Key Difference: Perimeter vs Area</h3>
        <div class='example-box'>
            <p><strong>Perimeter:</strong> Distance AROUND the shape (measured in units like metres)</p>
            <p><strong>Area:</strong> Space INSIDE the shape (measured in square units like m²)</p>
            <p>A rectangle 10 by 1:<br>
            Perimeter = 2(10+1) = 22 metres<br>
            Area = 10 × 1 = 10 m²</p>
        </div>
        """
    },
    {
        "title": "Area of Composite Shapes",
        "body": """
        <h3>What is a Composite Shape?</h3>
        <p>A composite shape is made up of <strong>two or more simpler shapes</strong> joined together. To find the area, we break it into pieces we know how to measure.</p>

        <h3>Strategy 1: Break into Rectangles</h3>
        <p>Divide the composite shape into separate rectangles, find each area, then add them up:</p>
        <div class='example-box'>
            <p><strong>An L-shaped figure:</strong></p>
            <p>Break it into 2 rectangles:<br>
            Rectangle 1: 5 × 3 = 15 m²<br>
            Rectangle 2: 3 × 2 = 6 m²<br>
            Total Area = 15 + 6 = <strong>21 m²</strong></p>
        </div>

        <h3>Strategy 2: Subtract from a Larger Rectangle</h3>
        <p>Sometimes it's easier to find the area of a large rectangle and subtract the cut-out part:</p>
        <div class='example-box'>
            <p><strong>A rectangle with a rectangular hole:</strong></p>
            <p>Large rectangle: 10 × 8 = 80 m²<br>
            Hole (to subtract): 4 × 3 = 12 m²<br>
            Area = 80 - 12 = <strong>68 m²</strong></p>
        </div>

        <h3>Step-by-Step Example</h3>
        <div class='example-box'>
            <p><strong>Find the area of this L-shape:</strong></p>
            <p>Horizontal part: 8 × 2 = 16 m²<br>
            Vertical part: 3 × 4 = 12 m²<br>
            But wait! We counted the corner twice!</p>
            <p><strong>Better approach:</strong><br>
            Method 1: Top rectangle (8×2=16) + Right rectangle (3×2=6) = 22 m²<br>
            Method 2: Large rectangle (8×4=32) - Cut corner (5×2=10) = 22 m²</p>
        </div>
        """
    },
    {
        "title": "Relationship Between Perimeter and Area",
        "body": """
        <h3>Key Insight: Perimeter and Area Are Independent</h3>
        <p><strong>Shapes with the SAME perimeter can have DIFFERENT areas!</strong><br>
        And shapes with the SAME area can have DIFFERENT perimeters!</p>

        <h3>Example 1: Same Perimeter, Different Areas</h3>
        <div class='example-box'>
            <p><strong>Shape A: Rectangle 5 × 1</strong><br>
            Perimeter = 2(5+1) = 12<br>
            Area = 5 × 1 = 5 m²</p>
            <p><strong>Shape B: Rectangle 4 × 2</strong><br>
            Perimeter = 2(4+2) = 12<br>
            Area = 4 × 2 = 8 m²</p>
            <p>Both have perimeter 12, but A has area 5 m² and B has area 8 m²!</p>
        </div>

        <h3>Example 2: Same Area, Different Perimeters</h3>
        <div class='example-box'>
            <p><strong>Shape C: Rectangle 12 × 1</strong><br>
            Perimeter = 2(12+1) = 26<br>
            Area = 12 × 1 = 12 m²</p>
            <p><strong>Shape D: Rectangle 4 × 3</strong><br>
            Perimeter = 2(4+3) = 14<br>
            Area = 4 × 3 = 12 m²</p>
            <p>Both have area 12 m², but C has perimeter 26 and D has perimeter 14!</p>
        </div>

        <h3>Why Does This Matter?</h3>
        <p>In real life, these are different:</p>
        <ul>
            <li><strong>Perimeter matters for:</strong> Fencing a garden, painting a border, tiling an edge</li>
            <li><strong>Area matters for:</strong> Painting a wall, carpeting a floor, seeding a lawn</li>
        </ul>
        <p>A long, thin garden (high perimeter, low area) needs a lot of fencing but covers little space. A square garden with the same perimeter covers more space!</p>

        <h3>For the Same Area, Which Shape Has the Smallest Perimeter?</h3>
        <p>A <strong>circle or square</strong> has the smallest perimeter for a given area. This is why manhole covers are round—efficient and stronger!</p>
        """
    },
    {
        "title": "Real-World Applications and Problem Solving",
        "body": """
        <h3>Application 1: Fencing a Garden</h3>
        <div class='example-box'>
            <p>You have 40 metres of fencing. You want to make a rectangular garden. What's the maximum area?</p>
            <p>Answer: A square uses space most efficiently. If perimeter = 40, each side = 10.</p>
            <p>Maximum area = 10 × 10 = <strong>100 m²</strong></p>
        </div>

        <h3>Application 2: Painting a Room</h3>
        <div class='example-box'>
            <p>A room is 5 metres by 4 metres with 3-metre ceilings. Paint costs $2 per m². What's the cost to paint all walls?</p>
            <p>Each wall area = perimeter × height = 2(5+4) × 3 = 18 × 3 = 54 m²<br>
            Cost = 54 × $2 = <strong>$108</strong></p>
        </div>

        <h3>Application 3: Tiling a Floor</h3>
        <div class='example-box'>
            <p>A bathroom floor is 3 metres by 2 metres. Tiles are 0.25 m × 0.25 m. How many tiles?</p>
            <p>Floor area = 3 × 2 = 6 m²<br>
            Tile area = 0.25 × 0.25 = 0.0625 m²<br>
            Number of tiles = 6 ÷ 0.0625 = <strong>96 tiles</strong></p>
        </div>

        <h3>Application 4: Composite Real-World Shapes</h3>
        <div class='example-box'>
            <p>A house footprint is rectangular (10m × 8m) with a triangular roof section. Find perimeter for guttering.</p>
            <p>This requires understanding how shapes connect and measuring carefully!</p>
        </div>
        """
    }
]
