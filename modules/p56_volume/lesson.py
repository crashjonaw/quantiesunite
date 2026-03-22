SECTIONS = [
    {
        "title": "Understanding Volume",
        "body": """
<h3>What is Volume?</h3>

<p>Volume measures how much space a 3D object takes up. It tells us how much a container can hold.</p>

<p>Think of volume as the amount of sand, water, or air that can fit inside a shape.</p>

<h3>Units of Volume</h3>

<p>Volume is measured in cubic units.</p>

<div class='example-box'>
<ul>
<li><strong>cm³</strong> (cubic centimetres) - for small objects</li>
<li><strong>m³</strong> (cubic metres) - for large objects</li>
<li><strong>mL</strong> (millilitres) - for liquids (1 mL = 1 cm³)</li>
<li><strong>L</strong> (litres) - for larger liquid amounts (1 L = 1000 mL)</li>
</ul>
</div>

<h3>Visualizing Volume</h3>

<p>A cube with sides 1 cm has a volume of 1 cm³.</p>

<p>A cube with sides 1 m has a volume of 1 m³.</p>

<p><strong>1 m³ = 1,000,000 cm³</strong></p>

<div class='example-box'>
<p>A cube made of 10 smaller cubes in each direction (length, width, height) contains 10 × 10 × 10 = 1000 small cubes total.</p>
</div>
"""
    },
    {
        "title": "Volume of Cubes and Cuboids",
        "body": """
<h3>Volume of a Cube</h3>

<p><strong>Formula: V = s × s × s = s³</strong></p>

<p>Where s = length of one side</p>

<div class='example-box'>
<p><strong>Find the volume of a cube with side 5 cm.</strong></p>
<ul>
<li>V = 5 × 5 × 5 = 125 cm³</li>
</ul>
</div>

<div class='example-box'>
<p><strong>A cube has a volume of 64 cm³. What is the length of each side?</strong></p>
<ul>
<li>s³ = 64</li>
<li>s = ∛64 = 4 cm (because 4 × 4 × 4 = 64)</li>
</ul>
</div>

<h3>Volume of a Cuboid (Rectangular Box)</h3>

<p><strong>Formula: V = length × width × height = l × w × h</strong></p>

<div class='example-box'>
<p><strong>Find the volume of a cuboid with length 8 cm, width 5 cm, and height 3 cm.</strong></p>
<ul>
<li>V = 8 × 5 × 3 = 120 cm³</li>
</ul>
</div>

<div class='example-box'>
<p><strong>A cuboid has length 10 m, width 4 m, and volume 200 m³. What is the height?</strong></p>
<ul>
<li>V = l × w × h</li>
<li>200 = 10 × 4 × h</li>
<li>200 = 40h</li>
<li>h = 200 ÷ 40 = 5 m</li>
</ul>
</div>

<h3>Base Area Method</h3>

<p>We can also think of volume as: <strong>V = Base Area × Height</strong></p>

<div class='example-box'>
<p><strong>A cuboid with a rectangular base of area 24 cm² and height 6 cm.</strong></p>
<ul>
<li>V = Base Area × Height = 24 × 6 = 144 cm³</li>
</ul>
</div>
"""
    },
    {
        "title": "Converting Between Volume Units",
        "body": """
<h3>Converting cm³ to m³</h3>

<p><strong>1 m = 100 cm</strong></p>

<p><strong>1 m³ = 100 × 100 × 100 = 1,000,000 cm³</strong></p>

<div class='example-box'>
<p><strong>Convert 5,000,000 cm³ to m³.</strong></p>
<ul>
<li>m³ = 5,000,000 ÷ 1,000,000 = 5 m³</li>
</ul>
</div>

<div class='example-box'>
<p><strong>Convert 3 m³ to cm³.</strong></p>
<ul>
<li>cm³ = 3 × 1,000,000 = 3,000,000 cm³</li>
</ul>
</div>

<h3>Converting mL and L</h3>

<p><strong>1 mL = 1 cm³</strong></p>

<p><strong>1 L = 1000 mL = 1000 cm³</strong></p>

<div class='example-box'>
<p><strong>A container has a volume of 2500 cm³. How many litres can it hold?</strong></p>
<ul>
<li>mL = 2500 mL (since 1 cm³ = 1 mL)</li>
<li>L = 2500 ÷ 1000 = 2.5 L</li>
</ul>
</div>

<div class='example-box'>
<p><strong>A tank can hold 50 litres. What is its volume in cm³?</strong></p>
<ul>
<li>cm³ = 50 × 1000 = 50,000 cm³</li>
</ul>
</div>

<h3>Conversion Summary</h3>

<div class='example-box'>
<ul>
<li>1 cm³ = 1 mL</li>
<li>1000 cm³ = 1 L</li>
<li>1 m³ = 1000 L</li>
<li>1 m³ = 1,000,000 cm³</li>
</ul>
</div>
"""
    },
    {
        "title": "Volume of Composite Solids",
        "body": """
<h3>What are Composite Solids?</h3>

<p>Composite solids are made by combining two or more simple shapes (cubes and cuboids).</p>

<p><strong>Strategy:</strong> Break the composite solid into simpler shapes, find the volume of each, then add them together.</p>

<div class='example-box'>
<p><strong>An L-shaped solid made of two cuboids.</strong></p>
<p>If we can split it into a vertical cuboid (2 cm × 2 cm × 5 cm) and a horizontal cuboid (4 cm × 2 cm × 2 cm):</p>
<ul>
<li>Volume 1 = 2 × 2 × 5 = 20 cm³</li>
<li>Volume 2 = 4 × 2 × 2 = 16 cm³</li>
<li>Total volume = 20 + 16 = 36 cm³</li>
</ul>
</div>

<h3>Finding Missing Dimensions</h3>

<div class='example-box'>
<p><strong>A composite solid is made of two cuboids joined together. The first cuboid is 3 cm × 4 cm × 5 cm. The second cuboid is 2 cm × 4 cm × h cm. The total volume is 100 cm³. Find h.</strong></p>
<ul>
<li>Volume of first = 3 × 4 × 5 = 60 cm³</li>
<li>Volume of second = 100 - 60 = 40 cm³</li>
<li>40 = 2 × 4 × h</li>
<li>40 = 8h</li>
<li>h = 5 cm</li>
</ul>
</div>

<h3>Subtracting Volumes (Hollowed Shapes)</h3>

<p>For shapes with holes or hollowed sections, find the volume of the outer solid and subtract the volume of the hollow part.</p>

<div class='example-box'>
<p><strong>A cube with side 6 cm has a small cubic hole with side 2 cm drilled through it. What is the remaining volume?</strong></p>
<ul>
<li>Volume of outer cube = 6 × 6 × 6 = 216 cm³</li>
<li>Volume of hole = 2 × 2 × 2 = 8 cm³</li>
<li>Remaining volume = 216 - 8 = 208 cm³</li>
</ul>
</div>
"""
    },
    {
        "title": "Capacity and Real-World Applications",
        "body": """
<h3>What is Capacity?</h3>

<p>Capacity is the maximum amount of liquid or material a container can hold. It's measured in litres or millilitres.</p>

<p><strong>Volume and capacity are related:</strong> If a container has a volume of 1000 cm³, its capacity is 1 L.</p>

<h3>Word Problems with Volume and Capacity</h3>

<div class='example-box'>
<p><strong>A rectangular tank measures 50 cm × 40 cm × 30 cm. How many litres of water can it hold?</strong></p>
<ul>
<li>Volume = 50 × 40 × 30 = 60,000 cm³</li>
<li>Capacity = 60,000 mL = 60 L</li>
</ul>
</div>

<div class='example-box'>
<p><strong>A swimming pool is 25 m long, 10 m wide, and 2 m deep. How much water does it need to fill completely?</strong></p>
<ul>
<li>Volume = 25 × 10 × 2 = 500 m³</li>
<li>In litres = 500 × 1000 = 500,000 L</li>
</ul>
</div>

<h3>Filling and Emptying Problems</h3>

<div class='example-box'>
<p><strong>A tank with capacity 200 L is being filled at a rate of 50 L per minute. How long does it take to fill completely?</strong></p>
<ul>
<li>Time = Capacity ÷ Rate = 200 ÷ 50 = 4 minutes</li>
</ul>
</div>

<div class='example-box'>
<p><strong>A container with volume 120 cm³ is being emptied at a rate of 10 mL per second. How many seconds does it take to empty?</strong></p>
<ul>
<li>Volume in mL = 120 mL</li>
<li>Time = 120 ÷ 10 = 12 seconds</li>
</ul>
</div>

<h3>Comparing Volumes and Capacities</h3>

<div class='example-box'>
<p><strong>Two containers: Container A is 20 cm × 15 cm × 10 cm. Container B is 25 cm × 12 cm × 8 cm. Which container has greater capacity?</strong></p>
<ul>
<li>Container A: 20 × 15 × 10 = 3000 cm³ = 3 L</li>
<li>Container B: 25 × 12 × 8 = 2400 cm³ = 2.4 L</li>
<li>Container A has greater capacity.</li>
</ul>
</div>
"""
    }
]
