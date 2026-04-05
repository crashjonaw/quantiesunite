TITLE = "Power Rule and Differentiation Rules"

SECTIONS = [
    {
        "title": "The Power Rule",
        "body": """
        <h3>Power Rule</h3>
        <p>If $f(x) = x^n$ where $n$ is any real number, then:</p>

        <div class="concept-box" style="text-align: center; font-size: 1.15em; padding: 16px; margin: 12px 0">
            <p>$$\\frac{d}{dx}[x^n] = nx^{n-1}$$</p>
        </div>

        <div class="success-box formula-box">
            <p><strong>Why?</strong> This can be proven from first principles using the binomial theorem.</p>
        </div>

        <h3>Examples</h3>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> $\\frac{d}{dx}[x^5] = 5x^4$</p>
            <p><strong>Example 2:</strong> $\\frac{d}{dx}[x] = \\frac{d}{dx}[x^1] = 1 \\cdot x^0 = 1$</p>
            <p><strong>Example 3:</strong> $\\frac{d}{dx}[x^{-3}] = -3x^{-4} = \\frac{-3}{x^4}$</p>
            <p><strong>Example 4:</strong> $\\frac{d}{dx}[\\sqrt{x}] = \\frac{d}{dx}[x^{1/2}] = \\frac{1}{2}x^{-1/2} = \\frac{1}{2\\sqrt{x}}$</p>
        </div>

        <h3>Special Case: Constant</h3>
        <p>If $f(x) = c$ (constant), then:</p>
        <p>$$\\frac{d}{dx}[c] = 0$$</p>
        <p>Constants have no rate of change.</p>
        """
    },
    {
        "title": "Linearity Rules",
        "body": """
        <h3>Constant Multiple Rule</h3>
        <p>If $k$ is a constant and $f$ is differentiable:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\frac{d}{dx}[k \\cdot f(x)] = k \\cdot f'(x)$$</p>
        </div>

        <p>Constants can be pulled out of derivatives.</p>

        <h3>Sum Rule</h3>
        <p>If $f$ and $g$ are differentiable:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$$</p>
        </div>

        <p>The derivative of a sum is the sum of derivatives.</p>

        <h3>Difference Rule</h3>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)$$</p>
        </div>

        <h3>Example: Polynomial</h3>

        <div class="worked-example formula-box">
            <p><strong>Differentiate:</strong> $y = 3x^4 - 2x^2 + 5x - 7$</p>
            <p>$\\frac{dy}{dx} = 3(4x^3) - 2(2x) + 5(1) - 0$</p>
            <p>$= $ <strong>$12x^3 - 4x + 5$</strong></p>
        </div>
        """
    },
    {
        "title": "Product, Quotient, and Chain Rules",
        "body": """
        <h3>Product Rule</h3>
        <p>If $u$ and $v$ are both differentiable functions of $x$:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\frac{d}{dx}[u \\cdot v] = u'v + uv'$$</p>
            <em style="font-size: 0.85em;">Or: "first times derivative of second, plus second times derivative of first"</em>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> $y = (x^2 + 1)(x - 3)$</p>
            <p>$u = x^2 + 1$, $u' = 2x$</p>
            <p>$v = x - 3$, $v' = 1$</p>
            <p>$\\frac{dy}{dx} = (2x)(x - 3) + (x^2 + 1)(1) = 2x^2 - 6x + x^2 + 1 = $ <strong>$3x^2 - 6x + 1$</strong></p>
        </div>

        <h3>Quotient Rule</h3>
        <p>If $u$ and $v$ are differentiable and $v \\neq 0$:</p>

        <div class="concept-box" style="text-align: center; font-size: 1.05em; padding: 12px; margin: 12px 0">
            <p>$$\\frac{d}{dx}\\left[\\frac{u}{v}\\right] = \\frac{u'v - uv'}{v^2}$$</p>
            <em style="font-size: 0.85em;">"Low times derivative of high minus high times derivative of low, over low squared"</em>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> $y = \\frac{3x + 1}{x^2 - 2}$</p>
            <p>$u = 3x + 1$, $u' = 3$</p>
            <p>$v = x^2 - 2$, $v' = 2x$</p>
            <p>$\\frac{dy}{dx} = \\frac{3(x^2 - 2) - (3x + 1)(2x)}{(x^2 - 2)^2}$</p>
            <p>$= \\frac{3x^2 - 6 - 6x^2 - 2x}{(x^2 - 2)^2} = $ <strong>$\\frac{-3x^2 - 2x - 6}{(x^2 - 2)^2}$</strong></p>
        </div>

        <h3>Chain Rule</h3>
        <p>If $y = f(u)$ and $u = g(x)$, then:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$$</p>
        </div>

        <p>Or equivalently: $\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> $y = (3x^2 - 1)^5$</p>
            <p>Let $u = 3x^2 - 1$, so $y = u^5$</p>
            <p>$\\frac{du}{dx} = 6x$, $\\frac{dy}{du} = 5u^4$</p>
            <p>$\\frac{dy}{dx} = 5u^4 \\cdot 6x = 5(3x^2 - 1)^4 \\cdot 6x = $ <strong>$30x(3x^2 - 1)^4$</strong></p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> $y = \\sin(x^2)$</p>
            <p>$\\frac{dy}{dx} = \\cos(x^2) \\cdot 2x = $ <strong>$2x\\cos(x^2)$</strong></p>
        </div>

        <h3>Special Derivatives</h3>
        <ul style="margin: 12px 0; line-height: 1.8;">
            <li>$\\frac{d}{dx}[e^x] = $ <strong>$e^x$</strong></li>
            <li>$\\frac{d}{dx}[\\ln(x)] = $ <strong>$\\frac{1}{x}$</strong></li>
            <li>$\\frac{d}{dx}[\\sin(x)] = $ <strong>$\\cos(x)$</strong></li>
            <li>$\\frac{d}{dx}[\\cos(x)] = $ <strong>$-\\sin(x)$</strong></li>
            <li>$\\frac{d}{dx}[\\tan(x)] = $ <strong>$\\sec^2(x)$</strong></li>
            <li>$\\frac{d}{dx}[a^x] = $ <strong>$a^x \\ln(a)$</strong> ($a > 0, a \\neq 1$)</li>
        </ul>
        """
    }
]
