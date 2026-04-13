TITLE = "The Binomial Theorem"

SECTIONS = [
    {
        "title": "The Statement: Expanding (a + b)ⁿ",
        "body": """
        <div class="concept-box">
            <h4 class="accent-heading">The Big Picture</h4>
            <p >
                Multiplying out \\((a + b)^n\\) by hand becomes tedious:
            </p>
            <ul >
                <li>\\((a+b)^2\\) has 4 terms to track</li>
                <li>\\((a+b)^3\\) has 8 terms</li>
                <li>\\((a+b)^{10}\\) has 1024 terms!</li>
            </ul>
            <p >
                The <strong>Binomial Theorem</strong> gives us a direct formula that avoids expansion.
            </p>
        </div>

        <h4 class="accent-heading" style="margin-top: 20px;">The Formula</h4>

        <div style="text-align: center; margin: 20px 0; padding: 20px; border-radius: 4px">
            <p style="margin: 5px 0; font-size: 1.05em">
                <strong class="accent-heading">$$(a + b)^n = \\sum_{k=0}^{n} C(n,k) a^{n-k} b^k$$</strong>
            </p>
        </div>

        <p style="margin: 20px 0">
            Or written out term-by-term:
        </p>

        <p style="text-align: center; margin: 15px 0; padding: 15px; border-radius: 4px">
            $$(a + b)^n = a^n + C(n,1)a^{n-1}b + C(n,2)a^{n-2}b^2 + \\cdots + C(n,n-1)ab^{n-1} + b^n$$
        </p>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example:</strong> Expand \\((a + b)^4\\)</p>
            <p style="margin: 5px 0;">
                Coefficients from row 4 of Pascal's Triangle: <strong>1, 4, 6, 4, 1</strong>
            </p>
            <p style="margin: 5px 0;">
                $$(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                ✓ Notice: Each term has total degree 4, and the coefficients are the binomial numbers.
            </p>
        </div>
        """
    },
    {
        "title": "Why It Works: The Combinatorial Proof",
        "body": """
        <h4 class="accent-heading">First Principles Reasoning</h4>

        <p >
            When we expand \\((a + b)^n\\), we multiply \\((a + b)\\) by itself n times:
        </p>

        <p style="text-align: center; margin: 15px 0; padding: 10px; border-radius: 4px">
            $$(a + b)^3 = (a + b)(a + b)(a + b)$$
        </p>

        <div class="concept-box">
            <p style="margin: 10px 0;">
                <strong class="accent-heading">Key insight:</strong> Each term in the final expansion comes from choosing either \\(a\\) or \\(b\\)
                from <em>each</em> factor.
            </p>
            <p style="margin: 10px 0;">
                To get \\(a^2b\\) in the expansion of \\((a+b)^3\\), we must:
            </p>
            <ul >
                <li>Choose \\(a\\) from exactly 2 of the 3 factors</li>
                <li>Choose \\(b\\) from exactly 1 factor</li>
            </ul>
            <p style="margin: 10px 0;">
                <strong>How many ways?</strong> Exactly \\(C(3, 1) = 3\\) ways
                (choose which 1 factor gives \\(b\\)).
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example:</strong> Expand \\((2x - 3)^3\\)</p>
            <p style="margin: 5px 0;">
                Use \\(a = 2x\\), \\(b = -3\\), \\(n = 3\\). Coefficients are 1, 3, 3, 1.
            </p>
            <p style="margin: 5px 0;">
                $$\\begin{align}
                (2x - 3)^3 &= (2x)^3 + 3(2x)^2(-3) + 3(2x)(-3)^2 + (-3)^3\\
                &= 8x^3 - 36x^2 + 54x - 27
                \\end{align}$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                Each coefficient comes from \\(C(3,k)\\), and we account for powers of \\(2x\\) and \\(-3\\).
            </p>
        </div>
        """
    },
    {
        "title": "Using the Theorem for Any Binomial",
        "body": """
        <h4 class="accent-heading">General Pattern</h4>

        <p >
            To expand \\((p + q)^n\\):
        </p>

        <div class="concept-box">
            <ol >
                <li><strong>Identify n:</strong> The exponent</li>
                <li><strong>Write out the pattern:</strong> \\(C(n,0)p^n + C(n,1)p^{n-1}q + \\cdots + C(n,n)q^n\\)</li>
                <li><strong>Calculate binomial coefficients:</strong> Use Pascal's Triangle or the formula</li>
                <li><strong>Substitute p and q:</strong> Apply the actual terms, paying attention to signs</li>
            </ol>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example:</strong> Expand \\((x + 2)^4\\)</p>
            <p style="margin: 5px 0;">
                \\(n = 4\\), coefficients: 1, 4, 6, 4, 1
            </p>
            <p style="margin: 5px 0;">
                $$\\begin{align}
                (x + 2)^4 &= x^4 + 4x^3(2) + 6x^2(2)^2 + 4x(2)^3 + (2)^4\\
                &= x^4 + 8x^3 + 24x^2 + 32x + 16
                \\end{align}$$
            </p>
        </div>

        <div class="warning-box" style="margin: 15px 0; padding: 12px; border-left: 4px solid #d29922; border-radius: 4px;">
            <p style="margin: 0;">
                <strong style="color: #d29922;">⚠️ Watch signs!</strong> When \\(b\\) is negative (like \\((a - b)^n\\)), alternating
                terms become negative.
            </p>
        </div>
        """
    }
]
