TITLE = "Solving Exponential and Logarithmic Equations"

SECTIONS = [
    {
        "title": "Solving Exponential Equations",
        "body": """
        <h3>Two Main Strategies</h3>

        <h4>Strategy 1: Same Base Method</h4>
        <p>If you can express both sides with the same base, equate the exponents.</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Solve $3^{2x-1} = 27$</p>
            <p>Notice $27 = 3^3$, so: $3^{2x-1} = 3^3$</p>
            <p>Equate exponents: $2x - 1 = 3$</p>
            <p>$2x = 4$, so <strong>$x = 2$</strong></p>
        </div>

        <h4>Strategy 2: Logarithm Method</h4>
        <p>Take the logarithm of both sides (use any base, but natural log is often convenient).</p>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Solve $5^x = 80$</p>
            <p>Take log of both sides: $\\log(5^x) = \\log(80)$</p>
            <p>$x \\cdot \\log(5) = \\log(80)$</p>
            <p>$x = \\frac{\\log(80)}{\\log(5)} \\approx \\frac{1.903}{0.699} \\approx $ <strong>$2.72$</strong></p>
        </div>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Solve $2 = e^{0.03t}$</p>
            <p>Take natural log: $\\ln(2) = 0.03t$</p>
            <p>$t = \\frac{\\ln(2)}{0.03} \\approx \\frac{0.693}{0.03} \\approx $ <strong>$23.1$</strong></p>
        </div>
        """
    },
    {
        "title": "Solving Logarithmic Equations",
        "body": """
        <h3>Main Strategy: Convert to Exponential Form</h3>

        <h4>Basic Approach</h4>
        <p>Remember: if $\\log_a(x) = y$, then $a^y = x$</p>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Solve $\\log_2(x + 3) = 4$</p>
            <p>Convert to exponential form: $x + 3 = 2^4 = 16$</p>
            <p>$x = 13$</p>
        </div>

        <h4>Using Logarithm Properties</h4>
        <p>Combine logarithmic properties with the conversion method.</p>

        <div class="worked-example">
            <p><strong>Example 5:</strong> Solve $\\log(x) + \\log(x - 3) = \\log(10)$</p>
            <p>Use product rule: $\\log(x(x - 3)) = \\log(10)$</p>
            <p>Therefore: $x(x - 3) = 10$</p>
            <p>$x^2 - 3x - 10 = 0$</p>
            <p>$(x - 5)(x + 2) = 0$</p>
            <p>$x = 5$ or $x = -2$</p>
            <p><strong>But $x > 3$ (domain restriction), so $x = 5$ only</strong></p>
        </div>

        <h4>Domain Restrictions</h4>
        <p>Always check your solutions! For $\\log_a(x)$: $x$ must be positive ($x > 0$)</p>

        <div class="warning-box">
            <p><strong>Critical:</strong> When solving log equations, verify that your solutions satisfy the original domain requirements. Reject any solutions where arguments of logarithms are non-positive.</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 6:</strong> Solve $\\log_3(x) + \\log_3(x-2) = 1$</p>
            <p>$\\log_3(x(x-2)) = 1$</p>
            <p>$x(x-2) = 3^1 = 3$</p>
            <p>$x^2 - 2x - 3 = 0$</p>
            <p>$(x-3)(x+1) = 0$</p>
            <p>$x = 3$ or $x = -1$</p>
            <p>Check: $x > 2$ required (so both $x$ and $x-2$ are positive), thus <strong>$x = 3$ only</strong></p>
        </div>
        """
    }
]
