SECTIONS = [
    {
        "title": "Markov Chains and Transition Matrices",
        "body": """
        <p><strong>Markov Chain:</strong> A sequence of random variables X₀, X₁, X₂, ... where the future depends only on the present, not the past (memoryless property):</p>
        <pre class='code-block'>P(Xₙ₊₁ = j | Xₙ = i, Xₙ₋₁ = k, ...) = P(Xₙ₊₁ = j | Xₙ = i)</pre>

        <p><strong>Transition Probability:</strong> P_{ij} = P(Xₙ₊₁ = j | Xₙ = i) is the probability of moving from state i to state j.</p>

        <p><strong>Transition Matrix:</strong> P with entries P_{ij}. Properties:</p>
        <ul>
        <li>Each row sums to 1: Σⱼ P_{ij} = 1 (stochastic matrix)</li>
        <li>All entries non-negative: P_{ij} ≥ 0</li>
        </ul>

        <p><strong>State Distribution:</strong> After n steps, the probability distribution is:</p>
        <pre class='code-block'>π^(n) = π^(0) P^n</pre>

        <p>where π^(0) is the initial distribution and P^n is the n-step transition matrix.</p>

        <p><strong>State space:</strong> Can be finite (e.g., weather: sunny, rainy, cloudy) or infinite (e.g., number of customers in queue).</p>

        <div class='example-box'>
        <p><strong>Example: Weather Markov Chain</strong></p>
        <pre class='code-block'>States: S (sunny), R (rainy), C (cloudy)
Transition matrix P:
        S    R    C
    S [0.7  0.2  0.1]
    R [0.3  0.4  0.3]
    C [0.2  0.3  0.5]

If today is sunny (π = [1, 0, 0]), tomorrow's distribution:
π · P = [1, 0, 0] · P = [0.7, 0.2, 0.1]
(70% chance sunny, 20% rainy, 10% cloudy)</pre>
        </div>

        <p><strong>Classification of states:</strong></p>
        <ul>
        <li><strong>Transient:</strong> Eventually leaves and never returns (with positive probability)</li>
        <li><strong>Recurrent:</strong> Returns to the state infinitely often (with probability 1)</li>
        <li><strong>Absorbing:</strong> Once entered, never leaves (P_{ii} = 1)</li>
        <li><strong>Communicating:</strong> States that reach each other</li>
        <li><strong>Irreducible:</strong> All states communicate</li>
        </ul>
        """
    },
    {
        "title": "Steady-State Distribution and Limiting Behavior",
        "body": """
        <p><strong>Steady-State Distribution:</strong> The long-run distribution π* such that:</p>
        <pre class='code-block'>π* = π* P  (left eigenvector of P with eigenvalue 1)
or equivalently: π*ᵢ = Σⱼ π*ⱼ P_{ji}</pre>

        <p><strong>Existence and uniqueness:</strong> For an irreducible, aperiodic Markov chain, a unique steady-state π* exists, and:</p>
        <pre class='code-block'>lim_{n→∞} π^(n) = π*  (independent of initial distribution π^(0))</pre>

        <p><strong>Computing steady-state:</strong> Solve π*P = π* with Σᵢ π*ᵢ = 1. Equivalently, solve (P^T - I)π* = 0.</p>

        <p><strong>Ergodic theorem:</strong> For an ergodic chain (irreducible and aperiodic), the long-run proportion of time in state i converges to π*ᵢ.</p>

        <p><strong>First passage time:</strong> E[τⱼ | X₀ = i] is the expected time to reach state j starting from i. Can be computed by solving a system of linear equations.</p>

        <div class='example-box'>
        <p><strong>Example: Steady-state of weather</strong></p>
        <pre class='code-block'>π* P = π* with π* = [πₛ, πᵣ, πc] and Σ π*ᵢ = 1

Equations:
πₛ · 0.7 + πᵣ · 0.3 + πc · 0.2 = πₛ
πₛ · 0.2 + πᵣ · 0.4 + πc · 0.3 = πᵣ
πₛ · 0.1 + πᵣ · 0.3 + πc · 0.5 = πc
πₛ + πᵣ + πc = 1

Solving: π* ≈ [0.418, 0.285, 0.297]
Long-run: ~42% sunny, ~29% rainy, ~30% cloudy
(regardless of today's weather)</pre>
        </div>

        <p><strong>Time-reversibility:</strong> A chain is time-reversible if π*ᵢ P_{ij} = π*ⱼ P_{ji}. This property is important for detailed balance and MCMC sampling.</p>
        """
    },
    {
        "title": "Absorbing States and Fundamental Matrix",
        "body": """
        <p><strong>Absorbing Chain:</strong> A Markov chain with at least one absorbing state (P_{ii} = 1) and from every state, absorption occurs with probability 1.</p>

        <p><strong>Canonical form:</strong> Rearrange states so absorbing states come first:</p>
        <pre class='code-block'>P = [I  0]
    [R  Q]

where I = identity (absorbing states), Q = transient transitions, R = absorption probabilities</pre>

        <p><strong>Fundamental matrix:</strong> N = (I - Q)^{-1}</p>

        <p>N_{ij} = expected number of visits to transient state j starting from transient state i before absorption.</p>

        <p><strong>Absorption probabilities:</strong> B = N R gives the probability of being absorbed into each absorbing state, starting from each transient state.</p>

        <p><strong>Mean time to absorption:</strong> t = N · 1, where 1 is the vector of ones. t_i is the expected time to absorption starting from state i.</p>

        <div class='example-box'>
        <p><strong>Example: Gambler's Ruin</strong></p>
        <pre class='code-block'>States: 0 (ruin), 1, 2, ..., N (wealth), N+1 (rich)
States 0 and N+1 are absorbing.

From state i: move to i+1 with prob p, to i-1 with prob 1-p
Fair game: p = 0.5

Probability of reaching ruin starting with i dollars:
P(ruin | start with i) = (1 - (p/(1-p))^i) / (1 - (p/(1-p))^(N+1))

For p = 0.5 (fair): P(ruin) = (N+1-i)/(N+1)  (linear in wealth)
For p > 0.5: P(ruin) is nonlinear, favoring the player</pre>
        </div>

        <p><strong>Applications:</strong> Job search (absorbing state: employed), epidemic models (absorbing state: no more infected).</p>
        """
    },
    {
        "title": "Applications and Examples",
        "body": """
        <p><strong>Application 1: Page Rank (Google):</strong> Model the web as a Markov chain where states are pages and transitions are links. Steady-state distribution gives importance scores.</p>

        <p><strong>Application 2: Queueing Systems:</strong> Customers arriving and being served can be modeled as a Markov chain. State = number in queue. Steady-state gives average queue length and waiting time.</p>

        <p><strong>Application 3: Epidemiology:</strong> Model disease spread with states (Susceptible, Infected, Recovered). Transition probabilities depend on contact rates and recovery rates. Steady-state indicates endemic level.</p>

        <p><strong>Application 4: MCMC (Markov Chain Monte Carlo):</strong> Construct a Markov chain whose steady-state is the target posterior distribution. Gibbs sampling and Metropolis-Hastings are standard algorithms.</p>

        <p><strong>Application 5: Weather Prediction:</strong> Model weather transitions as Markov chains to forecast future conditions probabilistically.</p>

        <p><strong>Higher-order Markov chains:</strong> If future depends on the last k steps, construct a chain on k-tuples of states. This increases state space but maintains the Markov property.</p>

        <p><strong>Continuous-time Markov chains:</strong> Transitions occur at random times (Poisson process). Modeled via infinitesimal generator Q and semigroup e^{tQ}.</p>

        <div class='example-box'>
        <p><strong>Example: Simple Queue (M/M/1)</strong></p>
        <pre class='code-block'>Arrivals: Poisson(λ) per unit time
Service: Exponential(μ) per customer
Steady-state exists if λ < μ

ρ = λ/μ (utilization)
π_n = (1 - ρ) ρ^n  (probability of n customers in system)

Average queue length: L = ρ/(1-ρ)
Average wait time: W = 1/(μ - λ)</pre>

        <p><strong>Example: MCMC sampling for posterior</strong></p>
        <pre class='code-block'>Construct Markov chain with steady-state = posterior p(θ|y)
Metropolis-Hastings or Gibbs sampling:
- Transition kernel Q ensures detailed balance with posterior
- After burn-in, samples from the chain approximate the posterior
- Longer chain = better approximation</pre>
        </div>

        <p><strong>Mixing time:</strong> How fast the chain reaches steady-state. Relevant for MCMC convergence diagnostics (effective sample size, R̂).</p>

        <p><strong>Conclusion:</strong> Markov chains model sequential dependence naturally and are ubiquitous in applied probability, statistics, and machine learning. They provide a framework for understanding long-run behavior and computing expectations.</p>
        """
    }
]
