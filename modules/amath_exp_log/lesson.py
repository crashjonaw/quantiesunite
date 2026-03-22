SECTIONS = [
    {
        "title": "Exponential Functions and Exponential Growth",
        "body": """
        <h3>Understanding Exponentials</h3>
        <p>An <strong>exponential function</strong> has the form f(x) = aˣ where a > 0 and a ≠ 1.</p>

        <h4>Key Properties</h4>
        <ul>
            <li>If a > 1: function increases (growth)</li>
            <li>If 0 < a < 1: function decreases (decay)</li>
            <li>Always passes through (0, 1): a⁰ = 1</li>
            <li>Domain: all real numbers</li>
            <li>Range: all positive numbers (y > 0)</li>
            <li>Horizontal asymptote at y = 0</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 1:</strong> f(x) = 2ˣ</p>
            <ul>
                <li>f(0) = 1, f(1) = 2, f(2) = 4, f(3) = 8</li>
                <li>f(-1) = 1/2, f(-2) = 1/4</li>
                <li>Rapid growth as x increases</li>
            </ul>
        </div>

        <h4>Exponential Growth Model</h4>
        <p>Many real phenomena follow: <strong>A(t) = A₀ · aᵗ</strong> or <strong>A(t) = A₀ · e^(kt)</strong></p>
        <ul>
            <li>A₀ = initial amount</li>
            <li>a = growth factor per time unit</li>
            <li>k = growth constant (if using e)</li>
            <li>t = time</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 2:</strong> A bacterial culture doubles every 3 hours. If we start with 1000 bacteria, find the population after 9 hours.</p>
            <p>A(t) = 1000 · 2^(t/3)</p>
            <p>A(9) = 1000 · 2^(9/3) = 1000 · 2³ = 1000 · 8 = 8000 bacteria</p>
        </div>

        <h4>Exponential Decay Model</h4>
        <p>Radioactive decay: <strong>A(t) = A₀ · (1/2)^(t/T)</strong> where T is the half-life</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Carbon-14 has a half-life of 5730 years. If an artifact contains 30% of original C-14, how old is it?</p>
            <p>0.3 = (1/2)^(t/5730)</p>
            <p>log(0.3) = (t/5730) log(0.5)</p>
            <p>t = 5730 × log(0.3)/log(0.5) ≈ 9953 years</p>
        </div>
        """
    },
    {
        "title": "Logarithms: Definition and Properties",
        "body": """
        <h3>Inverse of Exponentials</h3>
        <p><strong>Logarithm</strong> is the inverse function of exponential.</p>

        <h4>Definition</h4>
        <p style="text-align: center; font-size: 1.2em;">
            <strong>If aˣ = y, then log_a(y) = x</strong>
        </p>

        <p>Read: "log base a of y equals x"</p>

        <div class="example-box">
            <p><strong>Example 4:</strong> Express in logarithmic form</p>
            <ul>
                <li>2⁵ = 32 ⟹ log₂(32) = 5</li>
                <li>10³ = 1000 ⟹ log₁₀(1000) = 3</li>
                <li>eˣ = y ⟹ ln(y) = x (natural logarithm)</li>
            </ul>
        </div>

        <h4>Key Properties</h4>
        <ul>
            <li>log_a(1) = 0 (since a⁰ = 1)</li>
            <li>log_a(a) = 1 (since a¹ = a)</li>
            <li>log_a(aˣ) = x (logarithm undoes exponent)</li>
            <li>a^(log_a(y)) = y (exponent undoes logarithm)</li>
        </ul>

        <h4>The Power Rule</h4>
        <p style="text-align: center;"><strong>log_a(xʸ) = y · log_a(x)</strong></p>

        <h4>The Product Rule</h4>
        <p style="text-align: center;"><strong>log_a(xy) = log_a(x) + log_a(y)</strong></p>

        <h4>The Quotient Rule</h4>
        <p style="text-align: center;"><strong>log_a(x/y) = log_a(x) - log_a(y)</strong></p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Expand log₂(8x²y)</p>
            <p>log₂(8x²y) = log₂(8) + log₂(x²) + log₂(y)</p>
            <p>= 3 + 2log₂(x) + log₂(y)</p>
        </div>

        <h4>Change of Base Formula</h4>
        <p style="text-align: center;"><strong>log_a(x) = log_b(x) / log_b(a)</strong></p>

        <p>Useful to convert to a calculator base (usually base 10 or e).</p>

        <div class="example-box">
            <p><strong>Example 6:</strong> Calculate log₃(27)</p>
            <p>Method 1: 3ˣ = 27 = 3³, so x = 3</p>
            <p>Method 2: log₃(27) = log₁₀(27)/log₁₀(3) = 1.431/0.477 ≈ 3</p>
        </div>
        """
    },
    {
        "title": "Solving Exponential and Logarithmic Equations",
        "body": """
        <h3>Techniques for Solving</h3>

        <h4>Solving Exponential Equations</h4>
        <p><strong>Strategy:</strong> Take logarithm of both sides.</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Solve 5ˣ = 80</p>
            <p>Take log of both sides: log(5ˣ) = log(80)</p>
            <p>x · log(5) = log(80)</p>
            <p>x = log(80)/log(5) = 1.903/0.699 ≈ 2.72</p>
        </div>

        <div class="example-box">
            <p><strong>Example 8:</strong> Solve 3^(2x-1) = 27</p>
            <p>Notice 27 = 3³, so: 3^(2x-1) = 3³</p>
            <p>Equate exponents: 2x - 1 = 3</p>
            <p>2x = 4, so x = 2</p>
        </div>

        <h4>Solving Logarithmic Equations</h4>
        <p><strong>Strategy:</strong> Convert to exponential form or use properties.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Solve log₂(x + 3) = 4</p>
            <p>Convert to exponential: x + 3 = 2⁴ = 16</p>
            <p>x = 13</p>
        </div>

        <div class="example-box">
            <p><strong>Example 10:</strong> Solve log(x) + log(x - 3) = log(10)</p>
            <p>Use product rule: log(x(x - 3)) = log(10)</p>
            <p>x(x - 3) = 10</p>
            <p>x² - 3x - 10 = 0</p>
            <p>(x - 5)(x + 2) = 0</p>
            <p>x = 5 or x = -2</p>
            <p>But x > 3 (domain restriction), so x = 5 only</p>
        </div>

        <h4>Important: Domain Restrictions</h4>
        <ul>
            <li>For log_a(x): x must be positive (x > 0)</li>
            <li>For exponential functions: no restrictions on input, but output is always positive</li>
        </ul>
        """
    },
    {
        "title": "Natural Logarithms and e",
        "body": """
        <h3>The Natural Exponential Function</h3>
        <p><strong>e</strong> is a special constant ≈ 2.71828. The function y = eˣ is called the natural exponential.</p>

        <h4>Properties of e</h4>
        <ul>
            <li>eˣ grows faster than aˣ for any other base a</li>
            <li>The derivative of eˣ is eˣ (unique property)</li>
            <li>Used in continuous growth/decay models</li>
        </ul>

        <h4>Natural Logarithm: ln(x)</h4>
        <p><strong>ln(x) = log_e(x)</strong> is the logarithm with base e.</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> If eˣ = 50, find x</p>
            <p>x = ln(50) ≈ 3.912</p>
        </div>

        <h4>Continuous Growth Model</h4>
        <p style="text-align: center;"><strong>A(t) = A₀ · e^(kt)</strong></p>

        <p>Used when interest is compounded continuously or growth is truly continuous.</p>

        <div class="example-box">
            <p><strong>Example 12:</strong> A population grows continuously at 5% per year. Starting with 1000, find the population after 10 years.</p>
            <p>k = 0.05 (5% = 0.05), t = 10, A₀ = 1000</p>
            <p>A(10) = 1000 · e^(0.05×10) = 1000 · e^0.5 ≈ 1000 · 1.649 ≈ 1649</p>
        </div>

        <h4>Properties of ln</h4>
        <ul>
            <li>ln(e) = 1</li>
            <li>ln(1) = 0</li>
            <li>ln(eˣ) = x</li>
            <li>e^(ln(x)) = x</li>
            <li>ln(xy) = ln(x) + ln(y)</li>
            <li>ln(x/y) = ln(x) - ln(y)</li>
            <li>ln(xʸ) = y · ln(x)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 13:</strong> Expand ln(√(x²y))</p>
            <p>ln(√(x²y)) = ln((x²y)^(1/2))</p>
            <p>= (1/2) ln(x²y)</p>
            <p>= (1/2)[ln(x²) + ln(y)]</p>
            <p>= (1/2)[2ln(x) + ln(y)]</p>
            <p>= ln(x) + (1/2)ln(y)</p>
        </div>
        """
    },
    {
        "title": "Applications and Modeling",
        "body": """
        <h3>Real-World Problems</h3>

        <h4>Compound Interest</h4>
        <p><strong>Discrete:</strong> A = P(1 + r/n)^(nt)</p>
        <p><strong>Continuous:</strong> A = Pe^(rt)</p>

        <div class="example-box">
            <p><strong>Example 14:</strong> $5000 invested at 6% annual interest, compounded monthly. Find amount after 5 years.</p>
            <p>P = 5000, r = 0.06, n = 12, t = 5</p>
            <p>A = 5000(1 + 0.06/12)^(60) = 5000(1.005)^60 ≈ 5000 × 1.349 ≈ $6745</p>
        </div>

        <h4>Half-Life and Radioactive Decay</h4>
        <p><strong>A(t) = A₀(1/2)^(t/T)</strong> where T is half-life</p>

        <div class="example-box">
            <p><strong>Example 15:</strong> A radioactive isotope has a half-life of 10 days. After how long will 1/8 remain?</p>
            <p>1/8 = (1/2)ⁿ, so n = 3</p>
            <p>Time = 3 × 10 = 30 days</p>
        </div>

        <h4>pH Scale (Logarithmic)</h4>
        <p><strong>pH = −log₁₀[H⁺]</strong> where [H⁺] is hydrogen ion concentration</p>

        <div class="example-box">
            <p><strong>Example 16:</strong> A substance has pH = 3. Find [H⁺]</p>
            <p>3 = −log₁₀[H⁺]</p>
            <p>−3 = log₁₀[H⁺]</p>
            <p>[H⁺] = 10⁻³ = 0.001 M</p>
        </div>

        <h4>Richter Scale (Logarithmic)</h4>
        <p><strong>M = log₁₀(A/A₀)</strong> where A is amplitude, A₀ is reference amplitude</p>

        <p>Each unit increase means 10× more amplitude.</p>

        <h4>Exponential Regression</h4>
        <p>If data appears to follow exponential pattern y = abˣ, take logs: ln(y) = ln(a) + x·ln(b). This becomes linear in x and ln(y), making it easy to fit.</p>
        """
    }
]
