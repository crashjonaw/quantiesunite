SECTIONS = [
    {
        "title": "Vector Notation and Representation",
        "body": """
        <h3>What is a Vector?</h3>
        <p>A <strong>vector</strong> is a quantity with both magnitude (size) and direction. Vectors differ from scalars (which have only magnitude, like distance or temperature).</p>

        <h4>Vector Representation</h4>
        <p><strong>Column notation:</strong> A vector from point A to point B is written:</p>
        <p style="text-align: center;">⃗AB = <span style="font-size: 1.2em;">(</span><span style="vertical-align: top;">x</span><span style="vertical-align: bottom;">y</span><span style="font-size: 1.2em;">)</span></p>
        <p>This means "x units horizontally and y units vertically"</p>

        <p><strong>Alternative notations:</strong></p>
        <ul>
            <li><strong>Bold:</strong> <strong>v</strong> or <strong>AB</strong></li>
            <li><strong>Arrow:</strong> ⃗v or ⃗AB</li>
            <li><strong>Component form:</strong> (x, y) or ⟨x, y⟩</li>
            <li><strong>Unit vector form:</strong> x<strong>i</strong> + y<strong>j</strong></li>
        </ul>

        <div class="example-box">
            <p><strong>Example 1:</strong> The vector from A(1, 2) to B(4, 6) is:</p>
            <p>⃗AB = (4 − 1, 6 − 2) = (3, 4)</p>
            <p>This means move 3 units right and 4 units up.</p>
        </div>

        <h4>Magnitude of a Vector</h4>
        <p>The magnitude (or length) of vector <strong>v</strong> = (x, y) is:</p>
        <p style="text-align: center;"><strong>|v| = √(x² + y²)</strong></p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find the magnitude of <strong>v</strong> = (3, 4)</p>
            <p>|<strong>v</strong>| = √(3² + 4²) = √(9 + 16) = √25 = 5</p>
        </div>

        <h4>Equal Vectors</h4>
        <p>Two vectors are equal if they have the same magnitude and direction. They don't need to start from the same point.</p>

        <h4>Parallel Vectors</h4>
        <p>Vectors are parallel if one is a scalar multiple of the other: <strong>u</strong> = k<strong>v</strong> (k ≠ 0)</p>

        <p>Geometrically, parallel vectors have the same or opposite directions.</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Are vectors <strong>u</strong> = (2, 4) and <strong>v</strong> = (1, 2) parallel?</p>
            <p><strong>u</strong> = 2<strong>v</strong>, so yes, they are parallel.</p>
        </div>
        """
    },
    {
        "title": "Vector Addition and Subtraction",
        "body": """
        <h3>Basic Vector Operations</h3>

        <h4>Vector Addition</h4>
        <p>To add vectors, add their components:</p>
        <p style="text-align: center;"><strong>(a, b) + (c, d) = (a + c, b + d)</strong></p>

        <p><strong>Geometric interpretation (Triangle Rule):</strong> Place the tail of the second vector at the head of the first. The sum is the vector from the start to the end.</p>

        <p><strong>Parallelogram Rule:</strong> Place vectors tail-to-tail. The sum is the diagonal of the parallelogram.</p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Add vectors <strong>u</strong> = (2, 3) and <strong>v</strong> = (1, −1)</p>
            <p><strong>u</strong> + <strong>v</strong> = (2 + 1, 3 − 1) = (3, 2)</p>
        </div>

        <h4>Vector Subtraction</h4>
        <p>Subtract by adding the negative:</p>
        <p style="text-align: center;"><strong>(a, b) − (c, d) = (a − c, b − d)</strong></p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Subtract <strong>v</strong> = (1, −1) from <strong>u</strong> = (2, 3)</p>
            <p><strong>u</strong> − <strong>v</strong> = (2 − 1, 3 − (−1)) = (1, 4)</p>
        </div>

        <h4>Properties</h4>
        <ul>
            <li><strong>Commutative:</strong> <strong>u</strong> + <strong>v</strong> = <strong>v</strong> + <strong>u</strong></li>
            <li><strong>Associative:</strong> (<strong>u</strong> + <strong>v</strong>) + <strong>w</strong> = <strong>u</strong> + (<strong>v</strong> + <strong>w</strong>)</li>
            <li><strong>Identity:</strong> <strong>u</strong> + <strong>0</strong> = <strong>u</strong> (zero vector)</li>
            <li><strong>Inverse:</strong> <strong>u</strong> + (−<strong>u</strong>) = <strong>0</strong></li>
        </ul>

        <h4>Resultant Vector</h4>
        <p>The sum of multiple vectors is called the <strong>resultant</strong>. Useful in physics for combining forces or velocities.</p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Two forces act on an object: F₁ = (3, 4) N and F₂ = (−1, 2) N. Find the resultant force.</p>
            <p>Resultant = (3, 4) + (−1, 2) = (2, 6) N</p>
            <p>Magnitude = √(4 + 36) = √40 = 2√10 ≈ 6.32 N</p>
        </div>
        """
    },
    {
        "title": "Scalar Multiplication",
        "body": """
        <h3>Scaling Vectors</h3>

        <h4>Scalar Multiplication Definition</h4>
        <p>Multiplying a vector by a scalar k (a real number) stretches or shrinks it:</p>
        <p style="text-align: center;"><strong>k(a, b) = (ka, kb)</strong></p>

        <h4>Properties</h4>
        <ul>
            <li>If k > 1: vector lengthens</li>
            <li>If 0 < k < 1: vector shortens</li>
            <li>If k < 0: vector reverses direction and scales</li>
            <li>If k = 0: result is the zero vector (0, 0)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 7:</strong> If <strong>v</strong> = (2, −3), find 3<strong>v</strong> and −2<strong>v</strong></p>
            <p>3<strong>v</strong> = 3(2, −3) = (6, −9)</p>
            <p>−2<strong>v</strong> = −2(2, −3) = (−4, 6)</p>
        </div>

        <h4>Unit Vectors</h4>
        <p>A <strong>unit vector</strong> has magnitude 1. To convert any vector to a unit vector in the same direction:</p>
        <p style="text-align: center;"><strong>û = v / |v|</strong></p>

        <div class="example-box">
            <p><strong>Example 8:</strong> Find the unit vector in the direction of <strong>v</strong> = (3, 4)</p>
            <p>|<strong>v</strong>| = 5 (from Example 2)</p>
            <p>û = (3/5, 4/5) = (0.6, 0.8)</p>
            <p>Check: |û| = √(0.36 + 0.64) = √1 = 1 ✓</p>
        </div>

        <h4>Standard Unit Vectors</h4>
        <ul>
            <li><strong>i</strong> = (1, 0) — horizontal direction</li>
            <li><strong>j</strong> = (0, 1) — vertical direction</li>
        </ul>

        <p>Any vector can be written as a combination: <strong>v</strong> = a<strong>i</strong> + b<strong>j</strong></p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Express <strong>v</strong> = (−2, 5) using unit vectors</p>
            <p><strong>v</strong> = −2<strong>i</strong> + 5<strong>j</strong></p>
        </div>

        <h4>Properties of Scalar Multiplication</h4>
        <ul>
            <li><strong>Associative:</strong> k(m<strong>v</strong>) = (km)<strong>v</strong></li>
            <li><strong>Distributive:</strong> k(<strong>u</strong> + <strong>v</strong>) = k<strong>u</strong> + k<strong>v</strong></li>
            <li><strong>Distributive:</strong> (k + m)<strong>v</strong> = k<strong>v</strong> + m<strong>v</strong></li>
        </ul>
        """
    },
    {
        "title": "Position Vectors",
        "body": """
        <h3>Vectors from the Origin</h3>

        <h4>Position Vector</h4>
        <p>The <strong>position vector</strong> of a point P(x, y) is the vector from the origin O(0, 0) to P:</p>
        <p style="text-align: center;"><strong>OP⃗ = (x, y)</strong></p>

        <p>This is simply the coordinates of the point treated as a vector.</p>

        <div class="example-box">
            <p><strong>Example 10:</strong> Find the position vector of point A(3, −2)</p>
            <p>Position vector = (3, −2)</p>
        </div>

        <h4>Vector Between Two Points</h4>
        <p>If A and B have position vectors <strong>a</strong> and <strong>b</strong>:</p>
        <p style="text-align: center;"><strong>AB⃗ = b − a</strong></p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Find AB⃗ if A(1, 2) and B(4, 6)</p>
            <p>Position vector of A: <strong>a</strong> = (1, 2)</p>
            <p>Position vector of B: <strong>b</strong> = (4, 6)</p>
            <p><strong>AB⃗</strong> = <strong>b</strong> − <strong>a</strong> = (4, 6) − (1, 2) = (3, 4)</p>
        </div>

        <h4>Finding Points on Lines</h4>
        <p>Points on the line through A with direction <strong>d</strong> can be written as:</p>
        <p style="text-align: center;"><strong>r = a + t·d</strong></p>
        <p>where t is a parameter (can be any real number)</p>

        <div class="example-box">
            <p><strong>Example 12:</strong> Find the equation of the line through A(2, 3) in the direction of <strong>d</strong> = (1, −2)</p>
            <p><strong>r</strong> = (2, 3) + t(1, −2) = (2 + t, 3 − 2t)</p>
            <p>Point at t = 0: (2, 3)</p>
            <p>Point at t = 1: (3, 1)</p>
            <p>Point at t = 2: (4, −1)</p>
        </div>

        <h4>Collinearity</h4>
        <p>Three points A, B, C are collinear if vectors AB⃗ and AC⃗ are parallel.</p>

        <div class="example-box">
            <p><strong>Example 13:</strong> Check if A(1, 2), B(3, 6), C(5, 10) are collinear</p>
            <p><strong>AB⃗</strong> = (2, 4)</p>
            <p><strong>AC⃗</strong> = (4, 8) = 2(2, 4) = 2<strong>AB⃗</strong></p>
            <p>Since AC⃗ = 2·AB⃗, the vectors are parallel, so A, B, C are collinear.</p>
        </div>
        """
    },
    {
        "title": "Dot Product and Applications",
        "body": """
        <h3>Vector Multiplication</h3>

        <h4>Dot Product (Scalar Product)</h4>
        <p>The dot product of vectors <strong>u</strong> = (a, b) and <strong>v</strong> = (c, d) is:</p>
        <p style="text-align: center;"><strong>u · v = ac + bd</strong></p>
        <p>The result is a scalar (a single number), not a vector.</p>

        <div class="example-box">
            <p><strong>Example 14:</strong> Find the dot product of <strong>u</strong> = (2, 3) and <strong>v</strong> = (4, −1)</p>
            <p><strong>u · v</strong> = (2)(4) + (3)(−1) = 8 − 3 = 5</p>
        </div>

        <h4>Geometric Interpretation</h4>
        <p style="text-align: center;"><strong>u · v = |u| |v| cos(θ)</strong></p>
        <p>where θ is the angle between the vectors.</p>

        <h4>Finding the Angle Between Vectors</h4>
        <p style="text-align: center;"><strong>cos(θ) = (u · v) / (|u| |v|)</strong></p>

        <div class="example-box">
            <p><strong>Example 15:</strong> Find the angle between <strong>u</strong> = (1, 0) and <strong>v</strong> = (1, 1)</p>
            <p><strong>u · v</strong> = 1(1) + 0(1) = 1</p>
            <p>|<strong>u</strong>| = 1, |<strong>v</strong>| = √2</p>
            <p>cos(θ) = 1 / (1 × √2) = 1/√2</p>
            <p>θ = 45°</p>
        </div>

        <h4>Perpendicular Vectors</h4>
        <p>Two vectors are perpendicular if and only if their dot product is zero:</p>
        <p style="text-align: center;"><strong>u ⊥ v ⟺ u · v = 0</strong></p>

        <div class="example-box">
            <p><strong>Example 16:</strong> Are <strong>u</strong> = (2, 3) and <strong>v</strong> = (3, −2) perpendicular?</p>
            <p><strong>u · v</strong> = (2)(3) + (3)(−2) = 6 − 6 = 0</p>
            <p>Yes, they are perpendicular.</p>
        </div>

        <h4>Properties of Dot Product</h4>
        <ul>
            <li><strong>Commutative:</strong> <strong>u · v = v · u</strong></li>
            <li><strong>Distributive:</strong> <strong>u · (v + w) = u · v + u · w</strong></li>
            <li><strong>Scalar:</strong> (k<strong>u</strong>) · <strong>v</strong> = k(<strong>u · v</strong>)</li>
            <li><strong>Self-product:</strong> <strong>u · u = |u|²</strong></li>
        </ul>
        """
    }
]
