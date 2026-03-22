SECTIONS = [
    {
        "title": "Pascal's Triangle and Binomial Coefficients",
        "body": """
        <h3>Discovering the Pattern</h3>
        <p><strong>Pascal's Triangle</strong> is a triangular arrangement of numbers where each entry is the sum of the two numbers above it.</p>

        <table style="width: auto; margin: 20px auto; border-collapse: collapse; text-align: center;">
            <tr><td style="padding: 8px;">1</td></tr>
            <tr><td style="padding: 8px;">1</td><td style="padding: 8px;">1</td></tr>
            <tr><td style="padding: 8px;">1</td><td style="padding: 8px;">2</td><td style="padding: 8px;">1</td></tr>
            <tr><td style="padding: 8px;">1</td><td style="padding: 8px;">3</td><td style="padding: 8px;">3</td><td style="padding: 8px;">1</td></tr>
            <tr><td style="padding: 8px;">1</td><td style="padding: 8px;">4</td><td style="padding: 8px;">6</td><td style="padding: 8px;">4</td><td style="padding: 8px;">1</td></tr>
        </table>

        <h4>Connection to Binomial Expansion</h4>
        <p>The entries in row n of Pascal's Triangle are the binomial coefficients C(n,k) for the expansion of (a + b)ⁿ.</p>

        <h4>Binomial Coefficients: C(n,k) or "n choose k"</h4>
        <p style="text-align: center; font-size: 1.2em;">
            <strong>C(n,k) = (n!)/(k!(n-k)!)</strong>
        </p>

        <p>This counts the number of ways to choose k objects from n objects.</p>

        <div class="example-box">
            <p><strong>Example 1:</strong> Calculate C(5, 2)</p>
            <p>C(5, 2) = 5!/(2!3!) = (5 × 4)/(2 × 1) = 10</p>
        </div>

        <h4>Properties of Binomial Coefficients</h4>
        <ul>
            <li>C(n, 0) = 1 (one way to choose nothing)</li>
            <li>C(n, n) = 1 (one way to choose everything)</li>
            <li>C(n, k) = C(n, n-k) (symmetry)</li>
            <li>C(n, k) + C(n, k+1) = C(n+1, k+1) (Pascal's identity)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 2:</strong> Find C(6, 4)</p>
            <p>C(6, 4) = C(6, 2) = 6!/(2!4!) = 15</p>
        </div>
        """
    },
    {
        "title": "The Binomial Theorem",
        "body": """
        <h3>Expanding (a + b)ⁿ</h3>
        <p>The Binomial Theorem gives a formula for expanding any power of a binomial.</p>

        <h4>Statement of the Theorem</h4>
        <p style="text-align: center; font-size: 1.1em;">
            <strong>(a + b)ⁿ = Σ C(n,k) a^(n-k) b^k</strong> for k = 0 to n
        </p>

        <p>Or written out:</p>
        <p style="text-align: center;">
            <strong>(a + b)ⁿ = a^n + C(n,1)a^(n-1)b + C(n,2)a^(n-2)b² + ... + C(n,n-1)ab^(n-1) + b^n</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Expand (a + b)⁴</p>
            <p>Coefficients from row 4 of Pascal's Triangle: 1, 4, 6, 4, 1</p>
            <p>(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴</p>
        </div>

        <div class="example-box">
            <p><strong>Example 4:</strong> Expand (2x - 3)³</p>
            <p>Using the theorem with a = 2x, b = -3, n = 3:</p>
            <p>(2x)³ + 3(2x)²(-3) + 3(2x)(-3)² + (-3)³</p>
            <p>= 8x³ + 3(4x²)(-3) + 3(2x)(9) - 27</p>
            <p>= 8x³ - 36x² + 54x - 27</p>
        </div>

        <h4>Why It Works: Combinatorial Proof</h4>
        <p>(a + b)ⁿ means multiplying (a + b) by itself n times. Each term in the expansion comes from choosing either a or b from each factor. C(n, k) counts how many ways to choose b exactly k times (and a exactly n-k times).</p>
        """
    },
    {
        "title": "The General Term",
        "body": """
        <h3>Finding a Specific Term Without Full Expansion</h3>
        <p>For the expansion of (a + b)ⁿ, the (k+1)th term is:</p>

        <p style="text-align: center; font-size: 1.2em;">
            <strong>T_(k+1) = C(n,k) a^(n-k) b^k</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Find the 5th term in the expansion of (x + 2)⁷</p>
            <p>The 5th term means k+1 = 5, so k = 4</p>
            <p>T₅ = C(7, 4) x^(7-4) (2)⁴</p>
            <p>= 35 × x³ × 16</p>
            <p>= 560x³</p>
        </div>

        <h4>Finding a Term With a Specific Power</h4>
        <p>If you need the term containing x^m in (a + x)ⁿ:</p>
        <ol>
            <li>Set n - k = m (the power of the first term)</li>
            <li>Solve for k</li>
            <li>Use the general term formula</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 6:</strong> Find the term containing x² in (3 + x)⁵</p>
            <p>Need: n - k = 2, so 5 - k = 2, giving k = 3</p>
            <p>T₄ = C(5, 3) (3)^(5-3) (x)³</p>
            <p>= 10 × 9 × x³</p>
            <p>= 90x³ (wait, that's x³, not x²)</p>
            <p>Actually, if we need x², then n - k = 2 gives 5 - k = 2, so k = 3. But then the term is x³. If we want x², we need k = 2.</p>
            <p>Let me reconsider: We want the x² term, so the power of x is 2 = k. Then n - k = 5 - 2 = 3.</p>
            <p>T₃ = C(5, 2) (3)³ (x)²</p>
            <p>= 10 × 27 × x²</p>
            <p>= 270x²</p>
        </div>

        <h4>Middle Term(s)</h4>
        <p>In the expansion of (a + b)ⁿ:</p>
        <ul>
            <li>If n is even, there's one middle term: T_(n/2 + 1) = C(n, n/2) a^(n/2) b^(n/2)</li>
            <li>If n is odd, there are two middle terms: T_((n+1)/2) and T_((n+3)/2)</li>
        </ul>
        """
    },
    {
        "title": "Applications of the Binomial Theorem",
        "body": """
        <h3>Using the Binomial Theorem</h3>

        <h4>Finding Coefficients</h4>
        <div class="example-box">
            <p><strong>Example 7:</strong> Find the coefficient of x² in (1 + 3x)⁵</p>
            <p>The x² term comes from k = 2 (since b = 3x, so k tells us which power of 3x)</p>
            <p>T₃ = C(5, 2) (1)³ (3x)²</p>
            <p>= 10 × 9x²</p>
            <p>= 90x²</p>
            <p><strong>Coefficient = 90</strong></p>
        </div>

        <h4>Numerical Approximations</h4>
        <p>The binomial theorem can approximate values like (1 + x)ⁿ for small x.</p>

        <div class="example-box">
            <p><strong>Example 8:</strong> Approximate (1.02)³</p>
            <p>(1.02)³ = (1 + 0.02)³</p>
            <p>= 1 + 3(0.02) + 3(0.02)² + (0.02)³</p>
            <p>= 1 + 0.06 + 0.0012 + 0.000008</p>
            <p>≈ 1.061208</p>
            <p>(Exact: 1.061208, so our approximation is very good!)</p>
        </div>

        <h4>Proving Identities</h4>
        <p>The binomial theorem can prove sum identities.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Prove C(n,0) + C(n,1) + C(n,2) + ... + C(n,n) = 2ⁿ</p>
            <p>Set a = b = 1 in the binomial theorem:</p>
            <p>(1 + 1)ⁿ = Σ C(n,k)</p>
            <p>2ⁿ = Σ C(n,k)</p>
            <p>This proves the identity.</p>
        </div>

        <h4>Negative and Rational Exponents</h4>
        <p>The binomial theorem extends to non-integer exponents with the form:</p>
        <p style="text-align: center;">
            <strong>(1 + x)ⁿ = 1 + nx + n(n-1)x²/2! + n(n-1)(n-2)x³/3! + ...</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 10:</strong> Expand (1 + x)^(-1) = 1/(1 + x) for |x| < 1</p>
            <p>(1 + x)^(-1) = 1 + (-1)x + (-1)(-2)x²/2! + (-1)(-2)(-3)x³/3! + ...</p>
            <p>= 1 - x + x² - x³ + ...</p>
            <p>(This is the geometric series!)</p>
        </div>
        """
    },
    {
        "title": "Rational Index (Extension)",
        "body": """
        <h3>Expanding (a + b)^(1/n) and Similar Expressions</h3>
        <p>The binomial theorem generalizes to rational exponents, giving infinite series.</p>

        <h4>Using the General Binomial Series</h4>
        <p style="text-align: center;">
            <strong>(1 + x)^r = Σ C(r,k) x^k</strong> for k = 0 to ∞, valid when |x| < 1
        </p>

        <p>Where C(r, k) = r(r-1)(r-2)...(r-k+1) / k!</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Expand √(1 + x) = (1 + x)^(1/2) (first few terms)</p>
            <p>r = 1/2</p>
            <p>C(1/2, 0) = 1</p>
            <p>C(1/2, 1) = 1/2</p>
            <p>C(1/2, 2) = (1/2)(-1/2) / 2! = -1/8</p>
            <p>C(1/2, 3) = (1/2)(-1/2)(-3/2) / 3! = 1/16</p>
            <p>(1 + x)^(1/2) = 1 + (1/2)x - (1/8)x² + (1/16)x³ - ...</p>
        </div>

        <h4>Practical Applications</h4>
        <p>Used for approximating square roots, cube roots, and other calculations without a calculator.</p>

        <div class="example-box">
            <p><strong>Example 12:</strong> Approximate √1.1</p>
            <p>√1.1 = (1 + 0.1)^(1/2) ≈ 1 + (1/2)(0.1) - (1/8)(0.01) + (1/16)(0.001)</p>
            <p>≈ 1 + 0.05 - 0.00125 + 0.0000625</p>
            <p>≈ 1.04881</p>
            <p>(Exact: 1.04881, excellent agreement!)</p>
        </div>
        """
    }
]
