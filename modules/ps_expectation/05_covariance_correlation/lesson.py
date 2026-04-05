TITLE = "Covariance and Correlation"

SECTIONS = [
    {
        "title": "Definition of Covariance",
        "body": """
        <p>Covariance measures how two random variables vary <strong>together</strong>. While variance measures spread of a single variable, covariance measures their joint variation.</p>

        <div class='concept-box'>
        <p><strong>Covariance:</strong></p>
        <p>$$\\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$$</p>
        <p>This is the expected value of the product of deviations from their respective means.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Computational formula:</strong></p>
        <p>$$\\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$</p>
        <p>Often easier to compute: find $E[XY]$, $E[X]$, and $E[Y]$, then subtract.</p>
        </div>

        <p><strong>Interpretation:</strong></p>
        <ul>
        <li><strong>Positive covariance:</strong> $X$ and $Y$ tend to move together (both above/below mean simultaneously).</li>
        <li><strong>Negative covariance:</strong> $X$ and $Y$ tend to move oppositely.</li>
        <li><strong>Zero covariance:</strong> No linear trend.</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example 1: Dependent Variables</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$ and $Y = 2X + 1$.</p>
        <p>We have $E[X] = 0.5$, $E[Y] = 2(0.5) + 1 = 2$.</p>
        <p>Compute $\\text{Cov}(X, Y)$:</p>
        <pre class='code-block'>$E[XY] = E[X(2X + 1)]$
$= E[2X^2 + X]$
$= 2E[X^2] + E[X]$
$= 2(1/3) + 0.5$
$= 2/3 + 1/2$
$= 7/6$

$\\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$
$= 7/6 - (0.5)(2)$
$= 7/6 - 1$
$= 1/6$
$\\approx 0.167$</pre>
        <p>Positive covariance: $Y$ increases as $X$ increases, as expected.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Independent Variables</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$ and $Y \\sim \\text{Uniform}(0, 1)$ independently.</p>
        <p>$E[X] = 0.5$, $E[Y] = 0.5$, and by independence, $E[XY] = E[X]E[Y] = 0.25$.</p>
        <pre class='code-block'>$\\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$
$= 0.25 - (0.5)(0.5)$
$= 0.25 - 0.25$
$= 0$</pre>
        <p>Zero covariance for independent variables, as expected.</p>
        </div>
        """
    },
    {
        "title": "Properties of Covariance",
        "body": """
        <p>Covariance obeys several algebraic properties that make computation and analysis easier.</p>

        <div class='concept-box'>
        <p><strong>Covariance with itself:</strong></p>
        <p>$$\\text{Cov}(X, X) = \\text{Var}(X)$$</p>
        </div>

        <div class='concept-box'>
        <p><strong>Symmetry:</strong></p>
        <p>$$\\text{Cov}(X, Y) = \\text{Cov}(Y, X)$$</p>
        </div>

        <div class='concept-box'>
        <p><strong>Linear transformation:</strong></p>
        <p>$$\\text{Cov}(aX + b, cY + d) = ac \\cdot \\text{Cov}(X, Y)$$</p>
        <p>Constants ($b$, $d$) don't affect covariance; scaling factors multiply.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Bilinearity:</strong></p>
        <p>$$\\text{Cov}(X + Y, Z) = \\text{Cov}(X, Z) + \\text{Cov}(Y, Z)$$</p>
        </div>

        <div class='concept-box'>
        <p><strong>Independence implies zero covariance:</strong></p>
        <p>If $X \\perp Y$ (independent), then $\\text{Cov}(X, Y) = 0$.</p>
        <p><strong>BUT the converse is false:</strong> $\\text{Cov}(X, Y) = 0$ does not imply independence.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Counterexample to Converse</strong></p>
        <p>Let $X \\sim N(0, 1)$ and $Y = X^2$. Then $Y$ is determined by $X$ (highly dependent).</p>
        <p>But: $E[X] = 0$, $E[XY] = E[X^3] = 0$ (odd moment of symmetric distribution).</p>
        <pre class='code-block'>$\\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$
$= 0 - 0 \\cdot E[X^2]$
$= 0$</pre>
        <p>Covariance is zero, yet $X$ and $Y$ are perfectly dependent! The issue: they're nonlinearly related.</p>
        </div>
        """
    },
    {
        "title": "Variance of Sums (using covariance)",
        "body": """
        <p>Covariance appears naturally when computing the variance of sums of random variables.</p>

        <div class='concept-box'>
        <p><strong>Variance of a sum:</strong></p>
        <p>$$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y) + 2\\text{Cov}(X, Y)$$</p>
        <p>Special case (independence): $\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y)$.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 1: Independent Variables</strong></p>
        <p>Roll two dice independently. $X$ = first die, $Y$ = second die.</p>
        <p>$\\text{Var}(X) = \\text{Var}(Y) = 35/12$, and $\\text{Cov}(X, Y) = 0$ (independence).</p>
        <pre class='code-block'>$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y) + 2 \\cdot 0$
$= 35/12 + 35/12$
$= 70/12$
$= 35/6$
$\\approx 5.83$</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Dependent Variables</strong></p>
        <p>From earlier: $X \\sim \\text{Uniform}(0, 1)$ and $Y = 2X + 1$, with $\\text{Cov}(X, Y) = 1/6$.</p>
        <p>$\\text{Var}(X) = 1/12$, $\\text{Var}(Y) = \\text{Var}(2X + 1) = 4\\text{Var}(X) = 4(1/12) = 1/3$.</p>
        <pre class='code-block'>$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y) + 2\\text{Cov}(X, Y)$
$= 1/12 + 1/3 + 2(1/6)$
$= 1/12 + 4/12 + 4/12$
$= 9/12$
$= 3/4$</pre>
        </div>

        <div class='concept-box'>
        <p><strong>Generalization:</strong> For random variables $X_1, \\ldots, X_n$:</p>
        <p>$$\\text{Var}(X_1 + \\cdots + X_n) = \\sum_i \\text{Var}(X_i) + 2 \\sum_{i < j} \\text{Cov}(X_i, X_j)$$</p>
        </div>
        """
    },
    {
        "title": "Correlation Coefficient",
        "body": """
        <p>Covariance's magnitude depends on the units of $X$ and $Y$, making cross-variable comparisons difficult. Correlation standardizes this.</p>

        <div class='concept-box'>
        <p><strong>Correlation Coefficient (Pearson):</strong></p>
        <p>$$\\rho(X, Y) = \\frac{\\text{Cov}(X, Y)}{\\sigma_X \\cdot \\sigma_Y}$$</p>
        <p>where $\\sigma_X = \\sqrt{\\text{Var}(X)}$ and $\\sigma_Y = \\sqrt{\\text{Var}(Y)}$.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Key property:</strong></p>
        <p>$$-1 \\leq \\rho(X, Y) \\leq 1$$</p>
        <p>A dimensionless measure of linear association.</p>
        </div>

        <p><strong>Interpretation:</strong></p>
        <ul>
        <li>$\\rho = 1$: Perfect positive linear relationship ($Y = aX + b$, $a > 0$)</li>
        <li>$\\rho = -1$: Perfect negative linear relationship ($Y = aX + b$, $a < 0$)</li>
        <li>$\\rho = 0$: No linear relationship</li>
        <li>$|\\rho|$ close to 1: Strong linear relationship</li>
        <li>$|\\rho|$ close to 0: Weak linear relationship</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example 1: Linear Relationship</strong></p>
        <p>$X \\sim \\text{Uniform}(0, 1)$, $Y = 2X + 1$.</p>
        <p>From earlier: $\\text{Cov}(X, Y) = 1/6$, $\\text{Var}(X) = 1/12$, $\\text{Var}(Y) = 1/3$.</p>
        <pre class='code-block'>$\\sigma_X = \\sqrt{1/12} = \\frac{1}{2\\sqrt{3}}$
$\\sigma_Y = \\sqrt{1/3} = \\frac{1}{\\sqrt{3}}$

$\\rho = \\frac{1/6}{(1/(2\\sqrt{3})) \\cdot (1/\\sqrt{3})}$
$= \\frac{1/6}{1/(2 \\cdot 3)}$
$= \\frac{1/6}{1/6}$
$= 1$</pre>
        <p>Perfect positive correlation, as expected ($Y$ is a linear function of $X$).</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: From Covariance Calculation</strong></p>
        <p>$\\text{Cov}(X, Y) = 0.5$, $\\sigma_X = 2$, $\\sigma_Y = 3$.</p>
        <pre class='code-block'>$\\rho = \\frac{0.5}{2 \\cdot 3}$
$= \\frac{0.5}{6}$
$\\approx 0.083$</pre>
        <p>Weak positive correlation.</p>
        </div>

        <div class='warning-box'>
        <p><strong>Correlation $\\neq$ Causation!</strong> A high correlation does not imply that one variable causes the other. Confounding factors, reverse causation, or pure coincidence can produce high correlations.</p>
        </div>
        """
    }
]
