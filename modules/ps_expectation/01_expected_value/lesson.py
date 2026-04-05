TITLE = "Expected Value Definition and Interpretation"

SECTIONS = [
    {
        "title": "Definition of Expectation (Mean)",
        "body": """
        <p><strong>Expectation (Expected Value):</strong> The mean of a random variable $X$ is denoted $E[X]$ and represents the "average outcome" if an experiment is repeated infinitely many times.</p>

        <div class='concept-box'>
        <p><strong>For discrete random variables:</strong></p>
        <p>$$E[X] = \\sum_{x} x \\cdot P(X = x)$$</p>
        <p>where the sum is over all possible values of $X$, weighted by their probabilities.</p>
        </div>

        <div class='concept-box'>
        <p><strong>For continuous random variables:</strong></p>
        <p>$$E[X] = \\int_{-\\infty}^{\\infty} x \\cdot f(x)\\, dx$$</p>
        <p>where $f(x)$ is the probability density function.</p>
        </div>

        <p><strong>Intuitive interpretation:</strong> $E[X]$ is the "long-run average." If you repeat the random experiment many times and compute the sample mean, it approaches $E[X]$.</p>

        <div class='worked-example'>
        <p><strong>Example 1: Fair Die Roll</strong></p>
        <p>A fair 6-sided die shows each value 1, 2, 3, 4, 5, 6 with probability $1/6$.</p>
        <pre class='code-block'>$E[X] = 1 \\cdot (1/6) + 2 \\cdot (1/6) + 3 \\cdot (1/6) + 4 \\cdot (1/6) + 5 \\cdot (1/6) + 6 \\cdot (1/6)$
$= (1 + 2 + 3 + 4 + 5 + 6)/6$
$= 21/6$
$= 3.5$</pre>
        <p>On average, a fair die rolls 3.5. (Note: 3.5 is impossible on any single roll, but is the long-run average.)</p>
        </div>
        """
    },
    {
        "title": "Discrete vs. Continuous Expectations",
        "body": """
        <p>The calculation method differs based on the type of random variable, but the <strong>interpretation</strong> is identical: the long-run average.</p>

        <div class='worked-example'>
        <p><strong>Discrete Example: Coin Flips</strong></p>
        <p>Let $X$ = number of heads in 3 fair coin flips.</p>
        <p>$X$ can be 0, 1, 2, or 3 with probabilities $P(X=0)=1/8$, $P(X=1)=3/8$, $P(X=2)=3/8$, $P(X=3)=1/8$.</p>
        <pre class='code-block'>$E[X] = 0 \\cdot (1/8) + 1 \\cdot (3/8) + 2 \\cdot (3/8) + 3 \\cdot (1/8)$
$= 0 + 3/8 + 6/8 + 3/8$
$= 12/8$
$= 1.5$</pre>
        <p>Over many repetitions of "flip 3 coins," the average number of heads converges to 1.5.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Continuous Example: Uniform Distribution</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$, meaning $X$ is equally likely to be any value in $[0, 1]$.</p>
        <p>The PDF is $f(x) = 1$ for $x \\in [0, 1]$.</p>
        <pre class='code-block'>$E[X] = \\int_0^1 x \\cdot 1\\, dx$
$= [x^2/2]_0^1$
$= 1/2 - 0$
$= 0.5$</pre>
        <p>The "average" value of a uniform random variable on $[0, 1]$ is the midpoint, $0.5$.</p>
        </div>
        """
    },
    {
        "title": "Law of the Unconscious Statistician (LOTUS)",
        "body": """
        <p>Often we need $E[g(X)]$ for some function $g(\\cdot)$. We could find the distribution of $Y = g(X)$ and then compute $E[Y]$. But LOTUS gives us a shortcut:</p>

        <div class='concept-box'>
        <p><strong>Law of the Unconscious Statistician (LOTUS):</strong></p>
        <p>For a function $g$ and random variable $X$:</p>
        <pre class='code-block'>$E[g(X)] = \\sum_{x} g(x) \\cdot P(X = x)$ [discrete]
$E[g(X)] = \\int g(x) \\cdot f(x)\\, dx$ [continuous]</pre>
        <p>Use the <strong>original</strong> distribution of $X$; no need to find the distribution of $g(X)$.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: $E[X^2]$ for $\\text{Uniform}(0, 1)$</strong></p>
        <p>Let $X \\sim \\text{Uniform}(0, 1)$, and we want $E[X^2]$.</p>
        <p>By LOTUS, with $g(x) = x^2$:</p>
        <pre class='code-block'>$E[X^2] = \\int_0^1 x^2 \\cdot 1\\, dx$
$= [x^3/3]_0^1$
$= 1/3$</pre>
        <p>This will be used later to compute $\\text{Var}(X) = E[X^2] - (E[X])^2 = 1/3 - (1/2)^2 = 1/3 - 1/4 = 1/12$.</p>
        </div>

        <div class='success-box'>
        <p><strong>Why is LOTUS powerful?</strong></p>
        <ul>
        <li>Avoids having to derive the distribution of $Y = g(X)$</li>
        <li>Often the integral or sum is simpler than finding $f_Y(y)$</li>
        <li>Generalizes to any function $g$</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Conditional Expectation",
        "body": """
        <p>Sometimes we know the value (or partial information) of one random variable and want the expected value of another.</p>

        <div class='concept-box'>
        <p><strong>Conditional Expectation:</strong> The expected value of $X$ given that $Y = y$:</p>
        <pre class='code-block'>$E[X \\mid Y = y] = \\sum_{x} x \\cdot P(X = x \\mid Y = y)$ [discrete]
$E[X \\mid Y = y] = \\int x \\cdot f(x \\mid y)\\, dx$ [continuous]</pre>
        <p>Use the <strong>conditional</strong> distribution of $X$ given $Y = y$.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Law of Iterated Expectations (LIE):</strong></p>
        <p>$$E[X] = E[E[X \\mid Y]]$$</p>
        <p>This "law of total expectation" says: if you average the conditional expectations over all values of $Y$, you recover the unconditional expectation of $X$.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Two Fair Dice</strong></p>
        <p>Roll two fair dice. Let $X$ = first die, $Y$ = second die. Find $E[X \\mid Y = 3]$.</p>
        <pre class='code-block'>$E[X \\mid Y = 3] = 1 \\cdot (1/6) + 2 \\cdot (1/6) + \\cdots + 6 \\cdot (1/6)$
$= (1 + 2 + 3 + 4 + 5 + 6)/6$
$= 3.5$</pre>
        <p>Since the first die is independent of the second, knowing $Y = 3$ doesn't change the distribution of $X$. So $E[X \\mid Y = 3] = E[X] = 3.5$.</p>
        </div>
        """
    }
]
