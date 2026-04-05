TITLE = "Rate of Change and Limits"

SECTIONS = [
    {
        "title": "Understanding Rates of Change",
        "body": """
        <h3>Average Rate of Change</h3>
        <p>The <strong>average rate of change</strong> of a function $f(x)$ over an interval $[a, b]$ is:</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\text{Average rate} = \\frac{f(b) - f(a)}{b - a}$$</p>
        </div>

        <p>This represents the <strong>slope of the secant line</strong> connecting points $(a, f(a))$ and $(b, f(b))$.</p>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> A car travels 150 km in 2 hours. What is its average speed?</p>
            <p>Average rate $= 150 \\div 2 = $ <strong>75 km/h</strong></p>
            <p>This is the slope of the line connecting start and end positions.</p>
        </div>

        <h3>Instantaneous Rate of Change</h3>
        <p>As the interval gets smaller ($b$ gets closer to $a$), we approach the <strong>instantaneous rate of change</strong>—the rate at a specific moment.</p>

        <p>$$\\text{Instantaneous rate} = \\lim_{b \\to a} \\frac{f(b) - f(a)}{b - a}$$</p>

        <p>This is the slope of the <strong>tangent line</strong> at point $a$.</p>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> For $f(x) = x^2$, find the instantaneous rate of change at $x = 3$</p>
            <p>As $h \\to 0$: $\\frac{f(3+h) - f(3)}{h} = \\frac{(3+h)^2 - 9}{h} = \\frac{9 + 6h + h^2 - 9}{h} = \\frac{6h + h^2}{h}$</p>
            <p>$= 6 + h \\to $ <strong>6</strong> as $h \\to 0$</p>
        </div>
        """
    },
    {
        "title": "The Limit Concept",
        "body": """
        <h3>What is a Limit?</h3>
        <p>The <strong>limit</strong> of a function $f(x)$ as $x$ approaches $a$ is the value $f(x)$ approaches (but may never reach).</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\lim_{x \\to a} f(x) = L$$</p>
            <em style="font-size: 0.9em;">As $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$</em>
        </div>

        <div class="warning-box formula-box">
            <p><strong>Key Insight:</strong> The limit may exist even if $f(a)$ is undefined or different from $L$.</p>
        </div>

        <h3>Computing Limits</h3>
        <p><strong>Direct Substitution:</strong> If $f$ is continuous at $a$, then $\\lim_{x \\to a} f(x) = f(a)$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 3:</strong> Find $\\lim_{x \\to 2} (x^2 + 3x - 1)$</p>
            <p>By direct substitution: $2^2 + 3(2) - 1 = 4 + 6 - 1 = $ <strong>9</strong></p>
        </div>

        <h3>One-Sided Limits</h3>
        <p><strong>Left limit:</strong> $\\lim_{x \\to a^-} f(x)$ — $x$ approaches $a$ from the left</p>
        <p><strong>Right limit:</strong> $\\lim_{x \\to a^+} f(x)$ — $x$ approaches $a$ from the right</p>

        <p>The limit exists only if both one-sided limits are equal.</p>

        <div class="worked-example formula-box">
            <p><strong>Example 4:</strong> Consider $f(x) = \\frac{|x|}{x}$ for $x \\neq 0$</p>
            <p>$\\lim_{x \\to 0^-} f(x) = -1$ ($x$ is negative, so $|x| = -x$)</p>
            <p>$\\lim_{x \\to 0^+} f(x) = 1$ ($x$ is positive, so $|x| = x$)</p>
            <p>Since $-1 \\neq 1$, <strong>$\\lim_{x \\to 0} f(x)$ does not exist</strong></p>
        </div>
        """
    },
    {
        "title": "Intuition: From Secants to Tangents",
        "body": """
        <h3>The Secant Line</h3>
        <p>A <strong>secant line</strong> passes through two points on a curve. Its slope is the average rate of change.</p>

        <div class="concept-box formula-box" style="text-align: center; font-size: 1.1em;">
            <p>$$\\text{Slope of secant} = \\frac{\\Delta y}{\\Delta x} = \\frac{f(x+h) - f(x)}{h}$$</p>
        </div>

        <h3>The Tangent Line</h3>
        <p>A <strong>tangent line</strong> touches a curve at exactly one point. As we let the second point approach the first, the secant becomes the tangent.</p>

        <p>$$\\text{Slope of tangent} = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 5:</strong> Find the slope of the tangent to $f(x) = x^2$ at $x = 1$</p>
            <p>Slope $= \\lim_{h \\to 0} \\frac{(1+h)^2 - 1^2}{h} = \\lim_{h \\to 0} \\frac{1 + 2h + h^2 - 1}{h}$</p>
            <p>$= \\lim_{h \\to 0} \\frac{2h + h^2}{h} = \\lim_{h \\to 0} (2 + h) = $ <strong>2</strong></p>
        </div>

        <h3>Interpretation</h3>
        <ul style="margin: 12px 0;">
            <li><strong>Positive slope:</strong> Function increasing at that point</li>
            <li><strong>Negative slope:</strong> Function decreasing at that point</li>
            <li><strong>Zero slope:</strong> Function has a stationary point (local max/min or inflection)</li>
        </ul>
        """
    }
]
