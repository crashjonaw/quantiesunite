TITLE = "Applications and Modeling"

SECTIONS = [
    {
        "title": "Compound Interest and Continuous Growth",
        "body": """
        <h3>Money and Growth Models</h3>

        <h4>Compound Interest (Discrete)</h4>
        <p style="text-align: center;"><strong>A = P(1 + r/n)^(nt)</strong></p>
        <ul>
            <li>A = final amount</li>
            <li>P = principal (initial amount)</li>
            <li>r = annual interest rate (as decimal)</li>
            <li>n = compounding periods per year</li>
            <li>t = time in years</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 1:</strong> $5000 invested at 6% annual interest, compounded monthly. Find amount after 5 years.</p>
            <p>P = 5000, r = 0.06, n = 12, t = 5</p>
            <p>A = 5000(1 + 0.06/12)^(60) = 5000(1.005)^60</p>
            <p>A ≈ 5000 × 1.349 ≈ <strong>$6745</strong></p>
        </div>

        <h4>Continuous Compounding</h4>
        <p style="text-align: center;"><strong>A = Pe^(rt)</strong></p>
        <p>Used when interest is compounded continuously or growth is truly continuous.</p>

        <div class="worked-example">
            <p><strong>Example 2:</strong> A population grows continuously at 5% per year. Starting with 1000, find population after 10 years.</p>
            <p>k = 0.05 (5% = 0.05), t = 10, A₀ = 1000</p>
            <p>A(10) = 1000 · e^(0.05×10) = 1000 · e^0.5</p>
            <p>A(10) ≈ 1000 · 1.649 ≈ <strong>1649</strong></p>
        </div>

        <div class="worked-example">
            <p><strong>Example 3:</strong> How long until $5000 doubles at 3% continuous interest?</p>
            <p>10000 = 5000e^(0.03t)</p>
            <p>2 = e^(0.03t)</p>
            <p>ln(2) = 0.03t</p>
            <p>t = ln(2)/0.03 ≈ 0.693/0.03 ≈ <strong>23.1 years</strong></p>
        </div>
        """
    },
    {
        "title": "Radioactive Decay and Half-Life",
        "body": """
        <h3>Decay Processes</h3>

        <h4>Half-Life Model</h4>
        <p style="text-align: center;"><strong>A(t) = A₀(1/2)^(t/T)</strong></p>
        <ul>
            <li>A(t) = amount remaining after time t</li>
            <li>A₀ = initial amount</li>
            <li>T = half-life (time for amount to halve)</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 4:</strong> A radioactive isotope has a half-life of 10 days. After how long will 1/8 remain?</p>
            <p>1/8 = (1/2)ⁿ, so n = 3 half-lives</p>
            <p>Time = 3 × 10 = <strong>30 days</strong></p>
        </div>

        <h4>Carbon-14 Dating</h4>
        <p>Carbon-14 has a half-life of 5730 years. Used to date organic materials.</p>

        <div class="worked-example">
            <p><strong>Example 5:</strong> A fossil has 12% of original C-14. Estimate its age.</p>
            <p>0.12 = (0.5)^(t/5730)</p>
            <p>Take natural log: ln(0.12) = (t/5730)ln(0.5)</p>
            <p>t = 5730 × ln(0.12)/ln(0.5)</p>
            <p>t = 5730 × (-2.120)/(-0.693) ≈ 5730 × 3.06</p>
            <p>t ≈ <strong>17,528 years</strong></p>
        </div>
        """
    },
    {
        "title": "Logarithmic Scales in Real Life",
        "body": """
        <h3>pH, Richter, and Decibels</h3>

        <h4>pH Scale (Chemistry)</h4>
        <p style="text-align: center;"><strong>pH = −log₁₀[H⁺]</strong></p>
        <p>where [H⁺] is hydrogen ion concentration in moles per liter</p>
        <ul>
            <li>pH < 7 is acidic</li>
            <li>pH = 7 is neutral</li>
            <li>pH > 7 is basic</li>
            <li>Each unit change = 10× change in concentration</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example 6:</strong> A substance has pH = 3. Find [H⁺]</p>
            <p>3 = −log₁₀[H⁺]</p>
            <p>−3 = log₁₀[H⁺]</p>
            <p>[H⁺] = 10⁻³ = <strong>0.001 M</strong></p>
        </div>

        <h4>Richter Scale (Seismology)</h4>
        <p style="text-align: center;"><strong>M = log₁₀(A/A₀)</strong></p>
        <p>where A is amplitude and A₀ is reference amplitude</p>
        <ul>
            <li>Each unit increase = 10× more amplitude</li>
            <li>Energy release increases by factor of ~31.6 per unit</li>
        </ul>

        <div class="concept-box">
            <p><strong>Why logarithmic scales?</strong> Natural phenomena span enormous ranges. A log scale compresses this so we can compare values effectively. A magnitude 8 earthquake is only 1 unit higher than magnitude 7, but releases ~32 times more energy.</p>
        </div>
        """
    },
    {
        "title": "Exponential Regression and Data Fitting",
        "body": """
        <h3>Finding Exponential Models from Data</h3>

        <h4>The Strategy: Linearization</h4>
        <p>If data appears to follow y = abˣ, take natural logarithms of both sides:</p>
        <p style="text-align: center;">ln(y) = ln(a) + x·ln(b)</p>
        <p>This becomes linear in x and ln(y), making it easy to fit with linear regression.</p>

        <h4>Process</h4>
        <ol>
            <li>Take natural log of all y-values to get ln(y)</li>
            <li>Plot ln(y) vs x (should be approximately linear)</li>
            <li>Use linear regression to find ln(a) and ln(b)</li>
            <li>Take exponentials to recover a and b</li>
        </ol>

        <div class="worked-example">
            <p><strong>Example 7:</strong> Suppose data shows exponential growth. A few points are:</p>
            <ul>
                <li>x = 0, y = 100 (so ln(y) = 4.605)</li>
                <li>x = 1, y ≈ 150 (so ln(y) ≈ 5.011)</li>
                <li>x = 2, y ≈ 225 (so ln(y) ≈ 5.416)</li>
            </ul>
            <p>The ln(y) values are approximately linear with slope ≈ 0.406</p>
            <p>So ln(b) ≈ 0.406, thus b ≈ e^0.406 ≈ 1.5</p>
            <p>Model: y ≈ 100(1.5)ˣ</p>
        </div>

        <div class="success-box">
            <p><strong>Power of Logarithms:</strong> By taking logarithms, we transform exponential relationships into linear ones, allowing us to use familiar linear tools on exponential data.</p>
        </div>
        """
    }
]
