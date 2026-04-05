TITLE = "Properties of Expectation"

SECTIONS = [
    {
        "title": "Linearity of Expectation",
        "body": """
        <p>The most important and useful property of expectation is linearity: expectation respects addition and scalar multiplication.</p>

        <div class='concept-box'>
        <p><strong>Linearity of Expectation:</strong> For constants $a$, $b$ and random variables $X$, $Y$:</p>
        <p>$$E[aX + b] = aE[X] + b$$</p>
        </div>

        <p><strong>Why is this powerful?</strong> It holds <strong>regardless of whether $X$ and $Y$ are independent</strong>. No independence assumption needed!</p>

        <div class='worked-example'>
        <p><strong>Example 1: Scaling</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$, so $E[X] = 0.5$. If $Y = 3X - 2$:</p>
        <pre class='code-block'>$E[Y] = E[3X - 2]$
$= 3E[X] - 2$
$= 3(0.5) - 2$
$= 1.5 - 2$
$= -0.5$</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Expected Winnings from a Game</strong></p>
        <p>In a game, you roll a die and win the amount shown. If you play 100 times, what are your expected total winnings?</p>
        <p>Let $X_1, X_2, \\ldots, X_{100}$ be the outcomes. Then total $= X_1 + X_2 + \\cdots + X_{100}$.</p>
        <pre class='code-block'>$E[\\text{Total}] = E[X_1 + X_2 + \\cdots + X_{100}]$
$= E[X_1] + E[X_2] + \\cdots + E[X_{100}]$
$= 3.5 + 3.5 + \\cdots + 3.5$ (100 times)
$= 100 \\cdot 3.5$
$= 350$</pre>
        <p>Expected total winnings: \\$350.</p>
        </div>
        """
    },
    {
        "title": "Superposition (Additivity of Expectation)",
        "body": """
        <p>A special case of linearity that deserves emphasis: expectation is <strong>additive</strong>.</p>

        <div class='concept-box'>
        <p><strong>Superposition Property:</strong> For any random variables $X$ and $Y$:</p>
        <p>$$E[X + Y] = E[X] + E[Y]$$</p>
        <p><strong>This holds even if $X$ and $Y$ are dependent.</strong></p>
        </div>

        <p><strong>Generalization:</strong></p>
        <p>$$E[X_1 + X_2 + \\cdots + X_n] = E[X_1] + E[X_2] + \\cdots + E[X_n]$$</p>

        <div class='worked-example'>
        <p><strong>Example: Coupon Collector Problem (Simplified)</strong></p>
        <p>Suppose there are 3 types of coupons, equally likely. What is the expected number of coupons to collect until you have one of each type?</p>
        <p>Let $X$ = total coupons. We can decompose: $X = X_1 + X_2 + X_3$, where:</p>
        <ul>
        <li>$X_1$ = coupons to get the first type (always 1)</li>
        <li>$X_2$ = additional coupons needed to get the second type</li>
        <li>$X_3$ = additional coupons needed to get the third type</li>
        </ul>
        <p>$E[X_1] = 1$, $E[X_2] = 3/2$ (each coupon has $2/3$ chance of being new), $E[X_3] = 3$ (each coupon has $1/3$ chance).</p>
        <pre class='code-block'>$E[X] = E[X_1] + E[X_2] + E[X_3]$
$= 1 + 3/2 + 3$
$= 5.5$</pre>
        </div>

        <div class='success-box'>
        <p><strong>Key insight:</strong> Superposition often makes complex problems tractable by breaking them into simpler pieces.</p>
        </div>
        """
    },
    {
        "title": "Independence and Factorization",
        "body": """
        <p>When random variables are independent, we have a special property: the expectation of a product factors.</p>

        <div class='concept-box'>
        <p><strong>Independence Property:</strong> If $X$ and $Y$ are independent:</p>
        <p>$$E[XY] = E[X] \\cdot E[Y]$$</p>
        </div>

        <p><strong>Important caveat:</strong> This does NOT hold for dependent variables. We must be careful!</p>

        <div class='worked-example'>
        <p><strong>Example 1: Product of Independent Variables</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$ and $Y \\sim \\text{Uniform}(0, 1)$, independent.</p>
        <p>We have $E[X] = 0.5$ and $E[Y] = 0.5$. For the product:</p>
        <pre class='code-block'>$E[XY] = E[X] \\cdot E[Y]$ [independence]
$= 0.5 \\cdot 0.5$
$= 0.25$</pre>
        <p>Direct computation (to verify): $E[XY] = \\int\\int xy\\, dx\\, dy = (\\int_0^1 x\\, dx)(\\int_0^1 y\\, dy) = (1/2)(1/2) = 1/4$. ✓</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Dependent Variables (Contrast)</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$ and $Y = 2X$ (so $Y$ is completely determined by $X$).</p>
        <p>$E[X] = 0.5$ and $E[Y] = 1$. What is $E[XY]$?</p>
        <pre class='code-block'>$E[XY] = E[X \\cdot 2X]$
$= E[2X^2]$
$= 2E[X^2]$
$= 2(1/3)$
$= 2/3$</pre>
        <p>But $E[X] \\cdot E[Y] = 0.5 \\cdot 1 = 0.5 \\neq 2/3$. The property fails! Reason: $X$ and $Y$ are dependent.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Generalization for independent sequences:</strong></p>
        <p>If $X_1, X_2, \\ldots, X_n$ are mutually independent:</p>
        <p>$$E[X_1 X_2 \\cdots X_n] = E[X_1] \\cdot E[X_2] \\cdot \\ldots \\cdot E[X_n]$$</p>
        </div>
        """
    },
    {
        "title": "Monotonicity and Order Preservation",
        "body": """
        <p>Expectation preserves order: if one random variable is always larger, its expectation is larger.</p>

        <div class='concept-box'>
        <p><strong>Monotonicity Property:</strong> If $X \\leq Y$ almost surely (i.e., $P(X \\leq Y) = 1$), then:</p>
        <p>$$E[X] \\leq E[Y]$$</p>
        </div>

        <p><strong>Intuition:</strong> If $X$ is never larger than $Y$, the average of $X$ cannot exceed the average of $Y$.</p>

        <div class='concept-box'>
        <p><strong>Special case (nonnegativity):</strong> If $X \\geq 0$ almost surely:</p>
        <p>$$E[X] \\geq 0$$</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Comparing Die Rolls</strong></p>
        <p>Roll two dice. Let $X$ = outcome of first die, $Y$ = outcome of second die. Also consider $Z = X + Y$.</p>
        <p>We always have $X \\leq Z$ (since $Y \\geq 1$). So:</p>
        <pre class='code-block'>$E[X] \\leq E[Z]$
$3.5 \\leq E[X + Y]$
$3.5 \\leq E[X] + E[Y]$
$3.5 \\leq 3.5 + 3.5$
$3.5 \\leq 7$ ✓</pre>
        </div>

        <div class='concept-box'>
        <p><strong>Jensen's Inequality (for convex functions):</strong></p>
        <p>If $g$ is a convex function and $E[|X|]$ exists:</p>
        <p>$$g(E[X]) \\leq E[g(X)]$$</p>
        <p>Example: Since $x^2$ is convex, $(E[X])^2 \\leq E[X^2]$. This relates expectation and variance!</p>
        </div>
        """
    }
]
