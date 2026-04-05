TITLE = "Markov Property and Chains"

SECTIONS = [
    {
        "title": "The Markov Property",
        "body": """
        <div class="concept-box">
        <p><strong>Markov Chain:</strong> A sequence of random variables <code>X₀, X₁, X₂, ...</code> where the future depends only on the present state, not on how we arrived there (memoryless property).</p>
        </div>

        <p><strong>Formal Definition:</strong> A stochastic process has the Markov property if:</p>
        <pre class='code-block'>P(Xₙ₊₁ = j | Xₙ = i, Xₙ₋₁ = k, ..., X₀) = P(Xₙ₊₁ = j | Xₙ = i)</pre>

        <p>This equation states that the probability of the next state depends only on the current state, not on the entire history.</p>

        <div class="worked-example">
        <p><strong>Why Markov?</strong> Consider weather prediction:</p>
        <ul>
        <li><strong>Non-Markov approach:</strong> "Tomorrow's weather depends on today's weather AND whether it rained yesterday."</li>
        <li><strong>Markov approach:</strong> "Tomorrow's weather depends only on whether it's sunny, rainy, or cloudy today."</li>
        </ul>
        <p>We <em>condition</em> on today's state, which captures relevant information from the past.</p>
        </div>

        <p><strong>Key Insight:</strong> The Markov property means we can "forget" the past. This drastically simplifies modeling and computation.</p>
        """
    },
    {
        "title": "State Space and Discrete-Time Markov Chains",
        "body": """
        <p><strong>State Space:</strong> The set of all possible values the process can take. Markov chains can have:</p>
        <ul>
        <li><strong>Finite state space:</strong> e.g., {Sunny, Rainy, Cloudy} (3 states)</li>
        <li><strong>Countably infinite:</strong> e.g., {0, 1, 2, ...} (queue length)</li>
        <li><strong>Continuous:</strong> e.g., temperature ∈ [−∞, ∞]</li>
        </ul>

        <p><strong>Discrete-Time Markov Chains (DTMCs):</strong> Transitions occur at discrete time steps <code>n = 0, 1, 2, ...</code></p>

        <div class="worked-example">
        <p><strong>Example: A Simple 3-State Chain</strong></p>
        <p><strong>States:</strong> {S (Sunny), R (Rainy), C (Cloudy)}</p>
        <p><strong>Sample Path:</strong> Today is Sunny (S) → Tomorrow Cloudy (C) → Next day Sunny (S) → Sunny → Rainy → ...</p>
        <p>The transition S → C → S depends only on the current state at each step.</p>
        </div>

        <p><strong>Transition Probability:</strong> The probability of moving from state <code>i</code> to state <code>j</code> in one step is denoted:</p>
        <pre class='code-block'>P_{ij} = P(Xₙ₊₁ = j | Xₙ = i)</pre>

        <p>These probabilities are assumed to be <strong>time-homogeneous</strong> (constant over time). This means transitioning from state i to j always has the same probability, regardless of when the transition occurs.</p>
        """
    },
    {
        "title": "Examples and Applications",
        "body": """
        <div class="concept-box">
        <p><strong>A Markov chain models sequences where the next event depends only on the current state.</strong></p>
        </div>

        <div class="worked-example">
        <p><strong>Example 1: Weather (Finite Chain)</strong></p>
        <pre class='code-block'>States: S, R, C
Transition Probabilities:
- P(S tomorrow | S today) = 0.7
- P(R tomorrow | S today) = 0.2
- P(C tomorrow | S today) = 0.1
Similarly for other states...</pre>
        <p>This is a Markov chain: tomorrow's weather depends only on today's weather.</p>
        </div>

        <div class="worked-example">
        <p><strong>Example 2: Queue Length (Countably Infinite)</strong></p>
        <pre class='code-block'>States: {0, 1, 2, 3, ...} (number of customers in queue)
Transition: Depends on arrivals (Poisson) and service times (Exponential)
- With prob λ·Δt, a customer arrives
- With prob μ·Δt, a customer is served</pre>
        <p>The queue length is Markov: future length depends only on current length.</p>
        </div>

        <p><strong>Non-Markov Example:</strong> "An age-dependent process" where transition probabilities depend on how long we've been in the current state. (Not covered in basic Markov chains.)</p>

        <div class="success-box">
        <p><strong>Key Takeaway:</strong> When modeling real systems, the Markov assumption is valid if we condition on all <em>relevant</em> state information from the past.</p>
        </div>
        """
    }
]
