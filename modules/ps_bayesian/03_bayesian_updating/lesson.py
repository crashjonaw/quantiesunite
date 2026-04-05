TITLE = "Bayesian Updating and Posterior Inference"

SECTIONS = [
    {
        "title": "Sequential Updating: Learning as Data Arrives",
        "body": """
        <p><strong>One strength of Bayesian inference:</strong> Naturally incorporates new data sequentially. Today's posterior becomes tomorrow's prior.</p>

        <p><strong>Sequential updating formula:</strong></p>

        <pre class='code-block'>Step 1: Prior $p(\\theta)$
        $\\downarrow$ [observe $y_1$]
Step 2: Posterior $p(\\theta|y_1) \\propto p(y_1|\\theta)\\, p(\\theta)$
        $\\downarrow$ [observe $y_2$]
Step 3: Posterior $p(\\theta|y_1, y_2) \\propto p(y_2|\\theta)\\, p(\\theta|y_1)$</pre>

        <p>Notice: The posterior from step 2 becomes the prior for step 3. No information is lost; each new observation refines our belief incrementally.</p>

        <div class='worked-example'>
        <p><strong>Example: Estimating a Coin's Bias</strong></p>
        <p>Prior: $\\text{Beta}(1, 1)$ (uniform)</p>

        <p><strong>Day 1:</strong> Flip 5 times, get 3 heads</p>
        <pre class='code-block'>$\\text{Posterior}_1 = \\text{Beta}(1+3, 1+2) = \\text{Beta}(4, 3)$
Mean: $4/7 \\approx 0.571$</pre>

        <p><strong>Day 2:</strong> Flip 5 more times, get 2 heads (out of 5, total 5 heads in 10 trials)</p>
        <pre class='code-block'>$\\text{Posterior}_2 = \\text{Beta}(4+2, 3+3) = \\text{Beta}(6, 6)$
Mean: $6/12 = 0.5$</pre>

        <p>Each day, we incorporate new evidence. No need to reprocess all old data; the posterior summary from day 1 encodes all information from that day.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Key advantage:</strong> Bayesian updating is efficient and transparent. Each observation updates your belief proportionally.</p>
        </div>
        """
    },
    {
        "title": "Extracting Information from the Posterior",
        "body": """
        <p><strong>Once we have the posterior $p(\\theta|y)$, we can answer many questions:</strong></p>

        <p><strong>1. Point Estimation:</strong> Single best guess for $\\theta$</p>
        <ul>
        <li><strong>Posterior mean:</strong> $E[\\theta|y] = \\int \\theta\\, p(\\theta|y)\\, d\\theta$</li>
        <li><strong>Posterior median:</strong> Robust to outliers</li>
        <li><strong>Posterior mode:</strong> Most likely value (MAP: Maximum A Posteriori)</li>
        </ul>

        <p><strong>2. Credible Intervals:</strong> Range of plausible values for $\\theta$</p>

        <p>95% credible interval $[a, b]$: $P(a < \\theta < b \\mid y) = 0.95$</p>

        <p>Direct probability statement about $\\theta$, given the observed data. Different from frequentist confidence intervals (which are about repeated sampling).</p>

        <p><strong>3. Probability Statements:</strong> Direct answers to questions like "What is $P(\\theta > 0 \\mid y)$?"</p>

        <p>$$P(\\theta > 0 \\mid y) = \\int_0^{\\infty} p(\\theta|y)\\, d\\theta$$</p>

        <p>This is one of the great advantages of Bayesian inference: posteriors directly answer the scientist's question.</p>

        <div class='warning-box'>
        <p><strong>Frequentist confidence interval vs. Bayesian credible interval:</strong></p>
        <ul>
        <li><strong>CI:</strong> $P(\\text{interval covers true } \\theta) = 95\\%$ over repeated sampling ($\\theta$ is fixed)</li>
        <li><strong>Credible interval:</strong> $P(\\theta \\text{ is in interval} \\mid \\text{data}) = 95\\%$ ($\\theta$ is random)</li>
        </ul>
        <p>Bayesian intervals have the intuitive interpretation most people expect; frequentist CIs require careful language.</p>
        </div>
        """
    },
    {
        "title": "Posterior Predictive Distribution",
        "body": """
        <p><strong>Problem:</strong> We estimate $\\theta$, but ultimately we care about predicting future observations.</p>

        <p><strong>Solution:</strong> The posterior predictive distribution averages over posterior uncertainty in $\\theta$:</p>

        <p>$$p(y_{\\text{new}} \\mid y) = \\int p(y_{\\text{new}} \\mid \\theta)\\, p(\\theta \\mid y)\\, d\\theta$$</p>

        <p><strong>Interpretation:</strong> Probability of new data $y_{\\text{new}}$, accounting for:
        <ul>
        <li>Uncertainty in $\\theta$ (via posterior $p(\\theta|y)$)</li>
        <li>Random variation in new observations (via likelihood $p(y_{\\text{new}}|\\theta)$)</li>
        </ul>

        <p><strong>Why not just use the posterior mean?</strong> Using $p(y_{\\text{new}} \\mid E[\\theta|y])$ ignores posterior uncertainty. The posterior predictive is wider and more honest about our forecasting uncertainty.</p>

        <div class='worked-example'>
        <p><strong>Example: Predicting Tomorrow's Coin Flips</strong></p>
        <p>After 10 flips (5 heads), posterior: $\\text{Beta}(6, 6)$, mean $0.5$</p>

        <p>Posterior predictive for 1 new flip:</p>
        <pre class='code-block'>$p(y_{\\text{new}} = 1 \\mid y) = \\int p(y_{\\text{new}}=1|\\theta)\\, p(\\theta|y)\\, d\\theta$
$= \\int \\theta \\cdot \\text{Beta}(\\theta; 6, 6)\\, d\\theta$
$= E[\\theta|y] = 0.5$</pre>

        <p>For a new set of 5 flips, the posterior predictive is a Beta-Binomial distribution, wider than a $\\text{Binomial}(5, 0.5)$ because it accounts for $\\theta$ uncertainty.</p>
        </div>

        <div class='success-box'>
        <p><strong>Takeaway:</strong> The posterior predictive is the principled way to make forecasts in Bayesian inference. It incorporates parameter uncertainty and is always more conservative (wider) than if we pretended $\\theta$ was known.</p>
        </div>
        """
    },
    {
        "title": "Model Comparison: Bayes Factors",
        "body": """
        <p><strong>Goal:</strong> Compare two statistical models (e.g., $M_1$ vs. $M_2$) using observed data.</p>

        <p><strong>Bayes Factor:</strong> Ratio of marginal likelihoods (evidence) under each model.</p>

        <p>$$BF_{12} = \\frac{p(y \\mid M_1)}{p(y \\mid M_2)}$$</p>

        <p><strong>Interpretation (standard scales):</strong></p>
        <ul>
        <li>$BF > 10$: Strong evidence for $M_1$</li>
        <li>$3 < BF < 10$: Moderate evidence for $M_1$</li>
        <li>$1 < BF < 3$: Weak evidence for $M_1$</li>
        <li>$BF \\approx 1$: Data do not discriminate</li>
        <li>$BF < 0.1$: Strong evidence for $M_2$</li>
        </ul>

        <p><strong>Advantages over null hypothesis testing (p-values):</strong></p>
        <ul>
        <li>Symmetrical: can favor either model, not just reject $H_0$</li>
        <li>Penalizes model complexity automatically (via the evidence)</li>
        <li>Natural interpretation as odds</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Simple Example: Model Selection</strong></p>
        <p>Data: $y \\sim \\text{Normal}$, 100 observations, sample mean = 5, SD = 1</p>

        <p><strong>$M_1$:</strong> $\\mu \\sim N(5, 1)$ [believes $\\mu \\approx 5$]</p>
        <p><strong>$M_2$:</strong> $\\mu \\sim N(0, 100)$ [uninformative, wide prior]</p>

        <p>The evidence $p(y|M_1)$ will be higher because $M_1$ concentrates prior probability near the observed data. Thus $BF_{12} > 1$, favoring $M_1$. ($M_1$ predicted the data better!)</p>
        </div>

        <div class='warning-box'>
        <p><strong>Caveat:</strong> Bayes Factors depend heavily on the prior. Different priors can lead to different BF values. Always report prior specification when using BF for model comparison.</p>
        </div>
        """
    }
]
