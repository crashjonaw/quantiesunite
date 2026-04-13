TITLE = "Applications of Markov Chains"

SECTIONS = [
    {
        "title": "PageRank and Queueing Systems",
        "body": """
        <div class="worked-example">
        <p><strong>Application 1: Google PageRank</strong></p>
        <p>The web is modeled as a Markov chain where states are web pages and transitions are hyperlinks.</p>
        <pre class='code-block'>States: {Page1, Page2, ..., PageN}
Pᵢⱼ = probability of clicking a link from page i to page j
     = (# of links from i to j) / (total # of links from i)
     (with damping factor to handle dangling pages)</pre>
        <p>The steady-state distribution \(\\pi^*\) gives the PageRank scores—the long-run proportion of time a random surfer spends on each page. Pages with high \(\\pi^*_i\) are more "important".</p>
        </div>

        <div class="worked-example">
        <p><strong>Application 2: Queueing Systems (M/M/1)</strong></p>
        <p>Customers arrive (Poisson) and are served (Exponential). State = number of customers in the queue.</p>
        <pre class='code-block'>Arrivals: \(\\lambda\) per unit time
Service: \(\\mu\) per customer
\(\rho = \\lambda/\\mu\) (utilization)

Steady-state (if \(\rho < 1\)):
\(\\pi^*_n = (1 - \rho) \rho^n\)  (geometric distribution)

Average queue length: \(L = \rho/(1 - \rho)\)
Average wait time: \(W = 1/(\\mu - \\lambda)\)</pre>
        <p>This is used to dimension queues, staffing, and service capacity in banks, call centers, and manufacturing.</p>
        </div>

        <p><strong>Key Insight:</strong> When transitions are frequent and states are numerous, we often model using continuous-time Markov chains (CTMCs) with a generator matrix Q and semigroup e^{tQ}.</p>
        """
    },
    {
        "title": "Epidemiology and MCMC Sampling",
        "body": """
        <div class="worked-example">
        <p><strong>Application 3: Disease Modeling (SIR/SIS)</strong></p>
        <p>States represent the number of susceptible (S), infected (I), and recovered (R) individuals.</p>
        <pre class='code-block'>Transitions:
- S → I: new infections occur at rate \(\\beta SI/N\) (\(\\beta\) = contact rate)
- I → R: recovery occurs at rate \(\\gamma I\) (\(\\gamma\) = recovery rate)
- R → S: loss of immunity (SIS model)

Steady-state \(\\pi^*\) indicates the endemic level of disease.
If \(R_0 = \\beta/\\gamma > 1\), disease persists; else it dies out.</pre>
        <p>These models guide public health interventions (vaccination, quarantine) and predict long-term disease burden.</p>
        </div>

        <div class="worked-example">
        <p><strong>Application 4: Markov Chain Monte Carlo (MCMC)</strong></p>
        <p>Goal: Sample from a complex posterior distribution \(p(\\theta|y)\) (from Bayesian inference).</p>
        <pre class='code-block'>Construct a Markov chain whose steady-state = \(p(\\theta|y)\)

Metropolis-Hastings Algorithm:
1. Propose a move from \(\\theta\) to \(\\theta'\) with probability \(q(\\theta'|\\theta)\)
2. Accept with probability \(\min(1, p(\\theta'|y)q(\\theta|\\theta') / [p(\\theta|y)q(\\theta'|\\theta)])\)
3. Otherwise, stay at \(\\theta\)
4. Repeat many times (chain converges to posterior)

Gibbs Sampling: A special case where we update components sequentially
from their conditional distributions \(p(\\theta_j | \\theta_{-j}, y)\)

After burn-in, samples approximate the posterior distribution.</pre>
        <p>MCMC is ubiquitous in Bayesian statistics, enabling inference in complex models.</p>
        </div>
        """
    },
    {
        "title": "Advanced Topics and Extensions",
        "body": """
        <p><strong>Time-Reversibility and Detailed Balance:</strong></p>
        <p>A chain is time-reversible if \(\\pi^*_i P_{ij} = \\pi^*_j P_{ji}\) (detailed balance). This means the flow from \(i\) to \(j\) equals the flow from \(j\) to \(i\) at steady-state. Time-reversibility is crucial for MCMC (Metropolis-Hastings automatically ensures it).</p>

        <div class="worked-example">
        <p><strong>Example: Time-Reversibility Check</strong></p>
        <pre class='code-block'>\(P = \\begin{bmatrix} 0.6 & 0.4 \\ 0.3 & 0.7 \\end{bmatrix}\)    \(\\pi^* = [3/7,\ 4/7]\)

Check: \(\\pi^*_1 P_{12} = 3/7 \\cdot 0.4 = 12/49\)
       \(\\pi^*_2 P_{21} = 4/7 \\cdot 0.3 = 12/49\)
They're equal! Chain is time-reversible.</pre>
        </div>

        <p><strong>Higher-Order Markov Chains:</strong> If the next state depends on the last k states, construct a chain on k-tuples. This increases state space but maintains the Markov property.</p>

        <p><strong>Continuous-Time Markov Chains (CTMCs):</strong> Transitions occur at random (exponential) times, not discrete steps. Governed by a generator matrix Q. Applications: molecular dynamics, queueing, epidemic models.</p>

        <p><strong>Mixing Time:</strong> How many steps until the chain is "close" to steady-state? Important for MCMC convergence diagnostics (effective sample size, R̂ statistic).</p>

        <p><strong>Reversibility and Bounds:</strong> Mixing time depends on the spectral gap (\(1 - \\lambda_2\), where \(\\lambda_2\) is the second-largest eigenvalue). Faster mixing = faster convergence to steady-state.</p>

        <div class="success-box">
        <p><strong>Conclusion:</strong> Markov chains provide a powerful, general framework for modeling sequential phenomena. They appear in nearly every scientific and engineering discipline, from web analytics to drug discovery to climate modeling. Understanding the theory (Markov property, steady-states, absorption) enables building effective models and algorithms.</p>
        </div>
        """
    }
]
