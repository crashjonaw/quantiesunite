TITLE = "Finding Roots and Factoring"

SECTIONS = [
    {
        "title": "The Rational Root Theorem",
        "body": """
        <h3>A Strategy for Finding Rational Roots</h3>
        <p>Not all polynomial roots are easy to guess. The Rational Root Theorem limits the possible rational roots, making our search much more efficient.</p>

        <h4>The Rational Root Theorem</h4>
        <div class="concept-box formula-box">
            <p>For a polynomial with integer coefficients:</p>
            <p>$$f(x) = a_n x^n + a_{n-1} x^{n-1} + \\cdots + a_1 x + a_0$$</p>
            <p style="margin-top: 15px;">any rational root $\\frac{p}{q}$ (in lowest terms) must satisfy:</p>
            <ul style="margin-top: 10px;">
                <li>$p$ divides the constant term $a_0$</li>
                <li>$q$ divides the leading coefficient $a_n$</li>
            </ul>
        </div>

        <h4>How to Use It</h4>
        <ol style="margin-top: 10px;">
            <li>List all divisors of the constant term (these are possible values of $p$)</li>
            <li>List all divisors of the leading coefficient (these are possible values of $q$)</li>
            <li>Form all possible ratios $\\frac{p}{q}$</li>
            <li>Test these candidates using synthetic division or by evaluating $f(x)$</li>
        </ol>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> Find all rational roots of $2x^3 + 3x^2 - 8x - 12 = 0$</p>

            <p style="margin-top: 15px;"><strong>Step 1: Identify possible rational roots</strong></p>
            <p style="margin-top: 10px;">Divisors of $a_0 = -12$: $\\pm 1, \\pm 2, \\pm 3, \\pm 4, \\pm 6, \\pm 12$</p>
            <p style="margin-top: 5px;">Divisors of $a_n = 2$: $\\pm 1, \\pm 2$</p>
            <p style="margin-top: 15px;">Possible rational roots: $\\pm 1, \\pm 2, \\pm 3, \\pm 4, \\pm 6, \\pm 12, \\pm \\frac{1}{2}, \\pm \\frac{3}{2}$</p>

            <p style="margin-top: 15px;"><strong>Step 2: Test candidates</strong></p>
            <p style="margin-top: 10px;">$f(2) = 2(8) + 3(4) - 8(2) - 12 = 16 + 12 - 16 - 12 = 0$</p>
            <p style="margin-top: 5px;">So $x = 2$ is a root, and $(x - 2)$ is a factor.</p>

            <p style="margin-top: 15px;"><strong>Step 3: Use synthetic division</strong></p>
            <p style="margin-top: 10px;">$2x^3 + 3x^2 - 8x - 12 = (x - 2)(2x^2 + 7x + 6)$</p>

            <p style="margin-top: 15px;"><strong>Step 4: Factor the remaining quadratic</strong></p>
            <p style="margin-top: 10px;">$2x^2 + 7x + 6 = (2x + 3)(x + 2)$</p>

            <p style="margin-top: 15px;"><strong>Complete factorization:</strong></p>
            <p style="margin-top: 10px;"><strong>$2x^3 + 3x^2 - 8x - 12 = (x - 2)(2x + 3)(x + 2)$</strong></p>
            <p style="margin-top: 10px;">Roots: $x = 2$, $x = -\\frac{3}{2}$, $x = -2$</p>
        </div>

        <div class="warning-box formula-box">
            <p><strong>Important note:</strong> The Rational Root Theorem tells us which rational values could be roots. It does NOT guarantee that these values ARE roots—we still need to test them!</p>
        </div>
        """
    },
    {
        "title": "Complex Roots and the Conjugate Root Theorem",
        "body": """
        <h3>When Real Roots Don't Exist</h3>
        <p>Some polynomials have no real roots. Their roots are complex numbers.</p>

        <h4>Complex Numbers Review</h4>
        <div class="concept-box formula-box">
            <p>A complex number has the form <strong>$z = a + bi$</strong>, where:</p>
            <ul style="margin-top: 10px;">
                <li>$a$ is the real part</li>
                <li>$b$ is the imaginary part</li>
                <li><strong>$i^2 = -1$</strong></li>
            </ul>
        </div>

        <h4>The Conjugate Root Theorem</h4>
        <div class="concept-box formula-box">
            <p>If a polynomial has real coefficients and $a + bi$ is a root (where $b \\neq 0$), then <strong>$a - bi$ is also a root</strong>.</p>
            <p style="margin-top: 10px;">Complex roots always come in conjugate pairs!</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> Find the roots of $x^2 + 2x + 5 = 0$</p>

            <p style="margin-top: 15px;">Using the quadratic formula:</p>
            <p style="margin-top: 10px;">$x = \\frac{-2 \\pm \\sqrt{4 - 20}}{2} = \\frac{-2 \\pm \\sqrt{-16}}{2} = \\frac{-2 \\pm 4i}{2} = $ <strong>$-1 \\pm 2i$</strong></p>

            <p style="margin-top: 15px;">The two roots are:</p>
            <ul style="margin-top: 10px;">
                <li>$x_1 = -1 + 2i$</li>
                <li>$x_2 = -1 - 2i$ (conjugate of $x_1$)</li>
            </ul>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 3:</strong> If $2 + 3i$ is a root of a polynomial with real coefficients, what is another root?</p>

            <p style="margin-top: 15px;">By the Conjugate Root Theorem, <strong>$2 - 3i$ must also be a root</strong>.</p>

            <p style="margin-top: 15px;">The quadratic with these roots is:</p>
            <p style="margin-top: 10px;">$(x - (2 + 3i))(x - (2 - 3i))$</p>
            <p style="margin-top: 10px;">$= [(x - 2) - 3i][(x - 2) + 3i]$</p>
            <p style="margin-top: 10px;">$= (x - 2)^2 - (3i)^2$  (difference of squares)</p>
            <p style="margin-top: 10px;">$= (x - 2)^2 + 9$</p>
            <p style="margin-top: 10px;">$= x^2 - 4x + 4 + 9$</p>
            <p style="margin-top: 10px;">$= $ <strong>$x^2 - 4x + 13$</strong></p>
        </div>

        <div class="success-box formula-box">
            <p><strong>Key insight:</strong> When complex roots appear, they come in conjugate pairs. This means every polynomial of odd degree must have at least one real root!</p>
        </div>
        """
    },
    {
        "title": "Vieta's Formulas and Solving Higher Degree Equations",
        "body": """
        <h3>Relationships Between Roots and Coefficients</h3>
        <p>Vieta's Formulas connect the coefficients of a polynomial to sums and products of its roots. This is powerful for checking answers and solving problems without finding individual roots.</p>

        <h4>Vieta's Formulas for a Cubic</h4>
        <p>For a cubic equation $ax^3 + bx^2 + cx + d = 0$ with roots $r, s, t$:</p>
        <div class="concept-box formula-box">
            <ul style="margin-top: 10px;">
                <li>Sum of roots: <strong>$r + s + t = -\\frac{b}{a}$</strong></li>
                <li>Sum of products of pairs: <strong>$rs + rt + st = \\frac{c}{a}$</strong></li>
                <li>Product of all roots: <strong>$rst = -\\frac{d}{a}$</strong></li>
            </ul>
        </div>

        <h4>Vieta's Formulas for a Quadratic</h4>
        <p>For $ax^2 + bx + c = 0$ with roots $r$ and $s$:</p>
        <div class="concept-box formula-box">
            <ul style="margin-top: 10px;">
                <li>Sum of roots: <strong>$r + s = -\\frac{b}{a}$</strong></li>
                <li>Product of roots: <strong>$rs = \\frac{c}{a}$</strong></li>
            </ul>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 4:</strong> Find the sum and product of roots of $x^3 - 4x^2 + 5x - 2 = 0$</p>

            <p style="margin-top: 15px;">Using Vieta's formulas with $a = 1$, $b = -4$, $c = 5$, $d = -2$:</p>
            <p style="margin-top: 10px;">Sum of roots $= -\\frac{-4}{1} = 4$</p>
            <p style="margin-top: 10px;">Product of roots $= -\\frac{-2}{1} = 2$</p>

            <p style="margin-top: 15px;">We can verify: $x = 1$ is a root (checking: $1 - 4 + 5 - 2 = 0$)</p>
            <p style="margin-top: 10px;">Factoring gives: $(x - 1)^2(x - 2)$, so roots are $1, 1, 2$</p>
            <p style="margin-top: 10px;">Sum: $1 + 1 + 2 = 4$</p>
            <p style="margin-top: 10px;">Product: $1 \\times 1 \\times 2 = 2$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 5:</strong> Write a polynomial with roots $2$, $-1$, and $3$</p>

            <p style="margin-top: 15px;"><strong>Method 1: Using Vieta's formulas (backwards)</strong></p>
            <p style="margin-top: 10px;">Sum of roots: $2 + (-1) + 3 = 4$</p>
            <p style="margin-top: 10px;">Product of pairs: $(2)(-1) + (2)(3) + (-1)(3) = -2 + 6 - 3 = 1$</p>
            <p style="margin-top: 10px;">Product of roots: $(2)(-1)(3) = -6$</p>

            <p style="margin-top: 15px;">A monic polynomial (leading coefficient 1) is:</p>
            <p style="margin-top: 10px;">$x^3 - 4x^2 + 1x - (-6) = $ <strong>$x^3 - 4x^2 + x + 6$</strong></p>

            <p style="margin-top: 15px;"><strong>Method 2: Using factored form</strong></p>
            <p style="margin-top: 10px;">$(x - 2)(x - (-1))(x - 3) = (x - 2)(x + 1)(x - 3)$</p>
            <p style="margin-top: 10px;">$= (x - 2)(x^2 - 2x - 3) = $ <strong>$x^3 - 4x^2 + x + 6$</strong></p>
        </div>
        """
    }
]
