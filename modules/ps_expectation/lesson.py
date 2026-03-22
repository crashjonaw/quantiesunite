SECTIONS = [
    {
        "title": "Expectation (Mean) and its Properties",
        "body": """
        <p><strong>Expectation (Expected Value):</strong> The mean of a random variable X:</p>
        <pre class='code-block'>E[X] = Σₓ x·p(x)  for discrete X
E[X] = ∫ x·f(x) dx  for continuous X</pre>

        <p><strong>Interpretation:</strong> The "long-run average" if we repeat the random experiment many times.</p>

        <p><strong>Properties of expectation:</strong></p>
        <ul>
        <li><strong>Linearity:</strong> E[aX + b] = aE[X] + b</li>
        <li><strong>Superposition:</strong> E[X + Y] = E[X] + E[Y] (always true, even if dependent)</li>
        <li><strong>Independence:</strong> If X and Y independent, E[XY] = E[X]·E[Y]</li>
        <li><strong>Monotonicity:</strong> If X ≤ Y almost surely, then E[X] ≤ E[Y]</li>
        </ul>

        <p><strong>Examples of expectations:</strong></p>
        <ul>
        <li>E[X] for X ~ Bernoulli(p) is p</li>
        <li>E[X] for X ~ Binomial(n, p) is np</li>
        <li>E[X] for X ~ Poisson(λ) is λ</li>
        <li>E[X] for X ~ Uniform(a, b) is (a + b)/2</li>
        <li>E[X] for X ~ Normal(μ, σ²) is μ</li>
        <li>E[X] for X ~ Exponential(λ) is 1/λ</li>
        </ul>

        <p><strong>Law of the unconscious statistician:</strong> For Y = g(X):</p>
        <pre class='code-block'>E[Y] = E[g(X)] = Σₓ g(x)·p_X(x)  for discrete
E[Y] = ∫ g(x)·f_X(x) dx  for continuous</pre>

        <p>(No need to first find the distribution of Y!)</p>

        <div class='example-box'>
        <p><strong>Example: Expectation of discrete RV</strong></p>
        <pre class='code-block'>Fair die: X ∈ {1,2,3,4,5,6} with p(x) = 1/6
E[X] = 1·(1/6) + 2·(1/6) + ... + 6·(1/6) = (1+2+3+4+5+6)/6 = 21/6 = 3.5</pre>

        <p><strong>Example: Expectation of continuous RV</strong></p>
        <pre class='code-block'>X ~ Uniform(0, 1)
E[X] = ∫₀¹ x·1 dx = [x²/2]₀¹ = 1/2</pre>

        <p><strong>Example: E[X²] using LOTUS</strong></p>
        <pre class='code-block'>X ~ Uniform(0, 1), find E[X²]
E[X²] = ∫₀¹ x² · 1 dx = [x³/3]₀¹ = 1/3

(Later used to compute variance)</pre>
        </div>

        <p><strong>Conditional expectation:</strong> E[X|Y] is the expected value of X given Y:</p>
        <pre class='code-block'>E[X|Y=y] = Σₓ x·P(X=x|Y=y)  for discrete
E[X|Y=y] = ∫ x·f(x|y) dx  for continuous</pre>

        <p><strong>Law of iterated expectations:</strong></p>
        <pre class='code-block'>E[X] = E[E[X|Y]]</pre>
        """
    },
    {
        "title": "Variance, Standard Deviation, and Covariance",
        "body": """
        <p><strong>Variance:</strong> Measures the spread of a random variable around its mean:</p>
        <pre class='code-block'>Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²</pre>

        <p><strong>Standard Deviation:</strong></p>
        <pre class='code-block'>σ_X = SD(X) = √Var(X)</pre>

        <p><strong>Properties of variance:</strong></p>
        <ul>
        <li><strong>Shift invariance:</strong> Var(X + b) = Var(X)</li>
        <li><strong>Scaling:</strong> Var(aX) = a²Var(X)</li>
        <li><strong>Independence:</strong> If X and Y independent, Var(X + Y) = Var(X) + Var(Y)</li>
        <li><strong>General:</strong> Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)</li>
        </ul>

        <p><strong>Covariance:</strong> Measures joint variation of two variables:</p>
        <pre class='code-block'>Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]</pre>

        <p><strong>Properties:</strong></p>
        <ul>
        <li>Cov(X, X) = Var(X)</li>
        <li>Cov(X, Y) = Cov(Y, X)</li>
        <li>If X, Y independent, Cov(X, Y) = 0 (converse not always true)</li>
        <li>Cov(aX + b, cY + d) = ac·Cov(X, Y)</li>
        </ul>

        <p><strong>Correlation:</strong> Standardized measure of association:</p>
        <pre class='code-block'>ρ(X, Y) = Cov(X,Y) / (σ_X · σ_Y)</pre>

        <p>Always: -1 ≤ ρ ≤ 1. Measures linear relationship.</p>

        <div class='example-box'>
        <p><strong>Example: Variance of binomial</strong></p>
        <pre class='code-block'>X ~ Binomial(n, p)
E[X] = np  (computed from linearity and Bernoulli)
E[X²] = np + n(n-1)p²  (more complex)
Var(X) = E[X²] - (E[X])² = np + n(n-1)p² - (np)²
       = np - np² + n²p² - n²p² + np²
       = np(1 - p) = np(1 - p)  ✓</pre>

        <p><strong>Example: Variance of uniform</strong></p>
        <pre class='code-block'>X ~ Uniform(a, b), E[X] = (a+b)/2
E[X²] = ∫ₐᵇ x² / (b-a) dx = [(b³ - a³) / 3] / (b-a) = (a² + ab + b²) / 3
Var(X) = (a² + ab + b²) / 3 - [(a+b)/2]² = (b-a)² / 12</pre>
        </div>

        <p><strong>Chebyshev's Inequality:</strong> For any random variable X and ε > 0:</p>
        <pre class='code-block'>P(|X - E[X]| ≥ ε) ≤ Var(X) / ε²</pre>

        <p>Probability of being far from the mean is bounded by variance.</p>
        """
    },
    {
        "title": "Moment Generating Functions and Moments",
        "body": """
        <p><strong>Moments:</strong> The k-th moment of X is:</p>
        <pre class='code-block'>μ_k' = E[Xᵏ]</pre>

        <p><strong>Central Moments:</strong> The k-th central moment is:</p>
        <pre class='code-block'>μ_k = E[(X - E[X])ᵏ]</pre>

        <p>First two central moments: μ₁ = 0 (always), μ₂ = Var(X).</p>

        <p><strong>Moment Generating Function (MGF):</strong></p>
        <pre class='code-block'>M_X(t) = E[e^(tX)]</pre>

        <p><strong>Key property:</strong> If the MGF exists in a neighborhood of 0, then:</p>
        <pre class='code-block'>M_X^(k)(0) = E[Xᵏ]  (k-th derivative at 0)</pre>

        <p>The MGF uniquely determines the distribution.</p>

        <p><strong>MGF properties:</strong></p>
        <ul>
        <li>M_X(0) = 1</li>
        <li>If Y = aX + b, then M_Y(t) = e^(bt) M_X(at)</li>
        <li>If X and Y independent, M_{X+Y}(t) = M_X(t) · M_Y(t)</li>
        </ul>

        <p><strong>Common MGFs:</strong></p>
        <ul>
        <li>Bernoulli(p): M(t) = 1 - p + pe^t</li>
        <li>Poisson(λ): M(t) = e^(λ(e^t - 1))</li>
        <li>Normal(μ, σ²): M(t) = exp(μt + σ²t²/2)</li>
        <li>Exponential(λ): M(t) = λ/(λ - t) for t < λ</li>
        </ul>

        <p><strong>Skewness and Kurtosis:</strong></p>
        <ul>
        <li><strong>Skewness:</strong> γ₁ = μ₃/σ³ (measures asymmetry; 0 for symmetric)</li>
        <li><strong>Kurtosis:</strong> γ₂ = μ₄/σ⁴ - 3 (measures tail heaviness; 0 for normal)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: MGF of Poisson</strong></p>
        <pre class='code-block'>X ~ Poisson(λ)
M_X(t) = E[e^(tX)] = Σₖ₌₀^∞ e^(tk) · (e^(-λ)λᵏ)/k!
       = e^(-λ) Σₖ₌₀^∞ (λe^t)ᵏ/k!
       = e^(-λ) · e^(λe^t)
       = e^(λ(e^t - 1))

Find E[X]: M'(t) = λe^t · e^(λ(e^t - 1))
         M'(0) = λ · e^0 · e^0 = λ  ✓

Find Var(X): M''(t) = λe^t · e^(λ(e^t - 1)) + λ²e^(2t) · e^(λ(e^t - 1))
            M''(0) = λ + λ² = λ(1 + λ)
           Var(X) = M''(0) - [M'(0)]² = λ + λ² - λ² = λ  ✓</pre>
        </div>

        <p><strong>Why MGF is useful:</strong></p>
        <ul>
        <li>Computing moments algebraically (no integration)</li>
        <li>Proving limit theorems (Central Limit Theorem)</li>
        <li>Identifying distributions (unique correspondence)</li>
        <li>Handling sums of independent RVs (product of MGFs)</li>
        </ul>
        """
    }
]
