SECTIONS = [
    {
        "title": "Trigonometric Identities",
        "body": """
        <h3>Key Identities</h3>

        <h4>Fundamental Identities</h4>
        <ul>
            <li><strong>Pythagorean:</strong> sin²θ + cos²θ = 1</li>
            <li><strong>Quotient:</strong> tan θ = sin θ / cos θ</li>
            <li><strong>Reciprocal:</strong> csc θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ</li>
        </ul>

        <h4>Double Angle Formulas</h4>
        <ul>
            <li><strong>sin(2θ) = 2sin θ cos θ</strong></li>
            <li><strong>cos(2θ) = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ</strong></li>
            <li><strong>tan(2θ) = 2tan θ / (1 − tan²θ)</strong></li>
        </ul>

        <div class="example-box">
            <p><strong>Example 1:</strong> If sin θ = 3/5 and θ is acute, find sin(2θ)</p>
            <p>cos θ = 4/5 (from Pythagoras)</p>
            <p>sin(2θ) = 2 × (3/5) × (4/5) = 24/25</p>
        </div>

        <h4>Addition Formulas</h4>
        <ul>
            <li><strong>sin(A + B) = sin A cos B + cos A sin B</strong></li>
            <li><strong>sin(A − B) = sin A cos B − cos A sin B</strong></li>
            <li><strong>cos(A + B) = cos A cos B − sin A sin B</strong></li>
            <li><strong>cos(A − B) = cos A cos B + sin A sin B</strong></li>
        </ul>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find sin(75°) = sin(45° + 30°)</p>
            <p>sin(75°) = sin(45°)cos(30°) + cos(45°)sin(30°)</p>
            <p>= (√2/2)(√3/2) + (√2/2)(1/2)</p>
            <p>= (√6 + √2)/4</p>
        </div>

        <h4>Using Identities to Solve Equations</h4>
        <p>Simplify using identities, then solve.</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Solve sin(2θ) = sin θ for 0° ≤ θ ≤ 360°</p>
            <p>2sin θ cos θ = sin θ</p>
            <p>2sin θ cos θ − sin θ = 0</p>
            <p>sin θ (2cos θ − 1) = 0</p>
            <p>sin θ = 0 or cos θ = 1/2</p>
            <p>θ = 0°, 180°, 360° or θ = 60°, 300°</p>
            <p><strong>Solutions: 0°, 60°, 180°, 300°, 360°</strong></p>
        </div>
        """
    },
    {
        "title": "The R-formula (Auxiliary Angle Method)",
        "body": """
        <h3>Converting a sin + b cos to R sin(θ + φ)</h3>
        <p><strong>Formula:</strong> a sin θ + b cos θ = R sin(θ + φ)</p>
        <p>where <strong>R = √(a² + b²)</strong> and <strong>tan φ = b/a</strong></p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Express 3sin θ + 4cos θ in the form R sin(θ + φ)</p>
            <p>R = √(9 + 16) = √25 = 5</p>
            <p>tan φ = 4/3, so φ ≈ 53.1°</p>
            <p><strong>3sin θ + 4cos θ = 5sin(θ + 53.1°)</strong></p>
        </div>

        <h4>Applications</h4>
        <ul>
            <li>Find maximum and minimum values: max = R, min = −R</li>
            <li>Solve trigonometric equations more easily</li>
            <li>Analyze oscillations (amplitudes)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 5:</strong> Find maximum of y = 3sin θ + 4cos θ</p>
            <p>From Example 4: y = 5sin(θ + 53.1°)</p>
            <p><strong>Maximum = 5</strong> (when sin = 1)</p>
            <p><strong>Minimum = −5</strong> (when sin = −1)</p>
        </div>

        <h4>The Cosine Form</h4>
        <p><strong>a sin θ + b cos θ = R cos(θ − α)</strong></p>
        <p>where <strong>R = √(a² + b²)</strong> and <strong>tan α = a/b</strong></p>
        """
    },
    {
        "title": "Solving Trigonometric Equations",
        "body": """
        <h3>Systematic Approach</h3>

        <h4>General Solutions</h4>
        <p>For equations in a given range [0°, 360°]:</p>
        <ul>
            <li><strong>sin θ = k:</strong> θ = sin⁻¹(k) or θ = 180° − sin⁻¹(k)</li>
            <li><strong>cos θ = k:</strong> θ = cos⁻¹(k) or θ = 360° − cos⁻¹(k)</li>
            <li><strong>tan θ = k:</strong> θ = tan⁻¹(k) or θ = 180° + tan⁻¹(k)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 6:</strong> Solve 2cos²θ − 3cos θ + 1 = 0 for 0° ≤ θ ≤ 360°</p>
            <p>Let x = cos θ: 2x² − 3x + 1 = 0</p>
            <p>(2x − 1)(x − 1) = 0</p>
            <p>x = 1/2 or x = 1</p>
            <p>cos θ = 1/2 ⟹ θ = 60° or 300°</p>
            <p>cos θ = 1 ⟹ θ = 0° or 360°</p>
            <p><strong>Solutions: 0°, 60°, 300°, 360°</strong></p>
        </div>

        <h4>Using the R-formula to Solve</h4>
        <p>Convert to single trig function, then solve.</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Solve sin θ + cos θ = 1 for 0° ≤ θ ≤ 360°</p>
            <p>√2 sin(θ + 45°) = 1</p>
            <p>sin(θ + 45°) = 1/√2 = √2/2</p>
            <p>θ + 45° = 45° or θ + 45° = 135°</p>
            <p>θ = 0° or θ = 90°</p>
        </div>

        <h4>Checking for Extraneous Solutions</h4>
        <p>Always verify solutions in the original equation (especially when dividing or manipulating).</p>
        """
    },
    {
        "title": "Inverse Trigonometric Functions",
        "body": """
        <h3>Notation and Domains</h3>
        <ul>
            <li><strong>sin⁻¹(x)</strong> or <strong>arcsin(x):</strong> Range [−90°, 90°] or [−π/2, π/2]</li>
            <li><strong>cos⁻¹(x)</strong> or <strong>arccos(x):</strong> Range [0°, 180°] or [0, π]</li>
            <li><strong>tan⁻¹(x)</strong> or <strong>arctan(x):</strong> Range [−90°, 90°] or [−π/2, π/2]</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 8:</strong> Find sin⁻¹(1/2)</p>
            <p>The angle in [−90°, 90°] whose sine is 1/2 is 30°</p>
            <p>sin⁻¹(1/2) = 30°</p>
        </div>

        <h4>Properties</h4>
        <ul>
            <li>sin(sin⁻¹(x)) = x for −1 ≤ x ≤ 1</li>
            <li>sin⁻¹(sin θ) = θ only if θ ∈ [−90°, 90°]</li>
            <li>sin⁻¹(x) + cos⁻¹(x) = 90° (for 0 ≤ x ≤ 1)</li>
        </ul>

        <h4>Graphs of Inverse Trig Functions</h4>
        <p>The graph of y = sin⁻¹(x) is the reflection of y = sin(x) across the line y = x, restricted to the appropriate range.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Solve sin⁻¹(x) = π/4</p>
            <p>x = sin(π/4) = √2/2</p>
        </div>
        """
    },
    {
        "title": "Trigonometric Series and Equations in Radians",
        "body": """
        <h3>Radians vs. Degrees</h3>
        <p><strong>Radian:</strong> Unit where one full rotation = 2π radians (not 360°)</p>
        <p><strong>Conversion:</strong> θ(radians) = θ(degrees) × π/180</p>

        <h4>Common Angles in Radians</h4>
        <ul>
            <li>30° = π/6, 45° = π/4, 60° = π/3, 90° = π/2</li>
            <li>180° = π, 270° = 3π/2, 360° = 2π</li>
        </ul>

        <h4>Trigonometric Functions of Multiple Angles</h4>
        <p>For equations like sin(nθ) = k, solutions repeat every 2π/n radians.</p>

        <div class="example-box">
            <p><strong>Example 10:</strong> Solve sin(2θ) = 1/2 for 0 ≤ θ < 2π</p>
            <p>2θ = π/6, 5π/6, π/6 + 2π, 5π/6 + 2π, ...</p>
            <p>Within [0, 4π): 2θ = π/6, 5π/6, 13π/6, 17π/6</p>
            <p>θ = π/12, 5π/12, 13π/12, 17π/12</p>
        </div>

        <h4>Periodicity and General Solutions</h4>
        <p>For θ in full range (all real numbers):</p>
        <ul>
            <li>sin(θ) = k: θ = sin⁻¹(k) + 2πn or θ = π − sin⁻¹(k) + 2πn (n ∈ ℤ)</li>
            <li>cos(θ) = k: θ = ±cos⁻¹(k) + 2πn (n ∈ ℤ)</li>
            <li>tan(θ) = k: θ = tan⁻¹(k) + πn (n ∈ ℤ)</li>
        </ul>
        """
    }
]
