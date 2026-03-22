QUIZ = [
    {
        "question": "For a Markov chain with states {0, 1} and P = [[0.8, 0.2], [0.3, 0.7]], find the 2-step transition probability P(X₂=0 | X₀=1).",
        "answer": "P² = [[0.7, 0.3], [0.45, 0.55]]. P(X₂=0 | X₀=1) = (P²)_{1,0} = 0.45",
        "explanation": "Two-step transitions are given by P², computed via matrix multiplication."
    },
    {
        "question": "True or False: The steady-state distribution of an irreducible, aperiodic Markov chain is independent of the initial distribution.",
        "answer": "True",
        "explanation": "As n → ∞, π^(n) → π* regardless of π^(0). This is a key result of the ergodic theorem."
    },
    {
        "question": "For a Markov chain with steady-state π* = [0.4, 0.6], interpret π*₁.",
        "answer": "In the long run, approximately 40% of the time is spent in state 1 (and 60% in state 2).",
        "explanation": "The steady-state gives the long-run proportion of time in each state."
    },
    {
        "question": "What is the key property of a time-reversible Markov chain (detailed balance)?",
        "answer": "π*ᵢ P_{ij} = π*ⱼ P_{ji}. The flow from i to j equals the flow from j to i at steady-state.",
        "explanation": "Time-reversibility is important for MCMC and ensures stationary distributions."
    },
    {
        "question": "In the Gambler's Ruin problem with fair game (p=0.5), starting with $50 out of $100 total, what's the probability of reaching ruin?",
        "answer": "P(ruin) = (N+1-i)/(N+1) = 51/101 ≈ 0.505 (approximately 50.5% chance of ruin)",
        "explanation": "For a fair game, probability of ruin is linear in wealth: P(ruin) = (N+1-i)/(N+1) where i is current wealth, N is target."
    }
]
