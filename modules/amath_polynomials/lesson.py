SECTIONS = [
    {
        "title": "Polynomial Division and the Remainder Theorem",
        "body": """
        <h3>Dividing Polynomials</h3>
        <p>We can divide polynomials using long division, similar to dividing numbers.</p>

        <h4>Polynomial Long Division</h4>
        <ol>
            <li>Arrange both polynomials in descending order of degree</li>
            <li>Divide the leading term of the dividend by the leading term of the divisor</li>
            <li>Multiply the quotient by the divisor and subtract from the dividend</li>
            <li>Bring down the next term and repeat</li>
            <li>Continue until the remainder has lower degree than the divisor</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 1:</strong> Divide x³ + 5x² + 2x - 8 by x + 2</p>
            <p>Using long division:</p>
            <ul>
                <li>x³ ÷ x = x² (first quotient term)</li>
                <li>x²(x + 2) = x³ + 2x²</li>
                <li>Subtract: (x³ + 5x²) - (x³ + 2x²) = 3x²</li>
                <li>Bring down 2x: 3x² + 2x</li>
                <li>3x² ÷ x = 3x (next quotient term)</li>
                <li>Continue this process...</li>
                <li><strong>Result:</strong> Quotient = x² + 3x - 4, Remainder = 0</li>
            </ul>
        </div>

        <h3>The Remainder Theorem</h3>
        <p>When polynomial f(x) is divided by (x - a), the remainder is f(a).</p>

        <p style="text-align: center;"><strong>f(x) = (x - a)q(x) + r, where r = f(a)</strong></p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find the remainder when f(x) = 2x³ - 3x² + x - 5 is divided by (x - 2)</p>
            <p>By the Remainder Theorem: remainder = f(2) = 2(8) - 3(4) + 2 - 5 = 16 - 12 + 2 - 5 = 1</p>
            <p>Check: We can verify by long division if needed.</p>
        </div>

        <h3>The Factor Theorem</h3>
        <p><strong>Corollary:</strong> (x - a) is a factor of f(x) if and only if f(a) = 0.</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Is (x + 1) a factor of x³ + 2x² - x - 2?</p>
            <p>Check f(-1) = (-1)³ + 2(-1)² - (-1) - 2 = -1 + 2 + 1 - 2 = 0</p>
            <p>Yes! (x + 1) is a factor. We can write: x³ + 2x² - x - 2 = (x + 1)(x² + x - 2) = (x + 1)(x + 2)(x - 1)</p>
        </div>
        """
    },
    {
        "title": "Synthetic Division",
        "body": """
        <h3>A Faster Division Method</h3>
        <p><strong>Synthetic division</strong> is a shortcut for dividing by linear polynomials (x - a).</p>

        <h4>Steps</h4>
        <ol>
            <li>Write the coefficients of the polynomial in a row</li>
            <li>Write 'a' (the root) to the left</li>
            <li>Bring down the first coefficient</li>
            <li>Multiply it by 'a' and write the result under the next coefficient</li>
            <li>Add to get the next value and repeat</li>
            <li>The last value is the remainder; others are quotient coefficients</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 4:</strong> Divide 2x³ - 3x² + 4x - 5 by (x - 2) using synthetic division</p>
            <p>Setup: a = 2, coefficients: 2, -3, 4, -5</p>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;">2</td>
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">2</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">-3</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">4</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">-5</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">4</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">2</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">12</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">2</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">1</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">6</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">7</td>
                </tr>
            </table>
            <p><strong>Quotient:</strong> 2x² + x + 6, <strong>Remainder:</strong> 7</p>
        </div>
        """
    },
    {
        "title": "Partial Fractions Decomposition",
        "body": """
        <h3>Breaking Down Rational Expressions</h3>
        <p><strong>Partial fractions</strong> decompose a rational expression into simpler fractions that are easier to integrate or manipulate.</p>

        <h4>Basic Principle</h4>
        <p>For proper rational fractions (degree of numerator < degree of denominator), we can write:</p>
        <p style="text-align: center;"><strong>P(x)/Q(x) = A/(x - a) + B/(x - b) + ... (for linear factors)</strong></p>

        <h4>Case 1: Distinct Linear Factors</h4>
        <p>If Q(x) = (x - a)(x - b)(x - c), write:</p>
        <p style="text-align: center;"><strong>P(x)/Q(x) = A/(x - a) + B/(x - b) + C/(x - c)</strong></p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Decompose (5x + 7)/((x + 1)(x - 2))</p>
            <p>(5x + 7)/((x + 1)(x - 2)) = A/(x + 1) + B/(x - 2)</p>
            <p>Multiply both sides by (x + 1)(x - 2):</p>
            <p>5x + 7 = A(x - 2) + B(x + 1)</p>
            <p>Substituting x = 2: 17 = 3B, so B = 17/3</p>
            <p>Substituting x = -1: 2 = -3A, so A = -2/3</p>
            <p><strong>Result:</strong> -2/3 · 1/(x + 1) + 17/3 · 1/(x - 2)</p>
        </div>

        <h4>Case 2: Repeated Linear Factors</h4>
        <p>If (x - a) appears twice, include both (x - a) and (x - a)²:</p>
        <p style="text-align: center;"><strong>P(x)/(x - a)² = A/(x - a) + B/(x - a)²</strong></p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Decompose (x + 5)/(x + 1)²</p>
            <p>(x + 5)/(x + 1)² = A/(x + 1) + B/(x + 1)²</p>
            <p>x + 5 = A(x + 1) + B</p>
            <p>At x = -1: 4 = B</p>
            <p>Coefficient of x: 1 = A, so A = 1</p>
            <p><strong>Result:</strong> 1/(x + 1) + 4/(x + 1)²</p>
        </div>

        <h4>Case 3: Irreducible Quadratic Factors</h4>
        <p>If Q(x) has a quadratic factor x² + bx + c that doesn't factor over reals:</p>
        <p style="text-align: center;"><strong>P(x)/[(x - a)(x² + bx + c)] = A/(x - a) + (Bx + C)/(x² + bx + c)</strong></p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Decompose (x² + 1)/[(x - 1)(x² + 1)]</p>
            <p>Note: x² + 1 doesn't factor over reals</p>
            <p>(x² + 1)/[(x - 1)(x² + 1)] = 1/(x - 1) + 0/(x² + 1) = 1/(x - 1)</p>
            <p>Actually, this simplifies! The x² + 1 cancels, leaving 1/(x - 1)</p>
        </div>
        """
    },
    {
        "title": "Complex Numbers (Brief Introduction)",
        "body": """
        <h3>Working with Complex Roots</h3>
        <p>Not all polynomials have real roots. We use complex numbers: <strong>i² = -1</strong>, and <strong>i = √(-1)</strong></p>

        <h4>Complex Number Form</h4>
        <p><strong>z = a + bi</strong>, where a is the real part and b is the imaginary part</p>

        <h4>Operations with Complex Numbers</h4>
        <ul>
            <li><strong>Addition:</strong> (a + bi) + (c + di) = (a+c) + (b+d)i</li>
            <li><strong>Multiplication:</strong> (a + bi)(c + di) = (ac - bd) + (ad + bc)i</li>
            <li><strong>Division:</strong> Multiply by conjugate: (a+bi)/(c+di) × (c-di)/(c-di)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 8:</strong> Find roots of x² + 2x + 5 = 0</p>
            <p>Using quadratic formula: x = (-2 ± √(4-20))/2 = (-2 ± √(-16))/2 = (-2 ± 4i)/2 = -1 ± 2i</p>
            <p>Roots are complex: x = -1 + 2i and x = -1 - 2i</p>
        </div>

        <h4>Conjugate Roots Theorem</h4>
        <p>If a + bi is a root of a polynomial with real coefficients, then a - bi is also a root.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> If 2 + 3i is a root, then 2 - 3i is also a root</p>
            <p>A polynomial with these roots: (x - (2 + 3i))(x - (2 - 3i)) = (x - 2)² - (3i)² = x² - 4x + 4 + 9 = x² - 4x + 13</p>
        </div>
        """
    },
    {
        "title": "Solving Higher-Degree Polynomial Equations",
        "body": """
        <h3>Using Roots to Solve Cubics and Quartics</h3>

        <h4>The Rational Root Theorem</h4>
        <p>For a polynomial with integer coefficients, any rational root p/q has:</p>
        <ul>
            <li>p divides the constant term</li>
            <li>q divides the leading coefficient</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 10:</strong> Solve 2x³ + 3x² - 8x - 12 = 0</p>
            <p>Possible rational roots: ±1, ±2, ±3, ±4, ±6, ±12, ±1/2, ±3/2, etc.</p>
            <p>Test x = 2: 2(8) + 3(4) - 8(2) - 12 = 16 + 12 - 16 - 12 = 0 ✓</p>
            <p>So (x - 2) is a factor. Use synthetic division:</p>
            <p>2x³ + 3x² - 8x - 12 = (x - 2)(2x² + 7x + 6) = (x - 2)(2x + 3)(x + 2)</p>
            <p><strong>Roots:</strong> x = 2, x = -3/2, x = -2</p>
        </div>

        <h4>Vieta's Formulas (Relationship Between Roots and Coefficients)</h4>
        <p>For cubic ax³ + bx² + cx + d = 0 with roots r, s, t:</p>
        <ul>
            <li>r + s + t = -b/a</li>
            <li>rs + rt + st = c/a</li>
            <li>rst = -d/a</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 11:</strong> Find the sum and product of roots of x³ - 4x² + 5x - 2 = 0</p>
            <p>Sum of roots = 4</p>
            <p>Product of roots = 2</p>
            <p>By inspection/testing: x = 1 is a root, and factoring gives (x-1)(x² - 3x + 2) = (x-1)²(x-2)</p>
            <p>Roots: 1, 1, 2. Sum = 1 + 1 + 2 = 4 ✓, Product = 1 × 1 × 2 = 2 ✓</p>
        </div>
        """
    }
]
