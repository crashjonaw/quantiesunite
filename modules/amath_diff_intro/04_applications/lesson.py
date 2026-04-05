TITLE = "Tangent Lines, Normals, and Optimization"

SECTIONS = [
    {
        "title": "Equation of Tangent and Normal Lines",
        "body": """
        <h3>Tangent Line</h3>
        <p>The <strong>tangent line</strong> to $y = f(x)$ at point $(a, f(a))$ has:</p>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>Slope:</strong> $m = f'(a)$</li>
            <li><strong>Equation:</strong> $y - f(a) = f'(a)(x - a)$</li>
        </ul>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> Find the tangent to $y = x^2$ at $x = 2$</p>
            <p>Point: $(2, 4)$</p>
            <p>$f'(x) = 2x$, so $f'(2) = 4$</p>
            <p>Equation: $y - 4 = 4(x - 2)$</p>
            <p><strong>$y = 4x - 4$</strong></p>
        </div>

        <h3>Normal Line</h3>
        <p>The <strong>normal line</strong> is perpendicular to the tangent.</p>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>Slope:</strong> $m = -\\frac{1}{f'(a)}$</li>
            <li><strong>Equation:</strong> $y - f(a) = -\\frac{1}{f'(a)}(x - a)$</li>
        </ul>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> Find the normal to $y = x^2$ at $x = 2$</p>
            <p>Slope of tangent $= 4$, so slope of normal $= -\\frac{1}{4}$</p>
            <p>Equation: $y - 4 = -\\frac{1}{4}(x - 2)$</p>
            <p><strong>$y = -\\frac{1}{4}x + 4.5$</strong></p>
        </div>

        <div class="warning-box formula-box">
            <p><strong>Be careful:</strong> When $f'(a) = 0$, the tangent is horizontal and the normal is vertical (undefined slope).</p>
        </div>
        """
    },
    {
        "title": "Increasing and Decreasing Functions",
        "body": """
        <h3>First Derivative Test</h3>
        <p>The sign of $f'(x)$ tells us where the function increases or decreases:</p>

        <div class="concept-box formula-box">
            <p><strong>$f'(x) > 0$:</strong> $f$ is increasing on that interval</p>
            <p><strong>$f'(x) < 0$:</strong> $f$ is decreasing on that interval</p>
            <p><strong>$f'(x) = 0$:</strong> Critical point (possible max, min, or inflection)</p>
        </div>

        <h3>Critical Points</h3>
        <p>Points where $f'(x) = 0$ or $f'(x)$ is undefined are called <strong>critical points</strong>.</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Find critical points of $f(x) = x^3 - 3x$</p>
            <p>$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 0$</p>
            <p>$x^2 = 1 \\implies x = \\pm 1$</p>
            <p><strong>Critical points: $x = -1$ and $x = 1$</strong></p>
            <p>For $x < -1$: $f'(x) > 0$ (increasing)</p>
            <p>For $-1 < x < 1$: $f'(x) < 0$ (decreasing)</p>
            <p>For $x > 1$: $f'(x) > 0$ (increasing)</p>
        </div>

        <h3>Related Rates</h3>
        <p>When multiple variables change with respect to time, use implicit differentiation:</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> A ladder 10 m long leans against a wall. The base moves away at 2 m/s. How fast is the top sliding down when the base is 6 m from the wall?</p>
            <p>Constraint: $x^2 + y^2 = 100$</p>
            <p>Differentiate w.r.t. time: $2x\\frac{dx}{dt} + 2y\\frac{dy}{dt} = 0$</p>
            <p>When $x = 6$: $y = \\sqrt{100 - 36} = 8$</p>
            <p>$2(6)(2) + 2(8)\\frac{dy}{dt} = 0$</p>
            <p>$24 + 16\\frac{dy}{dt} = 0$</p>
            <p><strong>$\\frac{dy}{dt} = -1.5$ m/s</strong> (top slides down at 1.5 m/s)</p>
        </div>
        """
    },
    {
        "title": "Optimization and Stationary Points",
        "body": """
        <h3>Stationary Points (Critical Points)</h3>
        <p>At a stationary point, $f'(x) = 0$. The tangent is horizontal.</p>

        <h3>Second Derivative Test</h3>
        <p>To determine if a critical point is a max, min, or neither:</p>

        <div class="concept-box formula-box">
            <p>At critical point $x = c$:</p>
            <p><strong>$f''(c) > 0$:</strong> local minimum ($\\cup$ shape)</p>
            <p><strong>$f''(c) < 0$:</strong> local maximum ($\\cap$ shape)</p>
            <p><strong>$f''(c) = 0$:</strong> inconclusive (test further or use first derivative test)</p>
        </div>

        <h3>Optimization Procedure</h3>
        <ol style="margin: 12px 0; line-height: 1.8;">
            <li>Express the quantity to optimize as a function of one variable</li>
            <li>Find the domain (constraints)</li>
            <li>Solve $f'(x) = 0$ for critical points</li>
            <li>Evaluate $f$ at critical points and endpoints</li>
            <li>Compare to find global max/min</li>
        </ol>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> A rectangular box has a square base with side $x$ cm and height $h$ cm. Volume is fixed at 500 cm$^3$. Find dimensions that minimize surface area.</p>
            <p>Volume: $V = x^2 h = 500$, so $h = \\frac{500}{x^2}$</p>
            <p>Surface area: $S = 2x^2 + 4xh = 2x^2 + 4x \\cdot \\frac{500}{x^2} = 2x^2 + \\frac{2000}{x}$</p>
            <p>$\\frac{dS}{dx} = 4x - \\frac{2000}{x^2} = 0$</p>
            <p>$4x = \\frac{2000}{x^2} \\implies x^3 = 500 \\implies x \\approx 7.94$ cm</p>
            <p>$h = \\frac{500}{x^2} \\approx 7.94$ cm</p>
            <p><strong>The optimal box is approximately a cube!</strong></p>
        </div>

        <h3>Absolute vs Local Extrema</h3>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li><strong>Local maximum:</strong> Largest in a neighborhood of that point</li>
            <li><strong>Absolute (global) maximum:</strong> Largest value on the entire domain</li>
            <li>Always check endpoints when optimizing on a closed interval</li>
        </ul>
        """
    }
]
