TITLE = "Exponent Laws and Properties"

SECTIONS = [
    {
        "title": "Exponential Functions and Exponential Growth",
        "body": """
        <h3>Understanding Exponentials</h3>
        <p>An <strong>exponential function</strong> has the form $f(x) = a^x$ where $a > 0$ and $a \\neq 1$.</p>

        <h4>Key Properties</h4>
        <ul>
            <li>If $a > 1$: function increases (growth)</li>
            <li>If $0 < a < 1$: function decreases (decay)</li>
            <li>Always passes through $(0, 1)$: $a^0 = 1$</li>
            <li>Domain: all real numbers</li>
            <li>Range: all positive numbers ($y > 0$)</li>
            <li>Horizontal asymptote at $y = 0$</li>
        </ul>

        <div class="concept-box">
            <p><strong>Example 1:</strong> $f(x) = 2^x$</p>
            <ul>
                <li>$f(0) = 1$, $f(1) = 2$, $f(2) = 4$, $f(3) = 8$</li>
                <li>$f(-1) = \\frac{1}{2}$, $f(-2) = \\frac{1}{4}$</li>
                <li>Rapid growth as $x$ increases</li>
            </ul>
        </div>

        <h4>Exponential Growth Model</h4>
        <p>Many real phenomena follow: <strong>$A(t) = A_0 \\cdot a^t$</strong> or <strong>$A(t) = A_0 \\cdot e^{kt}$</strong></p>
        <ul>
            <li>$A_0$ = initial amount</li>
            <li>$a$ = growth factor per time unit</li>
            <li>$k$ = growth constant (if using $e$)</li>
            <li>$t$ = time</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 2:</strong> A bacterial culture doubles every 3 hours. If we start with 1000 bacteria, find the population after 9 hours.</p>
            <p>$A(t) = 1000 \\cdot 2^{t/3}$</p>
            <p>$A(9) = 1000 \\cdot 2^{9/3} = 1000 \\cdot 2^3 = 1000 \\cdot 8 = 8000$ bacteria</p>
        </div>

        <h4>Exponential Decay Model</h4>
        <p>Radioactive decay: <strong>$A(t) = A_0 \\cdot \\left(\\frac{1}{2}\\right)^{t/T}$</strong> where $T$ is the half-life</p>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Carbon-14 has a half-life of 5730 years. If an artifact contains 30% of original C-14, how old is it?</p>
            <p>$0.3 = \\left(\\frac{1}{2}\\right)^{t/5730}$</p>
            <p>$\\log(0.3) = \\frac{t}{5730} \\log(0.5)$</p>
            <p>$t = 5730 \\times \\frac{\\log(0.3)}{\\log(0.5)} \\approx 9953$ years</p>
        </div>
        """
    }
]
