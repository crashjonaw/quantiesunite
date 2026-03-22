SECTIONS = [
    {
        "title": "Maximum Likelihood Estimation (MLE)",
        "body": """
        <p><strong>Likelihood Function:</strong> Given data X₁, ..., Xₙ and parameter θ, the likelihood is the joint PDF/PMF viewed as a function of θ:</p>
        <pre class='code-block'>L(θ; X₁,...,Xₙ) = f(X₁,...,Xₙ | θ) = ∏ᵢ f(Xᵢ | θ)  (for independent data)</pre>

        <p><strong>Maximum Likelihood Estimator (MLE):</strong> The value of θ that maximizes the likelihood:</p>
        <pre class='code-block'>θ̂_MLE = arg max_θ L(θ; data)</pre>

        <p>Equivalently (often easier), maximize the log-likelihood:</p>
        <pre class='code-block'>ℓ(θ) = log L(θ), so θ̂_MLE satisfies dℓ/dθ = 0</pre>

        <p><strong>Properties of MLE:</strong></p>
        <ul>
        <li>Consistent: θ̂_MLE → θ₀ (true value) as n → ∞</li>
        <li>Asymptotically normal: θ̂_MLE ≈ N(θ₀, 1/(nI(θ₀))) for large n</li>
        <li>Efficient: achieves the Cramér-Rao lower bound asymptotically</li>
        <li>Invariant: if φ = g(θ), then φ̂_MLE = g(θ̂_MLE)</li>
        </ul>

        <p><strong>Fisher Information:</strong> I(θ) = -E[d²ℓ/dθ²] measures the curvature of the log-likelihood. Larger I means θ is estimated more precisely.</p>

        <div class='example-box'>
        <p><strong>Example: MLE for Bernoulli</strong></p>
        <pre class='code-block'>Data: X₁,...,Xₙ ~ Bernoulli(p), observed k successes
L(p) = p^k (1-p)^(n-k)
ℓ(p) = k log p + (n-k) log(1-p)
dℓ/dp = k/p - (n-k)/(1-p) = 0
Solving: k/p = (n-k)/(1-p), so p̂ = k/n

The MLE is the sample proportion.</pre>
        </div>

        <p><strong>Computational notes:</strong> For many distributions, closed-form MLEs exist. Numerical optimization is needed for complex likelihoods.</p>
        """
    },
    {
        "title": "Hypothesis Testing and p-values",
        "body": """
        <p><strong>Hypothesis Test Structure:</strong></p>
        <ul>
        <li><strong>H₀ (Null hypothesis):</strong> Usually a statement of "no effect" or "no difference"</li>
        <li><strong>H₁ (Alternative hypothesis):</strong> What we're looking for (could be one-sided or two-sided)</li>
        </ul>

        <p><strong>Test Statistic:</strong> A summary of the data (e.g., t = (X̄ - μ₀) / (S / √n)) that measures discrepancy from H₀.</p>

        <p><strong>p-value:</strong> The probability of observing a test statistic at least as extreme as the one observed, assuming H₀ is true:</p>
        <pre class='code-block'>p = P(Test statistic more extreme | H₀ true)</pre>

        <p><strong>Decision rule:</strong> Reject H₀ if p < α (significance level, typically 0.05).</p>

        <p><strong>Type I and Type II errors:</strong></p>
        <ul>
        <li><strong>Type I error (False positive):</strong> Reject H₀ when it's true. P(Type I) = α</li>
        <li><strong>Type II error (False negative):</strong> Fail to reject H₀ when it's false. P(Type II) = β</li>
        <li><strong>Power:</strong> 1 - β = P(reject H₀ | H₁ true)</li>
        </ul>

        <p><strong>Common tests:</strong></p>
        <ul>
        <li><strong>t-test:</strong> For testing mean with unknown σ</li>
        <li><strong>z-test:</strong> For testing mean with known σ or proportions with large n</li>
        <li><strong>χ² test:</strong> For goodness-of-fit and independence in contingency tables</li>
        <li><strong>F-test:</strong> For comparing variances or testing significance in regression</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: One-sample t-test</strong></p>
        <pre class='code-block'>H₀: μ = 100 (population mean)
H₁: μ ≠ 100 (two-sided)

Sample: n = 25, X̄ = 102, S = 8
t = (102 - 100) / (8 / √25) = 2 / 1.6 = 1.25

df = n - 1 = 24
p-value = P(|t| > 1.25 | H₀) from t(24) ≈ 0.22

At α = 0.05: p > α, so do not reject H₀ (insufficient evidence)</pre>
        </div>

        <p><strong>Misunderstanding p-values:</strong> p-value is NOT P(H₀ true | data). It's the tail probability under H₀. Multiple testing inflates false positives (use correction methods like Bonferroni).</p>
        """
    },
    {
        "title": "Confidence Intervals and Method of Moments",
        "body": """
        <p><strong>Method of Moments (MoM):</strong> Estimate population parameters by equating sample moments to population moments:</p>
        <pre class='code-block'>Sample moments: m_k = (1/n) Σᵢ Xᵢ^k
Population moments: μ_k' = E[Xᵏ]

Solve: m_k = μ_k' to get parameter estimates</pre>

        <p><strong>MLE vs. MoM:</strong> MLE is more efficient but sometimes harder to compute. MoM is simpler and often close to MLE.</p>

        <p><strong>Confidence Intervals (revisited):</strong></p>
        <ul>
        <li><strong>Pivotal quantity:</strong> A function of data and parameter whose distribution is known. Use it to construct CI.</li>
        <li><strong>Inversion method:</strong> Invert the test (e.g., find all θ not rejected by hypothesis test at level α)</li>
        </ul>

        <p><strong>Parametric vs. nonparametric:</strong> Parametric methods assume a specific distribution (faster, more powerful if assumption holds). Nonparametric methods make fewer assumptions (more robust).</p>

        <div class='example-box'>
        <p><strong>Example: MoM for exponential</strong></p>
        <pre class='code-block'>X₁,...,Xₙ ~ Exponential(λ)
E[X] = 1/λ (population moment)
X̄ = sample mean

By MoM: X̄ = 1/λ̂, so λ̂ = 1/X̄</pre>
        </div>

        <p><strong>Bayesian confidence intervals (credible intervals):</strong> Include the prior belief about parameters, offering alternative interpretation (section on Bayesian inference).</p>
        """
    },
    {
        "title": "Regression and Inference",
        "body": """
        <p><strong>Linear Regression:</strong> Model y = β₀ + β₁x + ε, where ε ~ N(0, σ²) are independent errors.</p>

        <p><strong>Ordinary Least Squares (OLS) Estimators:</strong></p>
        <pre class='code-block'>β̂₁ = Σ(Xᵢ - X̄)(Yᵢ - Ȳ) / Σ(Xᵢ - X̄)²
β̂₀ = Ȳ - β̂₁X̄</pre>

        <p><strong>Properties:</strong> Under regression assumptions (linearity, independence, homoscedasticity, normality of errors):</p>
        <ul>
        <li>β̂ are unbiased estimators of β</li>
        <li>β̂ are approximately normal for large n (by CLT)</li>
        <li>Residual standard error estimates σ</li>
        </ul>

        <p><strong>Inference for slopes:</strong> Test H₀: β₁ = 0 using t-test:</p>
        <pre class='code-block'>t = β̂₁ / SE(β̂₁), where SE(β̂₁) = σ̂ / √(Σ(Xᵢ - X̄)²)</pre>

        <p><strong>R² (coefficient of determination):</strong> Proportion of variance in y explained by x. Ranges [0, 1].</p>

        <p><strong>Model diagnostics:</strong> Check residuals for normality, constant variance, and independence via plots and tests.</p>

        <div class='example-box'>
        <p><strong>Example: Simple linear regression</strong></p>
        <pre class='code-block'>Data: (x, y) pairs, fit y = β₀ + β₁x
Test H₀: β₁ = 0 (no relationship)
If p-value < 0.05, conclude significant relationship

CI for β₁: β̂₁ ± t_{α/2,n-2} · SE(β̂₁)</pre>
        </div>

        <p><strong>Multiple regression:</strong> y = β₀ + β₁x₁ + ... + βₚxₚ + ε. Matrix formulation enables efficient computation and inference on multiple slopes simultaneously.</p>
        """
    }
]
