TITLE = "Partial Fractions Decomposition"

SECTIONS = [
    {
        "title": "Introduction to Partial Fractions",
        "body": """
        <h3>Breaking Down Complex Rational Expressions</h3>
        <p><strong>Partial fractions decomposition</strong> breaks a single rational expression into a sum of simpler fractions. This is useful for integration, solving differential equations, and simplifying calculations.</p>

        <h4>The Basic Idea</h4>
        <div class="concept-box formula-box">
            <p>We convert:</p>
            <p style="margin-top: 10px;">$$\\text{(Complicated fraction)} = \\text{Sum of (Simpler fractions)}$$</p>
            <p style="margin-top: 15px;"><strong>Example:</strong></p>
            <p style="margin-top: 10px;">$\\frac{7}{x^2 - 1} = \\frac{A}{x - 1} + \\frac{B}{x + 1}$</p>
        </div>

        <h4>When Can We Do This?</h4>
        <p>We need a <strong>proper rational fraction</strong>—one where the degree of the numerator is less than the degree of the denominator.</p>

        <ul style="margin-top: 10px;">
            <li><strong>Proper:</strong> $\\frac{2x + 3}{x^2 + 1}$ — degree 1 &lt; degree 2</li>
            <li><strong>Proper:</strong> $\\frac{5}{x^3 - 4x}$ — degree 0 &lt; degree 3</li>
            <li><strong>Improper:</strong> $\\frac{x^3 + 2}{x^2 + 1}$ — degree 3 &gt; degree 2</li>
        </ul>

        <div class="warning-box formula-box">
            <p><strong>If the fraction is improper:</strong> Use polynomial long division first to separate the polynomial part from the proper fraction part, then decompose the proper fraction.</p>
        </div>

        <h4>Key Strategy</h4>
        <ol style="margin-top: 10px;">
            <li>Factor the denominator completely</li>
            <li>Set up the partial fraction form based on the factors</li>
            <li>Clear denominators and solve for unknown coefficients</li>
            <li>Write the decomposition</li>
        </ol>
        """
    },
    {
        "title": "Case 1: Distinct Linear Factors",
        "body": """
        <h3>When All Factors Are Different Linear Terms</h3>
        <p>This is the simplest case. For each linear factor $(x - a)$ in the denominator, we get a term $\\frac{A}{x - a}$.</p>

        <h4>The Template</h4>
        <p>If the denominator factors as $(x - a_1)(x - a_2)(x - a_3)$, write:</p>
        <p>$$\\frac{P(x)}{(x - a_1)(x - a_2)(x - a_3)} = \\frac{A}{x - a_1} + \\frac{B}{x - a_2} + \\frac{C}{x - a_3}$$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> Decompose $\\frac{7}{x^2 - 1}$</p>

            <p style="margin-top: 15px;"><strong>Step 1: Factor the denominator</strong></p>
            <p style="margin-top: 10px;">$x^2 - 1 = (x - 1)(x + 1)$</p>

            <p style="margin-top: 15px;"><strong>Step 2: Set up the form</strong></p>
            <p style="margin-top: 10px;">$\\frac{7}{(x - 1)(x + 1)} = \\frac{A}{x - 1} + \\frac{B}{x + 1}$</p>

            <p style="margin-top: 15px;"><strong>Step 3: Clear denominators</strong></p>
            <p style="margin-top: 10px;">Multiply both sides by $(x - 1)(x + 1)$:</p>
            <p style="margin-top: 10px;">$7 = A(x + 1) + B(x - 1)$</p>

            <p style="margin-top: 15px;"><strong>Step 4: Solve for $A$ and $B$</strong></p>
            <p style="margin-top: 10px;"><strong>Method 1: Substitution</strong></p>
            <p style="margin-top: 5px;">Set $x = 1$: $7 = A(2) + B(0) \\to A = \\frac{7}{2}$</p>
            <p style="margin-top: 5px;">Set $x = -1$: $7 = A(0) + B(-2) \\to B = -\\frac{7}{2}$</p>

            <p style="margin-top: 15px;"><strong>Step 5: Write the decomposition</strong></p>
            <p style="margin-top: 10px;">$\\frac{7}{x^2 - 1} = $ <strong>$\\frac{7/2}{x - 1} - \\frac{7/2}{x + 1}$</strong></p>
            <p style="margin-top: 10px;">Or equivalently: $\\frac{7/2}{x - 1} + \\frac{-7/2}{x + 1}$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> Decompose $\\frac{5x + 7}{(x + 1)(x - 2)}$</p>

            <p style="margin-top: 15px;"><strong>Set up:</strong></p>
            <p style="margin-top: 10px;">$\\frac{5x + 7}{(x + 1)(x - 2)} = \\frac{A}{x + 1} + \\frac{B}{x - 2}$</p>

            <p style="margin-top: 15px;"><strong>Clear denominators:</strong></p>
            <p style="margin-top: 10px;">$5x + 7 = A(x - 2) + B(x + 1)$</p>

            <p style="margin-top: 15px;"><strong>Substitute convenient values:</strong></p>
            <p style="margin-top: 10px;">$x = 2$: $17 = A(0) + B(3) \\to B = \\frac{17}{3}$</p>
            <p style="margin-top: 10px;">$x = -1$: $2 = A(-3) + B(0) \\to A = -\\frac{2}{3}$</p>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <p style="margin-top: 10px;">$\\frac{5x + 7}{(x + 1)(x - 2)} = $ <strong>$\\frac{-2/3}{x + 1} + \\frac{17/3}{x - 2}$</strong></p>
        </div>
        """
    },
    {
        "title": "Case 2: Repeated Factors and Irreducible Quadratics",
        "body": """
        <h3>More Complex Denominators</h3>

        <h4>Case 2a: Repeated Linear Factors</h4>
        <p>If $(x - a)$ appears multiple times, include all powers from 1 up to the multiplicity.</p>

        <p><strong>For $(x - a)^2$:</strong></p>
        <p>$$\\frac{P(x)}{(x - a)^2} = \\frac{A}{x - a} + \\frac{B}{(x - a)^2}$$</p>

        <p style="margin-top: 20px;"><strong>For $(x - a)^3$:</strong></p>
        <p>$$\\frac{P(x)}{(x - a)^3} = \\frac{A}{x - a} + \\frac{B}{(x - a)^2} + \\frac{C}{(x - a)^3}$$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 3:</strong> Decompose $\\frac{x + 5}{(x + 1)^2}$</p>

            <p style="margin-top: 15px;"><strong>Set up:</strong></p>
            <p style="margin-top: 10px;">$\\frac{x + 5}{(x + 1)^2} = \\frac{A}{x + 1} + \\frac{B}{(x + 1)^2}$</p>

            <p style="margin-top: 15px;"><strong>Clear denominators:</strong></p>
            <p style="margin-top: 10px;">$x + 5 = A(x + 1) + B$</p>

            <p style="margin-top: 15px;"><strong>Solve for $A$ and $B$:</strong></p>
            <p style="margin-top: 10px;">Set $x = -1$: $4 = A(0) + B \\to B = 4$</p>
            <p style="margin-top: 10px;">Compare coefficients of $x$: $1 = A \\to A = 1$</p>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <p style="margin-top: 10px;">$\\frac{x + 5}{(x + 1)^2} = $ <strong>$\\frac{1}{x + 1} + \\frac{4}{(x + 1)^2}$</strong></p>
        </div>

        <h4>Case 2b: Irreducible Quadratic Factors</h4>
        <p>If the denominator has a quadratic factor $x^2 + bx + c$ that doesn't factor over the reals, use $(Dx + E)$ in the numerator.</p>

        <p>$$\\frac{P(x)}{(x - a)(x^2 + bx + c)} = \\frac{A}{x - a} + \\frac{Dx + E}{x^2 + bx + c}$$</p>

        <div class="worked-example formula-box">
            <p><strong>Example 4:</strong> Decompose $\\frac{3x^2 + 5}{x^3 - 1}$</p>

            <p style="margin-top: 15px;"><strong>Step 1: Factor the denominator</strong></p>
            <p style="margin-top: 10px;">$x^3 - 1 = (x - 1)(x^2 + x + 1)$</p>
            <p style="margin-top: 10px;">[Note: $x^2 + x + 1$ has discriminant $1 - 4 = -3 < 0$, so it's irreducible]</p>

            <p style="margin-top: 15px;"><strong>Step 2: Set up the form</strong></p>
            <p style="margin-top: 10px;">$\\frac{3x^2 + 5}{(x - 1)(x^2 + x + 1)} = \\frac{A}{x - 1} + \\frac{Bx + C}{x^2 + x + 1}$</p>

            <p style="margin-top: 15px;"><strong>Step 3: Clear denominators</strong></p>
            <p style="margin-top: 10px;">$3x^2 + 5 = A(x^2 + x + 1) + (Bx + C)(x - 1)$</p>

            <p style="margin-top: 15px;"><strong>Step 4: Solve</strong></p>
            <p style="margin-top: 10px;">Set $x = 1$: $8 = A(3) \\to A = \\frac{8}{3}$</p>
            <p style="margin-top: 10px;">Coefficient of $x^2$: $3 = A + B \\to B = 3 - \\frac{8}{3} = \\frac{1}{3}$</p>
            <p style="margin-top: 10px;">Constant term: $5 = A - C \\to C = \\frac{8}{3} - 5 = -\\frac{7}{3}$</p>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <p style="margin-top: 10px;">$\\frac{3x^2 + 5}{x^3 - 1} = $ <strong>$\\frac{8/3}{x - 1} + \\frac{\\frac{1}{3}x - \\frac{7}{3}}{x^2 + x + 1}$</strong></p>
        </div>

        <div class="success-box formula-box">
            <p><strong>General principle:</strong> The "numerator" above a factor depends on the factor's degree: degree 0 for linear factors, degree 1 for quadratic factors, etc.</p>
        </div>
        """
    }
]
