SECTIONS = [
    {
        "title": "Antiderivatives and Indefinite Integrals",
        "body": """
        <h3>The Antiderivative</h3>
        <p>An <strong>antiderivative</strong> of f(x) is a function F(x) such that F'(x) = f(x).</p>

        <p style="text-align: center;"><strong>If F'(x) = f(x), then F is an antiderivative of f</strong></p>

        <div class="example-box">
            <p><strong>Example 1:</strong> Find an antiderivative of f(x) = 3x²</p>
            <p>We need F(x) such that F'(x) = 3x²</p>
            <p>F(x) = x³ works, because (x³)' = 3x²</p>
        </div>

        <h4>The Indefinite Integral</h4>
        <p>The <strong>indefinite integral</strong> is the family of all antiderivatives:</p>

        <p style="text-align: center; font-size: 1.1em;">
            <strong>∫f(x)dx = F(x) + C</strong>
        </p>

        <p>where C is the <strong>constant of integration</strong>.</p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find ∫3x²dx</p>
            <p>∫3x²dx = x³ + C</p>
            <p>(Check: d/dx[x³ + C] = 3x² ✓)</p>
        </div>

        <h4>Why the Constant?</h4>
        <p>If F(x) is an antiderivative, so is F(x) + C for any constant C, because the derivative of C is 0.</p>

        <h4>Basic Integration Rules</h4>
        <ul>
            <li><strong>Power Rule:</strong> ∫xⁿ dx = x^(n+1)/(n+1) + C (for n ≠ −1)</li>
            <li><strong>Constant Multiple:</strong> ∫kf(x)dx = k∫f(x)dx</li>
            <li><strong>Sum/Difference:</strong> ∫[f(x) + g(x)]dx = ∫f(x)dx + ∫g(x)dx</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 3:</strong> Find ∫(4x³ − 2x + 5)dx</p>
            <p>= 4∫x³dx − 2∫xdx + 5∫1dx</p>
            <p>= 4 · x⁴/4 − 2 · x²/2 + 5x + C</p>
            <p>= x⁴ − x² + 5x + C</p>
        </div>

        <h4>Special Integrals</h4>
        <ul>
            <li>∫eˣ dx = eˣ + C</li>
            <li>∫1/x dx = ln|x| + C</li>
            <li>∫sin(x)dx = −cos(x) + C</li>
            <li>∫cos(x)dx = sin(x) + C</li>
            <li>∫sec²(x)dx = tan(x) + C</li>
        </ul>
        """
    },
    {
        "title": "Definite Integrals and Area Under Curves",
        "body": """
        <h3>The Definite Integral</h3>
        <p>The <strong>definite integral</strong> of f(x) from a to b gives the signed area under the curve:</p>

        <p style="text-align: center; font-size: 1.1em;">
            <strong>∫[a to b] f(x)dx = F(b) − F(a)</strong>
        </p>

        <p>where F is any antiderivative of f. This is the <strong>Fundamental Theorem of Calculus</strong>.</p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Calculate ∫[1 to 3] x² dx</p>
            <p>F(x) = x³/3 (an antiderivative)</p>
            <p>∫[1 to 3] x² dx = [x³/3]₁³ = 27/3 − 1/3 = 26/3</p>
        </div>

        <h4>Interpretation</h4>
        <ul>
            <li>If f(x) ≥ 0 on [a, b]: definite integral = area under the curve</li>
            <li>If f(x) < 0 on [a, b]: definite integral = negative of area above the curve</li>
            <li>For mixed signs: integral = area above x-axis minus area below</li>
        </ul>

        <h4>Properties</h4>
        <ul>
            <li>∫[a to b] f(x)dx = −∫[b to a] f(x)dx (reversing limits negates)</li>
            <li>∫[a to c] f(x)dx = ∫[a to b] f(x)dx + ∫[b to c] f(x)dx (splitting interval)</li>
            <li>∫[a to b] [f(x) + g(x)]dx = ∫[a to b] f(x)dx + ∫[a to b] g(x)dx</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 5:</strong> Find the area under y = 2x from x = 1 to x = 4</p>
            <p>Area = ∫[1 to 4] 2x dx = [x²]₁⁴ = 16 − 1 = 15</p>
        </div>

        <h4>Area Between Two Curves</h4>
        <p>If f(x) ≥ g(x) on [a, b], the area between them is:</p>

        <p style="text-align: center;">
            <strong>Area = ∫[a to b] [f(x) − g(x)]dx</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Find the area between y = x² and y = 2x from x = 0 to x = 2</p>
            <p>First, find which curve is on top. At x = 1: y = 1 for x², y = 2 for 2x. So 2x ≥ x²</p>
            <p>Area = ∫[0 to 2] (2x − x²)dx = [x² − x³/3]₀² = 4 − 8/3 = 4/3</p>
        </div>
        """
    },
    {
        "title": "Integration Techniques",
        "body": """
        <h3>Substitution (u-substitution)</h3>
        <p>For integrals of composite functions, use a substitution u = g(x).</p>

        <h4>Method</h4>
        <ol>
            <li>Let u = g(x)</li>
            <li>Find du = g'(x)dx</li>
            <li>Rewrite integral in terms of u</li>
            <li>Integrate with respect to u</li>
            <li>Substitute back to get answer in x</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 7:</strong> Find ∫(3x + 1)⁵ dx</p>
            <p>Let u = 3x + 1, then du = 3dx, so dx = du/3</p>
            <p>∫(3x + 1)⁵ dx = ∫u⁵ · (du/3) = (1/3)∫u⁵ du</p>
            <p>= (1/3) · u⁶/6 + C = u⁶/18 + C</p>
            <p>= (3x + 1)⁶/18 + C</p>
        </div>

        <h4>For Definite Integrals with Substitution</h4>
        <p>Change the limits of integration when you substitute:</p>

        <div class="example-box">
            <p><strong>Example 8:</strong> Calculate ∫[1 to 2] 2x(x² + 1)³ dx</p>
            <p>Let u = x² + 1, then du = 2x dx</p>
            <p>When x = 1: u = 2; when x = 2: u = 5</p>
            <p>∫[1 to 2] 2x(x² + 1)³ dx = ∫[2 to 5] u³ du = [u⁴/4]₂⁵</p>
            <p>= 625/4 − 16/4 = 609/4</p>
        </div>

        <h3>Integration by Parts</h3>
        <p>For products, use: <strong>∫u dv = uv − ∫v du</strong></p>

        <p>Choose u and dv such that ∫v du is easier to integrate.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Find ∫x eˣ dx</p>
            <p>Let u = x, dv = eˣ dx</p>
            <p>Then du = dx, v = eˣ</p>
            <p>∫x eˣ dx = x eˣ − ∫eˣ dx = x eˣ − eˣ + C = (x − 1)eˣ + C</p>
        </div>
        """
    },
    {
        "title": "Applications of Integration",
        "body": """
        <h3>Finding Area</h3>

        <div class="example-box">
            <p><strong>Example 10:</strong> Find the area enclosed by y = x² − 2x and the x-axis</p>
            <p>First, find x-intercepts: x² − 2x = x(x − 2) = 0, so x = 0, 2</p>
            <p>The parabola is below the x-axis between 0 and 2</p>
            <p>Area = |∫[0 to 2] (x² − 2x)dx| = |[x³/3 − x²]₀²|</p>
            <p>= |8/3 − 4| = |−4/3| = 4/3</p>
        </div>

        <h3>Volume of Solids of Revolution</h3>
        <p>When rotating y = f(x) about the x-axis from a to b:</p>

        <p style="text-align: center;">
            <strong>V = π ∫[a to b] [f(x)]² dx</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Find the volume when y = √x is rotated about the x-axis from x = 0 to x = 4</p>
            <p>V = π ∫[0 to 4] (√x)² dx = π ∫[0 to 4] x dx</p>
            <p>= π [x²/2]₀⁴ = π · 8 = 8π</p>
        </div>

        <h3>Accumulated Change</h3>
        <p>If we know the rate of change f'(t), the total change from t = a to t = b is:</p>

        <p style="text-align: center;">
            <strong>Total Change = ∫[a to b] f'(t) dt = f(b) − f(a)</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 12:</strong> A car's velocity is v(t) = 3t² m/s. How far does it travel from t = 1 to t = 4 seconds?</p>
            <p>Distance = ∫[1 to 4] 3t² dt = [t³]₁⁴ = 64 − 1 = 63 m</p>
        </div>

        <h3>Work Done by a Force</h3>
        <p>Work = ∫[a to b] F(x) dx, where F(x) is force at position x</p>

        <div class="example-box">
            <p><strong>Example 13:</strong> A spring force is F(x) = 5x N. How much work is done compressing the spring 0.2 m?</p>
            <p>Work = ∫[0 to 0.2] 5x dx = [5x²/2]₀^0.2 = 5(0.04)/2 = 0.1 J</p>
        </div>
        """
    },
    {
        "title": "Numerical Integration",
        "body": """
        <h3>The Trapezoidal Rule</h3>
        <p>Approximate ∫[a to b] f(x)dx by dividing [a, b] into n equal intervals.</p>

        <p style="text-align: center;">
            <strong>∫[a to b] f(x)dx ≈ (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]</strong>
        </p>

        <p>where h = (b − a)/n</p>

        <div class="example-box">
            <p><strong>Example 14:</strong> Approximate ∫[0 to 2] e^(−x²) dx using n = 4 intervals</p>
            <p>h = (2 − 0)/4 = 0.5</p>
            <p>x₀ = 0, x₁ = 0.5, x₂ = 1, x₃ = 1.5, x₄ = 2</p>
            <p>f(0) ≈ 1, f(0.5) ≈ 0.778, f(1) ≈ 0.368, f(1.5) ≈ 0.105, f(2) ≈ 0.018</p>
            <p>≈ (0.5/2)[1 + 2(0.778) + 2(0.368) + 2(0.105) + 0.018]</p>
            <p>≈ 0.25 × 3.628 ≈ 0.907</p>
        </div>

        <h3>Simpson's Rule</h3>
        <p>More accurate: fit parabolas instead of straight lines.</p>

        <p style="text-align: center;">
            <strong>∫[a to b] f(x)dx ≈ (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + f(xₙ)]</strong>
        </p>

        <p>Note: n must be even.</p>

        <div class="example-box">
            <p><strong>Example 15:</strong> Using Simpson's Rule with n = 4 for Example 14</p>
            <p>≈ (0.5/3)[1 + 4(0.778) + 2(0.368) + 4(0.105) + 0.018]</p>
            <p>≈ (1/6) × 5.442 ≈ 0.907</p>
        </div>
        """
    }
]
