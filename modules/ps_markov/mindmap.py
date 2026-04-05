MINDMAP = {
    "concepts": [
        {"title": "Markov Property", "points": [
            "Memoryless: future state depends only on present, not past",
            "\\(P(X_{n+1} | X_n, X_{n-1}, \\ldots) = P(X_{n+1} | X_n)\\)",
        ]},
        {"title": "Transition Matrix", "points": [
            "\\(P_{ij}\\) = probability of going from state \\(i\\) to state \\(j\\)",
            "Each row sums to 1 (stochastic matrix)",
            "\\(n\\)-step transitions: \\(P^{(n)} = P^n\\)",
        ]},
        {"title": "Stationary Distribution", "points": [
            "\\(\\boldsymbol{\\pi} P = \\boldsymbol{\\pi}\\) with \\(\\sum \\pi_i = 1\\)",
            "Long-run proportion of time in each state",
            "Exists and is unique for irreducible, aperiodic chains",
        ]},
        {"title": "Classification of States", "points": [
            "Absorbing: once entered, never left (\\(P_{ii} = 1\\))",
            "Transient vs recurrent: will the chain return?",
            "Irreducible: every state reachable from every other state",
            "Periodic: returns only at multiples of some period \\(d > 1\\)",
        ]},
    ],
    "formulas": [
        {"label": "n-step Transition", "expr": "\\(P^{(n)} = P^n\\)"},
        {"label": "Stationary Dist.", "expr": "\\(\\boldsymbol{\\pi} P = \\boldsymbol{\\pi}\\)"},
        {"label": "Absorption Prob.", "expr": "\\(\\mathbf{b} = N \\mathbf{r}\\) where \\(N = (I-Q)^{-1}\\)"},
    ],
    "tips": [
        "Draw the state transition diagram to visualise the chain",
        "Check irreducibility and aperiodicity before claiming a unique stationary distribution",
        "The fundamental matrix N = (I - Q)^{-1} gives expected visits to transient states",
    ],
}
