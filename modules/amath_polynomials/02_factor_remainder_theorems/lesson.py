TITLE = "Factor and Remainder Theorems"

SECTIONS = [
    {
        "title": "The Remainder Theorem",
        "body": """
        <h3>Finding Remainders Without Long Division</h3>
        <p>When we divide a polynomial $f(x)$ by a linear polynomial $(x - a)$, we want to find the remainder without doing lengthy long division. The Remainder Theorem gives us a shortcut.</p>

        <h4>The Remainder Theorem</h4>
        <div class="concept-box formula-box">
            <p>When a polynomial $f(x)$ is divided by $(x - a)$, the remainder is <strong>$f(a)$</strong>.</p>
            <p style="margin-top: 15px;">$$f(x) = (x - a) \\cdot q(x) + r, \\quad \\text{where } r = f(a)$$</p>
        </div>

        <h4>Why This Works</h4>
        <p>When we divide $f(x)$ by $(x - a)$, we get: $f(x) = (x - a) \\cdot q(x) + r$, where $r$ is a constant (remainder has lower degree than divisor).</p>
        <p>Substitute $x = a$ into both sides:</p>
        <p>$$f(a) = (a - a) \\cdot q(a) + r = 0 + r = r$$</p>
        <p style="margin-top: 10px;">So the remainder equals $f(a)$.</p>

        <div class="worked-example formula-box">
            <p><strong>Example 1:</strong> Find the remainder when $f(x) = 2x^3 - 3x^2 + x - 5$ is divided by $(x - 2)$</p>
            <p style="margin-top: 10px;">By the Remainder Theorem, the remainder $= f(2)$</p>
            <p style="margin-top: 10px;">$f(2) = 2(2)^3 - 3(2)^2 + (2) - 5$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= 2(8) - 3(4) + 2 - 5$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= 16 - 12 + 2 - 5$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= $ <strong>$1$</strong></p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 2:</strong> Find the remainder when $x^4 - 5x^2 + 3$ is divided by $(x + 1)$</p>
            <p style="margin-top: 10px;">The divisor is $(x - (-1))$, so $a = -1$</p>
            <p style="margin-top: 10px;">Remainder $= f(-1) = (-1)^4 - 5(-1)^2 + 3$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= 1 - 5(1) + 3$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= 1 - 5 + 3$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;$= $ <strong>$-1$</strong></p>
        </div>
        """
    },
    {
        "title": "The Factor Theorem",
        "body": """
        <h3>Determining When $(x - a)$ is a Factor</h3>
        <p>The Factor Theorem is a direct consequence of the Remainder Theorem. It tells us exactly when a linear polynomial $(x - a)$ is a factor of $f(x)$.</p>

        <h4>The Factor Theorem</h4>
        <div class="concept-box formula-box">
            <p>$(x - a)$ is a factor of $f(x)$ <strong>if and only if</strong> $f(a) = 0$.</p>
            <p style="margin-top: 15px;"><strong>In other words:</strong> $(x - a)$ divides $f(x)$ evenly with remainder 0 exactly when $a$ is a root (or zero) of $f(x)$.</p>
        </div>

        <h4>Proof</h4>
        <p>By the Remainder Theorem: $f(x) = (x - a) \\cdot q(x) + f(a)$</p>
        <ul style="margin-top: 10px;">
            <li>If $f(a) = 0$, then $f(x) = (x - a) \\cdot q(x)$, so $(x - a)$ is a factor</li>
            <li>If $(x - a)$ is a factor, then $f(x) = (x - a) \\cdot q(x)$, so $f(a) = 0$</li>
        </ul>

        <div class="worked-example formula-box">
            <p><strong>Example 3:</strong> Is $(x + 1)$ a factor of $x^3 + 2x^2 - x - 2$?</p>
            <p style="margin-top: 10px;">Let $f(x) = x^3 + 2x^2 - x - 2$. Check if $f(-1) = 0$:</p>
            <p style="margin-top: 10px;">$f(-1) = (-1)^3 + 2(-1)^2 - (-1) - 2$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= -1 + 2 + 1 - 2$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= $ <strong>$0$</strong></p>
            <p style="margin-top: 10px;">Yes! $(x + 1)$ is a factor.</p>
            <p style="margin-top: 15px;">We can factor completely:</p>
            <p style="margin-top: 10px;">$x^3 + 2x^2 - x - 2 = (x + 1)(x^2 + x - 2) = (x + 1)(x + 2)(x - 1)$</p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 4:</strong> Is $(x - 3)$ a factor of $x^3 - 6x^2 + 11x - 6$?</p>
            <p style="margin-top: 10px;">Let $f(x) = x^3 - 6x^2 + 11x - 6$. Check $f(3)$:</p>
            <p style="margin-top: 10px;">$f(3) = (3)^3 - 6(3)^2 + 11(3) - 6$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= 27 - 54 + 33 - 6$</p>
            <p style="margin-top: 10px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= $ <strong>$0$</strong></p>
            <p style="margin-top: 10px;">Yes! $(x - 3)$ is a factor.</p>
        </div>

        <div class="success-box formula-box">
            <p><strong>Key insight:</strong> If $a$ is a root of $f(x)$, then $x = a$, and $(x - a)$ is a factor. Roots, zeros, and factors are intimately connected!</p>
        </div>
        """
    },
    {
        "title": "Using the Theorems to Factor Polynomials",
        "body": """
        <h3>A Strategy for Factoring</h3>
        <p>The Factor Theorem gives us a systematic way to find factors of polynomials:</p>
        <ol style="margin-top: 10px;">
            <li>Find a value $a$ where $f(a) = 0$ (a root)</li>
            <li>Then $(x - a)$ is a factor</li>
            <li>Use polynomial division to find the remaining factor</li>
        </ol>

        <div class="worked-example formula-box">
            <p><strong>Example 5:</strong> Completely factor $f(x) = 2x^3 + 3x^2 - 8x - 12$</p>

            <p style="margin-top: 15px;"><strong>Step 1: Find a root by testing small integers</strong></p>
            <p style="margin-top: 10px;">$f(1) = 2 + 3 - 8 - 12 = -15$ (not a root)</p>
            <p style="margin-top: 5px;">$f(2) = 2(8) + 3(4) - 8(2) - 12 = 16 + 12 - 16 - 12 = 0$</p>
            <p style="margin-top: 5px;">So $(x - 2)$ is a factor.</p>

            <p style="margin-top: 15px;"><strong>Step 2: Divide by $(x - 2)$ to find the quotient</strong></p>
            <p style="margin-top: 10px;">Using synthetic division or long division:</p>
            <p style="margin-top: 10px;">$2x^3 + 3x^2 - 8x - 12 = (x - 2)(2x^2 + 7x + 6)$</p>

            <p style="margin-top: 15px;"><strong>Step 3: Factor the quotient</strong></p>
            <p style="margin-top: 10px;">$2x^2 + 7x + 6 = (2x + 3)(x + 2)$</p>

            <p style="margin-top: 15px;"><strong>Complete factorization:</strong></p>
            <p style="margin-top: 10px;">$f(x) = $ <strong>$(x - 2)(2x + 3)(x + 2)$</strong></p>
        </div>

        <div class="worked-example formula-box">
            <p><strong>Example 6:</strong> Factor $x^3 - 4x^2 + x + 6$</p>

            <p style="margin-top: 10px;">Test small values:</p>
            <p style="margin-top: 10px;">$f(-1) = -1 - 4 - 1 + 6 = 0$</p>
            <p style="margin-top: 10px;">So $(x + 1) = (x - (-1))$ is a factor.</p>

            <p style="margin-top: 15px;">Dividing: $x^3 - 4x^2 + x + 6 = (x + 1)(x^2 - 5x + 6)$</p>

            <p style="margin-top: 10px;">Factor the quadratic: $x^2 - 5x + 6 = (x - 2)(x - 3)$</p>

            <p style="margin-top: 15px;"><strong>Complete factorization:</strong></p>
            <p style="margin-top: 10px;">$f(x) = $ <strong>$(x + 1)(x - 2)(x - 3)$</strong></p>
        </div>
        """
    }
]
