TITLE = "What is a Polynomial?"

SECTIONS = [
    {
        "title": "Polynomials: Definition and Notation",
        "body": """
        <h3>Understanding Polynomials from First Principles</h3>
        <p>A <strong>polynomial</strong> is an expression built from variables and constants using only addition, subtraction, and multiplication. The most important feature of a polynomial is that all exponents must be non-negative integers.</p>

        <h4>Basic Form</h4>
        <p>A polynomial in one variable $x$ has the general form:</p>
        <p>$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\cdots + a_2 x^2 + a_1 x + a_0$$</p>
        <p>where:</p>
        <ul>
            <li><strong>$a_0, a_1, \\ldots, a_n$</strong> are constants called <strong>coefficients</strong></li>
            <li><strong>$n$</strong> is a non-negative integer</li>
            <li><strong>$a_n \\neq 0$</strong> (so we know the degree)</li>
        </ul>

        <div class="concept-box formula-box">
            <p><strong>Examples of polynomials:</strong></p>
            <ul style="margin-top: 10px;">
                <li>$P(x) = 3x^2 - 2x + 5$ (quadratic)</li>
                <li>$Q(x) = x^4 - 1$ (quartic)</li>
                <li>$R(x) = -7$ (constant polynomial)</li>
                <li>$S(x) = x^3 + 2x^2 + 3x$ (cubic, no constant term)</li>
            </ul>
        </div>

        <div class="warning-box formula-box">
            <p><strong>Not polynomials:</strong></p>
            <ul style="margin-top: 10px;">
                <li>$\\frac{1}{x}$ (negative exponent)</li>
                <li>$\\sqrt{x}$ (fractional exponent)</li>
                <li>$x^2 + \\sin(x)$ (transcendental function)</li>
                <li>$|x|$ (not algebraic in the polynomial sense)</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Degree and Terms",
        "body": """
        <h3>Key Polynomial Properties</h3>

        <h4>Degree of a Polynomial</h4>
        <p>The <strong>degree</strong> of a polynomial is the highest power of the variable that appears with a non-zero coefficient.</p>

        <div class="concept-box formula-box">
            <p><strong>Examples:</strong></p>
            <ul style="margin-top: 10px;">
                <li>$P(x) = 5x^3 - 2x^2 + 4x - 1$ has degree <strong>3</strong> (cubic)</li>
                <li>$Q(x) = 2x^2 - 7$ has degree <strong>2</strong> (quadratic)</li>
                <li>$R(x) = -3x + 8$ has degree <strong>1</strong> (linear)</li>
                <li>$S(x) = 42$ has degree <strong>0</strong> (constant polynomial)</li>
            </ul>
        </div>

        <h4>Terms and Coefficients</h4>
        <p>A polynomial is a sum of <strong>terms</strong>. Each term has a coefficient and a power of $x$.</p>
        <p>For $P(x) = 3x^2 - 2x + 5$:</p>
        <ul>
            <li>First term: $3x^2$ (coefficient: 3, power: 2)</li>
            <li>Second term: $-2x$ (coefficient: $-2$, power: 1)</li>
            <li>Third term: $5$ (coefficient: 5, power: 0)</li>
        </ul>

        <h4>Leading Term and Leading Coefficient</h4>
        <p>The <strong>leading term</strong> is the term with the highest degree. The coefficient of the leading term is the <strong>leading coefficient</strong>.</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> For $P(x) = -4x^5 + 2x^3 - x + 6$</p>
            <ul style="margin-top: 10px;">
                <li>Degree: <strong>5</strong></li>
                <li>Leading term: <strong>$-4x^5$</strong></li>
                <li>Leading coefficient: <strong>$-4$</strong></li>
            </ul>
        </div>
        """
    },
    {
        "title": "Standard Form and Operations",
        "body": """
        <h3>Writing Polynomials in Standard Form</h3>
        <p>A polynomial is written in <strong>standard form</strong> (also called <strong>descending order</strong>) when the terms are arranged from highest degree to lowest degree.</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Rewrite $5 - 3x + 2x^3 - x^2$ in standard form.</p>
            <p style="margin-top: 10px;">Arranging from highest to lowest degree: <strong>$2x^3 - x^2 - 3x + 5$</strong></p>
        </div>

        <h4>Why Standard Form Matters</h4>
        <ul>
            <li>Makes it easy to identify the degree and leading coefficient</li>
            <li>Essential for polynomial division and factoring</li>
            <li>Provides a consistent notation for communication</li>
        </ul>

        <h4>Adding and Subtracting Polynomials</h4>
        <p>Combine <strong>like terms</strong> (terms with the same power of $x$).</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Simplify $(3x^2 + 2x - 1) + (x^2 - 5x + 3)$</p>
            <p style="margin-top: 10px;">Combine like terms: $(3x^2 + x^2) + (2x - 5x) + (-1 + 3)$</p>
            <p style="margin-top: 10px;"><strong>Result: $4x^2 - 3x + 2$</strong></p>
        </div>

        <h4>Multiplying Polynomials</h4>
        <p>Multiply each term of the first polynomial by each term of the second, then combine like terms.</p>

        <div class="worked-example formula-box">
            <p><strong>Example:</strong> Multiply $(x + 2)(x^2 - 3x + 1)$</p>
            <p style="margin-top: 10px;">$x(x^2 - 3x + 1) + 2(x^2 - 3x + 1)$</p>
            <p style="margin-top: 10px;">$= x^3 - 3x^2 + x + 2x^2 - 6x + 2$</p>
            <p style="margin-top: 10px;">$= $ <strong>$x^3 - x^2 - 5x + 2$</strong></p>
        </div>

        <div class="success-box formula-box">
            <p><strong>Key insight:</strong> When you multiply a polynomial of degree $m$ by a polynomial of degree $n$, the result has degree $m + n$.</p>
        </div>
        """
    }
]
