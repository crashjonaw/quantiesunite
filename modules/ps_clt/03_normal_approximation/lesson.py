TITLE = "Normal Approximation"

SECTIONS = [
    {
        "title": "How Good is the Normal Approximation?",
        "body": """
        <p><strong>Practical question:</strong> For a finite sample size n, how close is the sampling distribution of X̄ to the normal distribution?</p>

        <p><strong>Berry-Esseen theorem:</strong> This theorem quantifies the rate of convergence. The maximum error is bounded by:</p>
        <pre class='code-block'>\(\sup_z |P(Z_n \\leq z) - \Phi(z)| \\leq C \\cdot \rho / \\sqrt{n}\)</pre>

        <p>where \(\rho = E[|X_1 - \\mu|^3] / \\sigma^3\) is the absolute third central moment (related to skewness), and \(C \\approx 0.7975\) is a universal constant.</p>

        <div class='concept-box'>
        <p><strong>What this means:</strong></p>
        <ul>
        <li>Error decreases as \(O(1/\\sqrt{n})\), so you need \(n \sim 4\) times larger to halve the error</li>
        <li>Symmetric distributions (\(\rho\) small) converge faster than skewed ones (\(\rho\) large)</li>
        <li>The error bound is universal—doesn't depend on the specific distribution shape</li>
        </ul>
        </div>

        <p><strong>Rule of thumb:</strong> For symmetric distributions, \(n \\geq 20\) is often adequate. For moderately skewed distributions, \(n \\geq 30\). For highly skewed data (e.g., Exponential, Pareto), \(n \\geq 50\) or more may be needed.</p>
        """
    },
    {
        "title": "Normal Approximation in Action: Examples",
        "body": """
        <div class='worked-example'>
        <p><strong>Example 1: Uniform distribution (symmetric)</strong></p>
        <pre class='code-block'>X₁, X₂, ..., X₁₀₀ ~ Uniform(0, 1) i.i.d.
\(\\mu = 0.5\), \(\\sigma^2 = 1/12 \\approx 0.0833\), \(\\sigma \\approx 0.289\)

E[X̄₁₀₀] = 0.5
SD(X̄₁₀₀) = 0.289 / √100 = 0.0289

By CLT: X̄₁₀₀ ≈ N(0.5, 0.0289²)

P(X̄₁₀₀ < 0.48) ≈ Φ((0.48 - 0.5) / 0.0289) = Φ(-0.692) ≈ 0.244</pre>
        <p><strong>Reality check:</strong> n = 100 is large and Uniform is symmetric, so normal approximation is excellent.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Exponential distribution (skewed)</strong></p>
        <pre class='code-block'>X₁, X₂, ..., Xₙ ~ Exponential(\(\\lambda = 1\)) i.i.d.
\(\\mu = 1\), \(\\sigma^2 = 1\), \(\\sigma = 1\)

For n = 50:
E[X̄₅₀] = 1
SD(X̄₅₀) = 1 / √50 ≈ 0.141

By CLT: X̄₅₀ ≈ N(1, 0.141²) approximately

P(0.9 < X̄₅₀ < 1.1) ≈ Φ((1.1 - 1) / 0.141) - Φ((0.9 - 1) / 0.141)
                    ≈ Φ(0.709) - Φ(-0.709) ≈ 0.761 - 0.239 = 0.522</pre>
        <p><strong>Reality check:</strong> Exponential is highly skewed. At n = 50, the approximation is reasonable but not perfect. n = 100 would be safer.</p>
        </div>

        <p><strong>Visually:</strong> Imagine a histogram of sample means. For small n, it may show slight asymmetry reflecting the skewness of the population. As n increases, the histogram becomes more bell-shaped and symmetrical, approaching the perfect normal curve.</p>
        """
    },
    {
        "title": "Normal Approximation for Binomial Distribution",
        "body": """
        <p><strong>Special case: Binomial(n, p)</strong> The number of successes X in n independent Bernoulli trials.</p>
        <pre class='code-block'>X ~ Binomial(n, p)
E[X] = np
Var(X) = np(1-p)
SD(X) = √(np(1-p))</pre>

        <p><strong>When is normal approximation good?</strong> The CLT applies to the sample mean p̂ = X/n, which has:</p>
        <pre class='code-block'>E[p̂] = p
Var(p̂) = p(1-p)/n
SD(p̂) = √(p(1-p)/n)</pre>

        <p><strong>Rule of thumb:</strong> Use normal approximation when both \(np \\geq 5\) and \(n(1-p) \\geq 5\).</p>

        <div class='worked-example'>
        <p><strong>Example 1: p = 0.5 (not too extreme)</strong></p>
        <pre class='code-block'>X ~ Binomial(100, 0.5)
\(np = 50\), \(n(1-p) = 50\) (both \(\\geq 5\) ✓)

Normal approximation: \(X \\approx N(50, 25)\), so SD = 5
\(P(X \\leq 45) \\approx \Phi((45.5 - 50) / 5) = \Phi(-0.9) \\approx 0.184\)
(Using continuity correction: \(P(X \\leq 45) = P(X < 45.5)\) for discrete \(X\))</pre>
        </div>

        <div class='warning-box'>
        <p><strong>Example 2: p = 0.1 (extreme)</strong></p>
        <pre class='code-block'>X ~ Binomial(10, 0.1)
np = 1, n(1-p) = 9 (np < 5 ✗)

Normal approximation is poor. Use exact binomial probabilities instead.</pre>
        </div>

        <p><strong>Continuity correction:</strong> Since binomial is discrete and normal is continuous, use \(P(X \\leq k) \\approx \Phi((k + 0.5 - np) / \\sqrt{np(1-p)})\) for better accuracy.</p>
        """
    }
]
