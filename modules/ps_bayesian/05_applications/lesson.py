TITLE = "Applications of Bayesian Inference"

SECTIONS = [
    {
        "title": "Medical Trials and Clinical Decision-Making",
        "body": """
        <p><strong>Application:</strong> Bayesian methods are revolutionizing clinical trial design.</p>

        <p><strong>Traditional frequentist trial:</strong> Fix sample size in advance based on power analysis, test hypothesis at end.</p>

        <p><strong>Bayesian adaptive trial:</strong></p>
        <ul>
        <li>Start with prior on treatment efficacy (from historical data, expert opinion)</li>
        <li>As patients enroll, update posterior of treatment effect sequentially</li>
        <li>Make mid-trial decisions: increase efficacy arm if promising, stop early if harmful, adapt allocation</li>
        <li>No multiple testing correction needed (posterior integrates over all analyses)</li>
        <li>Ethically superior: stop harmful treatments faster, allocate more patients to better treatments</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example: Drug Efficacy Trial</strong></p>
        <p>Prior belief: Drug improves outcomes with probability ~60% (based on preclinical data).</p>
        <p>Model: Bernoulli (responder/non-responder), Beta prior Beta(3, 2) centered at 0.6.</p>

        <p><strong>After 20 patients:</strong> 14 respond → Beta(3+14, 2+6) = Beta(17, 8)</p>
        <pre class='code-block'>Posterior mean: 17/25 = 0.68
P(efficacy > 0.5 | data) ≈ 0.97  (very confident drug works)</pre>

        <p><strong>Decision:</strong> Expand trial to more sites. Data strongly supports efficacy.</p>
        </div>

        <div class='concept-box'>
        <p><strong>Key advantage:</strong> Bayesian framework naturally handles sequential decisions. Prior knowledge informs the trial; early success can justify expansion without "p-hacking" concerns.</p>
        </div>
        """
    },
    {
        "title": "Machine Learning and Uncertainty Quantification",
        "body": """
        <p><strong>Traditional ML:</strong> Neural networks learn point estimates of weights. Hard to assess uncertainty.</p>

        <p><strong>Bayesian deep learning:</strong> Treat weights as random, learn posterior distribution over weights.</p>

        <pre class='code-block'>Prior p(w): Regularization (e.g., Gaussian prior on weights)
Likelihood p(y | x, w): Neural network output probabilities
Posterior p(w | data): Distribution of weights after training</pre>

        <p><strong>Benefits:</strong></p>
        <ul>
        <li><strong>Uncertainty quantification:</strong> Get credible intervals on predictions, not just point predictions</li>
        <li><strong>Out-of-distribution detection:</strong> Model is more uncertain for novel inputs</li>
        <li><strong>Principled regularization:</strong> Prior acts as regularization; no need to manually tune L1/L2 penalties</li>
        <li><strong>Active learning:</strong> Select most informative data points to label next</li>
        </ul>

        <p><strong>Computational methods:</strong> Dropout as approximate Bayesian inference, variational autoencoders, neural networks with probabilistic layers (TensorFlow Probability, PyMC).</p>

        <div class='worked-example'>
        <p><strong>Example: Predicting House Prices</strong></p>
        <p>Train a Bayesian neural network on 1000 houses with price, square footage, location.</p>

        <p>For a new house:</p>
        <pre class='code-block'>Standard NN: Price = $350,000
Bayesian NN: Price = $350,000 ± $45,000 (95% credible interval)</pre>

        <p>The credible interval reflects model uncertainty. For unfamiliar neighborhoods, the interval widens (more uncertain).</p>
        </div>
        """
    },
    {
        "title": "Finance and Belief Updating",
        "body": """
        <p><strong>Application:</strong> Bayesian methods model how rational agents update beliefs about asset returns.</p>

        <p><strong>Portfolio allocation:</strong> Prior belief on expected returns of stocks/bonds → posterior after observing recent returns → optimal portfolio allocation.</p>

        <p><strong>Risk management:</strong> Estimate value-at-risk (VaR) and expected shortfall.</p>
        <ul>
        <li>Prior: historical distribution of returns</li>
        <li>Data: recent returns (shifted by market shocks)</li>
        <li>Posterior: updated distribution of future returns</li>
        <li>Decision: adjust portfolio to control risk</li>
        </ul>

        <p><strong>Anomaly detection:</strong> Which trades are unusually extreme? Use posterior predictive to flag outliers.</p>

        <div class='worked-example'>
        <p><strong>Example: Stock Return Estimation</strong></p>
        <p>Stock ABC: Long-term mean return 8% (prior \(\\mu \sim N(0.08, 0.05^2)\)).</p>

        <p>Observe 50 daily returns, sample mean = 6%, sample SD = 12% (annualized).</p>

        <p><strong>Posterior:</strong> Updated belief balances historical (8%) with recent data (6%).</p>
        <pre class='code-block'>Posterior mean ≈ 7% (weighted average leaning toward historical)
Posterior SD: narrower (more confidence after observing data)</pre>

        <p>Use posterior mean for expected return; posterior SD for volatility; posterior distribution for portfolio optimization.</p>
        </div>
        """
    },
    {
        "title": "Hierarchical Models and Population-Level Inference",
        "body": """
        <p><strong>Problem:</strong> Many datasets have structure: students within schools, patients within hospitals, cities within countries.</p>

        <p><strong>Naive approach:</strong> Fit separate model for each group → many parameters, overfitting risk.</p>

        <p><strong>Bayesian hierarchical model:</strong> Share information across groups via a population-level distribution.</p>

        <pre class='code-block'>Student i in school j:
  \(y_{ij} \sim N(\\mu_j, \\sigma^2)\)           (individual variation)
  \(\\mu_j \sim N(\\mu_\\text{pop}, \tau^2)\)          (group means vary around population mean)
  \(\\mu_\\text{pop} \sim N(m, s^2)\)            (population prior)
  \(\tau^2 \sim \\text{Inverse-Gamma}(\ldots)\)      (between-group variation)</pre>

        <p><strong>Benefits:</strong></p>
        <ul>
        <li><strong>Shrinkage:</strong> Group estimates shrink toward population mean, reducing overfitting</li>
        <li><strong>Information sharing:</strong> Small groups borrow strength from large groups</li>
        <li><strong>Population inference:</strong> Naturally estimate both group-specific and population-level effects</li>
        <li><strong>Prediction:</strong> Posterior predictive for new group uses population distribution</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example: School Test Scores</strong></p>
        <p>3 schools with mean test scores: 75, 80, 70 (sample sizes 10, 100, 5 respectively).</p>

        <p>Naive estimate: Use sample means directly.</p>
        <p>Hierarchical Bayesian:</p>
        <pre class='code-block'>School 1 (n=10): Mean → 75 + shrinkage toward population
School 2 (n=100): Mean ≈ 80 (large n, low shrinkage)
School 3 (n=5): Mean → 70 + large shrinkage toward population</pre>

        <p>School 3's estimate moves toward population mean because it's based on few students. School 2 is confident. The amount of shrinkage is automatic and principled.</p>
        </div>

        <div class='success-box'>
        <p><strong>Key insight:</strong> Hierarchical Bayesian models formalize the intuition: "A small school's unusual score is probably due to random variation; trust the school less. A large school's score is more reliable."</p>
        </div>
        """
    },
    {
        "title": "Bayesian vs. Frequentist: When to Use Each",
        "body": """
        <p><strong>Bayesian inference excels when:</strong></p>
        <ul>
        <li>You have prior information (historical data, expert knowledge) worth incorporating</li>
        <li>You need to make sequential decisions (adaptive trials, online learning)</li>
        <li>You want direct probability statements ("What is \(P(\\theta > 0)\)?")</li>
        <li>You have hierarchical structure and need to share information across groups</li>
        <li>You need predictions with uncertainty quantification</li>
        <li>Small sample sizes (prior provides regularization)</li>
        </ul>

        <p><strong>Frequentist inference excels when:</strong></p>
        <ul>
        <li>You want to avoid subjective prior choices</li>
        <li>Large sample sizes (asymptotic theory applies, prior doesn't matter)</li>
        <li>You need p-values for hypothesis testing (though not always appropriate)</li>
        <li>Computational resources are limited and MCMC is slow</li>
        <li>Your field has established frequentist benchmarks (e.g., genetics GWAS)</li>
        </ul>

        <p><strong>Modern consensus:</strong> Both are valid statistical tools. In practice, many analyses use hybrid approaches: Bayesian priors for regularization, frequentist p-values for robustness, empirical Bayes to estimate prior from data.</p>

        <div class='concept-box'>
        <p><strong>Practical wisdom:</strong> "Think Bayesian, compute frequentist, report both if feasible." Bayesian thinking clarifies the problem; frequentist tools sometimes provide simpler computation or alignment with field standards.</p>
        </div>
        """
    }
]
