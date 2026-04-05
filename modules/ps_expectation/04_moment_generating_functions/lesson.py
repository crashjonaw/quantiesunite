TITLE = "Moment Generating Functions"

SECTIONS = [
    {
        "title": "Definition of MGF and Moments",
        "body": """
        <p>The <strong>$k$-th moment</strong> of a random variable is the expected value of $X^k$:</p>

        <div class='concept-box'>
        <p><strong>$k$-th raw moment:</strong></p>
        <p>$$\\mu_k' = E[X^k]$$</p>
        <p><strong>$k$-th central moment:</strong> (around the mean)</p>
        <p>$$\\mu_k = E[(X - E[X])^k]$$</p>
        </div>

        <p><strong>Examples:</strong></p>
        <ul>
        <li>$\\mu_1' = E[X]$ (the mean)</li>
        <li>$\\mu_2' = E[X^2]$</li>
        <li>$\\mu_2 = E[(X - E[X])^2] = \\text{Var}(X)$ (variance)</li>
        <li>$\\mu_3 = E[(X - E[X])^3]$ (related to skewness)</li>
        <li>$\\mu_4 = E[(X - E[X])^4]$ (related to kurtosis)</li>
        </ul>

        <p>Computing moments directly can require integration or summation. The <strong>Moment Generating Function (MGF)</strong> provides an elegant shortcut.</p>

        <div class='concept-box'>
        <p><strong>Moment Generating Function (MGF):</strong></p>
        <p>$$M_X(t) = E[e^{tX}]$$</p>
        <p>where $t$ is a parameter. The MGF "generates" moments via differentiation.</p>
        </div>
        """
    },
    {
        "title": "Recovering Moments from MGF",
        "body": """
        <p>The key property of the MGF is that derivatives at $t = 0$ give moments.</p>

        <div class='concept-box'>
        <p><strong>Moment Recovery Property:</strong> If the MGF exists in a neighborhood of 0:</p>
        <p>$$M_X^{(k)}(0) = E[X^k]$$</p>
        <p>The $k$-th derivative of $M_X(t)$ evaluated at $t = 0$ equals the $k$-th moment.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: MGF of Exponential Distribution</strong></p>
        <p>Let $X \\sim \\text{Exponential}(\\lambda)$ with PDF $f(x) = \\lambda e^{-\\lambda x}$ for $x \\geq 0$.</p>
        <p>Compute the MGF:</p>
        <pre class='code-block'>$M_X(t) = E[e^{tX}]$
$= \\int_0^{\\infty} e^{tx} \\cdot \\lambda e^{-\\lambda x}\\, dx$
$= \\lambda \\int_0^{\\infty} e^{(t-\\lambda)x}\\, dx$
$= \\lambda \\cdot \\frac{1}{\\lambda - t}$ [for $t < \\lambda$]
$= \\frac{\\lambda}{\\lambda - t}$</pre>
        <p>Now recover $E[X]$ and $\\text{Var}(X)$:</p>
        <pre class='code-block'>$M'(t) = \\frac{d}{dt}\\left[\\frac{\\lambda}{\\lambda-t}\\right] = \\frac{\\lambda}{(\\lambda-t)^2}$

$M'(0) = \\frac{\\lambda}{\\lambda^2} = \\frac{1}{\\lambda} = E[X]$ ✓

$M''(t) = \\frac{2\\lambda}{(\\lambda-t)^3}$

$M''(0) = \\frac{2\\lambda}{\\lambda^3} = \\frac{2}{\\lambda^2}$

$E[X^2] = \\frac{2}{\\lambda^2}$

$\\text{Var}(X) = E[X^2] - (E[X])^2 = \\frac{2}{\\lambda^2} - \\frac{1}{\\lambda^2} = \\frac{1}{\\lambda^2}$</pre>
        </div>

        <div class='success-box'>
        <p><strong>Advantage:</strong> Once you have the MGF, computing all moments is algebraic (differentiation), not integration or summation.</p>
        </div>
        """
    },
    {
        "title": "Properties and Common MGFs",
        "body": """
        <p>The MGF has useful properties for manipulating random variables and identifying distributions.</p>

        <div class='concept-box'>
        <p><strong>MGF at zero:</strong></p>
        <p>$$M_X(0) = E[e^0] = 1$$</p>
        </div>

        <div class='concept-box'>
        <p><strong>Linear transformation:</strong> If $Y = aX + b$:</p>
        <pre class='code-block'>$M_Y(t) = E[e^{t(aX+b)}]$
$= e^{bt} E[e^{atX}]$
$= e^{bt} M_X(at)$</pre>
        </div>

        <div class='concept-box'>
        <p><strong>Independence:</strong> If $X$ and $Y$ are independent:</p>
        <p>$$M_{X+Y}(t) = M_X(t) \\cdot M_Y(t)$$</p>
        <p>The MGF of a sum is the product of MGFs (for independent variables).</p>
        </div>

        <div class='concept-box'>
        <p><strong>Common MGFs:</strong></p>
        <pre class='code-block'>$\\text{Bernoulli}(p)$:        $M(t) = 1 - p + pe^t$

$\\text{Binomial}(n, p)$:      $M(t) = (1 - p + pe^t)^n$

$\\text{Poisson}(\\lambda)$:          $M(t) = e^{\\lambda(e^t - 1)}$

$N(\\mu, \\sigma^2)$:       $M(t) = \\exp(\\mu t + \\sigma^2 t^2/2)$

$\\text{Exponential}(\\lambda)$:      $M(t) = \\frac{\\lambda}{\\lambda - t}$ [$t < \\lambda$]

$\\text{Uniform}(a, b)$:       $M(t) = \\frac{e^{bt} - e^{at}}{t(b - a)}$ [$t \\neq 0$]</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Binomial from Bernoullis</strong></p>
        <p>If $X \\sim \\text{Binomial}(n, p)$, then $X = B_1 + B_2 + \\cdots + B_n$ where $B_i$ are independent $\\text{Bernoulli}(p)$.</p>
        <p>Each Bernoulli has MGF: $M_{B_i}(t) = 1 - p + pe^t$.</p>
        <p>By independence:</p>
        <pre class='code-block'>$M_X(t) = M_{B_1}(t) \\cdot M_{B_2}(t) \\cdot \\ldots \\cdot M_{B_n}(t)$
$= [1 - p + pe^t]^n$</pre>
        <p>This matches the $\\text{Binomial}(n, p)$ MGF.</p>
        </div>
        """
    },
    {
        "title": "MGF Uniqueness and Applications",
        "body": """
        <p>The MGF has a powerful uniqueness property and is used throughout probability and statistics.</p>

        <div class='concept-box'>
        <p><strong>Uniqueness Theorem:</strong> The MGF uniquely determines the probability distribution. If two random variables have the same MGF, they have the same distribution.</p>
        </div>

        <p><strong>Application:</strong> This is the foundation for proving limit theorems like the Central Limit Theorem. By showing that MGFs converge, we prove that distributions converge.</p>

        <div class='worked-example'>
        <p><strong>Example: Identifying a Distribution</strong></p>
        <p>Suppose $X$ and $Y$ are independent, $X \\sim \\text{Poisson}(\\lambda_1)$ and $Y \\sim \\text{Poisson}(\\lambda_2)$.</p>
        <p>Find the distribution of $Z = X + Y$.</p>
        <pre class='code-block'>$M_Z(t) = M_X(t) \\cdot M_Y(t)$
$= e^{\\lambda_1(e^t - 1)} \\cdot e^{\\lambda_2(e^t - 1)}$
$= e^{(\\lambda_1 + \\lambda_2)(e^t - 1)}$</pre>
        <p>This is the MGF of $\\text{Poisson}(\\lambda_1 + \\lambda_2)$! So $Z \\sim \\text{Poisson}(\\lambda_1 + \\lambda_2)$.</p>
        <p>By uniqueness, we've identified the distribution without computing probabilities directly.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Skewness and Kurtosis (higher moments):</strong></p>
        <p>Once you have moments $E[X^k]$, you can compute:</p>
        <pre class='code-block'>Skewness: $\\gamma_1 = \\frac{\\mu_3}{\\sigma^3} = \\frac{E[(X - \\mu)^3]}{\\sigma^3}$
   (measures asymmetry; 0 for symmetric distributions)

Kurtosis: $\\gamma_2 = \\frac{\\mu_4}{\\sigma^4} - 3 = \\frac{E[(X - \\mu)^4]}{\\sigma^4} - 3$
   (measures tail heaviness; 0 for normal distribution)</pre>
        </div>

        <div class='warning-box'>
        <p><strong>Note on MGF existence:</strong> Not all distributions have an MGF. The standard Cauchy distribution, for instance, has no finite MGF. Characteristic functions (using $e^{itX}$ instead) always exist.</p>
        </div>
        """
    }
]
