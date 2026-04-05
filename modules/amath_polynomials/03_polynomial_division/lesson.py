TITLE = "Polynomial Division"

SECTIONS = [
    {
        "title": "Polynomial Long Division",
        "body": """
        <h3>Dividing Polynomials Like Numbers</h3>
        <p>Just as we can divide numbers using long division, we can divide polynomials. The process is similar but we work with terms instead of digits.</p>

        <h4>Algorithm for Polynomial Long Division</h4>
        <ol style="margin-top: 10px;">
            <li>Arrange both polynomials in descending order of degree</li>
            <li>Divide the leading term of the dividend by the leading term of the divisor (this gives the first quotient term)</li>
            <li>Multiply the entire divisor by this quotient term and subtract from the dividend</li>
            <li>Bring down the next term and repeat steps 2-3</li>
            <li>Continue until the remainder has lower degree than the divisor</li>
        </ol>

        <h4>The Division Algorithm</h4>
        <div class="concept-box formula-box">
            <p>For polynomials $f(x)$ and $g(x)$, there exist unique polynomials $q(x)$ (quotient) and $r(x)$ (remainder) such that:</p>
            <p>$$f(x) = g(x) \\cdot q(x) + r(x)$$</p>
            <p style="margin-top: 10px;">where either $r(x) = 0$ or $\\deg(r) < \\deg(g)$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> Divide $x^3 + 5x^2 + 2x - 8$ by $x + 2$</p>

            <p style="margin-top: 15px;"><strong>Step 1: $x^3 \\div x = x^2$</strong></p>
            <p style="margin-top: 10px;">Multiply: $x^2(x + 2) = x^3 + 2x^2$</p>
            <p style="margin-top: 10px;">Subtract: $(x^3 + 5x^2) - (x^3 + 2x^2) = 3x^2$</p>
            <p style="margin-top: 10px;">Bring down $2x$: $3x^2 + 2x$</p>

            <p style="margin-top: 15px;"><strong>Step 2: $3x^2 \\div x = 3x$</strong></p>
            <p style="margin-top: 10px;">Multiply: $3x(x + 2) = 3x^2 + 6x$</p>
            <p style="margin-top: 10px;">Subtract: $(3x^2 + 2x) - (3x^2 + 6x) = -4x$</p>
            <p style="margin-top: 10px;">Bring down $-8$: $-4x - 8$</p>

            <p style="margin-top: 15px;"><strong>Step 3: $-4x \\div x = -4$</strong></p>
            <p style="margin-top: 10px;">Multiply: $-4(x + 2) = -4x - 8$</p>
            <p style="margin-top: 10px;">Subtract: $(-4x - 8) - (-4x - 8) = 0$</p>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <p style="margin-top: 10px;"><strong>Quotient: $x^2 + 3x - 4$, Remainder: $0$</strong></p>
            <p style="margin-top: 10px;">So: $x^3 + 5x^2 + 2x - 8 = (x + 2)(x^2 + 3x - 4)$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> Divide $2x^3 - 3x^2 + 4x - 5$ by $x^2 - 1$</p>

            <p style="margin-top: 15px;"><strong>Step 1: $2x^3 \\div x^2 = 2x$</strong></p>
            <p style="margin-top: 10px;">Multiply: $2x(x^2 - 1) = 2x^3 - 2x$</p>
            <p style="margin-top: 10px;">Subtract: $(2x^3 - 3x^2) - (2x^3) = -3x^2$</p>
            <p style="margin-top: 10px;">Bring down $4x$: $-3x^2 + 4x - 5$</p>

            <p style="margin-top: 15px;"><strong>Step 2: $-3x^2 \\div x^2 = -3$</strong></p>
            <p style="margin-top: 10px;">Multiply: $-3(x^2 - 1) = -3x^2 + 3$</p>
            <p style="margin-top: 10px;">Subtract: $(-3x^2 + 4x - 5) - (-3x^2 + 3) = 4x - 8$</p>

            <p style="margin-top: 15px;">The remainder $4x - 8$ has degree 1, which is less than degree of $x^2 - 1$, so we stop.</p>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <p style="margin-top: 10px;"><strong>Quotient: $2x - 3$, Remainder: $4x - 8$</strong></p>
            <p style="margin-top: 10px;">So: $2x^3 - 3x^2 + 4x - 5 = (x^2 - 1)(2x - 3) + (4x - 8)$</p>
        </div>
        """
    },
    {
        "title": "Synthetic Division",
        "body": """
        <h3>A Shortcut for Linear Divisors</h3>
        <p><strong>Synthetic division</strong> is a faster method for dividing by linear polynomials of the form $(x - a)$. It uses only the coefficients.</p>

        <h4>Steps for Synthetic Division</h4>
        <ol style="margin-top: 10px;">
            <li>Write the coefficients of the polynomial (including zeros for missing terms)</li>
            <li>Write $a$ (the value that makes $x - a = 0$) to the left</li>
            <li>Bring down the first coefficient</li>
            <li>Multiply it by $a$ and write the result under the next coefficient</li>
            <li>Add the column and write the result below</li>
            <li>Repeat until all coefficients are processed</li>
            <li>The last number is the remainder; the others are the quotient coefficients</li>
        </ol>

        <div class="worked-example formula-box">
            <p><strong>Example 3:</strong> Divide $2x^3 - 3x^2 + 4x - 5$ by $(x - 2)$ using synthetic division</p>

            <p style="margin-top: 15px;"><strong>Setup:</strong> $a = 2$, coefficients: 2, $-3$, 4, $-5$</p>

            <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
                <tr >
                    <td style="padding: 8px; text-align: center;"><strong>2</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">2</td>
                    <td style="padding: 8px; text-align: center;">$-3$</td>
                    <td style="padding: 8px; text-align: center;">4</td>
                    <td style="padding: 8px; text-align: center;">$-5$</td>
                </tr>
                <tr >
                    <td style="padding: 8px;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">4</td>
                    <td style="padding: 8px; text-align: center;">2</td>
                    <td style="padding: 8px; text-align: center;">12</td>
                </tr>
                <tr >
                    <td style="padding: 8px;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">2</td>
                    <td style="padding: 8px; text-align: center;">1</td>
                    <td style="padding: 8px; text-align: center;">6</td>
                    <td style="padding: 8px; text-align: center;"><strong>7</strong></td>
                </tr>
            </table>

            <p style="margin-top: 15px;"><strong>Reading the result:</strong></p>
            <ul style="margin-top: 10px;">
                <li>Quotient coefficients: 2, 1, 6 $\\to$ <strong>$2x^2 + x + 6$</strong></li>
                <li>Remainder: <strong>$7$</strong></li>
            </ul>
            <p style="margin-top: 10px;">So: $2x^3 - 3x^2 + 4x - 5 = (x - 2)(2x^2 + x + 6) + 7$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 4:</strong> Divide $x^3 + 2x^2 - 5x - 6$ by $(x + 1)$ using synthetic division</p>

            <p style="margin-top: 15px;"><strong>Setup:</strong> $a = -1$ (since divisor is $x + 1 = x - (-1)$), coefficients: 1, 2, $-5$, $-6$</p>

            <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
                <tr >
                    <td style="padding: 8px; text-align: center;"><strong>$-1$</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">1</td>
                    <td style="padding: 8px; text-align: center;">2</td>
                    <td style="padding: 8px; text-align: center;">$-5$</td>
                    <td style="padding: 8px; text-align: center;">$-6$</td>
                </tr>
                <tr >
                    <td style="padding: 8px;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">$-1$</td>
                    <td style="padding: 8px; text-align: center;">6</td>
                    <td style="padding: 8px; text-align: center;">$-1$</td>
                </tr>
                <tr >
                    <td style="padding: 8px;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;"><strong>&nbsp;</strong></td>
                    <td style="padding: 8px; text-align: center;">1</td>
                    <td style="padding: 8px; text-align: center;">1</td>
                    <td style="padding: 8px; text-align: center;">$-6$</td>
                    <td style="padding: 8px; text-align: center;"><strong>$0$</strong></td>
                </tr>
            </table>

            <p style="margin-top: 15px;"><strong>Result:</strong></p>
            <ul style="margin-top: 10px;">
                <li>Quotient: <strong>$x^2 + x - 6$</strong></li>
                <li>Remainder: <strong>$0$</strong></li>
            </ul>
            <p style="margin-top: 10px;">So: $x^3 + 2x^2 - 5x - 6 = (x + 1)(x^2 + x - 6)$</p>
            <p style="margin-top: 10px;">Further factoring: $= (x + 1)(x + 3)(x - 2)$</p>
        </div>

        <div class="success-box formula-box">
            <p><strong>When to use synthetic division:</strong> Use it when dividing by $(x - a)$. It's much faster than long division and requires less writing!</p>
        </div>
        """
    }
]
