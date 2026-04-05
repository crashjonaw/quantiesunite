TITLE = "Finding Specific Terms in Binomial Expansions"

SECTIONS = [
    {
        "title": "The General Term Formula",
        "body": """
        <div class="concept-box">
            <h4 class="accent-heading">Why Not Expand Everything?</h4>
            <p >
                For the expansion of \\((a + b)^{20}\\), we don't need all 21 terms.
                Often we only need <em>one specific term</em> — like the term with \\(x^5\\).
            </p>
            <p >
                The general term formula lets us find it directly.
            </p>
        </div>

        <p style="text-align: center; margin: 20px 0; padding: 15px; border-radius: 4px">
            <strong style="font-size: 1.1em">The (k+1)th term:</strong>
            <p style="margin: 10px 0;">
                $$T_{k+1} = C(n,k) \, a^{n-k} \, b^k$$
            </p>
        </p>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 1:</strong> Find the 3rd term in \\((x + 2)^5\\)</p>
            <p style="margin: 5px 0;">
                For the 3rd term: \\(k+1 = 3\\), so \\(k = 2\\)
            </p>
            <p style="margin: 5px 0;">
                $$T_3 = C(5, 2) \, x^{5-2} \, (2)^2 = 10 \\cdot x^3 \\cdot 4 = 40x^3$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                No need to expand the whole thing!
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 0;">
                <strong class="accent-heading">Key Point:</strong> The term number counts from 1, but k (in the binomial coefficient) starts from 0.
                So \\(\\text{term number} = k + 1\\).
            </p>
        </div>
        """
    },
    {
        "title": "Finding a Term With a Specific Power",
        "body": """
        <h4 class="accent-heading">The Strategy</h4>

        <p >
            Suppose we need the term containing \\(x^m\\) in the expansion of \\((a + x)^n\\).
        </p>

        <div class="concept-box">
            <p style="margin: 5px 0;"><strong class="accent-heading">Step 1:</strong> In the general term \\(T_{k+1} = C(n,k) \, a^{n-k} \, x^k\\), the power of \\(x\\) is \\(k\\).</p>
            <p style="margin: 5px 0;"><strong class="accent-heading">Step 2:</strong> Set \\(k = m\\) (to get \\(x^m\\)).</p>
            <p style="margin: 5px 0;"><strong class="accent-heading">Step 3:</strong> Substitute into \\(T_{k+1}\\) to find the term.</p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 2:</strong> Find the term with \\(x^2\\) in \\((3 + x)^5\\)</p>
            <p style="margin: 5px 0;">
                Power of \\(x\\) is \\(k\\), so \\(k = 2\\).
            </p>
            <p style="margin: 5px 0;">
                $$T_3 = C(5, 2) \, (3)^{5-2} \, x^2 = 10 \\cdot 27 \\cdot x^2 = 270x^2$$
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 3:</strong> Find the term with \\(x^0\\) (constant term) in \\((2x - \\frac{1}{x})^6\\)</p>
            <p style="margin: 5px 0;">
                General term: \\(T_{k+1} = C(6,k)(2x)^{6-k}(-\\frac{1}{x})^k = C(6,k) \\cdot 2^{6-k} \\cdot (-1)^k \\cdot x^{(6-k)-k}\\)
            </p>
            <p style="margin: 5px 0;">
                Power of \\(x\\) is \\((6-k) - k = 6 - 2k\\). For constant term: \\(6 - 2k = 0 \Rightarrow k = 3\\)
            </p>
            <p style="margin: 5px 0;">
                $$T_4 = C(6,3) \\cdot 2^3 \\cdot (-1)^3 = 20 \\cdot 8 \\cdot (-1) = -160$$
            </p>
        </div>
        """
    },
    {
        "title": "Finding Middle Terms",
        "body": """
        <h4 class="accent-heading">Special Case: The Middle of the Expansion</h4>

        <p >
            The expansion of \\((a + b)^n\\) has \\(n+1\\) terms total. The middle term(s) have special properties.
        </p>

        <div class="concept-box">
            <p style="margin: 5px 0;">
                <strong class="accent-heading">If n is even:</strong> There is one middle term at position \\(\\frac{n}{2} + 1\\)
            </p>
            <p style="margin: 5px 0;">
                $$T_{\\frac{n}{2}+1} = C(n, \\frac{n}{2}) \, a^{\\frac{n}{2}} \, b^{\\frac{n}{2}}$$
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 5px 0;">
                <strong class="accent-heading">If n is odd:</strong> There are two middle terms at positions \\(\\frac{n+1}{2}\\) and \\(\\frac{n+3}{2}\\)
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 4:</strong> Find the middle term(s) in \\((a + b)^6\\)</p>
            <p style="margin: 5px 0;">
                \\(n = 6\\) (even), so one middle term at position \\(\\frac{6}{2} + 1 = 4\\)
            </p>
            <p style="margin: 5px 0;">
                $$T_4 = C(6, 3) \, a^3 \, b^3 = 20 \, a^3 \, b^3$$
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 5:</strong> Find the middle terms in \\((x + y)^5\\)</p>
            <p style="margin: 5px 0;">
                \\(n = 5\\) (odd), so two middle terms at positions \\(\\frac{5+1}{2} = 3\\) and \\(\\frac{5+3}{2} = 4\\)
            </p>
            <p style="margin: 5px 0;">
                $$T_3 = C(5, 2) \, x^3 \, y^2 = 10 x^3 y^2$$
                $$T_4 = C(5, 3) \, x^2 \, y^3 = 10 x^2 y^3$$
            </p>
        </div>

        <div class="success-box" style="margin: 15px 0; padding: 12px;  border-left: 4px solid #3fb950; border-radius: 4px;">
            <p style="margin: 0;">
                ✓ The middle term(s) always have the largest binomial coefficient!
            </p>
        </div>
        """
    }
]
