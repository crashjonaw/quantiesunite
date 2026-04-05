TITLE = "Applications of the Binomial Theorem"

SECTIONS = [
    {
        "title": "Finding Coefficients",
        "body": """
        <h4 class="accent-heading">A Common Exam Question</h4>

        <p >
            Often you're asked to find <strong>just the coefficient</strong> of a specific term, not the entire expansion.
            Use the general term formula and extract the numeric coefficient.
        </p>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 1:</strong> Find the coefficient of \\(x^2\\) in \\((1 + 3x)^5\\)</p>
            <p style="margin: 5px 0;">
                The \\(x^2\\) term comes from \\(k = 2\\) (since the term is \\((3x)^2\\) times a power of 1).
            </p>
            <p style="margin: 5px 0;">
                $$T_3 = C(5, 2) \cdot (1)^{5-2} \cdot (3x)^2 = 10 \cdot 1 \cdot 9x^2 = 90x^2$$
            </p>
            <p style="margin: 5px 0;">
                <strong class="accent-heading">Coefficient = 90</strong>
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 2:</strong> Find the coefficient of \\(a^2b^3\\) in \\((a + 2b)^5\\)</p>
            <p style="margin: 5px 0;">
                We need \\(a^{5-k} = a^2\\), so \\(k = 3\\).
            </p>
            <p style="margin: 5px 0;">
                $$T_4 = C(5, 3) \cdot a^2 \cdot (2b)^3 = 10 \cdot a^2 \cdot 8b^3 = 80a^2b^3$$
            </p>
            <p style="margin: 5px 0;">
                <strong class="accent-heading">Coefficient = 80</strong>
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 0;">
                <strong class="accent-heading">Strategy:</strong> Identify which value of \\(k\\) gives you the term you want,
                then compute \\(C(n,k)\\) and multiply by all other factors.
            </p>
        </div>
        """
    },
    {
        "title": "Numerical Approximations",
        "body": """
        <h4 class="accent-heading">Using Binomial Expansion for Estimation</h4>

        <p >
            For expressions like \\((1 + x)^n\\) where \\(|x|\\) is small, the first few terms of the binomial expansion
            give an excellent approximation, without needing a calculator.
        </p>

        <div class="concept-box">
            <p style="margin: 10px 0;">
                <strong class="accent-heading">Why?</strong> When \\(|x|\\) is small, the terms \\(x^2, x^3, \ldots\\) become negligibly small very quickly.
                For example, if \\(x = 0.01\\), then \\(x^2 = 0.0001\\) and \\(x^3 = 0.000001\\).
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 3:</strong> Approximate \\((1.02)^3\\)</p>
            <p style="margin: 5px 0;">
                Write as \\((1 + 0.02)^3\\) with \\(n = 3, x = 0.02\\).
            </p>
            <p style="margin: 5px 0;">
                Coefficients: 1, 3, 3, 1
            </p>
            <p style="margin: 5px 0;">
                $$\\begin{align}
                (1.02)^3 &= 1 + 3(0.02) + 3(0.02)^2 + (0.02)^3\\
                &= 1 + 0.06 + 0.0012 + 0.000008\\
                &\approx 1.0612
                \\end{align}$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                (Exact value: 1.061208, so our approximation is extremely accurate!)
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 4:</strong> Approximate \\(\\sqrt{1.1}\\) to 4 decimal places</p>
            <p style="margin: 5px 0;">
                Write as \\((1 + 0.1)^{1/2}\\). Using the generalized binomial series (see next section):
            </p>
            <p style="margin: 5px 0;">
                $$(1.1)^{1/2} = 1 + \\frac{1}{2}(0.1) - \\frac{1}{8}(0.1)^2 + \\frac{1}{16}(0.1)^3 - \cdots$$
            </p>
            <p style="margin: 5px 0;">
                $$= 1 + 0.05 - 0.00125 + 0.0000625 - \cdots \approx 1.0488$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                (Exact: 1.048809, excellent agreement!)
            </p>
        </div>

        <div class="success-box" style="margin: 15px 0; padding: 12px;  border-left: 4px solid #3fb950; border-radius: 4px;">
            <p style="margin: 0;">
                ✓ For small x, often just 2-3 terms suffice for high accuracy!
            </p>
        </div>
        """
    },
    {
        "title": "Proving Algebraic Identities",
        "body": """
        <h4 class="accent-heading">A Powerful Proof Technique</h4>

        <p >
            The binomial theorem can prove sum identities by setting specific values of \\(a\\) and \\(b\\).
        </p>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 5:</strong> Prove \\(C(n,0) + C(n,1) + C(n,2) + \cdots + C(n,n) = 2^n\\)</p>
            <p style="margin: 5px 0;">
                Start with the binomial theorem:
            </p>
            <p style="margin: 5px 0;">
                $$(a + b)^n = \\sum_{k=0}^{n} C(n,k) \, a^{n-k} \, b^k$$
            </p>
            <p style="margin: 5px 0;">
                Set \\(a = 1, b = 1\\):
            </p>
            <p style="margin: 5px 0;">
                $$(1 + 1)^n = \\sum_{k=0}^{n} C(n,k) \cdot 1^{n-k} \cdot 1^k = \\sum_{k=0}^{n} C(n,k)$$
            </p>
            <p style="margin: 5px 0;">
                <strong class="accent-heading">Therefore:</strong> \\(2^n = C(n,0) + C(n,1) + \cdots + C(n,n)\\) ✓
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 6:</strong> Prove \\(C(n,0) - C(n,1) + C(n,2) - \cdots + (-1)^n C(n,n) = 0\\) for \\(n > 0\\)</p>
            <p style="margin: 5px 0;">
                Set \\(a = 1, b = -1\\):
            </p>
            <p style="margin: 5px 0;">
                $$(1 - 1)^n = \\sum_{k=0}^{n} C(n,k) \cdot 1^{n-k} \cdot (-1)^k$$
            </p>
            <p style="margin: 5px 0;">
                <strong class="accent-heading">Therefore:</strong> \\(0 = C(n,0) - C(n,1) + C(n,2) - \cdots + (-1)^n C(n,n)\\) ✓
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 0;">
                <strong class="accent-heading">Key insight:</strong> Substituting \\(a = 1, b = -1, a = 1, b = 1\\), etc., collapses the sum into something simple.
            </p>
        </div>
        """
    },
    {
        "title": "The Generalized Binomial Theorem (Non-Integer Exponents)",
        "body": """
        <h4 class="accent-heading">Extending Beyond Positive Integers</h4>

        <p >
            The binomial theorem extends to <strong>any exponent</strong> (negative, fractional, irrational), but the result
            is an <strong>infinite series</strong> instead of a finite sum.
        </p>

        <div style="text-align: center; margin: 20px 0; padding: 15px; border-radius: 4px">
            <p style="margin: 5px 0;">
                For any real \\(r\\) and \\(|x| < 1\\):
            </p>
            <p style="margin: 10px 0;">
                $$(1 + x)^r = 1 + rx + \\frac{r(r-1)}{2!}x^2 + \\frac{r(r-1)(r-2)}{3!}x^3 + \cdots$$
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 7:</strong> Expand \\((1 + x)^{-1}\\) as a series</p>
            <p style="margin: 5px 0;">
                With \\(r = -1\\):
            </p>
            <p style="margin: 5px 0;">
                $$\\begin{align}
                (1 + x)^{-1} &= 1 + (-1)x + \\frac{(-1)(-2)}{2!}x^2 + \\frac{(-1)(-2)(-3)}{3!}x^3 + \cdots\\
                &= 1 - x + x^2 - x^3 + \cdots
                \\end{align}$$
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                This is the geometric series!
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;"><strong class="accent-heading">Example 8:</strong> Expand \\((1 + x)^{1/2}\\) (first 3 terms)</p>
            <p style="margin: 5px 0;">
                With \\(r = 1/2\\):
            </p>
            <p style="margin: 5px 0;">
                $$\\begin{align}
                (1 + x)^{1/2} &= 1 + \\frac{1}{2}x + \\frac{(1/2)(-1/2)}{2!}x^2 + \cdots\\
                &= 1 + \\frac{1}{2}x - \\frac{1}{8}x^2 + \cdots
                \\end{align}$$
            </p>
        </div>

        <div class="warning-box" style="margin: 15px 0; padding: 12px; border-left: 4px solid #d29922; border-radius: 4px;">
            <p style="margin: 0;">
                <strong style="color: #d29922;">⚠️ Convergence:</strong> These series only converge for \\(|x| < 1\\).
                Always check convergence before using them!
            </p>
        </div>
        """
    }
]
