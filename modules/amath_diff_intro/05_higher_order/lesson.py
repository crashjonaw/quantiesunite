TITLE = "Higher-Order Derivatives and Curve Sketching"

SECTIONS = [
    {
        "title": "Second Derivative and Concavity",
        "body": """
        <h3>Second Derivative</h3>
        <p>The <strong>second derivative</strong> $f''(x)$ measures the rate of change of the slope:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$f''(x) = \\frac{d}{dx}[f'(x)] = \\frac{d^2y}{dx^2}$$</p>
        </div>

        <h3>Concavity</h3>
        <p>The second derivative determines the <strong>concavity</strong> of a curve:</p>

        <div class="concept-box formula-box">
            <p><strong>$f''(x) > 0$:</strong> Curve is concave up ($\\cup$-shaped). The function bends upward.</p>
            <p><strong>$f''(x) < 0$:</strong> Curve is concave down ($\\cap$-shaped). The function bends downward.</p>
            <p><strong>$f''(x) = 0$:</strong> Possible inflection point (change in concavity).</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Analyze concavity of $f(x) = x^3 - 3x^2$</p>
            <p>$f'(x) = 3x^2 - 6x$</p>
            <p>$f''(x) = 6x - 6 = 6(x - 1)$</p>
            <p>$f''(x) = 0$ when $x = 1$ (inflection point)</p>
            <p>For $x < 1$: $f''(x) < 0$ (concave down)</p>
            <p>For $x > 1$: $f''(x) > 0$ (concave up)</p>
        </div>

        <h3>Inflection Points</h3>
        <p>An <strong>inflection point</strong> is where the concavity changes (where $f''(x) = 0$ and sign changes).</p>

        <div class="warning-box formula-box">
            <p><strong>Important:</strong> $f''(x) = 0$ does not automatically mean an inflection point. The concavity must actually change.</p>
        </div>
        """
    },
    {
        "title": "Curve Sketching Strategy",
        "body": """
        <h3>Complete Curve Sketching Procedure</h3>
        <p>To sketch $y = f(x)$:</p>

        <ol style="margin: 12px 0; line-height: 2;">
            <li><strong>Find the domain:</strong> Where is $f$ defined?</li>
            <li><strong>Find intercepts:</strong> Where does $f$ cross axes?</li>
            <li><strong>Analyze symmetry:</strong> Is $f$ even, odd, or neither?</li>
            <li><strong>Find asymptotes:</strong> Vertical and horizontal limits</li>
            <li><strong>Find $f'(x)$:</strong> Determine increasing/decreasing</li>
            <li><strong>Find critical points:</strong> Solve $f'(x) = 0$</li>
            <li><strong>Find $f''(x)$:</strong> Determine concavity</li>
            <li><strong>Find inflection points:</strong> Solve $f''(x) = 0$</li>
            <li><strong>Mark key points:</strong> Plot critical points, inflection points</li>
            <li><strong>Sketch smoothly:</strong> Connect information appropriately</li>
        </ol>

        <h3>Example: Complete Sketch</h3>

        <div class="worked-example formula-box">
            <p><strong>Sketch:</strong> $f(x) = x^3 - 3x^2$</p>
            <p><strong>Domain:</strong> All real numbers</p>
            <p><strong>Intercepts:</strong> $x^3 - 3x^2 = 0 \\implies x^2(x - 3) = 0 \\implies x = 0, 3$</p>
            <p><strong>$f'(x) = 3x^2 - 6x = 3x(x - 2) = 0$ at $x = 0, 2$</strong></p>
            <p>$x < 0$: $f'(x) > 0$ (increasing)</p>
            <p>$0 < x < 2$: $f'(x) < 0$ (decreasing)</p>
            <p>$x > 2$: $f'(x) > 0$ (increasing)</p>
            <p>Local max at $(0, 0)$, local min at $(2, -4)$</p>
            <p><strong>$f''(x) = 6x - 6 = 0$ at $x = 1$</strong></p>
            <p>$x < 1$: $f''(x) < 0$ (concave down)</p>
            <p>$x > 1$: $f''(x) > 0$ (concave up)</p>
            <p>Inflection point at $(1, -2)$</p>
        </div>
        """
    },
    {
        "title": "Implicit Differentiation and Higher Derivatives",
        "body": """
        <h3>Implicit Differentiation</h3>
        <p>When a curve is defined implicitly (e.g., $x^2 + y^2 = 25$), differentiate both sides with respect to $x$, treating $y$ as a function of $x$.</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Find $\\frac{dy}{dx}$ for $x^2 + y^2 = 25$ (circle)</p>
            <p>Differentiate both sides: $2x + 2y\\frac{dy}{dx} = 0$</p>
            <p>$2y\\frac{dy}{dx} = -2x$</p>
            <p><strong>$\\frac{dy}{dx} = -\\frac{x}{y}$</strong></p>
        </div>

        <h3>Third Derivative and Higher</h3>
        <p>Higher derivatives measure increasingly finer details:</p>

        <div class="concept-box formula-box">
            <p><strong>$f'''(x)$:</strong> Rate of change of concavity (rate of change of curvature)</p>
            <p><strong>$f^{(4)}(x)$:</strong> Rate of change of $f'''(x)$</p>
            <p>In physics: if $s$ = position, then</p>
            <p>$v = \\frac{ds}{dt}$ (velocity)</p>
            <p>$a = \\frac{d^2s}{dt^2}$ (acceleration)</p>
            <p>$j = \\frac{d^3s}{dt^3}$ (jerk)</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> For $f(x) = x^4 - 2x^3 + 5x$</p>
            <p>$f'(x) = 4x^3 - 6x^2 + 5$</p>
            <p>$f''(x) = 12x^2 - 12x$</p>
            <p>$f'''(x) = 24x - 12$</p>
            <p>$f^{(4)}(x) = 24$</p>
        </div>

        <h3>Taylor Series (Preview)</h3>
        <p>Higher derivatives are used to approximate functions locally:</p>
        <p>$$f(x) \\approx f(a) + f'(a)(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\cdots$$</p>
        <p>This is the foundation of Taylor series expansions.</p>
        """
    }
]
