CHECKS = [
    {
        "q": "What is the Markov property? State it formally.",
        "a": "P(X_{n+1} = j | X_n = i, X_{n-1}, ..., X_0) = P(X_{n+1} = j | X_n = i). Future depends only on present, not past.",
        "hint": "Memoryless property: the chain forgets its history and only depends on the current state."
    },
    {
        "q": "Given transition matrix P, how do you compute the steady-state distribution π*?",
        "a": "Solve π* P = π* (equivalently, π* is a left eigenvector with eigenvalue 1) subject to Σ π*_i = 1.",
        "hint": "The steady-state satisfies the balance equation π* = π* P."
    },
    {
        "q": "What is an absorbing state? Give an example.",
        "a": "A state i where P_{ii} = 1 (once entered, never leaves). Example: state 'employed' in job search model.",
        "hint": "Absorbing states have transition probability 1 back to themselves."
    },
    {
        "q": "For a 2-state Markov chain with P = [[0.6, 0.4], [0.3, 0.7]], find the steady-state.",
        "a": "Solve π*[0.6, 0.4; 0.3, 0.7] = π* with π*_1 + π*_2 = 1. π*_1 · 0.6 + π*_2 · 0.3 = π*_1 gives 0.3π*_2 = 0.4π*_1, so π* = [0.6, 0.4].",
        "hint": "From balance: π*_1(0.6 - 1) + π*_2 · 0.3 = 0, and π*_1 + π*_2 = 1."
    },
    {
        "q": "What is the fundamental matrix N in an absorbing chain, and what does N_{ij} represent?",
        "a": "N = (I - Q)^{-1} where Q is the transient part of the transition matrix. N_{ij} = expected number of visits to transient state j before absorption, starting from state i.",
        "hint": "N encodes the expected behavior before absorption occurs."
    }
]
