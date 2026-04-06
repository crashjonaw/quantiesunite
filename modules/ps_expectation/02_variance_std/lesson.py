TITLE = "Variance and Standard Deviation"

SECTIONS = [
    {
        "title": "Definition and Interpretation of Variance",
        "body": """
        <p><strong>Variance:</strong> A measure of the <em>spread</em> or <em>dispersion</em> of a random variable around its mean.</p>

        <div class='concept-box'>
        <p><strong>Definition:</strong></p>
        <pre class='code-block'>Var(X) = E[(X − E[X])²]</pre>
        <p>Variance is the expected value of the squared deviation from the mean.</p>
        </div>

        <p><strong>Intuition:</strong> Large deviations from the mean contribute quadratically (squared), so extreme values heavily penalize the variance.</p>

        <div class='concept-box'>
        <p><strong>Computational formula (often easier):</strong></p>
        <pre class='code-block'>Var(X) = E[X²] − (E[X])²</pre>
        <p>This formula requires computing \(E[X]\) and \(E[X^2]\) but avoids expanding \((X - \mu)^2\).</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 1: Fair Die Roll</strong></p>
        <p>For a fair 6-sided die, we already computed E[X] = 3.5. Now find Var(X).</p>
        <p>First, compute E[X²]:</p>
        <pre class='code-block'>E[X²] = 1²·(1/6) + 2²·(1/6) + 3²·(1/6) + 4²·(1/6) + 5²·(1/6) + 6²·(1/6)
      = (1 + 4 + 9 + 16 + 25 + 36)/6
      = 91/6</pre>
        <p>Then apply the formula:</p>
        <pre class='code-block'>Var(X) = E[X²] − (E[X])²
       = 91/6 − (3.5)²
       = 91/6 − 49/4
       = 182/12 − 147/12
       = 35/12
       ≈ 2.92</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Uniform(0, 1)</strong></p>
        <p>For X ~ Uniform(0, 1), we have E[X] = 1/2 and E[X²] = 1/3 (computed earlier).</p>
        <pre class='code-block'>Var(X) = 1/3 − (1/2)²
       = 1/3 − 1/4
       = 4/12 − 3/12
       = 1/12</pre>
        </div>
        """
    },
    {
        "title": "Standard Deviation",
        "body": """
        <p><strong>Standard Deviation:</strong> The square root of variance, often denoted \(\sigma\) or \(\text{SD}(X)\).</p>

        <div class='concept-box'>
        <p><strong>Definition:</strong></p>
        <pre class='code-block'>\(\sigma_X = \text{SD}(X) = \sqrt{\text{Var}(X)}\)</pre>
        </div>

        <p><strong>Why is standard deviation useful?</strong> While variance uses squared units (e.g., if X is in dollars, \(\text{Var}(X)\) is in dollars\(^2\)), standard deviation has the <strong>same units as X</strong>, making it more interpretable.</p>

        <div class='worked-example'>
        <p><strong>Example: Fair Die (continued)</strong></p>
        <p>From the previous example, Var(X) = 35/12 ≈ 2.92.</p>
        <pre class='code-block'>SD(X) = √(35/12)
      = √(2.917)
      ≈ 1.71</pre>
        <p>The outcomes of a fair die deviate from the mean 3.5 by about 1.71 on average (in a root-mean-square sense).</p>
        </div>

        <div class='success-box'>
        <p><strong>Empirical Rule (for normal distributions):</strong></p>
        <ul>
        <li>About 68% of observations fall within \(\mu \pm 1\sigma\)</li>
        <li>About 95% fall within \(\mu \pm 2\sigma\)</li>
        <li>About 99.7% fall within \(\mu \pm 3\sigma\)</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Properties of Variance",
        "body": """
        <p>Variance obeys several important algebraic properties. Mastering these makes computation much easier.</p>

        <div class='concept-box'>
        <p><strong>Shift Invariance:</strong> Adding a constant doesn't change variance.</p>
        <pre class='code-block'>Var(X + b) = Var(X)</pre>
        <p>Reason: Shifting all values by b shifts the mean by b, but the spread around the mean is unchanged.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Scaling Property:</strong> Scaling by a constant scales variance by its square.</p>
        <pre class='code-block'>Var(aX) = a² Var(X)</pre>
        <p>Reason: Multiplying all values by a multiplies deviations by a, and deviations are squared.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Combined (linear transformation):</strong></p>
        <pre class='code-block'>Var(aX + b) = a² Var(X)</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Temperature Conversion</strong></p>
        <p>Suppose measurements of a quantity X have Var(X) = 100 (in degrees Celsius).</p>
        <p>Convert to Fahrenheit: Y = (9/5)X + 32.</p>
        <pre class='code-block'>Var(Y) = (9/5)² Var(X)
       = (81/25) · 100
       = 324</pre>
        <p>The variance in Fahrenheit is 324, reflecting the conversion scale.</p>
        </div>

        <div class='concept-box'>
        <p><strong>For independent random variables:</strong></p>
        <pre class='code-block'>Var(X + Y) = Var(X) + Var(Y)  [if X, Y independent]</pre>
        <p>Independence is key: variances add. (More generally, Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y).)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Sum of Independent Variables</strong></p>
        <p>Roll two independent fair dice. Let X = first die, Y = second die, Z = X + Y.</p>
        <p>We know Var(X) = Var(Y) = 35/12.</p>
        <pre class='code-block'>Var(Z) = Var(X + Y)
       = Var(X) + Var(Y)  [independence]
       = 35/12 + 35/12
       = 70/12
       = 35/6
       ≈ 5.83</pre>
        </div>
        """
    },
    {
        "title": "Chebyshev's Inequality",
        "body": """
        <p>Chebyshev's inequality provides a universal bound on how far a random variable can deviate from its mean in terms of its variance.</p>

        <div class='concept-box'>
        <p><strong>Chebyshev's Inequality:</strong> For any random variable X and any ε > 0:</p>
        <pre class='code-block'>\(P(|X - E[X]| \geq \varepsilon) \leq \text{Var}(X) / \varepsilon^2\)</pre>
        <p>The probability of being at least ε away from the mean is bounded by variance divided by ε².</p>
        </div>

        <p><strong>Intuition:</strong> If variance is small, large deviations are unlikely. The bound gets tighter as variance decreases.</p>

        <div class='worked-example'>
        <p><strong>Example: Fair Die</strong></p>
        <p>For a fair die, \(E[X] = 3.5\) and \(\text{Var}(X) = 35/12 \approx 2.92\). Find \(P(|X - 3.5| \geq 2)\).</p>
        <p>By Chebyshev with \(\varepsilon = 2\):</p>
        <pre class='code-block'>\(P(|X - 3.5| \geq 2) \leq (35/12) / 4\)
                  = 35/48
                  ≈ 0.729</pre>
        <p>So the probability is at most 72.9%. (The actual probability is lower; Chebyshev gives a <strong>worst-case bound</strong>.)</p>
        </div>

        <div class='warning-box'>
        <p><strong>Note on Chebyshev:</strong> The bound is often loose and valid for all distributions. For specific distributions (e.g., normal), tighter bounds exist.</p>
        </div>
        """
    }
]
