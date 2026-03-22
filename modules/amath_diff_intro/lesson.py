SECTIONS = [
    {
        "title": "Limits and the Concept of Derivatives",
        "body": """
        <h3>The Limit Concept</h3>
        <p>The <strong>limit</strong> of a function f(x) as x approaches a is the value f(x) gets arbitrarily close to.</p>

        <p style="text-align: center; font-size: 1.1em;"><strong>lim(x→a) f(x) = L</strong></p>

        <p>This means: as x gets closer and closer to a, f(x) gets closer to L.</p>

        <div class="example-box">
            <p><strong>Example 1:</strong> Find lim(x→2) (x² + 1)</p>
            <p>As x approaches 2, x² + 1 approaches 4 + 1 = 5</p>
            <p>lim(x→2) (x² + 1) = 5</p>
        </div>

        <h3>The Derivative: Instantaneous Rate of Change</h3>
        <p>The <strong>derivative</strong> of f(x) is the instantaneous rate of change of f with respect to x.</p>

        <h4>From First Principles</h4>
        <p style="text-align: center; font-size: 1.1em;">
            <strong>f'(x) = lim(h→0) [f(x+h) − f(x)] / h</strong>
        </p>

        <p>This limit represents the slope of the tangent line to the curve at x.</p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find the derivative of f(x) = x² from first principles</p>
            <p>f'(x) = lim(h→0) [(x+h)² − x²] / h</p>
            <p>= lim(h→0) [x² + 2xh + h² − x²] / h</p>
            <p>= lim(h→0) [2xh + h²] / h</p>
            <p>= lim(h→0) (2x + h)</p>
            <p>= 2x</p>
        </div>

        <h4>Notation</h4>
        <ul>
            <li><strong>f'(x)</strong> or <strong>dy/dx</strong>: derivative of f(x)</li>
            <li><strong>f''(x)</strong> or <strong>d²y/dx²</strong>: second derivative</li>
        </ul>

        <h4>Interpretation</h4>
        <ul>
            <li>f'(x) = slope of tangent to the curve at x</li>
            <li>f'(x) = instantaneous rate of change at x</li>
            <li>If f'(x) > 0: function is increasing</li>
            <li>If f'(x) < 0: function is decreasing</li>
        </ul>
        """
    },
    {
        "title": "Rules of Differentiation",
        "body": """
        <h3>Power Rule</h3>
        <p style="text-align: center; font-size: 1.2em;">
            <strong>If f(x) = xⁿ, then f'(x) = nxⁿ⁻¹</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Differentiate y = x⁵</p>
            <p>dy/dx = 5x⁴</p>
        </div>

        <h3>Constant Multiple Rule</h3>
        <p style="text-align: center;"><strong>d/dx[kf(x)] = k·f'(x)</strong></p>

        <h3>Sum/Difference Rule</h3>
        <p style="text-align: center;"><strong>d/dx[f(x) + g(x)] = f'(x) + g'(x)</strong></p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Differentiate y = 3x⁴ − 2x² + 5</p>
            <p>dy/dx = 3(4x³) − 2(2x) + 0 = 12x³ − 4x</p>
        </div>

        <h3>Product Rule</h3>
        <p style="text-align: center;">
            <strong>d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Differentiate y = (x² + 1)(x − 3)</p>
            <p>f = x² + 1, f' = 2x</p>
            <p>g = x − 3, g' = 1</p>
            <p>dy/dx = 2x(x − 3) + (x² + 1)(1)</p>
            <p>= 2x² − 6x + x² + 1</p>
            <p>= 3x² − 6x + 1</p>
        </div>

        <h3>Quotient Rule</h3>
        <p style="text-align: center;">
            <strong>d/dx[f(x)/g(x)] = [f'(x)g(x) − f(x)g'(x)] / [g(x)]²</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Differentiate y = (3x + 1)/(x² − 2)</p>
            <p>f = 3x + 1, f' = 3</p>
            <p>g = x² − 2, g' = 2x</p>
            <p>dy/dx = [3(x² − 2) − (3x + 1)(2x)] / (x² − 2)²</p>
            <p>= [3x² − 6 − 6x² − 2x] / (x² − 2)²</p>
            <p>= [−3x² − 2x − 6] / (x² − 2)²</p>
        </div>

        <h3>Chain Rule</h3>
        <p style="text-align: center;">
            <strong>dy/dx = dy/du · du/dx</strong>
        </p>

        <p>Or: If y = f(g(x)), then dy/dx = f'(g(x)) · g'(x)</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Differentiate y = (3x² − 1)⁵</p>
            <p>Let u = 3x² − 1, then y = u⁵</p>
            <p>du/dx = 6x, dy/du = 5u⁴</p>
            <p>dy/dx = 5u⁴ · 6x = 5(3x² − 1)⁴ · 6x = 30x(3x² − 1)⁴</p>
        </div>

        <h3>Special Derivatives</h3>
        <ul>
            <li>d/dx[eˣ] = eˣ</li>
            <li>d/dx[ln(x)] = 1/x</li>
            <li>d/dx[sin(x)] = cos(x)</li>
            <li>d/dx[cos(x)] = −sin(x)</li>
            <li>d/dx[tan(x)] = sec²(x)</li>
        </ul>
        """
    },
    {
        "title": "Applications: Tangent Lines and Rates of Change",
        "body": """
        <h3>Equation of a Tangent Line</h3>
        <p>The tangent line to y = f(x) at point (a, f(a)) has slope m = f'(a)</p>

        <p><strong>Equation:</strong> y − f(a) = f'(a)(x − a)</p>

        <div class="example-box">
            <p><strong>Example 8:</strong> Find the tangent to y = x² at x = 2</p>
            <p>f(2) = 4, f'(x) = 2x, so f'(2) = 4</p>
            <p>Tangent line: y − 4 = 4(x − 2)</p>
            <p>y = 4x − 4</p>
        </div>

        <h3>Equation of a Normal Line</h3>
        <p>The normal is perpendicular to the tangent. Its slope is −1/f'(a)</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Find the normal to y = x² at x = 2</p>
            <p>Slope of normal = −1/4</p>
            <p>Normal line: y − 4 = −(1/4)(x − 2)</p>
            <p>y = −(1/4)x + 4.5</p>
        </div>

        <h3>Rates of Change</h3>
        <p>dy/dt represents how y changes with respect to time.</p>

        <div class="example-box">
            <p><strong>Example 10:</strong> A particle's position is s = 5t² − 3t (t in seconds, s in meters). Find velocity at t = 2</p>
            <p>v = ds/dt = 10t − 3</p>
            <p>v(2) = 10(2) − 3 = 17 m/s</p>
            <p>Acceleration: a = dv/dt = 10 m/s²</p>
        </div>

        <h3>Optimization (Maxima and Minima)</h3>
        <p>To find local max/min:</p>
        <ol>
            <li>Find f'(x) = 0 (critical points)</li>
            <li>Use second derivative test: f''(x) > 0 ⟹ min, f''(x) < 0 ⟹ max</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 11:</strong> Find local maxima/minima of f(x) = x³ − 3x</p>
            <p>f'(x) = 3x² − 3 = 0 ⟹ x² = 1 ⟹ x = ±1</p>
            <p>f''(x) = 6x</p>
            <p>At x = 1: f''(1) = 6 > 0 ⟹ local minimum</p>
            <p>At x = −1: f''(−1) = −6 < 0 ⟹ local maximum</p>
        </div>
        """
    },
    {
        "title": "Higher-Order Derivatives and Curve Sketching",
        "body": """
        <h3>Second Derivative</h3>
        <p>The second derivative f''(x) = d/dx[f'(x)] represents the rate of change of the derivative.</p>

        <h4>Concavity</h4>
        <ul>
            <li>f''(x) > 0: curve is concave up (∪)</li>
            <li>f''(x) < 0: curve is concave down (∩)</li>
            <li>f''(x) = 0: inflection point (possible change in concavity)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 12:</strong> Find inflection points of f(x) = x³ − 3x²</p>
            <p>f'(x) = 3x² − 6x</p>
            <p>f''(x) = 6x − 6 = 0 ⟹ x = 1</p>
            <p>f(1) = 1 − 3 = −2</p>
            <p>Inflection point: (1, −2)</p>
        </div>

        <h3>Sketching Curves</h3>
        <p>To sketch y = f(x):</p>
        <ol>
            <li>Find domain and intercepts</li>
            <li>Find f'(x) and determine increasing/decreasing regions</li>
            <li>Find f''(x) and determine concavity</li>
            <li>Mark critical points, inflection points, asymptotes</li>
            <li>Connect the information smoothly</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 13:</strong> Sketch f(x) = x³ − 3x² (from Example 12)</p>
            <ul>
                <li>f'(x) = 3x(x − 2) = 0 at x = 0, 2</li>
                <li>f'(x) > 0 for x < 0 and x > 2 (increasing)</li>
                <li>f'(x) < 0 for 0 < x < 2 (decreasing)</li>
                <li>Local max at (0, 0), local min at (2, −4)</li>
                <li>Inflection at (1, −2)</li>
                <li>Concave down for x < 1, concave up for x > 1</li>
            </ul>
        </div>

        <h3>Higher Derivatives</h3>
        <p>Third derivative: f'''(x) = d/dx[f''(x)]</p>
        <p>Useful in physics: if s = position, then a = dv/dt = d²s/dt² (acceleration), j = da/dt = d³s/dt³ (jerk)</p>
        """
    },
    {
        "title": "Implicit Differentiation and Related Rates",
        "body": """
        <h3>Implicit Differentiation</h3>
        <p>Differentiate both sides with respect to x, treating y as a function of x.</p>

        <div class="example-box">
            <p><strong>Example 14:</strong> Find dy/dx for x² + y² = 25</p>
            <p>Differentiate both sides: 2x + 2y(dy/dx) = 0</p>
            <p>2y(dy/dx) = −2x</p>
            <p><strong>dy/dx = −x/y</strong></p>
        </div>

        <h3>Related Rates Problems</h3>
        <p>Use implicit differentiation when multiple variables change with time.</p>

        <div class="example-box">
            <p><strong>Example 15:</strong> A ladder 10 m long leans against a wall. The base moves away at 2 m/s. How fast is the top sliding down when the base is 6 m from the wall?</p>
            <p>x² + y² = 100 (Pythagoras)</p>
            <p>Differentiate: 2x(dx/dt) + 2y(dy/dt) = 0</p>
            <p>When x = 6: y = √(100 − 36) = 8</p>
            <p>2(6)(2) + 2(8)(dy/dt) = 0</p>
            <p>24 + 16(dy/dt) = 0</p>
            <p><strong>dy/dt = −1.5 m/s</strong> (top moves down at 1.5 m/s)</p>
        </div>
        """
    }
]
